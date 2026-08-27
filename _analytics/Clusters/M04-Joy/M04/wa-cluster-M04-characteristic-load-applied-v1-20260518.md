# M04 characteristic + observation schema load applied

**Date:** 2026-05-18 17:45
**Migration:** M49 (schema 3.22.0 → 3.23.0)
**Source:** M04-characteristic-map-v4-20260518

## Operations applied

**Schema (M49):**
- CREATE TABLE `characteristic` + 1 index
- CREATE TABLE `characteristic_subgroup` + 2 indexes
- CREATE TABLE `cluster_observation` + 3 indexes (partial unique on target_phase WHERE status='open')

**M04 data load:**
- INSERT 7 `characteristic` rows for M04
- INSERT 17 `characteristic_subgroup` links (16 sub-groups + M04-E partial second link)
- INSERT 4 `cluster_observation` rows (Phase 9 carry-forward notes)

## Characteristic inventory (M04)

| Seq | Short name |
|---:|---|
| 1 | Exultation |
| 2 | Joy |
| 3 | Gladness |
| 4 | Delight |
| 5 | Pleasure |
| 6 | Wonder |
| 7 | Suffering-Joy |

## Sub-group → characteristic mapping

| Sub-group | Characteristic(s) |
|---|---|
| M04-A | Exultation |
| M04-B | Joy |
| M04-C | Joy |
| M04-D | Joy |
| M04-E | Joy + Suffering-Joy |
| M04-F | Suffering-Joy |
| M04-G | Delight |
| M04-H | Delight |
| M04-I | Wonder |
| M04-J | Pleasure |
| M04-K | Pleasure |
| M04-L | Gladness |
| M04-M | Delight |
| M04-N | Delight |
| M04-O | Gladness |
| M04-P | Delight |

## Carry-forward observations (4)

| id | type | title | target_phase | status |
|---:|---|---|---|---|
| 1 | `INTER_RELATIONSHIP` | Joy/Gladness inter-relationship within M04-B and M04-C | phase_9_findings | open |
| 2 | `SPLIT_SUBGROUP` | M04-E serves both Characteristic 2 (Joy) and Characteristic 7 (Suffering-Joy) | phase_9_findings | open |
| 3 | `INTER_RELATIONSHIP` | Delight's breadth — affective/volitional/obedience/relational/corrupt inter-relationships | phase_9_findings | open |
| 4 | `INTEGRATION_NOTE` | M04-L evaluative-cognitive face integrates with M04-O circumstantial under Gladness | phase_9_findings | open |

## Next steps

1. Backfill: closed clusters (M01, M02, M03, M05, M06, M15, M20, M26, M39, M46) need their characteristic mapping done analogously to M04. Tracked in memory item `project-characteristic-backfill-backlog`.
2. M04 Phase 9: proceed under the new model — 189 prompts apply per characteristic (across constituent sub-groups). Layered v2 architecture (VCG-level Layer 1 → cluster aggregation Layer 2) sits on top.
3. v2_6 instruction draft: deferred until M04 Phase 9 validates the new model.

---

*End of apply report.*