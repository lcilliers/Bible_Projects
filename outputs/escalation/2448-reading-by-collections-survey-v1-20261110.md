# #2448 — Final reading based on collections: where the reading is still scoped by cluster

Status: survey and decisions for the researcher (B:105). Nothing is designed or changed. Read-only reads of `iba.db` and `iba/app/ps/Reading.ps1` on 2026-11-10. Researcher, verbatim (#2368): "the final reading for the narrative will be based on collections and not clusters."

## Where a reading is scoped by cluster today
| Place | What it does now |
|---|---|
| `iba/app/ps/Reading.ps1`, step `reading.open` | opens a reading on one subgroup of a cluster (`-Subgroup`, `-HomeCluster`, optional `-Surface` or `-Verse`); the scope JSON is filed under the home cluster's folder |
| `cfg_setting reading.output_dir` | `_analytics/Clusters/{cluster_folder}`: each reading's files are filed by cluster |
| `cfg_setting reading.whole_cluster_reading_start` | how a reading on a cluster starts (#2368 is closed; no code reads it) |
| `cfg_setting reading.gap_types` | the gap type `term_cluster` (a term in scope with no cluster) |
| behaviour rules (study_method) | 117 subgroups-are-surface-groups, 118 surface-mapping-conditions, 120 scope-home-and-multiplicity, 121 reading-recorded-per-occurrence, plus 89, 94 and 115 mention clusters |
| `cfg_method_rule` | 22 active rules mention clusters (not listed here) |

## Where collections already are the unit
Engagement (`iba/app/ps/Engagement.ps1`, setting `engagement.stage`) assesses the surfaces of one collection and writes observations of stage `engagement` to `ib_observation`. All 277 collections are `confirmed` (2026-11-10).

## Not surveyed
`USER-GUIDE.md` and `GOVERNANCE.md` text on readings, the narrative tables (`narrative_section`, `narrative_claim_telling`) and how claims are anchored today; the Excel tool sheets.

## Decisions needed
**R1. The unit a final reading opens on.**
- A: one collection (the reading's scope is the collection's confirmed members and their verses), replacing `-Subgroup`.
- B: one collection, but read through its engagement observations only (no re-reading of verses).
- C: leave `-Subgroup` readings for the earlier study, and add collection readings beside them.

**R2. The cluster-based rules and settings (table above).**
- A: retire them from the reading path (inactive, kept in history) and write the collection rules as new rows, once R1 is settled.
- B: keep them and add collection rules beside them.

**R3. Where the change is recorded.**
- A: one governance rule row stating the new basis (with your words verbatim), the settings changed through `configmaint.propose`, then `GOVERNANCE.md`, `USER-GUIDE.md` and BUILD.md updated.

I recommend R1 A or B (your call on whether verses are re-read), R2 A and R3 A. The code that opens and checks a reading is a build to design after R1.
