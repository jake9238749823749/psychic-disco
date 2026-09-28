---
name: meeting-to-actions
description: Turn meeting notes, call transcripts, or voice-memo dumps into decisions, action items, and follow-ups. Use whenever the user shares notes or a transcript, says "summarize this meeting/call," asks what was decided or who owns what, or wants a recap or follow-up email drafted from a conversation.
---

# Meeting → Actions

A meeting summary is a contract draft. Precision about who agreed to what matters more than polish.

## Why this is a standalone skill

Merge candidacy was considered and decided (v2.3): this content could live as a `business-docs/references/` page plus `output-standards` integrity rules. It stays separate for three reasons:

1. **The integrity rules are more enforceable than the general principle.** `output-standards` says "no silent assumptions." This skill says exactly what to do instead: mark `UNASSIGNED`, mark `NO DEADLINE`, keep `[unclear — confirm]`, keep commitment phrasing verbatim, never upgrade "I'll try" to "will deliver." Each is checkable in a way the general rule is not.
2. **This is a pipeline, not a document.** `business-docs` owns formats (what the finished doc looks like). This skill owns extraction (how an unstructured transcript becomes decisions and actions). Different job, different failure modes.
3. **Narrow trigger, narrow load.** It fires only on meeting notes and transcripts. Merging it into `business-docs` would tax every status update and proposal with extraction rules they never need.

Thin is not the same as redundant. If this skill's Gotchas stay seeded past 90 days with no real incidents, revisit the merge — thinness without field evidence is the actual merge signal.

## Extract in this order

1. **Decisions made** — stated faithfully to the original wording. A decision has the form "we will X." Vibes and leanings are not decisions.
2. **Action items** — each with owner, deadline, and blocked-by (if any).
3. **Open questions** — raised but not resolved.
4. **Context worth keeping** — numbers cited, commitments from outside parties, changed assumptions.

## Integrity rules

- **Never invent an owner or a date.** Missing owner → mark `UNASSIGNED`. Missing date → mark `NO DEADLINE`. Flagging gaps is the job; filling them silently is fabrication.
- Ambiguous decisions get `[unclear — confirm]` rather than a cleaned-up guess.
- Keep commitment phrasing close to verbatim. "I'll try to look at it" and "I'll do it by Friday" are different promises; do not upgrade one to the other.
- Attribute contested points ("A argued X; B disagreed") instead of averaging them into false consensus.

## Output template

```
DECISIONS
1. <decision> (owner of consequence: <name>)

ACTIONS
| # | Action | Owner | Due | Blocked by |

OPEN QUESTIONS
- <question> (needs: <who/what>)

CONTEXT
- <number, commitment, or assumption worth keeping>
```

## Gotchas

<!-- seeded -->
<!-- seeded: 2026-07-06 (v2, date inferred from CHANGELOG) -->

- "We'll circle back" extracted as a decision. It is a deferred non-decision — log it under Open Questions with the trigger that reopens it, or it becomes a zombie that resurfaces every meeting.
- An action item with neither deadline nor blocker silently dies. "Waiting on X" is a blocker; "sometime" is not. Every action needs one of the two.
- Verbatim commitments get upgraded in the recap email. "I'll try" becoming "will deliver by Friday" manufactures a promise the speaker never made — the recap is where fabrication risk peaks, because the pressure to sound decisive peaks there.

## Offer next

After the summary, offer exactly one follow-up: draft the recap email, or add the actions to a task list — whichever the context suggests. Do not do both unprompted.
