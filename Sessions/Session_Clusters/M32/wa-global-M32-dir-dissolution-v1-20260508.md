# wa-global-M32-dir-dissolution-v1-20260508

> Framework B Soul Word Analysis Programme — Cross-Cluster Directive
> Scope: Global (cross-cluster: M32 dissolution; terms redistributed to M15 and M26)
> Directive ID: DIR-20260508-005
> Version: v1 | Date: 2026-05-08
> Pattern: §11.6 Worked pattern C (cluster reassignment) — extended for full cluster dissolution
> Filename pattern: §2.2 global (cross-cluster scope per §11.7)
> Governing instruction: wa-directive-instruction-v1_4-20260506
> Obslog: wa-obslog-M32-conscience-self-awareness-v2-20260508

---

## Element 1 — MOTIVATION

The M32 (Conscience and Self-Awareness) cluster was subjected to a full Session B analytical pass (Phase 8 redo, 2026-05-08). Phase 10 review of the post-directive comprehensive report (wa-cluster-M32-comprehensive-v4-20260508.md) revealed that M32 is a conglomerate of terms evidencing different characteristics that properly belong in other clusters.

**Analytical grounds for dissolution (from verse evidence only):**

M32-A (Conscience): suneidō (G4894) in its three extracted verses (Act 5:2, 12:12, 14:6) evidences general cognitive awareness — realising, learning, shared knowing — not moral self-assessment. sunoida (G6083) in its one extracted verse (1Cor 4:4) evidences moral self-assessment within an explicitly judicial frame (acquittal, divine judgment). These two terms evidence different characteristics and belong in different clusters.

M32-B (Inner Attention): shit (H7896K) in its seven extracted verses consistently evidences the deliberate act of inner attending — setting the mind on something, taking to heart, considering — which is a cognitive-attentive characteristic belonging with wisdom/understanding/knowledge vocabulary.

M32-BOUNDARY: enthumeomai (G1760) evidences sustained inner reflection/pondering (cognitive). kardiognōstēs (G2589) evidences God's complete knowing of human hearts — an epistemological frame paired with sunoida's judicial context (1Cor 4:4). autokatakritos (G0843) evidences self-condemnation as a judicial verdict term.

**Redistribution decision:**

Three terms evidence cognitive awareness, attending, and inner reflection → **M15 (Wisdom, Understanding and Knowledge)**

Three terms evidence judicial moral self-assessment, divine heart-knowing as forensic ground, and self-condemnation → **M26 (Righteousness and Justice)**

**Preservation decision (researcher-confirmed):** M32 cluster_finding rows are retained in the database, flagged as legacy/superseded. They are NOT deleted. They remain available as reference context when M15 and M26 terms are later analysed in their new clusters' Session B passes.

**Source documents:**
- wa-obslog-M32-conscience-self-awareness-v2-20260508.md
- wa-cluster-M32-comprehensive-v4-20260508.md
- WA-M32-consolidated-findings-v1-20260508-parts 1–4

---

## Element 2 — SCOPE

**Tables touched:** `mti_terms`, `cluster_subgroup`, `cluster_finding`, `cluster`

**Clusters affected:** M32 (source, dissolving), M15 (destination), M26 (destination)

### 2.1 Term reassignments — `mti_terms`

Six terms require `cluster_code` update and `cluster_subgroup_id` cleared (sub-groups are M32-specific; destination clusters have not yet assigned sub-groups for these terms):

| Strong's | mti_id | Current cluster_code | New cluster_code | Analytical grounds |
|---|---|---|---|---|
| G4894 suneidō | 454 | M32 | M15 | 3 verses = cognitive awareness / realising |
| H7896K shit | 3578 | M32 | M15 | 7 verses = deliberate inner attending producing knowledge |
| G1760 enthumeomai | 3392 | M32 | M15 | 3 verses = sustained inner deliberation / pondering |
| G6083 sunoida | 2739 | M32 | M26 | 1Cor 4:4 = moral self-assessment in judicial frame |
| G2589 kardiognōstēs | 599 | M32 | M26 | Divine heart-knowing; epistemological frame above conscience |
| G0843 autokatakritos | 4848 | M32 | M26 | Self-condemnation; judicial verdict term |

**Operation per term:**
```sql
UPDATE mti_terms
SET cluster_code = '{new_cluster}',
    cluster_subgroup_id = NULL
WHERE id = {mti_id};
```

### 2.2 M32 sub-group rows — `cluster_subgroup`

Three sub-group rows exist for M32 (M32-A, M32-B, M32-BOUNDARY). These rows are to be marked inactive/dissolved — they must NOT be deleted (they are referenced by existing cluster_finding rows that are being preserved).

**Operation:**
```sql
UPDATE cluster_subgroup
SET status = 'dissolved',
    notes = 'M32 dissolved 2026-05-08 — terms redistributed to M15 and M26 per DIR-20260508-005. Sub-group retained for cluster_finding row integrity.'
WHERE cluster_code = 'M32';
```

**Note:** If `cluster_subgroup` does not have a `status` column, CC is to add a `dissolution_note` text field instead and record the note there. If neither approach is schema-supported, CC is to flag the constraint and propose the minimal schema-safe alternative. Do not delete the rows.

### 2.3 M32 cluster_finding rows — `cluster_finding`

All cluster_finding rows with `cluster_code = 'M32'` are to be preserved. They are to be flagged as legacy/superseded by updating a notes or status field.

**Operation:**
```sql
UPDATE cluster_finding
SET finding_status = 'superseded',
    notes = 'M32 dissolved 2026-05-08 — cluster_finding rows retained as legacy reference per DIR-20260508-005. Terms redistributed to M15 (suneidō, shit, enthumeomai) and M26 (sunoida, kardiognōstēs, autokatakritos).'
WHERE cluster_code = 'M32';
```

**Note:** If `finding_status = 'superseded'` is not a valid vocabulary value in the schema, CC is to use the closest available status that preserves the row without treating it as an active finding (e.g. a notes field update only, leaving finding_status unchanged). CC must not delete any cluster_finding rows. CC must flag which approach was used in the completion confirmation.

### 2.4 M32 cluster record — `cluster` table

The M32 cluster record is to be updated to reflect dissolution.

**Operation:**
```sql
UPDATE cluster
SET status = 'Dissolved',
    notes = 'Dissolved 2026-05-08 per DIR-20260508-005. Terms redistributed to M15 (G4894, H7896K, G1760) and M26 (G6083, G2589, G0843). cluster_finding rows retained as legacy reference. Analytical grounds: M32 was a conglomerate evidencing distinct characteristics belonging to separate clusters.'
WHERE cluster_code = 'M32';
```

**Note:** If 'Dissolved' is not a valid `status` vocabulary value, CC is to use the closest available value that takes the cluster out of the active analytical pipeline (e.g. 'Retired', 'Superseded') and record the dissolution detail in the notes field. CC must report which status value was applied.

### 2.5 verse_context_group rows — no change

The `verse_context_group` rows (group IDs 364, 1290, 1643, 2728, 350, 3605, 3606) are owned by the individual terms (by mti_term_id), not by the M32 cluster. When those terms move to M15 and M26, their group rows travel with them — no verse_context_group updates are required. The terms' verse analyses remain intact.

**Explicit instruction:** Do NOT modify any `verse_context` or `verse_context_group` rows. These are term-owned and remain valid in the destination clusters.

---

## Element 3 — OUTCOME REQUIRED

After all operations complete:

**3.1 mti_terms:**
- 6 terms have updated `cluster_code`: 3 = 'M15', 3 = 'M26'
- All 6 terms have `cluster_subgroup_id = NULL`
- M32 has 0 terms remaining: `SELECT COUNT(*) FROM mti_terms WHERE cluster_code = 'M32'` = 0

**3.2 cluster_subgroup:**
- M32-A, M32-B, M32-BOUNDARY rows are flagged as dissolved/inactive
- Rows are present (not deleted)
- M15 and M26 sub-group tables are NOT modified by this directive (destination sub-group assignment is a separate future operation when those clusters reach their own Session B)

**3.3 cluster_finding:**
- All M32 cluster_finding rows are present (not deleted)
- All M32 cluster_finding rows carry the superseded/legacy flag or note
- Row count by status confirms rows are present

**3.4 cluster:**
- M32 cluster record carries dissolution status and notes
- M15 and M26 cluster records are NOT modified by this directive (they gain terms but their cluster-level metadata update is not required here)

**3.5 verse_context / verse_context_group:**
- No rows modified — confirm with a count check

---

## Element 4 — COMPLETION CONFIRMATION

CC is required to produce confirmation covering all of the following:

**4.1 Term redistribution confirmed:**
```sql
SELECT cluster_code, strongs_number, cluster_subgroup_id
FROM mti_terms
WHERE id IN (454, 3578, 3392, 2739, 599, 4848)
ORDER BY cluster_code, strongs_number;
```
Expected: 3 rows with cluster_code='M15' (G4894, H7896K, G1760), 3 rows with cluster_code='M26' (G6083, G2589, G0843), all with cluster_subgroup_id = NULL.

**4.2 M32 emptied:**
```sql
SELECT COUNT(*) FROM mti_terms WHERE cluster_code = 'M32';
```
Expected: 0

**4.3 M32 cluster_finding rows preserved:**
```sql
SELECT finding_status, COUNT(*)
FROM cluster_finding
WHERE cluster_code = 'M32'
GROUP BY finding_status;
```
Expected: rows present, none deleted. Status values reflect superseded/legacy flag or unchanged if schema did not support status update.

**4.4 M32 cluster record status:**
```sql
SELECT cluster_code, status, notes
FROM cluster
WHERE cluster_code = 'M32';
```
Expected: dissolution status and notes recorded.

**4.5 M32 sub-group rows present:**
```sql
SELECT subgroup_code, status
FROM cluster_subgroup
WHERE cluster_code = 'M32';
```
Expected: M32-A, M32-B, M32-BOUNDARY present, not deleted, with dissolution flag or note.

**4.6 verse_context unchanged:**
```sql
SELECT COUNT(*) FROM verse_context
WHERE mti_term_id IN (454, 3578, 3392, 2739, 599, 4848);
```
Confirm count matches pre-directive count (no verse_context rows modified).

**4.7 Application report:**
Save to: `Sessions/Session_Clusters/M32/WA-M32-dissolution-applied-v1-20260508.md`

Report must include: directive ID, date applied, term redistribution table (6 terms × old/new cluster_code), M32 cluster_finding row count retained, cluster status applied, any schema constraints encountered and how resolved.

---

## Element 5 — NOTES

**Pre-flight checks CC must run before any write:**

1. Confirm all 6 mti_ids (454, 3578, 3392, 2739, 599, 4848) exist in `mti_terms` with `cluster_code = 'M32'`.
2. Confirm M15 and M26 exist as valid cluster records in the `cluster` table.
3. Confirm `cluster_subgroup` rows for M32-A, M32-B, M32-BOUNDARY exist and are linked to the correct mti_term_ids.
4. Confirm `cluster_finding` rows with `cluster_code = 'M32'` exist and are countable before write.
5. Confirm `verse_context_group` rows for groups 364, 1290, 1643, 2728, 350, 3605, 3606 are owned by the correct mti_term_ids (not cluster-owned) — confirming they travel with terms without modification.

**Halt-on-error:** Any pre-flight failure stops all writes. CC reports the failure and waits.

**Schema constraint handling:** Three operations (cluster_subgroup dissolution flag, cluster_finding superseded status, cluster dissolution status) may encounter vocabulary constraints. In each case CC must:
- Attempt the preferred operation as written
- If schema-blocked, apply the closest schema-safe alternative
- Report exactly what was applied in the completion confirmation

**No analytical writes to M15 or M26:** This directive moves terms only. It does NOT create sub-groups, group-verse mappings, or cluster_finding rows in M15 or M26. Those are produced when M15 and M26 reach their own Session B analytical passes. The terms arrive in destination clusters with their `verse_context_group` rows intact and `cluster_subgroup_id = NULL`.

**M32 cluster_finding rows as future reference:** When M15 and M26 later reach Session B, the analysts should be aware that M32 legacy findings exist and are queryable via `SELECT * FROM cluster_finding WHERE cluster_code = 'M32'`. These findings are reference context, not binding analytical conclusions for the destination clusters.

**Directive ID:** DIR-20260508-005
**Cross-cluster scope:** M32 (dissolving) → M15, M26 (receiving)
**Cluster status post-directive:** M32 = Dissolved; M15 and M26 unchanged at cluster level

---

*wa-global-M32-dir-dissolution-v1-20260508*
*Cross-cluster dissolution directive per wa-directive-instruction-v1_4-20260506 §11.6 + §2.2*
*Obslog: wa-obslog-M32-conscience-self-awareness-v2-20260508*
