# Flag Tables Extract — Query Reference

> Extracted 2026-04-15
> Companion documentation for: `data/exports/flag-tables-extract-20260414.json`
> Records the SQL join paths used to produce each section of the JSON extract.

---

## 1. storage_tables_summary

Simple row counts, no joins.

```sql
SELECT COUNT(*) FROM wa_term_phase2_flags;
SELECT COUNT(*) FROM mti_term_flags;
SELECT COUNT(*) FROM wa_data_quality_flags;
SELECT COUNT(*) FROM wa_session_research_flags;
SELECT COUNT(*) FROM wa_cross_registry_links;
```

---

## 2. reference_tables.phase2_flag_types

Reference rows with usage counts via correlated subqueries.

```sql
SELECT pft.id, pft.flag_code, pft.description,
    (SELECT COUNT(*) FROM wa_term_phase2_flags WHERE flag_id = pft.id) as used_in_phase2_flags,
    (SELECT COUNT(*) FROM mti_term_flags WHERE flag_id = pft.id) as used_in_mti_term_flags
FROM phase2_flag_types pft
ORDER BY pft.id;
```

**Join path:** `phase2_flag_types.id` &larr; `wa_term_phase2_flags.flag_id` and `mti_term_flags.flag_id`

---

## 3. reference_tables.wa_quality_flag_types

Reference rows with usage count.

```sql
SELECT qft.id, qft.flag_group, qft.flag_code, qft.description,
    (SELECT COUNT(*) FROM wa_data_quality_flags WHERE flag_id = qft.id) as used_in_data_quality_flags
FROM wa_quality_flag_types qft
ORDER BY qft.flag_group, qft.id;
```

**Join path:** `wa_quality_flag_types.id` &larr; `wa_data_quality_flags.flag_id`

---

## 4. reference_tables.wa_crosslink_type

Reference rows with usage count.

```sql
SELECT ct.id, ct.type_code, ct.description,
    (SELECT COUNT(*) FROM wa_cross_registry_links WHERE connection_type_id = ct.id) as used_in_links
FROM wa_crosslink_type ct
ORDER BY ct.id;
```

**Join path:** `wa_crosslink_type.id` &larr; `wa_cross_registry_links.connection_type_id`

---

## 5. in_use_analysis.wa_term_phase2_flags_by_code

Two-table join: one inner for flag code resolution, one LEFT to detect orphan and deleted-term flags.

```sql
SELECT ft.flag_code, COUNT(*) as count,
    COUNT(DISTINCT pf.term_inv_id) as distinct_terms,
    SUM(CASE WHEN ti.delete_flagged=0 THEN 1 ELSE 0 END) as on_active_terms,
    SUM(CASE WHEN ti.delete_flagged=1 THEN 1 ELSE 0 END) as on_deleted_terms
FROM wa_term_phase2_flags pf
JOIN phase2_flag_types ft ON ft.id = pf.flag_id
LEFT JOIN wa_term_inventory ti ON ti.id = pf.term_inv_id
GROUP BY ft.flag_code
ORDER BY count DESC;
```

**Join paths:**
- `wa_term_phase2_flags.flag_id` &rarr; `phase2_flag_types.id` (INNER — resolve flag code name)
- `wa_term_phase2_flags.term_inv_id` &rarr; `wa_term_inventory.id` (LEFT — preserves flags whose term_inv_id no longer exists, so they are visible as orphans)

---

## 6. in_use_analysis.mti_term_flags_by_code

Single inner join to resolve flag code.

```sql
SELECT ft.flag_code, COUNT(*) as count
FROM mti_term_flags mtf
JOIN phase2_flag_types ft ON ft.id = mtf.flag_id
GROUP BY ft.flag_code
ORDER BY count DESC;
```

**Join path:** `mti_term_flags.flag_id` &rarr; `phase2_flag_types.id`

---

## 7. in_use_analysis.wa_data_quality_flags_by_code

Single inner join to resolve flag code and group.

```sql
SELECT qft.flag_group, qft.flag_code, COUNT(*) as count
FROM wa_data_quality_flags dqf
JOIN wa_quality_flag_types qft ON qft.id = dqf.flag_id
GROUP BY qft.flag_code
ORDER BY count DESC;
```

**Join path:** `wa_data_quality_flags.flag_id` &rarr; `wa_quality_flag_types.id`

---

## 8. in_use_analysis.wa_session_research_flags_by_code

No join on main aggregation (`flag_code` is stored directly as a string on the row). Per-row lookup used to populate the reference_entry field.

**Main aggregation:**

```sql
SELECT flag_code, COUNT(*) as count,
    COUNT(DISTINCT registry_id) as distinct_registries,
    COUNT(DISTINCT cross_registry_id) as distinct_targets,
    SUM(CASE WHEN priority='HIGH' THEN 1 ELSE 0 END) as priority_high,
    SUM(CASE WHEN priority='MEDIUM' THEN 1 ELSE 0 END) as priority_medium,
    SUM(CASE WHEN priority='LOW' THEN 1 ELSE 0 END) as priority_low,
    SUM(CASE WHEN session_target='D' THEN 1 ELSE 0 END) as targets_session_d,
    SUM(CASE WHEN session_target='B' THEN 1 ELSE 0 END) as targets_session_b,
    SUM(CASE WHEN resolved=1 THEN 1 ELSE 0 END) as resolved_count,
    MIN(raised_date) as earliest_date,
    MAX(raised_date) as latest_date
FROM wa_session_research_flags
GROUP BY flag_code
ORDER BY count DESC;
```

**Per-row reference lookup (executed once per distinct flag_code):**

```sql
SELECT id, flag_group FROM wa_quality_flag_types WHERE flag_code = ?;
```

**Join path:** `wa_session_research_flags.flag_code` &harr; `wa_quality_flag_types.flag_code`

This is a string match, not an FK join. The design uses `flag_code` directly on the row rather than a foreign key `flag_id`. Because there is no FK constraint, research flags can be inserted with arbitrary codes that have no reference entry — which is why 15 of 16 in-use codes are unreferenced.

---

## 9. in_use_analysis.wa_cross_registry_links_by_type

Single inner join to resolve link type.

```sql
SELECT ct.type_code, COUNT(*) as count
FROM wa_cross_registry_links cl
JOIN wa_crosslink_type ct ON ct.id = cl.connection_type_id
GROUP BY ct.type_code
ORDER BY count DESC;
```

**Join path:** `wa_cross_registry_links.connection_type_id` &rarr; `wa_crosslink_type.id`

---

## 10. Summary of Join Paths

| Storage table | FK field | Reference table | Join type |
|---------------|----------|-----------------|-----------|
| wa_term_phase2_flags | flag_id | phase2_flag_types.id | integer FK |
| wa_term_phase2_flags | term_inv_id | wa_term_inventory.id | integer FK (LEFT, to find orphans) |
| mti_term_flags | flag_id | phase2_flag_types.id | integer FK |
| wa_data_quality_flags | flag_id | wa_quality_flag_types.id | integer FK |
| wa_session_research_flags | flag_code | wa_quality_flag_types.flag_code | **string match, no FK** |
| wa_cross_registry_links | connection_type_id | wa_crosslink_type.id | integer FK |

The `wa_session_research_flags` &rarr; `wa_quality_flag_types` relationship is the odd one out. It is a loose string match rather than an integer FK, which is why 15 of 16 in-use codes have no reference entry. This is a schema design choice with consequences for reference integrity.
