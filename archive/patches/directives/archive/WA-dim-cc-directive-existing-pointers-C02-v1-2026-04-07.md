# WA — CC Directive: Existing Pointers Extract for C02
**File:** WA-dim-cc-directive-existing-pointers-C02-v1-2026-04-07.md
**Date:** 2026-04-07
**Produced by:** Claude AI — WA-DimensionReview-Instruction-v1.3-2026-04-07
**Instruction reference:** Section 9.3
**Previous output:** wa-dim-existing-pointers-C02-2026-04-06.json (produced 2026-04-06 — scope covered session_d_pointers only; session_b_findings array was empty)

---

## Purpose

The existing pointers extract delivered at session start (wa-dim-existing-pointers-C02-2026-04-06.json) contains `session_d_pointers` but has an empty `session_b_findings` array. Before the C02 patch can be constructed, Claude AI requires the complete set of existing `wa_session_b_findings` records for all registries in cluster C02 to verify uniqueness of all new Session B finding IDs.

Per WA-DimensionReview-Instruction-v1.3 Section 9.3, the existing pointers extract must include both arrays. This directive requests a replacement extract covering both tables.

---

## Action Required

Claude Code is to query the database and produce a replacement existing pointers extract for cluster C02.

**Output file name:** `wa-dim-existing-pointers-C02-{date}.json`

---

## Registry filter

The following registries are members of cluster C02:

| Registry no | Word |
|---|---|
| 32 | counsel |
| 49 | discernment |
| 85 | imagination |
| 91 | insight |
| 93 | intention |
| 100 | knowledge |
| 108 | meditation |
| 110 | memory |
| 126 | purpose |
| 127 | reasoning |
| 160 | thought |
| 166 | understanding |
| 174 | wisdom |

---

## Query specification

**Session B findings:**

```sql
SELECT
  finding_id,
  registry_id,
  finding_type,
  finding,
  raised_date,
  session_b_instruction
FROM wa_session_b_findings
WHERE registry_id IN (32, 49, 85, 91, 93, 100, 108, 110, 126, 127, 160, 166, 174)
ORDER BY registry_id, finding_id;
```

**Session D pointers:**

```sql
SELECT
  flag_label,
  registry_id,
  flag_code,
  description,
  session_target,
  raised_date
FROM wa_session_research_flags
WHERE registry_id IN (32, 49, 85, 91, 93, 100, 108, 110, 126, 127, 160, 166, 174)
  AND session_target = 'D'
ORDER BY registry_id, flag_label;
```

---

## Output format

```json
{
  "extract_meta": {
    "extract_type": "existing_pointers",
    "cluster": "C02",
    "produced_date": "YYYY-MM-DD",
    "produced_by": "Claude Code — WA-DimensionReview-Instruction-v1.3-2026-04-07",
    "note": "Replacement extract — includes both session_b_findings and session_d_pointers per v1.3 Section 9.3"
  },
  "session_b_findings": [
    {
      "finding_id": "",
      "registry_id": 0,
      "finding_type": "",
      "finding": "",
      "raised_date": "",
      "session_b_instruction": ""
    }
  ],
  "session_d_pointers": [
    {
      "flag_label": "",
      "registry_id": 0,
      "flag_code": "",
      "description": "",
      "session_target": "D",
      "raised_date": ""
    }
  ]
}
```

---

## Delivery

Return the completed JSON file to Claude AI before patch construction proceeds. Claude AI will not construct Session B or Session D pointer inserts until this extract is received and the uniqueness check is complete.

No other action is required from Claude Code at this time.
