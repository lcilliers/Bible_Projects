# #2448 — The final reading based on observations by collection: design for decision

Status: design for the researcher's decision (B:105). Nothing is built or changed. Researcher, verbatim (#2448): "the final reading will be based on observations by collection"; approved R1 B, R2 A and R3 A on 2026-11-10 (survey: `outputs/escalation/2448-reading-by-collections-survey-v1-20261110.md`). Facts below are from reads of `iba/app/lib/reading.py` (`open_`, line 192), `iba/app/ps/Reading.ps1` and `iba.db` on 2026-11-10.

## How a reading is opened today
`Reading.ps1 -Step Open` takes exactly one `-Subgroup` of a cluster (optionally `-Surface` or `-Verse` to segment it). The scope is the subgroup's verses (`verse_scope.resolve`), the reading's home is the cluster (`reading.home_cluster`), the files go to `_analytics/Clusters/{cluster_folder}` (`reading.output_dir`), and `reading.gap_types` has a gap `term_cluster`. Observe puts verses in hand, Record writes the findings, Synergy and Apply make the claims, Narrate and Publish write the chapters. `ib_observation` holds 455 observations of stage `engagement` (written by `Engagement.ps1`); `ib_node` carries `role` and `reading_id`.

## What the new basis needs
A reading opened on one collection: its scope is the verses of the collection's member surfaces, and the observations it works from are the engagement observations on those verses (R1 B). The later steps (Synergy, Apply, Narrate, Publish) stay as they are.

## Decisions
**C1. Where the collection is held on the reading.**
- A (recommended): a new column `reading.collection_id` (an `ib_*`-style schema change through the stated procedure), `home_cluster` left empty for a collection reading.
- B: reuse `home_cluster` to hold the collection name (no schema change, but a column that means two things).

**C2. The scope of a collection reading (which verses).**
- A (recommended): the verses where a member surface of the collection occurs: members are the tiers in `collection.export_tiers` plus the new tier `phrase` (#2437).
- B: only verses already assessed by Engagement for that collection.

**C3. What Observe puts in hand.**
- A (recommended): per verse, the engagement observations of the collection's surfaces (their roles and faces) with the verse and its passage; the reading confirms, modifies or adds findings (the verse is read first, B:116).
- B: engagement observations only, no verse re-read.

**C4. Gaps.** The gap type `term_cluster` is replaced by: a member surface with no engagement assessment in a verse of the scope (recommended), so a collection is read only when it is fully engaged.

**C5. Files.** `reading.output_dir` becomes a collection folder pattern (recommended: `_analytics/Collections/{collection}`), registered through `configmaint.propose`.

**C6. Order of work.** Engagement must be run on a collection before it can be read (#2412: how to run engagement on all collections is still your decision). The first collection reading would be on a collection already engaged, as a pilot, before the code is generalised.

**C7. Existing cluster readings (10 rows in `reading`).** Left as they are (history); `-Subgroup` stays accepted until the cluster rules are retired (R2 A), then is refused with a pointer to `-Collection`.

## What approval starts
On approval of C1 to C7 as recommended I write the full change list (code in `lib/reading.py`, handler, `Reading.ps1`, the config rows, the cluster rules to retire, GOVERNANCE.md, USER-GUIDE.md, BUILD.md and a test plan, B:46) as a second design for your approval before any build.
