# #2463 The collections data structure (v1, 2026-11-14)

Status: a description for the researcher; read-only; nothing changed. Prompted by the researcher (#2463, 2026-11-14, verbatim): "before I decide on this, what is the collections data structure". Read first (B:123): `cfg_table.use` and `cfg_column.use` of every table below. Counts are my queries of 2026-11-14.

## 1. The tables and how they connect

```
verse_lexical.surface  (the word in a verse, lower-cased and trimmed)
      |   same text key
      v
surface_term           one row for each surface TEXT (and each base): its group, its base
      |  base_id (a surface points to its base term; a base is a row of the same table)
      v
collection_link        a term placed in a collection, with a tier
      |  collection_id
      v
collection             one row for each collection: the core word, status, concept_id (empty)

ib_node.collection_id  the collection of a node, found by the rule in section 3
```

## 2. The tables

| Table | Rows | What a row is | Columns that carry the meaning |
|---|---|---|---|
| `surface_term` | 6,241 (6,225 live) | a surface text or a base: 4,442 words, 1,783 phrases; 2,235 are their own base | `surface` (unique key, the same text as `verse_lexical.surface`), `form` (word or phrase), `origin` (surface, or computed for a base made by the structure step), `surface_group` (behaviour 1,204, inner_being_state 2,180, entity 717, other 2,068, 56 not yet), `group_state`, `base_id`, `base_source`, `base_state`, `collection_state` (placed 3,415, listed_only 176, set_aside 6, untouched 244; empty on 2,384 surfaces that are not a base) |
| `surface_derivation` | 4,769 | the evidence for a base: a construct that matched, a sibling group, an AI answer, the default "own", or the researcher | `term_id`, `method`, `kind` (inflection, derivation, lead_opposite, lead_other), `base_word`, `base_term_id`, `accepted` |
| `collection` | 278 | a collection of terms of like meaning, named for its core word | `core_term_id` (the seed term), `name`, `status` (confirmed 169, merged 86, retired 23; indicative is the not-yet-reviewed state), `merged_into_id`, `concept_id` (empty on all), `pole_word`, `pole_of_pole`, `pole_reciprocal`, `pole_real_word` |
| `collection_link` | 11,722 | a term placed or listed in a collection | `collection_id`, `term_id`, `tier`, `shared` (the exception: live in two collections), `superseded_by_id` (a change is a new row; the replaced row gets `deleted` = 1), `ai_call_id`, `reason` |
| `collection_listing` | 4,145 | a helper list: each synonym or opposite the model listed for a core word and what became of it | `word`, `kind`, `term_id`, `outcome` (bound, refused, not_in_pool, unjudged) |
| `surface_event` | 9,715 | the record of every change to a term, group, base, link or collection | `subject_kind`, `subject_id`, `action` (confirm, correct, move, remove, merge, retire, reopen, set_tier, set_group, set_base, mark_deleted), `value_before`, `value_after`, `by`, `reason` |
| `surface_flag` | 509 | an item met and not settled (a possible opposite, a meaning shift, a held pair, an AI failure) | `subject_kind`, `subject_id`, `kind`, `note`, `status` (open or settled), `escalation_id` |
| `surface_eval_case` | 252 | the provisional test cases a prompt or threshold is tried against | `module`, `a`, `b`, `expected`, `standing` |

The tiers of `collection_link` (live rows): core 169 (the seed), synonym 1,685, opposite 151 (the other pole, accepted when two judges agree), gathered 339 (members placed at the researcher's instruction, by `Gather`), phrase 1,069, associated 2,395 and possible_opposite 356 (listed apart for the researcher, not members), set_aside 216 (listed by the model and refused by the judge). The members are the tiers in `cfg_setting collection.member_tiers` (core, synonym, opposite, gathered, phrase). 6,380 live links belong to the 169 confirmed collections.

## 3. How a word in a verse reaches its collection

A surface text is a term. If the term has a link of its own in a member tier, the collection of that link is its collection. If it has none, the collection is that of its base term (`surface_term.base_id`). Each surface is in exactly one collection (B:129); `shared` marks the exception. `ib_node.collection_id` repeats the result on the node, so an observation is found through the collection (62,072 of 68,406 live nodes carry it). A phrase is one term and is placed in one collection, not by each of its words.

## 4. The thought collection as one example

`collection` row 56, name thought, status confirmed, core term 32 (`thought`), pole word thought (reciprocal), `concept_id` empty. Its live links: core 1 (thought); synonym 22 (conceive, considered, imagination, imagine, imagines, imagining, meditate, meditates, meditation, musing, opinion, pondering, ponders, reason, reasoned, reasoning, think, thinking, thinks, thoughts, weigh, weighing); gathered 4 (regard, regarded, suppose, supposing); phrase 6 (conflicting thoughts, gives thought, mind on, minds on, once regarded, setting your mind); set_aside 1 (ponder, the base, while its forms pondering and ponders have links of their own); and a list of associated words (abide, believe, consider, mind, muse, quiet and others), which are listed apart and are not members.

## 5. What the structure does not hold

- **No grouping inside a collection.** A tier says how a term stands to the core word (synonym, opposite, gathered); it is not a group by what the word does. Your layer 1 groups (starting, weighing, the types of thought) have no table, row or column.
- **No concept above it yet.** `collection.concept_id` is empty on all 169 live collections.
- **No domain.** Nothing links a collection to a domain; the 14 domains are linked only through the concepts built on subgroups.
- **No sense of a surface within a collection.** A surface is one term, so a word with two senses (for example `thoughts` as plan and as thinking, or `reason` as cause) is one member with no row for each sense. The old subgroup pairs (`strong` + `surface`) did carry that split.
- **The `shared` flag was not checked.** 274 live links are flagged shared (core 44, synonym 216, opposite 14), against the rule that each surface is in exactly one collection (B:129). I have not checked whether those flags are current.

## 6. Not done

Nothing changed. The record is in `surface_event`, `surface_flag` and `collection_link`; the report of any one collection is `Collection-Build.ps1 -Action Evidence`.
