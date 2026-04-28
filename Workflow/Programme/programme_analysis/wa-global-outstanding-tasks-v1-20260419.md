# DB-Wide Review — Outstanding Tasks v1 — 2026-04-19

| Field | Value |
|---|---|
| Filename | wa-global-outstanding-tasks-v1-20260419.md |
| Governs | Tasks beyond CC's current skill/scope, raised during the DB-wide review |
| Discipline | CC-SKILL-001 (surface skill-limit tasks explicitly) |
| Produced | 2026-04-19 (session 5 — Phase D script update sweep) |
| Persistent | Yes — carried across sessions until resolved |

---

## How to Read This File

Each task has:

- **Status:** OPEN / IN_PROGRESS / RESOLVED
- **Source:** where the need was surfaced
- **Missing capability:** specifically what CC can't do alone
- **Recommended path:** how it should be addressed

RESOLVED entries are retained with resolution notes for audit.

---

## Task OT-DBR-001 — `engine/audit_word.py` rewrite for `mti_term_flags` joins

**Status:** **RESOLVED — 2026-04-19** (session 5, same day as raising)

**Source:** Phase D script update sweep (session 5)

**Context:**

Post-M24, `wa_term_inventory` no longer has `somatic_link` or `god_as_subject` columns. `engine/audit_word.py` reads these extensively (~8 sites) to drive filter logic for assigning `mti_terms.status`. Additionally, the file writes to `mti_terms.status_note` (dropped in M22) in ~5 UPDATE sites.

Broken sites:

- Line ~1295: `SELECT ti.god_as_subject, ti.somatic_link ...` — column no longer exists
- Lines 1348–1349: `gas = ti["god_as_subject"] ... som = ti["somatic_link"]` — column access fails
- Lines 1368, 1381, 1398, 1411, 1421: `UPDATE mti_terms SET ... status_note = ? ...` — column no longer exists

**Missing capability:**

CC can mechanically edit the file, but a correct rewrite requires:

1. Replacing the direct column read with a JOIN or sub-query on `mti_term_flags` (flag_id=1 for god_as_subject; flag_id IN (3,4) for somatic)
2. Either (a) dropping the `status_note` UPDATEs entirely, (b) redirecting to a different tracking field, or (c) writing a new table for audit-write notes
3. End-to-end testing across NEW_WORD / AUDIT_WORD modes on a representative registry

This is a substantive engineering change that requires testing beyond simple dry-run — it touches the filter logic that classifies every term during extraction.

**Blast radius of leaving broken:**

Any invocation of `python -m engine.engine --mode=audit_word --registry=N` will fail at the first SELECT on the dropped columns. The 6-word reprocess trigger (Phase F) explicitly relies on this path. Cannot proceed with Phase F.6 reprocess before this is fixed.

**Recommended path:**

1. Dedicated rewrite session. Replace column reads with joins; drop or redirect status_note writes.
2. Unit test on a single-word re-audit against a non-committed DB copy.
3. Apply to live only after the rewrite is confirmed behaviour-equivalent.

**Priority:** HIGH — blocks Phase F.6 reprocess trigger.

**Resolution (2026-04-19 session 5):**

- `_detect_bleed_candidates` SELECT replaced with `mti_term_flags` EXISTS joins: `flag_id=1` for GOD_AS_SUBJECT; `flag_id IN (3,4)` for SOMATIC.
- Column reads updated: `ti["gas_flag"]` / `ti["som_flag"]` replace direct `god_as_subject` / `somatic_link`.
- 5 `UPDATE mti_terms SET ... status_note = ? ...` clauses rewritten: `status_note` column dropped in M22; diagnostic rationale now emitted to stdout (captured by engine run log) with `print()` calls for F1–F5 filters.
- DB_ONLY_TERM block (`_build_gap_report`) updated: gas/som derived from `snapshot['mti_flags_by_id']` via `strongs_number → mti_terms.id → flag_id` lookup (snapshot is loaded once in `_load_snapshot`).
- Docstring + inline comments updated to document post-DBR signal derivation.

**Verification (2026-04-19):**

- `python -c "from engine import audit_word"` — PASS (no syntax errors)
- Live-DB query test on r68 grace: 13 terms fetched, 8 gas_flag=1, 6 som_flag=1 (sensible distribution matching mti_term_flags population in M23)
- Sample verification: G5485 (charis) gas=1 som=1; G5487 gas=1 som=0 — as expected

**Not blocking anymore.** Full end-to-end audit_word re-run can now proceed; recommended to do a trial run on one registry (e.g. r1 abomination with its 14 span-filter-failure cases) before bulk reprocess of the 6 reset words.

---

## Task OT-DBR-002 — `engine/audit.py` update

**Status:** **RESOLVED — 2026-04-19** (session 5)

**Source:** Phase D script update sweep

**Context:**

`engine/audit.py` references `somatic_link` and `god_as_subject` in the `_WR13_EXCLUDED_FIELDS` set (undocumented-null check exclusions). These are string literals not column reads, so the check doesn't break — it just quietly no-ops on columns that no longer exist.

**Priority:** HIGH (audit checks run post-audit_word).

**Resolution (2026-04-19):**

- Removed `"god_as_subject", "somatic_link"` from `_WR13_EXCLUDED_FIELDS` (lines 272–277).
- Added comment pointing to M24 migration + mti_term_flags location.
- `python -c "from engine import audit"` — PASS.

No other references in audit.py needed attention. Both HIGH-priority DBR tasks now clear.

---

## Task OT-DBR-003 — `scripts/apply_session_patch.py` applicator extensions (PROSE patch type + operations)

**Status:** PARTIAL — raised 2026-04-19 at Phase D

**Source:** Phase D.6

**Context:**

Prose store design requires 7 new operation types in the applicator:

- `insert` on `prose_section`
- `supersede` on `prose_section`
- `delete` on `prose_section` (soft-delete)
- `approve` on `prose_section` (status transition)
- `bulk_supersede` on `prose_section` (programme-wide)
- `session_a_replace` on `prose_section` (in-place UPDATE exception per RD from Session A advice Q5)
- `insert` on `prose_section_dimension_link` and `prose_section_finding_link`

Plus `PROSE` patch type handler in the `_patch_meta` dispatch.

**Also still open (from CLAUDE.md §3.3 pre-existing gaps):**

- `update` on `wa_session_research_flags`
- `insert` on `wa_dimension_index`
- `SDPOINTERS` exempt patch type

**Missing capability:**

CC can edit the applicator file, but extending it with 7 new operations + proper test coverage is a coherent engineering task. Can be done as a dedicated session rather than mid-phase.

**Priority:** MEDIUM — needed before prose writes begin (which is post-Phase F anyway). Session A extract generator will emit PROSE patches.

---

## Task OT-DBR-004 — `scripts/build_dimension_extract.py` update for wa_dimension_index simplification

**Status:** OPEN — raised 2026-04-19 at Phase D

**Source:** Phase D.4

**Context:**

`build_dimension_extract.py` reads `wa_dimension_index` columns that no longer exist (mti_term_id, group_code, strongs_number, transliteration, gloss, language, owning_registry_word, context_description) — 8 dropped columns per M25.

Needs join-based rewrite:

- `mti_term_id` → JOIN `verse_context_group vcg ON vcg.id = wdi.verse_context_group_id`, read `vcg.mti_term_id`
- `group_code` → `vcg.group_code`
- `strongs_number`, `transliteration`, `gloss`, `language`, `owning_registry_word` → further JOIN `mti_terms mt ON mt.id = vcg.mti_term_id`
- `context_description` → `vcg.context_description`

**Priority:** MEDIUM (dimension review work is active; script is used per CLAUDE.md Common Operations).

---

## Task OT-DBR-005 — `scripts/word_full_extract.py` update

**Status:** OPEN

**Source:** Phase D.4

**Context:** Reads `somatic_link` and `god_as_subject`. Same join-rewrite pattern as audit_word.py.

**Priority:** LOW (used for ad-hoc CSV exports; not on the critical path).

---

## Task OT-DBR-006 — Redundant script archival per Q4

**Status:** RESOLVED-PARTIAL — completed during Phase D.5 of this session (see below)

**Source:** Phase D.5 per Q4 researcher decision

**Scripts moved to `archive/scripts/`:**

*(recorded after archival step completes this session — see Phase D change log)*

Candidates flagged for archival:

- `scripts/_analyse_term_inventory.py` — diagnostic on dropped columns; purpose moot
- `scripts/_repair_04_wa_term_inventory.py` — repair script for columns that no longer exist
- `scripts/_repair_09_mti.py` — repair script referencing dropped `mti_terms.status_note`
- `scripts/_preflight_validate.py` — uses dropped columns for validation
- `scripts/_extract_word_terms.py` — 3-phase extract pipeline; superseded by single-pass word_study_extract.py; also references dropped cols
- `scripts/_explore_soul_step_routes.py` — one-off exploration; references dropped status_note
- `scripts/_exploratory_sessionb_export_v1_20260415.py` — spec v1.1 extract; references dropped cols; superseded by build_complete_extract.py for post-migration

Not archived (leave in place):

- `engine/gap_fill.py`, `engine/new_word.py` — marked "superseded, retained for reference" in CLAUDE.md §4. Still referenced; leave alone.
- `scripts/apply_session_patch.py` — active applicator; update required (OT-DBR-003) not archive.
- `scripts/_update_reference_doc.py` — broader utility; may still be useful for other operations.

---

## Task OT-DBR-007 — `Workflow/schema/create_tables.sql` consumer validation

**Status:** OPEN

**Source:** Phase D regression testing

**Context:**

`create_tables.sql` was regenerated from the post-migration DB copy. Scripts that read/parse this file to generate schema-aware artefacts need to be re-run to confirm they handle the new shape:

- `scripts/export_database_schema.py` — produces JSON schema report
- Any script that reads DDL to generate DBML or similar

**Priority:** LOW — these are read-only; if they break they're silent (produce incorrect docs) rather than blocking.

---

## Task OT-DBR-008 — M26b follow-on migration to actually apply CHECK constraints

**Status:** OPEN

**Source:** Phase C/E

**Context:**

M26 was pre-check only. All 8 controlled-vocabulary columns confirmed clean (no violators). The actual CHECK constraint application requires SQLite's table-rebuild pattern (CREATE new TABLE with CHECK; INSERT-SELECT data; DROP old; RENAME; recreate indexes). This is non-trivial per table.

**Priority:** LOW — no active data issue; strengthening only. Defer to next Change Plan revision.

---

## Task OT-DBR-009 — `mti_terms` duplication cleanup (programme-wide)

**Status:** OPEN — raised 2026-04-19 session 5 (during r68 sweep trial)

**Source:** r68 grace sweep trial — XREF Path 1 findings surfaced that the pilot was targeting deprecated duplicate rows, not canonical entries.

**Context:**

Investigation during the r68 readiness sweep revealed that `mti_terms` carries significant **within-table duplication** that predates the DB-wide review:

| Metric | Value |
|---|---|
| Total `mti_terms` rows | 7,571 |
| Distinct `strongs_number` | 3,955 |
| Avg rows per strongs | 1.91 |
| Strongs with 1 row (clean) | 2,175 |
| Strongs with duplicates (2+ rows) | 1,780 (45%) |
| NULL-status rows | 2,276 |
| 'delete' status rows | 2,611 |
| `xref_*` status rows | **4** (design expected thousands) |

**Per-strongs pattern** (sample for `H2603A` from r68 XREF):

- 1 canonical row: `status='extracted'`, owned by r111 mercy
- 3 'delete' rows with no owning registry
- 1 NULL-status row

The canonical row is a valid XREF target. The other 4 rows are legacy artefacts from prior registrations / deletions / data imports that were never cleaned up.

**Why this matters for the sweep:**

The pilot's XREF Path 1 logic was targeting the NULL-status duplicate row with a proposal to set it to `xref_[word]`. This would have:

- **Not fixed anything** — the XREF relationship was already intact via the canonical `extracted` row in another registry
- **Polluted the schema** — created yet another non-canonical row

Plus two XREF terms in r68 (ti_ids 5590, 5591 — strongs H2606, H2433) have **no canonical row at all** — all 5 rows are either NULL or 'delete'. Those are genuinely broken XREF pointers.

**Required resolution:**

A dedicated migration (likely M29 or M30) to:

1. Identify the canonical row per strongs (status IN ('extracted','extracted_thin') if it exists, else the most recent non-delete)
2. Mark duplicates for merge / hard-delete
3. For XREF terms lacking a canonical (like H2606, H2433 cases): investigate whether the cross-reference is still valid; either restore or delete the wa_term_inventory XREF row
4. Backfill the `xref_[owning_word]` status values on rows used as XREF pointers (4 rows currently; should be ~1,470 per dimensions extract)

**Scope:** ~1,780 strongs need consolidation; ~3,600 rows to review/retire. Big enough to warrant its own Change Plan revision.

**Missing capability:**

CC can do the mechanical cleanup, but the decision of which row is canonical for edge cases (e.g. 2 `extracted` rows for same strongs) requires researcher direction. Raise as researcher decision item per strongs with ambiguity.

**Priority:** **HIGH (newly added)** — gates any future Path 1 patch that touches XREF or cross-registry mti_terms logic. Sweep can proceed (skipping Path 1 XREF patches) in the interim.

**Immediate workaround for sweep runs:**

Until OT-DBR-009 resolves, sweep pilot/runner should NOT emit Path 1 operations for XREF `mti_terms.status = NULL` findings. Those findings should be reclassified to Path 4 with reference to OT-DBR-009.

---

## Task OT-DBR-010 — Sweep pilot / runner XREF join correction

**Status:** **RESOLVED — 2026-04-19** (session 5 late)

**Source:** Same r68 trial

**Context:**

`scripts/readiness_sweep_pilot.py` Phase R.B uses `LEFT JOIN mti_terms ON mt.strongs_number = ti.strongs_number` WITHOUT filtering for canonical row. With mti_terms duplication (OT-DBR-009), this joins produce duplicate findings per term.

For each of the 7 r68 XREF ti_ids, the pilot emitted:

- 1 Path 1 "mti_terms.status=NULL" finding (against the NULL duplicate)
- 1 Path 4 "OWNER term has status='extracted'" finding (against the canonical — spurious)

**Fix (when mti_terms is cleaned up):**

Filter join to canonical row only:

```sql
LEFT JOIN mti_terms mt
  ON mt.strongs_number = ti.strongs_number
  AND mt.status IN ('extracted','extracted_thin')
  -- or WHERE mt.delete_flagged = 0 post-cleanup
```

**Alternative (pre-cleanup workaround):**

Filter to pick the "most relevant" row: one with an `owning_registry_fk` set, or status not NULL/'delete'.

**Priority:** MEDIUM — affects diagnostic accuracy but not critical until Path 1 patches are being auto-applied.

**Resolution (2026-04-19 session 5 late):**

- Rewrote the XREF section of `phase_rb_terms` in `scripts/readiness_sweep_pilot.py` — replaces naive `LEFT JOIN mti_terms ON strongs_number` with an EXISTS subquery that checks for a canonical row (`status IN ('extracted','extracted_thin')` with `owning_registry_fk IS NOT NULL AND != [this_registry]`).
- XREF findings collapse to a single Path 4 RD per truly-broken pointer (no canonical row), replacing the previous 2–3 spurious findings per ti_id.
- Verification on r68: 15 findings → 6 findings; 7 spurious Path 1 eliminated; remaining 3 Path 4 broken XREFs (ti_ids 5590, 5591, 5593) are genuine.
- Programme-wide re-scan (same session): total findings **14,284 → 7,411 (−48%)**; Path 1 **6,398 → 179 (−97%)**; clean-candidate registries 1 → 5.
- Scorecard v2 produced: `outputs/reports/wa-global-readiness-scorecard-v2-20260419.md` supersedes v1.

**No longer blocking.** Full sweep runner can safely operate on XREF-bearing registries.

---

## Task OT-DBR-011 — Sweep pilot `SMALL_VERSE_SAMPLE` classifier misuse

**Status:** OPEN — raised 2026-04-20 (Action Q investigation)

**Source:** Action Q Path 1 investigation — `research/investigations/action-q-path1-investigation-20260420.md`

**Context:**

`scripts/readiness_sweep_pilot.py:243–254` emits Path 1 findings proposing `INSERT SMALL_VERSE_SAMPLE` quality flags based on a **ratio** trigger (`occ > 20 AND active < occ * 0.2`). But the canonical writer in `engine/flag_engine.py:158–168` uses an **absolute** trigger (`confirmed_verses < 5`). Applying the pilot's 135 Path 1 findings would insert `SMALL_VERSE_SAMPLE` flags on terms that don't meet the flag's documented definition — semantic corruption.

**Scope:** 135 spurious Path 1 findings across ~80 registries from programme scan 2026-04-19.

**Recommended resolution:**

1. Remove the ratio-based Path 1 emitter for `SMALL_VERSE_SAMPLE`, or
2. Introduce a new flag code (e.g. `LOW_CAPTURE_RATIO`) with its own definition in `wa_quality_flag_types` + flag_engine support, or
3. Reclassify the ratio-based finding as Path 4 (researcher disposition — does it affect analytical confidence?)

Option 1 is simplest and safest. Can address the diagnostic via a read-only report rather than a DB flag.

**Priority:** MEDIUM — blocks Action Q completion; no active corruption because the 135 items weren't applied.

---

## Task OT-DBR-012 — Sweep pilot `dominant_subject='NONE'` misclassified as Path 1

**Status:** OPEN — raised 2026-04-20 (Action Q investigation)

**Source:** Action Q Path 1 investigation

**Context:**

`scripts/readiness_sweep_pilot.py:330–334` emits 44 Path 1 findings for `wa_dimension_index.dominant_subject = 'NONE'` with action "derive from context_description". But deriving a HUMAN/GOD/OTHER_HUMAN/UNSEEN classification from prose is semantic work, not mechanical — identical to what Claude AI does in Dimension Review. Spot-check on r23 compassion (5 groups) confirmed: correct subject is derivable only by reading context_description prose, not by string match.

**Scope:** 44 spurious Path 1 findings across ~17 registries.

**Recommended resolution:**

- Change pilot classifier to **Path 2** (directive: Dimension Review re-evaluation of `NONE` subjects), OR
- **Path 4** (RD: researcher dispositions each case)

Path 2 is more scalable — batch the 44 into a single DimReview sub-directive.

**Priority:** MEDIUM — blocks Action Q; no active corruption because items weren't applied.

---

## Task OT-DBR-013 — Full audit of sweep pilot Path 1 classifier sites

**Status:** OPEN — raised 2026-04-20 (follow-on from OT-DBR-011/012 pattern)

**Source:** Pattern recognition — 3 Path 1 misclassifications discovered in 2 days (OT-DBR-010 + 011 + 012)

**Context:**

Three independent pilot Path 1 misclassifications have now been caught by manual investigation before patch assembly. The pilot's "Path 1 = mechanical" claim is not uniformly reliable. A systematic audit of every `path=1` emitter site in the pilot is warranted.

**Missing capability:** CC can do the audit. Ideally after OT-DBR-011/012 are fixed so the audit has a clean baseline.

**Priority:** LOW — preventative; no active issue. Schedule after OT-DBR-009 dedup work.

---

## Task OT-DBR-014 — `prose_section_type` Session A seed label mismatch (chapters 3/4)

**Status:** OPEN — raised 2026-04-20 (Action S build)

**Source:** Action S — Session A extract generator build

**Context:**

The Session A advice (approved 2026-04-19) specifies in §5:

- Chapter 3 = Terms (OWNER + XREF with analytical metadata)
- Chapter 4 = Verses (group-first rendering)

The live DB seed (from M20 migration) has these swapped:

| id | code | chapter_no | label (current) | Should be |
|---|---|---:|---|---|
| 3 | sa_s1_d3 | 3 | `Session A — Verses` | `Session A — Terms` |
| 4 | sa_s1_d4 | 4 | `Session A — Terms` | `Session A — Verses` |

**Impact:**

- No active corruption: no Session A prose rows exist yet; seed was the initial state
- Action S generator was made robust to the mismatch (matches section types by label keyword rather than chapter_no), so output is correct regardless
- But the seed should still be corrected so `sort_order` / `chapter_no` semantics align with design ordering

**Options:**

1. **Swap labels**: `id=3` label → "Session A — Terms"; `id=4` label → "Session A — Verses". Labels describe content; chapter_no stays intact. Codes (sa_s1_d{n}) become meaningless positional identifiers.
2. **Swap chapter_no + sort_order**: `id=3` stays labelled "Verses" but chapter_no → 4; `id=4` stays labelled "Terms" but chapter_no → 3. Codes remain positionally meaningful but slight complication.
3. **Leave as-is**: Accept that chapter_no/sort_order do not reflect semantic order. Ugly.

Recommend Option 1 — cleanest and aligns labels with content.

**Why CC cannot auto-apply:**

Modifying a catalogue/seed row without explicit researcher approval violates the stop-the-line rule for shared reference tables. Requires researcher direction + approval for the label swap. Small enough to apply via direct SQL UPDATE (no schema change, no migration).

**Priority:** LOW — no operational blocker; generator workaround is in place. Should be corrected for cleanliness before broader Session A rollout.

---

## Task OT-DBR-015 — Dimension-vocabulary vintage mismatch (programme-wide)

**Status:** OPEN — raised 2026-04-20 (C01 DimReview Phase A)

**Source:** Claude AI Phase A observations log `wa-dim-c01-observations-v1_0-20260420.md` — confirmed by CC pre-check DV-1 in `wa-dim-C01-handoff-kickoff-v1-20260420.md`

**Context:**

Claude AI's Phase A on C01 revealed that **265 of 275** active groups in the cluster carry dimension labels from a **legacy vocabulary** that does not exist in the current §7.7 controlled vocabulary (`wa-reference-v5_7` / DimReview instruction v3.3).

**Pattern confirmed:** anchored groups (manual_override=1) carry legacy labels; unanchored groups (manual_override=0) carry current labels. This matches the history — legacy labels were the working vocabulary when those registries were reviewed under earlier instruction versions.

**Legacy labels in use (C01 sample):**

| Legacy label | C01 count | Proposed mapping |
|---|---:|---|
| `Moral/Conscience` | 57 | `Moral Character` (majority) / `Cognition` |
| `Theological/Divine-Human` | 55 | `Divine-Human Correspondence` |
| `Affective/Emotional` | 37 | `Emotion — Positive` / `Emotion — Negative` (per-group split) |
| `Spiritual/God-ward` | 25 | **no clean mapping** — new-dimension candidate |
| `Cognitive/Mind` | 23 | `Cognition` |
| `Character/Disposition` | 17 | `Moral Character` / `Relational Disposition` |
| `Volitional/Will` | 15 | `Volition` |
| `Relational/Social` | 14 | `Relational Disposition` |
| `Identity/Selfhood` | 9 | **no clean mapping** — new-dimension candidate |
| `Volitional/Capacity` | 7 | `Agency / Power` |
| `Somatic/Embodied` | 6 | **no clean mapping** — new-dimension candidate |

Three labels (`Spiritual/God-ward`, `Identity/Selfhood`, `Somatic/Embodied`) have NO clean counterpart in the current vocabulary and may warrant new §7.7 dimensions.

**Scope:** Likely programme-wide. C01 is a sample; needs a full programme scan across all 22 clusters.

**Recommended resolution paths:**

- **Option A** — Leave as-is. Accept permanent vintage heterogeneity. Cross-cluster analysis navigates both sets.
- **Option B** — Author a legacy→current mapping; data-migrate existing rows. Where no clean mapping exists, add new §7.7 dimensions OR redistribute.
- **Option C** — Keep legacy rows annotated with a `vocabulary_vintage` marker; distinguish in queries.

CC recommendation: **Option B** with the three unmapped legacy labels triaged as candidates for new dimensions. Requires design effort.

**Priority:** MEDIUM — not blocking current DimReview target work (r112 + r183 use current vocab for their own assignments), but blocks cross-cluster analytical coherence and future programme-wide operations.

**Next actions:**

1. Programme scan: count legacy labels across all 22 clusters
2. Researcher decision on Option A/B/C
3. If B: design mapping + migration; raise new §7.7 dimensions

---

## Task OT-DBR-016 — Rootfamily extractor over-reports cross-registry roots

**Status:** OPEN — raised 2026-04-20 (C01 DimReview Phase A)

**Source:** Claude AI Phase A observations — 3 of 5 reported cross-registry roots in C01 rootfamily extract (AT, YATSA, TAAM) identified as string-match artefacts rather than semantic clusters.

**Context:**

`scripts/build_dimension_extract.py --rootfamily={cluster}` produces cross-registry root lists. Phase A found the extractor over-reports — specifically, it treats roots with NULL `root_language` AND NULL `root_gloss` metadata as cross-registry links without verifying semantic cohesion.

**Two distinct signals surfaced:**

1. **False positives from NULL metadata** — e.g. `AT` (Hebrew pronoun forms vs. "mutterer" term); `YATSA` (offspring vs. come-out). DV-4 pre-check catches these (28 found in C01).
2. **False positives WITH metadata** — e.g. `TAAM` carrying `root_language='Hebrew' root_gloss='delicacy'` but linking a perceive-verb to a be-double-verb via string-match coincidence. DV-4 does NOT catch these.

**Secondary finding:** some NULL-metadata roots are GENUINE (e.g. `LEV`, `KARDIA`, `PSUCHĒ`, `SARX`) — just missing the language/gloss fields. DV-4 cannot distinguish legitimate-with-incomplete-metadata from string-match-artefact without semantic inspection.

**Recommended resolution:**

- Phase 1 (easy): Add a "cross-registry root quality" column on the rootfamily extract output: `cross_registry_confidence` = HIGH (metadata complete + semantic sanity) | MEDIUM (metadata complete, unchecked) | LOW (NULL metadata).
- Phase 2 (harder): When extracting, check basic semantic sanity — e.g. require at least 2 terms from different registries to share morphological root skeleton AND have glosses within the same domain-tag space.
- Phase 3 (later): Backfill NULL root_language / root_gloss fields on legitimate roots identified via Phase A cycles.

**Priority:** LOW-MEDIUM — affects DimReview signal quality but not data integrity. Phase A semantic inspection remains effective as the definitive filter.

---

## Summary

Updated 2026-04-19 session 5 after OT-DBR-001 + OT-DBR-002 rewrite work.

Updated 2026-04-19 session 5 late (post OT-DBR-010 fix + programme re-scan).

Updated 2026-04-20 Action Q investigation (OT-DBR-011, 012, 013 raised).

Updated 2026-04-20 Action S build (OT-DBR-014 raised — seed label mismatch).

Updated 2026-04-20 evening (Action Q closed — OT-DBR-011 absorbed into M29). Updated 2026-04-20 late (C01 Phase A incoming — OT-DBR-015 + OT-DBR-016 raised).

| Priority | Count | Items |
|---|---|---|
| HIGH | 1 | OT-DBR-009 (mti_terms deduplication migration) |
| MEDIUM | 0 | — (all resolved 2026-04-19) |
| LOW | 3 | OT-DBR-005, OT-DBR-007, OT-DBR-008 |
| RESOLVED | 7 | OT-DBR-001, OT-DBR-002, OT-DBR-003, OT-DBR-004, OT-DBR-006, OT-DBR-010, RD-DBR-004 |

**Effect on sweep and Phase F.6 reprocess:**

**FULLY UNBLOCKED** as of session 5 late.

- `audit_word.py` + `audit.py` rewritten for post-DBR schema (OT-DBR-001/002) — trial run on r1 abomination verified behaviour parity
- Applicator extended with PROSE + 3 pre-existing gaps closed (OT-DBR-003) — enables sweep remediation patches of any type
- `build_dimension_extract.py` updated with post-DBR joins (OT-DBR-004) — C01 extract production verified
- RD-DBR-004 disposed (r27 + r129 flags reset to NULL)
- Pilot XREF join fix (OT-DBR-010) — eliminated 6,200 spurious Path 1 findings; programme scan now reliable

**Remaining HIGH-priority blocker:**

- **OT-DBR-009** (mti_terms deduplication) — still open. Affects ~45% of strongs with duplicate rows. Not blocking the sweep (post OT-DBR-010 fix surfaces only genuine broken XREFs) but necessary for long-term schema cleanup. Scheduled as a dedicated Change Plan revision / migration M29+.

**Programme state post session 5:**

- 5 BANKED registries (per scorecard v2)
- 12 STRUCTURALLY CLEAN
- 9 with Path 1 remediation candidates (179 items total — a manageable batch patch)
- 154 with sub-process directive needs
- 30 UNPROCESSED (outside sweep scope)
- 3 OTHER

---

*End of outstanding tasks v1 — 2026-04-19*
