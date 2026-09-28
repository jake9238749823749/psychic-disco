# Agent Skills Standard — DRAFT 0.1 (candidate)

> **DRAFT STATUS — READ FIRST.** This is a **candidate standard, not a final one.**
> It has **not** passed independent review. The library it describes (v2.4) has
> **not** had an independent maker≠judge review either. Nothing here is
> certified, GREEN, or final. Treat every rule below as a proposal under test:
> adopt what survives contact with your own sessions, log what breaks in
> `corrections.log` per `skill-maintenance`, and expect this document to change
> after the pending independent review. A standard that cannot describe its own
> draft status cannot be trusted to describe anything else.

## 1. Skill manifest format

Every skill declares itself in YAML frontmatter at the top of its `SKILL.md`.
Two fields are required; both are load-bearing:

```yaml
---
name: delegation-verification          # kebab-case; matches the folder name exactly
description: Contract for multi-agent fan-out/fan-in: what a worker owes back,
  what the coordinator must verify, and how failures escalate. Use whenever ...
---
```

- **`name`** — kebab-case, unique across the registry, identical to the skill's
  folder name. Renaming a skill is a breaking change (see §5).
- **`description`** — one trigger paragraph: what the skill governs and the
  invocation condition ("use whenever X"). Descriptions control triggering; a
  skill that fires wrongly gets its `description` edited, not its body.
- Optional fields a skill MAY declare: `version`, `introduced_in`, `status`
  (see §6). If present they must match `registry/index.json`.

## 2. Skill anatomy

A skill is a folder. Required and optional contents:

```
<skill-name>/
  SKILL.md            # REQUIRED — the skill itself: manifest frontmatter + rules
  references/         # optional — supporting material (checklists, ai-tells, samples)
  assets/             # optional — templates (handoff templates, brief templates)
  *.log               # optional — append-only working memory, never rewritten:
                      #   corrections.log (skill-maintenance), decisions.log
                      #   (decision-analysis), durations.log (estimation)
  HANDOFF.md          # optional — session-handoff working document
```

Rules for the anatomy:

- `SKILL.md` is the only required file. Everything else is earned by use.
- Log files are **append-only**. Corrections use tombstone retractions
  (`SUPERSEDES <date>`), never in-place edits — history is evidence.
  (Authority: `memory-protocol`.)
- Cross-skill references carry a **one-line payload**, never a naked pointer:
  the pointer names the authority, the payload delivers the content.
  (Authority: `skill-maintenance`, no-naked-pointers rule.)
- Gotchas sections hold **observed failure patterns**, labeled `seeded` until
  replaced by real incidents from `corrections.log`. Seeded Gotchas expire in
  90 days if no real incident replaces them.

## 3. Eval protocol (summary)

A skill — or a change to one — is evaluated by outcome, not by prose quality.
The protocol, in firing order:

1. **Maker ≠ judge.** The agent that produced the work never grades it.
   Independent means a different session, a different agent instance, or a
   deterministic check *mechanically different* from the worker's method.
   Re-running the same procedure is self-verification in disguise ("second run"
   laundering) and is prohibited. (Authority: `delegation-verification`.)
2. **Red-team pass.** Adversarial review, maximum two passes with the same
   reviewer. Pass 1 is broad and checklist-driven; pass 2 targets ONLY the
   single highest-severity finding — verify the fix with evidence or confirm
   the flaw with evidence. Done when pass 2 answers the top-risk question
   with evidence, or when two passes complete with no above-nitpick findings
   AND the completed checklist is attached. (Authority: `red-team-review`.)
3. **Severity rubric.** Every finding carries one label with a one-clause
   justification — no vibes, no unlabeled findings:
   - `[fatal]` — wrong conclusion, or actionable harm if shipped. Blocks.
   - `[major]` — materially weakens the deliverable. Fix before shipping.
   - `[minor]` — polish. Fix if cheap.
   - `[nitpick]` — cosmetic. Never blocks.
   
   Severity downgrades require stated evidence; a severity drifting down with
   no cited reason is reviewer fatigue wearing the rubric. A clean pass
   (zero above-nitpick findings) is valid only with the completed
   line-by-line checklist attached — distrust a clean pass-1 the way you'd
   distrust a finding-less pass.
4. **Completion gate.** Verify before asserting: no claim of done/GREEN without
   checking real state. Past green is not evidence the gate runs today.
   (Authority: `output-standards`.)
5. **Correction capture.** Every correction during evaluation is logged to
   `corrections.log` before the next user-facing message; a rule is promoted
   to a Gotcha only after a **second** independent incident; Gotchas carry
   dated citations and 90-day expiry. (Authority: `skill-maintenance`.)

A self-graded PASS is void. Record "unseparated self-evaluation" and get a
human or an independent instance to re-run the gate.

## 4. Registry

`registry/index.json` is the machine-readable index of every skill in the
library: `name`, `path`, `version`, one-line `description`, `status`.
It is generated from the repo, not hand-maintained prose — if a skill folder
exists and is not in the index, the index is wrong. Consumers (installers,
marketplaces, auditors) read the index, not the README table.

## 5. Versioning rules

- Library versions are `v<major>.<minor>` (`v2.4`). A minor bump = new rules,
  loophole closures, or new skills. A major bump = breaking changes
  (renamed skills, removed rules, changed manifest fields).
- Every version gets a `CHANGELOG.md` entry with three parts: **why** the
  change, **what failure it prevents**, and **honest criticism** of the change
  itself. No praise without criticism — an entry that cannot name its own
  weakness is not finished.
- Individual skills carry the library `version` they ship in
  (`registry/index.json` records it) plus `introduced_in` for the version
  that first added them.

## 6. Certification levels

| Level | Meaning | Requirements |
|-------|---------|--------------|
| `candidate` | Authored and in-repo. Unproven. | Manifest valid, anatomy correct. |
| `reviewed` | Survived independent evaluation. | Candidate + maker≠judge review by a different agent/session + red-team two-pass with checklist attached + zero open fatal/major findings. |
| `certified` | Proven in the field. | Reviewed + field evidence (real `corrections.log` incidents or `durations.log` deposits from live sessions, not seeded content) + no open findings of any severity + 90 days without a fatal/major incident. |

**Current state (honest): all 17 skills and this standard itself are
`candidate`.** Independent review of v2.4 is pending. No skill in this library
may claim `reviewed` or `certified` until that review lands and each skill
individually clears the bar above. The registry records per-skill status so
this claim is checkable, not rhetorical.

## 7. Conformance

A third-party skill collection conforms to this standard (draft) when:

1. Every skill has a valid manifest (§1) and correct anatomy (§2).
2. `registry/index.json` lists every skill folder, parses as JSON, and its
   `status` values are honest per §6.
3. Changes ship with CHANGELOG entries meeting the §5 three-part rule.
4. No skill claims a certification level it has not earned — and the evidence
   (review reports, checklists, log excerpts) is linked from the registry
   entry or the skill folder.

Non-conformance is not a moral failure; it just means "not this standard."
Fork it, beat it, or ignore it — but don't claim it.
