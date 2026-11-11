# #2469 Evidence report: nodes in context and the Strong's data: plan (for approval, B:17)

Session 8ca87189, Developer Mode, 2026-11-11. Nothing built yet. The raise text of #2469 names this file under a slightly different number; the id of the item is 2469.

## What you said (chat, 2026-11-11, verbatim)

"I notice you have a long list of nodes, but the node itself have only context if it is shown with the observation and in relation to the verse or surface it supports. The same for Strongs and the verse-lexical. You are not showing the richness of the data about the strong."

## What is wrong today (checked in the built report and the tables)

1. Nodes are a flat table under each observation: id, vl_id, verse, surface, strong, cluster, role, disposition. The observation text, the verse text and the word's meaning are elsewhere, so a node row means nothing on its own. An observation grounded on other verses shows only "also grounded on N node(s) outside these occurrences".
2. A word is a row of codes (strong, morph, position). The Strong's code is never opened: no native word, transliteration, gloss, meanings, related terms, cluster placement.

## What the database holds about a Strong's code (read from `cfg_table`/`cfg_column` and sample rows for H4079, H3820A, G2147)

| Source | What it gives | Checked |
|---|---|---|
| `strong` | native script (accentedUnicode), transliteration, language, STEP gloss, STEP count (a token frequency, not a verse count), origin | all three |
| `strong_sense` | the sense head (the span's meaning) and whether the code is its own lemma | all three |
| `strong_meaning_tree` + `strong_meaning_parsed` | the lemma's whole definition tree (1), 1a), 1a1)...), with verse refs on the parsed rows; keyed on the lemma code (H3820A and H3820B share the tree of H3820) | H3820A: 24 nodes; H4079: 1; G2147: 2 |
| `strong_related` | related terms: code, native form, transliteration, gloss (H3820A: 14, H4079: 22) | all three |
| `strong_lsj_parsed`, `strong_mounce_parsed` | Greek only: LSJ senses and Mounce's definition | G2147: yes; Hebrew: none |
| `cluster_strong` + `cluster` | the cluster(s) the code is assigned to, with confidence, operation flag, review flag, alternative clusters and the rationale | all three |
| `surface_subgroup` + `cluster_subgroup` + `concept_subgroup` | for this surface and code: the subgroup, its label and core description, the concept and domain | H3820A: yes |
| `strong_verse` | the verses STEP attests the code in (count), against `verse_lexical` (what the parse found): H3820A 550 and 594 | all three |
| `verse_lexical` itself | surface, unit (unit_surface, unit_size, unit_role, surface_kind), morph code, role (the cluster list), is_negator, party_kind, status | the report shows only part of these today |

Not found: a table that decodes a morph code into words (the tables with morph in their name hold verse-level morphology counts). Morph codes would stay as stored. To confirm during the build.

## Proposed change

### A. A node is always shown with its observation and with what it supports

- **Observation card** (the unit of the observation section): header (id, stage, tag, status), the text fields, then **"Supports"**: every node of that observation, grouped by verse in Scripture order, each verse with its reference and ESV text once, and under it the node's word line: the surface, the Strong's code with its transliteration and gloss (`H3820A lev "heart"`), the node's role, disposition and note, and its cluster/subgroup. Nodes inside the report's scope are marked; nodes of the same observation outside the scope are listed in the same way (instead of a count), marked "outside this report".
- **The word's own view** (by-word and by-verse layouts): under each occurrence, the observations that ground on it are listed with the node's role and disposition and the observation's text, so the occurrence reads: word, Strong's entry, then what the study says of it.
- The standalone node table is dropped from the report (the rows are inside the cards). The CSV keeps one row for each node, now with the observation text beside it.

### B. The Strong's entry, shown where the Strong's code appears

- **A "Strong's entry" block for each distinct code**, with every item above: header line (code, native word, transliteration, language, gloss, sense head, own-lemma flag); STEP count, verses STEP attests and verse_lexical rows (counts as stored, labelled as different measures); the meaning tree as an indented list; related terms as a short table; LSJ senses and Mounce (Greek); the cluster assignments (cluster code and name, confidence, operation, review flag, alternatives, rationale); and, for the surface in hand, the subgroup with its label, core description, concept and domain.
- **Where:** in the default layouts, once for each code at the first word or verse that carries it, cited by place after that (the same rule as claims and sections). In `-ByType`, a "Strong's entries" type section, in alphabetical order of code.
- **Occurrences (verse_lexical) rows** get the added stored columns: unit size, role (cluster list), is_negator, party_kind, and the code shown as `code translit "gloss"`; unit and surface-kind stay.
- Large text is shown as stored, none cut (the Greek lexicon text in `strong_lexicon.lsj` is 11,000 characters for G2147; I would show only the parsed senses of `strong_lsj_parsed`, not the raw text).

### C. Size

The `search` report is 2.4 MB now; the entries add about 10 distinct codes' worth for that collection but about 700 for a large collection like `uncovered-words`. Shown once for each code, this stays far smaller than the node lists they replace in meaning but may grow the file. I will report the new sizes in the test results.

## Build (no schema change, no new table)

- `iba/app/lib/collectionevidence.py`: a `strong_entries` loader (the joins above, read-only), the observation card with its Supports block, the Strong's entry renderer, citations by place, the new occurrence columns, the CSV observation text. `iba/app/handlers/collectionbuild.py`: none beyond passing the existing switches. One setting only if you want a switch to leave the entries out (decision 1).
- USER-GUIDE 8.14 and BUILD.md updated; tests: counts of every block against direct queries for H4079, H3820A, G2147 and a Greek code with LSJ; one observation with nodes outside the scope; both layouts hold the same entries; sizes reported.

## Decisions for you (recommendation first)

1. A switch to leave the Strong's entries out (`-NoStrongs`) for a lighter report: **recommended no**, always shown, since you asked for the richness; say yes if you want the option.
2. List the nodes of an observation that lie outside the report's scope (compact, one line each): **recommended yes**. For an observation with very many nodes this makes long cards.
3. Strong's entry once at first use and cited later (recommended), or repeated under every word.
