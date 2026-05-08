# wa-cluster-M32-dir-002-subgroup-assign-v1-20260508

**DIRECTIVE ID:** DIR-20260508-001
**Cluster:** M32 — Conscience and Self-Awareness
**Phase:** 4 (Sub-group assignment)
**Date:** 2026-05-08
**Author:** Claude AI (analytical)
**Operator:** CC (database execution)
**Governing instruction:** wa-directive-instruction-v1_4-20260506 §11.4

---

## ELEMENT 1 — MOTIVATION

Source documents:
- `WA-M32-characteristic-debate-v1-20260508.md` — Phase 3 provisional sub-group debate
- `wa-obslog-M32-conscience-self-awareness-v1-20260508.md` Phase 4 — control read entries P4.1–P4.3

The Phase 3 gloss-level debate proposed four sub-groups (A, B, C, BOUNDARY). The Phase 4 control read of all 17 verses against the T1 characteristic definition resolved three open questions (OQ-001, OQ-002, OQ-003) with researcher confirmation, producing the following changes:

- Sub-group C (autokatakritos) dissolved — single verse insufficient for full catalogue pass; moved to BOUNDARY
- enthumeomai moved from Sub-group B to BOUNDARY — verses show cognitive deliberation, not conscience/self-awareness characteristic; insufficient analytical viability for sub-group pass
- Sub-group B now contains H7896K shit only (7 verses)
- kardiognōstēs confirmed in BOUNDARY — both verses have God as subject; no human inner-being characteristic

This directive creates the confirmed sub-group structure and assigns all six terms.

Cluster status transition: `Data - In Progress` → `Analysis - In Progress`.

---

## ELEMENT 2 — SCOPE

### 2.1 cluster_subgroup rows to CREATE (3 rows)

| subgroup_code | cluster_code | label | description |
|---|---|---|---|
| M32-A | M32 | Conscience | The faculty by which the person assesses their own moral state — inner knowing of one's own moral standing, complicity, or condition; operating under the awareness that God's judgment is the higher court |
| M32-B | M32 | Self-Awareness / Inner Attention | The directed inner act of setting attention — deliberate cognitive engagement and attending carefully to a matter, person, or situation; the attentiveness capacity that underlies conscience |
| M32-BOUNDARY | M32 | BOUNDARY | Supporting terms that contextualise the conscience and self-awareness characteristics without themselves being T1 characteristic-bearing: the reflective capacity (enthumeomai), the terminal conscience-state (autokatakritos), and the divine epistemological frame (kardiognōstēs) |

### 2.2 mti_terms.cluster_subgroup_id assignments

| Strong's | mti_id | Transliteration | Subgroup assigned |
|---|---|---|---|
| G4894 | 454 | suneidō | M32-A |
| G6083 | 2739 | sunoida | M32-A |
| H7896K | 3578 | shit | M32-B |
| G1760 | 3392 | enthumeomai | M32-BOUNDARY |
| G0843 | 4848 | autokatakritos | M32-BOUNDARY |
| G2589 | 599 | kardiognōstēs | M32-BOUNDARY |

All 6 terms assigned. No term is unassigned after this directive executes.

### 2.3 Cluster status update

`UPDATE cluster SET status = 'Analysis - In Progress', last_updated_date = CURRENT_TIMESTAMP WHERE cluster_code = 'M32'`

### 2.4 Scope limits

- Tables touched: `cluster_subgroup` (INSERT 3 rows), `mti_terms` (UPDATE 6 rows, `cluster_subgroup_id` field only), `cluster` (UPDATE 1 row, `status` + `last_updated_date`)
- No `verse_context` or `verse_context_group` writes in this directive — that is Phase 7
- Set-aside reasons: not applicable (0 set-aside verses in M32)
- No cluster reassignment: all terms confirmed within M32

---

## ELEMENT 3 — OUTCOME REQUIRED

Post-execution state:

| subgroup_code | term_count |
|---|---|
| M32-A | 2 |
| M32-B | 1 |
| M32-BOUNDARY | 3 |
| **Total** | **6** |

- `cluster.status` for M32 = `Analysis - In Progress`
- `mti_terms` rows for mti_id IN (454, 2739, 3578, 3392, 4848, 599): each has a non-null `cluster_subgroup_id` pointing to the correct subgroup row
- No other `mti_terms` fields modified
- `wa_session_research_flags` / `wa_session_b_findings` row counts: unchanged

---

## ELEMENT 4 — COMPLETION CONFIRMATION

CC runs the following queries and returns results:

**Query 1 — Sub-group counts:**
```sql
SELECT cs.subgroup_code, COUNT(mt.id) AS term_count
FROM cluster_subgroup cs
LEFT JOIN mti_terms mt ON mt.cluster_subgroup_id = cs.id
WHERE cs.cluster_code = 'M32'
GROUP BY cs.subgroup_code
ORDER BY cs.subgroup_code;
```
Expected: M32-A=2, M32-B=1, M32-BOUNDARY=3

**Query 2 — All terms assigned (no nulls):**
```sql
SELECT mt.id, mt.strongs_number, cs.subgroup_code
FROM mti_terms mt
JOIN cluster_subgroup cs ON cs.id = mt.cluster_subgroup_id
WHERE mt.cluster_code = 'M32'
ORDER BY cs.subgroup_code, mt.strongs_number;
```
Expected: 6 rows, all with non-null subgroup_code

**Query 3 — Cluster status:**
```sql
SELECT cluster_code, status, last_updated_date
FROM cluster
WHERE cluster_code = 'M32';
```
Expected: status = 'Analysis - In Progress'

**Query 4 — Legacy findings unchanged:**
```sql
SELECT COUNT(*) FROM wa_session_b_findings
WHERE mti_term_id IN (454, 2739, 3578, 3392, 4848, 599);
```
Expected: same count as pre-directive (record as baseline before executing)

---

## ELEMENT 5 — NOTES

- Companion document: `WA-M32-characteristic-debate-v1-20260508.md`
- Obslog reference: `wa-obslog-M32-conscience-self-awareness-v1-20260508.md` Phase 4
- Pre-flight: verify mti_id values (454, 2739, 3578, 3392, 4848, 599) all exist in `mti_terms` with `cluster_code = 'M32'` before any write
- Halt-on-error: if pre-flight fails, report and wait
- After confirmation, AI will proceed to Phase 5 (grouped report required from CC before Phase 5 begins)

---

*wa-cluster-M32-dir-002-subgroup-assign-v1-20260508*
*DIR-20260508-001*
*Companion: WA-M32-characteristic-debate-v1-20260508.md*
