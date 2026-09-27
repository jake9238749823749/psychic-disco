---
name: skill-maintenance
description: Turn corrections and costly mistakes into permanent one-line upgrades to this skill library. Use whenever the user corrects the same kind of behavior twice, a mistake costs more than ten minutes, or the user says "remember this," "you always do X," "add that to the skill," or "stop doing that" — even when nobody mentions skills. Also use for periodic library review and pruning.
---

# Skill Maintenance

A recurring pattern from production skill libraries: the best skills start as a few lines and a single gotcha, then grow one real failure at a time. Skills written to anticipate everything upfront bloat and railroad. This skill is the growth mechanism for the whole library.

## The loop

1. **Notice** a trigger: repeated correction, a mistake that cost real time, or an explicit "remember this."
2. **Log it — immediately.** Append one line to `corrections.log` in this skill's folder *before your next user-facing message*:
   `<date> | [topic-tags] | what went wrong | owning skill | proposed rule`
   Entry format, tagging, retraction, and retention follow `memory-protocol` (`<date> | [tags] | body`, tombstone retractions, 90-day expiry). Do not batch it for "later" — later is where corrections die. A trigger noticed but not logged is a trigger that never happened.
3. **Propose** a one-or-two-line Gotcha for the owning skill's SKILL.md. Show the exact diff. Never edit a skill silently.
4. **Apply on approval.** In environments that reload skills live, SKILL.md edits can take effect during a running session.

## Rule quality bar

A rule earns its context cost only if it is:

- **Specific and testable** — "check the forwarded-IP header, not the raw IP," not "be careful with networking."
- **The trap, not the virtue** — name what goes wrong, not a value statement.
- **Incident-derived** — it would have prevented the actual failure that spawned it.
- **Non-default** — never add a rule restating what a capable model does anyway; that adds context without adding value.

## Where a rule belongs

- Behavior mistake → the owning skill's **Gotchas** section.
- Skill fired at the wrong time (or failed to fire) → edit that skill's **description**, not its body.
- No skill owns it → propose a new skill of ~5 lines plus the one gotcha. Let it earn growth.

## Periodic review (monthly, or when the log hits ~10 entries)

- **Two-incident promotion.** No Gotcha is added until two independent log entries cite the same trap. One-off incidents stay in the log; only repeats earn context cost. This kills overfitting to a single bad afternoon.
- **Cite the evidence.** Every Gotcha cites the log dates that produced it (e.g. `<!-- 2026-09-26, 2026-10-02 -->`). A Gotcha with no citations is a hunch, not a rule.
- **Expiry.** Retention follows `memory-protocol`: unreferenced entries die by neglect. Gotchas are memory too — a Gotcha with no new citations in 90 days is deleted at review. Stale rules cost context and mislead; the raw log keeps the history.
- Delete rules that never fire, and rules the user keeps overriding — an overridden rule is a wrong rule.
- Split any SKILL.md drifting past ~150 lines: move detail to `references/`.

## Gotchas

- A rule drafted mid-frustration is usually too broad. Write the narrow version that covers the actual incident; widen it only if it recurs.
- Two similar rules in one skill means neither is being read. Merge them.
