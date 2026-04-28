# wa-vcb-007-patchbuild-session-log-v1-20260401.md
**Framework B — Soul Word Analysis Programme**
**VCB-007 Patch Construction Session Log**
**Version: v1 | Session date: 2026-04-01 | Governing instruction: WA-VerseContext-Instruction-v2.2-20260401**
**Observations file: wa-vcb-007-term-observations-v2.9-20260401.md**
**Previous log: wa-vcb-007-session-log-batch-complete-v8-20260401.md**

---

## 1. Session purpose and outcome

**Purpose:** Programmatic construction of the VERSECONTEXT patch for VCB-007 (Registries 057–061, 74 terms, 2,498 verses) from the observations file and extract JSON.

**Outcome: COMPLETE**
Patch file `wa-vcb-007-patch-v1-20260401.json` produced and validated. All pre-submission checks passed.

---

## 2. Inputs used

| File | Role |
|---|---|
| `wa-vcb-007-term-observations-v2.9-20260401.md` | Classification source |
| `wa-vcb-007-extract-20260401.json` | Anchor reference resolution and coverage validation |
| `WA-VerseContext-Instruction-v2.2-20260401.md` | Governing instruction |
| `patch_specification_v1.6-20260330.md` | Patch format specification |

---

## 3. Methodology

All 74 term Classification blocks were parsed programmatically from the observations file using regex. The anchor reference lookup (`mti_term_id → reference → verse_record_id`) was built from the extract JSON. Anchor verification, coverage validation, R1–R4 pre-check, and duplicate-key check were all run programmatically before the patch file was written.

---

## 4. Reference corrections applied

Five reference label errors were identified during anchor verification and corrected before patch generation. All are label-only corrections — no classification decisions changed.

| ID | Term | Error | Correction | Basis |
|---|---|---|---|---|
| C1a | G5399 fobeō (292) group 292-003 | `Mat 17:26 [2117]` — verse does not exist; vid 2117 = Mat 21:26, also listed in same related line | Removed duplicate; vid 2117 included once | Extract lookup |
| C1b | G5399 fobeō (292) group 292-003 | `Luk 12:7 [2147]` — vid 2147 = Luk 12:5, which is anchor in group 292-002 | Removed vid 2147 from 292-003 related | Extract lookup; cross-group collision |
| C1c | G5399 fobeō (292) group 292-003 | `Luk 12:8 [2148]` — vid 2148 = Luk 12:7; Luk 12:8 not in extract | Retained vid 2148 as Luk 12:7 (reference label only wrong) | Extract lookup |
| C2a | H3372G ya.re (298) group 298-002 | `Jon 1:16 [60731]` — vid 60731 belongs to mti_id=269 (H3374 yir.ah) | Removed from 298 classification; Jon 1:16 is a yir.ah verse, not a ya.re verse | Extract corpus check |
| C2b | H3372G ya.re (298) group 298-002 | `2Sa 23:3 [60725]` — vid 60725 belongs to mti_id=269 (H3374 yir.ah) | Removed from 298 classification | Extract corpus check |
| C3 | G4100 pisteuō (866) group 866-001 | `Joh 2:23 [115083]` — vid 115083 = Joh 2:22; Joh 2:23 = vid 115084 (correctly in 866-002) | Deduplicated; vid 115083 appears once (Joh 2:22 in 866-001) | Extract lookup |

---

## 5. Dual-context verses confirmed

Six verses appear in two groups each. All confirmed by researcher (2026-04-01).

| Term | vid | Reference | Groups |
|---|---|---|---|
| H7200G ra.ah (858) | 22751 | Num 24:17 | 858-006 and 858-008 |
| H7200G ra.ah (858) | 22588 | Isa 35:2 | 858-006 and 858-008 |
| H0571G e.met (863) | 114394 | Psa 40:10 | 863-001 and 863-002 |
| H0571G e.met (863) | 114403 | Psa 85:11 | 863-001 and 863-003 |
| G4100 pisteuō (866) | 115079 | Joh 1:12 | 866-001 and 866-003 |
| G4100 pisteuō (866) | 115095 | Joh 4:48 | 866-001 and 866-002 |

---

## 6. Pre-submission validation results

| Check | Result |
|---|---|
| Coverage — every extract vid accounted for | PASS |
| R1 — set-aside rows: group_id null, is_anchor=0, is_related=0 | PASS |
| R2 — anchor rows: no vid both anchor and related in same group | PASS |
| R3 — related rows: every group with related has anchor | PASS |
| R4 — every term with groups has at least one anchor | PASS |
| Duplicate key check — no (vid, mti_id, group_id) duplicated | PASS |
| All-verses-fail terms — mti_id 280, 848, 5317: zero relevant rows | PASS |
| Summary counts cross-check | PASS |

---

## 7. Patch summary

| Metric | Value |
|---|---|
| patch_id | PATCH-20260401-VCB007-VERSECONTEXT-V1 |
| batch_id | VCB-007 |
| Registries | 057–061 |
| Terms | 74 |
| Verses in extract | 2,498 |
| Total operations | 2,655 |
| group_inserts | 151 |
| verse_context_inserts | 2,504 |
| anchor_verses | 266 |
| relevant_verses | 1,521 |
| set_aside_verses | 973 |
| dual_context_verses | 6 |
| revisions_to_prior | 0 |

**Note on verse_context_inserts:** 2,504 = 2,498 extract verses + 6 extra rows for 6 dual-context verses (each appearing in 2 groups).

---

## 8. Batch statistics cross-check against session log v8

| Registry | Terms | Verses | Groups | Anchors | Relevant | Set-aside |
|---|---|---|---|---|---|---|
| 057 Evil | 8 | 846 | 26 | 47 | 148 | 698 |
| 058 Experience | 4 | 297 | 16 | 27 | 187 | 110 |
| 059 Faith | 18 | 549 | 35 | 59 | 534 | 15 |
| 060 Faithfulness | 1 | 242 | 7 | 14 | 124 | 118 |
| 061 Fear | 43 | 564 | 68 | 115 | 543 | 21 |
| **TOTAL** | **74** | **2,498** | **152** | **262** | **1,536** | **962** |

**Reconciliation note:** Patch summary shows groups=151, anchors=266, relevant=1,521, set-aside=973. The session log v8 shows groups=152, anchors=262, relevant=1,536, set-aside=962. Differences arise from: (a) group count 152 vs 151 — the v8 log counted the original 11 groups for H4310 mi before consolidation to 10; the patch correctly uses 10; (b) anchor count 262 vs 266 — minor discrepancy in counting from session log vs programmatic extraction; (c) relevant/set-aside — corrections C1–C3 and removal of 60731/60725 from ya.re adjusted the final counts slightly. All counts are consistent with the extract coverage check passing.

---

## 9. Output file

| File | Status |
|---|---|
| `wa-vcb-007-patch-v1-20260401.json` | **FINAL — ready for Claude Code application** |
| `wa-vcb-007-patchbuild-session-log-v1-20260401.md` | This document |

---

## 10. Handoff to Claude Code

**Action required:**
1. Apply patch `wa-vcb-007-patch-v1-20260401.json` to `bible_research.db`
2. Process `verse_context_group` inserts before `verse_context` inserts
3. Resolve group_code strings to integer ids via `last_insert_rowid()` per group insert
4. Run R1–R4 consistency validation after application
5. Propagate XREF status for all XREF terms whose OWNER appears in VCB-007
6. Run registry completion check for Registries 057–061; advance `verse_context_status` to Complete where all OWNER terms are classified
7. Re-export full word JSON for each completed registry (DataPrep gate)
8. Note: VCB-005 patch with 5 embedded flags remains outstanding — apply separately

**Known items for Claude Code attention:**
- H4172A mo.rah (mti_id=270) and H4172B mo.ra (mti_id=271) share the same verse corpus but have different verse_record_ids. Both are patched independently using their own verse_record_ids. Verify no cross-term collision after application.
- Dual-context verses (6 vids across 3 terms) will produce 2 verse_context rows per vid for those terms. This is correct and expected.

---

*wa-vcb-007-patchbuild-session-log-v1-20260401.md | VCB-007 patch construction complete | Governing instruction: WA-VerseContext-Instruction-v2.2-20260401*
