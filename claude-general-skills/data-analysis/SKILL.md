---
name: data-analysis
description: Sanity-check protocol for analyzing any data — spreadsheets, CSVs, metrics, survey results, analytics exports. Use whenever the user shares data or numbers and asks what they mean, wants trends, comparisons, or charts, or makes a decision that leans on a statistic — even for "quick looks," which is where the wrong conclusions usually happen.
---

# Data Analysis

Most wrong conclusions come from dirty inputs and missing denominators, not bad math. Check the data before analyzing the data.

## Before any analysis (report findings first)

- Row count — does it match expectations?
- Duplicates — on the key that should be unique.
- Date range — actual min/max vs. assumed; timezone consistency.
- Missing values — how many, and are they missing at random or systematically?
- Units — currency, thousands vs. millions, percent vs. proportion.

Report anomalies *before* the analysis. An interesting finding in unchecked data is a rumor.

## Rules of interpretation

- **State the question the analysis answers.** No question → no analysis, just a data dump.
- **Denominators always.** Raw counts mislead; rates and per-X comparisons inform. "500 signups" means nothing without "out of how many visitors, vs. what baseline."
- **Compare like with like**: same timeframe lengths, same cohort definitions, same units. Most "growth" artifacts are mismatched windows.
- **Distrust on sight**: n < 30, survivorship-shaped samples (only current customers, only completed deals), aggregate trends that could hide opposing subgroup trends, and any metric that improved right after its definition changed.
- **Precision matches confidence.** Dirty data does not earn four significant figures. Round to what is defensible.
- **Correlation is labeled as such.** Causal language ("drove," "caused," "because of") requires a mechanism or an experiment, not a scatter plot.

## Output rules

- Every chart or table gets one "so what" sentence. No naked exhibits.
- Show the work: the formula, query, or steps used, so the result is reproducible.
- End with: what this data *cannot* tell us (the honest limits section).
