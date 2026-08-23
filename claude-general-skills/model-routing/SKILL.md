---
name: model-routing
description: Choose the right Claude model (Sonnet, Opus, Fable) for a task and write briefs that get near-top-tier results from cheaper models. Use whenever the user asks which model to use, mentions usage limits, credits, cost, or rate limits, asks to draft a prompt or brief for another model or session, or starts multi-phase work where exploration and final execution could run on different tiers — even if they don't say the word "model."
---

# Model Routing

Route every task to the cheapest model that clears the quality bar. Escalate on evidence, not vibes.

## Default ladder

| Tier | Use for | Examples |
|------|---------|----------|
| Sonnet (default) | Routine, well-specified work | Boilerplate, refactors, test generation, summaries, first drafts, formatting, extraction |
| Opus | Hard reasoning, ambiguity, stakes | Architecture decisions, gnarly debugging, important documents, multi-constraint planning |
| Fable (metered) | Work that would justify a senior contractor | Whole-codebase changes, final pass on high-stakes deliverables, problems two Opus attempts failed on |

## Escalation triggers (go UP a tier)

- Two genuine attempts at the current tier failed or required heavy correction.
- The task is irreversible or has a large blast radius (production, money, reputation).
- Requirements are ambiguous AND the cost of a wrong interpretation is high.

## De-escalation triggers (go DOWN a tier)

- The task is now well-specified because a stronger model already produced the plan.
- The phase is exploration or iteration — cheap loops beat expensive ones.
- Output will be reviewed by a human anyway before it matters.

## The briefing protocol

Most of a stronger model's advantage disappears when the brief is good. (If the task itself is still under-specified, run `requirements-first` before this — you can't brief cleanly for a goal that isn't pinned down.) Before handing work to a cheaper model, write a brief containing:

1. **Goal** — one sentence, outcome not activity.
2. **Definition of done** — checkable criteria ("all tests pass", "under 500 words", "handles empty input").
3. **Constraints** — what must not change, style rules, dependencies to avoid.
4. **Context** — files/links to read first, in priority order.
5. **Known pitfalls** — the mistakes a naive attempt would make.
6. **Output format** — exact shape of the deliverable.
7. **Escape hatch** — "If X is ambiguous, ask before assuming."

Use the fill-in template in `references/brief-template.md` when drafting a brief.

## Budget rules

- Cap expensive-model output: request plans and diffs, not full rewrites.
- Never use the top tier for interactive back-and-forth chat; brief first, then execute.
- When on metered credits, spend them on judgment (plans, reviews, post-mortems), not typing (code generation, drafts).

## Gotchas

- Escalating the model without upgrading the brief reproduces the same failure at higher cost. Rewrite the brief first; escalate second.
- Top-tier models over-deliver by default: cap scope explicitly ("plan only", "diff only") or pay for output nobody asked for.
- When switching models mid-task, have the outgoing model write a handoff first (see the session-handoff skill) — its accumulated reasoning is worth more than its remaining tokens.
