# #2367 glossary currency check: findings and the design decision

Checked live on 2026-11-06 (B:34). Nothing built (B:105).

## What I found

1. **The check has nothing to check against.** `cfg_setting glossary.currency_check` says each term must exist and be current in "the programme glossary (prose_section)". There is no `prose_section` table in `iba.db` (tables with "prose" in the name: `cfg_prose`, `cfg_prose_concept` only), and no narrative chapter or section in `iba.db` is a glossary (`narrative_section` has 0 rows with "glossary" in the heading or text).
2. **The only glossary on file is a draft.** `Workflow/Catalogue/1377-glossary-draft-entries-v1-20260902.json`: 68 `prose_section` rows proposed for the old `bible_research` database, dated 2026-09-02, so it is older than every surface-cycle term.
3. **The 7 terms in the setting are all in that draft** as headings: role, characteristic, operation, M-Code cluster, T2, T3, inner being. Whether each is current against today's meaning is not established; the draft is two months old.
4. **The surface terminology is mostly not in it.** Draft headings that touch it: `surface`, `strong`, `lemma`, `family`, `family root`, `word`. No heading for: base (base form), inflection, derivation, collection, surface group (and its four values: behaviour, being, inner_being_state, other), subgroup, concept, concept domain. (Headings listed from the draft; a body may still define a term, which I did not read.)
5. **`cfg_prose_concept`** (8 rows) already points some controlled values at glossary entries by an old `prose_section` id (for example glossary_role to 1066), so those pointers are dead too.
6. The build name is unclear: the 2268 migration calls B10 both "the worked-examples table (a schema change)" and "the check". Inferential: the check was parked under that label.

## Decision needed: where does the glossary live?

The check cannot be designed until this is settled.

| option | what it means | consequence |
|---|---|---|
| A | A glossary table in `iba.db` (term, definition, status, dates), loaded from the draft and extended with the surface terms | The check is a plain query: each controlled term exists and is current. Matches governance.narrative_home (everything in iba.db). A schema change. |
| B | The glossary is a chapter of the narrative in `iba.db` (blocks under a "Glossary" chapter) | No new table; the check reads `narrative_section` by heading. Needs the register route for any change (B:78). |
| C | Keep the old draft file as the glossary | Not recommended: it is a proposed write to a database that no longer carries it. |

## What the check would cover once the home exists (for A or B)

- Every term named in `glossary.currency_check` exists and is current.
- Every controlled value of the surface cycle (the `surface_term` enums: surface_group, base_source, form, origin, and the base and collection states) is either defined in the glossary or marked as a code value that needs no entry. This is the "all the new surface terminology" part of your instruction.
- A term with no entry, or an entry older than the last change to its meaning, is a finding.
- Where it runs: part of `Config-Maintenance.ps1 -Step Validate` (advisory finding), so it needs no new script.

## To approve

Choose A or B (or give a different home). On that choice I will write the term list for the surface terminology as draft definitions for you to correct, then register the check.

| decision | note |
|---|---|
| A / B / other | |
