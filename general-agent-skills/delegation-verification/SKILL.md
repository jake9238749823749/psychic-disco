---
name: delegation-verification
description: Contract for multi-agent fan-out/fan-in: what a worker owes back, what the coordinator must verify, and how failures escalate. Use whenever spawning subagents, parallel workers, or any delegation where the result returns for integration — if one agent's output becomes another's input, this skill governs the handoff.
---

# Delegation & Verification

Delegation without verification produces confident garbage at scale. The coordinator that trusts worker output is not coordinating — it is laundering. Maker ≠ judge: the agent that produced the work never grades it.

## Worker return contract

Every delegated task returns all four, no exceptions:

1. **Claim** — what was done, in one paragraph.
2. **Evidence** — the artifacts, commands, or outputs backing the claim (paths, not descriptions).
3. **Confidence** — high / medium / low, with the single biggest reason it isn't higher.
4. **What was NOT verified** — the load-bearing assumption the worker did not check. Silence here is a lie; every task has one.

A result missing any of the four is incomplete. Do not integrate it.

## Coordinator verification duty

- **Independently check load-bearing claims.** Re-run the key command, open the key file, count the key items. The worker's evidence tells you *where* to look, not *what* you'll find.
- **Spot-check, don't re-do.** Verify the 1–2 claims everything else rests on. Full re-execution defeats the purpose of delegating.
- **Distrust the format.** A clean, well-structured worker report is not evidence of correct work. Polished wrongness is the common failure mode.
- **Never self-verify.** If you wrote the brief and ran the worker, your own second read of its output is not verification — and neither is a second run of the same procedure by you. Same author, same method, same blind spots: that is self-verification with extra steps, and it is forbidden. Independent means a different session, a different agent instance, or a deterministic check *mechanically different* from the worker's method (tests, linters, re-execution with different inputs).

## Failure protocol

1. **One narrowed retry.** If verification fails, re-brief the worker with the specific failure named and scope narrowed to the broken part. Never resend the same brief unchanged.
2. **Then escalate.** If the retry fails, stop delegating that piece and bring it to the user: what was attempted, the evidence trail, and what you need from them. Do not silently absorb the failure into a plausible-sounding summary.
3. **Log it.** Delegation failures that cost real time go to `skill-maintenance/corrections.log` like any other incident — including *which* part of this contract broke (bad brief? skipped verification? trusted the format?).

## Gotchas

<!-- seeded -->
<!-- seeded: 2026-07-06 (v2, date inferred from CHANGELOG) -->

- "The worker sounded confident" is not verification. Confidence is a property of the text, not the work.
- Splitting work across N workers multiplies the coordinator's verification duty, it does not divide it. Five unchecked workers produce five times the garbage, not five times the output.
- A worker that reports "done" with no evidence section has reported nothing. Send it back.
- A "second run" by the same agent that ran the first is not an independent check. If the method didn't change, the verification didn't happen.
