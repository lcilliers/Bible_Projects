# Flag-type ↔ question-catalogue review — are these flag types any use?

Requested: an INNER JOIN of `wa_flag_type_question_link` to the flag type and the question
catalogue, to judge whether these flag types are of any use in relation to the questions; then a
separate extract of the actual finds (applied instances) for these flag types.

**Bottom line, up front: no, not in their current state — three independent reasons, below.**

## Extract 1 — `wa_flag_type_question_link` INNER JOIN `wa_quality_flag_types` INNER JOIN `wa_obs_question_catalogue`

```sql
SELECT l.id AS link_id, l.flag_type_id, t.flag_group, t.flag_code AS flag_type_code,
       l.question_id, q.question_code, q.status AS question_status, q.deleted AS question_deleted,
       q.section, l.context_note, l.active AS link_active
FROM wa_flag_type_question_link l
INNER JOIN wa_quality_flag_types t ON t.id = l.flag_type_id
INNER JOIN wa_obs_question_catalogue q ON q.obs_id = l.question_id
ORDER BY l.id;
```

**7 of the link table's 12 rows returned** (the other 5 are not a JOIN mismatch to ignore — see
"orphaned rows" below, they're the more important half of the finding):

| link_id | flag_type_id | flag_group | flag_type_code | question_code | question_status | deleted |
|---|---|---|---|---|---|---|
| 1 | 1 | PROSE_QUALITY | Terminology change | Q-COV-01 | redundant_v1 | 1 |
| 2 | 1 | PROSE_QUALITY | Terminology change | Q-COV-02 | redundant_v1 | 1 |
| 3 | 1 | PROSE_QUALITY | Terminology change | Q-COV-03 | redundant_v1 | 1 |
| 4 | 1 | PROSE_QUALITY | Terminology change | Q-COV-04 | redundant_v1 | 1 |
| 5 | 3 | PROSE_QUALITY | Style change | Q-COV-05 | redundant_v1 | 1 |
| 6 | 3 | PROSE_QUALITY | Style change | Q-COV-06 | redundant_v1 | 1 |
| 7 | 3 | PROSE_QUALITY | Style change | Q-COV-07 | redundant_v1 | 1 |

### The other 5 rows — INNER JOIN silently drops these; shown here instead

`wa_flag_type_question_link.flag_type_id` also has values `36` and `319`, neither of which exists
in `wa_quality_flag_types` at all (that table currently holds only ids 1–3):

| link_id | flag_type_id | question_code | question_status | deleted | context_note |
|---|---|---|---|---|---|
| 8 | 36 | Q-COV-08 | redundant_v1 | 1 | Q-COV-08 — differential context value |
| 9 | 36 | Q-COV-09 | redundant_v1 | 1 | Q-COV-09 — OT/NT repetition analytic |
| 10 | 36 | Q-COV-10 | redundant_v1 | 1 | Q-COV-10 — frequency-importance correlation |
| 11 | 319 | Q-COV-11 | redundant_v1 | 1 | Q-COV-11 — nuance differentiation by context |
| 12 | 319 | Q-COV-12 | redundant_v1 | 1 | Q-COV-12 — breadth captured in correlations |

**Why these 5 are orphaned:** `wa_quality_flag_types` was repurposed wholesale on 2026-08-23
(`flag_management_build_v1_20260823` migration, escalation #833) — its old rows retired and
replaced with 3 new `PROSE_QUALITY` rows (ids 1–3: Terminology/Methodology/Style change). `flag_type_id`
36 and 319 are what the April-2026 link rows pointed at *before* that reset; they no longer resolve
to anything.

**Why the 7 "matching" rows aren't real matches either:** the resolution above only works by ID
coincidence. The current id-1/id-3 rows ("Terminology change"/"Style change") are a *different
vocabulary*, built for a different purpose (prose-quality checking), than whatever flag types
occupied ids 1 and 3 back in April 2026 when this link table was built for STEP-coverage
research-prompt questions (`Q-COV-*`). Nothing ties today's PROSE_QUALITY flags to these questions
semantically — the join succeeding is an artefact of id reuse, not a real relationship.

**And independently of both of the above:** all 12 linked questions — every single one,
`Q-COV-01` through `Q-COV-12` — carry `status='redundant_v1'` and `deleted=1` in
`wa_obs_question_catalogue`. The entire Q-COV question family this link table maps to is retired.

## Extract 2 — actual finds (applied instances) for these flag types

```sql
SELECT * FROM wa_data_quality_flags WHERE flag_id IN (1, 2, 3, 36, 319);
-- and, for completeness, with no filter at all:
SELECT * FROM wa_data_quality_flags;
```

**`wa_data_quality_flags` has 0 rows, full stop** — not just for these flag types, for *any* flag
type. None of the three current `PROSE_QUALITY` flag types (nor the two orphaned ids) have ever
actually been applied to a piece of data. The table this join would need is empty.

## Verdict

Not of any use in their current state, for three independent reasons, any one of which would be
enough on its own:

1. **Dead questions.** All 12 linked questions are `redundant_v1`/`deleted=1` — the Q-COV family
   this link table maps to no longer exists as a live catalogue entry.
2. **Broken references.** 5 of the 12 link rows (`flag_type_id` 36, 319) point at flag types that
   were removed in the 2026-08-23 flag-types reset and never existed under those ids again.
3. **Coincidental, not semantic, matches.** The remaining 7 rows only "resolve" because the
   2026-08-23 reset happened to reuse ids 1 and 3 for an unrelated PROSE_QUALITY vocabulary — there
   is no actual relationship between today's "Terminology change"/"Style change" flags and the
   STEP-coverage research questions this table once linked them to.
4. **No real-world evidence either way.** `wa_data_quality_flags` — the table that would show a
   flag type actually being applied — is completely empty, so there's no applied-instance data to
   fall back on even setting the above aside.

`wa_flag_type_question_link`'s 12 rows are a stale, one-time write from 2026-04-20 that never
survived the flag-types reset four months later — a candidate for retirement (soft-delete or
`inactive`) rather than a live mechanism, pending your call.
