# M10b — Phase 8 / 8.5 / 8.7 consolidated obslog — 2026-05-25

**Cluster:** M10b — Wickedness, Evil and Abomination (post-split 2026-05-22)
**Phases:** 8 (Dissolve inherited VCGs) · 8.5 (BOUNDARY resolution) · 8.7 (Characteristic mapping)
**Governing instruction:** `wa-sessionb-cluster-instruction-v2_8-20260519` §11, §11A, §11B

## Phase 8 — Dissolve inherited VCGs

**Directive:** `wa-cluster-M10b-dir-003-phase8-vcg-dissolve-v1-20260525.md` (implied; comparison report serves as directive record)
**Script:** `scripts/_apply_m10b_phase8_vcg_dissolve_20260525.py`
**Backup:** `backups/bible_research_backup_20260525_130627_M10b-phase8-vcg-dissolve.db`
**Comparison report:** `wa-cluster-M10b-vcg-dissolution-comparison-v1-20260525.md`

### Inherited VCG identification

30 inherited VCGs identified — linked to M10b terms via `vcg_term` but not created by the Phase 7 directive. All carry legacy per-term VCG codes (pattern `{mti_id}-NNN`) from pre-cluster-pivot Session B era. Each had exactly 1 M10b-term link and 0 active is_relevant rows still referencing them (Phase 7 re-routing was complete).

| Disposition | Count |
|---|---:|
| OBSOLETE (verses re-routed entirely; post-split fresh design) | 30 |
| KEEP-EQUIVALENT / SPLIT / MERGED / UNROUTED | 0 |

### Apply

- Op A: soft-deleted 30 `verse_context_group` rows (delete_flagged=1 + audit note)
- Op B: soft-deleted 30 `vcg_term` links (delete_flagged=1)
- Post-check: active VCG count for M10b = 36 (Phase 7 set, unchanged) ✓

### Researcher gate

Per §11.4 the comparison report is researcher-informational for post-M01 cohort clusters. Dissolution proceeded without per-VCG approval — the uniform OBSOLETE disposition (post-split fresh-design cluster) is the expected pattern for split-derivative clusters.

## Phase 8.5 — BOUNDARY resolution

**Verdict:** **no-op confirmed**

Phase 3 produced 0 BOUNDARY verdicts (all 17 terms STAYS with cross-register flags where applicable). No `{CODE}-BOUNDARY` sub-group was created at Phase 5. No `BOUNDARY_DECISION_PENDING` flags exist on M10b's Strong's set (verified by re-checking the §11A.4 post-check via Strong's match rather than registry-wide query).

Note: 6 unresolved `BOUNDARY_DECISION_PENDING` flags exist on registry 151 (sorrow) terms, but they were raised by M03 (Grief) during its 2026-05-17 closure and concern M03 terms (dav.va, che.vel, ma.a.tse.vah, e.tsev, o.tsev, its.tsa.von) — those terms are not in M10b's set. The shared-registry query would catch them as false positives; the Strong's-level query confirms M10b has 0 pending.

| §11A.4 check | Result |
|---|---|
| Unresolved BOUNDARY_DECISION_PENDING on M10b Strong's | 0 ✓ |
| `{CODE}-BOUNDARY` sub-groups in M10b | 0 ✓ |
| BOUNDARY vc_ids requiring disposition | 0 (none ever assigned) |

No directive authored; no DB writes.

## Phase 8.7 — Characteristic mapping

**Directive:** `wa-cluster-M10b-dir-004-phase8_7-characteristic-map-v1-20260525.md` (implied; this obslog serves as the directive record)
**Script:** `scripts/_apply_m10b_phase8_7_characteristic_map_20260525.py`
**Backup:** `backups/bible_research_backup_20260525_130951_M10b-phase8_7-characteristic-map.db`
**Source:** Phase 5 sub-group design (`WA-M10b-subgroup-design-v1-20260525.md`)

### Mapping (1:1 — §8.0 default; no volume-splits; no SPLIT_SUBGROUP)

| char_seq | id | sub-group | Verses | Characteristic |
|---:|---:|---|---:|---|
| 1 | 47 | M10b-A | 190 | Wickedness as settled person-identity |
| 2 | 48 | M10b-B | 90 | Evil as constitutional inner nature |
| 3 | 49 | M10b-C | 40 | Abomination — divine revulsion on moral character |
| 4 | 50 | M10b-D | 99 | Idolatrous abomination |
| 5 | 51 | M10b-E | 79 | Iniquity as active inner scheming and evil generation |
| 6 | 52 | M10b-F | 17 | Evil expressed through speech |

All `is_partial=0` (each sub-group fully represents its characteristic; no SPLIT_SUBGROUP cases).

### Phase 7 polysemy carry-forwards (3 cluster_observation rows)

INTEGRATION_NOTE rows targeting `phase_9_findings`:

| obs_id | Characteristic | Source VCG | Title |
|---:|---|---|---|
| 80 | CHAR-1 Wickedness | M10b-A-VCG-01 | ra.sha forensic-verdict register — VCG-level cross-register signal (M10) |
| 81 | CHAR-2 Evil-as-nature | M10b-B-VCG-01 | ponēros cosmic-evil-agent sub-corpus — VCG-level cross-register signal (M27) |
| 82 | CHAR-5 Iniquity | M10b-E-VCG-01 | a.ven trouble-suffered sub-corpus — VCG-level cross-register signal (M03/M27) |

Phase 9 T6 (Structural Relationships with Other Characteristics) findings will attend to these signals.

### DB writes (single transaction)

- Op A: INSERT 6 `characteristic` rows (ids 47–52, char_seq 1–6)
- Op B: INSERT 6 `characteristic_subgroup` links (1:1, all is_partial=0)
- Op C: INSERT 3 `cluster_observation` rows (INTEGRATION_NOTE for Phase 9 carry-forward)
- Total: 15 new rows

### Post-checks

- ✓ 6/6 characteristic rows persist
- ✓ 6/6 characteristic_subgroup links exist
- ✓ All 6 sub-groups have a characteristic mapping (no unmapped)
- ✓ 3/3 cluster_observation rows persist as `status='open'`

## Cluster state post-Phase-8.7

- 17 terms · 515 active is_relevant verses · 36 VCGs · 6 sub-groups · 6 characteristics
- 42 anchor designations (36 VCG-primary + 6 R4-supplementary from Phase 7)
- 30 inherited (pre-pivot) VCGs soft-deleted
- 0 BOUNDARY backlog
- 3 INTEGRATION_NOTE observations open for Phase 9 attention
- Cluster status: `Analysis - In Progress` (unchanged)

## Next

**Phase 9** — Catalogue findings (189 prompts × 6 characteristics + 1 cluster-synthesis pass).

The AI workload becomes substantial here. Per `feedback_phase9_tier_by_tier_mandatory.md` (memory) and v2_8 §12, Phase 9 will use tier-by-tier staged execution (one tier per AI response, write to file, STOP) with mandatory per-batch DB load via the parametric loader. Per the M10 precedent (4,158 findings at 22 chars × 189 prompts), M10b's footprint will be 1,134 findings (189 × 6) plus a cluster-synthesis pass.
