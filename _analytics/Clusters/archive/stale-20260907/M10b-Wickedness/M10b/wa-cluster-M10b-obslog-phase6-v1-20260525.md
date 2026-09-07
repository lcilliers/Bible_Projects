# M10b — Phase 6 obslog — 2026-05-25

**Cluster:** M10b — Wickedness, Evil and Abomination (post-split 2026-05-22)
**Phase:** 6 (Verse-to-sub-group mechanical routing + per-sub-group report)
**Directive:** `wa-cluster-M10b-dir-001-phase6-subgroup-assign-v1-20260525.md`
**Governing instruction:** `wa-sessionb-cluster-instruction-v2_8-20260519` §9
**Script:** `scripts/_apply_m10b_phase6_subgroup_assign_20260525.py`
**Backup:** `backups/bible_research_backup_20260525_~_M10b-phase6-subgroup-assign.db`

## DB writes (single transaction, COMMITTED)

| Op | Description | Rows |
|---|---|---:|
| A | INSERT `cluster_subgroup` (M10b-A through M10b-F) | 6 |
| B | INSERT `mti_term_subgroup` (17 primary + 3 secondary) | 20 |
| C | UPDATE `verse_context.cluster_subgroup_id` | 515 |
| D | `cluster.status` `Data - In Progress` → `Analysis - In Progress` | 1 |

## Per-sub-group verse counts (post-apply)

| Sub-group | Characteristic | Verses | % of substantive | Gate |
|---|---|---:|---:|---|
| M10b-A | Wickedness as settled person-identity | 190 | 36.9% | ✓ |
| M10b-D | Idolatrous abomination | 99 | 19.2% | ✓ |
| M10b-B | Evil as constitutional inner nature | 90 | 17.5% | ✓ |
| M10b-E | Iniquity — active inner scheming | 79 | 15.3% | ✓ |
| M10b-C | Abomination — divine-revulsion on moral character | 40 | 7.8% | ✓ |
| M10b-F | Evil expressed through speech | 17 | 3.3% | ✓ |
| **TOTAL** | | **515** | 100.0% | |

Biggest sub-group M10b-A at 36.9% sits below the 40% gate; no §8.6 trigger.

## Multi-faceted term splits (Op B placement)

| Term | Primary | Secondary | Split rule |
|---|---|---|---|
| to.e.vah | M10b-D (72V) | M10b-C (35V) | Passage-group content review: Lev/Deu/historical-reforms/Ezr/Jer/Eze idolatry corpus → D; residual → C |
| bdelugma | M10b-C (4V) | M10b-D (2V) | Mat 24:15 + Mar 13:14 (desolation event) → D; Luk 16:15, Rev 17:4, 17:5, 21:27 (moral abomination) → C |
| ro.a | M10b-E (13V) | M10b-A (1V) | 1Sa 17:28 (evil in heart of specific accused) → A; all others → E |

## to.e.vah split — actual vs AI estimate

The AI's design document estimated `~60 C / ~46 D`. The actual resolution (parsing the AI's explicit D-passage-group list against active vc references) yielded `35 C / 72 D`. The difference stems from the AI's D-list being more comprehensive (full Ezekiel idolatry sweep) than the AI's count estimate suggested. Both sub-groups remain well under the 206-verse gate.

## Phase 7 polysemy notes (preserved for Phase 7 VCG design)

Three sub-groups carry within-sub-group VCG-distinction tasks for Phase 7:

1. **M10b-A ra.sha forensic sub-corpus** (~5V — Exo 23:7, Deu 25:1, 25:2, 1Ki 8:32, 2Ch 6:23): M10 cross-register flag; will receive a distinct VCG.
2. **M10b-B ponēros cosmic-evil sub-corpus** (~10–15V — Mat 13:19, 13:38, Joh 17:15, Eph 6:16, 2Th 3:3, 1Jn 2:13, 2:14, 5:18, 5:19, Gal 1:4, Eph 5:16, 6:13): M27 cross-register flag; will receive a distinct VCG.
3. **M10b-E a.ven trouble/distress sub-corpus** (~18V): M03/M27 cross-register flag; will receive a distinct VCG.

Single-verse flag-only minorities (stay in primary sub-group):
- M10b-B kakia Mat 6:34 (M03 trouble register)
- M10b-B ponēria Eph 6:12 (M27 cosmic-evil)
- M10b-E ro.a Neh 2:2 + Ecc 7:3 (M03 sadness)

## Phase 7 readiness

- Per-sub-group verse-and-meaning report generated per §9.7: `wa-cluster-M10b-subgroup-meanings-v1-20260525.md` (120k chars, 6 sections).
- Cluster status: `Analysis - In Progress` ✓
- All 515 substantive verses routed; 0 unrouted.

## Next

Phase 7 — VCG (Verse Context Group) design within each sub-group. AI session (chat) consumes the per-sub-group meaning report and designs VCGs that subdivide each sub-group into analytically-coherent verse-context groups, with explicit Phase 7 polysemy resolution for the three within-sub-group tasks above.
