# The debate pipeline — authoritative technical reference

**Date:** 2026-08-06 (revised same day, second pass, after researcher review). **Purpose:** a
complete, step-by-step account of the debate analytic pipeline as actually built and tested today
(BUILD.md §56-66) — every DB interaction, every rule and where it's read from, every control and
how it's evaluated. Everything below is checked directly against the live code and the live
`cfg_*` tables, not reconstructed from memory or from BUILD.md's prose.

**What changed in this revision, directly against the researcher's own review comments:**
disaster-recovery is now its own investigated section (§2.5); Step 1 states the HIB determination
mechanism explicitly and captures the six-type scheme; every step's "method rules" now quotes
`cfg_method_rule` verbatim instead of paraphrasing a doc; every step gets a quality-control
sub-section reading `cfg_quality_check`; DB writes are now column-level, not just table-level; Step
2 gets a full treatment of the HIB-continuity wording and the non-linear/iterative-reset problem,
honestly, as an open design question with a proposed mechanism, not a solved one. Steps 6/7 are
left as they were (per the researcher's own "I will review step 6 and 7 after Step 1-5 is complete
and at the right level of depth") — §2.4's report-provenance preference is recorded for when that
review happens, not acted on now.

---

## 1. Pipeline map

| # | Step (digest) | Work package | `cfg_step` | Handler | Scope | Status |
|---|---|---|---|---|---|---|
| 0 | Lexical complete | `verse-lexical` | `lexical.build` → `report.verse_lexical` | `handlers/lexical.py` | book | **active** |
| 0/1 gate | Lexical-completeness hard stop | *(inside `hib.set`)* | — | `operations.py:_check_lexical_complete` | verses in payload | **active** |
| 1 | HIB identification | `operations-ingest` | `hib.set` | `operations.py:hib_set` | book | **active** |
| 2 | Passage boundaries | `build-passages` | `passage.build` | `passage.py:build` | book | **active** |
| 3 | Phenomena register | `operations-ingest` | `phenomenon.set` | `operations.py:phenomenon_set` | passage (book+range) | **active** |
| 4-5 | Operations | `operations-ingest` | `operation.set` | `operations.py:operation_set` | passage (book+range) | **active** |
| 6 | DB-backed report | *(standalone tool, no `cfg_step`)* | — | `tools/build_debate_report.py` | passage (book+range) | **active, read-only** — under review, see closing note |
| 7 | Closing sections | `operations-ingest` | `closing.set` | `operations.py:closing_set` | passage (book+range) | **built, PENDING approval** (§5) — under review |
| — | Old prose scaffold | `chapter-generate` | `report.passage_debate` | `lib/passagedebatereport.py` | book+range | **active, unchanged** — still the only path for legacy (pre-hib-continuity) books/chapters |

`operations-ingest` is `chained=0` — each step is invoked on its own, own `run_id`; nothing
auto-runs the next one. `build-passages` and `verse-lexical` are `chained=1` but each currently has
only one live step, so chaining is a no-op today.

**New reference tables, this revision:** `cfg_method_rule` (24 rows — the method rules Steps 1-4
run on, now config-resident, see each step below) and `cfg_quality_check` (10 rows — draft
reasonability/existence checks, one already enforced, the rest awaiting review — see each step
below and §2.6).

---

## 2. Cross-cutting mechanisms (apply at every step below, explained once)

### 2.1 Write-grant enforcement — `_may(ctx, writer, table)`

Every DB write in `operations.py`/`passage.py` is preceded by `_may(ctx, "<step>", "<table>")`,
which raises `PermissionError` unless `table in ctx.cfg.may_write(writer)` — a live read of
`cfg_write_grant WHERE writer=? AND table_name=? AND inactive=0`. **No grant row = no write,
unconditionally**, regardless of what the payload says. This is why `closing.set` cannot write
anything right now (§5) even though the code and schema are both already built and tested.

### 2.2 The reconciliation gate — `_reconcile(current, incoming, removals)`

Shared by `hib.set`, `phenomenon.set`, `operation.set`, and all four `closing.set` lists. Built
2026-08-06 to replace the original "blind clean re-derivation" (soft-delete everything in scope,
reinsert everything in the payload) with genuine read-compare-adjudicate-correct.

**Algorithm, exact:**
1. Every current live DB row for the write's scope is loaded, keyed by a **natural key** specific
   to the table (see §3 per step) and reduced to a **content tuple**.
2. Every incoming payload item is keyed and reduced the same way.
3. For each incoming key: not in current → **new**. In current, content equal → **unchanged**
   (never touched — original `id`/`created_at` survive). In current, content different →
   **changed**, and it **must** carry a `reconciliation_note` or the whole call fails.
4. Every explicit `remove` entry must name a key that IS currently live, with a `reason`, or the
   call fails.
5. **Every current key not addressed by either incoming or remove is a hard stop** — named
   explicitly, not silently dropped.
6. Any problem in 3-5 → `ReconciliationError`, raised **before any row is written** — fail
   condition `unreconciled` (or `unresolved-reference` for a broken cross-reference, checked even
   earlier).
7. Only on success: `changed`+`removed` rows soft-deleted, `new`+`changed` rows inserted fresh.
   `unchanged` rows: nothing happens.

**A reconciliation report is written on every successful call** (§2.4).

### 2.3 Soft-delete convention

Every table in this pipeline uses `deleted INTEGER NOT NULL DEFAULT 0`; every write path uses
`UPDATE ... SET deleted=1`, never `DELETE`. Nothing physically removes a row; everything is
recoverable by resetting the flag.

### 2.4 Report writing — two different mechanisms, deliberately

- **`reportkit.oneoff_path(cfg, topic)`** — every reconciliation log and `build_debate_report.py`'s
  output. Reads `governance.oneoff_report_dir`/`_naming_pattern`/`_format` — same-day collisions
  get `-v2`, `-v3`. No `cfg_report`/`cfg_report_section` row needed.
- **`reportkit.render_scaffold` + `write_report`** — what `report.passage_debate` (the OLD
  hand-fill scaffold) uses; requires a `cfg_report`/`cfg_report_section` row per section. Governs
  `report.version_on_regenerate`. Not used by anything built for Steps 1-5.

### 2.5 Disaster recovery — investigated, not newly built (already existed)

**The question:** does the pipeline survive a Claude failure, power loss, or session breakdown
mid-write, without losing everything? Traced directly against `run.py`/`lib/db.py`/`lib/
dbsnapshot.py`/`lib/cfg.py` rather than assumed.

**(a) Every write is one atomic transaction, and this is already true today.**
`sqlite3.connect(db_path, timeout=30.0)` (`lib/cfg.py`) uses Python's default deferred-transaction
isolation — nothing commits until each handler's own single, final `ctx.db.conn.commit()`.
`hib_set`/`phenomenon_set`/`operation_set`/`closing_set`/`passage.build` each do every one of their
soft-deletes and inserts inside ONE uncommitted transaction, committed exactly once at the very
end. **A hard kill at any point before that commit discards the entire transaction automatically**
(SQLite's own rollback on next open) — the DB file is left EXACTLY as it was before the call
started. There is no partial-write state to clean up. Re-submitting the identical call afterward is
always safe.

**(b) A full DB file snapshot is taken automatically before every NEW run.**
`run.py:_ensure_run` calls `dbsnapshot.snapshot(f"{package}-{run_id}")` the moment a new `run_id`
is first seen — before any write. WAL-checkpointed first for consistency, retained per
`retention.snapshot_keep_count` (default 20, oldest pruned), skippable only via `IBA_NO_SNAPSHOT=1`
for tight loops. Built 2026-07-22 after a real incident (a `candidate.load` bug overwrote 1029
rows with no recovery path but a stale manual backup) — this already covers every step in this
pipeline; nothing new was needed.

**(c) A resumed run doesn't lose its escalation/audit trail.** `run` rows track `state`
(running/paused/failed/done), `resume_point`, `started_at`/`ended_at`. An in-process exception
(a bug, not a hard kill) is caught, written as a permanent `type:"crash"` escalation row with the
full traceback, `run.state` set to `failed`, then re-raised — visible in `Escalation.ps1 -Action
List`, never silently swallowed.

**(d) A real gap found and closed in this pass.** `lib/retention.py` already surfaced *chained*
work packages stuck mid-sequence (`stuck_chained`) as archival candidates for human review — but
had no equivalent for `chained=0` packages, which is exactly what `operations-ingest` is (every
writer in Steps 1, 3, 4-5, 7). Unlike a chained package, a stuck non-chained run is **unambiguous**:
`run.py:207` shows a non-chained run always reaches `done` the instant its one step resolves, so
"still running/paused with nothing pending" only happens on a genuine crash — simpler to flag, not
harder. Added `stuck_nonchained` to `retention.build()`/`write_report()` (new `cfg_report_section`
row proposed, pending, batched with §5). **What to do when you see one:** just re-submit the same
call — per (a), the DB genuinely holds no partial state.

**Net answer:** yes, the pipeline already survives a hard crash without data loss or corruption —
this was true before today's work (the snapshot/transaction machinery is app-wide, not specific to
the debate pipeline) and is unaffected by anything built for Steps 1-7. The one gap found
(visibility of a stuck non-chained run) is now closed.

> **Correction, same day, second pass (BUILD.md §67).** The claim above — "nothing commits until
> the handler's own single final commit()" — is true for a genuine hard kill, but was **false**
> for an in-process exception (a code bug, not a crash of the process itself): `run.py`'s own
> exception handler wrote its escalation/run-state record on the SAME connection the crashed
> handler was still mid-transaction on, then called `db.close()`, which commits unconditionally —
> so a code bug mid-write could, and once did (caught live while testing the Step 2 rebuild
> below), commit the crashed handler's own partial writes along with the crash record, landing
> genuinely inconsistent state (a `passage` row with zero of its expected `verse_passage` rows).
> **Fixed**: the exception handler now calls `db.conn.rollback()` before writing anything, so a
> code-bug crash now has the SAME safety property a hard kill always had — nothing partial ever
> lands. The corrected, now-actually-true claim: any crash, of either kind, commits nothing from
> the interrupted handler.

### 2.6 Quality control — `cfg_quality_check`, now LIVE, not just draft content

Table: `step`, `check_key`, `question`, `test_kind` (`existence` | `non_existence` |
`reasonableness` — the researcher's own three kinds), `required`, `enforced_by`. **Third pass,
2026-08-06 — all 10 checks now `required=1` and mechanically enforced**, not sitting as unwired
draft content. Two enforcement shapes, matching what's actually checkable:

- **`kind-enum-membership`** — fully automated (`_valid_hib_kinds`, §3 Step 1); no analyst input
  needed, the code checks the value itself against the live `hib_kind` enum.
- **The other 9** (`enforced_by IS NULL` — genuinely a judgement call, not SQL-checkable) — a new
  shared gate, `_check_quality_attestations`, added to `hib.set`/`phenomenon.set`/`operation.set`:
  every NEW or CHANGED item's payload must carry `quality_checks: {check_key: "<reasoning>"}`
  covering every required, not-already-automated check for that step, or the whole call fails
  (`quality-check-incomplete`) **before any row is written**. Not a semantic judge — no code can
  verify "is this really a human being" — but a hard requirement that the judgement was actually
  made and written down, every time, not silently skipped. `unchanged`/`removed` items need no
  fresh attestation (nothing new is being asserted about them). Attestations are recorded in the
  reconciliation report (§2.2/§2.4) alongside the reconciliation note, auditable after the fact.

**Verified live**, same discipline as every other gate this session: no attestation → refused,
naming every missing `check_key`; partial attestation (1 of 3) → refused, naming only what's still
missing; full attestation → succeeds, all three answers visible in the written reconciliation
report. `passage.build` needs no separate wiring — its existing required `feasibility_note` field
already *is* this step's quality check (`boundary-not-arbitrary`'s question was reworded to match
the redefined Step 2, see §3).

---

## 3. Step by step

### Step 0 — Lexical must be complete for the scope

**(a) Building the lexical itself** — separate work package `verse-lexical`: `lexical.build`
(mechanical, deterministic — span/Strong's/morph, no interpretation) → `report.verse_lexical`.
Invoked via `VerseLexical.ps1 -Book <book> -Range <range>`. Writes `verse_lexical` (593 live rows
for Dan 8, confirmed).

**(b) The hard gate** — `operations.py:_check_lexical_complete`, called at the top of `hib_set`:
- **DB read:** `SELECT DISTINCT verse_id FROM verse_lexical WHERE deleted=0 AND verse_id IN (...)`
  — scoped to exactly the verse ids the payload references.
- **Control:** any referenced verse with zero live `verse_lexical` rows → `fail("lexical-
  incomplete", ...)`, before any other check. A verse genuinely absent from `verse` is never a
  candidate here (`governance.verse_gap_by_design`, 2026-07-29 ruling).

### Step 1 — HIB identification (`hib.set`)

**HIB determination mechanism — stated explicitly, as asked.** This is **not** an API call and
**not** a pure-mechanical/lexical rule. It is an LLM reading pass (Claude, working from the
`verse_lexical` row-level data — morph/Strong's, not the printed English gloss) applying the method
rules below, exactly the same boundary this app draws everywhere else ("Claude Code mechanical,
Claude AI/researcher analytical" — `operations.py`'s own module docstring). `hib.set` mechanises
turning that reading pass's *already-decided* findings into validated DB rows; it does not itself
decide anything about who is or isn't a HIB. There is no automated NLP/NER step, no external API,
and no lexical heuristic that proposes HIB candidates — the candidate list is entirely the reading
pass's own output.

**Invocation:** `Operations-Ingest.ps1 -Step hib.set -Book <book> -PayloadPath <json>` — book-scoped
only.

**Payload:** `{"book", "hibs": [{"label","kind","verses","referent_options",
"reconciliation_note"}], "remove": [{"label","reason"}]}`.

**DB reads:** `verse` (existence, per referenced verse); `verse_lexical` (Step 0's gate); `hib` +
`verse_hib` + `hib_referent_option` for the book (the current state `_reconcile` compares against).

**Method rules — quoted verbatim from `cfg_method_rule WHERE step='hib.set'` (7 rows, live):**

| rule_key | rule_text | source_doc | enforced_by |
|---|---|---|---|
| `presumptive-candidate` | Every human mentioned — named or collective, major or minor, however briefly — is a presumptive candidate: anyone who acts, undergoes an act, thinks, speaks, refrains from acting, or is simply named as present. This holds even where the act looks purely outward, administrative, locational, or incidental — the inner-being content may be hidden behind the act, with only the act stated in the text. | WA-passage-read-guidance-v1.5 step 2 note f | — |
| `non-human-scope` | A non-human being is in scope only where its state/characteristics bear directly on a human in the same context — otherwise the verse is set aside entirely. | WA-passage-read-guidance-v1.5 step 2 notes b, d | — |
| `collective-stays-collective` | A tribe, nation, "youths", "gentiles" etc. is recorded as ONE HIB representing the collection — not decomposed into individuals; any later operation involving it is a movement to/from a collection, not an individual. | WA-passage-read-guidance-v1.5 step 2 note c | — |
| `referential-named-not-skipped` | Where a party is unnamed but implied by the verse or wider passage, name it as a referential HIB; never assert an inferred identity as settled fact. | WA-passage-read-guidance-v1.5 step 2 note e | — |
| `referent-crux-resolution` | Where a pronoun or unnamed party is genuinely ambiguous, enumerate every live reading, give textual grounds for each, adopt one explicitly, keep rejected alternatives on record. | debate-analytic-process-digest-20260805.md Step 1 (T4 folded in) | schema: `hib_referent_option` |
| `six-type-scheme` | Every HIB is typed along two axes: plurality (individual \| collection) × specificity (named \| unnamed \| implicit) = six types: `named_individual`, `unnamed_individual`, `named_collection`, `unnamed_collection`, `implicit_individual`, `implicit_collection`. | nahum-1-inner-being-training-20260803.md (researcher's own prior training pass) | `cfg_enum 'hib_kind'` + `operations.py:_valid_hib_kinds` |
| `db-compare-adjudicate` | Read the verses in scope; compare the fresh reading against what's already in the DB; validate the list against the DB; where the fresh reading differs, adjudicate and correct the DB — not blind re-derivation. | researcher direction, 2026-08-06 | `operations.py:_reconcile` |

**The six-type scheme — found, not invented.** Searched rather than assumed: your own prior
training pass (`nahum-1-inner-being-training-20260803.md`) already worked this out fully, typing
every human being in Nahum 1:1-15 as one of (a) individual by name, (b) unknown individual, (c)
named collection, (d) unknown collection, (e) implicit individual, (f) implicit collection — two
clean orthogonal axes. `hib.kind` had **no enum constraint at all** before today
(`cfg_column.expectation` was `NULL` — genuinely free text). Now: `cfg_enum 'hib_kind'` (6 values,
proposed, pending approval) + `operations.py:_valid_hib_kinds` reads it live and rejects any
`hib.kind` not in the set (`invalid-kind`) — **the check is already coded and will activate the
moment the enum rows are approved**; until then it's a documented skip, not a false pass.

**Not yet differentiated downstream — flagged, not built.** You noted operations/phenomena may
later need to differentiate by HIB type. Nothing today reads `hib.kind` anywhere except `hib.set`
itself (to store it) and the debate report (to display it) — `phenomenon.set`/`operation.set` treat
every HIB identically regardless of type. The type is captured and queryable now; behavioural
differentiation is real future work, not attempted here.

**Quality checks — `cfg_quality_check WHERE step='hib.set'` (4 rows, all `required=1`, all
enforced — see §2.6):**

| check_key | question | test_kind | enforced? |
|---|---|---|---|
| `kind-enum-membership` | Is `hib.kind` one of the six live `enum.hib_kind` values (not free text)? | existence | **yes**, automated (`_valid_hib_kinds`) |
| `is-genuinely-human` | Does this candidate actually refer to a human being as Step 1 defines it — not a non-human being described in human-like terms, and not a place, object, or abstraction personified only grammatically? | reasonableness | **yes**, attestation required (`quality_checks` in payload) |
| `not-already-excluded` | Has this exact referent already been recorded as out-of-scope for this book/passage, and is this entry silently reintroducing it without new textual grounds? | non_existence | **yes**, attestation required |
| `verse-actually-supports-it` | Does the cited verse's own lexical row-level data actually support this HIB being present, or is the entry drifting from what the verse itself states? | reasonableness | **yes**, attestation required |

**Controls, in order, each a hard stop:** `unknown-verse` → `lexical-incomplete` → `invalid-kind`
(new, §above) → `unreconciled` (natural key = `label`; content = `(kind, sorted(verses),
sorted(referent_options))`) → write-grant check.

**DB writes, column-level:**
- `hib`: `book`, `label`, `kind`, `first_verse_id` (the payload's first listed verse), `created_at`,
  `deleted`.
- `hib_referent_option` (per referent-crux option): `hib_id`, `reading_text`, `textual_grounds`,
  `adopted`, `ordinal`, `created_at`, `deleted`.
- `verse_hib` (one per HIB×verse): `verse_id`, `hib_id`, `created_at`, `deleted`.
- `changed`/`removed` HIBs: cascade soft-delete their own `hib_referent_option`/`verse_hib`
  children first.

**Outputs, incl. by-type (new this revision):** `ok` message with unchanged/new/changed/removed
counts **and a live by-type count** (`{"named_individual": 3, "implicit_collection": 1, ...}`); a
reconciliation report; a **dedicated `hib.set-by-type-{book}.md`** listing every live HIB under its
type heading, written every call, reflecting the book's full current state (not just this call's
own changes).

**Unlocks:** `verse_hib` rows are what Step 2 reads.

### Step 2 — Passage registration (`passage.build`) — redefined 2026-08-06, second pass

**Superseded in place, same day.** Everything below replaces the original HIB-continuity algorithm
(B4, 2026-08-05). Trigger: an exploratory HIB-distribution visualization across four chapters from
four different books (Dan 8, Jonah 1, Hos 1, Mic 1 — see the published Artifact) showed no natural
sub-chapter break in any of them — every HIB's phenomena related to another HIB's, on equal footing
with a single HIB's own movement across verses (ram fought by goat; Jonah's flight causing the
mariners' storm; Hosea's three child-namings sharing one underlying referent throughout). The
researcher's own read: *"the thinking around passages is more about the capacity of AI to read the
entire chapter and digest it, rather than a logical breakup of the chapter into passages into
separable stories."* Confirmed against the text, not just the chart shape.

**New rule.** A passage IS the debate's own input scope (`-Chapters`/`-Range`), registered
verbatim — never algorithmically sub-divided. Step 2's real job: read the whole scope in light of
the HIBs already identified (Step 1), synthesise a high-level story, and self-assess whether the
scope can be read as a whole without quality loss. If not, refuse outright — no passage row
written, message tells the operator to narrow the scope and resubmit.

**Invocation:** `Build-Passages.ps1 -Book <book> (-Chapters <r>|-Range <r>) -PayloadPath <json>`.

**Payload:** `{"book", "story_summary", "feasible", "feasibility_note", "reconciliation_note"}` —
the last only required when correcting an already-registered scope's content.

**DB reads:** `verse` (the exact scope, via `versespanmeaningreport.fetch_verses`); `verse_hib`
(does this scope have any identified HIB at all — Step 1 must have run first); `passagetrack.
find_tracked_passage` (an exact-scope match, if one already exists); every OTHER live `passage`
row (any rule) owning any verse in this scope, via `verse_passage` (the overlap check — see below).

**Method rules — `cfg_method_rule WHERE step='passage.build'` (5 rows):**

| rule_key | rule_text | source_doc | enforced_by |
|---|---|---|---|
| `input-scope-is-the-passage` | A passage is the debate's own input scope, registered verbatim — never sub-divided by algorithm. | researcher direction, 2026-08-06, following the HIB-distribution visualization | `passage.py:build` |
| `story-synthesis-required` | Step 2's real output is a high-level story synthesis for the scope, read in light of the identified HIBs — not a derived boundary. | researcher direction, 2026-08-06 | schema: `passage.story_summary` |
| `feasibility-self-assessment` | Before registering a passage, self-assess whether the scope can be read as a whole without quality loss; if not, the debate is skipped with a message to revise the input scope, not silently sub-divided. | researcher direction, 2026-08-06 | `passage.py:build` (`scope-too-complex` refusal) |
| `one-passage-per-verse` | A verse belongs to at most one live passage at a time. | app convention (DB-enforced: `verse_passage.verse_id` unique) | schema: `verse_passage` unique constraint + `passage.py:build`'s overlap check |
| `legacy-superseded-unconditionally` | A legacy (pre-redefinition) passage overlapping a newly-registered scope is superseded wholesale — "not reconciling the old with the new." | researcher direction, 2026-08-05/06 | `passage.py:build` |

**Correction, this revision:** the previous version of this table claimed the original 4
HIB-continuity rule rows were "now `active=0`, superseded not deleted" — checked directly against
the DB and that was never actually true; they were still sitting `active=1`, a real doc/DB
mismatch. Per the researcher's explicit authorization ("go ahead and cleanout the configs... hard
deleting stuff that was added at some point and then replaced") they're now genuinely gone —
`migration/cleanout_retired_passage_config.py` hard-deleted all 5 rows (the corresponding
`cfg_setting`/`cfg_enum` rows for the retired algorithm too), rather than leaving them soft-deleted
clutter. BUILD.md §68 has the full record.

**Quality checks — `cfg_quality_check WHERE step='passage.build'` (1 row, reworded and
`required=1`):** `boundary-not-arbitrary`'s old wording ("does this passage's boundary fall where
HIB continuity genuinely breaks") no longer made sense once the algorithm it referred to was
retired — reworded: *"Is the feasibility_note a genuine, specific reading judgement about THIS
scope... would a second, independent read plausibly reach the same feasible/infeasible call for
the same reasons?"* Enforced structurally, not via the `quality_checks` mechanism the other three
steps use — the payload's own required `feasibility_note` field already IS this check's answer;
there was never a second place for it to live.

**Controls, in order:**
1. `bad-payload` — missing `story_summary`/`feasible`/`feasibility_note`.
2. **`scope-too-complex`** — `feasible=false` refuses outright, before any DB read beyond the
   payload itself. Nothing is written. This IS the "debate skipped, revise the input scope"
   behaviour, verbatim.
3. `no-verses` / `no-hibs` — the scope resolves to zero live verses, or has no `verse_hib` data at
   all (Step 1 hasn't run for it yet).
4. **`scope-overlaps-existing`** — new this revision, and the fix for a real bug caught live
   (BUILD.md §67): any OTHER live passage (legacy or new-model) already owning a verse in this
   scope, with a DIFFERENT range than the one being registered, refuses the call outright, naming
   the conflicting ref(s). A legacy-row overlap is NOT refused — it's superseded wholesale (the
   whole legacy passage retired, not just the overlapping verses), same rule as an exact-match
   legacy row.
5. `unreconciled` — an exact-scope match already exists with different `story_summary`/
   `feasibility_note` and no `reconciliation_note` was given.

**DB writes, column-level:**
- New passage: `passage` (`book`, `anchor_verse_id`, `start_chapter`, `start_verse`,
  `end_chapter`, `end_verse`, `ref`, `verse_count`, `rule="input-scope"`,
  `source="passage-build"`, `needs_review=0`, `story_summary`, `feasibility_note`, `created_at`,
  `deleted`); `verse_passage` per verse in the scope (`passage_id`, `verse_id`, `is_anchor`,
  `created_at`, `deleted`) — **every** verse in the scope, not only HIB-bearing ones (a verse with
  no identified HIB still belongs to the passage; it just contributes nothing to Step 3's control
  total).
- Correcting an existing exact-scope passage: `UPDATE passage SET story_summary=?,
  feasibility_note=? WHERE id=?` — same row, `verse_passage` untouched.
- Overlapping legacy row(s): soft-deleted wholesale (`passage` + their `verse_passage`).

**Outputs:** `ok` naming the ref, verse count, distinct-HIB count, and `passage_id` (new); or
"unchanged"/"corrected in place" with the same `passage_id` (resubmission).

**Unlocks:** a tracked passage row (any exact scope match) is what Step 3 resolves against.

**Verified live, twice** (BUILD.md §67) — first attempt crashed on a real bug (verse overlap with
an existing legacy passage wasn't checked before writing), which in turn surfaced a second, more
serious bug in `run.py`'s own crash handler (§2.5's correction, above). Both fixed, then the full
sequence re-verified end-to-end against real Daniel data: infeasible refusal, feasible creation
overlapping and superseding the real legacy `Dan 8:1-27` row, unreconciled-refusal on an
unexplained content change, corrected-in-place with a note, no-op on resubmission — all confirmed,
then fully reverted (legacy row restored exactly from a pre-test backup).

**What this resolves from the previous revision's open questions (§6):** items 1 (gap-tolerance
parameter) and 2 (`passage.release` mechanism) are now moot — there's no algorithm left to tune a
gap-tolerance into, and no automatic multi-passage rebuild left to need an escape hatch from
(registering one scope no longer touches any OTHER passage except a genuinely overlapping one).
**What's newly open:** whether HIB-continuity-derived, sub-chapter passaging is *ever* the right
call for an unusually long or complex chapter (e.g. Dan 11's 45 verses) — the feasibility
self-assessment can refuse a scope as too complex, but the redefinition doesn't yet say what the
operator should do NEXT beyond "narrow the scope" (split into two `-Range` calls manually, most
likely) — not a gap in the mechanism, just not yet spelled out as guidance.

### Step 3 — Phenomena register (`phenomenon.set`)

**Invocation:** `Operations-Ingest.ps1 -Step phenomenon.set -Book <book> (-Chapters|-Range)
-PayloadPath <json>`.

**DB reads:** `_find_new_model_passage` (range-identity match, refuses a legacy-row match); `hib`
(label→id); `phenomenon` JOIN `verse` JOIN `hib` (current state); `verse_passage` + `verse_hib`
(the control total).

**Method rules — `cfg_method_rule WHERE step='phenomenon.set'` (7 rows, live — one real citation
error found and fixed this pass, not just re-asserted as correct):**

| rule_key | rule_text | source_doc | enforced_by |
|---|---|---|---|
| `phase-separation` | The phenomena register (Phase 1) must be completed for the WHOLE passage before any operation (Phase 2) is written for ANY verse in it — not interleaved verse-by-verse. Running Phase 2 immediately after Phase 1 verse-by-verse reopens the same drift, since operation-writing momentum can bleed back into how the next verse's phenomenon gets identified. | WA-passage-read-guidance-v1.5 Phase 1/Phase 2 structure + its own 2026-08-02 change-control note (the direct fix for the Amos 1-3 drift) | `phenomenon.set` (gate) + `operation.set` (refuses while NULL) |
| `multi-chapter-vigilance` | Where a debate document spans multiple chapters, validation (Phase 3) should pay particular attention to phenomena/justifications that read as though they are describing the passage's own literary architecture rather than a specific inner being's own state. | WA-passage-read-guidance-v1.5 step 6 note b | — (belongs to Phase 3/Step 7, not Step 3 itself) |
| `hidden-behind-act` | A phenomenon may be hidden behind a stated act or a refrained-from act, with only the act recorded in the text — naming what the act is taken to evidence is exactly this step's job. | WA-passage-read-guidance-v1.5 step 3 note e | — |
| `warrant-required` | For every phenomenon isolated, record the specific textual warrant that grounds it (the verb, clause, or stated silence) and whether it is stated or inferred — its own register entry, written before and independently of any operation. | WA-passage-read-guidance-v1.5 step 3b | schema: `phenomenon.textual_warrant`/`status` |
| `not-literary-pattern` | A genuine literary/structural/genre observation is not a phenomenon — log it once as an emergent question (Step 7) instead, never built into the phenomena register. | WA-interpretation-questions-v1.4 Part B.12; WA-passage-read-guidance-v1.5 step 6 note c | — |
| `control-total` | Every HIB crossed with every verse it appears in, in this passage, equals the exact number of phenomena-register entries (including explicit "silent" entries) Step 3 must produce before it can be considered done. | debate-analytic-process-digest-20260805.md Step 3; b3-b5-operations-schema-design-20260805.md | `phenomenon.set` (verse_hib pair-set vs. live phenomenon pair-set) |
| `silence-is-a-finding` | "No phenomenon found, silent" is a valid RESULT of running the phenomenon check on a human-bearing clause, not an omission — and not a valid substitute for running the check. | WA-interpretation-questions-v1.4 Part B.4; WA-passage-read-guidance-v1.5 step 2 note f | schema: `phenomenon.status='silent'` |

**The error, found by actually re-reading each source line by line, not by re-asserting the prior
check was fine:** the original `phase-separation` row cited a single source ("Phase 1 change-control
note") for a rule_text that actually blended content from TWO different locations — the phase-
separation principle genuinely IS from that note, but "multi-chapter batched passages need the most
vigilance" is from a completely different place, **Phase 3 / step 6 note b** (validation), copied in
from the digest's own paraphrase without checking where the digest itself got it from. Split into
two correctly-and-separately-cited rows above. This is very likely what "I can see you have it
wrong just by looking at which documents you are quoting" was pointing at — found this pass by
reading `WA-passage-read-guidance-v1.5` fresh, line by line, against each stored rule, not by
trusting the previous revision's own "re-verified, matches exactly" claim.

**Quality checks — `cfg_quality_check WHERE step='phenomenon.set'` (3 rows, all `required=1`,
enforced — `_check_quality_attestations` in `phenomenon_set`):**

| check_key | question | test_kind |
|---|---|---|
| `genuinely-inner-being` | Is this phenomenon actually a state, disposition, or characteristic of the HIB's inner life — not a purely outward/administrative fact restated without any interior content identified? | reasonableness |
| `not-a-literary-pattern` | Is this entry a genuine per-verse, per-HIB phenomenon — not a textual/structural pattern (recurring formula, book-wide thesis) smuggled in as if it were one? | non_existence |
| `warrant-is-specific` | Does `textual_warrant` name an actual verb/clause/stated silence in this verse, not a vague restatement of the description field? | existence |

**Controls, in order:** `no-passage`/`legacy-passage` → `unresolved-reference` → `unreconciled`
(natural key = `(verse_osis, hib_label, ordinal)`; content = `(description, textual_warrant,
status)`) → **the control total**: `vh_pairs` (every live `(verse_id, hib_id)` from `verse_hib` for
the passage's verses) vs. `live_pairs` (same shape from `unchanged ∪ new ∪ changed` phenomena,
`removed` excluded) → `missing` non-empty sets `phenomena_complete_at = NULL` (explicitly
re-opening a previously-set gate, the bug fixed this session — it used to only ever move forward);
`missing` empty sets it to the current UTC timestamp.

**DB writes, column-level:**
- `phenomenon` (per new/changed entry): `passage_id`, `verse_id`, `hib_id`, `description`,
  `textual_warrant`, `status`, `ordinal`, `created_at`, `deleted`.
- `passage.phenomena_complete_at`: written every call, one way or the other.

**Outputs:** `ok` with counts + gate status; reconciliation report.

**Unlocks:** `phenomena_complete_at IS NOT NULL` is what Step 4-5 requires.

### Step 4-5 — Operations (`operation.set`)

**Invocation:** `Operations-Ingest.ps1 -Step operation.set -Book <book> (-Chapters|-Range)
-PayloadPath <json>`.

**DB reads:** same passage resolution as Step 3, plus `phenomena_complete_at` itself; `hib`
(label→id); `phenomenon` (resolve `(verse, hib_label, ordinal)` → `phenomenon_id`); `operation`
JOIN `phenomenon` JOIN `verse` JOIN `hib` (current state); `operation_party` (children, part of the
content comparison).

**Method rules — `cfg_method_rule WHERE step='operation.set'` (6 rows, live):**

| rule_key | rule_text | source_doc | enforced_by |
|---|---|---|---|
| `operation-from-phenomenon-only` | An operation may only originate from an already-registered phenomenon — never identify a fresh phenomenon while writing one. If writing an operation reveals no genuine phenomenon underlies it, the Step 3 entry was mis-identified — go back and correct it; do not paper over the mismatch. | WA-interpretation-questions-v1.4 Part B.12 | schema: `operation.phenomenon_id NOT NULL` + `operation.set` |
| `four-parts` | Every operation has: process (a state/status, or a movement — come from / go to / impact on / emerge / go away / become evident); source; target; and an action-type label. Source and target may be singular, multiple, mixed, or non-existent. | WA-passage-read-guidance-v1.5 step 1 note a | schema: `operation` + `operation_party` |
| `source-vs-enablement` | Keep source of the interior state and source of enablement to act distinct — a non-human being may be the stated source of an outcome or an enablement without the text sourcing the actor's own disposition; extending sourcing from outcome to interior is an interpretive step to flag, never to assume. | WA-interpretation-questions-v1.4 Q4 / Part B.5 | schema: `operation_party.enablement_only` |
| `action-type-is-a-label` | The action-type is a short, natural, verb-based tag — a label for cross-passage/cross-book comparison, not a taxonomy; no controlled vocabulary is being built. | WA-interpretation-questions-v1.4 Q11 / Part B.10 | schema: `operation.action_type` (free text) |
| `divine-mirroring-anchored` | Record a human/divine operation comparison only where the text's own juxtaposition or wording anchors it — a merely plausible resemblance is logged as an emergent question, never asserted or theologically elaborated. | WA-interpretation-questions-v1.4 Q12 / Part B.11 | — |
| `decision-enum` | decision = retain \| set_aside \| retain_referential \| recorded_silence. | WA-interpretation-questions-v1.4 Part C section 3 | schema: `operation.decision` (free text, not yet `cfg_enum`-enforced — see follow-up below) |

**Quality checks — `cfg_quality_check WHERE step='operation.set'` (2 rows, all `required=1`,
enforced — `_check_quality_attestations` in `operation_set`):**

| check_key | question | test_kind |
|---|---|---|
| `phenomenon-actually-underlies-it` | Having written this operation, does a genuine phenomenon actually underlie it — or has writing it revealed the Step 3 entry needs correcting? | reasonableness |
| `source-target-not-invented` | Are the source/target parties actually named or clearly identifiable in the verse/passage, not invented to complete the operation's shape? | non_existence |

**Controls, in order:** `no-passage`/`legacy-passage` → **`phenomena-incomplete`** (hard refusal if
`phenomena_complete_at` is NULL, checked live, never assumed) → `unresolved-reference` →
`unreconciled` (natural key = `(verse_osis, hib_label, phenomenon_ordinal)`; content = `(process,
action_type, decision, observation_text, description_text, sorted(sources), sorted(targets))`).

**DB writes, column-level:**
- `operation` (per new/changed): `phenomenon_id`, `process`, `action_type`, `decision`,
  `observation_text`, `description_text`, `created_at`, `deleted`.
- `operation_party` (per source/target): `operation_id`, `role`, `kind`, `detail`,
  `enablement_only`, `ordinal`, `created_at`, `deleted`.

**Outputs:** `ok` with counts + party-record count; reconciliation report.

**Follow-up flagged, not built:** `operation.decision`/`operation.action_type` are free text today,
same as `hib.kind` was before this revision. `decision`'s four values are a genuinely closed set
(`WA-interpretation-questions-v1.4` Part C names exactly four) — a natural next `cfg_enum` +
write-time check, same shape as `hib_kind`, not done in this pass given the volume already covered
today. `action_type` is explicitly NOT meant to be a controlled vocabulary (Part B.10) so should
stay free text.

**Unlocks:** every live phenomenon having a live operation is what `closing.set` (Step 7) checks.

---

## 4. Live `cfg_*` snapshot

**`cfg_method_rule`:** 26 rows — `hib.set` (7), `passage.build` (5), `phenomenon.set` (7, one real
citation error found and split into two correctly-sourced rows this pass), `operation.set` (6).
All `active=1`. The original 5 HIB-continuity `passage.build` rows are hard-deleted, not soft —
`migration/cleanout_retired_passage_config.py`, researcher-authorized 2026-08-06.

**`cfg_quality_check`:** 10 rows, **all `required=1`, all mechanically enforced** — 1 fully
automated (`hib.set/kind-enum-membership`), 8 via the new `_check_quality_attestations` gate in
`hib.set`/`phenomenon.set`/`operation.set` (every new/changed item's payload must carry a
non-empty `quality_checks` note per required check or the call refuses), 1 (`passage.build`)
structurally satisfied by its existing required `feasibility_note` field.

**`cfg_step` — `operations-ingest`** (chained=0): `hib.set` (0), `phenomenon.set` (1),
`operation.set` (2), all active; `closing.set` — proposed, pending.

**`cfg_write_grant`:** `hib.set → hib/hib_referent_option/verse_hib`; `phenomenon.set →
phenomenon/passage`; `operation.set → operation/operation_party`; `passage.build →
passage/verse_passage`; `closing.set` — none yet, 5 proposed.

**`cfg_enum 'hib_kind'`:** 6 values (`named_individual`, `unnamed_individual`,
`named_collection`, `unnamed_collection`, `implicit_individual`, `implicit_collection`) —
proposed, pending; code (`_valid_hib_kinds`) already reads it live and will activate the check the
moment it's approved.

**`cfg_enum 'passage_rule'`:** hard-deleted entirely (both values) — nothing validates an
incoming `passage.rule` choice any more (it's a hardcoded literal, never analyst-supplied), so the
enum itself was clutter, not just its two stale values.

**`cfg_setting`** (relevant subset, live): `report.version_on_regenerate=true`,
`governance.oneoff_report_dir="iba/app/reports/"`,
`governance.oneoff_report_naming_pattern="{topic}-{YYYYMMDD}.{format}"`,
`governance.oneoff_report_format="md"`. The 4 retired `passage.*` algorithm settings
(`default_rule`/`cross_chapter`/`min_shared_hibs`/`review_over`) are hard-deleted, not listed —
`passage.quality_report_path`/`passage.debate_session_chapter_guideline` are still genuinely read
elsewhere and were NOT touched by the cleanup.

---

## 5. What's pending your approval, all `configmaint.propose`, none self-answered

**From the first round (§65):** 6 — `closing.set`'s `cfg_step` insert + 5 `cfg_write_grant` inserts.

**From the second round (§66):** 8 — 6 `cfg_enum` inserts (`hib_kind`'s six values), 1 `cfg_column`
update (`hib.kind`'s `expectation`, pointing at the new enum), 1 `cfg_report_section` insert
(`retention.report`'s new `stuck_nonchained` section).

**Total: 14.** (The Step 2 rebuild's own retirement batch — 4 settings + 2 enum values — is no
longer part of this list: researcher-authorized direct hard-delete superseded it, §4 above; the
6 corresponding `configmaint.propose` escalations were answered `reject` as redundant, not left
pending.) Approving §65's batch unlocks Step 7 (`closing.set`). §66's batch activates the
already-built, currently-skipped `invalid-kind` check in `hib.set`, and makes §2.5(d)'s stuck-run
visibility check show up in `retention.report`. Neither blocks Steps 0-5 — everything in §3 for
Steps 0-5 is fully live and was exercised for real against real Daniel data, repeatedly, today.

**`configmaint.validate` — back to exactly the 2 pre-existing baseline advisories, zero new
findings**, confirmed after the config cleanout (the 3 orphan-setting findings the previous
revision reported are gone, not just deferred — the rows themselves no longer exist). A separate,
real bug was found and fixed in the same investigation: `configmaint.validate` was raising a brand
new duplicate escalation every time it ran (including this session's own ~10 verification calls),
because its within-run dedup never caught re-runs under a fresh `run_id`. Fixed at the root
(`lib/escalation.py:open_duplicate`) — see BUILD.md §68.

---

## 6. Open design questions — not decided here, needing your confirmation before any further build

1. **`operation.decision`/`operation.action_type` enum-ification** — flagged as a natural
   follow-up (same shape as `hib_kind`), not built this pass.
2. **What an operator does when a scope is refused as `scope-too-complex`** — narrowing via
   `-Range` is the obvious move, but nothing yet says how to handle a chapter whose HIB-relational
   density genuinely doesn't fit any sub-range cleanly (Micah 1's kind of fragmentation, but too
   large to read whole) — not encountered yet, not designed for.
3. **Steps 6/7** — per your own instruction, held for review until Steps 1-5 are at the right
   depth. §2.4's report fact-provenance preference ("must be specific... distinguish 'facts' in
   memory from reading from DB") is recorded here for that review, not acted on now.

**Resolved this round, no longer open:** the previous revision's gap-tolerance-parameter and
`passage.release`-mechanism items (both patches to the retired HIB-continuity algorithm — moot, see
Step 2 in §3); `cfg_quality_check` enforcement wiring (all 10 checks now `required=1` and
mechanically enforced, §2.6/§3); the Step 3 citation error (found and fixed, §3).
