# Claude General Skills Library — v2

Fifteen general-purpose skills drafted by Claude Fable 5 (July 6, 2026) so any Claude model — Sonnet, Opus, future models — can inherit the same working standards. Each skill is a folder with a `SKILL.md` (open Agent Skills format), plus reference files, templates, and append-only log files that act as persistent memory.

## The library

| Skill | What it enforces |
|-------|------------------|
| `requirements-first` | Clarify-before-building gate: pin down goal, scope, done-criteria before any work |
| `model-routing` | Cheapest-model-that-clears-the-bar routing; briefing protocol + template |
| `session-handoff` ★ | Handoff notes so fresh sessions/models continue without re-discovery |
| `skill-maintenance` ★ | The self-improving loop: corrections → logged → one-line Gotcha upgrades |
| `red-team-review` ★ | Adversarial final pass; iterate until findings degrade to nitpicks |
| `output-standards` | Universal definition-of-done; verify before asserting |
| `debugging-playbook` | Reproduce-first, hypothesis-driven debugging; regression tests |
| `code-review-standards` | Correctness → security → edges order; severity-labeled comments |
| `writing-standards` | BLUF, cut-lists, 4+1 editing passes incl. AI-tells sweep |
| `research-methodology` | Source hierarchy, triangulation, confidence labels, stop rule |
| `decision-analysis` | Reversibility triage, pre-mortems, persistent decisions.log |
| `business-docs` | Status/proposal formats; numbers over adjectives; one ask per doc |
| `meeting-to-actions` | Decisions/owners extraction without fabrication |
| `data-analysis` | Data sanity checks, denominators, honest limits |
| `estimation` ★ | Ranges not points; reference-class forecasting; planning-fallacy correction |

★ = new in v2

## What changed in v2 (and why)

Based on Anthropic's engineering write-up of running hundreds of internal skills, plus community skill-library patterns:

- **Gotchas sections** — Anthropic's team calls gotchas the highest-signal content in a skill, built up from real failures. Key skills now carry seeded Gotchas sections that `skill-maintenance` grows over time.
- **Grow-from-failures model** — their best skills started as a few lines plus one gotcha. `skill-maintenance` (new) operationalizes exactly that loop, with an append-only `corrections.log`.
- **Memory inside skills** — skills can persist state in simple log files that future sessions read. `decision-analysis` now keeps `decisions.log`; `skill-maintenance` keeps `corrections.log`.
- **Handoffs** — `session-handoff` (new) preserves reasoning across sessions and model switches; templates live in `assets/`.
- **Adversarial review** — `red-team-review` (new) mirrors the internal pattern of critiquing until new findings are only nitpicks.
- **Don't state the obvious** — rules that restate default model behavior were cut; the quality bar for new rules is codified in `skill-maintenance`.
- **AI-tells sweep** — `writing-standards/references/ai-tells.md` catches the patterns readers most reliably flag as machine-written.

## Hardening pass (after v2)

- **Trigger de-confliction** — three skill pairs claimed the same trigger without saying who defers to whom. Fixed with explicit division-of-labor lines: `business-docs`→`writing-standards` (structure then polish), `code-review-standards`→`red-team-review` (routine then adversarial), and `output-standards`↔`red-team-review` (checklist always, red-team when stakes justify it).
- **`estimation` added** — the one genuine gap: models give confident point estimates that are reliably wrong across code, projects, and research. Corrects for the planning fallacy with decomposition, reference-class forecasting, and ranges over points.

## Install

**Claude Code (recommended):** copy skill folders into `~/.claude/skills/` (applies across all projects):

```bash
unzip claude-general-skills-v2.zip
cp -r claude-general-skills/*/ ~/.claude/skills/
```

For one project only, use `<repo>/.claude/skills/`. SKILL.md edits take effect live in a running session. The `.log` files inside skills are writable working memory — keep them with the skill folders.

**Claude apps:** individual `.skill` files can be saved as custom skills where supported.

## Before enabling — review checklist

1. Read each SKILL.md. **Delete any rule you disagree with** — a confidently wrong rule mis-steers every future session.
2. Edit rules to match how *you* work. Descriptions control triggering; if a skill fires wrongly later, edit its `description`, not its body.

## Personalize (highest value first)

1. `writing-standards/references/voice-samples.md` — paste 2–3 real samples of your writing.
2. `model-routing` — adjust the ladder to your plan's models and limits.
3. Let `skill-maintenance` do the rest: every correction you make becomes a one-line permanent upgrade.
