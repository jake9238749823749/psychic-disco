---
name: memory-protocol
description: The library's unified memory authority: which persistent store to write when, entry format, topic tagging, tombstone retractions, expiry, and compaction. Use whenever writing to HANDOFF.md, corrections.log, or decisions.log, when a log approaches ~50 entries, or when deciding whether a memory entry should exist at all.
---

# Memory Protocol

Three stores, one protocol. Every persistent memory in this library follows the rules below. The owning skills — session-handoff, skill-maintenance, decision-analysis — define *what* goes in their store; this skill defines *how* it is stored, retained, and retired.

## The stores

| Store | Owned by | Write when |
|---|---|---|
| `HANDOFF.md` | session-handoff | A session ends with unfinished work, or a model switches mid-task. State the next agent needs cold. |
| `corrections.log` | skill-maintenance | The user corrected you, or a mistake cost real time. Feed for the improvement loop. |
| `decisions.log` | decision-analysis | A protocol-level decision was made: options weighed, a pick committed. |

## Decision tree: which memory?

1. **Session ending with unfinished work?** → `HANDOFF.md`. Nothing else captures in-flight state.
2. **Were you corrected, or did something cost real time?** → `corrections.log`. Even if a handoff is also written — corrections feed the library, handoffs feed the next session.
3. **Did you weigh options and commit to one?** → `decisions.log`. A choice made without considered alternatives is a guess, not a decision; log it only if the protocol ran.
4. **None of the above?** → write nothing. Memory is not a diary. An entry nobody will consult is context tax on every future read.

Two stores can fire in one session — a corrected decision at session end lands in both logs. That is correct; they serve different readers.

## Entry format (log-line stores)

`<date> | [topic-tags] | <body per owning skill's convention>`

Applies to `corrections.log` and `decisions.log`. `HANDOFF.md` is a document, not log lines — see Document stores below.

- **Date** is ISO (`2026-09-26`), always first — expiry and ordering depend on it.
- **Topic tags** are 1–3 lowercase slugs (`auth-flow`, `estimation`, `multi-agent`). Tags are the index; without them every consultation is a full scan. Reuse existing tags before inventing new ones.
- **Body** follows the owning skill's field convention.

## Document stores (HANDOFF.md, doctrine.md, references/ pages)

Some stores are documents, not log lines. For them:

- **Provenance header, mandatory.** Every derived or distilled document opens with: source log entries (dates + which log), distillation date, and next review/expiry date. A derived document without provenance is unsourced authority — the exact failure this protocol exists to prevent.
- **Body follows the owning skill's template.** memory-protocol governs provenance and retention; the owning skill governs sections.
- **Tags live in the header**, not per line — one tag set covers the whole document.
- **Retraction = new version + tombstone.** Never edit a derived document in place to change its claims. Append a superseding version note citing the new evidence, and tombstone the superseded claims in the source log.
- **Expiry applies to the provenance.** A `doctrine.md` whose source entries have all expired gets re-distilled or deleted at compaction.

## Retractions: tombstones, never edits

To retract or supersede an entry, append a new line:

`<date> | [topic-tags] | SUPERSEDES <original-date>: <reason>`

Never rewrite or delete a past entry. History with holes teaches the wrong lessons — a superseded entry stays readable so future sessions see what was believed, when, and why it changed.

## Breakage point and compaction

Append-only breaks at **~50–100 entries**: the read cost of "scan the log for similar past ones" exceeds the value of the read, so agents skip it — memory that is never consulted is functionally no memory. Three fractures arrive together: no indexing (fixed by tags above), no supersession (fixed by tombstones), no compaction (fixed below).

**Compaction trigger:** any store hits 50 entries, or any entry passes 180 days old. On trigger:

1. Distill a `doctrine.md` in the same folder: the current standing rules, each citing its source log dates.
2. Archive the raw log to `archive/<store>-<date-range>.log`. Do not delete it — the archive is the audit trail.
3. Reset the live log to entries from the last 90 days, plus any tombstones those entries reference.

Never compact before the trigger fires — sparse logs compact into vibes, destroying the evidence the improvement loop needs.

## Expiry

Any entry with no new citations, references, or corroborating entries in **90 days** is eligible for deletion at the next compaction. Frequently-consulted entries survive by use; dead entries die by neglect. Unreferenced memory is indistinguishable from noise — this generalizes skill-maintenance's Gotcha expiry to every store.

## Gotchas

- <!-- seeded --> A log that is written but never read is the most expensive file in the folder: it costs context on every scan and returns nothing. If a store has zero reads in 90 days, the answer is not better entries — it is deleting the store.
- <!-- seeded --> Tag drift recreates the indexing problem tags were meant to solve: five spellings of one tag (`auth`, `auth-flow`, `authentication`) means five partial scans. Check the log for an existing tag before inventing one.
- <!-- seeded --> Compacting on vibes instead of the trigger destroys the raw material skill-maintenance promotes from. The 50-entry / 180-day trigger is a floor, not a suggestion.
