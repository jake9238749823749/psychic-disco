# General Agent Skills Library — v2.2

Seventeen general-purpose skills for agentic AI systems to inherit consistent working standards. Each skill is a folder with a `SKILL.md` (open Agent Skills format), plus reference files, templates, and append-only log files that act as persistent memory.

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
| `delegation-verification` ★ | Worker return contract; coordinator verification duty (maker≠judge); failure protocol |
| `memory-protocol` ★ | Unified memory authority: store selection, entry format, tombstones, expiry, compaction |

★ = new since v2

## What changed in v2.2 (memory unification + boundary repair)

- **memory-protocol** (new) — unified memory authority for all three stores (HANDOFF.md, corrections.log, decisions.log): which-store decision tree, standard entry format with topic tags, tombstone retractions (never rewrite history), 90-day expiry generalized, compaction trigger (50 entries / 180 days) distilling `doctrine.md`.
- **skill-maintenance / session-handoff / decision-analysis** — memory format and retention centralized under memory-protocol; each skill keeps its domain content (what to log), memory-protocol owns the mechanics (how to store it).
- **business-docs** — BLUF removed (single home is now `writing-standards`); seeded Gotchas added (was zero).
- **meeting-to-actions** — seeded Gotchas added (was zero).
- **research-methodology ↔ data-analysis** — mirrored invocation boundary: which skill for world-questions vs. data-questions, statistics-question routing, contradiction protocol (data first, then world).
- **decision-analysis** — ask-vs-test arbitration rule (reversibility triage decides); **requirements-first** — reversibility triage and ask-vs-test now cross-reference decision-analysis instead of re-deriving.
- **CHANGELOG.md** (new) — long-form record of every version with rationale and criticism per change.

## What changed in v2.1 (red-team hardening)

- **delegation-verification** (new) — closes the multi-agent gap: worker return contract (claim, evidence, confidence, what-was-not-verified), coordinator verification duty, one-narrowed-retry-then-escalate failure protocol.
- **skill-maintenance** — the loop now fires: mandatory log capture before the next user-facing message (hooked into output-standards' completion gate), two-incident promotion threshold, Gotcha citations with 90-day expiry.
- **estimation** — ungrounded reference classes must be declared and widen the range by 50%; new Gotcha against lab-coat guessing.

## What changed in v2 (and why)

Based on field-tested skill-library patterns from production agent deployments and community practice:

- **Gotchas sections** — real failure patterns are the highest-signal content in a skill. Key skills now carry seeded Gotchas sections that `skill-maintenance` grows over time.
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

Copy the skill folders into the skills directory used by your agent environment:

```bash
unzip general-agent-skills-v2.zip
cp -r general-agent-skills/*/ <agent-skills-dir>/
```

For one project only, copy the folders into that project's skills directory. SKILL.md edits take effect live in environments that reload skills during a running session. The `.log` files inside skills are writable working memory — keep them with the skill folders.

If your platform supports packaged skills, each skill folder can be packaged or imported individually.

## Before enabling — review checklist

1. Read each SKILL.md. **Delete any rule you disagree with** — a confidently wrong rule mis-steers every future session.
2. Edit rules to match how *you* work. Descriptions control triggering; if a skill fires wrongly later, edit its `description`, not its body.

## Personalize (highest value first)

1. `writing-standards/references/voice-samples.md` — paste 2–3 real samples of your writing.
2. `model-routing` — adjust the ladder to your available model tiers, pricing, and limits.
3. Let `skill-maintenance` do the rest: every correction you make becomes a one-line permanent upgrade.
