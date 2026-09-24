# Cascade soft-delete discrepancies — live records referencing a soft-deleted parent

> Ad-hoc investigation, 2026-09-24, following escalation #1868 ("why is the 8 tables listed as unsafe not ready to be purged") and the researcher's follow-up directive: "ensure that every record that refers to deleted record are also marked as soft delete - report any discrepancies". Recomputed live via `iba.app.handlers.purge`'s own column-lookup helpers (not hand-typed table/column names), cross-checked against `purge.audit`'s own persisted findings (`research/discovery/purge-audit-v5-20260924.md`) — every count matches exactly, 0 mismatches. Read-only: nothing changed by this investigation.

**656,729 live rows across 23 parent/child pairs (8 distinct parent tables) reference a soft-deleted parent record while remaining live (not soft-deleted) themselves.** This is exactly why `purge.execute` (#1766/#1868) marks these 8 parent tables UNSAFE and refuses to touch them.

## Per parent/child pair

| database | parent (soft-deleted count) | child.fk_column | discrepancy count | sample child id -> parent fk |
|---|---|---|---|---|
| bible_research | finding (404,757) | finding_verse_index.finding_id | 405,197 | 438037->1048883; 438038->1048883; 438039->1048883 |
| bible_research | wa_verse_records (171,156) | wa_verse_term_links.verse_id | 168,121 | 750->62304; 751->62305; 754->62308 |
| bible_research | wa_term_inventory (713) | wa_verse_term_links.term_inv_id | 37,220 | 979->36; 980->36; 981->36 |
| bible_research | verse_context_group (3,067) | verse_context.group_id | 19,352 | 1->1; 2->2; 3->3 |
| bible_research | wa_term_inventory (713) | wa_term_related_words.term_inv_id | 9,257 | 11->7; 12->7; 13->7 |
| bible_research | wa_obs_question_catalogue (336) | cluster_finding.obs_id | 8,803 | 9->225; 10->225; 11->225 |
| bible_research | verse_context_group (3,067) | wa_dimension_index.verse_context_group_id | 2,957 | 1665->1782; 1666->1783; 1667->1784 |
| bible_research | wa_obs_question_catalogue (336) | wa_finding_catalogue_links.question_id | 2,705 | 1->1; 2->1; 3->1 |
| bible_research | wa_verse_records (171,156) | verse_context.verse_record_id | 918 | 20613->3720; 20615->3721; 20653->3677 |
| bible_research | wa_term_inventory (713) | wa_meaning_parsed.term_inv_id | 688 | 46->759; 100->813; 103->816 |
| bible_research | mti_terms (5,131) | mti_term_flags.mti_term_id | 644 | id->432; id->433; id->434 |
| bible_research | verse_context (2,102) | ve_lexical_legacy.verse_context_id | 242 | 4137652->42610; 4139046->9246; 4139059->9311 |
| iba | verse_lexical (975,478) | verse_lexical_note.verse_lexical_id | 173 | 319->883118; 320->883118; 321->883119 |
| bible_research | wa_term_inventory (713) | wa_term_phase2_flags.term_inv_id | 145 | id->7; id->36; id->37 |
| bible_research | mti_terms (5,131) | mti_term_cross_refs.mti_term_id | 87 | 3->22; 7->31; 14->41 |
| bible_research | wa_term_inventory (713) | wa_term_root_family.term_inv_id | 86 | 7->7; 13->14; 29->36 |
| bible_research | verse_context (2,102) | ve_lexical.verse_context_id | 68 | 7244933->64180; 7244934->64180; 7244935->64180 |
| iba | verse_lexical (975,478) | verse_lexical_note.target_verse_lexical_id | 21 | 320->436312; 341->885442; 343->885441 |
| bible_research | mti_terms (5,131) | vcg_term.mti_term_id | 13 | 3482->7540; 3483->7541; 3484->7541 |
| bible_research | verse_context_group (3,067) | vcg_term.vcg_id | 12 | 221->221; 223->223; 358->358 |
| bible_research | wa_obs_question_catalogue (336) | wa_flag_type_question_link.question_id | 12 | 1->195; 2->196; 3->197 |
| bible_research | mti_terms (5,131) | verse_context.mti_term_id | 7 | 28082->573; 63040->2689; 63041->2689 |
| bible_research | mti_terms (5,131) | mti_term_subgroup.mti_term_id | 1 | 1102->7553 |

## What this means

Each row above is a live (not soft-deleted) record whose foreign key points at a row that IS soft-deleted in its own table. Under a strict cascade-soft-delete invariant ("a record referencing a deleted record should also be deleted"), every one of these 656,729 rows is a violation. **Not fixed here** — this is a data-quality judgement call, not a mechanical correction: for the largest pair alone (`finding_verse_index.finding_id`, 405,197 rows), blindly cascading the soft-delete would soft-delete the majority of that table outright, and it isn't yet established whether that's the correct read (vs. e.g. `finding` rows that were soft-deleted for a reason that doesn't invalidate the index entries pointing at them, or a data-entry bug on the `finding` side instead). Reported per #1868's existing three-way framing: cascade the soft-delete, repoint/null the FK, or leave the parent soft-deleted rather than hard-purge it -- a per-table (or per-pair) call for the researcher, not Claude.
