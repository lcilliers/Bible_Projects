# #2509 The method for grouping the surfaces of a collection (stage 2): design (v2, 2026-11-15)

Status: design for approval (B:105). Nothing is built. v1 (archived) was not approved: it grouped by what the surfaces do for the inner being. The researcher's ruling (2026-11-15, verbatim): "2509 not approved. the surface groups has nothing to do with the inner being. it is about the meaning of the surface words. the meaning of the words should already be available in the strong meaning and in the majority of cases is about simply judging the dictionary meaning of the words".

## 1. What the grouping is

Stage 2, last part ("creating surface subgroups with collections", #2507 v7). For one collection, its surfaces are grouped **by meaning**: surfaces whose words mean the same thing, or the same kind of thing, are one subgroup, named for the meaning they share. Nothing in it judges what a word does for the inner being; that is the later stages. The researcher's groups of `thought` (#2463 v16: starting (conceive, gives thought, imagine), weighing (considered, conflicting thoughts), and the kinds of thought (imagination, meditation, minding and musing, opinion, reasoning, pondering, thinking, suggestion)) are groups of this kind: they divide the meaning of thinking.

## 2. The evidence is the dictionary meaning, already in the database

For each member surface and each Strong's code it carries: the head sense (`strong_sense`), the sense tree (`strong_meaning_tree`, by the exact code), the lexicons (`strong_lexicon`, LSJ and Mounce) where the code has them, the surface's base and its link in the collection (core, synonym, opposite; `collection_link`), and the count of its occurrences. **No verse is needed** in the majority of cases: the judgement is of the dictionary meaning. Where a surface carries two codes whose dictionary meanings differ (for example H2029 `conceive`, to conceive a child, against its figurative use) the surface is split by code, as the index already allows, and each code is judged on its own meaning. A word that is a function word in every occurrence needs no placement (RG-22).

## 3. The routine

Two new actions of `Collection-Build.ps1`, the pattern of LayerPull and LayerRecord, nothing new in the tables:

1. **`GroupPull -Collection <name>`** writes a working file (`layer.working_dir`) with a row for each member surface (and each code of a split surface) carrying the dictionary evidence of section 2, and the empty `fill`: the group's name, or `set_aside` with the reason; and a `groups` list (name, definition: the shared meaning, in words the dictionary supports).
2. **`GroupRecord -File <file> [-Check]`** checks the whole file and writes it in one transaction, or refuses all: every surface (and every code of a split surface) is covered once; every group has a unique name and a definition; every group holds a surface; a `set_aside` surface has its reason (its dictionary meaning is not the meaning this collection gathers, for example a preposition or a different sense of the same spelling); a split follows the index rule. It writes the groups and placements through `collectionindex.make_group` and `place`, each change a `surface_event` with the reason "judged from the dictionary meaning, file <name>, run <id>", `created_by` Claude, and refreshes the group on the nodes.
3. **The scrutiny:** `IndexCheck` lists for a collection each group with its definition and surfaces, each set-aside surface with its reason, and each placement marked `uncertain` (where the dictionary leaves two groups open) with what is unsettled. The researcher's `Subgroup` instruction stays for corrections and wins over Claude's placement.

The grouping gate of step 1.1 stays (every surface placed or set aside with a reason, every group holding a surface).

## 4. What the ruling changes in what is already built (applied on approval, one unit of work)

The wording and the node role of the layered reading say the groups are judged by the inner being; the ruling says they are not. Each item is a correction to the researcher's ruling and a restatement of an existing row, not a new design.

| # | Item | Home | Change |
|---|---|---|---|
| C1 | step 1.1, item `group-definition`: "What do the surfaces of this group do for the inner being? ... says definitively that these words are part of the inner being's working" | `cfg_setting layer.reading` | the group's observation states the shared meaning the dictionary gives its surfaces; node role `lexical` (not `characteristic`, an inner-being verdict) |
| C2 | B:132 (stage 2 and step 1.1 "isolates a surface with no inner-being role"), LR-01, LR-02 ("only the group definition of step 1.1 ... states what the group is or does for the inner being") | `cfg_behaviour_rule`, `cfg_method_rule` | grouping by meaning; a surface that does not carry the collection's meaning is set aside with its reason; no step states what a word does for the inner being |
| C3 | `isolated` state, "no inner-being role" in the docstrings and errors | `lib/collectionindex.py`, `handlers/collectionbuild.py` | "set aside: its meaning is not the collection's"; the state value `isolated` stays (no data change) |
| C4 | step texts of `collection.subgroup` and `collection.index`; the layered-reading paragraph and the collection-index paragraph | cfg_step, USER-GUIDE | reword; add GroupPull and GroupRecord |
| C5 | glossary entries `subgroup`, `layer (collection reading)`, `stage (collection reading)` (they say "for the inner being") | `prose_section` (B:126) | amend through Prose.ps1 |
| C6 | steps `collection.group_pull`, `collection.group_record`, grants (`collection_subgroup`, `collection_subgroup_surface`, `surface_event`, `ib_node`, `ib_observation_change`), settings for the file fields and the minimum lengths, method rules GP-01 to GP-04 | config | add |
| C7 | code `GroupPull`, `GroupRecord` (`lib/collectionindex.py` or `lib/collectiongroup.py`), `IndexCheck` report, `Collection-Build.ps1`; test `temp_2509_grouping_test_run.py` on a copy (the refusals; the nodes' group; a regroup; the comparison of the result for `thought` with the researcher's groups) | code, tests | add |

The 10 words of `thought` already recorded in stage 1 are lexical observations and are not affected.

## 5. First run and scale

The first run is `thought` (33 surfaces); the researcher's groups are the test. The scale is 169 collections, about 3,400 surfaces; because the judgement is of the dictionary meaning it needs no verse and is a short pass for each collection. Stage 1, by contrast, is read in the verses and is the large part of the work (about 17,900 surface and code words over all collections; `thought` has 177 rows).

## 6. Approval

On approval I build as the control list says, test on a copy, apply, run on `thought` and bring the report and the comparison with the researcher's groups.
