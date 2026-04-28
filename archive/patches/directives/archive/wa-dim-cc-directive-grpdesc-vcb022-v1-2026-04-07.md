# wa-dim-cc-directive-grpdesc-vcb022-v1-2026-04-07
**Type:** Claude Code Directive — Group Description ID Resolution
**Date:** 2026-04-07
**Produced by:** WA-DimensionReview-Instruction-v1.3-2026-04-07
**Reference:** wa-dim-grpdesc-patch-vcb022-r192-v1-2026-04-07.json (already applied — Registry 192 done)

---

## Purpose

VCB-022 patch (PATCH-20260404-VCB022-VERSECONTEXT-V1) truncated 155 of 159
`verse_context_group.context_description` values at exactly 80 characters.

Registry 192 (7 groups) has already been corrected via a separate patch applied
to the C03 cluster session. The remaining **148 groups** across Registries
187–191, 193, 194, and 196 require correction via a single
`DIMREVIEW-GRPDESC` patch.

Claude AI has already produced the full corrected descriptions (sourced from
`wa-vcb-022-term-observations-v2.8-20260404.md`). What is needed from Claude
Code is the database IDs (`verse_context_group.id` and `wa_dimension_index.id`)
for each of the 148 group_codes, so Claude AI can assemble the final patch.

---

## Task

Run the following query and return the results as JSON:

```sql
SELECT
    vcg.id            AS vcg_id,
    vcg.group_code    AS group_code,
    wdi.id            AS dim_id
FROM verse_context_group vcg
JOIN wa_dimension_index wdi ON wdi.verse_context_group_id = vcg.id
WHERE vcg.group_code IN (
    '643-001', '643-002', '643-003', '643-004',
    '670-001', '669-001', '669-002', '668-001', '668-002',
    '7035-001', '7032-001', '7032-002',
    '7029-001', '7029-002',
    '7030-001', '7030-002', '7030-003', '7030-004',
    '7031-001', '7031-002', '7034-001', '7108-001', '7109-001',
    '681-001', '7107-001', '6973-001',
    '6948-001', '6948-002', '6996-001',
    '6965-001', '6965-002', '6965-003', '6965-004', '6965-005',
    '638-001',
    '654-001', '654-002', '654-003', '654-004', '654-005', '654-006',
    '6908-001', '6900-001', '6900-002', '6900-003', '6907-001',
    '646-001', '6888-001', '7052-001',
    '659-001', '659-002',
    '6989-001', '6989-002', '6989-003', '6989-004',
    '6896-001', '6895-001', '6895-002', '6895-003',
    '648-001', '674-001',
    '675-001', '675-002', '675-003', '675-004', '675-005',
    '644-001',
    '7092-001', '7092-002', '7092-003',
    '642-001', '7096-001', '7093-001',
    '7112-001', '7112-002', '7112-003', '7113-001',
    '653-001',
    '6889-001', '6889-002', '6889-003', '6889-004',
    '6890-001', '6891-001',
    '673-001', '672-001', '6992-001',
    '7000-001', '7001-001', '7002-001',
    '655-001', '660-001', '7003-001',
    '6943-001', '6944-001',
    '1271-001',
    '1270-001', '1270-002', '1270-003', '1270-004',
    '1269-001', '1273-001', '7117-001', '1272-001',
    '1275-001',
    '1284-001', '1279-001', '1280-001', '1281-001', '1283-001',
    '7156-001', '7158-001', '1282-001',
    '1276-001', '1276-002', '1276-003', '1277-001', '7151-001',
    '7161-001',
    '1285-001', '1285-002', '7160-001', '1288-001',
    '7186-001', '7183-001', '7184-001', '7185-001',
    '7182-001', '7181-001', '1289-001', '1287-001',
    '1286-001', '7162-001', '7164-001', '7163-001',
    '1295-001', '7222-001', '1296-001',
    '1298-001', '1298-002', '1298-003',
    '1300-001', '1301-001',
    '1299-001', '1299-002', '1299-003', '1299-004',
    '1316-001'
)
ORDER BY vcg.group_code;
```

Expected result: **148 rows** — one per group_code.

---

## Validation

Before returning results, verify:
1. Row count = 148 (no missing group_codes)
2. No group_code appears more than once
3. Every `dim_id` is non-null (all groups have a `wa_dimension_index` entry)

If any group_code returns zero rows, report it explicitly — do not silently omit.

---

## Return format

```json
[
  { "group_code": "643-001", "vcg_id": 9999, "dim_id": 9999 },
  ...
]
```

Return as a JSON file named:
`wa-dim-grpdesc-idresolution-vcb022-v1-2026-04-07.json`

---

## What happens next

Claude AI will receive this file and use it to assemble
`wa-dim-grpdesc-patch-vcb022-remaining-v1-2026-04-07.json` — a single
`DIMREVIEW-GRPDESC` patch covering all 148 groups. Claude Code then applies
that patch in the normal way.

---

*wa-dim-cc-directive-grpdesc-vcb022-v1-2026-04-07 | 2026-04-07*
*Companion to: wa-dim-grpdesc-patch-vcb022-r192-v1-2026-04-07.json (applied)*
