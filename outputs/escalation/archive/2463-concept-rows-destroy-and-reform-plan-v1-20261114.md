# #2463 Destroying the concept rows and reforming them from the collections: what it touches and the plan (v1, 2026-11-14)

Status: a plan for the researcher to correct; read-only; nothing destroyed, built or changed. Prompted by the researcher (#2463 v31, 2026-11-14, verbatim): "I started off with the concept journey, and that lead to the discovery that cluster and sub cluster is not a good source. that gave rise to the surface analysis, base forming and collections.  What must happen is the current concept rows must all be destroyed, and then reformed based on the collections and the layer 1 work to form the concepts.  the domains sit on top of the collections but I have not yet thought that through". Counts and references are from the database and code on 2026-11-14.

## 1. What I understand

1. The concept chain built on clusters and subgroups (`concept_subgroup` to `cluster_subgroup`) is not a good source, which the collections work already showed (the subgroup is retired as a starting unit, BUILD 527).
2. The 101 concept rows are to be removed and then reformed from the collections and the layer 1 groups, so the concept is a grouping of collection surfaces (concept level, the one you want the comparisons at).
3. The domains sit on top of the collections. How is not thought through, so nothing is decided about them.

## 2. What exists now

| Table | Live rows | Link | Notes |
|---|---|---|---|
| `concept` | 101 | `domain_id` to `concept_domain`; `narrative_section_id` empty on all | no description on any |
| `concept_subgroup` | 411 | `concept_id` to `concept`; `cluster_subgroup_id` | the link to the retired subgroups; the only way a concept reaches the words |
| `concept_domain` | 14 | `narrative_chapter_id` empty on all | "domains as chapters, concepts as sub-chapters" was the ruling of 2026-10-31 (#2339); the narrative was never rebuilt on it |
| `collection.concept_id` | empty on all 169 live collections | foreign key to `concept` | described as "NULL until the rollup of collections into concepts, which will replace concept_subgroup" |

Nothing else references these tables: no narrative table, no claim, no observation, no node. The only foreign keys are those three.

## 3. What reads or writes the concept rows (found by search, 2026-11-14)

| Reader or writer | What it does with them | If the rows go |
|---|---|---|
| `iba/app/ps/Concept-Edit.ps1`, `lib/conceptedit.py`, `handlers/conceptedit.py`, four steps `concept_edit.*` (#2355), `iba/app/tools/temp_2339_*` and `temp_2355_*` tests | the researcher's tool to describe a concept or domain, add a domain, set a delete flag | the tool edits rows that no longer exist; retire it (script, handler, library, steps, work package, USER-GUIDE 8.7) until the new concept is designed, or keep it for the domains |
| `lib/collectionexport.py` (`ExportMembers`, `ExportSurfaces`) | the columns `domain` and `concept` through `concept_subgroup` | the two columns become empty; remove them or point them at the new concept |
| `lib/collectionevidence.py` (docstring and the strongs listing) and `collectionevidencereport.py` | the `Cluster assignments` sheet and the Strong's section show subgroup, concept, domain | the same |
| `cfg_setting glossary.currency_check` | a glossary currency check names the concept tables | to be read and amended |
| `iba/app/USER-GUIDE.md` section 8.7 and the exports sections | describe the grouping | amended in the same unit of work (B:42) |
| `cfg_table` and `cfg_column` rows of the three tables | their recorded meaning ("a domain, a chapter of the narrative", "a concept, a sub-chapter of its domain") | the meaning has to change with the data (B:123); kept if the tables are reused, set inactive if they are dropped |
| `iba/docs/concept-mapping-spec-v1-20261031.json` | the file the rows were loaded from | stays as history |
| The programme glossary and the narrative plan (#2376, #2377 on hold) | use concepts and domains as the structure of the narrative | the structure is replaced by the collections' roll-up (your earlier ruling that the narrative follows the collections); read before it is relied on |

## 4. The plan I propose (nothing started)

1. **A named snapshot and a rehearsal on a copy** (B:97): the counts predicted before, checked after.
2. **Remove the rows.** Two options for what "destroyed" means; the project convention is a soft delete (`deleted` = 1, never removed, as `conceptedit.py` states), and a physical delete is allowed only as a one-time migration on your explicit instruction (B:51). My recommendation is a soft delete of `concept` (101) and `concept_subgroup` (411), with the reason kept, so the old grouping can still be read as history and no report needs a foreign key repaired.
3. **The domains.** Leave `concept_domain` as it is until you have thought it through (it has no rows that depend on it once the concepts are gone; it would be a list of 14 domain names with no concepts). Or remove it with the concepts. Your choice.
4. **The readers.** Retire or amend each reader in section 3, with the tool, the exports, the evidence report and USER-GUIDE together, so the code and the data agree; the rule that a code change updates BUILD.md in the same unit of work applies.
5. **Reform** (later, after layer 1 for the pilot collection): the concept is formed from the layer 1 groups of a collection and the collections that group together; the design of where a concept is held, what links a surface or a collection to it, and how it reaches the nodes is the open decision of `2463-concept-level-in-the-database-v1-20261114.md` section 5, and is not made here.

## 5. Decisions for the researcher

| # | Decision | Options | My recommendation |
|---|---|---|---|
| 1 | What "destroyed" means | soft delete of the concept and link rows (kept as history); or a physical delete (your explicit one-time instruction, B:51) | soft delete |
| 2 | The 14 domains | keep until reformed; or remove with the concepts | keep until you have thought them through; they have no dependants once the concepts go |
| 3 | When | now, with the readers amended; or at the time the new concepts are formed, so that the old ones stay readable meanwhile | at the same time as the new concepts, unless the old ones are misleading someone today; the exports and the evidence report show them as history columns until then |
| 4 | `Concept-Edit.ps1` and its steps | retire with the concepts; or keep for the domains | retire, and bring back a tool when the new concept is designed |
| 5 | The 2026-10-31 ruling "domains as chapters, concepts as sub-chapters" | superseded by the collections (the narrative follows the collections, #2486); or kept for the domains | to be decided with the domains; I have not changed it |

## 6. Not done

No row, table, tool, report, rule or document changed. I did not read the glossary entries or the narrative plan files named in section 3 beyond the search; that is part of step 4.
