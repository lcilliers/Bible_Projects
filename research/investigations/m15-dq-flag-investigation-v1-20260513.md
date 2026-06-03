# M15 — Data-quality flag investigation

**Date:** 2026-05-13
**Purpose:** Understand the implications of the 477 data-quality flag rows reported for M15 in the outstanding-research report (specifically `NO_WORD_ANALYSIS` and `PROSE_ONLY_MEANING`). Pick representative terms, trace their journey through the data, and confirm how the flagged terms were handled in the cluster.

---

## 1. Conclusion up front

The 477 flag count on M15 is **inflated by structural repetition** and does **not** indicate analytical gaps in the cluster's published study.

- `NO_WORD_ANALYSIS` and `PROSE_ONLY_MEANING` are **STEP data-coverage descriptors** — they record what STEP did and did not return at extraction time. They are not analytical findings.
- `wa_data_quality_flags` carries a `file_id`. One flag row is written **per (file × term × flag_code)** — so a term that exists in 8 registries (1 OWNER + 7 XREF copies) accumulates 8 rows of each flag code that applies to it.
- The 477 rows on M15 reduce to roughly **85 distinct terms** for `NO_WORD_ANALYSIS` and **64 distinct terms** for `PROSE_ONLY_MEANING` — and those distinct counts include both OWNER and XREF rows on the same term, so the underlying number of *terms with the flag* is even smaller.
- **None of these flags gated anything.** All three traced terms (below) were placed in sub-groups, joined VCGs, contributed anchor verses where appropriate, and feature in cluster findings.

---

## 2. What the flags actually mean

| Flag | Group | Description |
|---|---|---|
| `NO_WORD_ANALYSIS` | DATA_COVERAGE | No word-level analysis is available for this term — STEP did not return the structured word-analysis section at extraction time. |
| `PROSE_ONLY_MEANING` | DATA_COVERAGE | Meaning stored as single prose block — STEP `medium_def` contains no structured sense numbering for this term. No further subdivision available. |

The `research_actions` field is NULL for both flags — they carry no required follow-up. The flags simply record what STEP returned.

---

## 3. M15 distribution

| Flag code | Total rows | Distinct terms |
|---|---:|---:|
| NO_WORD_ANALYSIS | 201 | 85 |
| PROSE_ONLY_MEANING | 145 | 64 |
| VERSE_EVIDENCE_CONCENTRATED | 121 | 58 |
| VERSE_EVIDENCE_MINIMAL | 6 | 6 |
| VERSE_EVIDENCE_HIGH | 4 | 2 |
| **Total** | **477** | — |

The two flag codes the user flagged together account for **346** of the 477 rows. The remaining 131 are the evidence-flag family — which CLAUDE.md §14 calls "informational, never gating."

---

## 4. Three terms traced end-to-end

### 4.1 G4894 *suneidō* (be aware) — 24 flag rows

| Field | Value |
|---|---|
| Canonical owner | registry 26 (conscience) — OWNER |
| Cluster | M15 |
| Sub-group placement | M15-B (Understanding) AND BOUNDARY (dual placement) |
| `short_def_mounce` | "to share knowledge with; to be conscious (of oneself) aware…" |
| `parsed_meaning_id` | 5282 (LSJ entry IS parsed and stored) |
| `meaning` field | empty (this is what trips the flag — but the *real* meaning is in `short_def_mounce` + parsed LSJ) |
| Inventory rows | 8 (1 OWNER + 7 XREF) |
| Verse records | 3 active |
| M15 VCG memberships | 1 |
| M15 anchors contributed | 0 |
| Findings mentioning the term | 1 |

**Flag breakdown:** 8 rows × 3 flag codes = 24 rows (each registry's file_id gets one row per applicable flag).

**Handling in M15:** The term was placed in two sub-groups (M15-B and BOUNDARY), joined a VCG, and is cited in one finding. Its three verses entered the cluster's verse evidence base. No flag blocked anything.

---

### 4.2 G0050 *agnoeō* (be ignorant) — 14 flag rows

| Field | Value |
|---|---|
| Canonical owner | registry 26 (conscience) — OWNER |
| Cluster | M15 |
| Sub-group placement | M15-C (Knowledge) AND M15-E (Deliberative planning) |
| `short_def_mounce` | "to be ignorant, not know, not understand…" |
| `parsed_meaning_id` | 5292 |
| Inventory rows | 6 (1 OWNER + 5 XREF) |
| Verse records | 21 active |
| M15 VCG memberships | 1 |
| **M15 anchor contributed** | **Rom 10:3** in M15-C-VCG09 |
| Findings mentioning the term | 3 |

**Flag breakdown:** 7 rows × 2 flag codes = 14 rows.

**Handling in M15:** *agnoeō* provided one of the cluster's published anchor verses (Rom 10:3 — "ignorant of the righteousness of God") — used verbatim in Appendix B of the M15 publication and quoted in Chapter 3 (the divine pattern). Three findings cite the term. Despite the flags, this term carries substantial weight in the cluster's analytical record.

---

### 4.3 G1014 *boulomai* (to plan) — 8 flag rows

| Field | Value |
|---|---|
| Canonical owner | registry 43 (desire) — OWNER |
| Cluster | M15 |
| Sub-group placement | M15-E (Deliberative planning, counsel, and purposive intent) |
| `short_def_mounce` | "to wish, will, desire; to choose, determine, plan…" |
| `parsed_meaning_id` | 3950 |
| Inventory rows | 5 (1 OWNER + 4 XREF) |
| Verse records | 34 active |
| M15 VCG memberships | 1 |
| **M15 anchor contributed** | **2Pe 3:9** in M15-E-VCG01 |
| Findings mentioning the term | 14 |

**Flag breakdown:** 4 rows × 2 flag codes = 8 rows.

**Handling in M15:** *boulomai* provided 2Pe 3:9 ("not wishing that any should perish, but that all should reach repentance") as the anchor for M15-E-VCG01 — the meaning group for divine salvific desire. **Fourteen findings** in the cluster mention this term — it is one of the more analytically productive terms in M15-E despite the flags.

---

## 5. The repetition pattern explained

`wa_data_quality_flags` schema:

```
wa_data_quality_flags (id, file_id, term_id, flag_id, description, last_changed)
```

The flag is recorded per `file_id` — and `file_id` is registry-scoped via `wa_file_index`. So when registry 26 (conscience) extracts G4894 *suneidō* and records the flag, the flag is tied to file_id=8 (the conscience file). When registry 100 (knowledge) later pulls G4894 as an XREF, a *new* flag row is written tied to file_id=137 (the knowledge file). The flag describes the *same fact about STEP's output for G4894*, but it appears 8 times in the table — once per registry that pulled it.

This means the "count" of flags is **not** a count of distinct data-coverage issues. To get the true count of *terms with the flag*, you need `COUNT(DISTINCT term_id)` (not `COUNT(*)`).

---

## 6. What the flags would block (and what they don't)

| Pipeline step | Blocked by these flags? |
|---|---|
| Verse extraction from STEP | No — the term has its verses regardless |
| Term placement in `mti_term_subgroup` | No — three traced terms are all placed |
| VCG construction | No — all traced terms have VCG memberships |
| Anchor verse selection | No — *agnoeō* and *boulomai* both provided anchors |
| Phase 8 finding generation | No — all three appear in findings |
| Inclusion in Session C publication | No — *agnoeō*'s Rom 10:3 and *boulomai*'s 2Pe 3:9 are both quoted in the M15 publication |

**The flags are descriptive, not gating.** A future Session B pass might revisit the flagged terms to:
- Decompose their `short_def_mounce` text into structured senses (addressing PROSE_ONLY_MEANING)
- Capture word-analysis data from another source (addressing NO_WORD_ANALYSIS)

But these are enhancements, not corrections. The cluster's analytical claims are not weakened by the flags.

---

## 7. Recommended action on the outstanding-research report

Two options for sharpening the data-quality flag section in the outstanding-research report:

**Option A — count distinct terms, not rows.**
Change Section 5c of the outstanding-research report to display `COUNT(DISTINCT term_id)` per flag code, with the row count as a parenthetical inflation indicator. Result for M15:

| Flag code | Distinct terms | Row count |
|---|---:|---:|
| NO_WORD_ANALYSIS | 85 | 201 |
| PROSE_ONLY_MEANING | 64 | 145 |
| VERSE_EVIDENCE_CONCENTRATED | 58 | 121 |
| VERSE_EVIDENCE_MINIMAL | 6 | 6 |
| VERSE_EVIDENCE_HIGH | 2 | 4 |

**Option B — filter the evidence-flag family out entirely.**
Evidence flags (`VERSE_EVIDENCE_*`) are explicitly informational per CLAUDE.md §14. Exclude them from the outstanding-research report and surface only the data-coverage flags (`NO_WORD_ANALYSIS`, `PROSE_ONLY_MEANING`). Result: the report's flag section becomes much shorter and more meaningful.

**Recommended:** apply both — count distinct terms AND exclude the evidence-flag family. Confirmation requested before changing the report script.

---

## 8. Source data and reproducibility

Trace script: [scripts/_tmp_m15_dq_flag_trace.py](../../scripts/_tmp_m15_dq_flag_trace.py)
Outstanding-research report: [Sessions/Session_Clusters/M15/wa-cluster-M15-outstanding-research-v1-20260513.md](../../Sessions/Session_Clusters/M15/wa-cluster-M15-outstanding-research-v1-20260513.md)
M15 publication using the flagged terms: [Sessions/Session_Clusters/M15/wa-cluster-M15-publication-v1-20260512.pdf](../../Sessions/Session_Clusters/M15/wa-cluster-M15-publication-v1-20260512.pdf)
