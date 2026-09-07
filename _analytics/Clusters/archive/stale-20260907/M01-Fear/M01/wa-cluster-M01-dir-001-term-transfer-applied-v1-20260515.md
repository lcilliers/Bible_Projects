# WA-M01-dir-001-term-transfer-applied-v1-20260515

**Directive:** [DIR-20260515-001 — wa-global-dir-001-m01-term-transfer-v1-20260515.md](wa-global-dir-001-m01-term-transfer-v1-20260515.md)
**Apply date:** 2026-05-15
**Apply timestamp:** 2026-05-15T10:24:18Z (committed)

---

## Outcome

**12 terms transferred. M01 reduced 94 → 82. M24 increased 67 → 77 (+10). M03 increased 86 → 88 (+2). 3 BOUNDARY terms remain in M01 unchanged. No verse_context or VCG row updates were required (no `cluster_code` denormalisation in those tables).**

---

## Pre-execution verification (Q1)

All 15 transfer-set Strong's resolved to single active `mti_terms` rows, all `cluster_code='M01'`, all with zero `mti_term_subgroup` rows.

| Strong's | mti_id | Directive's expected mti_id | Match | Initial cluster | Initial subgroup links |
|---|---:|---:|---|---|---:|
| G2347 | 21 | 21 | ✓ | M01 | 0 |
| G4730 | 51 | 51 | ✓ | M01 | 0 |
| H4867 | 4814 | 4814 | ✓ | M01 | 0 |
| H5076 | 5572 | 5572 | ✓ | M01 | 0 |
| H1742 | 6385 | 6385 | ✓ | M01 | 0 |
| H8513 | 2494 | 2494 | ✓ | M01 | 0 |
| H7661 | 240 | 240 | ✓ | M01 | 0 |
| H6125 | 5157 | 5157 | ✓ | M01 | 0 |
| H4164 | 156 | 156 | ✓ | M01 | 0 |
| H6115 | 6210 | 6210 | ✓ | M01 | 0 |
| H6330 | 198 | 198 | ✓ | M01 | 0 |
| H2750 | 1552 | 1552 | ✓ | M01 | 0 |
| G1280 | 4481 | 4481 | ✓ | M01 | 0 |
| G0639 | 4482 | 4482 | ✓ | M01 | 0 |
| H7672 | 4483 | 4483 | ✓ | M01 | 0 |

**Note on `mti_terms.cluster_subgroup_id`:** directive Q1 expected this field on `mti_terms`, but the table has no such column. The cluster-to-subgroup mapping is held in the m:n table `mti_term_subgroup`. CC verified the equivalent condition — zero active `mti_term_subgroup` rows for each transferred mti_term_id — as the correct schema-mapped check.

---

## Schema checks (directive Q7, Q8)

| Table | `cluster_code` column? | Action |
|---|---|---|
| `verse_context` | **NO** | no row updates required; cluster ownership resolves through `mti_terms.cluster_code` via the `mti_term_id` FK |
| `verse_context_group` | **NO** | no row updates required; VCG ownership resolves through `mti_terms.cluster_code` via the m:n `vcg_term` table |

The 12 transferred terms automatically carry their associated verse_context rows (76 total) and verse_context_group rows (15 total) to the new cluster via FK resolution — no row-level cluster_code update needed.

**Carry-along counts:**

| Destination | vc rows that moved | VCG rows that moved |
|---|---:|---:|
| M24 | 69 | 13 |
| M03 | 7 | 2 |
| **Total** | **76** | **15** |

---

## Post-execution verification

### Q2 — M01 term count (expected 82)

```sql
SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M01' AND status IN ('extracted','extracted_thin');
```

Result: **82** ✓

### Q3 — M24 term count (expected prior + 10)

- Prior M24 count: 67
- Post-transfer M24 count: **77** ✓

### Q4 — M03 term count (expected prior + 2)

- Prior M03 count: 86
- Post-transfer M03 count: **88** ✓

### Q5 — Confirm 12 transferred terms (active rows only)

| Strong's | New cluster |
|---|---|
| G2347 | **M24** ✓ |
| G4730 | **M24** ✓ |
| H1742 | **M24** ✓ |
| H4164 | **M24** ✓ |
| H4867 | **M24** ✓ |
| H5076 | **M24** ✓ |
| H6115 | **M24** ✓ |
| H6125 | **M24** ✓ |
| H7661 | **M24** ✓ |
| H8513 | **M24** ✓ |
| H2750 | **M03** ✓ |
| H6330 | **M03** ✓ |

### Q6 — Confirm 3 BOUNDARY terms unchanged

| Strong's | Cluster |
|---|---|
| G0639 *aporeō* | **M01** ✓ |
| G1280 *diaporeō* | **M01** ✓ |
| H7672 *she.vash* | **M01** ✓ |

All three remain `cluster_code='M01'` with zero `mti_term_subgroup` rows, ready for BOUNDARY sub-group assignment in DIR-20260515-002 (Phase 4).

---

## Notes on duplicate `mti_terms` rows for 5 transferred Strong's

For 5 of the 12 transferred Strong's (G2347, G4730, H2750, H4164, H7661), the database contains additional `mti_terms` rows that are **soft-deleted (`delete_flagged=1`, `status=NULL`)** and not in the active 94-term pool:

| Strong's | Active mti_id (transferred) | Inactive duplicate mti_ids (untouched, delete_flagged=1) |
|---|---:|---|
| G2347 | 21 → M24 | 5175 |
| G4730 | 51 → M24 | 4641 |
| H2750 | 1552 → M03 | 5185, 6790 |
| H4164 | 156 → M24 | 4718, 5115 |
| H7661 | 240 → M24 | 7444 |

These 7 inactive rows still carry `cluster_code='M01'` from earlier programme state. They are excluded from all active-status counts and from the directive's term-set queries (which filter `status IN ('extracted','extracted_thin')`). No analytical or schema-integrity issue — this is the known OT-DBR-009 `mti_terms` dedup residue. **No action taken on these rows per directive §5 ("No other tables touched") and the explicit `status` filter in directive Q2/Q3/Q4 queries.** They will be cleaned up if/when OT-DBR-009 is addressed.

---

## Tables not touched (directive §5 — Do not modify)

| Table | Modified? |
|---|---|
| `cluster_subgroup` | NO |
| `cluster_finding` | NO |
| `wa_session_b_findings` | NO |
| `verse_context.is_relevant` / `is_anchor` / `set_aside_reason` etc. | NO |
| `verse_context_group.context_description` / `notes` | NO |
| `vcg_term` | NO |
| `mti_term_subgroup` | NO |

---

## Cluster state after transfer

| Cluster | Active terms |
|---|---:|
| M01 Fear | **82** (was 94) — includes 3 BOUNDARY terms (aporeō, diaporeō, she.vash) |
| M03 Grief | **88** (was 86) |
| M24 Weakness | **77** (was 67) |

---

## Next directive

**DIR-20260515-002** — Phase 4 sub-group assignment for M01 (will create the M01-A/B/.../BOUNDARY sub-groups and bind the 82 remaining terms; the 3 BOUNDARY terms get their `mti_term_subgroup` row at that stage).

---

## Provenance

- Directive: [Sessions/Session_Clusters/M01/wa-global-dir-001-m01-term-transfer-v1-20260515.md](wa-global-dir-001-m01-term-transfer-v1-20260515.md)
- Source comprehensive report: `wa-cluster-M01-comprehensive-v3-20260515.md`
- Phase 3 obslog (analytical basis): `wa-obslog-M01-cluster-m01-v1-20260515.md`
- Governing instruction: `wa-sessionb-cluster-instruction-v1_13-20260514` §4–§7
