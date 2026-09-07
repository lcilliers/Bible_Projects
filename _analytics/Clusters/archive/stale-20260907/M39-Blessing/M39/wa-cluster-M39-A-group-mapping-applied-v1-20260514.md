# WA-M39-A-group-mapping-applied-v1-20260514

**Directive:** DIR-20260514-002
**Segment:** M39-A
**Source directive:** [Sessions/Session_Clusters/M39/wa-cluster-M39-dir-002-A-mapping-v1-20260514.md](Sessions\Session_Clusters\M39\wa-cluster-M39-dir-002-A-mapping-v1-20260514.md)
**Applied:** 2026-05-14T05:12:28Z
**Mode:** live

## Operations applied

- Op 1 — `verse_context_group` `context_description` UPDATE: **9** rows
- Op 2 — `verse_context` `group_id` UPDATE: **16** rows
- No NEW VCGs → no `vcg_term` INSERTs

## Post-state

- Remaining P-status verses in M39-A (is_relevant=1, group_id IS NULL): **0** (expected 0)

## Schema deviations from directive text

Intent applied per actual schema. Surface for AI's future reference:

| Directive said | Actual column |
|---|---|
| `verse_context_group.subgroup_code` | `group_code` |
| `verse_context_group.core_description` | `context_description` |
