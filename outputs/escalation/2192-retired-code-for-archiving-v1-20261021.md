# #2192: code serving no active function, listed for archiving

Session 3cea0e6c, Developer Mode, 2026-10-21. Researcher, verbatim: "Exclude code serving retired
functions from the sweep. List it for archiving under governance.redundancy_archiving, then continue
the sweep on active code only."

## Method

Run by `iba/app/tools/temp_2192_active_reach.py`, read-only. The modules checked are the 115 under
`iba/app/` (migrations, archive and `__init__` excluded). A module **serves an active function** if
an active entry point reaches it, directly or through imports. Imports inside functions count, and
so does the handler lookup in `run.py`. The entry points are:

- `run.py` and `init.py`;
- the handler module of every **active** `cfg_step` row;
- every `iba.app` module named by a PS script under `iba/app/ps/`, or by a hook or settings file
  under `.claude/`. This covers `python -m iba.app.x`, `from iba.app.x import y` and `iba/app/...py`
  paths;
- `iba.app` modules imported by an active `cfg_utility` file outside `iba/app/`.

**Result: 90 modules serve an active function and 22 do not.** The other 3 of the 115 are this
sweep's own temp scripts, which are archived when it ends.

**Correction to what I said earlier:** `lib/lexicalenrich.py` is still active (imported by
`iba/app/ps/VerseLexical.ps1`), and so is `lib/lexicalenrichgenerate.py` (imported by the active
char-reading stage, `lib/charreadinggenerate.py`). `tools/build_debate_report.py` is active too
(called by `iba/app/ps/Debate-Run.ps1`). I had called all three retired; they are not, and they
stay in the sweep.

## A. Retired: nothing calls them, no active registration (archive)

| file | what it was | registration |
|---|---|---|
| `iba/app/handlers/candidate.py` | candidate-characteristic steps; all 5 `cfg_step` rows are inactive | none |
| `iba/app/tools/word_strong_span_report.py` | prototype; replaced by `lib/wordregistryspanreport.py` | `cfg_utility` inactive=1 |
| `iba/app/tools/log_retention.py` | old entry for the retention report; `Log-Retention.ps1` now dispatches through run.py | none |
| `iba/app/tools/build_verse_span_meaning_extract.py` | one-off extract; replaced by `lib/versespanmeaningreport.py` | none |
| `iba/app/tools/build_verse_span_strongtree_extract.py` | one-off base-data dump | none |
| `iba/app/tools/build_span_heatmap_v1.py` | one-off span heat map | none |
| `iba/app/tools/build_lexicon_combined_extract.py` | exploratory extract, says itself "not wired into the app" | none |
| `iba/app/tools/build_lexicon_lookup_extract.py` | exploratory extract | none |
| `iba/app/tools/build_lsj_sense_extract.py` | exploratory extract (rules now in `lib/lexiconparse.py`) | none |
| `iba/app/tools/build_meaning_tree_extract.py` | exploratory extract (rules now in `lib/lexiconparse.py`) | none |
| `iba/app/tools/build_mounce_lexicon_extract.py` | exploratory extract (rules now in `lib/lexiconparse.py`) | none |
| `iba/app/tools/build_span_term_reconciliation.py` | exploratory extract | none |
| `iba/app/tools/build_strong_info_extract.py` | exploratory extract | none |
| `iba/app/tools/build_strong_related_extract.py` | exploratory extract | none |
| `iba/app/tools/lexicon_split_common.py` | helpers used only by the exploratory extracts above | none |
| `iba/app/tools/ib_relevance_classifier.py` | wordlist first pass, used only by the exploratory extracts above | none |
| `iba/app/tools/_check_ib_related_span_step_coverage.py` | read-only diagnostic, "not wired into the app" | none |
| `iba/app/tools/_check_missing_strongs_in_step.py` | read-only diagnostic | none |
| `iba/app/tools/_check_span_unmatched_lexicon_json.py` | read-only diagnostic | none |

## B. Nothing calls them, but they may be run by hand (your call before archiving)

| file | what it is | registration |
|---|---|---|
| `iba/app/lib/clusterfamilyscan.py` | cluster-reallocation candidate scan (#1598), run by hand for review batches | `cfg_utility` active |
| `iba/app/tools/_apply_verse_plaintext_column.py` | idempotent backfill of `verse.text`; its registration calls it the catch-up for future ingestion gaps | `cfg_utility` active |
| `iba/app/tools/purge_word.py` | removes a word's own records, for clearing test data (`handlers/purge.py` is the registered purge) | none |

## C. Retired steps inside active files (not listed per function)

Some active files also hold functions for inactive steps. `handlers/lexical.py` has 2 inactive
steps, `handlers/reports.py` 6 and `handlers/passage.py` 1. Their files serve active steps, so they
stay in the sweep; taking those functions out is a separate code change, not part of this list.

## What happens next

The archiving itself (`git mv` to `iba/app/tools/archive/` or `iba/app/handlers/archive/`, with
each `cfg_utility` row set inactive or added as inactive) is carried by its own escalation, raised
with this list. The sweep goes on over the 90 active modules only.
