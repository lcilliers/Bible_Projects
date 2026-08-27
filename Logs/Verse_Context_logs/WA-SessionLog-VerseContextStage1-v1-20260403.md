# Session Log — Verse Context Stage 1 Launch

**Period:** 2026-03-30 to 2026-04-03
**Participants:** le Roux Cilliers (researcher), Claude Code, Claude AI
**Scope:** CLAUDE.md upgrade, data integrity fixes, Verse Context Stage 1 batches VCB-001 through VCB-015

---

## Day 1 — 2026-03-30: Instruction Upgrade and Data Discovery

### CLAUDE.md brought to v5.5/v5.6

Read through the entire Session_B instruction suite (9 documents). Produced a full audit comparing new instructions against CLAUDE.md ([CLAUDE-MD-Update-Audit-20260330.md](../outputs/investigations/CLAUDE-MD-Update-Audit-20260330.md)). Updated CLAUDE.md with Sections 14–17 covering Verse Context operations, patch system, pool-based processing, and controlled vocabulary.

Key new references: WA-SessionB-ClaudeCode-Instructions v3.2, WA-VerseContext-Instruction v1.5, patch_specification v1.5.

### First VCB-001 attempt — stopped by Claude AI

Built VCB-001 batch and submitted to Claude AI. Claude AI correctly identified a structural problem: 262 term entries but only 122 unique mti_term_ids. Same Strong's number appearing under multiple registries all marked as OWNER.

### Root cause investigation — mti_terms duplicates

Investigation revealed two compounding problems:
1. **mti_terms had 3,616 duplicate rows** — the engine created a new row per registry extraction instead of reusing existing ones
2. **1,006 Strong's numbers marked OWNER in multiple registries** — caused by the duplication

Full investigation documented in [mti-dedup-investigation-20260330.md](../outputs/investigations/mti-dedup-investigation-20260330.md).

### Data fixes applied

- Added `delete_flagged` column to mti_terms
- Flagged 64 orphan mti_terms (no inventory reference)
- Deduplicated mti_terms: 3,616 rows flagged (survivor selected by field population score)
- OWNER/XREF fix: 1,871 excess OWNERs flipped to XREF, 48,237 XREF verses delete_flagged
- Backfilled all NULL `owning_registry_fk` (1,373 rows)
- Set `status = 'extracted'` for 810 NULL-status terms with active verses
- Fixed NULL `owning_word` (1), `extraction_date` (538), `word_analysis_gloss` (16), `occurrence_count` (1)

Google Drive sync caused DB lock contention throughout — resolved by copying DB to local temp, applying fixes, copying back.

### Engine guard

Updated `audit_word.py` to prevent future duplicates: both `_insert_new_term` and MISSING_MTI stream now check for existing mti_terms before inserting. Also added `owning_registry_fk` to new inserts and `word_analysis_gloss` to stale field refresh list.

### Schema and constants

Updated `engine/constants.py` EXPECTED_SCHEMA_VERSION from 3.7.0 to 3.8.0 to match the database.

---

## Day 1-2 — VCB-001 through VCB-005

Rebuilt VCB-001 with clean data. Second attempt still had issues — the batch query wasn't filtering on `mt.delete_flagged = 0`, allowing deleted mti rows to pass through. Fixed and rebuilt successfully.

Claude AI raised a further issue: duplicate verses (Php vs Phili reference format). Confirmed these were superseded records correctly marked `verse_delete_flagged = 1` in the JSON — working as designed.

VCB-001 through VCB-005 applied. 34 registries reached Complete.

### apply_session_patch.py upgrades

- Added verse_context_group and verse_context insert/update handlers
- Added group_code → integer ID resolution via `last_insert_rowid()`
- Added `_resolve_group_id()` function handling both direct group_codes and `integer_id_` placeholder patterns
- Fixed `session_b_status` exemption logic for VC patch types (including DIFFERENTIAL and SUPPLEMENTAL sub-types)
- Added duplicate verse_context insert handling (skip with warning instead of failing)
- Fixed Unicode box-drawing characters in print statements (cp1252 encoding)

---

## Day 2 — 2026-03-31: VCB-006 through VCB-008, Reports, Filing

### Verse Context batches

VCB-006 through VCB-008 applied. VCB-004 had 2 orphan verse_context records (Psa 51:6 under H2654A/B) — resolved by delete_flagging the duplicates. VCB-006 received a differential correction patch for H7451A.

### Word report script

Built `_produce_vc_word_report.py` — generates .docx reports per registry showing terms organised by Strong's root, with sub-glosses nested, meaning senses, stems, LSJ data, verse context groups with full anchor/related/set-aside verse text. Produced reports for all completed registries.

### File organisation

Published [file-organisation-rules.md](../docs/file-organisation-rules.md). Reorganised outputs/: created reports/programme/, reports/words/, investigations/. Moved all misplaced files. Removed empty csv/ and markdown/ folders. Updated report scripts to use correct paths.

### VC Instruction updates

Tracked VC instruction through v1.7, v1.8, v1.9, v2.0, v2.1, v2.2. Updated `_build_vc_batch.py` version references each time. Changes were primarily Claude AI-side (session discipline, file writing rules, particle filter criterion, all-verses-fail expansions).

---

## Day 3 — 2026-04-01: VCB-009 through VCB-011, H5207 Fix

### VCB-009 — deferred term

VCB-009 included a deferred term: H4480A min- (284 verses) excluded pending full individual inspection. Applied without issues.

### H5207 data error

Claude AI found John 1:18 (NT Greek verse) linked to H5207 (Hebrew term, "soothing aroma"). Confirmed as STEP extraction artefact — numeric collision between H5207 and G5207 (monogenes). Delete_flagged the spurious verse record.

### VCB-010 and VCB-011

Applied. Justice (reg 98) completed in VCB-011. Kindness (reg 99) split across VCB-011/VCB-012.

---

## Day 4 — 2026-04-02: VCB-012 through VCB-014, Verification, Analysis

### VCB-012 + H2617A supplemental

VCB-012 applied. H2617A (chesed) received a supplemental patch classifying 223 remaining verses. Required fix to `apply_session_patch.py` exemption logic for `VERSECONTEXT-SUPPLEMENTAL` patch type.

### VCB-009 state verification — false alarm resolved

Claude AI issued instruction wa-vcb-009-claudecode-instruction-v1 requesting verification of flagged terms. Investigation found 36 "unclassified" terms — but 35 had `mti_terms.status = 'delete'`, correctly excluded from Verse Context. The verification query was missing the `mt.status IN ('extracted', 'extracted_thin')` filter.

5 registries were incorrectly reverted to In Progress and then restored to Complete. Registry 89 (iniquity) showed as a discrepancy in v2 instruction but was correctly Complete — H4480A had been classified in VCB-010 after being deferred from VCB-009.

**Lesson:** Verification queries must always include the status filter. Documented the correct template in the v2 instruction.

### VCB-013 — anomaly resolution

Claude AI identified two anomalies:
1. **G4894 (mti:454) in reg 26 (conscience)** — unclassified despite registry showing Complete. Confirmed: registry was incorrectly marked Complete (1 term missed). Reverted to In Progress.
2. **G4893 (suneidesis, mti:53) in reg 73 (guilt)** — FK mismatch: mti pointed to reg 112 (mind) but OWNER ti was in reg 73. Fixed FK to point to reg 73.

VCB-013 applied successfully — 12 registries completed including conscience, counsel, desire, guilt (long-running partials finally resolved).

**Programme reached 92/181 (50.8%) — halfway mark.**

### VCB-014 — duplicate handling

VCB-014 had one internal duplicate (OP-1708 duplicated OP-1701 for verse_record_id=5897). Added try/except duplicate handling to the applicator — skips with warning instead of rolling back the entire transaction. Applied successfully with 1 skip.

### Remaining work analysis

Produced [vc-remaining-work-analysis-20260402.md](../outputs/reports/programme/vc-remaining-work-analysis-20260402.md) analysing the verse count skew. Key finding: 71 terms (6%) with 100+ verses hold 46.6% of remaining verse load. Many are grammatical particles processable as bulk set-asides.

Researcher and Claude AI discussed but decided no significant productivity improvement from changing approach — continue standard batching.

---

## Day 5 — 2026-04-03: VCB-015, Term Explorer, Characteristic Layer Concept

### VCB-015 prepared

Built and ready for Claude AI submission.

### Term exploration script

Built `extract_term_data.py` — explores the database through the lens of a single Strong's number. Shows the term itself, every registry it connects to, and the full term/gloss landscape of each connected registry. Outputs JSON (machine-readable) with optional `--md` flag for human-readable markdown alongside.

Tested with H2734 (charah) — showed OWNER in anger, XREF in distress and wrath, with 340 sibling terms across those 3 registries.

### Characteristic layer concept

Researcher observed that verse_context_group descriptions form a proto-taxonomy of inner-being functions that cuts across registries. Documented as [characteristic-layer-concept-20260403.md](../outputs/investigations/characteristic-layer-concept-20260403.md) — a potential Layer 2 between Verse Context and Session B that would cluster context descriptions programme-wide into characteristic families. Parked for discussion when Stage 1 nears completion.

### Git commit and push

Committed all 4 days of work (295 files). Excluded `love_full_extract.csv` (1.3GB) from Git — added to .gitignore. Pushed to origin/main.

---

## Programme State at End of Session

| Metric | Value |
|--------|-------|
| Registries Complete | 97 / 181 (53.6%) |
| Batches processed | 14 + 2 supplemental/differential |
| verse_context records | ~22,000 |
| verse_context_groups | ~2,000 |
| Terms remaining | ~990 |
| Verses remaining | ~26,000 |
| Estimated batches left | ~12 |
| Data health | All checks CLEAN |
| Schema | v3.8.0 |
| VC Instruction | v2.3 |

---

## Key Decisions

1. **mti_terms dedup approach:** Survivor selected by field population score, then verse count, then lowest ID. No analytical judgement required.
2. **OWNER assignment rule:** Where mti FK was set and matched a registry, that registry is OWNER. Otherwise lowest registry number. Deterministic and stable.
3. **Particle triage:** Discussed but deferred — no significant throughput improvement from changing batch approach.
4. **Characteristic layer:** Concept documented for future discussion. Not a current pipeline stage.
5. **Verification queries:** Must always include `mt.status IN ('extracted', 'extracted_thin')` filter to avoid false positives from delete-status terms.

---

## Open Items

- VCB-015 built, awaiting Claude AI classification
- `vc-report-116-patience` could not be regenerated due to file lock — needs retry
- Characteristic layer concept parked for ~80% Stage 1 completion
- `love_full_extract.csv` excluded from Git (too large) — retained locally

---

*WA-SessionLog-VerseContextStage1-v1-20260403.md | Covers 2026-03-30 through 2026-04-03*
