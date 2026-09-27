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
3. **Rank findings against the rubric.** Every finding carries one label, justified in one clause — no vibes, no unlabeled findings:
  - `[fatal]` — wrong conclusion, or actionable harm if shipped (bad advice sent, money moved, security hole).
  - `[major]` — materially weakens the deliverable (a section that doesn't hold up, a number that can't be defended). Fix before shipping.
  - `[minor]` — polish: unclear phrasing, weak structure, missing caveat. Fix if cheap.
  - `[nitpick]` — cosmetic: typos, formatting, style. Never blocks.
4. **Fix in severity order, then one targeted pass.** Fix findings fatal → serious → cosmetic. Pass 2 checks ONLY the single highest-severity finding from pass 1: was it actually fixed? Re-verify with evidence — do not re-read the whole work.
5. **Stop rule.** Done when (a) pass 2 answers the top-risk question with evidence, or (b) two passes complete with no above-nitpick findings AND the completed checklist is attached showing what was checked. No third pass with the same reviewer.
6. **Report both lists**: what was fixed, and what was attacked but held. Surviving objections are what justify confidence.

## Rules

- Steelman the strongest counterargument before dismissing it; a weak version knocked down proves nothing.
- If two full passes find nothing serious, say so and stop. Inventing findings to appear rigorous is its own failure.
- On own output: fresh work reviewed by its author finds almost nothing. Re-read as a hostile stranger after a break, or hand it to a separate session.

## Gotchas

- Severity inflation makes reports unusable. Most findings are cosmetic; label them honestly or the fatal ones get ignored too.
- The most dangerous flaw is usually in the sentence the author is proudest of. Check it first.
- A pass that finds nothing without a completed checklist is not a pass — it is a skipped pass. Findings that get weaker across passes is evidence of reviewer fatigue, not work quality: stop and escalate to a fresh session instead of running a third pass with the same reviewer.
