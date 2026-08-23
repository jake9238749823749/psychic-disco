#!/usr/bin/env python3
"""Audit a Pump.fun launch dataset without turning a graduation label into a trade claim.

This uses only the Python standard library after a parquet reader is available. It first
tries pyarrow, then the zero-dependency `pqlite` reader. It intentionally does NOT fit a
model: if a dataset lacks an exact launch timestamp, it cannot support the required
chronological train/validation/test protocol.

Example used for the M100 first-session audit:
  git clone --depth=1 https://github.com/Vriti29/pqlite /tmp/pqlite
  git clone --depth=1 https://github.com/tomdelcarlo-lgtm/pumpfun-graduation-prediction /tmp/pump-study
  PYTHONPATH=/tmp/pqlite/src python m100/scripts/audit_reference_dataset.py \
    /tmp/pump-study/data/pumpfun_training_dataset.parquet \
    --out m100/output/reference_dataset_audit.json

The input dataset is deliberately not committed here. See the report for source, period,
selection limitations, and why its random split / 30-minute observation window cannot
validate a live strategy.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import statistics
from pathlib import Path
from typing import Any


LABEL = "graduated"
IDENTIFIER = "mint"
EXCLUDED = {LABEL, IDENTIFIER, "launch_month"}
FOCUS_FEATURES = (
    "volume_first_30min",
    "n_trades_30min",
    "unique_buyers_30min",
    "max_single_buy_30min",
    "top1_wallet_pct_30min",
    "buy_sell_ratio_30min",
)


def load_columns(path: Path) -> dict[str, list[Any]]:
    """Load a flat parquet file while keeping this audit dependency-light."""
    try:
        import pyarrow.parquet as pq  # type: ignore

        table = pq.read_table(path)
        return {name: table[name].to_pylist() for name in table.column_names}
    except ModuleNotFoundError:
        pass

    try:
        from pqlite import ParquetFile  # type: ignore
    except ModuleNotFoundError as exc:
        raise SystemExit(
            "No parquet reader found. Install pyarrow or put Vriti29/pqlite/src on PYTHONPATH. "
            "The M100 report documents the exact pqlite command used."
        ) from exc

    parquet = ParquetFile(str(path))
    return {name: parquet.column(name) for name in parquet.column_names()}


def percentile(values: list[float], probability: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    index = (len(ordered) - 1) * probability
    low = int(index)
    high = min(low + 1, len(ordered) - 1)
    return ordered[low] + (ordered[high] - ordered[low]) * (index - low)


def describe(values: list[float]) -> dict[str, float | int | None]:
    return {
        "n": len(values),
        "mean": sum(values) / len(values) if values else None,
        "median": percentile(values, 0.50),
        "p25": percentile(values, 0.25),
        "p75": percentile(values, 0.75),
        "p90": percentile(values, 0.90),
        "p99": percentile(values, 0.99),
    }


def wilson_95(successes: int, trials: int) -> list[float | None]:
    """Wilson interval is preferable to a normal interval for rare positives."""
    if trials == 0:
        return [None, None]
    z = 1.96
    proportion = successes / trials
    denominator = 1 + z * z / trials
    center = (proportion + z * z / (2 * trials)) / denominator
    radius = z / denominator * math.sqrt(
        proportion * (1 - proportion) / trials + z * z / (4 * trials * trials)
    )
    return [center - radius, center + radius]


def event_rate(labels: list[int], eligible: list[int]) -> dict[str, Any]:
    positives = sum(labels[index] for index in eligible)
    count = len(eligible)
    return {
        "n": count,
        "graduated": positives,
        "rate": positives / count if count else None,
        "wilson95": wilson_95(positives, count),
    }


def source_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def audit(path: Path) -> dict[str, Any]:
    data = load_columns(path)
    columns = list(data)
    if LABEL not in data:
        raise SystemExit(f"Expected a {LABEL!r} label. Found: {columns}")

    labels = [int(value) for value in data[LABEL]]
    row_count = len(labels)
    if any(len(values) != row_count for values in data.values()):
        raise SystemExit("Column lengths do not match.")

    feature_names = [column for column in columns if column not in EXCLUDED]
    by_label: dict[str, dict[str, Any]] = {"0": {}, "1": {}}
    for feature in feature_names:
        for label in (0, 1):
            values = [
                float(value)
                for value, actual in zip(data[feature], labels)
                if actual == label and value is not None
            ]
            by_label[str(label)][feature] = describe(values)

    deciles: dict[str, Any] = {}
    for feature in FOCUS_FEATURES:
        if feature not in data:
            continue
        values = [float(value) for value in data[feature]]
        cutoff = percentile(values, 0.90)
        eligible = [index for index, value in enumerate(values) if value >= cutoff]
        deciles[feature] = {"cutoff": cutoff, **event_rate(labels, eligible)}

    threshold_specs = (
        ("volume_first_30min", ">=", 10_000.0),
        ("max_single_buy_30min", ">=", 10_000.0),
        ("unique_buyers_30min", ">=", 100.0),
        ("n_trades_30min", ">=", 400.0),
        ("top1_wallet_pct_30min", "<=", 0.25),
    )
    thresholds: dict[str, Any] = {}
    for feature, operator, threshold in threshold_specs:
        if feature not in data:
            continue
        values = [float(value) for value in data[feature]]
        if operator == ">=":
            eligible = [index for index, value in enumerate(values) if value >= threshold]
        else:
            eligible = [index for index, value in enumerate(values) if value <= threshold]
        thresholds[f"{feature}_{operator}_{threshold:g}"] = {
            "feature": feature,
            "operator": operator,
            "threshold": threshold,
            **event_rate(labels, eligible),
        }

    timestamp_fields = [
        column
        for column in columns
        if any(term in column.lower() for term in ("timestamp", "created_at", "time", "slot", "date"))
    ]
    has_exact_ordering = any(
        term in field.lower()
        for field in timestamp_fields
        for term in ("timestamp", "created_at", "slot")
    )

    positives = sum(labels)
    return {
        "source": {
            "path": str(path),
            "sha256": source_sha256(path),
            "columns": columns,
        },
        "universe": {
            "rows": row_count,
            "positives": positives,
            "base_rate": positives / row_count,
            "base_rate_wilson95": wilson_95(positives, row_count),
        },
        "descriptive_by_label": by_label,
        "top_decile_graduation_rates": deciles,
        "illustrative_threshold_graduation_rates": thresholds,
        "point_in_time_audit": {
            "timestamp_like_fields": timestamp_fields,
            "has_exact_ordering_field": has_exact_ordering,
            "temporal_split_permitted": has_exact_ordering,
            "warning": (
                "Graduation association is not a tradeable-return label. A dataset without exact "
                "creation order cannot validate a chronological split. A full first-30-minute feature "
                "window also cannot be used for a pre-graduation decision if the coin may graduate "
                "inside that window; verify lifecycle timing before treating model scores as signals."
            ),
        },
        "not_estimated": [
            "post-cost tradable winner labels",
            "MFE/MAE barriers",
            "wallet independence",
            "deployer linkage",
            "slippage or failed-transaction costs",
            "out-of-time calibrated probabilities",
            "strategy expectancy or ruin probability",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("parquet", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    result = audit(args.parquet)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"written": str(args.out), "rows": result["universe"]["rows"]}, indent=2))


if __name__ == "__main__":
    main()
