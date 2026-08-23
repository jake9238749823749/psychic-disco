# Task Brief Template

Copy, fill in, delete unused lines. A good brief is short but leaves no room for wrong assumptions.

```
GOAL
<One sentence. The outcome, not the activity.>

DONE WHEN
- <Checkable criterion 1>
- <Checkable criterion 2>

CONSTRAINTS
- Do not change: <files, APIs, behavior that must stay fixed>
- Style/conventions: <link or rules>
- Avoid: <libraries, patterns, approaches ruled out and why>

READ FIRST (in order)
1. <file or link — why it matters>
2. <file or link>

KNOWN PITFALLS
- <Mistake a naive attempt would make, and what to do instead>

OUTPUT FORMAT
<Exact deliverable: "a diff", "a 1-page memo with BLUF", "a plan as numbered steps, no code yet">

IF STUCK OR AMBIGUOUS
Ask before assuming. Specifically flag: <the decisions you want surfaced, not made>.
```

## Example (filled in)

```
GOAL
Add rate limiting to the public /search endpoint.

DONE WHEN
- Requests over 30/min per IP get HTTP 429 with a Retry-After header
- Existing tests pass; new tests cover the limit boundary and header

CONSTRAINTS
- Do not change: response schema of successful requests
- Use the middleware pattern already in src/middleware/, not a new framework

READ FIRST
1. src/middleware/auth.py — the pattern to copy
2. tests/test_search.py — the test style to match

KNOWN PITFALLS
- The load balancer sets X-Forwarded-For; raw client IP is the proxy. Use the forwarded header.

OUTPUT FORMAT
A plan as numbered steps first. Wait for approval before writing code.

IF STUCK OR AMBIGUOUS
Ask before assuming. Flag: choice of storage for counters (memory vs Redis).
```
