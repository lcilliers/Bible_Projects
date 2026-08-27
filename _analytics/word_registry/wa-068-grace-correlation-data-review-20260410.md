# Correlation Data Review — Registry 068 (Grace)

**Date:** 2026-04-10
**Context:** Claude AI reviewed the grace complete extract and programme-wide correlation file, identifying 8 data gaps. This document assesses each claim against the actual database state.

---

## Point 1 — Verse co-occurrence: "0 entries"

**Verdict: WRONG — data exists.**

The database shows extensive co-occurrence for grace:

| Partner Registry | Word | Shared Verses |
|-----------------|------|---------------|
| 140 | seeking | 40 |
| 187 | strength | 15 |
| 103 | love | 14 |
| 57 | evil | 12 |
| 43 | desire | 12 |
| 213 | listen | 11 |
| 173 | will | 11 |
| 19 | calling | 11 |
| 198 | might | 10 |
| 117 | peace | 10 |
| 73 | guilt | 10 |
| 59 | faith | 10 |

Claude AI's explanation ("Verse Context Reset" caused it) is also incorrect — grace's `verse_context_status` is `Complete`, and co-occurrence doesn't depend on verse_context at all; it uses `wa_verse_records.reference` matching. The real issue is that the correlation data was never included in the complete extract — there is no Layer 9.

---

## Point 2 — Dimension overlap: "0 entries"

**Verdict: CORRECT — data genuinely absent.**

Grace has 11 `wa_dimension_index` rows but all at `KEYWORD_WEAK` confidence. The correlation script filters on `dimension_confidence = 'CLAUDE_AI'` only. Grace's `dim_review_status` is NULL — it has not been through Dimension Review yet (only C20/C21/C22 have been reviewed so far; grace is in C17).

**Action needed:** Dimension Review for C17 must complete before this signal can fire.

---

## Point 3 — Root family connections: "0 entries"

**Verdict: WRONG — data exists.**

The CHAR root spans 2 registries:

- **grace (68):** G5485, G5483, G5487
- **anger (4):** H2740, H2734, H8474

This meets the correlation script's threshold of 2 registries. CHEN is grace-only (1 registry), so it correctly doesn't fire.

Some CHAR entries have `root_gloss = NULL` — this shouldn't prevent the grouping (the script groups by `root_code`). If CHAR+anger is missing from the file Claude AI reviewed, the file may have been generated before the root family backfill (963 roots added on 2026-04-09).

---

## Point 4 — Grace not in ranked_pairs

**Verdict: WRONG — consequence of incorrect premises.**

Grace should appear via:

- **XREF sharing:** 10 shared terms with pray/mercy/compassion, 9 with guilt — well above `min_xref=3`
- **Shared anchor verses:** 8 shared anchors (pride, debauchery, yielding, heart, kindness, praise, hope, mourning)

These alone produce composite scores. If the correlation file was generated before the latest data, this explains the absence.

**XREF sharing detail:**

| Partner | Word | Cluster | Shared Terms |
|---------|------|---------|-------------|
| 212 | pray | C15 | 10 |
| 111 | mercy | C17 | 10 |
| 23 | compassion | C17 | 10 |
| 73 | guilt | C13 | 9 |
| 132 | rejoicing | C03 | 1 |

**Shared anchor verses:**

| Verse | Partner Reg | Partner Word |
|-------|------------|-------------|
| 2Cor 12:9 | 123 | pride |
| Eph 2:8 | 39 | debauchery |
| Eph 2:8 | 180 | yielding |
| Eph 4:32 | 183 | heart |
| Eph 4:32 | 99 | kindness |
| Pro 31:30 | 121 | praise |
| Rom 5:2 | 78 | hope |
| Zec 12:10 | 113 | mourning |

---

## Point 5 — cross_registry_link_count is 0

**Verdict: CORRECT — genuinely empty.**

The `wa_cross_registry_links` table has zero rows for grace. These are formal, manually-curated cross-registry relationships — a different mechanism from the automated correlation signals.

**Action needed:** These are typically populated during Session D synthesis, which has not run for grace.

---

## Point 6 — session_b_finding_count and session_d_pointer_count are 0

**Verdict: PARTIALLY CORRECT.**

- **Session B findings** (`wa_session_b_findings`): zero rows — despite grace being at `Analysis Complete`. This suggests the analysis patch for grace may not have included structured findings rows.
- **Session D pointers**: legitimately zero — Session D has not run.
- Grace does have 5 `PH2_CROSS_REF_ENRICHMENT` research flags, so research flag data exists but not in the Session B/D categories.

---

## Point 7 — sb_classification is null

**Verdict: WRONG — field is populated.**

The database shows:

- `sb_classification`: `Spirit-soul interface`
- `sb_classification_reasoning`: 795-character text present

If Claude AI saw NULL, it was looking at an older export file produced before the classification was written, or the export was generated before this field was set. The complete extract pulls `word_registry.*` which includes this field.

---

## Point 8 — Named registries absent from correlations file

**Verdict: STALE FILE — registries exist.**

All named registries are present in the database:

| Reg | Word | VC Status | Session B Status | Cluster |
|-----|------|-----------|-----------------|---------|
| 135 | repentance | Complete | Verse Context Reset | C13 |
| 64 | forgiveness | Complete | Verse Context Reset | C17 |
| 80 | humility | Complete | Verse Context Reset | C08 |
| 117 | peace | Complete | Verse Context Reset | C17 |
| 82 | identity | NULL | NULL | C19 |
| 174 | wisdom | Complete | Verse Context Reset | C02 |

Identity has NULL VC status (excluded from scope), so it legitimately wouldn't appear. The others all have data and should produce correlation signals if the file is regenerated. Their absence suggests the correlation file Claude AI reviewed was either stale or truncated (the script caps `ranked_pairs` at 200 and `verse_cooccurrence` at 100).

---

## Summary

| # | Claim | Verdict | Action |
|---|-------|---------|--------|
| 1 | No verse co-occurrence | **Wrong** — data exists, 40+ shared verses | Include in extract |
| 2 | No dimension overlap | **Correct** — C17 not reviewed yet | Dim Review C17 needed |
| 3 | No root family | **Wrong** — CHAR links grace+anger | Regenerate correlation / include in extract |
| 4 | Not in ranked_pairs | **Wrong** — XREF + anchors produce scores | Regenerate correlation / include in extract |
| 5 | No cross-registry links | **Correct** — table empty | Session D work needed |
| 6 | No SB findings / SD pointers | **Correct** — not written | Check if analysis patch should have included them |
| 7 | sb_classification is null | **Wrong** — field is populated | Verify extract captures it correctly |
| 8 | Named registries absent | **Stale file** — registries exist | Regenerate correlation file |

**Core action:** Add a correlations layer to the complete extract so word-level correlation data is self-contained in each word's export file.
