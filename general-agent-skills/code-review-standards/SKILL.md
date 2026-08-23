---
name: code-review-standards
description: How to review code, pull requests, and diffs to a consistent standard. Use whenever the user asks to review, check, critique, or audit code, shares a PR or diff, asks "is this code good/safe/correct," or before merging or shipping any code change — even for the user's own code or code this assistant just wrote.
---

# Code Review Standards

Review in priority order. A beautifully named variable in insecure code is a failed review.

## Review order

1. **Correctness** — Does it do what it claims? Trace the main path and one failure path by hand.
2. **Security** — Unvalidated input, injection surfaces, secrets in code, missing authorization checks, unsafe deserialization.
3. **Edge cases** — Empty, null, zero, negative, huge, duplicate, concurrent, unicode. Pick the three most likely for this code and check them explicitly.
4. **Tests** — Do tests exist, do they test behavior (not implementation), would they fail if the code were wrong?
5. **Readability** — Names say what things are; functions do one thing; no cleverness that needs a comment to survive.
6. **Performance** — Only flag if this is a hot path or the complexity class is wrong (accidental O(n²), query in a loop). Otherwise skip.

## Comment rules

- Label every comment: **[blocker]** must fix before merge, **[should]** fix soon, **[nit]** optional.
- Every [blocker] includes a concrete suggested fix, not just the objection.
- Do not request speculative abstraction ("might need this to be generic later"). Review the code that exists.
- Approve with nits rather than blocking on nits.

## Output format

1. Verdict in one line: approve / approve with changes / request changes.
2. Findings grouped by severity, each with `file:line` and suggested fix.
3. One sentence on what the change does well (genuine, not padding — omit if nothing).

## Self-review addendum

When reviewing code written in this same session, apply the list above with extra suspicion on steps 1–3: run it, don't just read it. For code where a bug would be expensive or irreversible, this checklist is the routine pass — escalate to `red-team-review` for the adversarial one.
