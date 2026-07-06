---
name: feedback_verse_raw_data_must_pull_all_study_evidence
description: a verse's RAW data = ALL evidence the study already holds, retrieved not re-derived; assembling it is the task, not confirming a prior verse's point
metadata:
  type: feedback
---

When fanning out to a verse, the RAW data extract must pull **everything the study already holds** about that verse and its terms — not surface text + morphology only. Shortcutting the raw data (so as to "confirm a point raised by a previous verse") is a failure: it is **not geared to the task**, which is to analyse a verse with **all the evidence the study has**.

**Why:** the study has years of digested material keyed to the verse's terms. For Lev 25:43, `yare` (fear) → **M01 Fear** (755 cluster findings; char M01-A "Reverential Fear" definition *already* names fear-of-God as a "restraining force on cruelty and injustice (Lev 19:14; 25:17; 25:43)"); `radah` (rule) → **M23** (not started — a real gap); `perek` (ruthlessness) → untracked. The verse also already carried 2 `verse_context` analysis-notes, 2 verse-read findings, and 23 `ve_lexical` values. I re-derived the fear-of-God-restraint reading cold — it was already in the DB.

**How to apply:** before reading any fanned-out verse, assemble its full raw extract — pull, per content term: the cluster (`mti_terms.cluster_code`), registry word, STEP/lexical meaning, corpus fan-out size; the verse's own `verse_context` (analysis_note, keywords, pole), `ve_lexical` values, `finding` rows; the cluster-level digested material (`cluster_finding`/`characteristic` for each term's cluster); the term fan-outs (related verses); and the **coverage gaps** (untracked terms, not-started clusters). Retrieve what is digested; do not re-derive it. **Reading comes after the raw data, built on it.** See [[project_verse_fanout_operating_model]], [[project_multi_contributor_spiderweb]], [[feedback_source_of_truth_is_written_record]].
