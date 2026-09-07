# Phase 5 distribution validation — M09

**Verdict:** ✅ PASS — Phase 6 may proceed
**Generated:** 2026-05-22T03:17:31Z
**Substantive total:** 109 verses
**§8.6 gate:** biggest substantive sub-group ≤ 40.0% of substantive corpus

## Sub-group distribution

| Sub-group | Char | Verses | % of substantive | Status |
|---|---|---:|---:|---|
| `M09-A` | HUMILITY | 37 | 33.9% | ok |
| `M09-B` | HUMILITY | 13 | 11.9% | ok |
| `M09-C` | SUBMISSION | 17 | 15.6% | ok |
| `M09-D` | SUBMISSION | 30 | 27.5% | ok |
| `M09-E` | CONTRITION | 2 | 1.8% | ok |
| `M09-F` | MEEKNESS_GENTLENESS | 2 | 1.8% | ok |
| `M09-G` | DIGNITY | 3 | 2.8% | ok |
| `M09-H` | WILLING_HEARTEDNESS | 5 | 4.6% | ok |
| **TOTAL substantive** | | **109** | 100.0% | |

## §8.6 gate diagnosis

- Biggest: `M09-A` with 37 verses (33.9%)
- Next biggest: `M09-D` (30 verses, 27.5%)

## Phase 8.5 flags (11 diatassō verses)

These are provisionally routed to M09-D for Phase 5/6 structural integrity. Phase 8.5 will resolve: SET-ASIDE or ROUTE-TO-M23.

- vc=55682 G1299 Mat 11:1 → M09-D
- vc=55681 G1299 Luk 3:13 → M09-D
- vc=55673 G1299 Luk 17:9 → M09-D
- vc=55678 G1299 Act 7:44 → M09-D
- vc=55677 G1299 Act 18:2 → M09-D
- vc=55672 G1299 1Cor 7:17 → M09-D
- vc=55676 G1299 1Cor 9:14 → M09-D
- vc=55674 G1299 1Cor 11:34 → M09-D
- vc=55675 G1299 1Cor 16:1 → M09-D
- vc=55679 G1299 Gal 3:19 → M09-D
- vc=55683 G1299 Tit 1:5 → M09-D

## Phase 5.5 set-aside candidate

- vc=21121 G5013 Luk 3:5 (currently in M09-A)

## Phase 6 readiness

§8.6 gate PASS. Phase 6 may proceed. Recommended sequence:

1. (No Phase 5.5 patch needed pre-Phase-6 — keep tapeinoō Luk 3:5 in M09-A; Phase 5.5 patch optional or defer to Phase 8.5 alongside the diatassō flags.)
2. CC builds Phase 6 directive from resolved JSON.
3. Phase 6 routes 109 vc_ids to verse_context_group rows under their respective sub-group codes.

---
*End of v1 validation report.*