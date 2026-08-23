---
name: requirements-first
description: Pin down an under-specified request before building anything. Use at the START of any create/build/implement/design/write task where the goal, scope, or success criteria aren't already explicit — before writing code, drafting a document, or scaffolding a solution. Trigger whenever a request could be built more than one way and the wrong interpretation would waste real work. Skip only when the user has already given a detailed spec or explicitly says "just do it."
---

# Requirements First

Most wasted work is building the wrong thing fast. A few minutes clarifying scope beats hours of well-executed misunderstanding. This is a gate: it runs before the building skills, not alongside them.

## The gate

Do not produce implementation, code, or scaffolding until the goal, constraints, and definition of done are agreed. State plainly: "Let me confirm what you need before I build."

## Elicit — one question at a time

Ask the *fewest* questions that remove the *most* uncertainty. One per turn, so each answer sharpens the next — a wall of questions gets skimmed and half-answered. Cover, in rough priority:

1. **Purpose** — what is this for, and who uses it? (Reframes half of all requests.)
2. **Definition of done** — how will we both know it's finished? Get a checkable criterion, not a vibe.
3. **Hard constraints** — what must it do, avoid, integrate with, or stay under (time, budget, stack, format)?
4. **What it is *not*** — the single fastest scope-cutter. "Out of scope for now: X, Y."

Stop asking the moment further answers wouldn't change what you build. Over-interrogation is its own failure.

## Propose before you build

For anything non-trivial, offer 2–3 approaches with the real trade-off named (fast vs. flexible, simple vs. complete), and a recommendation. Let the user pick the direction before you commit to it.

## Confirm, then build

Play back the agreed spec in 2–4 lines — goal, done-criteria, key constraints, what's excluded — and get a yes. That playback is the contract; it's what you're accountable to. Use `assets/spec-playback.md` as the template. Then, and only then, hand off to the building skills.

## When to skip the gate

- The user already gave a detailed, unambiguous spec — don't re-interrogate; just restate your understanding in one line and proceed.
- The user explicitly says "just do it" / "your call" — make reasonable assumptions, **state them inline**, and build.
- The task is trivial or fully reversible — a wrong guess costs seconds, so guess.

## Gotchas

- The instinct to look helpful by immediately producing something is exactly the failure this gate prevents. Resist the first-turn artifact when scope is unclear.
- "Any preferences?" as a single vague catch-all gets a vague answer. Ask specific, answerable questions.
- Clarifying is not stalling only if it converges. If you've asked twice and still can't start, you're over-scoping — make an assumption, state it, and build.
- Don't smuggle in a full solution disguised as a "clarifying question." Ask, then wait.
