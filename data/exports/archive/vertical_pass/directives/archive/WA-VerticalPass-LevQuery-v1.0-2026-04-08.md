# WA-VerticalPass-LevQuery-v1.0-2026-04-08

**Framework B — Soul Word Analysis Programme**
**Vertical Pass Experiment — Lev Coverage and vr_del Pattern Query**
**Version 1.0 | 2026-04-08 | Status: Active**

| **Document** | **Value** |
|---|---|
| Filename | WA-VerticalPass-LevQuery-v1.0-2026-04-08.md |
| Supersedes | — |
| For | Claude Code |
| Purpose | Two targeted queries arising from vertical pass heart investigation |
| Depends on | wa-verticalpass-heartquery-20260408.json |
| Database | bible_research.db (schema v3.8.0 + VCB-031 additions) |

---

## Background

The heart query (WA-VerticalPass-HeartQuery-v1.0) established:

1. H3820A lev has `status=delete` — deliberate split decision; H3824 le.vav is the active Hebrew heart term in Registry 183
2. No active verse record links H3824 le.vav to Jer 7:24, despite "stubbornness of their evil **hearts**" (*libbam* — construct of levav) being present in the verse text
3. 17 of 21 verse records for Jer 7:24 have `delete_flagged=1`, covering six terms with potential inner-being relevance

Two questions must be answered before the vertical pass analysis can proceed:

- **Question 1:** Does H3824 le.vav have *any* verse record for Jer 7:24 (active or deleted)? If yes, what is its status? If no, the construct form was not captured.
- **Question 2:** Is the 17/21 deleted ratio for Jer 7:24 normal across the corpus, or is it anomalous to this verse?

---

## Naming convention

Output file: `wa-verticalpass-levresults-20260408.json`

Per WA-Reference-v5.5-20260330.md §1:
- Instruction documents: `WA-{DescriptiveName}-v{n}-{date}.md` (PascalCase)
- Vertical pass outputs: `wa-verticalpass-{scope}-{date}.json` (lowercase)

---

## Schema reference — fields used

**`wa_verse_records`:** `id`, `reference`, `delete_flagged`, `mti_term_id`
**`mti_terms`:** `id`, `strongs_number`, `transliteration`, `gloss`, `status`, `delete_flagged`

Joins: `wa_verse_records.mti_term_id = mti_terms.id`

---

## Query 1 — Does H3824 le.vav have any verse record for Jer 7:24?

Returns all wa_verse_records rows where the linked term is H3824 and the reference is Jer 7:24 — active and deleted.

```sql
SELECT
    wvr.id              AS verse_record_id,
    wvr.reference,
    wvr.delete_flagged  AS vr_del,
    mt.id               AS mti_id,
    mt.strongs_number,
    mt.transliteration,
    mt.gloss,
    mt.status           AS mt_status,
    mt.delete_flagged   AS mt_del
FROM wa_verse_records wvr
JOIN mti_terms mt
    ON wvr.mti_term_id = mt.id
WHERE mt.strongs_number = 'H3824'
AND wvr.reference LIKE '%Jer%7%24%';
```

Expected outcomes:
- **Row returned, vr_del=0** — le.vav is actively linked; the original query filtered it out by status. Follow up: why was it not in Q2 results from the initial query?
- **Row returned, vr_del=1** — le.vav was extracted but the verse record was deleted; same pattern as H3820A
- **No rows** — the construct form *libbam* was not captured during Session A extraction; this is a data coverage gap

---

## Query 2 — Active vs deleted verse record ratio for Jer 7:24 and neighbours

Establishes whether the 17/21 deleted ratio for Jer 7:24 is normal or anomalous by comparing with the five surrounding verses.

```sql
SELECT
    wvr.reference,
    COUNT(*)                                                        AS total_records,
    SUM(CASE WHEN wvr.delete_flagged = 0 THEN 1 ELSE 0 END)        AS active,
    SUM(CASE WHEN wvr.delete_flagged = 1 THEN 1 ELSE 0 END)        AS deleted,
    ROUND(
        100.0 * SUM(CASE WHEN wvr.delete_flagged = 0 THEN 1 ELSE 0 END)
        / COUNT(*), 1
    )                                                               AS pct_active
FROM wa_verse_records wvr
WHERE wvr.reference IN (
    'Jer 7:22', 'Jer 7:23', 'Jer 7:24', 'Jer 7:25', 'Jer 7:26'
)
GROUP BY wvr.reference
ORDER BY wvr.reference;
```

If the pct_active for Jer 7:24 is consistent with its neighbours, the deleted records reflect normal programme extraction behaviour — multiple terms extracted, many subsequently filtered out by Session A decisions. If Jer 7:24 has a markedly lower pct_active than neighbours, the verse was subject to specific deletion decisions worth investigating.

---

## Query 3 — Programme-wide active ratio baseline

Establishes the typical active vs deleted ratio across all verse records so we can calibrate the Jer 7:24 result.

```sql
SELECT
    COUNT(*)                                                        AS total_records,
    SUM(CASE WHEN delete_flagged = 0 THEN 1 ELSE 0 END)            AS active,
    SUM(CASE WHEN delete_flagged = 1 THEN 1 ELSE 0 END)            AS deleted,
    ROUND(
        100.0 * SUM(CASE WHEN delete_flagged = 0 THEN 1 ELSE 0 END)
        / COUNT(*), 1
    )                                                               AS pct_active
FROM wa_verse_records;
```

---

## Output format

Return as JSON named: `wa-verticalpass-levresults-20260408.json`

```json
{
  "produced_date": "2026-04-08",
  "produced_by": "Claude Code — WA-VerticalPass-LevQuery-v1.0-2026-04-08.md",
  "query_1_lev_jer724": [...],
  "query_2_vrdel_neighbours": [...],
  "query_3_programme_baseline": [...]
}
```

---

*WA-VerticalPass-LevQuery-v1.0-2026-04-08 | No prior version*
