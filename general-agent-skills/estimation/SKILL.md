---
name: estimation
description: Produce defensible estimates of time, effort, cost, or size — and correct for the optimism that makes them wrong. Use whenever the user asks "how long will this take," "how much will it cost," "how big is this," "can we hit this deadline," or wants a timeline, budget, or scope estimate, for code, projects, research, or business work. Trigger even when the user wants "just a rough number" — rough numbers are where the planning fallacy does its damage.
---

# Estimation

A confident single number is the least useful estimate. The default failure is optimism — the planning fallacy is that people (and models) estimate as if nothing will go wrong, when something always does. Correct for it explicitly.

## Method

1. **Decompose.** Break the whole into parts small enough to reason about (rough rule: nothing over a day of work, or 20% of the total, stays a single line). The sum of estimated parts beats one estimate of the whole, because it forces the hidden pieces into view.
2. **Reference class first, then adjust.** Ask "how long did similar things actually take?" before "how long should this take?" The outside view (comparable past cases) beats the inside view (reasoning from this case's details), which is almost always too optimistic. **The reference class is `durations.log`** in this skill's folder: real past estimates with real actuals, read newest-first, filtered to similar task categories. **Fewer than 3 similar entries: say so explicitly, label the estimate `uncalibrated`, and widen the range by 50%** — that widening is a bootstrap rule with an expiration condition, not a license. Once 3+ entries exist, the log replaces the guess.
3. **Give a range, not a point.** State low / likely / high. If forced to one number, give the high one — estimates skew optimistic far more often than pessimistic.
4. **Surface the assumptions the estimate rests on.** "Assumes the API is documented; assumes no data migration." Each assumption is a place the number breaks. The estimate is only as good as its shakiest assumption.
5. **Add a contingency for the unknown**, and label it. Novel/unclear work needs more; routine work needs less. Naming the buffer is honest; hiding it in inflated line items is not.

## Calibration rules

- **Round to your real precision.** "Three to five days" is honest; "4.25 days" pretends to knowledge you don't have.
- **Separate estimate from target.** What it will take and what someone wants it to take are different numbers. State the estimate; then, if there's a deadline, say what fits inside it and what would have to be cut.
- **Distinguish effort from duration.** Two days of work is not two calendar days once waiting, dependencies, and other commitments intrude.
- **The unknowns dominate.** Most overruns come from work nobody listed, not from listed work taking longer. Budget for the un-listed.

## Durations log — the reference class, self-filling

Every estimate you produce is a deposit; every actual you record is interest. This log is what makes reference-class forecasting real instead of rhetorical.

- **Entry format:** `date | task category | estimated range | actual | error ratio`
  `2026-09-26 | api-integration | 2–4 days | 6 days | 1.5x over`
  (error ratio = actual ÷ likely estimate; `1.5x over` means the work took 1.5× the likely estimate. Category doubles as the topic tag per `memory-protocol`.)
- **Mandatory deposit.** After ANY task you estimated, append the actual outcome — no exceptions. Even when it was right, even when it was embarrassing, even when the session is ending. An estimate without a recorded actual is a prediction that taught nothing.
- **Reading it.** For a new estimate, scan newest-first for the same task category. 3+ similar entries is a calibrated reference class: report the median error ratio as your adjustment factor.
- **Cold start.** The first 3 estimates in any category are explicitly labeled `uncalibrated`. The label is the honesty mechanism while the data accumulates.
- Storage format, tagging, and retention follow `memory-protocol` (`<date> | [tags] | body`, tombstone retractions, 90-day expiry).

## Output format

- Range (low / likely / high) with the unit.
- The decomposition that produced it.
- Key assumptions, each flagged as a risk to the number.
- If a deadline exists: does the estimate fit, and if not, the smallest cut that makes it fit.

## Gotchas

- The first number that comes to mind is the inside-view guess — anchor to reference class *before* saying it, or it contaminates everything after.
- "Rough estimate" is not license to skip decomposition; it's where skipping it hurts most, because there's no detail to catch the omission.
- An estimate with no stated assumptions can't be checked, defended, or safely relied on. No naked numbers.
- A reference class with no cited source is a guess wearing a lab coat. "Similar projects take two weeks" without a source is the inside view with better branding.
- An estimate logged without its actual is a prediction that taught nothing. The deposit after the work is what turns today's guess into tomorrow's reference class — skip it and the log stays a bootstrap forever.
