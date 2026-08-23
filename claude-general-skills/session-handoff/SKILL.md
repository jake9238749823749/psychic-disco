---
name: session-handoff
description: Write a handoff note so a fresh session or a different model can continue work without re-discovery. Use whenever a work session is winding down, context is getting long, or before switching models (especially expensive to cheap), and whenever the user says "continue later," "pick this up tomorrow," "save progress," "handoff," or "compact." Proactively offer a handoff at the end of any substantial multi-step task.
---

# Session Handoff

Context dies when a session ends. A handoff note converts spent context into an asset — it is the mechanism by which judgment survives a model switch.

## When to write one

- A session is ending with the task unfinished.
- Switching models mid-task (write the handoff on the expensive model; it captures the reasoning the cheap model can't reconstruct).
- Context is filling up — write the handoff *before* quality degrades, not at the last moment.

## Where it goes

A file, never chat: `HANDOFF.md` in the project or task folder. Chat scrollback is where handoffs go to die.

## What it contains

Copy `assets/handoff-template.md` and fill it in. The sections, in order of importance:

1. **Goal + status** — one line each.
2. **Decisions made, with WHY** — "chose X because Y failed when Z." Reasons are the one thing a fresh session cannot reconstruct; conclusions without reasons get re-litigated.
3. **Next steps, priority order** — step 1 described fully enough to start cold.
4. **Gotchas discovered this session** — the traps that cost time. Highest-signal section in the file.
5. **Done so far** — with evidence: file paths, commit hashes, links. Paths, not descriptions.
6. **Do-not-touch list** — what looks wrong but is deliberate.
7. **Open questions for the human.**

## Rules

- Write for a competent stranger with zero context. If it assumes memory of this session, it failed.
- One page maximum. A handoff nobody reads protects nothing.
- On the receiving end: read `HANDOFF.md` first, restate step 1 back to the user, then act.

## Gotchas

- A handoff written at the last sliver of context is written by a degraded author. Write it while there is still room to think.
- "Refactored the auth flow" is not a handoff entry. "Moved token refresh into middleware (commit a1b2c3) because the old inline version raced on concurrent requests" is.
