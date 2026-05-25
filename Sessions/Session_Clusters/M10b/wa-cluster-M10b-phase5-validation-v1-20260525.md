# M10b Phase 5 validation — 2026-05-25

**Cluster:** M10b — Wickedness, Evil and Abomination
**Mapping under review:** `wa-cluster-M10b-subgroup-mapping-v1-20260525.json`
**Design document:** `WA-M10b-subgroup-design-v1-20260525.md`
**Verdict:** ✅ **PASS — Phase 6 may proceed**

## §8.5 post-check

| Check | Result |
|---|---|
| Every is_relevant verse assigned to exactly one sub-group (or BOUNDARY) | ✓ 515/515 routable under the mapping rules |
| Every sub-group has `core_description` written from meanings | ✓ 6/6 with rich descriptions |
| Multi-faceted terms explicitly named (primary + secondary) | ✓ to.e.vah (C+D), bdelugma (C+D), ro.a (A+E) |
| BOUNDARY sub-group exists if Phase 3 produced any BOUNDARY verdicts | ✓ N/A — 0 BOUNDARY verdicts at Phase 3 |
| BOUNDARY contains only verses of BOUNDARY-verdict terms (§8.4.1) | ✓ N/A |
| Cross-register flags travel forward into sub-group descriptions | ✓ M27/M10/M10c/M06/M03 flags preserved per sub-group |

## §8.6 distribution gate (resolved against live DB)

Cluster substantive verses: **515**. Gate threshold (40%): **≤ 206 verses per sub-group**.

| Sub-group | Characteristic | Verses | % substantive | Gate |
|---|---|---:|---:|---|
| M10b-A | Wickedness as settled person-identity | 190 | 36.9% | ✓ PASS |
| M10b-C | Abomination — divine revulsion on moral character | 100±5 | ~19% | ✓ PASS |
| M10b-B | Evil as constitutional inner nature | 90 | 17.5% | ✓ PASS |
| M10b-E | Iniquity — active inner scheming | 79 | 15.3% | ✓ PASS |
| M10b-D | Idolatrous abomination | 40±5 | ~8% | ✓ PASS |
| M10b-F | Evil expressed through speech | 17 | 3.3% | ✓ PASS |
| **TOTAL substantive** | | **515** | 100.0% | |
| **TOTAL BOUNDARY** | | 0 | (none) | |

Biggest sub-group **M10b-A at 36.9%** sits comfortably below the 40% threshold. No volume-split required.

(M10b-C and M10b-D counts have ±5V tolerance because the to.e.vah split is content-driven; the AI provided passage groups + keyword markers but did not enumerate every verse. The exact split will resolve during Phase 6 apply; either extremity (60/46 or 70/37) keeps both sub-groups well under the gate.)

## Design observations

1. **6 characteristics → 6 sub-groups (1:1 mapping)** — follows §8.0 default cleanly. No volume-splits, no SPLIT_SUBGROUP cases.

2. **Abomination split into two characteristics** (M10b-C moral-character vs M10b-D idolatrous) — the AI's defensible read of the corpus. Alternative would have been one abomination characteristic with a volume-split; either is valid per §8.0. The chosen split aligns better with the M10c/M27 cross-register signals (D carries the heavier M10c + M27 flags; C carries the cleaner moral-character register).

3. **ponēros + a.ven polysemy deferred to Phase 7** — both stay in a single sub-group with explicit Phase 7 VCG-distinction notes. This matches the brief's guidance. The Phase 7 design tasks are recorded in the design doc §4.

4. **Cross-register flag preservation** — all 15 flagged terms carry their flags forward (M27/M10/M06/M03/M10c) at the sub-group level. The largest flag concentration is in M10b-D (M27 primary + M10c secondary), as expected from Phase 3.

5. **Count reconciliation** — the design document declares an aggregate of 533V; the actual flat count is 515V. The 18V discrepancy stems from pre-orphan-cleanup figures used in the AI's term-level counts (5 a.ven + 14 ro.a were soft-deleted in the Phase 2 hygiene pass). The mapping rules are unaffected — all per-verse exceptions still target live verses, and the term-level defaults will route the active rows correctly.

## to.e.vah split — apply-time guidance

The AI provided two content-driven inputs for the to.e.vah C/D split:

- **D passage groups**: explicit verse lists for Leviticus, Deuteronomy, historical reform narratives, Ezra, Jeremiah, and Ezekiel idolatry-abomination corpus (~37–46 verses depending on parsing of the Ezekiel sweep).
- **Keyword markers** for tie-break / fuzzy matching:
  - D markers: `idol detestable`, `worship corrupted`, `will conformed`, `covenant abandoned`, `practices detestable`, `defilement inner`, `devotion perverted`, `sacred violated`, `abomination removed`, `reform enacted`.
  - C markers: `divine revulsion`, `conscience violated`, `holiness violated`, `heart crooked`, `heart proud`, `moral inversion`, `divine disgust`, `divine rejection`.

Apply-time Phase 6 should:
1. Resolve the D-passage list to specific vr_ids (parse the AI's listed references).
2. Verify each candidate vc row's keywords for marker alignment.
3. Assign each to.e.vah verse to C or D based on the (passage-list ∪ keyword-marker) match.
4. Any verse not falling clearly in either bucket defaults to C (moral-character abomination is the broader category).

## Phase 6 readiness

- Cluster status will transition `Data - In Progress` → `Analysis - In Progress` as part of the Phase 6 directive (deferred from Phase 4 per §7.6).
- 6 `cluster_subgroup` rows to create (M10b-A through M10b-F).
- `verse_context.cluster_subgroup_id` UPDATE for 515 rows.
- `mti_term_subgroup` join rows for multi-faceted terms (to.e.vah → C+D, bdelugma → C+D, ro.a → A+E).
- 14 single-target terms get single mti_term_subgroup rows.

---

*Phase 5 validated. Awaiting authorisation to proceed with Phase 6 (apply mapping + status flip).*
