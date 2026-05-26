# M10c — Phase 8 + Phase 8.7 obslog — 2026-05-26

**Cluster:** M10c — Defilement and Impurity (8 terms · 263V · 5 sub-groups · 26 VCGs)
**Phases:** 8 (silent VCG dissolution) + 8.7 (characteristic mapping)
**Governing instruction:** `wa-sessionb-cluster-instruction-v2_9-20260526` §11 + §11B
**Directives:** §11 — no directive (no-op recorded); §11B — `wa-cluster-M10c-dir-003-phase8_7-characteristic-map-v1-20260526`

---

## Phase 8 — Silent VCG dissolution (v2_9)

**Outcome: NO-OP.**

M10c was constituted from scratch on 2026-05-22 (post-split from the previous M10 — see [[feedback_pre_phase1_split_pattern]]). It had 0 inherited VCGs entering this cluster cycle. The Phase 7 apply created 26 new VCGs against an empty inherited set.

Verification query (executed 2026-05-26 post-Phase-7):

```sql
SELECT vcg.id, vcg.group_code
FROM verse_context_group vcg
JOIN vcg_term vt ON vt.vcg_id = vcg.id
JOIN mti_terms mt ON mt.id = vt.mti_term_id
WHERE mt.cluster_code = 'M10c'
  AND COALESCE(vcg.delete_flagged, 0) = 0
  AND vcg.id NOT IN (<Phase 7 VCG ids>)
GROUP BY vcg.id;
-- Result: 0 rows
```

No directive written; no DB writes. Phase 8 proceeds directly to Phase 8.5.

## Phase 8.5 — BOUNDARY resolution

**Outcome: NO-OP.**

Phase 3 produced 0 BOUNDARY verdicts (every term STAYS; 0 TRANSFERS, 0 BOUNDARY). The `M10c-BOUNDARY` sub-group does not exist (was never created at Phase 5). `BOUNDARY_DECISION_PENDING` count = 0.

No directive written; no DB writes. Phase 8.5 proceeds directly to Phase 8.7.

---

## Phase 8.7 — Characteristic mapping (CC-direct, v2_8/v2_9 §8.0 reduction)

Under v2_8 §8.0 (characteristic-as-objective), the AI's Phase 5 design produces the characteristic identification as a structural input rather than as a separate Phase 8.7 AI debate. M10c's Phase 5 design declared 4 characteristics with one volume-split (M10c-A vs M10c-B → char 1). Phase 8.7 reduces to CC-side loading + carry-forward observation seeding.

### Characteristic map applied

| char_seq | short_name | sub-groups | Volume |
|---:|---|---|---:|
| 1 | Ritual defilement-state | M10c-A + M10c-B | 133V (93 + 40) |
| 2 | Moral-inner defilement-state | M10c-C | 26V |
| 3 | Corporate/covenantal defilement | M10c-D | 83V |
| 4 | Defilement by external spiritual agency | M10c-E | 21V |
| **Total** | — | **5 links** | **263V** |

### §8.6 volume-split rationale (char 1, M10c-A + M10c-B)

- Combined ritual register: 133V / 263V = **50.6%** — breaches §8.6 cap (40%, 105V)
- Split-axis: **mechanism (M10c-A bodily-contact) vs verdict (M10c-B categorical/classificatory)**
- Both sub-groups *fully* serve characteristic 1 (each is a complete register, not a partial VCG-level split); `is_partial=0` for both
- Per [[feedback_phase5_subgroups_represent_characteristics]], the M:N binding preserves characteristic identity across the volume-split

### Carry-forward observations (4 rows, all status=`open`, target_phase=`phase_9_findings`)

1. **SPLIT_DESIGN_RATIONALE on char 1** — Records the §8.6 volume-split rationale for M10c-A vs M10c-B. Phase 9 T1.1 (characteristic in its inner-being aspect) should integrate both registers; T1.2.1 sub-group structural descriptions distinguish them.
2. **INTEGRATION_NOTE on M10c-E (char 4)** — Unclean-spirit register cross-cluster signal to M27 (cosmic-evil agents). Phase 9 T6 (Structural Relationships) attends to M10c (defilement-state) ⇄ M27 (cosmic-evil agency).
3. **INTEGRATION_NOTE on M10c-D (char 3)** — Ezekiel idolatry sub-corpus cross-cluster signal to M10b (Wickedness/Evil/Abomination). Phase 9 T6 attends to M10c-D (defilement of sanctuary/land/name through idolatry) ⇄ M10b-D (idolatry as abomination).
4. **INTEGRATION_NOTE on M10c-C (char 2)** — Moral-inner register has the densest cross-register network (M10, M11, M29, M08, M09). Phase 9 T6 maps the relational pairs explicitly: defilement-state ⇄ sin-act / cleansing-response / desire-vehicle / pride-companion / consecration-opposite.

## Apply

- Script: `scripts/_apply_m10c_phase8_7_characteristic_map_20260526.py --live`
- Backup: `backups/bible_research_backup_20260526_081202_M10c-phase8_7-characteristic-map.db`

| Op | Result |
|---|---|
| A — `characteristic` INSERT | 4 rows (char_seq 1–4) |
| B — `characteristic_subgroup` INSERT | 5 rows (1:2 for char 1; 1:1 for chars 2/3/4) |
| C — `cluster_observation` INSERT | 4 rows (1 SPLIT_DESIGN_RATIONALE + 3 INTEGRATION_NOTE) |

## Post-checks (all PASS)

- ✓ 4 characteristic rows for M10c
- ✓ 5 characteristic_subgroup links
- ✓ All 5 sub-groups have ≥1 characteristic mapping (M10c-A, M10c-B → char 1; M10c-C/D/E → chars 2/3/4)
- ✓ 4 cluster_observation rows seeded with status='open', target_phase='phase_9_findings'

## Cluster state post-Phase-8.7

- Cluster status: `Analysis - In Progress` (unchanged)
- 4 characteristics · 5 characteristic_subgroup links · 4 carry-forward observations
- Ready for Phase 9 — 4 per-characteristic batches + 1 cluster-synthesis batch

## Next

Phase 9 — Catalogue findings. AI authors 189-prompt findings per characteristic, then synthesis. CC builds per-char briefs + structural inputs (the per-batch packaging that worked for M04/M07/M08/M09/M10/M10b).
