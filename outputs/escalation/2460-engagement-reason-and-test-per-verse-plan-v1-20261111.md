# #2460 Engagement keeps no reason or test per verse: build plan (for approval, B:17)

Session 8ca87189, Developer Mode, 2026-11-11. Nothing built yet.

## What you approved

#2460 v5 (2026-11-11T11:12:54Z, researcher): "approved", on a resolution that asked "choose A, B or C". I take it as **A**, the option marked recommended: keep each verse's reason and test with the verse's node, written by Record and Close from the assessment, with a repair of the collections already done. If you meant B or C, say so and this plan is void.

## The defects #2460 named (v3, 2026-11-10), re-measured today

1. The per-verse reason is stored in no observation table. Today: 7,690 live engagement nodes (the item counted 5,321 before `uncovered-words` and later batches), none keeps its reason; the reasons live only in the 26 assessment files of `_analytics/surfaces/working_files/engagement` (and the confirm and reopen reasons of the 8 review files in `ib_observation_change`: 1,835 `reviewed` rows).
2. The observation's Strong code is the first verse code. Today it differs from the node's own code on 4,208 of the 7,690 nodes (2,797 of 5,321 when the item was written).
3. The one test per observation (`parts.test`) is wrong where an observation holds verses judged by different tests (the item found 52 of 685 in `search`).

## What the assessment files hold (read-only check today)

All 7,690 live engagement nodes match exactly one evaluation in the assessment files (by `verse_lexical_id`; no node unmatched, none matched twice). Every evaluation has a reason; 3,723 have a test (the rest are `not_relevant`: 3,967; `bears_on` 1,958; `relevant` 1,765). So a backfill is a clean one-to-one fill.

## Proposed build

1. **Storage (decision D1).** Two nullable columns on `ib_node`: `reason` (the verse's reason as assessed) and `test` (the test of specification 4.1 it passed; empty for a verse with no bearing). Registered in `cfg_column`; a Developer Mode migration; no other table changes. **Recommended** over rows in `ib_observation_change` (a row per node and per field is 15,000+ rows for what is the node's own data, read through a join, and a creation is not a change). If you prefer change rows, say so.
2. **Record and Close write them.** `iba/app/lib/engagement.py` `_write_plan` fills `reason` and `test` on each node it writes from the assessment's evaluation of that verse; Close does the same for a reopened item and keeps writing `reviewed` for a confirm. A node already there is filled if its columns are empty and never overwritten.
3. **Repair of the collections already done.** A one-off, idempotent migration with `-Check` fills the 7,690 nodes from the 26 assessment files (the pull file each names is checked first: a node whose evaluation is not found is listed and left empty, none expected). It writes the node columns only; observations are not touched. A second run changes nothing.
4. **Where it shows.** The evidence report's node line shows the reason and the test; `Engagement.ps1 -Action Check` reports counts of nodes with and without them.
5. **The observation Strong code (decision D2).** **Recommended:** leave `ib_observation.strong` as it is and state in `cfg_column` that for an engagement observation the node's own `strong` is the authority (the code of each verse is on each node, correct on all 7,690). Rewriting the observation code has no right answer for an observation that covers several codes. Alternative: set it to the node code when all its nodes share one and leave it otherwise.
6. **The wrong test on 52 `search` observations (D3).** Resolved by the per-node `test`; `parts.test` stays as the most common test and is no longer relied on (stated in `cfg_column`). No observation text is changed.

## Not in this build

No change to what an observation says (you said on 2026-11-10 the observations captured are far from right and the method is not settled, #2412 v26; this build only stores the reason and test beside each verse). No new assessment or model call.

## Tests (B:29, B:46)

A node with a reason and test after Record on a built assessment (a verse with bearing and one with none); Close reopen and confirm; a second Record and a second backfill change nothing; the backfill on a copy of the database: 7,690 filled, 3,723 with a test, each equal to its evaluation read from the file; a node with no evaluation is listed and left empty; the evidence report shows both; `Config-Maintenance.ps1 -Step Validate` clean; counts reported with the results.

## What you are asked

Approve this plan, with D1, D2, D3 as recommended, or name the change. `needs_followup` is set so your approval comes back to me to build.
