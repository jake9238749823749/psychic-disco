# The Five Dimensions

For each dimension: the question, how to assess it in ten minutes, and what good looks like.
Score 1–5 with the scale in `02-maturity-scale.md`.

---

## 1. Leverage — does the system multiply you, or employ you?

**The question:** for every 100 agent runs, how many minutes of your attention do they consume?

Count it honestly for a week: interventions, corrections, re-runs, checking outputs "just in case,"
answering the agent's questions, fixing what it broke. Divide by runs.

- Under 30 min per 100 runs: the system works for you.
- Over 4 hours per 100 runs: you work for the system. You don't have agents — you have needy employees
  who never sleep and never learn unless you teach them.

**What good looks like:** the human touchpoints are enumerated and shrinking. There's a list of
"things I used to intervene on," and it's getting shorter. Nobody checks outputs "just in case" —
either the verification is automated or the blast radius is small enough not to care.

**The killer follow-up:** if you doubled usage tomorrow, would your intervention hours double too?
If yes, you have a linear cost disguised as automation.

## 2. Blast radius — what's the worst one bad run can do?

**The question:** enumerate the maximum damage of a single runaway run. Not the likely damage — the maximum.

Walk the permission envelope: money it can move, messages it can send (and to whom), data it can read
and exfiltrate, production systems it can change, credentials it can touch. Write the list. Read it back.
If reading it makes you uncomfortable, the radius is too big.

**What good looks like:** the worst case is boring. Staging-only writes, draft-only outputs, spending caps
that trigger before anything real happens. The scary permissions require a human gate, and the gate
can't be bypassed by a clever prompt.

**The killer follow-up:** could a prompt injection do any of it? If your blast radius assumes a
well-behaved agent, you haven't measured the radius — you've measured the weather.

## 3. Verification — evidence or the builder's word?

**The question:** who verifies the verifier, and would you believe a bad result?

Map your confidence chain: the agent's output is checked by X, X is checked by Y, and so on up to you.
Now ask two things: (a) is any link in that chain the same entity that produced the work (maker = judge)?
(b) has the chain ever produced a failing verdict that was acted on? A verification system that has never
said "no" is decoration.

**What good looks like:** at least one check in the chain is independent of the builder — a separate model,
a deterministic test, a different session, a human who didn't write the thing. And there's a written record
of something that failed verification and got fixed. That record is your confidence.

**The killer follow-up:** if the system told you "everything is fine" for a month straight, would you
believe it or would you go look? If you'd go look, your verification is theater.

## 4. Unit economics — cheaper or more expensive at scale?

**The question:** what does one successful outcome cost, at 1x, 10x, and 100x current volume?

Not cost per run — cost per *successful outcome*, including re-runs, corrections, human intervention time
(priced at your hourly value), and infra. Now project it: which components scale sublinearly (fixed cost
amortized) and which scale linearly or worse (every run needs a human glance)?

**What good looks like:** the dominant costs are fixed or sublinear — the system gets cheaper per outcome
as it grows. The linear costs (human review, per-run API spend with no caching) are enumerated and have
a plan to bend down: caching, batching, smaller models for routine steps, review sampling instead of
review-everything.

**The killer follow-up:** at 100x volume, what breaks first — the budget or the human? If it's the human,
you don't have a scaling problem, you have a leverage problem (see dimension 1).

## 5. Compounding — is month six automatically better than month one?

**The question:** does every incident make the system permanently better, without you remembering to do it?

Check for the loop: incident → written record → new check or regression test → the same failure becomes
structurally impossible. Then check the loop runs on its own: is there a scheduled review, or does
improvement depend on someone feeling motivated on a Friday?

**What good looks like:** the system has scar tissue in the right places — checks that exist because
something broke, each dated, each still earning its place. And there's a pruning rule: checks older than
90 days get re-examined, because a checklist that only grows becomes a ritual nobody runs.

**The killer follow-up:** name the last three things the system learned. If you can't, it isn't learning —
it's just running.
