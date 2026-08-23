---
name: debugging-playbook
description: Systematic debugging method for any bug, error, failing test, or "why doesn't this work" situation. Use whenever the user pastes an error message or stack trace, says something is broken, failing, flaky, or behaving unexpectedly, or asks to fix a bug — in any language or system, even if they don't use the word "debug."
---

# Debugging Playbook

Debug by narrowing, not by guessing. Every step should cut the search space roughly in half.

## The loop

1. **Reproduce first.** Get a minimal, deterministic reproduction before changing anything. If it can't be reproduced, the task is "make it reproducible," not "fix it."
2. **Read the actual error.** Top of the stack trace, exact message, exact line. Quote it back. Most bugs are solved by taking the error message literally.
3. **State a hypothesis before touching code.** "I believe X because Y. If true, Z will happen when I check W." No hypothesis, no edit.
4. **Change one thing at a time.** After each change: re-run the reproduction, record the result, revert if it didn't help.
5. **Bisect when lost.** Binary-search commits (git bisect), inputs, or code paths. Ten steps covers a thousand suspects.
6. **Instrument instead of staring.** Add targeted logging/prints at the boundary where good state becomes bad state. Remove them after.

## Check the boring things first

Before deep theories, verify in under two minutes: wrong environment or branch, stale cache or build artifact, version mismatch, typo in config/env var name, the code being edited is the code being run.

## After the fix

- State the root cause in one sentence. If it can't be stated, the bug isn't understood — the symptom moved.
- Add a regression test that fails without the fix.
- Search for the same bug class elsewhere in the codebase before closing.

## Anti-patterns (stop if doing these)

- Shotgun edits: changing several things and re-running.
- "It works now" with no explanation of why it was broken.
- Blaming the framework/library/compiler before checking own code twice.
- Deleting the reproduction before the regression test exists.
