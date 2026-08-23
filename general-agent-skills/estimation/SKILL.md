---
name: estimation
description: Produce defensible estimates of time, effort, cost, or size — and correct for the optimism that makes them wrong. Use whenever the user asks "how long will this take," "how much will it cost," "how big is this," "can we hit this deadline," or wants a timeline, budget, or scope estimate, for code, projects, research, or business work. Trigger even when the user wants "just a rough number" — rough numbers are where the planning fallacy does its damage.
---

# Estimation

A confident single number is the least useful estimate. The default failure is optimism — the planning fallacy is that people (and models) estimate as if nothing will go wrong, when something always does. Correct for it explicitly.

## Method

1. **Decompose.** Break the whole into parts small enough to reason about (rough rule: nothing over a day of work, or 20% of the total, stays a single line). The sum of estimated parts beats one estimate of the whole, because it forces the hidden pieces into view.
2. **Reference class first, then adjust.** Ask "how long did similar things actually take?" before "how long should this take?" The outside view (comparable past cases) beats the inside view (reasoning from this case's details), which is almost always too optimistic.
3. **Give a range, not a point.** State low / likely / high. If forced to one number, give the high one — estimates skew optimistic far more often than pessimistic.
4. **Surface the assumptions the estimate rests on.** "Assumes the API is documented; assumes no data migration." Each assumption is a place the number breaks. The estimate is only as good as its shakiest assumption.
5. **Add a contingency for the unknown**, and label it. Novel/unclear work needs more; routine work needs less. Naming the buffer is honest; hiding it in inflated line items is not.

## Calibration rules

- **Round to your real precision.** "Three to five days" is honest; "4.25 days" pretends to knowledge you don't have.
- **Separate estimate from target.** What it will take and what someone wants it to take are different numbers. State the estimate; then, if there's a deadline, say what fits inside it and what would have to be cut.
- **Distinguish effort from duration.** Two days of work is not two calendar days once waiting, dependencies, and other commitments intrude.
- **The unknowns dominate.** Most overruns come from work nobody listed, not from listed work taking longer. Budget for the un-listed.

## Output format

- Range (low / likely / high) with the unit.
- The decomposition that produced it.
- Key assumptions, each flagged as a risk to the number.
- If a deadline exists: does the estimate fit, and if not, the smallest cut that makes it fit.

## Gotchas

- The first number that comes to mind is the inside-view guess — anchor to reference class *before* saying it, or it contaminates everything after.
- "Rough estimate" is not license to skip decomposition; it's where skipping it hurts most, because there's no detail to catch the omission.
- An estimate with no stated assumptions can't be checked, defended, or safely relied on. No naked numbers.
