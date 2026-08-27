# M10b — Phase 7 obslog — 2026-05-25

**Cluster:** M10b — Wickedness, Evil and Abomination
**Phase:** 7 (VCG design within sub-groups)
**Directive:** `wa-cluster-M10b-dir-002-phase7-vcg-create-v1-20260525.md`
**Governing instruction:** `wa-sessionb-cluster-instruction-v2_8-20260519` §10
**Script:** `scripts/_apply_m10b_phase7_vcg_create_20260525.py`
**Backup:** `backups/bible_research_backup_20260525_125925_M10b-phase7-vcg-create.db`

## AI session output

- 6 per-sub-group design documents (`files phase 7/wa-cluster-M10b-M10b-{A..F}-vcg-design-v1-20260525.md`)
- Unified VCG creation JSON: `files phase 7/wa-cluster-M10b-vcg-creation-v1-20260525.json`

## CC §10.9 validation: PASS

| # | Check | Result |
|---|---|---|
| 1 | Every vc_id in JSON exists in DB as M10b is_relevant active | ✓ 515/515 |
| 2 | No vc_id appears in two VCGs | ✓ 0 duals |
| 3 | Sum of `verses` per sub-group = DB Phase-6 count | ✓ All 6 exact |
| 4 | Every `anchor_vc_id` is in its VCG's `verses` | ✓ 36/36 |
| 5 | BOUNDARY-VCG check | N/A (0 BOUNDARY) |

Two design-doc text discrepancies (M10b-A and M10b-D prose miscounts; JSON authoritative and correct) noted but non-blocking.

## DB writes (single transaction, COMMITTED)

| Op | Description | Rows |
|---|---|---:|
| A | INSERT `verse_context_group` (36 new M10b VCGs) | 36 |
| B | INSERT `vcg_term` links | 53 |
| C | UPDATE `verse_context.group_id` | 515 |
| D | Clear inherited anchors + set Phase 7 anchors | 35 cleared, 36 set |

Post-apply correction: 6 supplementary R4 anchors added (see below).

## VCG distribution

| Sub-group | VCGs | Verses |
|---|---:|---:|
| M10b-A | 11 | 190 |
| M10b-D | 6 | 99 |
| M10b-B | 6 | 90 |
| M10b-E | 5 | 79 |
| M10b-C | 5 | 40 |
| M10b-F | 3 | 17 |
| **TOTAL** | **36** | **515** |

## Three mandatory polysemy VCGs (preserved from Phase 6 obslog)

| VCG | Sub-group | Size | Cross-register | Notes |
|---|---|---:|---|---|
| M10b-A-VCG-01 | Forensic-verdict register | 5 | M10 | ra.sha as legal-status label |
| M10b-B-VCG-01 | Cosmic evil / evil one / evil age | 13 | M27 | ponēros supra-personal sub-corpus |
| M10b-E-VCG-01 | Trouble and distress as affliction | 7 | M03/M27 | a.ven affliction-suffered uses (tighter than the brief's ~18V estimate — the AI's per-verse read identified just the cleaner trouble-register cases) |

## R4 anchor gate — 6 supplementary anchors

The initial Op D set 36 VCG anchors (one per VCG, per Phase 7 design). The R4 post-check identified 6 small terms whose verses sit in VCGs anchored on other terms — R4 requires every term with is_relevant ≥1 to carry ≥1 anchor of its own. CC added one definitional anchor per term:

| Term | Anchor verse | vc_id | VCG |
|---|---|---:|---|
| G0947 bdeluktos (1V) | Tit 1:16 | 27 | M10b-C-VCG-02 |
| G5337 faulos (1V) | 2Cor 5:10 | 14486 | M10b-B-VCG-06 |
| G4189 ponēria (7V) | Rom 1:29 | 14411 | M10b-B-VCG-05 |
| G0093 adikia (8V) | Rom 1:18 | 14336 | M10b-B-VCG-05 |
| G0824 atopos (1V) | Act 25:5 | 65874 | M10b-F-VCG-03 |
| H4849 mir.sha.at (1V) | 2Ch 24:7 | 42511 | M10b-A-VCG-11 |

5 VCGs end up with multiple anchors (the VCG primary + per-term supplementary): M10b-A-VCG-11 (2), M10b-B-VCG-05 (3), M10b-B-VCG-06 (2), M10b-C-VCG-02 (2), M10b-F-VCG-03 (2). Total `is_anchor=1` on M10b verses: **42**.

## §10.6 post-checks: all PASS

- ✓ Every is_relevant vc row has `group_id` set to a new (Phase 7) VCG (0 unrouted)
- ✓ Every VCG has at least one anchor (36 VCG-primary anchors)
- ✓ H3 health check (mti not in VCG term set): 0 violations
- ✓ R4 anchor gate: every term with is_relevant ≥1 has ≥1 anchor

## Cluster state post-Phase-7

- 36 new M10b VCGs (group_code `M10b-{X}-VCG-{NN}`)
- 53 mti_term ↔ VCG links
- 515 active is_relevant verses, all routed
- 42 anchor designations (36 VCG-primary + 6 R4-supplementary)
- Cluster status: `Analysis - In Progress` (unchanged from Phase 6)
- Inherited (pre-cluster-pivot) VCGs still present in DB but no longer referenced by any active is_relevant verse — Phase 8 will dissolve them.

## Next

Phase 8 — Dissolve inherited VCGs (CC, no AI). Identify pre-cluster-pivot `verse_context_group` rows linked to M10b's terms (none expected — M10b is a fresh split with no pre-existing VCG structure). Produce a researcher comparison report before any deletion. If no inherited VCGs to dissolve, Phase 8 is a no-op and the cluster moves directly to Phase 8.5 (BOUNDARY resolution, also a no-op for M10b since Phase 3 produced 0 BOUNDARY verdicts), then Phase 8.7 (characteristic mapping), then Phase 9 (tier findings).
