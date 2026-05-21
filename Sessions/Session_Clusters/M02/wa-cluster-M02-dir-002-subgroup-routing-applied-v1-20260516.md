# WA-M02-dir-002-subgroup-routing-applied-v1-20260516

**Phase 6 (v2_2):** Sub-group creation + term placement + verse routing
**Apply timestamp:** 2026-05-16T12:29:58Z
**Loader:** [scripts/_apply_m02_phase6_subgroup_routing_20260516.py](../../../scripts/_apply_m02_phase6_subgroup_routing_20260516.py)
**Directive:** [wa-cluster-M02-dir-002-subgroup-routing-v1-20260516.md](wa-cluster-M02-dir-002-subgroup-routing-v1-20260516.md)
**Governing instruction:** wa-sessionb-cluster-instruction-v2_2-20260516 §9

---

## Outcome

**7 sub-groups created · 52 term placements · 641 verses routed.** Single transaction. All health checks pass.

| Operation | Rows |
|---|---:|
| A — INSERT `cluster_subgroup` | 7 |
| B — INSERT `mti_term_subgroup` | 52 (43 primary + 9 secondary) |
| C — UPDATE `verse_context.cluster_subgroup_id` | 641 |
| **Total DB writes** | **700** |

## Sub-groups created

| Code | Label | Terms (primary) | Verses |
|---|---|---:|---:|
| M02-A | Divine Wrath as Judicial Force | 6 | 109 |
| M02-B | Burning Rage and Inner Heat | 10 | 263 |
| M02-C | Indignation and Moral Displeasure | 6 | 36 |
| M02-D | Provocation — Anger Aroused | 5 | 58 |
| M02-E | Jealousy, Zeal and Possessive Passion | 4 | 77 |
| M02-F | Strife, Quarrel and Contentious Anger | 6 | 16 |
| M02-BOUNDARY | Boundary — Pending Researcher Disposition | 6 | 82 |
| **Total** | | **43** | **641** |

Plus 9 multi-faceted terms placed at secondary level in additional sub-groups (per AI's design).

## Notable analytical decisions by AI

- **Burning Rage and Inner Heat (M02-B)** is the largest sub-group (263 verses, 10 primary terms) — captures the fire/heat metaphor family: cha.rah, cha.ron, cho.ri, che.ma, che.mah, zal.a.phah, plus Greek orgizō and others.
- **Divine Wrath as Judicial Force (M02-A)** holds orgē, qe.tseph, qe.tsaph, a.naph, qa.tsaph, re.gaz — terms that name wrath as settled judicial action / oaths / eschatological judgment.
- **Jealousy, Zeal and Possessive Passion (M02-E)** consolidates the qa.na / qin.ah / qan.na / qan.no family into one sub-group (AI judged unified rather than split divine-vs-human).
- **BOUNDARY (82 verses)** retained all 5 designated BOUNDARY terms plus tsur (mti=205) — Phase 3 STAYED tsur with the "no active relevant corpus" note, but it actually has 4 is_relevant rows; AI sensibly placed it in BOUNDARY rather than a characteristic-bearing sub-group given its ambiguous status.

## Health checks (post-apply)

| Code | Check | Expected | Actual | Status |
|---|---|---|---|---|
| H1 | Active M02 sub-groups | 7 | 7 | ✓ |
| H2 | is_relevant verses without `cluster_subgroup_id` | 0 | 0 | ✓ |
| H3 | Active `mti_term_subgroup` placements | 52 | 52 | ✓ |
| H4 | `cluster.status M02` | `Analysis - In Progress` (unchanged) | `Analysis - In Progress` | ✓ |

## State summary (M02, post-Phase-6)

| Item | Value |
|---|---|
| `cluster.status` | `Analysis - In Progress` (unchanged) |
| Active terms | 43 |
| Active sub-groups | **7** |
| Primary placements | 43 |
| Secondary placements | 9 |
| is_relevant verses routed | 641 |
| Inherited VCGs (still in DB; to be dissolved at Phase 8) | 73 |

## Provenance

- Phase 5 design (input): [WA-M02-subgroup-design-v1-20260516.md](WA-M02-subgroup-design-v1-20260516.md)
- Phase 5 mapping (input): [WA-M02-subgroup-mapping-v1-20260516.json](WA-M02-subgroup-mapping-v1-20260516.json)
- Phase 7 input report (output): [wa-cluster-M02-subgroup-meanings-v1-20260516.md](wa-cluster-M02-subgroup-meanings-v1-20260516.md)
- Apply script: [scripts/_apply_m02_phase6_subgroup_routing_20260516.py](../../../scripts/_apply_m02_phase6_subgroup_routing_20260516.py)
- Pre-apply backup: `backups/bible_research_backup_20260516_122945_DIR-20260516-009.db`

---

## Next step — Phase 7 (VCG design within sub-groups, AI)

AI designs new VCGs within each sub-group from the per-sub-group verse-and-meaning report. Per v2_2 §10 (Phase 7) — inherited VCGs remain suppressed; VCG design from meaning corpus only. CC produces the Phase 7 brief next.

*End of applied report.*
