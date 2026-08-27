# A single consolidated `Sessions/` folder — v2: processing/results split, results side drafted

Prepared for escalation #933. Supersedes v1's single undifferentiated tree per the researcher's
correction: *"keeping project processing (escalations, methodology, instructions, processing
investigations, table management, prose.programme, prose.detail design, patches, config etc etc
etc) separate from research results/findings (word, verses, clusters etc) I think is key. This
split should not be mixed. Focussing first on the results/findings."* Still a design only — nothing
moved. `#929` v2's census stays the untouched reference.

## 1. The governing split

Two trees, never mixed:

- **Processing** — how the work gets done: escalations, methodology, instructions, investigations
  into the process itself, database/table management, `prose.programme` (governance/method prose —
  Chapters 4–6 of this very document set), `prose.detail design` (the per-word technical output of
  the old Session A–D pipeline — readiness data, DB status logs, analysis-stage prose), patches,
  config. **Named but not designed here** — out of scope for this round.
- **Results / findings** — the actual research content: cluster, book, word, verse, passage,
  `prose.findings`, `prose.essay`, `prose.concordance`, and raw data (lexicals, STEP extracts).
  **This round's focus.**

The four `prose.*` labels are not something I invented for this document — they are the live
`prose_section_type.book_label` values already in `bible_research.db`: `Programme` (51 active
rows), `Detail design` (169), `Findings` (**583** — the largest, and the one this split puts on the
results side), `Essays` (9), and `Concordance` (declared in `cfg_prose.book_stage_map` but not yet
built, 0 rows). A `Programme`/`Detail design` row is process output by this same logic; a
`Findings`/`Essays`/`Concordance` row is a result. 137 active rows currently carry no `book_label`
at all — an existing classification gap, not something this consolidation can silently resolve.

## 2. Results / findings — proposed shape

```
Sessions/results/
├── by-cluster/{M-code}-{Name}/
├── by-book/{book}/
├── by-word/{word}/
├── verse/          (see §4 -- largely not a real file location today)
├── passage/        (see §4 -- ditto)
├── prose-findings/     (DB-resident, exportable per book -- see §4)
├── prose-essay/        (DB-resident, exportable per book)
├── prose-concordance/  (not yet built -- placeholder only)
└── raw-data/
    ├── step-extracts/
    └── lexicals/
```

## 3. What actually maps here, from the real corpus

**`by-cluster/`** — `Sessions-v2/{code}-{Name}/` (641 files) and `Sessions/Session_Clusters/{code}/`
(2,006 files) both land here. Same open question as v1: two generations of the same baseline, which
is current is not established by a file count alone.

**`by-book/`** — `verse-analysis/{book}/` (2,835) and `iba/app/verse-analysis/{book}/` (308, the
Title-Case tree) both land here, same "which generation" question as v1.

**`by-word/`** — this is where the processing/results split actually bites, and it is not a clean
move. `Sessions/Session_A/`, `_B/`, `_C/`, `_D/` are, per `cfg_prose.book_stage_map`, the *"Detail
design"* stage — **processing side**, not results, by the researcher's own framework — except each
of those folders also holds genuinely raw material (`Session_A/STEP Extracts/`) that belongs in
`raw-data/`, not in processing at all. `research/discovery/{NNN}_{word}_step_data_*` (637 files) is
raw STEP-pull data and belongs in `raw-data/` outright, not `by-word/`. Splitting `Session_A`–`_D`
this finely is real re-sorting work, not a folder rename — flagged, not attempted here.

**`raw-data/step-extracts/`** — `Sessions/Session_A/STEP Extracts/` and `research/discovery/`'s
`*_step_data_*.json/.md` pairs (637 files) are the clearest, least contested mapping in this whole
document: verbatim STEP pulls, no processing judgement embedded in them.

**`raw-data/lexicals/`** — no dedicated file-based lexical-dump location was found in the v2 census;
the programme's lexical data lives in `iba.db` (`strong_lexicon`, `strong_meaning_parsed`, etc.),
not as standing files. This sub-bucket would hold future exports, not an existing folder move.

**`prose-findings/`, `prose-essay/`, `prose-concordance/`** — none of these exist as populated file
locations today. The 583 `Findings` rows and 9 `Essays` rows are DB-resident `prose_section` rows;
`Prose.ps1 -Step Extract -Book Findings` (or `Essays`) can produce files from them, but nothing has
been extracted to a standing folder in the current corpus. Populating these three buckets is an
export/build task, not a file move — named here so the shape is visible, not implied to already
have content.

## 4. "Verse" and "passage," specifically

Neither is a real top-level file location anywhere in the corpus (confirmed again on this pass, not
just carried over from v1). Verse- and passage-grained content lives two ways: *inside* `by-book/`
folders (`readings/`, `phase1-views/` — passage/verse detail for one book at a time), and in
`iba.db`'s own tables (`verse_lexical`, `passage`, `verse_passage`) with no file export at all. If a
true cross-book verse or passage view is wanted — "show me everything touching Gen 6:5 or this
passage, regardless of which book folder it's filed under" — that's new indexing work building on
top of the consolidation, not something the existing files already provide.

## 5. Open questions carried over, unchanged

The same five from v1 remain, now sharpened by the processing/results split: `Sessions-v2` vs.
`Session_Clusters` (cluster generations), the two `verse-analysis` trees (book-key format
generations), `Session_A`–`_D`'s internal mix of processing prose and raw data needing to be
pulled apart rather than moved whole, whether `verse`/`passage` get built as real file exports at
all, and the 137 `book_label`-less prose rows that don't sort into either tree as things stand.
