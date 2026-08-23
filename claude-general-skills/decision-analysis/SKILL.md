---
name: decision-analysis
description: Structured method for making decisions and weighing tradeoffs. Use whenever the user asks "should I…", "which option…", "help me decide," "pros and cons," or describes being torn between alternatives — for business, technical, or personal-professional choices, even when they only seem to want validation of a choice already made.
---

# Decision Analysis

Match the depth of analysis to the reversibility of the decision. Most decisions deserve less analysis; a few deserve much more.

## Step 0: Classify

- **Reversible + cheap** → decide in minutes, pick the option that is easiest to undo, move on. Do not run the full protocol.
- **Hard to reverse or expensive** → run the protocol below.

## The protocol

1. **Frame it in one sentence**, with a deadline. "Deciding X by DATE." No deadline means it is not a decision yet, it is a worry.
2. **List real options** — always include "do nothing" and "decide later at a defined trigger." Fewer than three options usually means the framing is too narrow.
3. **Criteria, max five, weighted.** More than five criteria means none of them matter.
4. **Find the cheapest test** that shrinks the biggest unknown before committing (a call, a prototype, a week's trial). A $100 test beats $10,000 of analysis.
5. **Pre-mortem**: "It is a year later and this choice failed — what went wrong?" Write the top two failure modes and whether they are survivable.
6. **Recommend explicitly.** State the pick, the strongest argument *against* it, and why it wins anyway. A recommendation without its best counterargument is advocacy, not analysis.

## Decision log (persistent memory)

Append every protocol-level decision to `decisions.log` in this skill's folder — five lines: decision, date, options considered, reasoning, expected outcome + review date. Before analyzing a new decision, scan the log for similar past ones and check how expectations matched reality. Comparing expected vs. actual is how judgment improves, and the log is what lets future sessions inherit it.

## Anti-patterns

- Analysis as procrastination: re-deriving the same comparison a third time.
- Criteria invented to justify the emotionally pre-chosen option (the pre-mortem usually exposes this).
- Treating a reversible decision as irreversible — the most expensive habit in this file.
