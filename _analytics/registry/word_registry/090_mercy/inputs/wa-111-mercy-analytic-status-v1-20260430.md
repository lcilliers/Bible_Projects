# R111 Mercy — Analytic Status (v1.8 revision-session input)

**Generated:** 2026-04-30 16:47 UTC
**Source:** SQLite `database/bible_research.db` (schema v3.17.0)
**Governing instruction:** [wa-sessionb-analysis-output-v1_8-20260430.md](../../../../Workflow/Instructions/wa-sessionb-analysis-output-v1_8-20260430.md) §1 (revision-session input)

**Purpose.** Capture the prior analytical state for R111 mercy so a Stage 2 session can resume cleanly under v1.8. Lifecycle summary, resolved Q&As, resolved SD pointers, prior chapters, anchor analyses, and open items.

---

## 1. Registry header

| Field | Value |
| --- | --- |
| `no` | 111 |
| `id` | 111 |
| `word` | mercy |
| `category_hint` | None |
| `dimensions` | Relational/Social |
| `cluster_assignment` | C17 |
| `phase1_status` | Complete |
| `verse_context_status` | Complete |
| `session_b_status` | Verse Context Reset |
| `dim_review_status` | Complete |
| `dim_review_version` | WA-DimensionReview-Instruction-v1.9-2026-04-09 |

## 2. Lifecycle summary

**Active findings (`wa_session_b_findings`):** 1

**By finding_type:**

| finding_type | count |
| --- | ---: |
| DIMENSION_REVIEW | 1 |

**By status:**

| status | count |
| --- | ---: |
| pending | 1 |

## 3. Open research flags (`wa_session_research_flags`)

| flag_code | open count |
| --- | ---: |
| SD_POINTER | 15 |
| DIMREVIEW_SESSION_D | 1 |

### 3.1 SD pointers — HIGH priority (full list in data package §9)

- **DIM-111-SD001** (HIGH) — Strength/power/authority/dominion registries (Reg 187/196/197/198/199) share all 4 of mercy dimensions. Structural question: is mercy the mo…
- **DIM-111-SD002** (HIGH) — Reg 73 (guilt) shares 9 terms with mercy -- primarily supplication vocabulary. Guilt as inner condition generating authentic mercy-seeking. …
- **DIM-111-SD003** (HIGH) — Jam 2:13 and Mat 23:23 encode mercy-justice structural relationship. Mercy triumphing over judgment. Justice, mercy, faithfulness as weighti…
- **DIM-111-SD004** (HIGH) — 1Jo 4:10: divine love -> sending of Son -> propitiation -> mercy received. Eph 2:4: God rich in mercy because of great love. Structural ques…

### 3.2 Open SB findings (Session B follow-on items)

_(no open SB findings)_

## 4. Prior Q&A coverage — v1 catalogue (retired 2026-04-30)

**Q&A links to retired v1 catalogue:** 0

_No prior v1 Q&A work for this registry. This is a first Session B Stage 2 pass under the v2 catalogue._

## 5. v2 catalogue coverage status (Stage 2b under v1.8)

**v2 prompts in catalogue:** 189
**v2 prompts with R111 link:** 0
**v2 prompts NOT YET covered for R111:** 189

**Status:** R111 has not yet been processed against the v2 catalogue. Stage 2b under v1.8 is **outstanding** — all 189 prompts need disposition (A / P / S / N).

## 6. Stage 2c synthesis state (under v1.8)

**Synthesis findings in DB:** 0 (target: 28 — 7 intra-tier T1–T7 + 21 inter-tier T1–T7 pairs)

**Status:** Stage 2c synthesis pass under v1.8 has not been run. All 28 synthesis entries are **outstanding**.

Per v1.8 SB-29: every entry carries one of three outcomes (D / F / N). T0 is excluded from Stage 2c (held for Session D).

## 7. Prior prose chapters

**Session A chapters (Phase 1 outputs):** 6

| code | label | version | body chars | status | created |
| --- | --- | ---: | ---: | --- | --- |
| `sa_s1_d1` | Session A — Word Summary | v1 | 1,519 | approved | 2026-04-28 |
| `sa_s1_d2` | Session A — Meaning | v1 | 17,096 | approved | 2026-04-28 |
| `sa_s1_d3` | Session A — Verses | v1 | 113,700 | approved | 2026-04-28 |
| `sa_s1_d4` | Session A — Terms | v1 | 187,257 | approved | 2026-04-28 |
| `sa_s1_d5` | Session A — Pointers | v1 | 7,189 | approved | 2026-04-28 |
| `sa_s1_d6` | Session A — Questions | v1 | 35,127 | approved | 2026-04-28 |

## 8. Anchor-verse analyses (`verse_context.analysis_note`)

**Anchor verses with analysis_note populated:** 0

_No anchor-verse analyses captured. Stage 2a Unit 7 in this session will populate `analysis_note` per anchor verse._


## 9. Open Session B items — §N for the v1.8 session

Per v1.8 §3, every open item must reach one of four outcomes by session close: resolve via Q&A, raise as new GAP question, convert to SD pointer, or mark not_relevant.

**Open findings (status=open/pending):** 1

- **DIM-111-001** (DIMENSION_REVIEW, status=pending) — The atonement/propitiation vocabulary (kipper, kaphar, kapporet, hilasmos, hilastērios) within the mercy registry produces a cluster of Transformation/GOD group…

## 10. What v1.8 expects on (re)submission

**Stage 2a:** observations layer is in place (1 findings). No new Stage 2a reading required unless gaps surface during Stage 2b.

**Stage 2b:** all 189 v2 catalogue prompts (T0–T7) require disposition (A / P / S / N) per §10. Prior v1 Q&A answers are Stage 2a source material — every v2 prompt receives a fresh answer grounded in the data package.

**Stage 2c:** new under v1.8 — produce 28 synthesis entries (7 intra T1–T7 + 21 inter T1–T7 pairs). T0 excluded (Session D). Each entry: outcome D/F/N; D needs ≥2 Q&A citations; F always raises an SD pointer; N requires a one-sentence rationale. See §SB-29.

**Output:** comprehensive obslog `wa-111-mercy-obslog-v{n}-{date}.md` + session log. CC parses obslog into DB.

---

*Generated by `scripts/_tmp_build_resubmission_artefacts.py` at 2026-04-30 16:47 UTC.*