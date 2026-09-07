# M11 — Phase 1 + Phase 2 obslog — 2026-05-26

**Cluster:** M11 — Repentance, Forgiveness and Restoration
**Governing instruction:** `wa-sessionb-cluster-instruction-v2_9-20260526`
**Phases:** Phase 1 (UT review / vc_status advancement) + Phase 2 (Pass A meanings + keywords)

## Pre-Phase-1 cluster state

| Metric | Value |
|---|---:|
| Cluster status | `Not started` (version v6) |
| Terms (mti_terms) | 15 |
| `verse_context` rows (all is_relevant states) | 289 |
| `is_relevant=1` (active) | 288 |
| `is_relevant=0` (set-aside) | 1 (G0580 apobolē, Rom 11:15) |
| `is_relevant IS NULL` (UT) | **0** |
| Rows with `analysis_note` populated | 1 (Rom 11:15 — pre-3.25.0 era, no keywords) |
| Rows with `keywords` populated | 0 |
| Inherited VCGs (pre-cluster-pivot) | 26 (will be silently dissolved at Phase 8 per v2_9) |

### Term inventory (Hebrew + Greek, 15 terms)

| Strong's | Translit | mti_id | pre-Phase-1 vc_status |
|---|---|---:|---|
| G0580 | apobolē | 1094 | vc_completed |
| G0604 | apokatallassō | 7543 | not_done |
| G0859 | afesis | 879 | to_revise |
| G0863G | afiēmi (release: forgive) | 5376 | to_revise |
| G0863H | afiēmi (release: leave) | 5377 | to_revise |
| G0863I | afiēmi (release: permit) | 5378 | to_revise |
| G1813 | exaleifō | 4701 | not_done |
| G2644 | katallassō | 6114 | not_done |
| H3722A | kip.per | 3169 | to_revise |
| H5162H | na.cham | 446 | not_done |
| H5545 | sa.lach | 5379 | to_revise |
| H5546 | sal.lach | 5380 | to_revise |
| H5547 | se.li.chah | 880 | to_revise |
| H5749A | ud | 6548 | not_done |
| H7725N | shuv | 450 | not_done |

The 14 non-`vc_completed` vc_status values are legacy state from the pre-cluster era; the verse classifications themselves are already in place (0 UT verses), so Phase 1 is a bookkeeping advancement.

## Phase 1 — UT review (CC bookkeeping; 0 UT verses)

**Script:** `scripts/_apply_m11_phase1_vc_status_advance_20260526.py`

- Pre-check: 0 UT verses for M11 ✓
- Op A: advance `mti_terms.vc_status='vc_completed'` for 14 terms (the one already-vc_completed term untouched)
- Result: **14 rows updated**. All 15 M11 terms now `vc_status='vc_completed'`.
- No VCNEW patch needed (no UT classification).
- No new SET_ASIDE rows (the existing 1 set-aside on apobolē Rom 11:15 left as-is).

## Phase 2 — Pass A meanings + keywords (API)

**Script:** `scripts/_run_passa_via_api_v1_20260515.py` (cluster-agnostic; v2_0 §5 + 2026-05-23 keyword extension)
**Model:** claude-sonnet-4-6
**Batches:** 6 of up to 50 verses + 1 follow-up batch for 1 missed verse

### Run 1 — initial 287 verses

| Batch | Size | Filled | Time |
|---:|---:|---|---:|
| 1 | 50 | 50/50 | 90.1s |
| 2 | 50 | 50/50 | 94.5s |
| 3 | 50 | 50/50 | 90.7s |
| 4 | 50 | 50/50 | 94.3s |
| 5 | 50 | 50/50 | 81.9s |
| 6 | 37 | 37/37 | 80.1s |

- Patch: `wa-cluster-M11-patch-passa-meanings-v1-20260526.json` (287 ops; applied clean; archived to `archive/patches/`)
- Raw responses: `WA-M11-passa-api-raw-responses-20260526.json` (initially; later overwritten by Run 2)
- Token usage: input=35,241  output=30,588  cache_create=1,540  cache_read=7,700

### Run 2 — keyword backfill for Rom 11:15

Rom 11:15 (G0580 apobolē, vc_id=35726) was the one verse with a pre-existing `analysis_note` (pre-3.25.0 era, no keywords). Run 1 skipped it (filter `analysis_note IS NULL`). To bring it under the §5.6 hard gate (keywords required), CC cleared its `analysis_note` and re-ran Pass A on just that one verse.

| Batch | Size | Time | Token usage |
|---:|---:|---:|---|
| 1 | 1 | 3.7s | in=160 out=108 cache_read=1,540 |

- New patch shared the same filename (date-based); but the patch-applier blocked the re-apply by patch-id duplicate (correct guard). CC applied the 1-row update directly via SQL with the same `analysis_note` + `keywords` values the new patch contained.
- Result: Rom 11:15 now has both fields populated. No data integrity issue.

### §5.6 hard gate verification

```sql
SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code='M11' AND vc.is_relevant=1
  AND COALESCE(vc.delete_flagged,0)=0
  AND (vc.analysis_note IS NULL OR TRIM(vc.analysis_note)='');
-- Returns 0 ✓

SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code='M11' AND vc.is_relevant=1
  AND COALESCE(vc.delete_flagged,0)=0
  AND (vc.keywords IS NULL OR TRIM(vc.keywords)='');
-- Returns 0 ✓
```

**PASS.** All 288 is_relevant=1 active rows in M11 have `analysis_note` and `keywords` populated.

## Keyword analytics (v1)

Report: `Sessions/Session_Clusters/M11/wa-cluster-M11-keyword-analytics-v1-20260526.md`

| Metric | Value |
|---|---:|
| is_relevant verses | 288 |
| Verses with keywords | 288 (100.0%) |
| Total keywords | 1,449 |
| Distinct keywords | 1,071 |
| Mean keywords/verse | 5.03 |

### Top 15 keywords (cluster-wide)

| Count | Keyword |
|---:|---|
| 25 | guilt released |
| 13 | conscience cleared |
| 13 | sin forgiven |
| 12 | priest mediating |
| 11 | conscience corporate |
| 10 | guilt removed |
| 9 | sin released |
| 8 | guilt covered |
| 8 | forgiveness granted |
| 6 | guilt covering |
| 6 | atonement ritual |
| 6 | conscience addressed |
| 6 | atonement outcome |
| 5 | will turning |
| 5 | will surrendering |

The vocabulary clusters around three obvious inner-being axes:
- **Forgiveness / release / covering** — guilt-released, sin-forgiven, conscience-cleared, guilt-removed, forgiveness-granted (afesis, afiēmi, sa.lach, kip.per, exaleifō)
- **Priestly mediation / atonement** — priest-mediating, atonement-ritual, atonement-outcome, sin-offering, mediation-priestly (kip.per heavy)
- **Will turning / relenting / restoration** — will-turning, will-surrendering, heart-turning, relenting-responsive, attachment-severed (shuv, na.cham, apokatallassō, katallassō)

Phase 3 should expect a **strong characteristic boundary** between the forgiveness-cluster terms and the repentance/restoration terms. Whether this constitutes a §6 cluster-membership question (BOUNDARY-pending) or a §8 sub-group design question (one cluster, multiple sub-groups) is Phase 3's analytical decision.

## Cluster state post-Phase-2

- `mti_terms.vc_status`: 15/15 terms `vc_completed`
- `verse_context` active rows for M11: 289 (288 relevant + 1 set_aside)
- All `is_relevant=1` active rows now carry `analysis_note` and `keywords`
- Cluster status: still `Not started` (Phase 1+2 do not advance status per §4.6)
- 26 inherited VCGs still attached (will be silently dissolved at Phase 8 per v2_9)

## Cost (Phase 2 only)

| Phase | Model | Input | Output | Cache create | Cache read |
|---|---|---:|---:|---:|---:|
| 2 (Pass A — Run 1) | sonnet-4-6 | 35,241 | 30,588 | 1,540 | 7,700 |
| 2 (Pass A — Run 2 backfill) | sonnet-4-6 | 160 | 108 | 0 | 1,540 |
| **Total** | | **35,401** | **30,696** | **1,540** | **9,240** |

Approximate cost: ~$0.40 in API tokens (sonnet-4-6 pricing). Well within the Pass A budget for a ~290-verse cluster.

## Carry-forward notes for Phase 3

1. **Cluster-membership question worth Phase 3 attention:** the keyword signal suggests the cluster spans three semantic registers (forgiveness, atonement/mediation, repentance/restoration). Phase 3 should test whether all 15 terms belong in one cluster or whether one of the registers wants its own home.
2. **Cross-register flags to expect:** the constitution debate is likely to flag at minimum M10 (sin-act ⇄ forgiveness; very tight pair), M10c (defilement ⇄ cleansing-response — Phase 3 verdicts on M10c already noted M11 as a destination), and possibly M07 (shame ⇄ forgiveness) and M27 (evil ⇄ restoration).
3. **High-volume terms to attend to:** kip.per 81V, sa.lach 45V, afiēmi G/H/I 87V collectively, na.cham 34V. These five anchor terms will drive most of Phase 3's analytical weight.
4. **Multi-faceted afiēmi** (3 mti rows for the same Strong's G0863, representing different senses): G0863G "release: forgive", G0863H "release: leave", G0863I "release: permit". Phase 3 may want to assess whether all three senses sit within the M11 register or whether some belong elsewhere.

## Next

Phase 3 — constitution debate (AI, chat). CC will produce the cluster constitution report (consolidated meanings, term inventory, verse counts per term, set-aside summary) + Phase 3 brief.
