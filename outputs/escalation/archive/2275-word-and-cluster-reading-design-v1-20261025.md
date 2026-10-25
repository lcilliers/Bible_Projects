# #2275 Design (v1): D1 and D2 read in a session; the API steps retired (#2268 B3)

**Date:** 2026-10-25 · **Escalation:** #2275, from #2268 · **Status:** design for the researcher's decision. Nothing has
been built or changed.

Researcher, chat 2026-10-25 (verbatim): *"proceed with B3"*.

What B3 must deliver is fixed in `outputs/escalation/2268-config-alignment-change-set-v1-20261024.md` §5.4 and §9 B3,
and the plan `outputs/escalation/2268-analytic-process-and-reading-plan-v2-20261024.md` §2: **D1 (word level)** and
**D2 (characteristics)** run on their own schedule, not per reading (R3a), with Claude reading in a session (R3c). The
API generator steps are retired, being tested and not cost-effective (P-4). It builds on B1 and B2
(`outputs/escalation/2273-2274-reading-phases-and-observation-record-design-v6-20261024.md`): what D1 and D2 record
are findings, one observation each, applied by nodes.

---

## 1. What is there now (live, 2026-10-25)

**The API steps to retire.**

| Work package | Step | Writes | Script | Library |
|---|---|---|---|---|
| verse-lexical | `lexical.meaning` (Stage 1, word level) | ib_observation, ib_node, run_batch | `iba/app/ps/VerseReading.ps1` | `iba/app/lib/versereadinggenerate.py` |
| verse-lexical | `lexical.relational` (Stage 1, relational half) | ib_observation, ib_node, run_batch | `iba/app/ps/RelationalReading.ps1` | `iba/app/lib/versereadinggenerate.py` |
| cluster-reading | `cluster.subgroup` (char-subgroup) | cluster_subgroup, cluster_subgroup_strong, ib_observation, ib_node, run_batch | `iba/app/ps/ClusterSubgroup.ps1` | `iba/app/lib/subgroupgenerate.py` |
| cluster-reading | `cluster.reading` (char-reading) | ib_observation, ib_node, run_batch | `iba/app/ps/CharReading.ps1` | `iba/app/lib/charreadinggenerate.py` |
| cluster-reading | `cluster.answer` (char-answers) | ib_observation, ib_node, run_batch | `iba/app/ps/CharAnswer.ps1` | `iba/app/lib/charanswergenerate.py` |

The handlers are `lexical:meaning`, `lexical:relational` (`iba/app/handlers/lexical.py`) and `cluster:subgroup`,
`cluster:reading`, `cluster:answer` (`iba/app/handlers/cluster.py`). Both handler files also serve steps that stay:
`lexical.build`, `lexical.readiness` and the lexical reports; `cluster.assign`, `cluster.validate`.

**Their settings.** `lexical.llm_api_url`, `_api_version`, `_chars_per_token`, `_model`, `_max_output_tokens`,
`_rate_input_per_million`, `_rate_output_per_million`, `_max_cost_per_batch`, `_usage_log_path`;
`lexical.meaning_max_verses_per_batch`, `lexical.relational_max_verses_per_batch`;
`cluster.recording_similarity_threshold`; `report.stage1_coverage_validation_pattern`;
`ib_observation.meaning_source_aliases`. The last is read by `recordingpass.py`, but only on the API recording path.

**What they wrote, which stays.** Live observations: verse-reading 5,642, char-answers 748, char-reading 118,
char-subgroup 19. Subgroups: `cluster_subgroup` 13 rows (M49 5, M67 4, M83 4) with 21 member rows.

**D1 and D2 in config.** Method rules RC-01 to RC-06 on step `cluster.read` and RC-07 on `word.read` exist, inactive.
Neither step exists.

---

## 2. D1: the word read (`word.read`)

**What it is.** One word at its grain, the lettered Strong's code (RG-21, B:113), read across all its occurrences in
a session. It follows the ledger method (`outputs/escalation/2273-what-a-verse-reading-teases-out-v1-20261024.md` §2):
every occurrence gets its face, grouped where occurrences share one, and the word's term reading is recorded once.

**What it reads (RO6: table data and the verses of the word only).**
- The word: its gloss, its clusters and subgroup.
- The three meaning sources: the meaning tree, and for Greek also Mounce and LSJ (`strong_lexicon`).
- Its related words (`strong_related`, keyed on the exact code).
- Its surfaces with their counts (B:110).
- Every occurrence, grouped by surface: the verse text, the morph, and every finding already applied to that
  occurrence.
- The earlier term findings on the word.
- The prompts for the face and term kinds (`reading.observe_prompts`).

**What it records.** Findings through `observationrecord`:
- **face:** applied to every occurrence that shows it;
- **term:** meaning in context against the three sources, surface variants, related words; a node on the word, with
  no verse;
- **use:** where it applies;
- **silence:** an occurrence with no inner-being bearing, a homonym or a name (RG-16).

The other kinds belong to the verse read in context (D4) and are refused here (D4 in §5).

**Its gate (RC-07, restated):** every occurrence of the word has a node of this word read, or a reason or an open
item.

## 3. D2: the cluster read (`cluster.read`)

**What it is.** One cluster read as a characteristic, from its member words' D1 results (RO6).

**What it reads.**
- Every member word with its term and face findings from D1.
- The cluster's current subgroups and their members.
- The open items matched to the cluster.

**What it records.**
- **Subgroups,** into `cluster_subgroup` and `cluster_subgroup_strong`, to RC-01 to RC-04:
  - every member's glosses and surfaces read first;
  - grouped by shared meaning;
  - at most 10 real subgroups, FLAG excluded, each with a label naming its essence and its anchor verse chosen by
    reading;
  - each word in exactly one subgroup, or in FLAG with its reason.

  A changed subgroup keeps its old row, marked deleted with its reason.
- **Characteristic findings,** through `observationrecord`: statement, link and use findings about the
  characteristic, applied by nodes to the subgroup (`cluster_subgroup_code`) or to its words. Among them, the
  comparison of a subgroup's words (RC-06).
- **Open items.**

**Its gate:**
- every member word is placed, or flagged with its reason;
- every real subgroup has its label and its anchor verse;
- every member word has a passed word read, or a reason (RC-05: D1 before D2);
- every subgroup of two or more words has a comparison finding (RC-06).

## 4. How they are held and run

| Part | Proposal |
|---|---|
| The record of a word or cluster read | a row in `reading`, with a new column `kind` (scope, word, cluster) and `subject` (the lettered strong, or the cluster code). The node's `reading_id` then names its home for D1 and D2 as for a scope reading, and Account, the files, the anchoring escalation and the close gate are shared (D1 in §5). |
| States | open -> observed. A word or cluster read is done at `observed`; the close gate counts it as finished there. |
| Steps | `word.read` (the word JSON, built from the tables), `word.record`, `word.check`; `cluster.read`, `cluster.record`, `cluster.check`. The method rules stay on `word.read` and `cluster.read`, where the reading happens. |
| Scripts | `iba/app/ps/Word-Reading.ps1` and `iba/app/ps/Cluster-Reading.ps1` (B:41), dispatching through run.py; work packages `word-reading` and `cluster-reading` (D2 in §5) |
| Library | `iba/app/lib/levelreading.py`, reusing `reading.py`'s helpers and `observationrecord`; `observationrecord` accepts a node on a subgroup or cluster with no word, for D2 |
| Files | `reading.output_dir/<label>/`, as a scope reading |
| Rules | RC-01 to RC-07 made active; RC-07 restated ("has a node of the word read"); RC-05 restated (D1 before D2) |

---

## 5. Retiring the API steps

| What | Change |
|---|---|
| Steps `lexical.meaning`, `lexical.relational`, `cluster.subgroup`, `cluster.reading`, `cluster.answer` | inactive, with their grants |
| Work package `cluster-reading` | its three steps retired; the name taken by the new D2 package (D2) |
| Scripts VerseReading, RelationalReading, ClusterSubgroup, CharReading, CharAnswer (`.ps1`) | moved to `iba/app/ps/archive/`; cfg_utility inactive at the archive path; their rule-scope link retired; their worksheet tabs removed |
| Libraries `versereadinggenerate.py`, `subgroupgenerate.py`, `charreadinggenerate.py`, `charanswergenerate.py` | moved to `iba/app/lib/archive/`; cfg_utility inactive |
| Handler functions `lexical:meaning`, `lexical:relational`, `cluster:subgroup`, `cluster:reading`, `cluster:answer` | removed; the files keep the steps that stay |
| The 14 settings in §1 | inactive, each checked first that no kept code reads it |
| `recordingpass.py` | stays as a library (the reading uses its occurrence resolution and text check); its purpose restated, its API path left as history |
| What the API steps wrote | unchanged: the 6,527 live observations and the 13 subgroups (W-3; D5) |

---

## 6. Test, on a copy (B:97)

1. **Migration:** run from the pre-run snapshot and re-run (nothing written); validate clean.
2. **Retirement:**
   - the retired steps inactive;
   - their scripts and libraries archived;
   - the kept steps (`lexical.build`, `lexical.readiness`, `cluster.assign`, `cluster.validate`) still dispatch.
3. **A word read** on a word with few occurrences:
   - read, record, check;
   - the gate refuses while an occurrence has no node, and passes when each has a face finding or a reason;
   - a term finding is applied to the word with no verse;
   - a statement finding is refused.
4. **A cluster read** on a small cluster:
   - the gate refuses a word placed twice, more than 10 subgroups, a subgroup with no anchor, a FLAG with no reason,
     a member word with no word read and no reason;
   - it passes when all are right;
   - a changed subgroup keeps its old row, marked deleted with its reason.
5. **The close gate** counts a word or cluster read at `observed` as finished.
6. **The #2273 test plan** re-run: the scope reading unchanged.

The results go to `outputs/escalation/2275-test-results-v1-<date>.md`.

---

## 7. Decisions for the researcher

Each is a new decision (B:44). My recommendation is first.

| # | Question | Options | Decision |
|---|---|---|---|
| D1 | Where is a word or cluster read held? | (a) a row in `reading` with `kind` and `subject`, sharing nodes' home, Account and the close gate; (b) its own tables, with nodes' home extended to name them | |
| D2 | What are the work packages and scripts called? | (a) `word-reading` (Word-Reading.ps1) and `cluster-reading` (Cluster-Reading.ps1), the latter taking the retired package's name; (b) both as steps of Reading.ps1 | |
| D3 | Does D1 record faces across all the word's occurrences? | (a) yes, the ledger method: every occurrence gets its face, grouped where shared (RC-07); D4 then reads them into focus; (b) no: D1 records term findings only, and faces come in D4 per verse | |
| D4 | Which kinds may a word read record? | (a) face, term, use, silence; (b) any of the eight | |
| D5 | What happens to the 13 subgroups the API made (M49, M67, M83)? | (a) kept until that cluster is read, then restated by the read, the old rows marked deleted with the reason; (b) marked deleted now | |
| D6 | Does a word read need an anchoring escalation, as a scope reading does? | (a) yes: the task or issue it serves (a build, a cluster's reading plan), so the work stays tied to the register; (b) no: a word or cluster read stands alone, on its own schedule | |

Once approved, B3 is built and tested on a copy, and the results are recorded on #2275.
