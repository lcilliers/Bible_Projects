# #2268 The ledger work and the observations: what was done, and how it relates (v1)

**Date:** 2026-10-24 · **Escalation:** #2268 · **Status:** an account from the live tables and files, read-only. Nothing has been changed.

Researcher, chat 2026-10-24 (verbatim): *"R14-R17.  It looks like the ledger work you did in the last few days got lost, and got confused with the catalogue work in the past.  I am now confused about you have done in the ledger work and how does in correlate with the observations."*

**In short.** `ib_observation` holds two bodies of work, made by two different methods at two different times, on almost entirely different verses:
- **the catalogue work** (September);
- **the ledger work** (October).

My #2268 files treated them as one record under one set of rules: the September catalogue rules. That is the confusion you saw. #2260's findings carry the same confusion, because they measured the ledger observations against the catalogue's rules (§5).

## 1. The two bodies of work, side by side

| | Catalogue work (September) | Ledger work (October) |
|---|---|---|
| **Method** | the API generator stages: Stage 1 (`lexical.meaning`, `lexical.relational`) and the characteristic stages (`cluster.subgroup`, `.reading`, `.answer`) | strand readings: each strand's words read verse by verse, written up in observation **ledgers** (files), with each word's **faces** |
| **What it answers** | the question catalogue (`wa_obs_question_catalogue`): one answer per word occurrence per question (M0.1, M0.5, M0.6, M0.7, M0.8, D7.7 …) | the strand's own questions: what the inner being does in the verse, by face and by party; key statements with setting, meaning, implication, chain, parties, basis |
| **Its rules** | the checklist `iba/docs/ib-observation-governing-rules-checklist-v1-20260916.md`; the method rules on those steps; `ib_observation.tag_guidance`; the #1782 status meanings | the strand rules B:69 to B:73, B:79, B:88 to B:95, and the role guide v2 (2026-10-19); the ledger layout itself (faces by party, units, key statements) |
| **Stage in `ib_observation`** | `verse-reading` (10,595 rows, 4,953 withdrawn by re-runs); `char-answers` 748; `char-reading` 118; `char-subgroup` 19 | `strand-reading` (773 rows) |
| **Verses observed (live rows)** | 718 | 2,428 |
| **Verses in both** | 55 | 55 |
| **Carries a catalogue question** | every `verse-reading` row; the `char-answers` rows | none |
| **Claims resting on it** | 2 claims (C-331 on a `verse-reading` row, C-387 on `char-answers` rows), each also resting on ledger rows | 66 claims (63 current, 3 held), on 83 observations |

66 claims rest on an observation: 63 current and 3 held, all on ledger observations, two of them also on a catalogue row. The other 303 current claims cite verses only.

## 2. The ledger work, end to end

**1. The ledgers (October, files).** Each strand was read in units, and the readings were written into observation ledgers under `_analytics/`:

| Strand | Ledger files |
|---|---|
| fear (M01) | 7 files in `_analytics/Clusters/M01 - fear-awe/` |
| anger (M02) | 11 files in `_analytics/Clusters/M02 - anger-wrath/`, including an M47 seat ledger |
| life-death (M25) | 6 files in `_analytics/Clusters/M25 - life-death/` |
| origin of thought | 1 file in `_analytics/cross-cluster-web/origin-of-thought/` |

A ledger has two parts:
- **(A) the faces:** each face of the word by party, with its hits, the parties named and example verses;
- **(B) the observations:** key statements, each with an id (e.g. `AN-01`), its verses, and its parts (setting, meaning, implication, chain, parties, basis).

**2. The strand tables (October, #2172).** `Strand-Reading.ps1` put each strand into the tables:
- its words, in `reading_strand_strong`;
- every occurrence, in `reading_strand_hit`, with the face it was read as, or a reason it has none.

| Strand | Words | Hits | With a face | With a reason | Linked to an observation |
|---|---|---|---|---|---|
| fear | 94 | 1,012 | 1,012 | 0 | 0 |
| anger | 65 | 892 | 892 | 0 | 0 |
| life-death | 26 | 2,218 | 2,218 | 0 | 0 |
| origin of thought | 23 | 358 | 117 | 14 | 111 |

All four strands are now `superseded` (#2228 D-a).

**3. The catch-up import (2026-10-22, #2172).** The key statements of the October ledgers were imported into `ib_observation` as stage `strand-reading`, tag `key-statement`:

| Strand | Rows | Run |
|---|---|---|
| fear | 140 | `CATCHUP-2172-B-20261022-fear` |
| anger | 313 | `CATCHUP-2172-B-20261022-anger` |
| life-death | 159 | `CATCHUP-2172-B-20261022-life-death` |
| origin of thought | 24 | `CATCHUP-2172-B-20261022-origin-of-thought` |
| anger (Record) | 26 | `RUN-20261022_135240_954-STRANDREAD` |

How a ledger observation maps onto the table:

| In the ledger | In `ib_observation` / `ib_node` |
|---|---|
| the observation's id (e.g. `AN-01`) | `stable_key` (`anger:AN-01`) |
| the key statement | `obs_text` and `meaning` |
| setting, implication, chain, parties | the columns of the same names |
| basis (stated / read) | `basis` |
| its verses and words | one `ib_node` per verse and word |

How full those parts are, across all 773 rows:

| Part | Rows that have it |
|---|---|
| meaning | 773 |
| basis | 773 |
| parties | 294 |
| strong | 268 |
| implication | 257 |
| chain | 197 |
| setting | 180 |
| catalogue question | none, by design |

**4. The readings (2026-10-23 and 24, #2228, `Reading.ps1`).** These wrote 111 more `strand-reading` rows: the M64 readings of #2247 and others, with no `stable_key`. They also changed the status of imported rows at gate 2: `resolved` where a claim carries the row, `open` where it is held on an item.

**5. What did not carry across.**
- **The faces.** 4,239 faces are recorded on `reading_strand_hit`, and only 111 of them are linked to an observation. The rest exist only on the hits and in the ledger files' part A. The reading process collates strand hits only to ask whether a hit is still unread; it does not show a reader the faces already recorded.
- **The ledgers' part A** (faces by party, with their verse counts) has no table of its own.
- **The file readings not yet imported** are found by `Reading-Index.ps1` as `read_in_files_only` gaps: 235 indexed files, 230 of them in the cluster folders.

## 3. The catalogue work, end to end

- **Stage 1** (`verse-reading`, through the API, per cluster):
  - one answer per word occurrence per catalogue question;
  - 718 verses in 49 of the 80 M-clusters;
  - 4,953 rows withdrawn by re-runs (B:68).
- **The characteristic stages** (`char-*`, through the API, per subgroup): 885 rows, for the few clusters that reached them (92 of 95 clusters are still at the first status).
- **Its rules** are the September checklist and the method rules on those steps. Its statuses follow #1782: `draft` until looked at, `resolved` when cleared for analysis.
- Under R3c (your ruling), the API steps are retired. Their results are work already done, to be gathered (RO3) unless found below the rules.

## 4. How they correlate

- **Different verses.** 2,428 ledger verses and 718 catalogue verses, of which 55 are in both.
- **Different questions.** The catalogue answers fixed questions per word occurrence. The ledger records what the inner being does, by face and party, in key statements.
- **Different grain.** A catalogue answer is one verse and one word. A ledger key statement often spans several verses (3.8 verses on average in the catch-up, #2260).
- **Different rules and status meanings** (§1).
- **One meeting point:** the claims. Almost all claims that rest on observations rest on ledger observations.

## 5. Where my #2268 files and #2260 mixed them up

| Where | What was mixed | What it should say |
|---|---|---|
| #2260 findings (and #2261 to #2267) | the ledger observations judged against the catalogue rules: no question code, multi-verse, no Stage 1 coverage | the ledger observations have their own method (the strand rules and the role guide). Whether they meet *that* method (role per word, faces, parties, route) is the real question. The catalogue yardstick was the wrong one for them |
| overlay §2.OBS, inventory RECORD | "one record, one rule set" | two bodies of work in one table, each with its own method |
| R14 (statuses) | #1782's catalogue meanings set against gate 2's use as if one lifecycle | the ledger rows have a lifecycle of their own (imported as `draft`, then `resolved` or `open` by a reading) |
| R15 (rule set for writes) | the catalogue checklist offered as the rule set for every write | which method's rules govern observations is the open question |
| R17 (catalogue) | "does a reading answer catalogue questions" | with the API retired (R3c), what becomes of the catalogue and its 6,527 live answers (5,642 `verse-reading`, 885 `char-*`) |
| R13 (gaps) | a register of gaps | your definition: a gap is an item missing from the tables, recorded by writing it, with the gap JSON per gap type and the table id written back (#2228 v32 D.1; #2161 v8) |

The rulings review v4 rephrases R5, R6 and R13 to R17 on this footing, and adds R18 (the faces) and R19 (#2260 to #2267).
