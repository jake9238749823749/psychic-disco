# Changelog — general-agent-skills

Long-form record of what changed, why, and what failure each change prevents.
No praise without criticism: every entry names its own weakness.

## v2.4 (2026-09-26) — loophole closures, ungameable severity, external tripwires

This pass closed the v2.3 "brutal remainder": the two live loopholes the first loop run logged but couldn't fix, red-team severity-label gaming, the handoff checkpoint's missing external tripwire, and the v2.2 cross-reference indirection tax.

### `delegation-verification`: "second run" loophole closed

**Why.** The "Never self-verify" rule listed "a second run" as an acceptable deterministic check. A rerun of the same procedure by the same agent is self-verification in disguise — laundering with extra steps — and it directly weakened maker≠judge, the skill's load-bearing rule. This was corrections.log incident #2 from the v2.3 loop run: known, logged, live.

**What it does.** The rule now names the loophole explicitly and forbids it: independent means a different session, a different agent instance, or a deterministic check *mechanically different* from the worker's method (tests, linters, re-execution with different inputs). New Gotcha: "If the method didn't change, the verification didn't happen."

**Process note.** This is a direct defect fix, not a Gotcha promotion — the two-incident rule governs promotion of incident-derived rules from the log; it does not block repairing a known defect in a shipped skill. The distinction is recorded here so a future review doesn't misread the fix as rule-breaking.

**Failure prevented.** Coordinator rubber-stamping worker output while holding a paper trail that claims independent verification.

**Criticism.** "Mechanically different" still requires judgment — is re-running with different inputs different enough, or does it share the worker's flawed oracle? The rule pushes the ambiguity into a smaller box without eliminating it. And the fix depends on the coordinator *wanting* real verification; a coordinator determined to coast can still pick the weakest available independent check.

### `memory-protocol`: document-store section with mandatory provenance

**Why.** The protocol claimed a uniform entry format across "all stores," but HANDOFF.md is a 7-section document and doctrine.md is distilled prose — neither is log lines. The format section had no carve-out, so the protocol's own authority didn't cover its most-read artifact. Corrections.log incident #3.

**What it does.** New "Document stores" section: every derived/distilled document opens with a mandatory provenance header (source log entries + dates, distillation date, next review/expiry date); body follows the owning skill's template; tags live in the header; retraction means a new version plus a tombstone in the source log (never in-place edits); expiry applies to the provenance — a doctrine.md whose sources all expired gets re-distilled or deleted at compaction. Entry format section re-scoped to log-line stores explicitly.

**Failure prevented.** Derived documents becoming unsourced authority — doctrine.md cited as truth with no trail back to the evidence, the exact failure the protocol exists to prevent.

**Criticism.** Provenance headers are only as honest as their author, and distillation is exactly where motivated reasoning hides — a distiller can cherry-pick which source entries to cite. The section constrains the *format* of honesty, not honesty itself. Also: no doctrine.md exists yet, so this section is currently untested machinery guarding a future artifact.

### `red-team-review`: severity rubric kills label gaming

**Why.** v2.3's two-pass stop rule moved the gaming to severity labels: a reviewer who wants out labels everything cosmetic in pass 1 and the apparatus ratifies a skipped review. Worse, the skill itself had a latent inconsistency — step 3 defined `[fatal]/[serious]/[cosmetic]` while step 5's stop rule referenced "nitpick," a label that didn't exist.

**What it does.** Fixed four-level rubric with definitions and one-clause justification required per finding: fatal (wrong conclusion / actionable harm), major (materially weakens; fix before shipping), minor (polish; fix if cheap), nitpick (cosmetic; never blocks). Labels unified across steps (serious→major). Two new Rules: downgrades need evidence (pass 2 lowering a severity must state what changed — a severity drifting down with no cited reason is reviewer fatigue wearing the rubric), and a clean pass must be earned (zero above-nitpick findings valid only with a line-by-line completed checklist attached). New Gotcha: severity deflation is the new gaming surface — distrust a clean pass-1 the way you'd distrust a finding-less pass.

**Failure prevented.** The ratified skipped review: a documented two-pass adversarial process that never threatened the work because the labels were chosen, not the findings.

**Criticism.** The rubric is still self-applied — a reviewer can write a one-clause justification for anything ("cosmetic: phrasing"). The checklist backstop can be pencil-whipped. Gaming didn't die; it moved to justification quality, which is at least *visible* in the report — a tired reviewer's thin justifications are now auditable, which is the real win. The two-pass ceiling from v2.3 still stands, still trading depth for ungameability.

### `session-handoff`: external tripwire + receiver distrust

**Why.** The 60–70% checkpoint and the skimming trigger both relied on the degraded author monitoring itself — the original problem, moved earlier. A degraded author is, by definition, bad at self-observation.

**What it does.** New primary trigger: after every 3rd substantive user-facing deliverable, or after every decision appended to decisions.log, append a checkpoint line to the HANDOFF-draft. Deliverables and log appends are observable events — they fire whether or not the author notices its own degradation. The 60–70% rule is demoted to backup. On the receiving end, distrust is now the default first step: verify the skepticism header's claims against the actual artifacts *before* acting; a handoff is a hypothesis about the work, not a record of it.

**Failure prevented.** The never-written checkpoint (advice without a mechanical trigger) and the receiver inheriting false certainty from a confident-but-wrong handoff.

**Criticism.** "Every 3rd deliverable" is a heuristic that will misfire — three trivial deliverables trigger a pointless checkpoint; one massive deliverable deserves one immediately. The receiver-distrust rule assumes the receiver has the context to re-verify; a cold-start cheap model may not be able to check the claims it's told to doubt, turning "verify first" into "stall first." And the skepticism header still depends on the author's honesty at the moment they're most incentivized to sound certain.

### Indirection tax paid: payloads on every pointer

**Why.** v2.1–v2.3 added cross-skill pointers everywhere (memory-protocol ×3, decision-analysis ×2, writing-standards ×1, plus hooks). A pointer that only says "see X" gets skipped when the agent is busy; a skipped rule is a dead rule. Centralization reduced drift risk but increased skip risk.

**What it does.** Audited every cross-skill pointer added in v2.1–v2.3. Pointers that already carried their payload (decision-analysis ask-vs-test, requirements-first reversibility, model-routing brief-before-cheap-model) were kept as-is. Five naked or near-naked pointers got one-line payloads: decision-analysis, estimation (×2), session-handoff, skill-maintenance memory-protocol references now inline the format (`<date> | [tags] | body`, tombstone retractions, 90-day expiry); business-docs' BLUF pointer now states the rule inline. New forward rule in skill-maintenance: "No naked pointers — every cross-skill reference carries its one-line payload. The pointer names the authority; the payload delivers the content."

**Failure prevented.** Format rules skipped because they lived one hop away — the agent writing a handoff never opening memory-protocol.

**Criticism.** Payloads duplicate content, which reintroduces the drift the centralization was meant to kill — if memory-protocol's format ever changes, five payloads go stale. The bet is that format changes are rare and skips are common; that bet is unmeasured. The no-naked-pointers rule itself adds a line to every future cross-reference, a small tax on every edit forever.

## v2.3 (2026-09-26) — first real loop run, self-filling calibration, ungameable review

### `skill-maintenance`: the improvement loop runs for the first time

**Why.** The loop had machinery since v2.1 (mandatory capture, two-incident promotion, 90-day expiry) and zero executions since 2026-07-06. A loop that never runs is decoration. This pass executed it for real: the v2.1/v2.2 commit history and the new/edited skills were re-read with fresh eyes, and three genuine incidents were found and logged to `corrections.log` — the seed entry deleted per its own instruction.

**What was logged.** (1) The v2.1 authoring script wrote a literal `\u2260` instead of the ≠ character into `delegation-verification/SKILL.md`; caught by a re-read and fixed before pushing — proposed rule: use literal characters when generating file content programmatically, unicode escapes in the generator language do not survive the write. (2) `delegation-verification`'s "Never self-verify" rule lists "a second run" as an acceptable check — a rerun of the same procedure is self-verification in disguise — proposed rule: deterministic checks must be mechanically different from the worker's method. (3) `memory-protocol` claims a uniform entry format across "all stores," but `HANDOFF.md` is a full document, not log lines — proposed rule: the format section must distinguish log-line stores from document stores.

**Failure prevented.** The specific failure this run prevents is meta: an improvement loop that exists only in documentation. Every future correction now has a live example of the format to follow.

**Criticism.** Honestly applied, the two-incident rule meant *no Gotcha was promoted*: all three incidents are singles, so all three sit in the log as proposals. That is the rule working as designed — but it also means this run changed zero skill content. The loop's value is still entirely prospective. If the log has no second incidents in 90 days, the honest conclusion is that the trigger surface is too narrow, not that the library is flawless. Also note: incident (2) is a live loophole in a shipped skill, logged but not fixed — the loop chose process over repair, which is correct per its rules and unsatisfying in the specific.

### `estimation`: self-filling `durations.log` reference class

**Why.** The v2.1 "widen the range by 50%" rule was a placeholder for the durations database nobody was building — an ungrounded heuristic standing in for the reference class the skill's own Method step demands. Nobody builds the database because no rule required anyone to.

**What it does.** New `estimation/durations.log` (format: `date | task category | estimated range | actual | error ratio`, category doubling as topic tag). New skill section: after ANY task you estimated, append the actual — no exceptions, even when right, even when embarrassing. For new estimates, scan newest-first for the same category; 3+ similar entries is a calibrated class and the median error ratio becomes the adjustment factor. Cold start handled explicitly: the first 3 estimates per category are labeled `uncalibrated`. Method step 2 now points at the log; the 50% widening survives only as a bootstrap rule with an expiration condition (fewer than 3 similar entries), not a permanent placeholder.

**Failure prevented.** Reference-class forecasting that is rhetorical rather than real — the skill demanded an outside view while providing no outside data to look at.

**Criticism.** The mandatory-deposit rule depends on the same session (or a diligent later one) circling back after the work — sessions end, attention moves on, and "no exceptions" will be the first rule bent. The log starts empty, so the skill's calibration is still entirely prospective; until the first real deposits land, every estimate remains uncalibrated and the 50% widening is still doing all the work. A log nobody writes to is a more elaborate placeholder.

### `red-team-review`: ungameable two-pass stop rule

**Why.** "Iterate until new findings degrade to nitpicks" was satisfiable by generating weaker findings on each pass — the reviewer could comply with the letter while the fatal flaw survived. The done-signal measured reviewer output, not work state.

**What it does.** Exactly two passes: pass 1 broad and checklist-driven with severity labels; pass 2 targets ONLY the single highest-severity finding — verify the fix with evidence, or confirm the flaw with evidence. Done when pass 2 answers the top-risk question with evidence, or when two passes complete with no above-nitpick findings AND the completed checklist is attached. No third pass with the same reviewer. New anti-gaming Gotcha: a finding-less pass without a completed checklist is a skipped pass, and weakening findings across passes is reviewer fatigue — escalate to a fresh session.

**Failure prevented.** The paper-trail review: a documented adversarial process that never actually threatened the work.

**Criticism.** The stop rule now leans hard on pass 1's severity labeling being honest — a reviewer who wants out can still label everything cosmetic in pass 1 and coast. The checklist-attachment requirement is the backstop, but checklists can be pencil-whipped too. Two passes is also a ceiling that could cut off a genuinely productive third angle; the rule trades depth for ungameability, and that trade is not free.

### `session-handoff`: fixing the degraded author (the WHEN, not the format)

**Why.** The skill warned against last-sliver handoffs, but its triggers fired exactly when the author was already degraded — "context is filling up" is observed by the party losing the ability to observe. memory-protocol fixed the format; nobody fixed who writes it or when.

**What it does.** (a) Checkpoint rule: at ~60–70% context, write a HANDOFF-draft while still sharp; the end-of-session handoff UPDATES the draft, never written from scratch at the last sliver. (b) Skepticism header, first section in the template: three things the outgoing session may have gotten wrong, stated plainly — the receiver inherits doubt instead of false certainty. (c) New trigger: catching yourself skimming your own earlier reasoning means you are past the checkpoint — write the handoff NOW.

**Failure prevented.** The confident, detailed, wrong handoff — worse than no handoff, because no handoff at least preserves the receiver's skepticism.

**Criticism.** The 60–70% checkpoint requires the author to notice context level while busy — the same self-observation the old trigger demanded, just earlier. The skimming trigger is the more honest mechanism (it names an internal sensation rather than a meter reading), but agents that don't introspect won't fire it. And the skepticism header only works if the author is honest about uncertainty at the moment they are most incentivized to sound certain — the handoff is often written to demonstrate competence, not doubt.

### `meeting-to-actions`: merge candidacy closed — stays standalone

**Why.** The original analysis flagged it as the merge candidate: thinnest content, narrowest trigger, expressible as a `business-docs/references/` page plus `output-standards` integrity rules. v2.2 gave it Gotchas instead of merging it. The question was left open; open questions rot.

**Decision and rationale.** It stays a standalone skill, recorded in its SKILL.md: (1) its integrity rules are more enforceable than the general principle — `output-standards` says "no silent assumptions," this skill says exactly what to do instead (`UNASSIGNED`, `NO DEADLINE`, `[unclear — confirm]`, verbatim commitment phrasing, never upgrade "I'll try"); (2) it is an extraction pipeline, not a document format — `business-docs` owns what finished docs look like, this owns how unstructured transcripts become decisions; (3) narrow trigger means narrow load — merging would tax every status update with extraction rules they never need. Thin is not redundant.

**Criticism.** The decision includes its own tripwire: if the Gotchas stay seeded past 90 days with no real incidents, the merge gets revisited — thinness without field evidence is the actual merge signal. This is a bet that meeting notes are a distinct enough failure surface; the next 90 days of the corrections log will confirm or refute it.

## v2.2 (2026-09-26) — memory unification and boundary repair

### New skill: `memory-protocol` (17th)

**Why.** Three persistent stores existed — `HANDOFF.md` (session-handoff), `corrections.log` (skill-maintenance), `decisions.log` (decision-analysis) — with no shared entry format, no retraction story, and no retention story. A session-ending agent had to consult three skills to persist state and still produced logs that rot: append-only breaks at ~50–100 entries, when the read cost of "scan the log for similar past ones" exceeds the value of the read and agents simply stop consulting the memory.

**What it does.** Decision tree for which store to write when (unfinished session → HANDOFF.md; correction → corrections.log; weighed-and-committed choice → decisions.log; otherwise write nothing). Standard entry format (`<date> | [topic-tags] | body`). Tombstone retractions — `SUPERSEDES <date>` appended, history never rewritten. 90-day expiry generalized across all stores. Compaction trigger (50 entries or 180-day-old entries) distilling a `doctrine.md` with the raw log archived.

**Failure prevented.** Stale guidance accumulating with no recency metadata; three stores aging under different rules (`decisions.log` had no size trigger at all); memory that exists but is never read — functionally identical to no memory.

**Criticism.** This is the 17th skill in a library already fighting bloat. The bet: centralizing mechanics removes more lines than it adds. If the owning skills' files don't shrink after adoption, the centralization failed and this skill should be merged back into its three owners.

### `session-handoff`, `skill-maintenance`, `decision-analysis`: defer to `memory-protocol`

**Why.** skill-maintenance carried its own 90-day Gotcha expiry while decisions.log had no retention rule whatsoever — two stores, two aging regimes, one rotting silently.

**Failure prevented.** Retention rules drifting apart across stores; a future edit to expiry landing in one skill while the others age under stale rules.

**What was kept.** Each skill's domain content is untouched: session-handoff still owns what goes in a handoff, skill-maintenance still owns promotion mechanics (two-incident threshold, citation requirements — those are loop logic, not storage logic), decision-analysis still owns what counts as a log-worthy decision. Only storage mechanics moved.

**Criticism.** Cross-references add indirection: an agent writing a handoff must now hold two skills open. If that indirection causes agents to skip the format rules, the cure is worse than the fragmentation.

### `business-docs`: BLUF removed; `writing-standards` named single home

**Why.** The same rule lived in two homes ("BLUF" in business-docs, "lead with the point" in writing-standards). Two copies means edits land in one and the other goes stale, and every agent reading both pays the context cost twice.

**Failure prevented.** Divergent lead-with-the-point rules after a future edit touches only one copy.

**Criticism.** The division-of-labor paragraph that "papered over" the duplication is gone, which removes the only place that told agents *why* the two skills both talked about openings. The cross-reference replaces it — thinner, but honest.

### Seeded Gotchas for `business-docs` and `meeting-to-actions`

**Why.** Both shipped zero Gotchas while the library's own doctrine declares failure patterns the highest-signal content. An empty Gotchas section signals "this skill has no known failure modes," which agents read as "this skill cannot fail" — the most dangerous possible reading.

**Failure prevented.** Blind spots in the two least-scrutinized skills: multi-ask status docs that get zero decisions, cost buried below recommendations, zombie "circle back" items, action items with neither deadline nor blocker, commitment upgrades in recap emails.

**Criticism.** Seeded Gotchas are invented, not observed — they are hypotheses wearing the uniform of experience. They are labeled as seeded, and they earn their keep only if skill-maintenance replaces them with real incidents. If they are still seeded in 90 days, the expiry rule should delete them.

### `research-methodology` ↔ `data-analysis`: invocation boundary

**Why.** Neither skill stated where external-evidence work ends and internal-data work begins. An agent facing a statistics question had no guidance on which to invoke.

**Failure prevented.** The two most expensive evidence errors: citing external statistics to explain dirty data without checking the data, and generalizing one dataset to the world without external triangulation. The boundary is a decision rule (where does the number come from? → start there; contradiction → data first, then world), not prose, so it fires at invocation time.

**Criticism.** Mirrored text in two files is duplication by design — the exact pattern v2.2 otherwise removes. The justification: invocation-time guidance must be visible in whichever skill the agent opened first. If the library grows a skill-index, this paragraph should move there and both skills should point at it.

### `decision-analysis`: ask-vs-test arbitration; `requirements-first`: cross-references

**Why.** Two skills prescribed opposite behaviors with no arbiter: requirements-first said interrogate serially ("one question at a time"), decision-analysis said act to learn ("find the cheapest test"). Worse, requirements-first re-derived reversibility triage ("trivial or reversible → guess") instead of referencing the skill that owns it — two implementations of one idea, zero cross-references.

**Failure prevented.** The signature failure: four rounds of user interrogation when a five-minute prototype had the answer. And the slow divergence failure: a future edit to reversibility logic landing in one copy only.

**Criticism.** The arbitration rule ("test if cheaper than the next question round-trip") requires the agent to estimate two costs — itself an estimation task, invoking the skill with the weakest enforceability score in the library. In practice agents will guess both costs. The rule is still better than no arbiter, but its inputs are soft.

## v2.1 (2026-09-26) — red-team top-3

### New skill: `delegation-verification` (16th)

**Why.** Every skill in the library assumed a single agent doing the work. Uncoordinated delegation is the dominant silent failure in multi-agent systems: confident garbage produced at scale, with no skill requiring the coordinator to distrust worker output.

**What it does.** Worker return contract (claim, evidence, confidence, what-was-not-verified), coordinator verification duty (independently check load-bearing claims — maker≠judge as an enforceable rule), failure protocol (one narrowed retry, then escalate with the evidence trail).

**Failure prevented.** Polished wrongness integrated without verification; workers reporting "done" with no evidence; coordinators absorbing failures into plausible-sounding summaries.

**Criticism.** Process overhead on every delegation — for trivial fan-out the contract costs more than it saves. The "spot-check, don't re-do" clause is the load-bearing defense; if coordinators full-re-verify, delegation was pointless and this skill becomes a tax with no benefit.

### `skill-maintenance`: mandatory capture, two-incident promotion, 90-day expiry

**Why.** The self-improvement loop had zero executions in ~3 months of the library's existence. Triggers were self-reported by the erring party — the agent with the least incentive to fire them.

**Failure prevented.** Cargo-cult rule accretion (judged by the agent that made the error, rubber-stamped on approval) and one-off overfitting (a rule born from a single bad afternoon).

**Criticism.** Mandatory capture adds a write to every corrected session; two-incident promotion means real one-off traps wait for a repeat before earning a rule. Both are deliberate taxes — the first buys a loop that runs, the second buys rules that generalize. If the log is still empty in 90 days, the problem was never the triggers.

### `estimation`: ungrounded reference classes

**Why.** Reference-class anchoring with no reference data is inside view in outside-view clothing — rigorous-looking ranges with ungrounded cores, the most dangerous silent failure in the skill.

**Failure prevented.** False precision: low/likely/high ranges inheriting authority from a single ungrounded guess.

**Criticism.** The 50% widening is itself ungrounded — a heuristic, not a measured correction. It is a placeholder until someone builds the durations database the skill actually needs. Also unaddressed: the skill still has no mechanism to *build* that database, so the widening rule may become permanent.

### `output-standards`: corrections.log capture hook

**Why.** The completion gate is the one checkpoint every session passes; hooking mandatory capture there makes the improvement loop fire without relying on any agent remembering skill-maintenance exists.

**Failure prevented.** The loop starving because its trigger lived in a skill nobody opens at session end.

## v2 (2026-07-06) — the library

Fifteen skills shipped: requirements-first, model-routing, session-handoff, skill-maintenance, red-team-review, output-standards, debugging-playbook, code-review-standards, writing-standards, research-methodology, decision-analysis, business-docs, meeting-to-actions, data-analysis, estimation.

What v2 introduced and why: Gotchas sections (failure patterns are the highest-signal content); grow-from-failures model (best skills start as a few lines plus one gotcha, operationalized via corrections.log); memory inside skills (decisions.log, corrections.log); session-handoff (reasoning surviving model switches); red-team-review (adversarial pass until findings degrade to nitpicks); don't-state-the-obvious (rules restating default model behavior cut, quality bar codified); AI-tells sweep for published prose.

Hardening pass after v2: trigger de-confliction across three skill pairs (business-docs→writing-standards for structure-then-polish, code-review-standards→red-team-review for routine-then-adversarial, output-standards↔red-team-review for checklist-always/red-team-when-stakes-justify); estimation added as the one genuine gap.

**Honest criticism of v2.** It shipped the memory mechanisms with no unified protocol — the exact fragmentation v2.2 had to repair. It shipped business-docs and meeting-to-actions with zero Gotchas while declaring Gotchas the highest-signal content. And the v2.1 red-team pass found the self-improvement loop had never executed once in three months: v2 built the machinery and never checked whether it ran. A library about verification that didn't verify itself.
