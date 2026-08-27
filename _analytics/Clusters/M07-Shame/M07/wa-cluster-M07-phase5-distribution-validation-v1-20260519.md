# M07 Phase 5 — Distribution validation

**Date:** 2026-05-19
**Cluster:** M07 — Shame, Disgrace and Humiliation
**Per:** v2_8 §8.6 (40% distribution hard gate)
**Verdict:** **PASS**

---

## Distribution

| Sub-group | Characteristic | Verses | % of substantive |
|---|---|---:|---:|
| M07-A | CHAR-1a Shame as unjust inner wound | 63 | 18.8% |
| M07-B | CHAR-1b Shame as moral consequence | 110 | **32.7%** (largest) |
| M07-C | CHAR-1c Shame before God | 50 | 14.9% |
| M07-D | CHAR-2 Humiliation as enforced abasement | 50 | 14.9% |
| M07-E | CHAR-3 Dishonour as relational worth-denial | 15 | 4.5% |
| M07-F | CHAR-4 Shamefulness as moral judgment | 16 | 4.8% |
| M07-G | CHAR-5 Shame produced by contempt/rejection | 24 | 7.1% |
| M07-H | CHAR-6 Innocence as structural counter | 8 | 2.4% |
| M07-BOUNDARY | (BOUNDARY terms) | 27 | (excluded from gate) |
| **Substantive total** | | **336** | 100% |

**Biggest substantive sub-group:** M07-B (32.7%) — under the 40% gate ✓

## Notes

- CHAR-1 (the dominant "shame as experienced inner state" characteristic) is volume-split into 3 sub-groups (M07-A unjust-wound, M07-B moral-consequence, M07-C divine-encounter) per §8.0 rule 2. The cumulative share is 63+110+50 = 223 / 336 = 66.4% — typical for a single dominant characteristic.
- §8.0 1:1 characteristic-to-sub-group default: 5 of 6 characteristics (CHAR-2 through CHAR-6) map cleanly to a single sub-group. Only CHAR-1 (the primary shame experience) required volume-splitting.
- Cross-register flags preserved:
  - **M07-G** flagged M06 (contempt is M06 source-side; M07-G is the shame-recipient side; Phase 9 T6 will address the cross-cluster relationship)
  - **M07-H** flagged M12 (innocence is M12 primary purity register; these terms stay in M07 because every verse evidences the innocence–shame polarity)
- No SPLIT_SUBGROUP cases flagged at Phase 5.

## Mapping-file vs DB count discrepancy

DB has **365 is_relevant verses**; mapping has **363 entries**. The 2 missing entries are the **orphan vc rows** from Phase 2 (vc rows whose underlying `wa_verse_records.delete_flagged=1`):

| vc_id | mti_id | Strong's | Reference |
|---:|---:|---|---|
| 34973 | 324 | G0152 aischunē | Php 3:19 |
| 49397 | 628 | G2699 katatomē | Php 3:2 |

The AI's design document listed both verses textually (G0152 Phili 3:19 → M07-F; G2699 Phili 3:2 → M07-BOUNDARY) but the mapping JSON omitted them — defensible because they have `analysis_note=NULL` (no Pass A meaning). To unblock Phase 6, CC will **soft-delete** these 2 orphan vc rows (same cleanup pattern as M04 Step 1 orphan precedent), bringing M07's is_relevant count to 363 and matching the mapping exactly.

(The third Phase 2 orphan, Pro 25:10 H2616B cha.sad, already moved to M05 at Phase 4 and is M05's housekeeping now.)

---

*Distribution gate PASS — proceed to Phase 6 with orphan-cleanup as Op 0.*
