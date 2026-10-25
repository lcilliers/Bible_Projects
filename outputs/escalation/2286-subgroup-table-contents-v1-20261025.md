# #2286 prototype step 4: what the subgroup table holds

Date: 2026-10-25. Escalation #2286 v9. Read-only queries on live iba.db.

## 0. The researcher's reframing (v9, verbatim)

> path c) is the reverse engineering of path a) verse, belongs to subgroup, subgroup have verse
> collection; path f) is again a reverse engineering of path a). I understood threads wrong. threads
> are open items which in itself is either cluster, strong or verse entry point. If this is true it
> means everything is scoped by cluster / sub group. If I have it right, there is a subgroup table.
> what does it contain.

## 1. The tables

There are two tables, both in iba.db and both live:

- **`cluster_subgroup`:** one row per subgroup. Its cfg_table entry describes it as "a curated group
  of Strong-numbered codes within one cluster (M-code), the unit of per-subgroup reading". The columns
  are: cluster code, subgroup code, label, core description, anchor verse, sort order, status,
  source, notes, delete flag, and dates.
- **`cluster_subgroup_strong`:** which Strong's codes are in each subgroup, each with a placement
  note. `UNIQUE(strong)` holds, so each code is in at most one subgroup.

A legacy table of the same name in bible_research.db is inactive and outside the IBA results
(B:61, B:67). It is not read here.

**How a subgroup is made.** Subgroups are written by step `cluster.subgroup` (work package
cluster-reading, still registered as active). That step reads a cluster's whole list of codes,
their glosses and surfaces, and the Stage 1 observations already captured. It does this in one
session and groups the codes by meaning, at most 10 subgroups per cluster. On success it moves
cluster.status from `ready_for_subgroup_allocation` to `ready_for_reading`.

## 2. What it holds

Subgroups exist for **3 of the 80 live M clusters**, all made on 2026-09-18. There are 13 subgroups
and 21 code placements. Across all M clusters there are 2,924 code links (`cluster_strong`), so
fewer than 1 in 100 cluster codes is in a subgroup.

| cluster | subgroup | label | codes (verses each) | anchor | status |
|---|---|---|---|---|---|
| M49 Thanksgiving | A_thanksgiving_act | The verbal act of giving thanks | G2168 to thank (38) | 1Thess.5.18 | answer_complete |
| | B_thankfulness_state | The noun-named state and expression of gratitude | G2169 thankfulness (15) | 1Tim.2.1 | answer_complete |
| | C_thankful_disposition | The settled character-trait of being thankful | G2170 thankful (1) | Col.3.15 | answer_complete |
| | D_yadah_praise_confess | Outward-cast acknowledgment: praise and confession before God | H3034 to give thanks (111) | Ps.100.4 | answer_complete |
| | E_todah_offering_noun | The instituted noun-form of thanksgiving: hymn, choir, and offering | H8426 thanksgiving (30) | Lev.7.12 | answer_complete |
| M67 Sloth & Diligence | M67_A_dispositional_idleness | Idleness as inert state or condition | G0691 be idle (1), G0692 idle (7), H8220 idleness (1) | Matt.20.6 | answer_complete |
| | M67_B_dereliction_of_duty | Failure to fulfill an entrusted obligation | G0812 be idle (1), G3636 lazy (3) | 2Thess.3.7 | answer_complete |
| | M67_C_earnest_diligence | Zealous, energetic application to a task or relationship | G4709 diligently (3), G4710 diligence (12) | Rom.12.11 | answer_complete |
| | M67_D_administrative_thoroughness | Exact, complete execution of an official command | H0149 diligently (1), H0629 diligently (7) | Ezra.6.12 | answer_complete |
| M83 Seeking & Inquiring | A_general_seeking | Generic active seeking/searching | G2212 to seek (113), H1245 to seek (215) | Matt.7.7 | ready_for_reading |
| | B_intensified_seeking | Intensive/exhaustive seeking and demanding | G1567 to seek out (7), G1934 to seek after (13), H7836 to seek (12) | Luke.11.50 | answer_complete |
| | C_hostile_pursuit | Seeking with lethal or hostile intent | G2614 to seek (1) | John.5.18 | answer_complete |
| | D_consultative_inquiry | Formal consultation and diligent inquiry | H1875 to seek (152) | 1Kgs.22.8 | answer_complete |

**Coverage within the three clusters:** M49 has all 5 of its codes placed and M83 all 7. M67 has 9 of
its 11 placed; H7423B and H5647I are in no subgroup.

**Use by observations:** 1,847 `ib_node` rows carry a subgroup code, spread over 12 of the 13
subgroups. A_general_seeking, still at ready_for_reading, has none.

## 3. What this means for "everything is scoped by cluster / subgroup"

These are facts from the tables. What follows from them is for the researcher to rule on.

- **F1. A subgroup is a group of words, not of verses.** Its verse collection is derived: every verse
  holding one of its codes. Path a (subgroup to verses) is therefore query a2 with S1 and S2 from the
  step 3 file. Reversed (paths c and f), a verse belongs to every subgroup that one of its words
  is placed in.
- **F2. The reverse path is empty for most verses today.** With 21 codes placed, almost no verse has
  a word in a subgroup. Take Psa 51:10 (step 3): its five M-coded words are clean (M61), heart and
  spirit (M47), renew (M45) and right (M23). None of those clusters has subgroups, so the verse
  belongs to no subgroup.
- **F3. A word sits whole in one subgroup.** Because of `UNIQUE(strong)`, a code with two senses
  can't be split across subgroups. H3034 (to give thanks) covers both praise and confession of sin,
  and its subgroup says so in its label. Any split by sense happens later, in the reading (the word's
  face, RG-09).
- **F4. Making subgroups is a reading step in itself.** It needs the cluster's Stage 1 observations
  first and a whole-cluster read in one session. For 77 clusters it has not been done. This is the
  same point as step 3 Q1, now sharper. If everything is scoped by cluster and subgroup, the
  subgroups must come first, either as part of the work unit step or before it.
- **F5. Threads, as you now define them,** are open items that each enter at a cluster, a Strong's
  code or a verse. So a thread item is an entry into path a at one of its stages, not a stage of its
  own. Today 296 of the 305 open items are of kind `scope`: a pairing of a source cluster's codes
  against a target cluster's codes, with their verses stored. How a pairing maps to "cluster, strong
  or verse" is open.

| question | your answer |
|---|---|
| F4: are subgroups made inside the work unit step, or must they exist before it? | |
| F5: how does a scope item (a pairing across two clusters) enter path a: at its target cluster, at its codes, or at its stored verses? | |
