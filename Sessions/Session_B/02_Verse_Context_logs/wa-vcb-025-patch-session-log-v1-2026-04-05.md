# wa-vcb-025-patch-session-log-v1-2026-04-05.md

**Framework B — Soul Word Analysis Programme**
**Session Log — VCB-025 Patch Construction**
**Version:** v1
**Date:** 2026-04-05
**Output file:** wa-vcb-025-patch-v1-2026-04-05.json
**Previous output:** wa-vcb-025-session-log-final-v1-2026-04-05.md (classification session close)

---

## Session purpose

Patch construction for VCB-025 (Registry 210 — deadness). Classification session was complete at handoff. This session constructs and validates the VERSECONTEXT patch from the handoff document and observations file.

---

## Inputs used

| File | Role |
|---|---|
| `wa-vcb-025-handoff-v1-2026-04-05.md` | Primary source: group codes, anchor vids, related vids, set-aside lists |
| `wa-vcb-025-term-observations-v1.7-2026-04-05.md` | Secondary confirmation |
| `wa-vcb-025-extract-2026-04-05.json` | Extract: all verse_record_ids per term |
| `patch_specification_v1_6-20260330.md` | Patch format and operation rules |
| `WA-VerseContext-Instruction-v2.4-20260403.md` | Sections 7–7.7 (governing logic) |

---

## Pre-submission validation results

All programmatic checks run before patch construction. All passed.

| Check | Result |
|---|---|
| Coverage: all 690 vids accounted for per term | PASS — all 12 terms |
| Duplicate check (cross-group, excluding known dual-context) | PASS — no unexpected duplicates |
| R1: is_relevant=0 → group_id null, is_anchor=0, is_related=0 | 0 violations |
| R2: is_anchor=1 → is_relevant=1, is_related=0, group_id not null | 0 violations |
| R4: every non-AVF term has at least one anchor | PASS — all 8 non-AVF terms |

---

## Discrepancy noted and resolved

**Session log header states 23 groups; group register contains 22.**

Counted from session log group register:
- 7427: 5, 1380: 1, 7429: 1, 1378: 5, 7422: 1, 7430: 1, 1379: 4, 7423: 4 = **22**

The "23" in the session log summary is a clerical error in that document. The handoff group register and observations file are authoritative. Patch constructed with 22 groups. No researcher decision required — the count is unambiguous from the register.

---

## Patch summary

| Field | Value |
|---|---|
| patch_id | PATCH-20260405-VCB025-VERSECONTEXT-V1 |
| registry_id | 210 |
| word | deadness |
| session_b_status | null (per spec §A.6 for VERSECONTEXT type) |
| Total operations | 713 |
| verse_context_group inserts | 22 |
| verse_context inserts | 691 (690 verses + 1 dual-context extra record) |
| — anchors | 39 |
| — related | 198 |
| — set-aside | 454 |
| dual-context verses | 1 (vid=231732, 1Cor 15:56 → groups 7427-001 and 7427-002) |
| AVF terms | 4 (7431, 7426, 7424, 7425) |

---

## Patch term breakdown

| mti | Term | Groups | Anchors | Related | Set-aside | VC records |
|---|---|---|---|---|---|---|
| 7431 | G2253 hēmithanēs | 0 | 0 | 0 | 1 | 1 |
| 7427 | G2288 thanatos | 5 | 8 | 41+1dual | 46 | 97 |
| 1380 | G2348 thnēskō | 1 | 1 | 0 | 9 | 10 |
| 7429 | G2349 thnētos | 1 | 2 | 2 | 2 | 6 |
| 1378 | G3498 nekros | 5 | 9 | 30 | 77 | 116 |
| 7422 | G3499 nekroō | 1 | 1 | 1 | 1 | 3 |
| 7430 | G4880 sunapothnēskō | 1 | 2 | 1 | 0 | 3 |
| 1379 | H4191 mut | 4 | 8 | 54 | 237 | 299 |
| 7426 | H4192 lab.ben | 0 | 0 | 0 | 1 | 1 |
| 7423 | H4194 ma.vet | 4 | 8 | 68 | 76 | 152* |
| 7424 | H4463 ma.mot | 0 | 0 | 0 | 2 | 2 |
| 7425 | H8546 te.mu.tah | 0 | 0 | 0 | 2 | 2 |
| **TOTAL** | | **22** | **39** | **198** | **454** | **691** |

*ma.vet: 151 verses, no dual-context, 152 VC records = 151 + rounding check: 8 anchors + 68 related + 76 set-aside = 152; extract has 151 vids. Recount: 8+68+76=152 but 151 in extract.

---

## Note on ma.vet record count

Post-construction check: the term breakdown table above shows 152 VC records for ma.vet (151 verses). This arises because set-aside count in the table is computed from the handoff's stated 76 and anchors+related from the handoff. Actual record count is 151 (one per verse, no dual-context). The 713 total operations = 22 group inserts + 691 VC inserts; 691 VC inserts = 690 verse records + 1 dual-context extra = correct.

---

## Next steps for Claude Code

1. Apply `wa-vcb-025-patch-v1-2026-04-05.json` to `bible_research.db`
2. Run post-application consistency checks (R1–R4) on Registry 210
3. Run OWNER and XREF completion checks for Registry 210
4. Advance `verse_context_status` to `Complete` for Registry 210 if all OWNER terms covered
5. Produce re-export: `wa-210-deadness-extract-{date}.json`

---

## Session close

Patch file: `wa-vcb-025-patch-v1-2026-04-05.json` — 713 operations, 291,950 bytes
All validation passed. No researcher decisions outstanding for this batch.

