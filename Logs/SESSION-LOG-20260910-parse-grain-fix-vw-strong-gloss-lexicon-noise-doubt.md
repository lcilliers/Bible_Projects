# Session log — 2026-09-10 — parse-grain fix, vw_strong_gloss, lexicon-join noise doubt, Window 1/2 open question

**Scope:** Reviewed escalations #1596-#1613 for approval/follow-up. Corrected a wrong first attempt
at "resolved meaning of a verse's strongs" (used dead/faulty lexical machinery); rebuilt it clean
via a new `vw_strong_gloss` view per the researcher's own specified join (verse ⋈ span ⋈ parse
construct). Investigated a 3,454-long-gloss data-quality concern, found and fixed a real
parse-vs-strong grain mismatch (escalation #1655, corpus-wide), and separately diagnosed (but could
not safely fix) an LSJ multi-sense concatenation bug. Confirmed no "elaborate engine" exists beyond
what's already in `lib/lexiconparse.py`. The researcher then used `vw_strong_gloss` directly, found
it produces overwhelming per-occurrence noise, and — after digging into the mechanism — concluded
the entire lexicon-enrichment approach has no place in bulk characteristic analysis (escalation
#1660, closed with the researcher's own verbatim ruling). That in turn opened a larger, still-open
question: whether Window 1 Layer 1/Layer 2 (`verse_lexical`/`verse_lexical_note`) add real value
over cluster-driven Window 2 reading — surfaced, not decided, not escalated yet; researcher is
digging further.

## Escalations touched

- **#1596/#1606/#1607/#1613** (review pass, all pre-existing) — reviewed per researcher request;
  most follow-ups already completed. #1613 closed out this session (see below). #1596/#1606/#1607
  remain genuinely open, left for the researcher (gloss_consistent_in_verse design decisions,
  cluster-allocation classification work, D5-D10 not yet worked) — untouched beyond review.
- **#1654** — Register `vw_strong_gloss` view in `cfg_table`. Applied, then **crashed
  `Start-Iba.ps1`** the same turn: `build_data_tables()`/`Cfg.tables()` has no category filter and
  generates malformed `CREATE TABLE` DDL for a view with no `cfg_column` rows. Reverted (deleted
  the bad `cfg_table` row) same turn, app confirmed clean again. `completed` — reported as applied
  then reverted, not silently absorbed.
- **#1655** — Fix parse-vs-strong grain mismatch. Researcher ruling, verbatim: *"every strong code
  must agree with span... every parse must support the strong table code, if STEP does not return a
  result for the variant, then A NOTE MUST BE IN parse... and the lemma level can be used in parse
  as the derived value."* Root cause: `fix_strong_meaning_tree_collapse.py` (2026-07-26) had
  narrowed its own backfill to "genuine collapse" siblings only, leaving 522 exact-variant codes
  with no `strong_meaning_tree` row (only their base lemma had one) — verified 519/522 have real
  distinct STEP content, only 3 genuinely empty. Fixed: broadened backfill migration (519/522
  filled) + standing code fix in `handlers/lexicon.py` (`_derived_variant_rows` — any strong still
  gapped after rebuild gets its base lemma's senses copied in, tagged with an explicit derived-value
  note). Verified corpus-wide via `spine.check` (0 FATAL) and 100% strong-code coverage through
  `vw_strong_gloss`. `completed`.
- **#1656** — Register the grain-mismatch backfill migration in `cfg_utility`. `completed`.
- **#1657** — Register `handlers/lexicon.py` itself (pre-existing gap, found fixing #1655).
  `completed`.
- **#1658** — `cfg_table` has no safe way to register a view (the #1654 root cause, as a standing
  gap, not just an incident report). Raised, left open for the researcher — real gap, no fix
  attempted this session. `raised`.
- **#1659** — Register `create_vw_strong_gloss_v1_20260910.py` in `cfg_utility`. `re-assigned`,
  open, awaiting researcher approval.
- **#1660** — new this session. Researcher, live, looking at `strong ⋈ vw_strong_gloss ⋈ span ⋈
  verse` for G3004G: *"the parsing process does not make it any easier to digest meaning... causes
  a significant layer of noise... Feeding the meaning data into the lexicon actually does not help
  the analysis. that really leaves me with great doubt about how to approach the analysis of the
  characteristics."* Diagnosed live: G3004G has 1,314 span occurrences x 27 `vw_strong_gloss` rows
  (24 from LSJ classical-citation senses) = 35,478-row join for one word — the direct, predictable
  consequence of the view's deliberately unresolved design, never meant to be joined 1:1 against
  span. Raised as a two-option decision (wrong grain entirely vs. missing resolution layer), not
  prejudged. Researcher's own follow-up settled it outright: the parse layer is a per-code sense
  inventory, not a per-occurrence resolution — valuable only as a rare, targeted, doubt-driven
  manual lookup, never a bulk join; characteristic analysis proceeds by direct contextual
  verse-reading with no lexicon join. Closed with that ruling as the resolution (`completed`,
  effectively `closed`/`noted`).

## Files created or changed

- `iba/app/handlers/lexicon.py` — `_derived_variant_rows()` added; `rebuild_parsed_tables()`
  inserts derived rows for any strong still gapped after the normal rebuild; return dict/handler
  message updated (#1655). Registered in `cfg_utility` (#1657).
- `iba/app/migration/backfill_all_strong_meaning_tree_gaps_v1_20260910.py` — created, run live:
  519/522 `strong_meaning_tree` gaps filled via the existing `write_tree_rows` mechanism
  (broadened continuation of `fix_strong_meaning_tree_collapse.py`). Registered in `cfg_utility`
  (#1656).
- `iba/app/migration/create_vw_strong_gloss_v1_20260910.py` — created, run live (twice — once with
  short source aliases, once updated to full table names per researcher request: *"adjust the view
  to show the label for the source table is a column"*). Creates `vw_strong_gloss` (union of
  `strong_meaning_parsed`/`strong_lsj_parsed`/`strong_mounce_parsed` onto one `gloss` column,
  keyed by exact strong code). Deliberately not a resolution mechanism. Awaiting registration
  approval (#1659); the view itself is live either way.
- `iba/app/handlers/spine.py`, `iba/app/ps/Spine-Check.ps1` — built earlier this session (spine
  integrity check), used repeatedly today to verify #1655's fix corpus-wide (0 FATAL throughout).
- `iba/app/migration/fix_no_vocab_shells_v1_20260910.py`, `delete_strongs_not_in_verses_v1_20260910.py`
  — applied earlier this session, registered (#1648/#1649).
- `.claude/commands/start-project.md` — step 4A added earlier this session (runs `Spine-Check.ps1`
  at session start, surfaces FATAL findings first).
- `iba/app/GOVERNANCE.md` — §73 (spine ruling + `candidate_seed` retirement), §74 (409-desync fix +
  `spine.check` tool), §75 (parse-grain fix, #1655) appended, same unit of work as each change.
- `iba/docs/1596-resolved-meaning-spine-test-v1-20260910.md` — created, then **rewritten in place**
  after the researcher's correction (wrong first approach used `strong_sense.head`/`resolve_code()`
  — dead/faulty lexical machinery). Now: §0 self-critique, §1 corrected process via
  `vw_strong_gloss`, §2 honest 132-verse result (9.4% zero-gloss-on-exact-match finding).
- `iba/docs/1613-meaning-layer-config-inventory-v1-20260909.md` — read/referenced (not modified
  this session; carried the D2/D3-gating context reviewed at session start).
- `iba/app/lib/lexiconparse.py` — **edited then fully reverted.** Attempted fix for the 805-row
  LSJ multi-sense concatenation bug (every `<b>` span inside one block joined into a single gloss,
  found via the 3,454-long-gloss investigation). Mirrored `_MeaningSegmentParser`'s working
  "new `<b>` after existing gloss starts a new segment" pattern; dry-run tested against the full
  corpus (`lexiconparse.lsj_rows(cfg)`, read-only, before any DB write) and found it created 3,839
  garbage single-fragment rows (LSJ also bolds dialectal spelling variants and inflection endings,
  which the naive rule can't distinguish from genuine new senses — e.g. G1096's three dialect
  variants of "become"). Reverted cleanly; confirmed output byte-identical to pre-change (35,571
  rows, 805 long). **Never touched the live DB.** Status quo: 805 rows unchanged.
- `iba/app/tools/build_lsj_sense_extract.py` (read only, not modified) — confirmed it contains
  nothing beyond what's already ported into `lib/lexiconparse.py` (dedupe, sub-label composition);
  its own docstring already flags the exact same multi-bold-span gap as unfixed from the original
  2026-07-25 build. No hidden "elaborate engine" exists.
- Memory: `project_base_data_spine_verse_span_strong_parse.md` updated throughout; new
  `project_characteristic_analysis_lexicon_noise_doubt.md` created for #1660/the open Window 1/2
  question, indexed in `MEMORY.md`.

## Decisions made

**Researcher's own decisions:**
- The resolved-meaning join process: *"without going through any of the faulty code, configs and
  pointers... join verse, with span get all the strongs per verse from span, join with a parse
  construct... prepare a fixed view."* → `vw_strong_gloss` built exactly to this spec.
- `vw_strong_gloss.source` must show the literal source table name as a column, not a short alias.
- Parse-grain fix (#1655): every strong code must agree with span at variant grain; STEP misses
  must carry an explicit note and fall back to lemma-level as the derived value; fix the code and
  rerun the entire parse corpus-wide.
- **#1660 — lexicon-join noise is real and the parse layer should never be bulk-joined for
  characteristic analysis.** Verbatim: *"the analysis of characteristics does not need a lexical.
  it is just noise."* The parse/lexicon tables remain correctly built but are now a targeted,
  manual, on-demand reference only — never joined in bulk against span/verse. This extends the
  already-live pull-side principle (`spine-on-demand-pull-mechanism`) to the use side.

**Claude's own diagnostic work, not a design decision:**
- Explained G0003's "3 rows in the view" pattern (2 real LSJ blocks + 1 genuine "LSJ has no entry"
  disclaimer row, a pattern affecting 451 rows corpus-wide).
- Confirmed `strong_meaning_parsed` is dual-language (100% Greek, 99.97% Hebrew); LSJ/Mounce raw
  coverage is 99.95% joint with no project-side filtering — purely STEP's own bundled data.
- LSJ multi-sense fix: attempted, tested, found regressive, reverted — reported honestly rather
  than shipped.
- Confirmed (re: "are you using the elaborate engine") that no such engine exists beyond what's
  already in `lib/lexiconparse.py` — the exploratory precursor tool's own docstring already
  documents the same unfixed limitation.

## Open items carried into next session

- **The Window 1 / Window 2 question — genuinely open, researcher digging further, no escalation
  raised yet.** Researcher's own framing: *"maybe it is because the core value I wanted to reduce
  from meaning table into a parses value has not materialised... let me dig deeper."* Distinctions
  surfaced this session, not resolved:
  - Layer 1 (`lexical.build`/`verse_lexical`) — mechanical structural tagging, and the literal join
    spine the already-approved Window 2 cluster methodology (`737-window2-cluster-based-
    methodology-proposal-v1-20260905.md`) depends on (`cluster_strong → strong → verse_lexical →
    verse`). Not obviously noise like the lexicon layer, but individual precomputed columns need
    the same scrutiny — `gloss_consistent_in_verse` is already known-stale (#1596).
  - Layer 2 (`lexical.enrich`/`verse_lexical_note`) — genuinely judgement-bearing, closer to what
    the researcher just endorsed as valuable, but essentially unproven at scale (173 live notes
    against 544,572 live `verse_lexical` rows) and currently a hard prerequisite gate per cluster
    in the #737 Window 2 proposal — never yet tested against real cluster work.
  - A live, already-documented coupling bug (`GOVERNANCE.md` §72): `passage.build`'s `no-hibs` gate
    requires Window 2 `hib.set` data before confirming a Window-1-only passage proposal — the two
    windows are not cleanly separable today regardless of which is led with.
  - Not raised as a formal escalation — offered to file (likely a review of #737's Layer-2-as-
    prerequisite assumption) once the researcher has finished digging.
- **#1596** — `gloss_consistent_in_verse` stale/dead formula — two design decisions still open,
  assigned Researcher.
- **#1606** — 111 strongs with zero cluster allocation — classification work, assigned Researcher.
- **#1607** — D5-D10 still open (narrative_morph Greek signal, `updated_at` INSERT-scope,
  `passage_id` drop-or-repurpose, `evidence_text` enforce-vs-merge, `verb_argument`
  trigger+T7-T14 wiring, H3477H disposition).
- **#1658** — `cfg_table` has no safe way to register a view — real standing gap, unresolved.
- **#1659** — register `create_vw_strong_gloss_v1_20260910.py` — awaiting approval.
- **LSJ 805-row multi-sense concatenation** — unresolved, status quo, no further attempt planned
  unless the researcher asks (and possibly moot depending on how the Window 1/2 question resolves —
  if the lexicon layer stays on-demand-only, this stops being corpus-wide noise and becomes a
  per-lookup cosmetic issue).

## Git state

Branch `main`, commit `4a7093d2` ("session 20260910: parse-grain fix (#1655), vw_strong_gloss,
lexicon-join noise doubt (#1660)"), parent `374b70bd`. `git push` succeeded: `374b70bd..4a7093d2
main -> main`. `git status` confirmed clean immediately after push. Working tree has this line's
own edit pending, filled in immediately after (same pattern as prior session logs' own "(cont.)"
commits).
