# #1701 — new catalogue component T2.11 "Faculty Engagement"

**Closes #1701.** Per #1704 §5 decision 4 (faculty is an end-of-read, subgroup-level reflection,
not a per-strong tag) — the fresh catalogue question that decision said still needed authoring.
Consolidates the retired T3 (Inner Faculties) tier's 11 separate per-faculty questions into one
question per axis (engagement, then pattern), asked once per subgroup's read, not per-verse-per-
faculty (the shape that made the old tier fail, #1598/#1700's own T3-Inner-Faculties-failure
analysis).

**Not written to `bible_research.db`** — per researcher instruction, this content is finalized here
and inserted directly into `iba.db` as part of **#1696's migration script**, alongside the 98
existing candidate rows and the `pattern_type` crosswalk (#1704 Phase 3). `obs_id`, `date_added`,
and `last_modified` are set at actual migration/insert time, not backdated to today.

## The two rows

| Column | T2.11.1 | T2.11.2 |
|---|---|---|
| `question_code` | `T2.11.1` | `T2.11.2` |
| `section` | `T2 — Constitutional Location and Boundaries` | same |
| `component_code` | `T2.11` | same |
| `component_title` | `Faculty Engagement` | same |
| `question_text` | *"In this verse, does the characteristic engage or is affected by specific faculties — the inner senses (hearing, sight, taste, touch, smell), spiritual discernment, the cognitive faculty (knowing, understanding, discerning), the memory faculty (the holding and retrieving of inner-being reality across time), the affective faculty (feeling and emotional experience), the creative faculty (imagination and the capacity to originate), the volitional faculty (the capacity to choose), the agency faculty (the capacity to act, initiate, and make happen), the moral-evaluation faculty (the capacity to assess against a standard of right, wrong, good, and true), conscience (the acute inner witness of sin, guilt, and conviction), conscientiousness (the integrated response of moral awareness, volition, and action), or relational capacity (the constitutional equipment for genuine connection with another person) — and if so, which faculty/faculties and how? Record none if it does not."* | *"Across the verses, what does the pattern of engagement and non-engagement with the faculties indicate about the characteristic's nature?"* (typo "facultiwa" → "faculties" fixed) |
| `pattern_type` | `faculty-engagement-reflection` | `faculty-engagement-reflection` |
| `scope` | `Verse-context` (matches the per-verse-question sibling pattern, e.g. T2.1.1/T2.9.1) | `Characteristic (HIB behaviour)` (matches the pattern-across-verses sibling, e.g. T2.9.2 — the question is explicitly about the characteristic's nature) |
| `source_word` | `Programme` (matches every other live row) | same |
| `source_registry_no` | NULL | NULL |
| `status` | `active` | `active` |
| `deleted` | `0` | `0` |
| `catalogue_version` | `v2-2026-09-16` (matches the project's own versioning: same v2, new date-stamped batch) | same |
| `review_note` | *"Added 2026-09-16, escalation #1701 — consolidates the retired T3 (Inner Faculties) tier's 11 per-faculty questions into one engagement question per subgroup read, per #1704 §5 decision 4. Not the same axis as T2.1 (constitutional location) — a genuinely separate component, confirmed with the researcher before placement."* | same |
| `tier` | `T2` | `T2` |
| `prompt_seq` | `1` | `2` |
| `source` | NULL | NULL |
| `obs_id` / `date_added` / `last_modified` | set at migration/insert time | set at migration/insert time |

## What this does NOT resolve

`T2.1`'s own gap (#1704 Phase 2 event 13, "constitutional-level vocabulary detection" — no T-code
covers spirit/soul/heart/mind location vocabulary) is a **different, separate, still-open item** —
location and faculty-type are different axes, which is exactly why this became its own component
(`T2.11`) rather than extending `T2.1`. Not resolved by this addition.
