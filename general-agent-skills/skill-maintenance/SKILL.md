---
name: skill-maintenance
description: Turn corrections and costly mistakes into permanent one-line upgrades to this skill library. Use whenever the user corrects the same kind of behavior twice, a mistake costs more than ten minutes, or the user says "remember this," "you always do X," "add that to the skill," or "stop doing that" — even when nobody mentions skills. Also use for periodic library review and pruning.
---

# Skill Maintenance

A recurring pattern from production skill libraries: the best skills start as a few lines and a single gotcha, then grow one real failure at a time. Skills written to anticipate everything upfront bloat and railroad. This skill is the growth mechanism for the whole library.

## The loop

1. **Notice** a trigger: repeated correction, a mistake that cost real time, or an explicit "remember this."
2. **Log it** — append one line to `corrections.log` in this skill's folder:
   `<date> | what went wrong | owning skill | proposed rule`
   The log is append-only memory; future sessions read it to spot patterns.
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

- Promote repeated log entries into rules.
- Delete rules that never fire, and rules the user keeps overriding — an overridden rule is a wrong rule.
- Split any SKILL.md drifting past ~150 lines: move detail to `references/`.

## Gotchas

- A rule drafted mid-frustration is usually too broad. Write the narrow version that covers the actual incident; widen it only if it recurs.
- Two similar rules in one skill means neither is being read. Merge them.
