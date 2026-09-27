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
- **Checkpoint at ~60–70% context.** Write a HANDOFF-draft while you are still sharp: goal, status, decisions so far, next step. The end-of-session handoff UPDATES the draft — it is never written from scratch at the last sliver. A draft you later revise beats a perfect handoff you were too degraded to write.
- **Skimming your own reasoning is the trigger.** If you catch yourself skimming earlier reasoning instead of following it, you are past the checkpoint — stop and write the handoff NOW, before the next step.
- **Observable-event trigger (primary).** After every 3rd substantive user-facing deliverable, or after every decision appended to `decisions.log`, append a checkpoint line to the HANDOFF-draft: goal, status, latest decision, next step. Deliverables and log appends are observable events — they fire whether or not you notice your own degradation. The 60–70% context rule is the backup, not the plan.

## Where it goes

A file, never chat: `HANDOFF.md` in the project or task folder. Chat scrollback is where handoffs go to die.

Entry format, topic tagging, retraction, and retention follow `memory-protocol` — this skill defines what goes in the handoff, memory-protocol defines how it is stored.

## What it contains

Copy `assets/handoff-template.md` and fill it in. The sections, in order of importance:

1. **What I may have gotten wrong** — three things this session may have gotten wrong, stated plainly, placed first. The receiver inherits doubt, not false certainty; everything below is read through this section.
2. **Goal + status** — one line each.
3. **Decisions made, with WHY** — "chose X because Y failed when Z." Reasons are the one thing a fresh session cannot reconstruct; conclusions without reasons get re-litigated.
4. **Next steps, priority order** — step 1 described fully enough to start cold.
5. **Gotchas discovered this session** — the traps that cost time. Highest-signal section in the file.
6. **Done so far** — with evidence: file paths, commit hashes, links. Paths, not descriptions.
7. **Do-not-touch list** — what looks wrong but is deliberate.
8. **Open questions for the human.**

## Rules

- Write for a competent stranger with zero context. If it assumes memory of this session, it failed.
- One page maximum. A handoff nobody reads protects nothing.
- On the receiving end: read `HANDOFF.md` first, restate step 1 back to the user, then act.

## Gotchas

- A handoff written at the last sliver of context is written by a degraded author. Write it while there is still room to think.
- "Refactored the auth flow" is not a handoff entry. "Moved token refresh into middleware (commit a1b2c3) because the old inline version raced on concurrent requests" is.
