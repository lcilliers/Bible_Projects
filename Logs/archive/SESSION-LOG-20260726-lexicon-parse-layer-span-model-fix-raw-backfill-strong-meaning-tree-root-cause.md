# Session log — 2026-07-25/26 — lexicon-parsed layer baked into the core app, `span` combined-code model correction, progressive meaning-only backfill, and the `strong_meaning_tree` collapse bug traced to its exact root cause

**Session closed 2026-07-26 — the next session starts fresh, with no memory of this conversation.**
This log is a cold-start entry point: read it first, then follow its pointers. Directly continues
[`SESSION-LOG-20260725-verse-span-meaning-extract-and-strong-meaning-tree-defect.md`](SESSION-LOG-20260725-verse-span-meaning-extract-and-strong-meaning-tree-defect.md)
(prior session, same day) — its open item #1 is **resolved** below (root cause found, fix not yet
built — no tokens left this session).

---

## What this session did, start to finish

Opened with `Start-Iba.ps1`. Work fell into two distinct halves: (A) exploratory lexicon-parsing
fixes that were then, on explicit instruction, baked into the governed core app; (B) applying that
new capability to a real passage (Dan 1:1-7) and hitting a series of real defects, each investigated
and either fixed or root-caused.

### A. Lexicon extraction — bugs found and fixed, then baked into the app

1. **`strong_meaning_tree`/`strong_lexicon.lsj`/`strong_lexicon.mounce` parsing bugs**, found by
   checking back against STEP directly before trusting anything:
   - Comma/semicolon/colon were being treated as sense separators (`split_multi_gloss`) — wrong.
     E.g. G0019's `<b>goodness, virtue, beneficence,</b>` is ONE sense as STEP displays it, not
     three. Fixed: only a literal line break splits a gloss further (mounce has real `<br>`
     separators; meaning-tree/lsj currently have none, so they no longer explode at all).
   - `strong_meaning_tree` refs/notes were pooled across a WHOLE source row instead of scoped to the
     exact `<b>` span they followed — misattributed a later span's verse citation onto an earlier,
     unrelated gloss in the same row (G0019: `Gal.5.22` landing on "goodness" too). Fixed via a
     `SegmentParser` (one segment per `<b>` span).
   - All three ported into `iba/app/tools/build_*_extract.py` first (exploratory,
     `outputs/csv|json/`), verified, THEN ported again into `iba/app/lib/lexiconparse.py` — the
     app's own governed copy (the tools/ scripts stay standalone/independent, not imported from).
2. **`strong_related`** — STEP's `relatedNos` was fetched for the first time ever (not stored in
   `iba.db` at all before this session). `build_strong_related_extract.py` → `strong_related` table.
3. **`strong` table columns already existed but were never extracted** (`accentedUnicode`/
   `stepGloss`/`stepTransliteration`/`count`/`freqList`) — wired in via `build_strong_info_extract.py`.
4. **Combined JSON**, then **normalized into real tables** on explicit instruction ("bake this into
   the app... check governance... build in accordance with the rules"):
   - `migration/bootstrap_lexicon_parsed_layer.py` — 4 new tables (`strong_meaning_parsed`,
     `strong_lsj_parsed`, `strong_mounce_parsed`, `strong_related`), physically built FROM
     `cfg_column` (not hand-written DDL — `lib/db.py:build_data_tables`), full `cfg_table`/
     `cfg_column`/`cfg_write_grant` registration, new `lexicon` `config_module` enum value.
   - New standalone work package **`lexicon-parse`**, 3 steps: `lexicon.parse` (no network, full
     rebuild), `lexicon.related` (STEP fetch), `lexicon.validate` (coverage + value-quality,
     persists `iba/app/reports/lexicon-parse.md` every run, escalates only on findings — same shape
     as `candidate.validate`/`passage.validate`).
   - A **real pre-existing coherence bug found and fixed** while verifying: an earlier
     `span.strong_variant.fk` correction (see B1 below) had used `''` instead of `NULL` — the
     coherence checker treats any non-NULL `fk` as a declared reference to parse. Fixed via
     `configmaint.propose`.
   - `configmaint.validate` clean throughout (`ok`, 0 errors, 0 orphans) after every change.

### B. Applying it to Dan 1:1-7 — defects found in the field, most fixed live

1. **`span` model was itself wrong** (found via the researcher's own span-unmatched-lexicon-json
   review): the OLD `parse_spans()` exploded a `<span>` tag's multiple Strong's codes into one row
   PER CODE, even when STEP's own HTML combines them on one tag (`strong='G1722 G0054'` on
   "purity" — confirmed via a live STEP re-fetch, byte-identical to the stored `preview`, so the
   combination originates in STEP's data, not this app's parsing). That misattributed a co-tagged
   code's surface text onto the code with none of its own. **Corrected the declared model in
   config first** (`cfg_table.span`/`cfg_column.span.strong_variant`/`.is_particle`, all via
   approved `configmaint.propose` — the config was ALSO wrong, not just the code, since it said
   "ONE ROW PER CODE" and justified the bug), then `lib/stepapi.py:parse_spans()`, then
   `handlers/raw.py:validate()`'s parse-check (token-membership, not exact match), then a full
   `span` table rebuild (`migration/rebuild_span_combined_units.py`, from already-stored
   `verse.preview`, no re-fetch needed): 534,075 → 370,200 rows. Global parse-check re-verified
   clean afterward (found and left-flagged one SEPARATE pre-existing gap: 1,076 span tags across
   823 verses have no `morph=` attribute at all and are silently skipped by the regex — not caused
   by this fix, not fixed this session).
2. **`build_verse_span_meaning_extract.py`** (the researcher's own base-data report tool, built
   last session) needed updating THREE times the same day, each a real regression/defect this
   report had silently absorbed without being touched itself:
   - Switched from raw unparsed `strong_meaning_tree`/`strong_lexicon.mounce` to the new parsed
     tables.
   - Per-span meaning lookup made PER-CODE (the §B1 fix broke the old single-code-per-row
     assumption — would have silently shown "not yet registered" on 50% of Daniel's spans).
   - **Researcher's direct correction, the sharpest finding of the session**: "you are not working
     strictly with the strong variant... Meaning means considering the three parse files together,
     not pick the first one." Both true: `strong_meaning_parsed` was being presented as if specific
     to the exact span code when it's actually base-keyed (can genuinely be a DIFFERENT homonym's
     sense — see B4); and `stepGloss`/`meaning_tree`/`lsj`/`mounce` were a priority cascade instead
     of all shown together. Fixed: every applicable source now rendered on its own labeled line,
     `meaning_tree` explicitly flagged `[AMBIGUOUS - base shared with <siblings>]` whenever the
     base isn't unique to that code (22 of Dan 1:1-7's spans carry this flag).
   - Also extended with `--range C:V-V` (e.g. `1:1-7`) for a study passage narrower than a chapter.
3. **Progressive meaning-only backfill**, the researcher's own design choice among three offered
   (bulk-pull everything / live-fetch at render time / progressive per-passage, persisted — chose
   the third): `handlers/raw.py:backfill_meaning`, new standalone work package `raw-backfill`.
   Reuses `raw.detail_one()` completely unchanged (already meaning-only, already independent of
   `raw.verses` — the split asked for already existed). No new "meaning pulled" marker needed — a
   `strong` row existing with no matching `strong_verse` row already IS that signal. Later folded
   `lexicon.parse`/`lexicon.related` calls directly INTO `backfill_meaning` (found live: the first
   backfill run left 62 strongs with no `strong_related` fetch, caught by `lexicon.validate`, fixed
   by refactoring `handlers/lexicon.py` into reusable `rebuild_parsed_tables()`/`fetch_related_for()`
   and calling both from `backfill_meaning`). Verified on Dan 1:1-7: coverage **24% → 100%**; smoke
   -tested the fully-folded version on Dan 1:8, one command did the whole job.
4. **`strong_meaning_tree` collapse bug — root cause found and confirmed, NOT fixed (no budget
   left).** Continues last session's open item #1 directly. Researcher spotted `H3581B` ("competent",
   Dan 1:4) rendering the WRONG sense — checked live: `H3581A`="reptile", `H3581B`="strength", true
   homonyms (same `accentedUnicode`/transliteration, unrelated meanings), and `strong_meaning_parsed`
   for base `H3581` only ever held `H3581A`'s two "reptile" rows. **Confirmed the exact mechanism**:
   called `STEP getInfo("H3581B")` live — it correctly returns `H3581B`'s own `mediumDef` ("1)
   strength, power, might; 1a) human strength; 1b) strength (of angels)..." — matching exactly what
   the researcher sees in STEP's own UI word-click popup). So STEP returns the right data per exact
   code; **`handlers/raw.py:detail_one()` throws it away**: `if tree and not ctx.db.get(
   "strong_meaning_tree", lemma_key=lemma): ...write...` only writes a tree if the BASE has no row
   at all yet — since `H3581A` was onboarded earlier and already occupies `lemma_key="H3581"`,
   `H3581B`'s correct tree was silently discarded when the backfill pulled it today. This is last
   session's already-known "collapses sub-lettered codes" issue, but now with the precise cause
   identified (a write-time guard bug, not a fundamental STEP-data limitation) — answers last
   session's open question (a) definitively: yes, STEP DOES return distinct content per exact
   sub-lettered code; the raw-layer build just isn't storing it that way.
5. **Also fixed while chasing #4**: `raw.backfill_meaning`'s `related()` design was verified to
   correctly distinguish "genuinely fetched, zero related terms" from "never attempted" (a
   placeholder row with empty `related_strong`) — found this was ALSO wrong on the first pass
   (`lexicon.validate` flagged 362 false gaps), fixed before it went further.

---

## Where the researcher landed

Explicitly out of budget for the `strong_meaning_tree` schema fix this session. Reflected on the
recurring pattern — real defects keep surfacing on first genuine use of each data component, not
just this session — and questioned whether a database-as-lookup-layer is worth the ongoing
correction cost versus pulling directly from STEP per passage. Response given (not argued away,
but not agreed with wholesale either): every defect found this session was a specific, fixable
write/parse-path bug, not evidence the architecture can't faithfully reflect STEP — and today's own
`[AMBIGUOUS]` flag is already the practical mitigation (tells you exactly which spans need a live
STEP cross-check, rather than putting the whole database under suspicion). Asked to close with a
log and clear context rather than continue.

---

## Artifacts this session

**New core-app mechanism** (governed — cfg_table/cfg_column/cfg_step/cfg_work_package/cfg_write_grant/cfg_on_fail/cfg_report all registered, `configmaint.validate` clean):
- `iba/app/lib/lexiconparse.py`, `iba/app/handlers/lexicon.py`
- `iba/app/migration/bootstrap_lexicon_parsed_layer.py`, `bootstrap_raw_backfill.py`,
  `rebuild_span_combined_units.py`
- `iba/app/ps/Lexicon-Parse.ps1`, `Raw-Backfill.ps1`
- New tables: `strong_meaning_parsed`, `strong_lsj_parsed`, `strong_mounce_parsed`, `strong_related`
- New handler: `handlers/raw.py:backfill_meaning` (+ its on_fail rows)
- `handlers/raw.py:validate()`, `lib/stepapi.py:parse_spans()` — both corrected (§B1)
- `lib/cfgquality.py` — `lexicon.validate` registered in `QUALITY_CHECK_REPORT_PATH`/`REPORT_STEPS`

**Exploratory (unchanged in status — still `iba/app/tools/`, not wired into the app):**
- `build_meaning_tree_extract.py`, `build_lsj_sense_extract.py`, `build_mounce_lexicon_extract.py`,
  `lexicon_split_common.py` — all corrected this session (comma-splitting removed, segment-scoped
  refs/notes)
- `build_strong_info_extract.py`, `build_strong_related_extract.py`, `build_lexicon_combined_extract.py` (new)
- `_check_span_unmatched_lexicon_json.py` (new — the diagnostic that found the span-model bug)
- `build_verse_span_meaning_extract.py` — corrected three times this session (§B2)
- CSV/JSON outputs: `outputs/csv/*-iba-20260725.csv` (6 files), `outputs/json/lexicon-combined-iba-20260725.json`

**Reports:**
- `iba/app/reports/lexicon-parse.md` (new, governed, regenerates each `lexicon.validate` run)
- `iba/app/reports/dan-1-3-verse-span-meaning-20260725.md`,
  `dan-1-1-7-verse-span-meaning-20260725{,-v2,-v3}.md`, `dan-1-1-7-verse-span-meaning-20260726.md`
  (successive corrected versions, per-day/-version file-naming convention — nothing overwritten)

**Docs:** `BUILD.md` §16-19 (span model, lexicon-parse layer, backfill self-containment, meaning-
renderer correction) — all written same-session per `governance.build_md_on_code_change`.

## Where to start a fresh session

1. **`strong_meaning_tree` write-time bug — root cause confirmed, fix not built.** In
   `handlers/raw.py:detail_one()`, the guard `if tree and not ctx.db.get("strong_meaning_tree",
   lemma_key=lemma):` silently drops a sub-lettered variant's own tree whenever ANY sibling already
   populated that base. Fixing this properly needs a real schema decision — `strong_meaning_tree` is
   base-keyed by design; making it hold every sub-entry's own tree needs either a variant column
   added (migration on a core L2 raw table `strong_meaning_parsed` derives from) or an equivalent
   redesign. Do NOT re-run `raw.backfill_meaning`/`lexicon.parse` broadly assuming this is fixed —
   it isn't; the `[AMBIGUOUS]` flag in `build_verse_span_meaning_extract.py`'s output is the only
   current signal for which spans are affected. Likely affects most of the ~173 base lemma_keys
   known (from earlier sessions) to have multiple sub-lettered variants with distinct glosses.
2. **The Dan 1:1-7 report is usable NOW with that caveat** — every span not flagged `[AMBIGUOUS]`
   has held up against live STEP cross-checks this session; flagged ones need a manual STEP look
   until #1 is fixed.
3. **Progressive backfill is the established workflow going forward**: `Raw-Backfill.ps1 -Book
   <book> -Range <c:v-v>` now does the full job in one command (meaning pull + parsed-layer rebuild
   + related fetch for the new codes). Use this, not the older manual 3-step sequence, for any new
   passage.
4. **The "movement" definition is still open** (unchanged from last session) — researcher working
   this manually; do not pre-empt.
5. `git status` after this log — stage only this session's own files (see Artifacts above), not the
   several pre-existing untracked items from before this session (an "AI failures" research thread
   under `outputs/markdown/`, a session-log folder relocation) which are not this session's work.
