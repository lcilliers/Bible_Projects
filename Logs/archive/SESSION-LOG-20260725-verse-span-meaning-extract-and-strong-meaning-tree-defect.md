# Session log — 2026-07-25 — verse/span base-data extracts for manual Daniel analysis; found `strong_meaning_tree` collapses sub-lettered Strong's codes to their base lemma (confined to this app, main study unaffected)

**Session closed 2026-07-25 — the next session starts fresh, with no memory of this conversation.**
This log is written as a cold-start entry point: read it first, then follow its pointers.

---

## What this session did, start to finish

Opened with `Start-Iba.ps1`, a full read of `BUILD.md`/`GOVERNANCE.md`, and a re-run of
`SchemaOverview-Report.ps1` (the researcher's own standard routine) to ground the session in the
live schema before any design discussion. Confirmed live: 17 data tables; the whole candidate system
(`candidate_seed`/`span_candidate`) is retracted per the prior session's own closeout (§15D,
`GOVERNANCE.md`) and stays that way — nothing in this session revisits it.

### 1. Direction-setting: no replacement for candidate/passage; verse-first, book-driven reading

The researcher stated the next phase plainly: **nothing replaces `candidate_seed`/`span_candidate`.**
The prior method's flaw was fanning out from a *pre-assigned* characteristic; passage itself must now
be a **discovery output**, not a mechanical pre-stamp. Working design, as stated: analysis proceeds
**by book**, verses read **in true sequence** (verse-table order, but the researcher's framing — not
yet implemented as a build), each verse presented to the AI with its spans and each span's meaning
(Hebrew: sense/tree; Greek: sense/tree + Mounce), asking for (a) every inner-being **movement** in the
verse (term flagged by the researcher as still needing a definition) and (b) a one-paragraph
narrative. An existing, never-actioned design doc covering close territory —
`iba/docs/lexical-phase-plan-v1-20260719.md` ("DESIGN FOR CONFIRMATION", passage- not verse-unit,
predates the candidate retraction) — was surfaced but not adopted; the researcher's verse-first
framing supersedes it for now.

**The researcher's own decision on how to proceed:** work out the "movement" definition **manually**,
alone, against one book, before any of this becomes config or code — "that would clear my mind, and
set a standard." AI's role for now is narrow: prepare base-data material, nothing more.

### 2. What the old (main-study) project already has for Daniel

Before building anything, checked whether Daniel had already been worked — it had. Two artifacts,
2026-07-04, in the **main Bible-study project** (`verse-analysis/daniel/`, not IBA):
- `phase1-views/wa-dan{1-12}-phase1-lexical-view-20260704.md` — per-span mechanical decomposition
  (sense/type/bearer/operation/role tags), explicitly marked **DRAFT / sanity-check** in its own
  header — the old grid/role method the main study's 2026-06-25 "Characteristics → Movements" reset
  later closed as legacy.
- `readings/wa-daniel{1-12}-oracle-synthesis-20260704.md` — scene-level inner-being narrative
  reading, verse-cited, STATED/INFERRED-marked, threaded across chapters. This is the real "we did
  complete Daniel" the researcher remembered.
Separately, in `bible_research.db`: 100 registry words / 322 distinct Strong's terms have verse hits
landing in Daniel (`wa_verse_records`), incidental coverage from other words' studies, not a
deliberate whole-book pass.

### 3. Base-data extracts built for the researcher's manual work

Two new, reusable, read-only tools, both under `iba/app/tools/`, both parameterized (book/chapter/
verse range), both writing via `lib.reportkit.oneoff_path` (`iba/app/reports/`, governance-driven
naming, same-day collision gets `-v2` etc.):

- **`build_verse_span_meaning_extract.py`** — first attempt: verse text + spans + an interpreted
  "meaning" column (merged `strong_sense.head` + `strong_meaning_tree.sense_text` + Mounce for
  Greek). Produced `dan-1-3-verse-span-meaning-20260724.md`. Coverage caveat surfaced up front: only
  ~21-27% of non-particle spans in Dan 1-3 have any meaning row at all (only 178 words have been
  onboarded into this app so far).
- The researcher rejected the interpreted/merged approach outright: **"I asked for the full table
  record for each section by each verse."** Built **`build_verse_span_strongtree_extract.py`** —
  strictly literal, three raw blocks per verse, no merging, no decoding: (a) the verse row, (b) every
  span row (position order), (c) `strong_meaning_tree` rows for each distinct `strong_variant` in (b).
  Produced `dan-1-1-7-verse-span-strongtree-20260725.md`.

### 4. Two real bugs found and fixed in the literal extract, both from the researcher's own scrutiny

1. **Rendering fidelity** — the first version used Python's `repr()` to render field values, which
   escapes/quotes content rather than showing it verbatim ("the preview is not what is in the verse
   table"). Fixed: raw values only, no `repr()`.
2. **The real one — `strong_meaning_tree` key mismatch.** The researcher's report showed
   `sense_code`/`sense_text` as blank for spans like `H6696A` ("besieged") despite a `strong` row
   existing. Traced, not guessed: `strong_meaning_tree.lemma_key` is **always** the base code with any
   sub-letter suffix stripped (`BUILD.md` D3: "the tree is written once per lemma"). Checked DB-wide,
   not just Daniel: **3,498 distinct sub-lettered `strong_variant` values appear in `span`; zero of
   them ever get an exact `lemma_key` match.** A base-lemma fallback was added and initially presented
   as a fix — then checked properly and found **semantically unsafe in general**: 173 base codes have
   sub-lettered siblings with genuinely different meanings sharing one base number (`H2617A`
   "kindness" vs `H2617B` "shame"; `H1984A` "to shine" vs `H1984C` "to be foolish"; the `H5674`
   family spans "to pass"/"be angry"/"be arrogant"). The fallback was kept in the script (labeled,
   not silent) but is **not validated as correct** — it is a same-base guess, not a verified match.

### 5. Scoping the damage — checked, not assumed, whether the main 7-month study has the same flaw

The researcher's reaction was sharp: this looked like meaning had never been correctly matched back
to the verse's actual variant, "since the start of the study... 7 months." Rather than argue the
framing, checked the main study's own meaning-linking chain directly for the exact same test case:
`wa_term_inventory.strongs_number` (exact, sub-letter included) → `parsed_meaning_id` →
`wa_meaning_parsed` → `wa_meaning_sense.sense_text`.

**Result: the main study does NOT have this defect.** `H2617A` → "goodness, kindness, faithfulness";
`H2617B` → "a reproach, shame" — correctly separated, distinct `parsed_meaning_id` values per exact
sub-lettered code (2,109 of 2,155 sub-lettered `wa_term_inventory` rows carry their own
`parsed_meaning_id`, not shared with siblings). **The defect is confined to `strong_meaning_tree`, a
table this IBA app built in the last ~8 days (2026-07-17-on), on a design assumption (D3) that turned
out to be wrong** — it is not something that has been silently running under the main study's own
word-sense linkage. This was reported to the researcher plainly, correcting the scope of the concern
with evidence rather than either agreeing or minimizing.

### 6. Where the researcher landed

Session closed on the researcher's own reflection: AI lacks persistent, comprehensive, self-checking
memory/judgment across a project this long-running, so the load of remembering and verifying what's
actually correct falls on the researcher — "I need to work out what we have, is it correct, and use
the building blocks correctly." Declined an offered building-blocks inventory for now; asked instead
to close this session with a log and clear context to start fresh.

---

## Artifacts this session

- `iba/app/tools/build_verse_span_meaning_extract.py` (new)
- `iba/app/tools/build_verse_span_strongtree_extract.py` (new, the literal extractor — has the
  base-lemma fallback, clearly labeled as unverified when it fires)
- `iba/app/reports/dan-1-3-verse-span-meaning-20260724.md` (new — interpreted/merged approach,
  superseded in method by §3-4 above but left as-is, not deleted)
- `iba/app/reports/dan-1-1-7-verse-span-strongtree-20260725.md` and `-v2.md` (new — v1 has the
  `repr()` rendering bug, v2 is corrected; both kept per the project's own versioning rule, nothing
  overwritten in place)
- `iba/app/reports/schema-overview.md` (regenerated this session; prior version auto-archived to
  `iba/app/reports/archive/schema-overview-20260724-113250.md`)

## Where to start a fresh session

1. **`strong_meaning_tree` needs a real fix, not a script-level workaround.** Two live options, not
   yet decided: (a) check whether STEP's own `getInfo` call returns different content per exact
   sub-lettered code (untested this session — if yes, the raw-layer build should fetch and store per
   exact code, not collapse to base); (b) port the main study's already-correct
   `wa_term_inventory`→`parsed_meaning_id`→`wa_meaning_parsed`/`wa_meaning_sense` linkage pattern into
   this app instead of `strong_meaning_tree`'s current design. Until this is resolved, any report
   built on `strong_meaning_tree` for a sub-lettered code should be treated as unverified where the
   base-lemma fallback fires.
2. **The "movement" definition is still open**, deliberately — the researcher is working Daniel
   manually, independent of AI, using `dan-1-1-7-verse-span-strongtree-20260725-v2.md` (and can
   request further verse ranges via the same tool) plus the old project's
   `verse-analysis/daniel/readings/` (oracle-synthesis) as reference/comparison material. Do not
   pre-empt this by proposing a movement definition next session unless asked.
3. **A building-blocks correctness inventory was offered and declined this session** — the researcher
   may ask for it next time (IBA raw-layer tables: `verse`/`span`/`strong`/`strong_sense`/
   `strong_lexicon`/`strong_meaning_tree`, verified-correct vs. defective vs. not-yet-checked, each
   with evidence, no unverified claims).
4. `git status` after this log — this session's own files only (tools, reports, this log) should be
   staged and committed per `governance.session_log_triggers_commit`; several unrelated pre-existing
   untracked items from prior sessions (a session-log folder move, an "AI failures" research thread
   under `outputs/markdown/`) are not this session's work and should be left untouched.
