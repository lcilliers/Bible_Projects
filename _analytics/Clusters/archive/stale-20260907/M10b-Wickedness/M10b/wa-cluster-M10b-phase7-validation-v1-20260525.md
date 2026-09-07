# M10b Phase 7 validation — 2026-05-25

**Cluster:** M10b — Wickedness, Evil and Abomination
**Unified JSON under review:** `files phase 7/wa-cluster-M10b-vcg-creation-v1-20260525.json`
**Design docs:** 6 (one per sub-group, in `files phase 7/`)
**Verdict:** ✅ **PASS — Phase 7 apply may proceed**

## §10.9 CC validation checks

| # | Check | Result |
|---|---|---|
| 1 | Every vc_id exists in DB with is_relevant=1, delete_flagged=0, cluster_code=M10b | ✓ 515/515 exist; 0 phantoms; 0 missing |
| 2 | No vc_id appears in two VCGs (no double-membership) | ✓ 0 duals |
| 3 | Sum of `verses` per sub-group = DB Phase-6 count | ✓ All 6 sub-groups exact |
| 4 | Every `anchor_vc_id` is in its VCG's `verses` array | ✓ 36/36 anchors valid |
| 5 | BOUNDARY-VCG check | N/A (0 BOUNDARY-verdict terms at Phase 3) |

### Per-sub-group reconciliation

| Sub-group | DB | AI JSON | Match |
|---|---:|---:|---|
| M10b-A | 190 | 190 | ✓ |
| M10b-B | 90 | 90 | ✓ |
| M10b-C | 40 | 40 | ✓ |
| M10b-D | 99 | 99 | ✓ |
| M10b-E | 79 | 79 | ✓ |
| M10b-F | 17 | 17 | ✓ |
| **TOTAL** | **515** | **515** | ✓ |

## VCG count summary (36 total)

| Sub-group | VCGs | Verses | Avg |
|---|---:|---:|---:|
| M10b-A | 11 | 190 | 17.3 |
| M10b-D | 6 | 99 | 16.5 |
| M10b-B | 6 | 90 | 15.0 |
| M10b-E | 5 | 79 | 15.8 |
| M10b-C | 5 | 40 | 8.0 |
| M10b-F | 3 | 17 | 5.7 |
| **TOTAL** | **36** | **515** | **14.3** |

VCG count lands within the brief's expected range (25–45).

## Three mandatory polysemy VCGs — all present

| Sub-group | VCG | Verses | Cross-register flag |
|---|---|---:|---|
| M10b-A-VCG-01 | Forensic-verdict register | 5 | M10 |
| M10b-B-VCG-01 | Cosmic evil — the evil one, the evil age | 13 | M27 |
| M10b-E-VCG-01 | Trouble and distress as the affliction of evil | 7 | M03/M27 |

(Note: M10b-E-VCG-01 at 7V is smaller than the brief's ~18V estimate. The AI's per-verse reading identified a tighter trouble-register set — likely because many a.ven Psalms uses describe evildoers as agents rather than the trouble they cause. The smaller VCG is acceptable since the §10.9 sum check passes.)

## Design-doc text discrepancies (informational, non-blocking)

Two design documents contain prose miscounts that do NOT affect the apply (the JSON is authoritative and validates clean):

- **M10b-A design doc** reports its sum as `5+8+22+19+29+21+22+12+31+9+10 = 188; 2V unresolved discrepancy flagged for CC validation. Expected 190 ✓ pending CC resolution.`
  Actual JSON sum: `5+8+22+18+30+21+22+12+33+9+10 = 190` — JSON is correct; the design doc text has 3 off-by-one count errors that net to -2. The VCG member lists in the JSON are complete.

- **M10b-D design doc** reports its sum as `6+14+17+14+42+5 = 98; 1V unresolved discrepancy flagged for CC validation. Expected 99 ✓ pending CC resolution.`
  Actual JSON sum: `6+14+17+14+43+5 = 99` — JSON is correct; the design doc text has 1 off-by-one error on VCG-05 (43 vs 42).

Both are documentation-prose drift, not data errors. The JSON's member arrays are the operational truth; CC's §10.9 validation operates against the JSON and confirms 190 and 99 exactly.

## Spot-check observations

- **M10b-A-VCG-09 (Wickedness against divine justice — 33V)** — the largest M10b VCG. Proverbs-heavy corpus addressing the wicked person's soul, appetites, and moral hollowness.
- **M10b-D-VCG-05 (Ezekiel idolatry — 43V)** — concentrated Ezekiel idolatry-driving-divine-presence-away corpus. Strong M27 cross-register cluster.
- **M10b-A** has 11 VCGs (largest VCG count) — appropriate for the 190V corpus, allowing fine-grained register-distinction within the wicked-person characteristic.
- **M10b-C-VCG-05 (Identity and choice constituted by abomination — 6V)** — picks up the harder-to-classify bdelugma verses (Rev 17:4/5/21:27) and similar identity-constitution uses. Good catch.

## Cross-register flag preservation

The AI preserved cross-register flags in VCG descriptions where Phase 3/Phase 5 noted them:
- M10b-A-VCG-01 — M10 flag (forensic-verdict)
- M10b-B-VCG-01 — M27 flag (cosmic-evil)
- M10b-D-VCG-* — M27 / M10c flags (idolatry sub-corpora)
- M10b-E-VCG-01 — M03/M27 flag (trouble register)
- M10b-F-VCG-01 — M06 flag (blasfēmeō hardened-defiance)

## Phase 7 apply readiness

The unified JSON is structurally valid and matches DB ground truth. Proceeding to apply:

- Op A: INSERT 36 `verse_context_group` rows (one per VCG)
- Op B: INSERT `vcg_term` links — one per (VCG, term) where the VCG covers any of the term's verses
- Op C: UPDATE `verse_context.group_id` for all 515 vc rows
- Op D: UPDATE `verse_context.is_anchor=1` for the 36 Phase 7 anchors; reset prior anchors to 0 within M10b's terms (except those preserved)

---

*Phase 7 validated. Proceeding with apply directive.*
