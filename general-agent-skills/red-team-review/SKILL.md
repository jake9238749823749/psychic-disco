---
name: red-team-review
description: Adversarially attack a plan, document, analysis, or piece of code before it ships. Use whenever the user says "poke holes," "stress test," "what am I missing," "grill me," "devil's advocate," or "is this ready" — and as the final pass on anything high-stakes about to be sent, launched, published, or merged. Trigger even when the user only asks for a "quick look" at something that clearly matters.
---

# Red-Team Review

Assume the work is wrong somewhere; the job is to find where. Praise is out of scope until the attack is finished.

**When to reach for this vs. output-standards:** `output-standards` is the routine done-checklist that runs on everything. This skill is the *escalation* — the adversarial attack you run on top, only when being wrong is genuinely expensive. Checklist always; red-team when stakes justify it.

## Protocol

1. **Restate the claim.** One sentence: what does this work promise or assert? Attacks aim at that sentence.
2. **Attack from distinct angles** (pick the relevant ones, minimum three):
  - *Factual* — which claims would a domain expert verify first? Verify those.
  - *Logical* — does the conclusion follow? What unstated assumption carries the load?
  - *Hostile reader* — read as the competitor, the lawyer, the annoyed customer, the person with the least goodwill. What do they seize on?
  - *Failure modes* — how does this break in practice? Wrong input, bad timing, scale, the step a tired person skips.
  - *Incentives* — who is worse off if this succeeds, and what do they do about it?
3. **Rank findings**: `[fatal]` sinks it / `[serious]` fix before shipping / `[cosmetic]`. Every finding names the specific sentence, number, or step — no vibes.
4. **Fix and re-run.** Iterate until new findings degrade to nitpicks. That degradation, not a clean first pass, is the done signal.
5. **Report both lists**: what was fixed, and what was attacked but held. Surviving objections are what justify confidence.

## Rules

- Steelman the strongest counterargument before dismissing it; a weak version knocked down proves nothing.
- If two full passes find nothing serious, say so and stop. Inventing findings to appear rigorous is its own failure.
- On own output: fresh work reviewed by its author finds almost nothing. Re-read as a hostile stranger after a break, or hand it to a separate session.

## Gotchas

- Severity inflation makes reports unusable. Most findings are cosmetic; label them honestly or the fatal ones get ignored too.
- The most dangerous flaw is usually in the sentence the author is proudest of. Check it first.
