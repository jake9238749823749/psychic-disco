#!/usr/bin/env python3
"""Compute mechanical AMM friction for a small Solana meme-token position.

This is deliberately an execution-cost calculator, not a PnL forecaster. It makes no
claim about price direction, wallet quality, graduation probability, or alpha. Its output
is useful for rejecting a trade whose theoretical edge is smaller than mechanical friction.

The model is a two-reserve constant-product pool with a balanced USD value at entry. It
applies the stated swap fee on entry and exit, calculates endogenous pool impact exactly,
and then adds configurable off-quote slippage, latency drift, network cost, and a Jito tip.

Usage:
  python m100/scripts/execution_stress.py m100/data/execution_stress_inputs.json \
      --out m100/output/execution_stress.json
"""

from __future__ import annotations

import argparse
import itertools
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Scenario:
    position_usd: float
    total_pool_liquidity_usd: float
    pool_fee_bps: float
    fee_multiplier: float
    slippage_multiplier: float
    delay_seconds: int
    adverse_latency_bps: float
    network_cost_usd: float
    jito_tip_usd: float


def round_trip(s: Scenario) -> dict[str, float]:
    """Execute a buy and immediate sell in a balanced constant-product pool.

    Quote reserve and base reserve are normalized to half total liquidity and $1/token.
    Price movement is intentionally modeled separately as an *adverse latency* deduction;
    that parameter is a stress input, not a measured forecast.
    """
    reserve_quote = s.total_pool_liquidity_usd / 2.0
    reserve_base = s.total_pool_liquidity_usd / 2.0
    fee = s.pool_fee_bps * s.fee_multiplier / 10_000.0

    # Entry decomposition at the displayed pre-trade mid price. The no-fee counterfactual
    # isolates constant-product price impact from the stated swap fee.
    tokens_without_fee = reserve_base * s.position_usd / (reserve_quote + s.position_usd)
    entry_price_impact = s.position_usd - tokens_without_fee
    effective_in = s.position_usd * (1.0 - fee)
    tokens_bought = reserve_base * effective_in / (reserve_quote + effective_in)
    entry_fee_effect = tokens_without_fee - tokens_bought
    entry_mark_to_mid_loss = s.position_usd - tokens_bought

    # Fees are modeled as removed from the active reserves. That is intentionally conservative
    # for a trader and matches a protocol/creator-fee pool better than assuming all fees deepen LP.
    reserve_quote_after_buy = reserve_quote + effective_in
    reserve_base_after_buy = reserve_base - tokens_bought
    post_buy_mid = reserve_quote_after_buy / reserve_base_after_buy
    pre_exit_mid_value = tokens_bought * post_buy_mid
    quote_out_without_exit_fee = reserve_quote_after_buy * tokens_bought / (
        reserve_base_after_buy + tokens_bought
    )
    exit_price_impact = pre_exit_mid_value - quote_out_without_exit_fee
    effective_token_in = tokens_bought * (1.0 - fee)
    quote_out = reserve_quote_after_buy * effective_token_in / (
        reserve_base_after_buy + effective_token_in
    )
    exit_fee_effect = quote_out_without_exit_fee - quote_out

    # An immediate reversal partially unwinds its own price impact, so its exact round-trip
    # loss is mostly fee. The multiplier below is a *separate pessimistic overlay* for route
    # uncertainty / changed pool state when the intended exit happens later, not an assertion
    # that the immediate reversal has this extra loss.
    immediate_round_trip_loss = s.position_usd - quote_out
    single_leg_impact_reference = entry_price_impact + exit_price_impact
    extra_unquoted_slippage = single_leg_impact_reference * (s.slippage_multiplier - 1.0)
    latency_cost = s.position_usd * s.adverse_latency_bps / 10_000.0

    net_proceeds = (
        quote_out
        - extra_unquoted_slippage
        - latency_cost
        - s.network_cost_usd * 2.0
        - s.jito_tip_usd * 2.0
    )
    net_loss = s.position_usd - net_proceeds
    return {
        "entry_mid_mark_loss_usd": entry_mark_to_mid_loss,
        "entry_price_impact_vs_mid_usd": entry_price_impact,
        "entry_pool_fee_effect_usd": entry_fee_effect,
        "exit_price_impact_vs_post_buy_mid_usd": exit_price_impact,
        "exit_pool_fee_effect_usd": exit_fee_effect,
        "immediate_round_trip_loss_before_addons_usd": immediate_round_trip_loss,
        "single_leg_impact_reference_usd": single_leg_impact_reference,
        "extra_unquoted_slippage_overlay_usd": extra_unquoted_slippage,
        "latency_cost_usd": latency_cost,
        "network_and_tip_round_trip_usd": 2.0 * (s.network_cost_usd + s.jito_tip_usd),
        "net_proceeds_under_stress_usd": net_proceeds,
        "net_round_trip_loss_under_stress_usd": net_loss,
        "net_round_trip_loss_under_stress_pct": 100.0 * net_loss / s.position_usd,
        "minimum_gross_move_to_break_even_under_stress_pct": 100.0 * net_loss / max(net_proceeds, 1e-12),
    }


def build_scenarios(config: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    base_latency_bps_per_second = float(config["latency_stress_bps_per_second"])
    for (
        position,
        liquidity,
        fee_bps,
        fee_mult,
        slippage_mult,
        seconds,
        jito_tip,
    ) in itertools.product(
        config["position_usd"],
        config["total_pool_liquidity_usd"],
        config["pool_fee_bps"],
        config["fee_multipliers"],
        config["slippage_multipliers"],
        config["delay_seconds"],
        config["jito_tip_usd"],
    ):
        scenario = Scenario(
            position_usd=float(position),
            total_pool_liquidity_usd=float(liquidity),
            pool_fee_bps=float(fee_bps),
            fee_multiplier=float(fee_mult),
            slippage_multiplier=float(slippage_mult),
            delay_seconds=int(seconds),
            adverse_latency_bps=float(seconds) * base_latency_bps_per_second,
            network_cost_usd=float(config["network_cost_usd_per_transaction"]),
            jito_tip_usd=float(jito_tip),
        )
        mechanics = round_trip(scenario)
        bankroll = float(config["account_bankroll_usd"])
        rows.append(
            {
                **asdict(scenario),
                **mechanics,
                "position_pct_of_100_account": 100.0 * scenario.position_usd / bankroll,
                "stress_loss_pct_of_100_account": 100.0
                * mechanics["net_round_trip_loss_under_stress_usd"]
                / bankroll,
            }
        )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    config = json.loads(args.config.read_text())
    rows = build_scenarios(config)
    result = {
        "model": {
            "type": "balanced constant-product immediate round trip",
            "does_not_model": [
                "price alpha", "market depth outside one pool", "failed transactions",
                "route changes", "sandwiching", "unexitability", "rug probability", "wallet linkage",
            ],
            "latency_note": (
                "adverse_latency_bps is a transparent sensitivity assumption based on configured "
                "bps-per-second; it is not a measured return forecast. The slippage multiplier is "
                "also an explicit pessimistic overlay based on one-leg AMM impact, because an "
                "immediate reversal partially unwinds its own price impact."
            ),
        },
        "config": config,
        "scenarios": rows,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"written": str(args.out), "scenarios": len(rows)}, indent=2))


if __name__ == "__main__":
    main()
