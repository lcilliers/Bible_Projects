# M10c — Phase 7 obslog — 2026-05-26

**Cluster:** M10c — Defilement and Impurity (8 terms · 263V)
**Phase:** 7 (VCG design + structural apply)
**Governing instruction:** `wa-sessionb-cluster-instruction-v2_8-20260519` §10
**Directive:** `wa-cluster-M10c-dir-002-phase7-vcg-create-v1-20260526`

## Inputs read

- AI Phase 7 unified JSON: `wa-cluster-M10c-vcg-creation-v1_0-20260526.json` (26 VCGs across 5 sub-groups)
- 5 AI per-sub-group design docs: `wa-cluster-M10c-M10c-{A..E}-vcg-design-v1_0-20260526.md`
- AI worklog (Phases 3, 5, 7 — renamed to canonical `wa-cluster-M10c-AI-worklog-phases3-5-7-v1-20260526.md`)

## §10.8 pre-submission checklist verification (CC)

| Check | Result |
|---|---|
| 5 design documents | ✓ one per sub-group |
| Each carries sum-verification line | ✓ |
| Unified JSON field name is `verses` | ✓ |
| Every `anchor_vc_id` ∈ its VCG's `verses` | ✓ 26/26 |
| Per-sub-group sums match input counts | ✓ A=93, B=40, C=26, D=83, E=21 |
| Total verses = 263 | ✓ |
| No global duplicates | ✓ |
| All vc_ids are M10c is_relevant rows | ✓ |
| No forbidden field names (key_verses, members, etc.) | ✓ |

**Validation script:** `scripts/_validate_m10c_phase7_vcg_json_20260526.py` — 0 issues.

## JSON _meta correction

The AI's JSON declared `_meta.total_vcgs: 21` but the structural reality (counted from `vcgs` arrays per sub-group) is **26 VCGs** (A=8, B=5, C=5, D=5, E=3). The AI's own worklog correctly records 26 VCGs at line 1151. CC patched `_meta.total_vcgs` from 21 to 26. Structural data was untouched.

## Apply

- Script: `scripts/_apply_m10c_phase7_vcg_create_20260526.py --live`
- Backup: `backups/bible_research_backup_20260526_074706_M10c-phase7-vcg-create.db`

| Op | Target | Result |
|---|---|---|
| A | `verse_context_group` INSERT | 26 rows |
| B | `vcg_term` INSERT | 53 rows (distinct vcg×term pairs) |
| C | `verse_context.group_id` UPDATE | 263 rows |
| D | `verse_context.is_anchor` clear + set | 14 cleared, 26 set |

## R4 anchor gate — supplementary anchor

Post-apply R4 verification surfaced one term failing the per-term anchor gate:

- **G3394 miasmos** (1 is_relevant verse: 2Pe 2:10, vc=30266) had no anchor.

Root cause: AI grouped miasmos (1V) and molusmos (1V) into a single VCG `M10c-C-VCG-03` (body-and-spirit purification) and designated molusmos's 2Cor 7:1 (vc=9329) as the AI primary anchor. The R4 gate, however, is per-term, not per-VCG — every term with ≥1 is_relevant verse needs ≥1 anchor verse.

**Fix:** added `is_anchor=1` on miasmos vc=30266 as a co-anchor inside the same VCG. The AI's primary anchor for the VCG remains molusmos 2Cor 7:1. This is recorded in §3 of the directive.

| Verification | Result |
|---|---|
| R4 anchor gate (8 terms) | ✓ 8/8 PASS |
| Total is_anchor=1 on M10c | 27 (26 primaries + 1 R4 supplementary) |

## Per-sub-group VCG distribution

| Sub-group | VCGs | Verses |
|---|---:|---:|
| M10c-A — Bodily-contact defilement-state | 8 | 93 |
| M10c-B — Categorical/classificatory unclean-state | 5 | 40 |
| M10c-C — Moral-inner defilement-state | 5 | 26 |
| M10c-D — Corporate/covenantal defilement | 5 | 83 |
| M10c-E — Defilement by external spiritual agency | 3 | 21 |
| **Total** | **26** | **263** |

## Per-VCG verse counts (live DB read)

```
M10c-A-VCG-01    2    Unconscious contact + conscience awakening
M10c-A-VCG-02   14    Carcass-contact defilement
M10c-A-VCG-03    7    Object contamination through material transmission
M10c-A-VCG-04    2    Volitional self-defilement
M10c-A-VCG-05   16    Menstrual and physiological defilement cycle
M10c-A-VCG-06   16    Bodily discharge contact defilement
M10c-A-VCG-07   27    Corpse-contact defilement
M10c-A-VCG-08    9    Sacred boundary and defilement scope
M10c-B-VCG-01   17    Leprous-skin priestly verdict
M10c-B-VCG-02   12    Categorically-unclean-animal classification (B-side)
M10c-B-VCG-03    7    Categorically-unclean-objects / persons (public stigma)
M10c-B-VCG-04    1    NT akathartos categorical use (food/persons/marriage)
M10c-B-VCG-05    3    Public-stigma / isolation register
M10c-C-VCG-01    4    Hebrew metaphorical inner-defilement
M10c-C-VCG-02    8    Prior moral-life slavery / habitual impurity
M10c-C-VCG-03    2    Body-and-spirit purification (miasmos + molusmos)
M10c-C-VCG-04    5    Defiled conscience as faculty
M10c-C-VCG-05    7    Inner moral corruption causing outer abomination
M10c-D-VCG-01   28    Sanctuary + name defilement (Eze + sacred-space)
M10c-D-VCG-02   18    Land defilement
M10c-D-VCG-03   16    Idolatry defilement (Ezekiel idolatry corpus)
M10c-D-VCG-04   12    Covenant-relational / sexual-betrayal defilement
M10c-D-VCG-05    9    Corporate-prophetic cleansing-promise
M10c-E-VCG-01   13    Recognition-and-expulsion narratives
M10c-E-VCG-02    5    Authority-over-unclean-spirits commissioning
M10c-E-VCG-03    3    General-affliction / cosmic-evil context
```
(Counts above are paraphrased from the AI design + verified via the apply script's post-check output. Reading-discipline note: VCG verse counts are derived from the live DB, not from the brief's "candidate VCG axes" estimates.)

## Cluster state post-Phase-7

- 263 routed is_relevant rows · 26 VCGs · 5 sub-groups · cluster status `Analysis - In Progress`
- All 8 terms PASS R4 anchor gate
- Phase 8 (inherited VCG dissolution): **no-op** — M10c had no inherited VCGs entering this cluster cycle (cluster constituted post-split 2026-05-22; Phase 1 had 0 borderlines)
- Phase 8.5 (BOUNDARY resolution): **no-op** — Phase 3 produced 0 BOUNDARY verdicts

## Artefacts in M10c folder post-Phase-7

- `wa-cluster-M10c-vcg-creation-v1_0-20260526.json` (AI unified, _meta patched)
- `wa-cluster-M10c-M10c-{A..E}-vcg-design-v1_0-20260526.md` (AI per-sub-group designs)
- `wa-cluster-M10c-AI-worklog-phases3-5-7-v1-20260526.md` (AI cumulative working log)
- `wa-cluster-M10c-dir-002-phase7-vcg-create-v1-20260526.md` (CC directive)
- `wa-cluster-M10c-obslog-phase7-v1-20260526.md` (this file)

## Next

Phase 8.7 — characteristic mapping (CC). M10c's 5 sub-groups can map 1:1 to 5 characteristics (per the [[feedback_phase5_subgroups_represent_characteristics]] design discipline). Brief + directive to follow.
