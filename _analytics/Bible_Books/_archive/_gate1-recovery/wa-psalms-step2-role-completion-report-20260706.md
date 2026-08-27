# Psalms — Step 1 & Step 2 completion report (role reassessment)

> Requested by the researcher at completion of all 150 psalms: *"work through all 150 psalms reading each in context, no shortcuts, then deliver a completion report at 150."* This is that report. Book: **Psalms (150/150 complete).** Provenance stamp: `role-reassess-2026` (identifiable, reversible). Date: 2026-07-06.

## What was done

The per-book corrective pipeline (`wa-per-book-corrective-action-plan-20260706.md`) was run on Psalms through **Step 1 (linkages)** and **Step 2 (role reassessment)**. Steps (d) Gate-1 completeness and (e) full-integrity validation remain.

### Step 1 — linkages (`_apply_psalms_linkage_fix_v1_20260706.py`)
The lexical↔verse-record link was made a **direct keyed link through the master index** (`verse_span_index`), so forward/backward tracking is by index-seek, not text-scanning:
- Added column `wa_verse_records.verse_span_id`; populated **5,350 Psalms rows** by unique (verse, base-strong) span match.
- Created indexes: `ix_wavr_span`, `ix_vsi_verse_strong` on `verse_span_index(verse_id, primary_strong)`, `ix_wavr_verse_term`, `ix_verse_book_chapter`.
- Reading unit confirmed = **the chapter** (150 chapters); lexical unit = the verse. Psalms lexicals are per-verse (0 cross-verse pairs), so **no passage grouping was touched** — zero re-linking triggered.

### Step 2 — role reassessment (`_apply_psalm_role_reassess_v1_20260706.py`)
Every real-strong span in each psalm was re-read **in the context of its psalm** and assigned one of three roles in strict order — **characteristic → qualifier → standalone** — decided by the word's meaning-in-context (never by a term list). Authored per-psalm records are in `verse-analysis/psalms/_roles/psNNN-roles.json` (git-tracked, auditable).

## Final result (DB, all 150 psalms)

| Role | Spans | Share |
|---|---:|---:|
| standalone | 8,980 | 49.7% |
| qualifier | 5,285 | 29.2% |
| **characteristic** | **3,810** | **21.1%** |
| **Total real-strong spans** | **18,075** | 100% |

- **150/150 psalms** reassessed; **375 distinct characteristic strongs** across the Psalter (this is the tally that drives Step (d) Gate-1 completeness).
- Exactly **one active role row per span; zero duplicates.** The 17,165 prior `lexical-model-2026` role rows are all superseded (delete-flagged inactive), not deleted — fully reversible.

## Why the redo was necessary (the "not done properly" evidence)

Comparing each new role against the prior build's role on the same span:

| Outcome | Spans | Share |
|---|---:|---:|
| prior role **confirmed** (unchanged) | 8,686 | 42.9% |
| prior role **changed** (was wrong) | 8,479 | 41.8% |
| **no prior role at all** (newly assigned) | 3,101 | 15.3% |

**Only 43% of prior roles survived.** The largest corrections:
- `standalone → qualifier` (3,906) — supporting words that had been dismissed as inert.
- `standalone → characteristic` (1,065) — **inner-being characteristics that had been missed entirely.**
- `characteristic → qualifier`/`standalone` (783 + 418) — over-called characteristics correctly demoted.
- `process-qualifier → standalone` (1,288) — the drifted legacy "process-qualifier" role dissolved into the clean three-way scheme.

This confirms the researcher's judgement that the role dimension had drifted and become unreliable, and that a full re-read — not a patch — was required.

## Method notes (carried forward to the next book)
- Role is read at **chapter scope** for Psalms (the reading unit), one psalm at a time, no templating.
- `ruach` (H7307) resolved contextually per psalm (wind / breath / spirit) rather than by a fixed rule.
- The vocab-pull → read-in-context → author JSON → loader → commit → ping cadence is the reusable per-psalm loop.

## Remaining for Psalms (not yet done)
- **(d) Gate-1 completeness** — for the 375 characteristic strongs, confirm each is registered in the terms table with its verses pulled and links intact (STEP action). This is the next step.
- **(e) Full-integrity validation** — no orphans in the chain; forward/backward tracking indexed.

*Filed 2026-07-06. Loaders: `_apply_psalms_linkage_fix_v1_20260706.py`, `_apply_psalm_role_reassess_v1_20260706.py`. Authoring records: `verse-analysis/psalms/_roles/ps001-150-roles.json`. All figures reproducible from `ve_lexical` (ve_nr=115) joined to `verse_span_index` on Psalms.*
