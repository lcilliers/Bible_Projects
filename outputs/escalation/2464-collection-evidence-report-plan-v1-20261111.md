# #2464 Collection evidence report: understanding and proposed plan (for approval, B:17)

Session 8ca87189, Developer Mode, 2026-11-11. Nothing has been built or written to the database.

## What I understand you want (your words in #2463 v4 and #2464 v1)

A report, for one collection or a list of them, that exposes the actual table entries for every aspect of the
members of the collection: from base data, through observations, through claims, into narrative.
- It evaluates nothing, except blatant errors or omissions (shown as such).
- It includes no inferred data: only what exists in the database.

## What I read first (B:123), recorded meanings in cfg_table / cfg_column

- `collection`: a collection of bases of like meaning, named for its core word; `status` (indicative, confirmed, merged, retired); `merged_into_id`; `deleted` (soft delete).
- `collection_link`: where a base stands in a collection and why; `tier` (core, synonym, opposite, possible_opposite, associated, gathered, phrase, ...); `superseded_by_id`; `shared`; `reason`; `ai_call_id`; `deleted`.
- `surface_term`: the surface text, its group, and its base (`base_id`).
- `verse_lexical`, `ib_node` (`verse_lexical_id`, `observation_id`, `role`, `disposition`), `ib_observation`: the observations.
- `narrative_claim_source` (`observation_id`, `verse_id`), `narrative_claim`, `narrative_claim_telling`, `narrative_section.block_text`, `narrative_chapter`: claims and narrative.
- Not yet read (to do before building): the column-level `use` and `expectation` of every column I will print, and `cfg_setting` modules `collection` and `engagement`.

## Proposed chain (every step a join on stored keys, no inference)

1. **Collection and members:** the `collection` row; its live `collection_link` rows by tier (with reason, shared, run, who made it); the member terms and the terms whose base is a member (the member rule of `collection.export_tiers` and Engagement).
2. **Base data:** for each member surface, its `verse_lexical` rows (verse, position, Strong's code, morph, surface kind, unit) and the verse's ESV text.
3. **Observations:** every live `ib_node` on those `verse_lexical` rows, with its `ib_observation` (stage, kind, role, text, basis, status), and the history in `ib_observation_change` where it exists.
4. **Claims:** `narrative_claim_source` rows that rest on those observations or those verses, with the claim in `narrative_claim` (text, status, verdict).
5. **Narrative:** `narrative_claim_telling` to `narrative_section` (block text) and `narrative_chapter`.

Each section prints the rows as stored. Where a link in the chain has no row, the report says "no rows in <table> for <key>" (an omission shown, not judged). Blatant errors (a link to a deleted or missing row, a node with no observation, a claim source pointing at a verse not in the collection) go in a separate "stored-data faults" section with the query that found them.

## Proposed form (new code only, no schema change)

- A new action `Evidence -Collection a[,b,c]` on `iba/app/ps/Collection-Build.ps1`, code in a new `iba/app/lib/collectionevidence.py`, registered through the app's normal step registration (this mode bypasses only the approval gate). It reads the tables and writes nothing to them.
- Output: one `.md` file per run under a new `collection.evidence_path` setting, plus the same rows as CSV beside it. Chat gets a pointer and counts.
- `-Collection` takes one name or a comma list; an unknown name refuses at once and writes nothing.
- USER-GUIDE.md section 8.14 and BUILD.md updated (E:12, `governance.build_md_on_code_change`); a test run on one small and one large collection, with counts checked against direct queries (B:1, B:2).

## Points where you may want to decide (B:44, B:105), my recommendation first

1. **Home:** a new action `Evidence` on `Collection-Build.ps1` (recommended), or a separate script `Collection-Evidence.ps1`.
2. **Size:** a large collection gives thousands of rows. Recommended: the `.md` carries every row grouped by member surface then verse, with CSV for sorting, and no cap.
3. **Phrases:** collections also hold `phrase` tier links (#2437). Recommended: show them as their own section, since they are stored, with their reason route.
4. **Test collections:** `search` (the subject of #2463) and one small collection.

## Not in this report

No evaluation, no ranking, no counts presented as findings, no model calls, no inferred links.
