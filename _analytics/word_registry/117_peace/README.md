# R117 Peace — Session B Artefact Bundle

**Created:** 2026-05-01

**Folder layout:**

- `inputs/` — readiness output (**v10, READY**) + readiness validation (v1) + STEP discovery extract + 6 per-term Session A `.md` files for H7965 sub-forms + 2026-05-02 C17 DimReview bundle
- `obslog/` — VCNEW patch (H7965G applied) + Session B obslog v1 + sessionlog v2 from earlier (pre-recovery)
- `chapters/` — (to be populated by chapter assembler post-Analysis-Complete)

**Status (snapshot 2026-05-02):**

- VC: **Complete** · DimRev: **Complete** · session_b_status: **Analysis Complete**
- v1.8 obslog v2 captured 2026-05-02: 154 OBS findings + 28 synthesis (7 INTRA + 21 INTER) + 21 SD pointers · 187 catalogue Q&A links · 154/189 distinct v2 prompts answered
- 6 chapters assembled · 364.8 KB combined extract
- 1 open anomaly (QA_GAP — 35 prompts uncovered) · 1 archived (ANOMALY-117-001 resolved)
- Phase A prose (sa_s1_d1..d6) generated 2026-05-01 by `generate_session_a_extract.py` — patch `PATCH-20260501-SESSIONA-R117-V1`, 6 prose rows, ~105k words.

**H7965 shalom recovery — 2026-05-01** (`Sessions/Patches/wa-117-peace-h7965-recovery-v1-20260501.json`):

The H7965 sub-letter family was extracted under R117 at original Phase 1 (2026-03-17) but marked `status='delete'` in a programme-wide sweep on 2026-03-26 with no `exclusion_reason` recorded. Surfaced by AI as SP-117-001 (HIGH) during Stage 2a readiness review. STEP re-extract on 2026-05-01 confirmed the same 209-verse footprint as originally captured.

| Strong's | Status | Owner | Verses |
| --- | --- | --- | ---: |
| H7965G shalom (peace) | extracted | R117 | 148 |
| H7965I shalom (peace: well-being) | extracted | R117 | 46 |
| H7965K shalom (peace: greeting) | extracted_thin | R117 | 8 |
| H7965J shalom (peace: friendship) | extracted_thin | R117 | 5 |
| H7965H shalom (Peace [God]) | extracted_thin | R117 | 1 |
| H7965L shalom (peace: completely) | extracted_thin | R117 | 1 |

R117 OWNER count: 43 → **49**. Active OWNER verses: 1462 → **1671** (+209). All 6 sub-forms set to `vc_status='not_done'` for VC pickup. R34 covenant copies demoted to XREF.

**VC re-run progress (VCB-030):**

| Term | mti | Verses | VCNEW patch | vc_status |
| --- | ---: | ---: | --- | --- |
| H7965G shalom | 2508 | 148 | Applied 2026-05-01 (4 groups, 13 anchors, 83 relevant, 65 set-aside) | `vc_completed` (md_v 2) |
| H7965I shalom | 2509 | 46 | Pending | `not_done` |
| H7965K shalom | 2511 | 8 | Pending | `not_done` |
| H7965J shalom | 2510 | 5 | Pending | `not_done` |
| H7965H shalom | 406 | 1 | Pending | `not_done` |
| H7965L shalom | 2512 | 1 | Pending | `not_done` |

Patch applied: [PATCH-20260501-VCB030-VCNEW-H7965G-V1](archive/patches/wa-vcb-030-patch-vcnew-H7965G-v1-20260501.json) · 148 verse_context inserts + 4 group inserts. Per-term VC status manually flipped to `vc_completed` (the patch metadata was missing the `patch_type: "VCNEW"` field, so the applicator's VC-2 helper didn't auto-run; this is recorded for future AI patches).

The 5 remaining H7965 sub-forms cover only 61 verses total — small follow-on session. Per-term Session A `.md` files are still in `inputs/` (md_version=v1, fresh). Once all 6 are classified, R117's `verse_context_status` can derive back to `Complete` and Stage 2b proceeds with the full peace inventory.

**Dimension Review handoff package (Registry Mode for R117):**

Per `wa-dimensionreview-instruction [current]` §2.2, generated via `scripts/build_dimension_extract.py --bundle C17` (2026-05-01). Skeleton `wa_dimension_index` rows pre-seeded for the 4 new H7965G groups (3581/3582/3583/3584) with `dimension=NULL` so AI can see them as review targets. R117 `dim_review_status` flipped Complete → NULL to mark it as the only target in C17.

| File | Size | Purpose |
| --- | ---: | --- |
| `wa-dim-C17-extract-2026-05-01.json` | (canonical) | 303 groups across 9 active C17 registries (R117's 73 + 8 cross-context registries' 230) |
| `wa-dim-C17-existing-pointers-2026-05-01.json` | — | 1744 SB findings + 207 SD pointers cross-cluster |
| `wa-dim-C17-rootfamily-2026-05-01.json` | 120 KB | 69 roots, 5 cross-registry — supports Phase A coherence check |
| `wa-dim-C17-handoff-kickoff-v1-20260501.md` | — | Kickoff brief + DV-1..DV-5 pre-checks; researcher signs off then hands to AI |

**Phase C completed 2026-05-01** — `PATCH-20260501-DIMREVIEW-C17-REG117-V2-CANONICAL` applied (v1 normalised in-flight to canonical DIMENSION_LABEL prefix per researcher waiver). All 73 R117 groups now carry dimension assignments:

| Group | Anchors | Relevant | Dimension | Subject |
| --- | ---: | ---: | --- | --- |
| 2508-001 | 5 | 19 | 01 — Emotion — Positive | HUMAN |
| 2508-002 | 3 | 24 | 06 — Relational Disposition | GOD |
| 2508-003 | 2 | 25 | 05 — Moral Character | HUMAN |
| 2508-004 | 3 | 15 | 11 — Divine-Human Correspondence | NONE |

Plus 1 SD pointer raised: **DIM-117-SD003** — group 2508-004 establishes shalom as constitutively identified with the messianic king (Isa 9:6 / Mic 5:5 / Isa 53:5); flagged for Session D examination of the OT-prophetic ground for the NT claim that Christ IS peace (Eph 2:14, G1515 eirēnē).

`word_registry.dim_review_status: Complete` (instruction `wa-dimensionreview-instruction-v3_3-20260418.md`). The other 69 R117 groups continue to carry their CLAUDE_AI dimensions from the original cluster review (DIM v1.9 2026-04-09).

**VC re-run completed 2026-05-02 (path a):** AI returned VCNEW patches for the 5 remaining H7965 sub-forms; both applied via canonical-injected copies (patch_type: VCNEW). 5 new groups, 61 verse_context inserts (1 H7965L all-verses-fail — no group). Legacy 43 R117 OWNER terms retro-flipped to `vc_completed` (they passed VC pre-2026-03-26 under registry-level workflow; per-term tag now consistent). Registry `verse_context_status` derived back to `Complete` (49/49 OWNER terms `vc_completed`). **ANOMALY-117-001** resolved.

**Second-pass DimReview applied 2026-05-02** — `PATCH-20260502-DIMREVIEW-C17-REG117-V2-CANONICAL` (v1 normalised in-flight; researcher waiver per ad-hoc flow). 5 new groups dimensioned:

| Group | mti | Strong's | Dimension | Subject |
| --- | ---: | --- | --- | --- |
| 2509-001 | 2509 | H7965I | 07 — Vitality / Existence | HUMAN |
| 2509-002 | 2509 | H7965I | 05 — Moral Character | HUMAN |
| 2511-001 | 2511 | H7965K | 06 — Relational Disposition | HUMAN |
| 2510-001 | 2510 | H7965J | 06 — Relational Disposition | HUMAN |
| 406-001 | 406 | H7965H | 11 — Divine-Human Correspondence | GOD |

R117 now carries dimensions across all 78 active groups: 4 H7965G + 5 H7965H/I/J/K + 69 original peace family.

**Readiness v10 generated 2026-05-02** — validation: **READY · 12 PASS · 3 WARN · 0 FAIL.** All gates pass. Remaining warnings are informational only (C11 set-aside ratios, C13 dimension_confidence still CLAUDE_AI for now, C15 researcher fields blank).

**R117 is cleared for v1.8 Stage 2b** — ready for AI session-output (Q&A across the 189 v2 catalogue prompts + synthesis + chapter pass).

**WARN flags from validation (informational):** C11 (27 groups with high set-aside ratios — possible VC drift signal), C12 (legacy-VC caveat — all 49 OWNER terms vc_status='not_done'), C13 (no 'confirmed' dimensions — all 'CLAUDE_AI'), C15 (researcher fields absent).

**Cluster:** C17 (covenant / kindness / peace family) · 8/9 active words at Analysis Complete (R022 communion excluded).

**Notes:** R117 is the largest C17 word — now 49 OWNER terms (post H7965 recovery), 69 VC groups before recovery, ~579 KB readiness markdown (v7).
