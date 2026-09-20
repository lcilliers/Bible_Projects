> **v2 note:** identical content to the original — refiled through `filingkit.versioned_path()`
> (the actual governed one-off-report mechanism, `governance.oneoff_report_dir`/
> `_naming_pattern`/`_archive_dir`) instead of a hand-typed path. v1 is archived at
> `outputs/archive/1766-soft-delete-purge-audit-20260918.md`.

# Escalation #1766 — soft-delete purge audit

Built per your v2 spec: (a) report by table of soft-deleted counts, (b) for tables >10, check
dependencies and report unsafe tables. Run live against BOTH databases, all 73 registered
soft-delete columns (`cfg_column` name IN `deleted`/`delete_flagged`) — not a sample.

## Safe to purge (no live row references any of its soft-deleted rows)

| database | table | soft_deleted | pk |
|---|---|---|---|
| iba | candidate_seed | 281 | id |
| iba | cluster_strong | 1,904 | id |
| iba | hib | 42 | id |
| iba | operation | 56 | id |
| iba | operation_party | 114 | id |
| iba | passage | 18,516 | id |
| iba | phenomenon | 56 | id |
| iba | span | 13,268 | id |
| iba | strong | 250 | strongNumber |
| iba | strong_lexicon | 241 | strong |
| iba | strong_meaning_tree | 262 | id |
| iba | strong_related | 409 | id |
| iba | strong_sense | 250 | strong |
| iba | verse_hib | 250 | id |
| iba | verse_passage | 24,913 | id |
| iba | word_strong | 262 | id |
| bible_research | cluster_finding | 1,633 | id |
| bible_research | cluster_subgroup | 19 | id |
| bible_research | finding_question_link | 342 | id |
| bible_research | mti_term_subgroup | 173 | id |
| bible_research | segment_unit | 89 | id |
| bible_research | vcg_term | 3,093 | id |
| bible_research | ve_lexical | 174,223 | id |
| bible_research | ve_lexical_legacy | 83,243 | id |
| bible_research | wa_dimension_index | 29 | id |
| bible_research | wa_finding_catalogue_links | 414 | id |
| bible_research | wa_term_root_family | 24 | id |

(Tables at or under the 10-row threshold — e.g. `ve_lexical_faculty_backup` (2),
`wa_term_phase2_flags` (1), `passage_emergent_question` (1), `hib_referent_option` (5),
`cluster` (5), `wa_obs_question_catalogue`/iba (4) — not dependency-checked per your own
threshold, but also all trivially small.)

## UNSAFE — a live (non-deleted) row still references a soft-deleted row's PK

| database | table | soft_deleted | referenced by (table.column) | live rows at risk |
|---|---|---|---|---|
| iba | **verse_lexical** | 975,478 | verse_lexical_note.verse_lexical_id | 173 |
| iba | | | verse_lexical_note.target_verse_lexical_id | 21 |
| bible_research | **finding** | 404,757 | finding_verse_index.finding_id | 405,197 |
| bible_research | **wa_verse_records** | 171,156 | verse_context.verse_record_id | 918 |
| bible_research | | | wa_verse_term_links.verse_id | 168,121 |
| bible_research | **wa_term_inventory** | 713 | wa_meaning_parsed.term_inv_id | 688 |
| bible_research | | | wa_term_phase2_flags.term_inv_id | 145 |
| bible_research | | | wa_term_related_words.term_inv_id | 9,257 |
| bible_research | | | wa_term_root_family.term_inv_id | 86 |
| bible_research | | | wa_verse_term_links.term_inv_id | 37,220 |
| bible_research | **mti_terms** | 5,131 | mti_term_cross_refs.mti_term_id | 87 |
| bible_research | | | mti_term_flags.mti_term_id | 644 |
| bible_research | | | mti_term_subgroup.mti_term_id | 1 |
| bible_research | | | vcg_term.mti_term_id | 13 |
| bible_research | | | verse_context.mti_term_id | 7 |
| bible_research | **verse_context** | 2,102 | ve_lexical.verse_context_id | 68 |
| bible_research | | | ve_lexical_legacy.verse_context_id | 242 |
| bible_research | **verse_context_group** | 3,067 | vcg_term.vcg_id | 12 |
| bible_research | | | verse_context.group_id | 19,352 |
| bible_research | | | wa_dimension_index.verse_context_group_id | 2,957 |
| bible_research | **wa_obs_question_catalogue** | 336 | cluster_finding.obs_id | 8,803 |
| bible_research | | | wa_finding_catalogue_links.question_id | 2,705 |
| bible_research | | | wa_flag_type_question_link.question_id | 12 |

**Reading this table:** "live rows at risk" = rows that are themselves NOT soft-deleted but still
point at a PK that a blind `DELETE FROM table WHERE deleted=1` would remove — physically purging
the left column's table today would leave those referencing rows dangling. This isn't necessarily
wrong forever (some of these may be legitimately supersede-able), but none of the 8 flagged tables
can be blindly bulk-purged as-is.

## Not built yet: (c) the actual removal utility

Deliberately not built this turn — two reasons: (1) v1's open design questions (dependency-aware
purge ORDER vs. a deny policy, and whether there's a retention window before physical deletion)
weren't actually answered by v2's spec, just restated as "provide utility"; (2) the safe-list above
includes `verse_passage` (24,913 rows) and `span` (13,268) etc. — none individually huge, but I'd
rather build the real removal logic against a confirmed policy than guess at ordering/batching for
73 tables across two databases in the same turn as first computing which are even safe.

**Proposed next step:** build `Purge-SoftDeletes.ps1` (mirrors `Spine-Check.ps1`'s shape — report-
first, `-Preview` default true, an explicit `-Preview:$false` to actually delete, one table at a
time) restricted to the 27-table safe-list above at first; the 8 unsafe tables stay blocked until
you decide, per table, whether to also purge the referencing rows (cascade) or leave both sides
alone. Say go and I'll build it as its own registered utility (cfg_step/cfg_utility, same unit of
work per governance.new_utility_registration_timing).
