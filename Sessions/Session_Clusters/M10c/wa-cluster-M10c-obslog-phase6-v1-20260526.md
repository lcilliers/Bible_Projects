# M10c — Phase 6 obslog — 2026-05-26

**Cluster:** M10c — Defilement and Impurity
**Phase:** 6 (sub-group structural apply + verse routing)
**Governing instruction:** `wa-sessionb-cluster-instruction-v2_8-20260519` §9
**Directive:** `wa-cluster-M10c-dir-001-phase6-subgroup-assign-v1-20260526`

## Inputs read

- AI Phase 5 design: `wa-cluster-M10c-subgroup-design-v1_0-20260526.md` (5 sub-groups, §8.6 gates PASS)
- AI Phase 5 mapping: `wa-cluster-M10c-subgroup-mapping-v1_0-20260526.json`
- Pass A meanings: `wa-cluster-M10c-passa-meanings-v1-20260526.json` (used to resolve 3 gap verses)

## Pre-apply validation

- All 8 terms have an assignment entry; per-verse-range entries cover 4 terms, term-level cover 4 terms
- Live DB resolution: 260/263 routable from `verse_ranges`; **3 unassigned**: Num 5:3, Hag 2:13, Zec 13:1
- Gap-fix decisions (from Pass A meaning content):
  - **Num 5:3** (ta.me verb): "do not defile the camp in which I dwell" → corporate/sanctuary register → **M10c-D**
  - **Hag 2:13** (ta.me adj): "one defiled by a corpse touches food → it becomes unclean" → bodily-contact contagion → **M10c-A**
  - **Zec 13:1** (nid.dah): "a fountain opened … for sin and uncleanness" → corporate-prophetic cleansing → **M10c-D**

## Apply

- Script: `scripts/_apply_m10c_phase6_subgroup_assign_20260526.py --live`
- Backup: `backups/bible_research_backup_20260526_070410_M10c-phase6-subgroup-assign.db`
- First live attempt aborted before DB transaction (JSON serialization on tuple keys in GAP_FIXES `_meta` payload). Script patched (gap-fixes serialised as list of dicts); re-run succeeded.

## Operations result

| Op | Target | Result |
|---|---|---|
| A | `cluster_subgroup` INSERT | 5 rows (ids 162–166) |
| B | `mti_term_subgroup` INSERT | 16 rows (primary + secondaries) |
| C | `verse_context.cluster_subgroup_id` UPDATE | 263 rows |
| D | `cluster.status` UPDATE | `Data - In Progress` → `Analysis - In Progress` |

## Sub-group verse distribution

| Sub-group | Verses | §8.6 gate (≤105) |
|---|---:|---|
| M10c-A — Bodily-contact defilement-state | 93 | ✓ PASS |
| M10c-B — Categorical/classificatory unclean-state | 40 | ✓ PASS |
| M10c-C — Moral-inner defilement-state | 26 | ✓ PASS |
| M10c-D — Corporate/covenantal defilement | 83 | ✓ PASS |
| M10c-E — Defilement by external spiritual agency | 21 | ✓ PASS |
| **Total** | **263** | — |

## Per-term sub-group placements

| Strong's | Translit | V | Sub-groups |
|---|---|---:|---|
| H2930A | ta.me (verb) | 128 | M10c-A=50, M10c-D=63, M10c-B=15 |
| H2931 | ta.me (adj) | 66 | M10c-A=28, M10c-B=21, M10c-D=11, M10c-C=6 |
| G0169 | akathartos | 30 | M10c-E=21, M10c-C=5, M10c-B=4 |
| H5079 | nid.dah | 24 | M10c-A=15, M10c-D=9 |
| G0167 | akatharsia | 10 | M10c-C=10 |
| G3435 | molunō | 3 | M10c-C=3 |
| G3436 | molusmos | 1 | M10c-C=1 |
| G3394 | miasmos | 1 | M10c-C=1 |

## Post-checks

- ✓ 0 unrouted is_relevant rows for M10c
- ✓ cluster.status = 'Analysis - In Progress'
- ✓ 5 cluster_subgroup rows, 16 mti_term_subgroup rows, 263 vc rows routed
- ✓ Sub-group totals match Phase 5 design (93/40/26/83/21)

## Artefacts written

- `Sessions/Session_Clusters/M10c/wa-cluster-M10c-subgroup-mapping-resolved-v1-20260526.json` — flat vc_id→subgroup_code resolution (post gap-fix), for audit
- `Sessions/Session_Clusters/M10c/wa-cluster-M10c-subgroup-meanings-v1-20260526.md` — Phase 7 input report (per-sub-group verse + meaning corpus)

## Cluster state post-Phase-6

- 263 routed is_relevant rows · 5 sub-groups · cluster status `Analysis - In Progress`
- Phase 7 input ready (per-sub-group verse-meaning corpus)
- No new cluster_observation rows from Phase 6 (rationale captured in Phase 5 design doc and validation report; SUBGROUP_DESIGN_RATIONALE and SPLIT_DESIGN_RATIONALE seeding deferred to Phase 8.7 carry-forwards per cluster precedent)

## Next

Phase 7 — VCG design within sub-groups (AI, chat). Input report already written. CC writes Phase 7 brief and hands off.
