# #2437 — Phrase attachment step: design from the researcher's D1 to D4 answer

Status: design for the researcher's approval (B:105). Nothing is built. Counts are from a read-only query on `iba/app/db/iba.db`, 2026-11-10. This file replaces `2437-phrase-head-word-design-v1-20261110.md`, which is archived with this unit of work.

## What the researcher decided (verbatim in #2437 v4)
- D1: a simple match of the phrase words with other bases; doubt the validity of those that do not match.
- D2: each match is attached to the collection of that base; more than one collection is fine.
- D3: no match is flagged for inspection.
- D4: Engagement runs only for completed collections where new verses are added.

## The step as I read it
For each live phrase of collection a (surface_term, form phrase, group behaviour or inner_being_state, 1166):
1. Split into words. A word matches when it is a live word surface_term; its base is its `base_id` (itself when none). This uses the bases already resolved, so "cried" and "gave" reach "cry" and "give" with no new model call.
2. If that base has a live `collection_link` of tier core, synonym, opposite or gathered, the phrase is attached to that collection. One attachment per (phrase, collection), with the matched words as its reason.
3. A phrase with no such word is flagged for inspection (D3).
4. No model call and no Engagement in this step (D1, D4).

## What the rule does on the live data
| Result | Phrases |
|---|---|
| Attached to exactly one collection | 399 |
| Attached to two or more collections | 518 |
| No match, flagged for inspection | 249 |

Examples with no match: done wrong, lift up, paid attention, fell down, look for, anxious about, appealed to.
Words that bring in most attachments: made 25, give 22, become 21, evil 19, became 17, good 17, take 16, make 16.

## Decisions still needed
**E1. Generic words.** Under a plain match, any phrase containing give, make, take, put, become, good or evil attaches to the collection of that word, whatever else the phrase says ("give thanks" reaches give as well as thanks). That fits your D2, but it will put many phrases in collections that are not what the phrase is about. Options: (A, recommended) attach on every match as you said, and record each match's word so you can see and remove the generic ones afterwards; (B) set aside a short, listed set of function words (up, out, him and the like) that never match, held in config, and attach on every other word.
**E2. Where an attachment is stored.** (A, recommended) a new tier `phrase` in `collection_link`, with term_id the phrase, so one row per phrase and collection and the existing check and history rules apply; (B) a separate table. A needs a new tier value registered through configmaint; B needs a new table by the stated procedure.
**E3. Where the flag is stored.** (A, recommended) `surface_flag` with a new kind `phrase_no_match` (one row per phrase, settled when you inspect it), since that table is for per-item flags and the escalation table is not (its use text).
**E4. Exports.** Setting `collection.export_tiers` lists core, synonym, opposite, gathered. (A, recommended) leave it as it is so phrases do not enter the exports yet; (B) add `phrase` so the member exports carry them.

## Engagement (D4)
Every collection is currently status `indicative`; none is recorded as completed. So no collection qualifies today and the step triggers no Engagement. How a collection is marked completed, and how "new verses added" is detected, is a separate design that I have not started.

## Build once approved (for the record, not started)
Register the tier, the flag kind and a step `collection.attach_phrases` (plan then apply, re-runnable, writes a surface_event per change) through `Config-Maintenance.ps1 -Action Propose`; code in `iba/app/lib/collectionbuild.py` and `Collection-Build.ps1`; BUILD.md and USER-GUIDE.md entries; a run proved against the counts above.
