# #2479 Phrases as members of their collections, with engagement: plan

Researcher decision (2026-11-11, verbatim): 'the should be members, if the verses for the phrase and not the same verses as another member already included. Also, phrases that is not a repeat of another member, should have its own observations and should be covered by engagement process.'

## How I read "not the same verses as another member"

A phrase is a repeat of a member when one of its `verse_lexical` rows is already an occurrence of a member: the same row counted twice. Checked for the collection `search` (21 phrases, 45 rows in 42 verses): no phrase row is a member row. A phrase surface never equals a member surface, so a row cannot be both. The build keeps a guard that no row is counted twice, and the test proves it.

Read at the level of the verse instead, three phrases would be left out, because every verse of theirs already holds a member word: 'search for' (Job 10:6, where the member 'seek' is H1245 and the phrase is H1875), 'searching for' (Luk 2:45, member 'find' G2147, phrase G2212) and 'seek me diligently' (Pro 1:28 and Pro 8:17, member 'find' H4672, phrase H7836). In each the phrase is a different word of the verse with its own Strong's code, so I treat it as not a repeat and include it (4 rows). **If you mean the verse-level reading, say so and those 4 rows are left out.**

## What changes

1. **New setting `collection.member_tiers`** = core, synonym, opposite, gathered, phrase. The exports (`lib/collectionexport.py`), the evidence report (`lib/collectionevidence.py`) and engagement (`lib/engagement.py`) read members from it. `collection.export_tiers` stays as it is: `attach_phrases` reads it as the word tiers a phrase is matched against, so adding phrase to it would match phrases against themselves. Its `use` text is updated to say so.
2. **Engagement `Pull -Missing`**: only the items (verse_lexical rows) with no live engagement observation, so the 685 word occurrences of `search` already assessed are not pulled again. Without `-Missing` Pull works as now. `check_collection` then reports the unassessed phrase rows.
3. **Evidence report**: phrases move from the Phrases section into the members and the occurrences: a member row of tier phrase, their rows in the codes section (each phrase row sits under its own Strong's code), their engagement. The Phrases section keeps the route each was attached by.
4. **Engagement of the phrases of `search`** after the build: Pull -Missing gives the 45 rows; I assess them (every assessment inferential, B:4) and record them as engagement observations, one for each phrase and role with a node for each verse, as for the words; the check and the group step follow. They are the phrases' own observations.
5. Documents: USER-GUIDE.md (Collection-Build, Engagement), BUILD.md; `cfg_setting` rows through `apply_logged` in a migration; test file `iba/app/tools/temp_2479_phrase_members_test_run.py`.

## What this does to the other collections

The member tiers are project-wide. 38 collections have been through engagement; their phrases are 4,414 verse rows that become unassessed members (the other 239 collections have no engagement yet). Nothing is run on them in this build: `check_collection` shows the gap, and I raise one item for it. All other exports gain the phrase rows as members.

## Test plan (run after the build; results go in the escalation resolution)

| id | case | expected |
|---|---|---|
| P1 | evidence report for `search` | 730 occurrences (685 + 45), no `vl_id` twice, the 21 phrases are member rows |
| P2 | engagement `Pull -Missing` for `search` before assessment | 45 items, none of the 685 |
| P3 | engagement `Pull` without `-Missing` | 730 items (behaviour as now plus phrases) |
| P4 | `attach_phrases -Check` | the same result as before the change (it uses `export_tiers`) |
| P5 | `check_collection` for `search` | the 45 phrase rows unassessed, the words complete |
| P6 | exports of a collection with phrase links | phrase rows present with tier phrase, none doubled |
| P7 | a phrase whose row is already a member row (synthetic) | counted once |
| P8 | after the engagement of the 45 rows | `check_collection` complete; observations carry the phrase surface |
| P9 | 38 engaged collections | their unassessed phrase rows counted (4,414), nothing written |

## Approval sought

Approve this plan, including my reading of "not the same verses" (row level, 4 rows of 3 phrases kept) and engagement of the 45 `search` phrase rows after the build; or name what to change.
