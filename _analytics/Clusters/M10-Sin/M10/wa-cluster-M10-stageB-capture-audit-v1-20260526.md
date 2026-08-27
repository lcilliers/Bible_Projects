# M10 Stage B capture audit

**Date:** 2026-05-26
**Question (researcher):** Are all M10 synthesis findings captured in the DB, or is content missing?

## Direct answer

**The synthesis findings file is fully captured.** The thematic observations file (a separate analytical document) is **not in the DB** — that may or may not be a gap depending on whether you consider it Phase 9 finding content or Session C input.

## What's in the DB (cluster_observation, 58 rows for M10)

| Type | Count | Source | Status |
|---|---:|---|---|
| TIER_READING_GUIDE | 27 | wa-cluster-M10-phase9-synthesis-findings-v1-20260524.md (PART A) | open |
| CLUSTER_SYNTHESIS | 15 | wa-cluster-M10-phase9-synthesis-findings-v1-20260524.md (PART B) | open |
| INTEGRATION_NOTE | 8 | Phase 3 BOUNDARY pre-decisions + Phase 8.5 closure | open |
| INTER_RELATIONSHIP | 7 | Phase 8.7 characteristic-mapping carry-forwards | open |
| CROSS_CLUSTER_HANDOFF | 1 | Phase 8.5 routing for che.vel | open |
| **TOTAL** | **58** | | |

Source verification: the synthesis findings file has 27 `[M10-SYNTH] T#-GUIDE-NN` markers + 15 `[M10-SYNTH] OBS-NN` markers. DB has 27 + 15 matching rows. **No content was dropped on load.**

## What's not in the DB — `wa-m10-thematic-observations-v1-20260524.md`

This 67 KB file contains **8 analytical sections** authored on the same day as the synthesis findings file (2026-05-24). Its header reads:

> **Source data:** T1, T2, T3 tier files (22 characteristics)
> **Purpose:** Identify reader-facing windows/themes for Session C architecture

The 8 sections:

| # | Section | Body chars |
|---:|---|---:|
| 1 | The Heart is the Cluster's Constitutional Centre | 1,090 |
| 2 | The Conscience is the Cluster's Primary Diagnostic Instrument | 2,119 |
| 3 | The Will is the Cluster's Primary Faculty — But Its Role Changes | 1,028 |
| 4 | Constitutional Deposit: The Progressive Entrenchment of Sin | 1,179 |
| 5 | Three Structural Tiers Emerge from the Data | 1,339 |
| 6 | Two Characteristics Are Resolution-Facing (Not Sin-Describing) | 484 |
| 7 | The Relational Damage Pattern | 650 |
| 8 | Spirit-Level Pattern | **58,896** |
| | **Total** | **66,785** |

### Section 8 is the heavy one

58,896 chars = ~10–12 typed pages of analytical content. The other 7 sections collectively are 7,889 chars (~1–2 pages each).

### Overlap with captured OBS rows

The thematic sections share titles with several captured OBS rows:

| Thematic section | Matching DB OBS |
|---|---|
| §1 Heart as Constitutional Centre | OBS-02 (Heart) |
| §2 Conscience as Primary Diagnostic | OBS-03 (Conscience) |
| §3 Will as Primary Faculty | (no direct match) |
| §4 Constitutional Deposit | OBS-05 (Sin's Constitutional Deposits) |
| §5 Three Structural Tiers | (no direct match) |
| §6 Resolution-Facing Characteristics | OBS-10 (Resolved State) |
| §7 Relational Damage Pattern | (no direct match) |
| §8 Spirit-Level Pattern | (no direct match) |

For sections WITH a matching OBS row, the OBS is a 400–800 char distillation of the longer thematic section (2.2× shorter). For sections WITHOUT a match (§3, §5, §7, §8), the analytical content **only exists on disk**, not in the DB.

## What this means in practice

The synthesis findings file's content is in the DB — that's the authoritative Phase 9 Stage B output per its filename and structure.

The thematic observations file is harder to classify:
- If it's **Phase 9 analytical findings** (just shaped differently) → 4 of its 8 sections have no DB counterpart and are missing
- If it's **Session C architecture input** (per its stated purpose) → it stays on disk; not part of Phase 9 capture

Section 8 (Spirit-Level Pattern, 59 KB) is the biggest unknown — it's an order of magnitude larger than any individual OBS row in the DB, suggesting it's substantial analytical content that wasn't condensed elsewhere.

## Recommendation

Treat the thematic file as **findings to be captured** based on its content depth (especially Section 8). Two ways to load:

**Option 1 — Load all 8 sections as new CLUSTER_SYNTHESIS rows.**
- 8 new cluster_observation rows
- Titles: `M10 thematic observation §N — {section title}`
- Some overlap with existing OBS-02/03/05/10 but the longer treatment is preserved
- Audit trail: source_file pointing to the thematic .md

**Option 2 — Selective load: only the 4 sections without a DB counterpart.**
- 4 new rows (§3, §5, §7, §8 — the unique analytical content)
- Avoids duplication with already-captured OBS rows
- Section 8 is the big win (59 KB of unique content)

**Option 3 — Leave on disk; treat as Session C input.**
- No DB writes
- Document the file's role in the M10 obslog
- Session C reads it directly when needed

## Other working files (already on disk, not in DB)

For completeness, these other M10 working documents are also on disk only — but they're clearly NOT findings:

| File | Role |
|---|---|
| wa-cluster-M10-phase9-cluster-synthesis-brief-v1 (2 versions) | AI session brief (input doc) |
| wa-cluster-M10-phase9-cluster-synthesis-input-v1 (2 versions) | Per-prompt matrix (input doc) |
| wa-cluster-M10-phase9-findings-distribution-v1/v2 | Pre-synthesis E/S/G distribution analytics |
| 8 tier interrogation files (T0-by-char.md through T7-by-char.md) | Per-prompt char-stacked inputs for tier-batched synthesis |

These are inputs / working analytics, not findings outputs. They legitimately stay on disk.

---

*Decision required: Option 1, 2, or 3 for the thematic observations file?*
