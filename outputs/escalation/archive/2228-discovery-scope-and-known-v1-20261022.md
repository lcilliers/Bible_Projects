# 2228 — Discovery: request to verses, what is known per verse, the gap (v1)

Escalation: #2228 v7. Status: discovery only, for your decisions. Nothing is designed or built
(rule 105). All numbers are from read-only queries on `iba/app/db/iba.db` and a read-only scan of
`_analytics`, 2026-10-22. The queries are listed under each table.

Your instruction (v7), in short: (a) every kind of request comes down to a collection of verses, and
the first tool is an engine that takes the request and returns that collection as JSON; (b) what is
known of each verse must be reachable without reading everything each time; (c) the gap in each core
table must be worked out inside the verse collection only.

**The finding in one line.** The tables can almost all be cut to a verse collection today, each
with named holes. The large pool that cannot is the files: `_analytics` (2,449 live files, 263 MB,
about 290,000 verse references written in the text) and the study readings kept under `outputs/`.
No index says which file reads which verse.

---

## (a) Entry point: how each kind of request reaches verses today

| Request | Route to verses that exists today | Code that already does it | Holes or open questions |
|---|---|---|---|
| Cluster | `cluster_strong` (live rows) → `verse_lexical.strong` → `verse_id` | `iba/app/lib/lexicalscope.py` `resolve_strongs` + `resolve_verse_ids_for_strongs` (config-exempt library, #2221; it reads `span`, a full scan) | None measured. All 15,528 live `cluster_strong` codes occur in `verse_lexical`. |
| Subset of a cluster | **Not defined.** Candidates that exist: `cluster_subgroup` (13 rows, 21 strongs), a strand's word family (`reading_strand_strong`, 208 rows), an English word (`word_registry` → `word_strong`), or a list of strongs given in the request | — | Q1 |
| Strong, or a collection of strongs | `verse_lexical.strong` = the exact code → `verse_id` | `lexicalscope.resolve_strongs(strong_list=…)` refuses a code that occurs nowhere and suggests the suffixed forms | Q2: does a bare code (H0430) mean all its suffixed forms (H0430G, H0430H…)? |
| Verse, or a collection of verses | A written reference (Php 3:19, Luk 14:12-14) → `verse.id` | `iba/app/lib/narrativeregister.py` `parse_refs` + `VerseIndex` (written refs, ranges, follow-ons); `lexicalscope.resolve_verse_ids_for_refs` (OSIS only) | A verse with no `verse` row is missing by design (`governance.verse_gap_by_design`). The engine has to report it, not drop it. |
| Narrative, or a section of it | `narrative_citation` (current rows, by `section_id`) → `verse_id`; a chapter is the blocks of its chapter | The citation index is filled by `narrativeregister.py` | 7,408 citations resolved, 37 unresolved. 39 of 404 current blocks cite no verse. Q3 |
| Claim | `narrative_claim_source` (`source_kind='verse'`) → `verse_id` | — | 293 of 306 current claims have a verse source; 13 do not. |
| Open item: a thread item | Thread item kinds `verse`, `cluster`, `strong` and `chapter` resolve as above; `strand` resolves through `reading_strand_strong` | Thread matching in `Escalation.ps1 -Action Match` | The kinds `escalation`, `event` and `researcher` name no verse. Of 126 `verse` items, 5 are ranges or lists. |
| Open item: a task or issue | **No structured link.** The verses are only in the free text (`comment`, `context`, `resolution`) | — | 8 of the 25 open tasks and issues have a verse-like reference in their text. Q4 |
| Not on your list: an observation | `ib_node.verse_reference` (OSIS) → `verse.osisId` | — | All 16,506 node references resolve. |
| Not on your list: an English word | `word_registry` → `word_strong` → as for strongs | `lexicalscope.resolve_strongs(word=…)` | Q1 |

So most routes exist, but they are scattered over three modules, and the cluster route scans the
whole `span` table. The open questions are about what a request means, not about missing data.

---

## (b) What is known of each verse: the sources

Your list was ib_observation, the `_analytics` files, the narrative, open items and claims. **It is
not complete.** Every source found, and whether it is keyed by verse:

| # | Source | Size (live) | Keyed by verse? | How, and the holes |
|---|---|---|---|---|
| 1 | Observations (`ib_observation`) | 7,244 draft, 4,953 withdrawn | **Indirectly** | Through `ib_node.verse_reference`. Draft observations touch 2,717 verses. 63 draft observations have no node at all, so they are tied to nothing (char-answers 43, char-reading 13, char-subgroup 5, verse-reading 2). The October dispositions sit only as text in `revisit_note`. |
| 2 | `_analytics` files | 2,449 `.md` files, 263 MB | **No** | See the table below. |
| 3 | Narrative blocks (`narrative_section`) | 404 current | Yes | Through `narrative_citation`. The holes are under (a). |
| 4 | Claims (`narrative_claim`) | 306 current, 9 held | Yes | Through `narrative_claim_source`. 40 sources are a study file and 5 are lexical, with no verse. **`observation_id` is empty on all 1,851 sources**, so no claim is linked to the observations it rests on. |
| 5 | Open items: thread items | 513 rows | Partly | See (a). |
| 6 | Open items: tasks and issues | 25 open | **No** | Free text only. Item responses (`escalation_thread_item_response`, 315 rows) are also free text. |
| 7 | *Not listed:* strand hits and faces (`reading_strand_hit`) | 4,480 hits on 3,773 verses | Yes | 4,122 hits have a face. 358 have neither a face nor a reason (#2217). **`observation_id` is empty on all 4,480**, so no hit is linked to the observation it went into. |
| 8 | *Not listed:* verse status (`verse_meta.status`) | 3,643 verses marked `analysed` | Yes | 1,554 of the analysed verses have no draft observation. The reading is recorded as done, but its result is not in the tables. Inferential: it is probably in `_analytics`, which is not checked. |
| 9 | *Not listed:* the lexical layer per verse | `verse_lexical` 1.5M rows; `verse_lexical_note` 173 rows on 10 verses | Yes | `verse_lexical` carries role, party_kind, narrative_morph and the gloss check per word. |
| 10 | *Not listed:* lexicon meaning and parse | `strong_meaning_tree`, `strong_meaning_parsed`, `strong_lexicon`, `strong_lsj_parsed`, `strong_mounce_parsed` | By strong | A verse reaches them through its strongs. 9,120 of 52,522 parsed-meaning rows also name verses (`verse_refs`). |
| 11 | *Not listed:* the debate digest | `hib` 21, `verse_hib` 235, `phenomenon` 121 on 48 verses, `operation` 121, `passage` 42, `verse_passage` 777, plus 4 small passage tables | Yes | All registered as live in `cfg_table`. Q5: are they still part of the method? |
| 12 | *Not listed:* study readings kept outside `_analytics` | `outputs/escalation` 260 `.md`, `outputs/strand-reading`, `research/discovery` 20 | **No** | For example, today's anger inner-seat reading for #2172 is under `outputs/escalation`. |
| 13 | *Not listed:* cluster subgroup anchors | `cluster_subgroup.anchor_verse_reference` | Yes | Small. |
| 14 | *Not listed, not per verse:* programme prose and Sciences | `Workflow/Programme` 102 files, `Workflow/Sciences` 104 files, `prose_section` | No | These state concepts, not verse readings. Listed so the boundary is explicit. |

History tables (`narrative_claim_change`, `narrative_update`, `narrative_passage`, `escalation_history`)
and the chapter export files are left out. They are history or copies (rules 61, 96).

### `_analytics` in detail (live files, excluding `archive/` and `.obsidian/`)

| Folder | Files | Files citing a verse | Written refs | OSIS refs | MB | Main kinds of file |
|---|---|---|---|---|---|---|
| Bible_Books | 1,740 | 1,664 | 111,671 | 29,513 | 226.4 | per-book lexical views by phase, book readings, oracle syntheses, re-read logs |
| registry | 352 | 242 | 95,048 | 16 | 26.4 | word-registry chapters (love, peace, mercy…) |
| Clusters | 230 | 217 | 32,146 | 294 | 6.4 | batch readings, observation ledgers by unit, validation registers |
| essay | 77 | 73 | 18,257 | 0 | 3.2 | the earlier essay parts, the narrative claim register |
| cross-cluster-web | 23 | 15 | 3,724 | 0 | 0.9 | co-occurrence and relationship probes |
| characteristics | 22 | 19 | 828 | 0 | 0.2 | characteristic harvests and readings |
| dimensions | 5 | 1 | 9 | 0 | 0.0 | |

"Written refs" counts patterns like `Psa 10:2`; "OSIS refs" counts patterns like `Psa.10.2`. Both are
pattern counts, not checked against `verse`. The file record (`file_manifest`) holds path, size and
date only, never content. It tags 17 of these files with a cluster and 163 with a word.

---

## (c) Can each core table be cut to a verse collection?

| Core table | Cut by verse today? | Through | What stops a clean cut |
|---|---|---|---|
| Observations | Yes, mostly | `ib_node` | 63 draft observations with no node. A strand hit does not point to its observation. |
| Claims | Yes, mostly | `narrative_claim_source` | 13 current claims with no verse source. No claim points to an observation. |
| Narrative | Yes, mostly | `narrative_citation` | 39 blocks cite no verse. 37 citations are unresolved. |
| Open items | Partly | thread items | Tasks and issues name verses only in text. |
| Lexicals (missing meaning or parse) | Yes | `verse_lexical` → strong → meaning and parse tables | The rule for what counts as missing is set: `governance.base_data_spine`. |
| Readings in files (`_analytics`, `outputs`) | **No** | none | No index exists. |

So the blocker for (b) and (c) has two parts:

1. **Files with no verse index.** About 2,700 files, where the verses appear only as text.
2. **Missing links between the tables.** Strand hit → observation and claim source → observation
   are both empty. Tasks and issues have no structured scope.

Inside the tables, the cut by verse already works through joins. It needs no reading.

---

## Already on the register (cross-checked, rule 65)

Open or parked items that touch the same ground:
- #2217: strand hits with no face recorded (the 358 above).
- #2147: Chapter 2 sections with no claims register link.
- #2146: duplicated claim source rows.
- #2175: 15 quoted parts not found in the ESV text.
- #2213: in-part tellings with no part recorded.
- #1891: `iba.db` verse coverage gap against the full canon.
- #2176: the thread audit's 187 findings.
- #2207: findings in `cfg_*`, including the free-text spellings in `ib_observation.meaning_source`.

None of them covers the verse index or the missing links. Those belong to #2228.

## Side findings, raised separately

- #2231: `cfg_table.use` for `ib_observation` describes "a small transitional store of 81
  observations". The table holds 12,197 rows.
- #2232: `file_manifest` marks 664 `.md` files under `_analytics/**/archive/` as not archived
  (`archived=0`).

---

## Decisions for you

| # | Question | Your choice | Comment |
|---|---|---|---|
| Q1 | What is "a subset of a cluster"? A cluster subgroup, a strand's word family, an English word, a list of strongs given in the request, or more than one of these? | | |
| Q2 | Does a bare strong code (H0430) mean all its suffixed forms (H0430G, H0430H…), or only an exact code? | | |
| Q3 | For a narrative section: only the verses it cites, or also the verses of the claims it tells? | | |
| Q4 | A task or issue names verses only in its text. Should it carry a structured scope (cluster, strong, verse), as thread items do, so it can be a request? | | |
| Q5 | Which of the sources not on your list belong in "what is known": 7 strand faces, 8 verse status, 9 lexical layer, 10 lexicon meaning, 11 debate digest, 12 readings in `outputs`, 13 subgroup anchors? | | |
| Q6 | Next step: design (i) the request-to-verses engine (JSON out) and (ii) the verse index for the files and the missing links, for your review, in that order? | | |
