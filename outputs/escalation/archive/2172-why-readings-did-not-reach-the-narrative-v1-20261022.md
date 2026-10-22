# 2172 — Why the readings did not reach the narrative: the infrastructure was bypassed

Escalation: #2172. Status: a diagnosis, with two questions for you. Nothing is proposed or built.

## Your correction

Researcher, 2026-10-22 (verbatim): "not approved.  the iba table infrastructure already includes all
the components you need to track and manage the analytics.  You have not even looked at the current
infrastructure, you just propose more new tables, more new methods with no regard to understand or
figure out what you are doing wrong".

You were right. The rejected design looked only at the narrative tables. It is archived at
`outputs/escalation/archive/2172-reading-completeness-control-design-v1-20261022.md`.

## The chain the infrastructure already provides

All of these are active in `cfg_table` (iba.db):

| Step | Table | What it holds | Rows |
|---|---|---|---|
| what a reading found | `ib_observation` | one typed finding (stage, tag, strong, obs_text, meaning_source) | 11,480 |
| where it is grounded | `ib_node` | the verse and strong each finding rests on | 12,909 |
| verse state | `verse_meta.status` | exclude / citated / analysed, with `status_changed_at` | 29,762 verses |
| what the narrative rests on | `narrative_claim_source` | claim to verse | 1,851 |
| what the narrative cites | `narrative_citation` | passage to verse | 7,562 |
| the weave | `narrative_update`, `narrative_update_ref` | each weave, its sources, and the escalations and thread items it names | 160, 219 |
| the work | `escalation_thread_item` | each strand item and its settlement | 496 |

With these, a reading's findings can be traced mechanically to the narrative. For any reading, the
verses its observations rest on (`ib_node`) can be compared with the verses the narrative cites or
rests on (`narrative_citation`, `narrative_claim_source`). No new table is needed.

## What actually happened (live queries, 2026-10-22)

- **`ib_observation`:** every row was written in September 2026; the last is 2026-09-23. No reading
  since then wrote an observation.
- **Clusters with observations:** M67 (3,183), M83 (1,553) and M49 (954), plus 5,712 rows with no
  cluster. Every other cluster has 1 to 6.
- **What the October weaves read:** the 73 `narrative_update` rows that name source files point at
  readings of M25 (18), M18 (18), M09 (13), M64 (12), M08 (11), M02 (6), M01 (6), M72 (3), M47 (2)
  and M20 (1). None of those clusters has more than 3 observations.
- **`verse_meta.status`:** NULL for all 29,760 live verses. No verse has ever been marked analysed
  or citated.
- **The link from a weave to its reading** is the file path in `narrative_update.source_files`
  (text), not rows.

**What I did wrong:** I did the October readings as free-standing md files and wove from them by
hand. The findings were never recorded in `ib_observation`/`ib_node`, and the verses were never
marked in `verse_meta.status`. So the database could not show what a reading found or whether it
reached the narrative. The infrastructure was there; I worked around it.

## What I do not know (inferential, not confirmed)

- Why the readings left the pipeline after 2026-09-23. A method change you directed, or my own
  drift? The written record I have checked does not say.
- Whether `verse_meta.status` was meant to be set by the reading (analysed) and the weave (citated).
  Its `cfg_enum` values suggest so, but no code sets it except `VerseMeta.ps1` by hand.

## Two questions

1. Should every reading record its findings in `ib_observation`/`ib_node` (through the existing
   stages, or `Observation-Enhancer.ps1`), instead of in md files? ____
2. Is `verse_meta.status` meant to mark a verse analysed when read and citated when woven? ____

When both are answered, the check is a comparison of tables that already exist.
