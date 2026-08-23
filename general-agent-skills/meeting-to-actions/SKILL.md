---
name: meeting-to-actions
description: Turn meeting notes, call transcripts, or voice-memo dumps into decisions, action items, and follow-ups. Use whenever the user shares notes or a transcript, says "summarize this meeting/call," asks what was decided or who owns what, or wants a recap or follow-up email drafted from a conversation.
---

# Meeting → Actions

A meeting summary is a contract draft. Precision about who agreed to what matters more than polish.

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

## Offer next

After the summary, offer exactly one follow-up: draft the recap email, or add the actions to a task list — whichever the context suggests. Do not do both unprompted.
