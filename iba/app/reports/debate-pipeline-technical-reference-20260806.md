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

**2026-08-07 addendum (third pass, researcher correction):** re-reading this document, the
researcher found that across its revisions it had lost its HIB-centric focus — the schema was
HIB-capable at every step but nothing written down said HIB was the actual *working order*. New
§2.7 states the cross-cutting principle explicitly (dominant-HIB selection; the three dimensions of
fanning out to other HIBs; which step each dimension belongs to; why phenomena must be genuinely
complete before operations can work). Steps 2/3/4-5 each get a short addition applying it. Mirrored
into `cfg_method_rule` the same session (`story-organized-by-hib` / `hib-first-traversal` /
`hib-fanout-dimensions`, one row per step) via the direct-write convention this table already uses
(`migration/add_hib_centric_traversal_method_rules_20260807.py` — not `configmaint.propose`-gated,
same lesson as escalation #539) — config first, this doc restates it, per
`governance.rules_must_be_config_driven`. `configmaint.validate` clean after.

**2026-08-07 addendum (fourth pass, full-app schema remediation, `BUILD.md` §79 / `GOVERNANCE.md`
§33).** Researcher's own live discovery: this pipeline's ten debate/closing tables had no real FK,
UNIQUE, or index of any kind despite `cfg_column`/`cfg_unique` already declaring the correct rules
— retrofitted, root cause + full record in `BUILD.md` §79. New §2.3a documents the schema fix. New
§2.2a documents a second, related fix found generalising it: `hib.set`/`phenomenon.set`/
`operation.set` each silently orphaned a downstream row on a `changed` correction (new id every
time) — now update the existing row in place, and a `removed` item is refused outright while a
live dependent exists. `operation_party` gained a real `hib_id` link (Finding 2 of the traceability
report) — §3 Step 4-5 and the `hib-can-be-party-in-another-hibs-operation` method rule (both this
doc's quote and the live `cfg_method_rule` row) corrected to match. Steps 1/3/4-5's own "Controls"
and "DB writes" sub-sections updated in place to reflect all of the above.

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
| 6 | Closing sections | `operations-ingest` | `closing.set` | `operations.py:closing_set` | passage (book+range) | **active** |
| 7 | Report | *(standalone tool, deliberately not a `cfg_step`)* | — | `tools/build_debate_report.py` | passage (book+range) | **active** — generated LAST, from the complete DB state, after Step 6 |
| — | Old prose scaffold | `chapter-generate` | `report.passage_debate` | `lib/passagedebatereport.py` | book+range | **RETIRED 2026-08-07** (`chapter-generate`/`passage-debate-report`/`passage-debate-sync`/`verse-analysis-report` work packages and their `report.passage_debate`/`passage.debate_sync` steps all `inactive=1`, confirmed live — BUILD.md §72). The 24 pre-existing scaffold-model debate files (Amos/Hosea/Joel/Jonah/Micah/Obadiah) remain on disk, unaffected, but this route no longer runs for anything, legacy books included. |

`operations-ingest` is `chained=0` — each step is invoked on its own, own `run_id`; nothing
auto-runs the next one. `build-passages` and `verse-lexical` are `chained=1` but each currently has
only one live step, so chaining is a no-op today.

**New reference tables, this revision:** `cfg_method_rule` (35 active rows as of 2026-08-07,
verified live — `hib.set` 7, `passage.build` 6, `phenomenon.set` 9, `operation.set` 8,
`closing.set` 5 — see each step below; the `passage.build`/`closing.set` gaps this document's own
counts once flagged are now backfilled, `migration/complete_method_config_20260807.py`) and
`cfg_quality_check` (11 rows — draft reasonability/existence checks, most already enforced — see each step
below and §2.6).

---

## 2. Cross-cutting mechanisms (apply at every step below, explained once)

### 2.1 Write-grant enforcement — `_may(ctx, writer, table)`

Every DB write in `operations.py`/`passage.py` is preceded by `_may(ctx, "<step>", "<table>")`,
which raises `PermissionError` unless `table in ctx.cfg.may_write(writer)` — a live read of
`cfg_write_grant WHERE writer=? AND table_name=? AND inactive=0`. **No grant row = no write,
unconditionally**, regardless of what the payload says. `closing.set`'s own 5 write-grants were
exactly this kind of gap for one day (2026-08-06 approved, applied) — confirmed live and unchanged
since; every step's grants are live now, §4a.

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
7. Only on success, **corrected 2026-08-07** (was: "changed+removed soft-deleted, new+changed
   inserted fresh" — that inserted a BRAND NEW id for every `changed` item, silently orphaning any
   already-written downstream row still pointing at the old one; see §2.2a): `new` items insert
   fresh; `changed` items **`UPDATE` the existing row in place** (same `id`) — only genuinely
   child-only rows with no downstream referent (`hib_referent_option`/`verse_hib`,
   `operation_party`) are still soft-deleted-and-reinserted under a `changed` parent, since nothing
   else references their own id; `removed` items are soft-deleted, but only after §2.2a's guard
   confirms nothing live still depends on them; `unchanged` rows: nothing happens.

**A reconciliation report is written on every successful call** (§2.4).

### 2.2a Cascade guards — every reconciling writer, not just one (added 2026-08-07)

`hib.set`, `phenomenon.set`, `operation.set` each write a table another live table can point at
(`hib`←`phenomenon`, `phenomenon`←`operation`, `operation`←`passage_linkage`). Two rules now apply
uniformly to all three (`BUILD.md` §79, `passage.py`'s own §67 fix generalised, never a `hib.set`-
only special case):

1. **A `changed` item preserves its row's id** (§2.2 step 7) — a correction can never silently
   orphan a downstream row just by existing.
2. **A `removed` item is checked for live dependents FIRST, refused outright if any exist** — new
   fail conditions `hib-has-dependent-phenomena` (`hib.set`), `phenomenon-has-dependent-operations`
   (`phenomenon.set`), `operation-has-dependent-linkage` (`operation.set`). The dependent must be
   cleared first (via that lower step's own `remove` list) or the removal withdrawn — never a
   silent orphan, same "fail clean before any row is touched" convention as every other check in
   this pipeline.

### 2.3 Soft-delete convention

Every table in this pipeline uses `deleted INTEGER NOT NULL DEFAULT 0`; every write path uses
`UPDATE ... SET deleted=1`, never `DELETE`. Nothing physically removes a row; everything is
recoverable by resetting the flag.

### 2.3a Schema — real FK/UNIQUE/index constraints, retrofitted 2026-08-07 (previously absent)

**Corrects this document's own earlier silence on the point** — none of the ten debate/closing
tables (`hib`, `hib_referent_option`, `verse_hib`, `phenomenon`, `operation`, `operation_party`,
`passage_linkage`, `passage_insufficiency`, `passage_emergent_question`, `passage_validation_note`)
had a real `FOREIGN KEY`, `UNIQUE`, or index of any kind before 2026-08-07, despite `cfg_column.fk`/
`cfg_unique` already declaring the correct relationships — a build-vs-config conformance bug, not a
design choice (root cause + full change record: `BUILD.md` §79). All ten now carry:

- **Real `FOREIGN KEY` constraints** matching `cfg_column.fk` exactly (`hib.first_verse_id →
  verse.id`, `phenomenon.{passage_id,verse_id,hib_id} → passage.id/verse.id/hib.id`,
  `operation.phenomenon_id → phenomenon.id`, `operation_party.{operation_id,hib_id} →
  operation.id/hib.id`, `passage_linkage.{from,to}_operation_id → operation.id`, etc.) — declarative
  and `PRAGMA foreign_key_check`-auditable, same as every other FK in the app; `PRAGMA foreign_keys`
  runtime enforcement stays OFF app-wide (unchanged, pre-existing convention), so real-time rejection
  of a bad reference still comes from each writer's own existence checks (`_verse_id`,
  `_find_phenomenon`, `hib_by_label`), not the constraint itself.
- **A partial unique index** (`... WHERE deleted=0`), not a plain table-level `UNIQUE`, on each
  table's natural key (`verse_hib(verse_id,hib_id)`, `phenomenon(passage_id,verse_id,hib_id,
  ordinal)`) — live-rows-only, so a table's own soft-deleted correction history never collides with
  itself (matches `passage`'s own pre-existing `idx_passage_range_live` pattern).
- **A composite `(fk_col, deleted)` index** for every FK column — config-driven via the new
  `cfg_index` table (`GOVERNANCE.md` §33), not a one-off. Before this, every JOIN in `operations.py`
  (e.g. `operation.set`'s `phenomenon ph JOIN verse v ON v.id=ph.verse_id JOIN hib h ON
  h.id=ph.hib_id`) ran as a full table scan on the child side.

**The one genuinely missing many-to-many link, also closed:** `operation_party.hib_id` (nullable,
→ `hib.id`) — an operation's source/target party, when it IS a previously-registered HIB, is now a
real structural link, not only the free-text `detail` gloss (§3 Step 4-5's payload contract gained
an optional `hib_label` per party). Checked live before the fix: only 3 of 42 distinct `detail`
values matched a `hib.label` even as *text*.

Full investigation + before/after evidence: `iba/app/reports/
debate-schema-traceability-gap-findings-20260807.md` and `-remediation-design-20260807.md`.

### 2.4 Report writing — two different mechanisms, deliberately

- **`reportkit.oneoff_path(cfg, topic)`** — every reconciliation log and `build_debate_report.py`'s
  output. Reads `governance.oneoff_report_dir`/`_naming_pattern`/`_format` — same-day collisions
  get `-v2`, `-v3`. No `cfg_report`/`cfg_report_section` row needed.
- **`reportkit.render_scaffold` + `write_report`** — what `report.passage_debate` (the OLD
  hand-fill scaffold, RETIRED 2026-08-07, §1/§72) used; requires a `cfg_report`/
  `cfg_report_section` row per section. Governs `report.version_on_regenerate`. Not used by
  anything built for Steps 1-7 — this mechanism has no live caller left in the debate pipeline.

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
harder. Added `stuck_nonchained` to `retention.build()`/`write_report()` (`cfg_report_section` row
approved and applied 2026-08-06, confirmed live — §5). **What to do when you see one:** just
re-submit the same call — per (a), the DB genuinely holds no partial state.

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
`reasonableness` — the researcher's own three kinds), `required`, `enforced_by`. **17 active rows
as of 2026-08-07, all `required=1` and mechanically enforced**, not sitting as unwired draft
content (grew from the original 10 as `closing.set` and the full-lexical-weight checks were added
— §75/§76). Two enforcement shapes, matching what's actually checkable:

- **`kind-enum-membership`** — fully automated (`_valid_hib_kinds`, §3 Step 1); no analyst input
  needed, the code checks the value itself against the live `hib_kind` enum.
- **The other 16** (`enforced_by IS NULL` — genuinely a judgement call, not SQL-checkable) — the
  shared gate, `_check_quality_attestations`, wired into `hib_set`/`phenomenon_set`/
  `operation_set`/`closing_set`: every NEW or CHANGED item's payload must carry `quality_checks:
  {check_key: "<reasoning>"}` covering every required, not-already-automated check for that step,
  or the whole call fails (`quality-check-incomplete`) **before any row is written**. `closing.set`
  is the one exception to "flat per-step list" — it has four heterogeneous item types under one
  step name, so its own required-check list is filtered per item type before this gate is called
  (§3 Step 6) rather than applied as one combined list. Not a semantic judge — no code can verify
  "is this really a human being" — but a hard requirement that the judgement was actually made and
  written down, every time, not silently skipped. `unchanged`/`removed` items need no fresh
  attestation (nothing new is being asserted about them). Attestations are recorded in the
  reconciliation report (§2.2/§2.4) alongside the reconciliation note, auditable after the fact.

**Verified live**, same discipline as every gate in this app: no attestation → refused, naming
every missing `check_key`; partial attestation → refused, naming only what's still missing; full
attestation → succeeds, every answer visible in the written reconciliation report. `passage.build`
needs no separate wiring — its existing required `feasibility_note` field already *is* this step's
quality check (`boundary-not-arbitrary`'s question was reworded to match the redefined Step 2, see
§3).

### 2.7 HIB-centric traversal — one principle, a different effect at every step (added 2026-08-07, researcher correction)

**The principle, stated plainly.** The HIB dominates the entire cycle, not just Step 1. Concretely:
HIB identified (Step 1) → the story is told **around** HIBs, not as a generic plot summary (Step
2) → phenomena are identified **by HIB**, across the whole passage, not verse-by-verse (Step 3) →
HIB + phenomenon is the **centre** the operation description is built around (Step 4-5). Found
missing 2026-08-07: the schema was already HIB-capable at every step (`phenomenon.hib_id` is a
real column; the control total is genuinely HIB×verse), but nothing written down said this was the
*working order* — every step's own natural key and DB-read description defaulted to verse-first
phrasing (`(verse_osis, hib_label, ...)`), and the first real attempt at Dan 1's phenomena register
defaulted to verse-by-verse traversal as a direct result. This section is the fix — restated below
in each step's own section, not just here.

**Selecting which HIB to start with.** The most *dominant* HIB — read as: cross-check Step 1's own
verse-count per HIB (a plain, checkable number, already in every `hib.set-by-type-{book}.md`
output) against Step 2's story synthesis for who the passage's own throughline actually follows.
Where they agree, start there (Daniel, Dan 1: 16 of 21 verses, and the story's own protagonist —
both signals agree). Where they diverge — a collective mentioned often but not narratively central,
or a pivotal HIB mentioned only a few times — the story's judgement about centrality wins over the
raw count, and the divergence itself is worth a line in the working notes, not silently resolved
either way.

**Fanning out to every other HIB in the passage — three distinct dimensions, not one.** Once the
dominant HIB's own read is complete, the *other* HIBs in the passage relate to it (and to each
other) in three genuinely different ways:

- **(A) Party-within-operation.** While the focused HIB's own operation is being built (source /
  target / process / action-type, the four-parts rule), another HIB may BE that operation's source
  or target — e.g. Ashpenaz is a party within Daniel's own operation wherever Daniel addresses or
  is addressed by him.
- **(B) The mirror, once focus switches.** When that OTHER HIB later becomes the one in focus, the
  PREVIOUSLY-focused HIB may now appear as source or target of *its* operations — e.g. once Ashpenaz
  is in focus, Daniel becomes the target of Ashpenaz's own favor/compassion operation (Dan 1:9).
  This is a consistency/completeness check across two HIBs' own operation records, not fresh
  information — the same real-world relationship, seen from the other side.
- **(C) Movement/process BETWEEN separate HIBs' phenomena.** Not "who is the party within this one
  operation," but how one HIB's already-registered phenomenon/operation connects to — leads to,
  answers, is caused by — a DIFFERENT HIB's own, elsewhere in the passage (Ashpenaz's fear at v10
  leading to the test Daniel proposes at v12-13, leading to Melzar's compliance at v14). This is a
  passage-level linkage between two already-registered items, not a property of either one alone.

**These three dimensions do NOT all belong to the same step — confusing them is exactly the
phase-separation violation, now with a precise diagnostic.** `phenomenon` has no source/target
columns at all — a phenomenon is only ever `(description, textual_warrant, status)` for ONE HIB in
ONE verse. So:

- **(A) and (B) belong to Step 4-5 (`operation.set`) only.** Source and target are literally
  `operation`/`operation_party` schema. If, while doing Step 3's phenomena read, the question "who
  caused this" or "who does this affect" starts to feel necessary to answer — that question belongs
  to the operation this phenomenon will later feed, not to the phenomenon itself. Stop, record
  status/warrant only, and move on; the source/target answer is Step 4-5's job, done once every
  HIB's own phenomena are already on record to reference.
- **(C) belongs to Step 7 (`closing.set`, `passage_linkage`, Q7) — not Step 3, and not really Step
  4-5 either.** A linkage connects two already-registered phenomena/operations; it cannot exist
  before both sides of it do.

**Why phenomena must be fully settled before operations can properly function — substantively, not
just because the code refuses.** This is already a hard gate (`phenomena_complete_at` NULL →
`operation.set` refuses, `phenomena-incomplete`) but the reason runs deeper than the gate: writing
ANY operation means resolving dimension (A) — naming source/target parties — and those parties are
frequently OTHER HIBs' own registered phenomena. If the full cast's phenomena aren't on record yet,
an operation's source/target references are citing data that doesn't exist yet, forcing a guess or
an invention instead of a citation to an actual phenomenon row. The gate isn't just process
hygiene; it's the only way dimension (A) has anything real to point at.

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
clean orthogonal axes. `hib.kind` had **no enum constraint at all** originally
(`cfg_column.expectation` was `NULL` — genuinely free text). Now: `cfg_enum 'hib_kind'` (6 values,
approved and active, confirmed live 2026-08-07 — §4a) + `operations.py:_valid_hib_kinds` reads it
live and rejects any `hib.kind` not in the set (`invalid-kind`) — the check is genuinely active
now, not a documented skip.

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
(§above) → `unreconciled` (natural key = `label`; content = `(kind, sorted(verses),
sorted(referent_options))`) → **`quality-check-incomplete`** (§2.6 — checked against `new`/
`changed` items only, after reconciliation, before any write) → **`hib-has-dependent-phenomena`**
(§2.2a, new 2026-08-07 — any `remove` entry with a live `phenomenon` row still pointing at it) →
write-grant check. (Corrected 2026-08-07: `quality-check-incomplete` was missing from this list —
verified directly against `handlers/operations.py:hib_set`, not assumed from an earlier draft of
this line.)

**DB writes, column-level — corrected 2026-08-07, §2.2a/§2.2 step 7:**
- `hib`, **`new`**: `book`, `label`, `kind`, `first_verse_id` (the payload's first listed verse),
  `created_at`, `deleted`. `hib`, **`changed`**: `UPDATE ... SET kind=?, first_verse_id=? WHERE
  id=?` — the existing row's `id` is preserved (was: soft-delete + reinsert under a new id, which
  silently orphaned any `phenomenon.hib_id` already pointing at it — fixed, not just documented).
- `hib_referent_option` (per referent-crux option): `hib_id`, `reading_text`, `textual_grounds`,
  `adopted`, `ordinal`, `created_at`, `deleted` — always fully replaced under `new`+`changed`
  (nothing else references its own id, so there's no identity to preserve here).
- `verse_hib` (one per HIB×verse): `verse_id`, `hib_id`, `created_at`, `deleted` — same, always
  fully replaced.
- `changed`/`removed` HIBs: `hib_referent_option`/`verse_hib` children are cascade-soft-deleted
  first, same as before; `removed` HIBs' own `hib` row is also soft-deleted (only `changed` HIBs
  keep their `hib` row alive, updated in place) — and only after the `hib-has-dependent-phenomena`
  guard above has already confirmed nothing live depends on it.

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

**Told AROUND the HIBs, not as a generic plot summary (§2.7).** `story_summary` is one prose field,
but what fills it is not "what happens in this chapter" in the abstract — it is the passage read
through its own cast: which HIB the throughline follows, who else enters and what role they play in
that HIB's own arc, in roughly the dominance order §2.7 describes (most-dominant HIB's arc as the
spine, others introduced as they bear on it). A story that could be told with the HIB list deleted
and read identically has not actually done this step's job, even if `feasible=true` is otherwise a
correct call.

**Invocation:** `Build-Passages.ps1 -Book <book> (-Chapters <r>|-Range <r>) -PayloadPath <json>`.

**Payload:** `{"book", "story_summary", "feasible", "feasibility_note", "reconciliation_note"}` —
the last only required when correcting an already-registered scope's content.

**DB reads:** `verse` (the exact scope, via `versespanmeaningreport.fetch_verses`); `verse_hib`
(does this scope have any identified HIB at all — Step 1 must have run first); `passagetrack.
find_tracked_passage` (an exact-scope match, if one already exists); every OTHER live `passage`
row (any rule) owning any verse in this scope, via `verse_passage` (the overlap check — see below).

**Method rules — `cfg_method_rule WHERE step='passage.build'` (6 rows — 5 backfilled 2026-08-07,
see note below):**

| rule_key | rule_text | source_doc | enforced_by |
|---|---|---|---|
| `input-scope-is-the-passage` | A passage is the debate's own input scope, registered verbatim — never sub-divided by algorithm. | researcher direction, 2026-08-06, following the HIB-distribution visualization | `passage.py:build` |
| `story-synthesis-required` | Step 2's real output is a high-level story synthesis for the scope, read in light of the identified HIBs — not a derived boundary. | researcher direction, 2026-08-06 | schema: `passage.story_summary` |
| `story-organized-by-hib` | The story synthesis is told through the passage's own cast, not as a generic plot summary — the dominant HIB's own arc as the spine, others introduced as they bear on it. | researcher direction, 2026-08-07 | — |
| `feasibility-self-assessment` | Before registering a passage, self-assess whether the scope can be read as a whole without quality loss; if not, the debate is skipped with a message to revise the input scope, not silently sub-divided. | researcher direction, 2026-08-06 | `passage.py:build` (`scope-too-complex` refusal) |
| `one-passage-per-verse` | A verse belongs to at most one live passage at a time. | app convention (DB-enforced: `verse_passage.verse_id` unique) | schema: `verse_passage` unique constraint + `passage.py:build`'s overlap check |
| `legacy-superseded-unconditionally` | A legacy (pre-redefinition) passage overlapping a newly-registered scope is superseded wholesale — "not reconciling the old with the new." | researcher direction, 2026-08-05/06 | `passage.py:build` |

**Backfilled 2026-08-07:** the 4 non-`story-organized-by-hib` rows above were documented in this
table since this document's first draft but, checked live, never actually existed in
`cfg_method_rule` — a pre-existing doc/DB gap unrelated to the HIB-centricity correction, found
while responding to it. `migration/complete_method_config_20260807.py` (idempotent) wrote them
verbatim from this table's own prior wording — the content was never wrong, only never actually
config-resident.

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

**Traversal order — HIB-first, not verse-first (§2.7).** Start with the passage's most dominant
HIB (§2.7's selection rule); read every verse THAT HIB appears in, in verse order, checking each
call against the verse's own `verse_lexical` row (full range, not the story or the printed gloss —
the researcher's own correction, 2026-08-07: *"the phenomena MUST be validate against the lexical
of the verse. That is the whole purpose of doing the lexical"*), producing that HIB's complete
phenomena list before moving to the next HIB. Repeat per HIB until the control total (below) is
met. **Stay inside dimension-free territory the whole time** — no reasoning yet about who caused a
phenomenon or what it leads to (§2.7's (A)/(B)/(C)); the only question this step ever answers is
"does THIS HIB's own inner life show a state/disposition/characteristic in THIS verse, and is it
stated, inferred, or silent."

**Invocation:** `Operations-Ingest.ps1 -Step phenomenon.set -Book <book> (-Chapters|-Range)
-PayloadPath <json>`.

**DB reads:** `_find_new_model_passage` (range-identity match, refuses a legacy-row match); `hib`
(label→id); `phenomenon` JOIN `verse` JOIN `hib` (current state); `verse_passage` + `verse_hib`
(the control total).

**Method rules — `cfg_method_rule WHERE step='phenomenon.set'` (9 rows, live — one real citation
error found and fixed 2026-08-06, three rows added 2026-08-07, `multi-chapter-vigilance` moved OUT
to `closing.set` 2026-08-07, its actual home per its own text — see Step 6 below):**

| rule_key | rule_text | source_doc | enforced_by |
|---|---|---|---|
| `phase-separation` | The phenomena register (Phase 1) must be completed for the WHOLE passage before any operation (Phase 2) is written for ANY verse in it — not interleaved verse-by-verse. Running Phase 2 immediately after Phase 1 verse-by-verse reopens the same drift, since operation-writing momentum can bleed back into how the next verse's phenomenon gets identified. | WA-passage-read-guidance-v1.5 Phase 1/Phase 2 structure + its own 2026-08-02 change-control note (the direct fix for the Amos 1-3 drift) | `phenomenon.set` (gate) + `operation.set` (refuses while NULL) |
| `hib-first-traversal` | Work HIB-by-HIB, not verse-by-verse — start with the passage's most dominant HIB, read every verse it appears in against its own `verse_lexical` row (full range, not the story or the printed gloss), complete that HIB's full phenomena list, then move to the next HIB. No source/target/cross-HIB reasoning during this step. | researcher direction, 2026-08-07 | — |
| `hidden-behind-act` | A phenomenon may be hidden behind a stated act or a refrained-from act, with only the act recorded in the text — naming what the act is taken to evidence is exactly this step's job. | WA-passage-read-guidance-v1.5 step 3 note e | — |
| `warrant-required` | For every phenomenon isolated, record the specific textual warrant that grounds it (the verb, clause, or stated silence) and whether it is stated or inferred — its own register entry, written before and independently of any operation. | WA-passage-read-guidance-v1.5 step 3b | schema: `phenomenon.textual_warrant`/`status` |
| `not-literary-pattern` | A genuine literary/structural/genre observation is not a phenomenon — log it once as an emergent question (Step 7) instead, never built into the phenomena register. | WA-interpretation-questions-v1.4 Part B.12; WA-passage-read-guidance-v1.5 step 6 note c | — |
| `control-total` | Every HIB crossed with every verse it appears in, in this passage, equals the exact number of phenomena-register entries (including explicit "silent" entries) Step 3 must produce before it can be considered done. | debate-analytic-process-digest-20260805.md Step 3; b3-b5-operations-schema-design-20260805.md | `phenomenon.set` (verse_hib pair-set vs. live phenomenon pair-set) |
| `silence-is-a-finding` | "No phenomenon found, silent" is a valid RESULT of running the phenomenon check on a human-bearing clause, not an omission — and not a valid substitute for running the check. | WA-interpretation-questions-v1.4 Part B.4; WA-passage-read-guidance-v1.5 step 2 note f | schema: `phenomenon.status='silent'` |
| `hib-still-warranted` | Once a HIB's phenomena list is complete across the whole passage, review whether it still genuinely warrants being a HIB at all — if there is no inner-being role or effect anywhere, and no reasonable basis to infer one, go back and correct `hib.set` (remove, with reason) before treating this HIB's phenomena as final. Distinct from `silence-is-a-finding`: some/all-silent is not automatically suspect. Mirrors `operation.set`'s existing `operation-from-phenomenon-only` one level down. | researcher direction, 2026-08-07 | — |
| `full-lexical-weight-in-description` | A phenomenon's description must draw on the word's actual full lexical range (the whole `meaning_tree` entry for its governing Strong's code, per T2) — not a brief, generic, or stereotyped label. The specific sense operative in THIS context, in its own fullness, is where the phenomenon's real content resides; flattening it into a stock gloss compromises that content. Context-specific every time, never a reusable stock phrase. | researcher direction, 2026-08-07 | — |

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

**Quality checks — `cfg_quality_check WHERE step='phenomenon.set'` (5 rows, all `required=1`,
enforced — `_check_quality_attestations` in `phenomenon_set`; rows 4-5 added 2026-08-07):**

| check_key | question | test_kind |
|---|---|---|
| `genuinely-inner-being` | Is this phenomenon actually a state, disposition, or characteristic of the HIB's inner life — not a purely outward/administrative fact restated without any interior content identified? | reasonableness |
| `not-a-literary-pattern` | Is this entry a genuine per-verse, per-HIB phenomenon — not a textual/structural pattern (recurring formula, book-wide thesis) smuggled in as if it were one? | non_existence |
| `warrant-is-specific` | Does `textual_warrant` name an actual verb/clause/stated silence in this verse, not a vague restatement of the description field? | existence |
| `hib-still-warranted` | Having completed this HIB's full phenomena list for the passage, does it still genuinely warrant being a HIB — or has the review revealed `hib.set` needs correcting (and has that correction already been submitted)? | reasonableness |
| `description-uses-full-lexical-range` | Does this description draw on the governing word's full lexical range and its specific contextual sense here — not a brief, generic, or stereotyped label that could apply to any similar-sounding phenomenon regardless of context? | reasonableness |

**Controls, in order:** `no-passage`/`legacy-passage` → `unresolved-reference` → `unreconciled`
(natural key = `(verse_osis, hib_label, ordinal)`; content = `(description, textual_warrant,
status)`) → **`quality-check-incomplete`** (§2.6, `new`/`changed` items only) →
**`phenomenon-has-dependent-operations`** (§2.2a, new 2026-08-07 — any `remove` entry with a live
`operation` row still pointing at it) → write-grant check → writes → **the control total, computed
AFTER the write, not a pre-write hard stop like the others above** — it decides the phase-gate
flag, it never refuses the call itself: `vh_pairs` (every live `(verse_id, hib_id)` from
`verse_hib` for the passage's verses) vs. `live_pairs` (same shape from `unchanged ∪ new ∪ changed`
phenomena, `removed` excluded) → `missing` non-empty sets `phenomena_complete_at = NULL`
(explicitly re-opening a previously-set gate, the bug fixed this session — it used to only ever
move forward); `missing` empty sets it to the current UTC timestamp.

**DB writes, column-level — corrected 2026-08-07, §2.2a/§2.2 step 7:**
- `phenomenon`, **`new`**: `passage_id`, `verse_id`, `hib_id`, `description`, `textual_warrant`,
  `status`, `ordinal`, `created_at`, `deleted`. `phenomenon`, **`changed`**: `UPDATE ... SET
  description=?, textual_warrant=?, status=? WHERE id=?` — the existing row's `id` is preserved
  (was: soft-delete + reinsert under a new id, silently orphaning any `operation.phenomenon_id`
  already pointing at it).
- `passage.phenomena_complete_at`: written every call, one way or the other — unchanged.

**Outputs:** `ok` with counts + gate status; reconciliation report.

**Unlocks:** `phenomena_complete_at IS NOT NULL` is what Step 4-5 requires.

### Step 4-5 — Operations (`operation.set`)

**Where §2.7's dimensions (A) and (B) actually get resolved.** This is the first step where
"who is the source, who is the target" is even an answerable question — `phenomenon` carries no
such field, deliberately. Working HIB-first here too: for the focused HIB's own operations,
naming another HIB as source/target (dimension A) means citing that OTHER HIB's own already-
registered phenomenon (Step 3 must already be complete for the whole passage, every HIB, before
this can be done honestly — see §2.7's closing paragraph). Once every HIB's operations are built,
check the mirror (dimension B): where HIB-X was named as a party inside HIB-Y's operation, does
HIB-X's OWN operation (once reached) show the reciprocal relationship consistently — not
duplicated data, a coherence check on the same real-world relationship seen from both sides.
Dimension (C) — movement/linkage BETWEEN separate HIBs' operations across the passage — is
deliberately NOT this step's job; it is Step 7's (`passage_linkage`, Q7), because a linkage can
only be drawn between two operations that already exist.

**Invocation:** `Operations-Ingest.ps1 -Step operation.set -Book <book> (-Chapters|-Range)
-PayloadPath <json>`.

**DB reads:** same passage resolution as Step 3, plus `phenomena_complete_at` itself; `hib`
(label→id); `phenomenon` (resolve `(verse, hib_label, ordinal)` → `phenomenon_id`); `operation`
JOIN `phenomenon` JOIN `verse` JOIN `hib` (current state); `operation_party` (children, part of the
content comparison).

**Method rules — `cfg_method_rule WHERE step='operation.set'` (9 rows, live — the 7th row below
was added 2026-08-06 and was missing from this table until now, found correcting the same-day
row-count staleness this session):**

| rule_key | rule_text | source_doc | enforced_by |
|---|---|---|---|
| `operation-from-phenomenon-only` | An operation may only originate from an already-registered phenomenon — never identify a fresh phenomenon while writing one. If writing an operation reveals no genuine phenomenon underlies it, the Step 3 entry was mis-identified — go back and correct it; do not paper over the mismatch. | WA-interpretation-questions-v1.4 Part B.12 | schema: `operation.phenomenon_id NOT NULL` + `operation.set` |
| `four-parts` | Every operation has: process (a state/status, or a movement — come from / go to / impact on / emerge / go away / become evident); source; target; and an action-type label. Source and target may be singular, multiple, mixed, or non-existent. | WA-passage-read-guidance-v1.5 step 1 note a | schema: `operation` + `operation_party` |
| `source-vs-enablement` | Keep source of the interior state and source of enablement to act distinct — a non-human being may be the stated source of an outcome or an enablement without the text sourcing the actor's own disposition; extending sourcing from outcome to interior is an interpretive step to flag, never to assume. | WA-interpretation-questions-v1.4 Q4 / Part B.5 | schema: `operation_party.enablement_only` |
| `action-type-is-a-label` | The action-type is a short, natural, verb-based tag — a label for cross-passage/cross-book comparison, not a taxonomy; no controlled vocabulary is being built. | WA-interpretation-questions-v1.4 Q11 / Part B.10 | schema: `operation.action_type` (free text) |
| `divine-mirroring-anchored` | Record a human/divine operation comparison only where the text's own juxtaposition or wording anchors it — a merely plausible resemblance is logged as an emergent question, never asserted or theologically elaborated. | WA-interpretation-questions-v1.4 Q12 / Part B.11 | — |
| `decision-enum` | decision = retain \| set_aside \| retain_referential \| recorded_silence. | WA-interpretation-questions-v1.4 Part C section 3 | schema: `operation.decision` (free text, not yet `cfg_enum`-enforced — see follow-up below) |
| `hib-can-be-party-in-another-hibs-operation` | A HIB can be a party within another HIB's own operation (e.g. a king acting against Daniel) — `operation_party.kind='human'`, with an optional `hib_label` naming the other HIB (resolved to `operation_party.hib_id`, a real structural link) alongside the existing free-text `detail`. **Corrected 2026-08-07** (Finding 2, `debate-schema-traceability-gap-findings-20260807.md`): `detail` alone was not sufficient traceability — only 3 of 42 live `detail` values matched a `hib.label` even as text; `hib_id` is now the real link, `detail` stays as a gloss alongside it, not a replacement. Distinct from a non-human party (`kind='non_human'`), which never gets its own hib/phenomenon/operation rows at all. | researcher direct correction, same session as `dan8-debate-run-failure-review-20260806.md`; corrected 2026-08-07 | schema: `operation_party.hib_id` (FK → `hib.id`) + `operations.py:operation_set` hib_label resolution |
| `hib-fanout-dimensions` | Fanning out from the focused HIB to the rest of the passage's cast has three distinct dimensions: (A) another HIB as source/target within the focused HIB's own operation; (B) the mirror once focus switches to that other HIB, checked for consistency, not re-derived; (C) movement/process BETWEEN two different HIBs' already-registered phenomena/operations, which belongs to `closing.set`'s `passage_linkage` (Q7), not to `operation.set` itself. Only (A) and (B) are this step's job. | researcher direction, 2026-08-07 | — |
| `full-lexical-weight-in-observation` | The same discipline as `phenomenon.set`'s `full-lexical-weight-in-description` rule, applied to an operation's `observation_text`/`description_text`: draw on the governing word's full lexical range, in this exact context, not a brief generic label. Distinct from `action_type` (a short label, deliberately — `action-type-is-a-label`) — observation/description text is where the full weight belongs. | researcher direction, 2026-08-07 | — |

**Quality checks — `cfg_quality_check WHERE step='operation.set'` (3 rows, all `required=1`,
enforced — `_check_quality_attestations` in `operation_set`; 3rd row added 2026-08-07):**

| check_key | question | test_kind |
|---|---|---|
| `phenomenon-actually-underlies-it` | Having written this operation, does a genuine phenomenon actually underlie it — or has writing it revealed the Step 3 entry needs correcting? | reasonableness |
| `source-target-not-invented` | Are the source/target parties actually named or clearly identifiable in the verse/passage, not invented to complete the operation's shape? | non_existence |
| `observation-uses-full-lexical-range` | Does `observation_text`/`description_text` draw on the governing word's full lexical range and its specific contextual sense here — not a brief, generic, or stereotyped label? | reasonableness |

**Controls, in order:** `no-passage`/`legacy-passage` → **`phenomena-incomplete`** (hard refusal if
`phenomena_complete_at` is NULL, checked live, never assumed) → `unresolved-reference` (now also
covers an unresolvable party `hib_label`, 2026-08-07) → **`invalid-decision`** (existence check —
`operation.decision` must be one of `enum.operation_decision`'s 4 values; `action_type`
deliberately gets no such check, `action-type-is-a-label`) → `unreconciled` (natural key =
`(verse_osis, hib_label, phenomenon_ordinal)`; content = `(process, action_type, decision,
observation_text, description_text, sorted(sources), sorted(targets))` — `sources`/`targets`
content now includes each party's resolved `hib_id`, 2026-08-07, so a `hib_label` correction alone
registers as `changed`) → **`quality-check-incomplete`** (§2.6, `new`/`changed` items only) →
**`operation-has-dependent-linkage`** (§2.2a, new 2026-08-07 — any `remove` entry a live
`passage_linkage` still points at) → write-grant check. (Corrected 2026-08-07: `invalid-decision`
and `quality-check-incomplete` were both missing from this list — verified directly against
`handlers/operations.py:operation_set`.)

**DB writes, column-level — corrected 2026-08-07, §2.2a/§2.2 step 7:**
- `operation`, **`new`**: `phenomenon_id`, `process`, `action_type`, `decision`, `observation_text`,
  `description_text`, `created_at`, `deleted`. `operation`, **`changed`**: `UPDATE ... SET
  process=?, action_type=?, decision=?, observation_text=?, description_text=? WHERE id=?` — the
  existing row's `id` is preserved (was: soft-delete + reinsert under a new id, silently orphaning
  any `passage_linkage.from/to_operation_id` already pointing at it).
- `operation_party` (per source/target, `new`+`changed`): `operation_id`, `role`, `kind`, `detail`,
  **`hib_id`** (new column, resolved from an optional payload `hib_label`), `enablement_only`,
  `ordinal`, `created_at`, `deleted` — always fully replaced regardless of whether the parent
  `operation` is `new` or `changed` (nothing else references a party's own id).

**Outputs:** `ok` with counts + party-record count; reconciliation report.

**Follow-up flagged, not built:** `operation.decision`/`operation.action_type` are free text today,
same as `hib.kind` was before this revision. `decision`'s four values are a genuinely closed set
(`WA-interpretation-questions-v1.4` Part C names exactly four) — a natural next `cfg_enum` +
write-time check, same shape as `hib_kind`, not done in this pass given the volume already covered
today. `action_type` is explicitly NOT meant to be a controlled vocabulary (Part B.10) so should
stay free text.

**Unlocks:** every live phenomenon having a live operation is what `closing.set` (Step 7) checks.

### Step 6 — Closing sections (`closing.set`)

**Full review completed 2026-08-07 — not deferred, nothing left open.** Four lists plus one single
field, each independently reconciled, each independently quality-gated, all four write-grants live,
all four content sources verified fresh against `WA-interpretation-questions-v1.4` line by line —
not trusted from an earlier pass's own paraphrase (two of the five rule_texts were strengthened
this same review, below).

**Invocation:** `Operations-Ingest.ps1 -Step closing.set -Book <book> (-Chapters|-Range)
-PayloadPath <json>`.

**Payload:** `{"book",
"linkages": [{"from_verse","from_hib_label","from_phenomenon_ordinal","to_verse","to_hib_label","to_phenomenon_ordinal","note","ordinal","reconciliation_note","quality_checks"}],
"insufficiencies": [{"verse","note","ordinal","reconciliation_note","quality_checks"}],
"emergent_questions": [{"verse","question_text","kind","ordinal","reconciliation_note","quality_checks"}],
"validation_notes": [{"phenomenon_verse","phenomenon_hib_label","phenomenon_ordinal","finding_text","corrected","ordinal","reconciliation_note","quality_checks"}],
"open_decisions_note": "...",
"remove": {"linkages": [...], "insufficiencies": [...], "emergent_questions": [...], "validation_notes": [...]}}`
— `verse`/`phenomenon_verse` are optional on `insufficiencies`/`emergent_questions`/
`validation_notes` (a passage-level, not verse-specific, finding is legitimate); `quality_checks`
required on every NEW or CHANGED item, per that item's own list (see quality checks below).

**DB reads:** `_find_new_model_passage` (range-identity match, refuses a legacy-row match);
live operations-completeness (`phenomenon` JOIN `operation`, computed fresh every call, never
trusted from a stored flag); `_find_operation_id`/`_find_phenomenon_id` (cross-reference resolution
for `linkages`/`validation_notes`); current live state of all four target tables, for
reconciliation.

**Method rules — `cfg_method_rule WHERE step='closing.set'` (6 rows — 5 added 2026-08-07, 2 of
those strengthened same day after a fresh line-by-line re-check against source; `multi-chapter-
vigilance` MOVED IN from `phenomenon.set` same day, its actual home per its own text, found doing
the researcher-requested full step-linkage audit):**

| rule_key | rule_text | source_doc | enforced_by |
|---|---|---|---|
| `linkages-q7` | What linkages run to other operations in the passage? Where a linkage is absent, surface the absence; do not pass over it silently. A Q7 linkage connects two specific, already-registered phenomena/operations — not licence to narrate a pattern across a whole chapter range. | WA-interpretation-questions-v1.4 Part A Q7 / Part B.12 / Part C item 4 | schema: `passage_linkage` |
| `insufficiencies-register` | Where required data (e.g. name etymologies) is absent from the base extract, name it as an insufficiency; do not substitute remembered or external knowledge. | WA-interpretation-questions-v1.4 Part B.7 / Part C item 5 | schema: `passage_insufficiency` |
| `emergent-questions-log` | Interpretive forks and genuine literary/structural observations are carried forward here. An interpretive fork is NOT a researcher decision awaiting a ruling — it is named where it bites, weighed against each new data point as the corpus grows, and answered (or left open) by what the accumulating evidence actually shows, not settled in the abstract before the evidence is in. "The researcher should decide" is reserved for genuine resourcing/data-curation choices this instrument cannot make for itself, not for interpretive questions the study itself exists to answer. Not merged with other passages' logs. | WA-interpretation-questions-v1.4 Part A Q10 / Part B.8-B.9 / Part C item 6 | schema: `passage_emergent_question` |
| `debate-quality-validation` | Once phenomena and operations are assembled: re-examine each (or a representative sample) — is it genuinely an inner-being phenomenon, does its Phase 1 justification actually warrant it, does its Phase 2 operation track faithfully back to it? **Correct any failure found before the debate is considered filled — do not merely log it for later.** | WA-interpretation-questions-v1.4 Part C item 7 | schema: `passage_validation_note` (`corrected` flag) |
| `multi-chapter-vigilance` | Where a debate document spans multiple chapters, this validation pass should pay particular attention to phenomena/justifications that read as though they are describing the passage's own literary architecture rather than a specific inner being's own state — the exact failure mode `phenomenon.set`'s `phase-separation` rule exists to prevent, and this pass is the last check that it did not recur. | WA-passage-read-guidance-v1.5 step 6 note b | — |
| `open-decisions` | Next steps / open decisions, a single evolving summary field, not a repeating list. | WA-interpretation-questions-v1.4 Part C item 8 (field shape: `b3-b5-operations-schema-design-20260805.md`) | schema: `passage.open_decisions_note` |

**The progressive-correction principle, and how it relates to `debate-quality-validation`.**
`debate-quality-validation` is a single closing pass ("once phenomena and operations are
assembled"), matching its source exactly — it is the LAST check, not the ONLY one.
`phenomenon.set`'s `hib-still-warranted` rule and `operation.set`'s `operation-from-phenomenon-only`
rule are the same correction discipline applied one step earlier each time (§2.7), so an error is
caught and fixed before the next step builds on it, not only discovered here at the very end.

**Quality checks — `cfg_quality_check WHERE step='closing.set'` (4 rows, added 2026-08-07):**

| check_key | question | test_kind | applies to |
|---|---|---|---|
| `linkage-genuinely-registered` | Do both the from/to sides of this linkage reference already-registered phenomena/operations — not licence to narrate a pattern across the whole passage as if it were a linkage? | existence | `linkages` |
| `insufficiency-genuinely-absent` | Is this data genuinely absent from the base extract/lexical, not substituted from remembered or external knowledge? | non_existence | `insufficiencies` |
| `emergent-question-not-resolvable-now` | Is this a genuine interpretive fork or literary/structural observation that could not be resolved within the phenomena/operations themselves? | reasonableness | `emergent_questions` |
| `validation-finding-corrected-not-just-logged` | If this finding identifies a real failure, has it actually been corrected (`corrected=true`, correction submitted) rather than merely logged for later? | existence | `validation_notes` |

`closing.set` is the only step with FOUR heterogeneous item types under one step name — each check
applies to exactly one list, never all four at once. Enforced by filtering
`_required_quality_checks(ctx, "closing.set")` per `list_name` on its own `check_key` prefix before
calling `_check_quality_attestations`, checked once per section. A first version called it once
with the combined list, which wrongly demanded a linkage's own attestation on an
`emergent_questions` item — caught live before shipping (an `emergent_questions` test item was
asked to attest all four checks, not just its own) and fixed the same pass.

**Controls, in order, every one a hard stop before the next is even attempted:**
1. `legacy-passage` / `no-passage` — passage resolution.
2. `operations-incomplete` — every live `phenomenon` in the passage must already have a live
   `operation` (computed fresh, never assumed) before Step 6 can begin at all.
3. Per section, in this fixed order — `linkages` → `insufficiencies` → `emergent_questions` →
   `validation_notes` — `unresolved-reference` (an unknown verse, or an unresolvable
   phenomenon/operation cross-reference) then `unreconciled` (natural key = `ordinal` within the
   passage; content = that table's own tuple). A failure in any section stops the whole call —
   nothing from an earlier, cleanly-reconciled section is written either.
4. Once all four sections reconcile cleanly: quality-check attestations, per section as above —
   `quality-check-incomplete` if any new/changed item anywhere is missing its own required
   check(s).
5. Only now, for real: every section's writes (soft-delete `changed`/`removed`, insert `new`/
   `changed`), then `open_decisions_note` if present (its own `_may` write-grant check), then
   commit. Nothing is written piecemeal before this point — confirmed by the 2026-08-07 refactor
   that moved this function from reconcile-then-immediately-write per section to reconcile-all,
   quality-check-all, write-all.

**DB writes, column-level:**
- `passage_linkage` (per new/changed): `passage_id`, `from_operation_id`, `to_operation_id`,
  `note`, `ordinal`, `created_at`, `deleted`.
- `passage_insufficiency` (per new/changed): `passage_id`, `verse_id`, `note`, `ordinal`,
  `created_at`, `deleted`.
- `passage_emergent_question` (per new/changed): `passage_id`, `verse_id`, `question_text`,
  `kind`, `ordinal`, `created_at`, `deleted`.
- `passage_validation_note` (per new/changed): `passage_id`, `phenomenon_id`, `finding_text`,
  `corrected`, `ordinal`, `created_at`, `deleted`.
- `passage.open_decisions_note` — single-field `UPDATE`, only if the payload key is present.
- `changed`/`removed` rows across all four tables: soft-deleted before any new/changed row for
  that same table is inserted.

**Outputs:** `ok` with per-section unchanged/new/changed/removed counts + whether
`open_decisions_note` was updated; a reconciliation report
(`reportkit.oneoff_path`, `closing.set-reconciliation-{book}-{passage_id}`).

**Unlocks:** nothing further writes after this — Step 6 is the pipeline's last content-writing
step. What it unlocks is Step 7, which reads the complete DB state Step 6 just finished.

**Verified live**, real Dan 8 passage (id 37465), cleaned up after every test: empty payload
succeeds with 0 items everywhere; an item missing its required attestation correctly refuses,
0 rows written; the same item WITH the attestation succeeds and writes; a follow-up `remove` call
cleans it back out, 0 live rows confirmed after — Dan 8's real data unaffected throughout.

---

### Step 7 — Report (`build_debate_report.py`)

**Generated LAST, from the complete DB state, after Step 6 — this is the design, stated plainly,
not left implicit.** Nothing renders until the whole cast's phenomena, operations, AND closing
sections are already on record. `Debate-Run.ps1` enforces this by construction: it invokes this
tool automatically, once, immediately after `closing.set` succeeds — that is the only way this
normally runs.

**Invocation:** `python -m iba.app.tools.build_debate_report --book <book> (--chapters <r>|--range
<r>) [--out <path>]` — a standalone script, not `python -m iba.app.run` (no `Ctx`/dispatcher
involved), same shape as `build_verse_span_meaning_extract.py`.

**Why standalone, not a registered `cfg_report` step — a closed design decision, not deferred.**
`reportkit.render_scaffold` needs a `cfg_report`/`cfg_report_section` row per section (9 sections
here, each its own `configmaint.propose` approval cycle). This tool instead hand-builds Markdown
and writes via `reportkit.oneoff_path` — already governed by `governance.oneoff_report_dir`/
`_naming_pattern`/`_format`, zero new config required, same precedent
`build_verse_span_meaning_extract.py` already established for a read-mostly, DB-sourced report.
If the 9 section headings are ever wanted config-editable, promoting this to a registered
`cfg_report` step is a small, separately-scoped follow-up — not a gap in what's built now.

Refuses cleanly against a legacy (`rule IS NULL`) passage (`_find_passage`'s own guard).

**DB reads, broad — every table an earlier step wrote, nothing written here:** `verse_passage` +
`verse` (verse order — anchor first, then chapter/verse tiebreak in Python, since `verse` carries
no chapter/verse columns of its own); `verse_hib` (the control-total denominator shown in Process
control); `hib` (label/kind for every HIB in scope); `phenomenon`; `operation` +
`operation_party`; `passage_linkage`; `passage_insufficiency`; `passage_emergent_question`;
`passage_validation_note`; `passage.open_decisions_note`.

**Render structure — 9 sections, fixed order:**
0. **Process control** (researcher, 2026-08-06: *"I would expect both detail and controls
   regarding each table that was updated, and that the report tells the story"*) — live row-counts
   for every table this passage touches, the Step 3 phase-gate status
   (`passage.phenomena_complete_at`), the live-computed operations-completeness check,
   `needs_review`, and the computed `debate_status` (below).
1. Preliminaries — passage ref/id/rule/source, verse count, HIBs in scope.
2. Phenomena register (Phase 1) — per verse, per HIB: status, description, textual_warrant.
3. Per-verse operations (Phase 2) — per verse, per HIB's operation: action_type, decision,
   observation_text, process, every source/target party, description_text.
4. Passage-level linkages (Q7).
5. Insufficiencies register.
6. Emergent questions log.
7. Debate quality validation (Phase 3).
8. Open decisions / next steps.

**`debate_status` — computed live every call, never stored or hand-set:** `empty` (zero
phenomena) → `in-progress` (phenomena exist, but `phenomena_complete_at` isn't set, or some
phenomenon still has no operation) → `complete` (phase gate set AND every phenomenon has an
operation). Legacy `scaffold`/`filled` values coexist in the same `enum.passage_debate_status` for
the retired scaffold route's own historical passages — this tool never produces them.

**DB writes, narrow, column-level:** `passage.debate_path` (the rendered file's path),
`passage.debate_written_at` (UTC timestamp), `passage.debate_status` (computed above) —
grant-checked (`cfg_write_grant WHERE writer='report.debate' AND table_name='passage'`, confirmed
active) even with no `Ctx`/dispatcher here, same principle as every other write in this app. If
that grant is ever inactive, the file still renders; the 3 columns are skipped with an explicit
printed NOTE — never a silent partial write.

**Outputs:** the rendered `.md` file (`reportkit.oneoff_path`, topic `{book}-{scope}-debate-
report`, versioned on regenerate per `report.version_on_regenerate`); the 3 tracking columns.

**Unlocks:** nothing — Step 7 is the pipeline's terminal step. Regenerating it is always safe (a
narrow, idempotent write plus a full re-read) and is the correct way to see a passage's current
state after any of Steps 1-6 change: *"regenerate after any hib.set/phenomenon.set/operation.set/
closing.set call; never hand-edit,"* per the report's own header line.

---

## 4. Live `cfg_*` snapshot

**`cfg_method_rule`:** 37 active rows, confirmed against a live query 2026-08-07, final state this
session — `hib.set` (7), `passage.build` (6, 5 backfilled + `story-organized-by-hib`),
`phenomenon.set` (9, includes `hib-first-traversal`/`hib-still-warranted`/
`full-lexical-weight-in-description`), `operation.set` (9, includes
`hib-can-be-party-in-another-hibs-operation` [2026-08-06] and `hib-fanout-dimensions`/
`full-lexical-weight-in-observation` [2026-08-07]), `closing.set` (6, 5 added 2026-08-07 — this
step had zero before this session — plus `multi-chapter-vigilance` moved in from `phenomenon.set`
the same day, its actual home per its own text). The original 5 HIB-continuity `passage.build`
rows are hard-deleted, not soft — `migration/cleanout_retired_passage_config.py`, researcher-
authorized 2026-08-06 (unrelated to the 5 backfilled rows above, which are the CURRENT model's own
rules). **Full, unabbreviated text of every one of these 37 rows, verified complete against this
same live query, is in §4a below** — the tables in §3 above are convenient per-step summaries, not
the source of truth; §4a is.

**`cfg_quality_check`:** 17 active rows, **all `required=1`, all mechanically enforced** — `hib.set`
4 (1 fully automated, `kind-enum-membership`; 3 attestation-gated), `passage.build` 1 (structurally
satisfied by the required `feasibility_note` field, no separate mechanism), `phenomenon.set` 5,
`operation.set` 3, `closing.set` 4 (added 2026-08-07, the first step needing per-item-type
filtering rather than one flat required-list — see Step 6 above for the bug this caught before
shipping).

**`cfg_step` — `operations-ingest`** (chained=0): `hib.set` (0), `phenomenon.set` (1),
`operation.set` (2), `closing.set` (3), all active — `closing.set` approved and applied 2026-08-06
(§65/§71), this section's own "proposed, pending" wording was stale since then, corrected here.

**`cfg_write_grant`:** `hib.set → hib/hib_referent_option/verse_hib`; `phenomenon.set →
phenomenon/passage`; `operation.set → operation/operation_party`; `passage.build →
passage/verse_passage`; `closing.set → passage/passage_linkage/passage_insufficiency/
passage_emergent_question/passage_validation_note` — also approved and applied 2026-08-06, same
correction as above.

**`cfg_enum 'hib_kind'`:** 6 values (`named_individual`, `unnamed_individual`,
`named_collection`, `unnamed_collection`, `implicit_individual`, `implicit_collection`) —
approved and active, confirmed live 2026-08-07; `_valid_hib_kinds` genuinely enforces
`invalid-kind` now, not a documented skip.

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

## 4a. Every `cfg_method_rule` row, full text, grouped by step — the source of truth

Pulled directly from a live query 2026-08-07 (`SELECT step, rule_key, rule_text, source_doc,
enforced_by FROM cfg_method_rule WHERE active=1 ORDER BY step, ordinal`), not reconstructed from
§3's own tables — this is the check on §3, not a copy of it. **37 rows, 5 steps, every one linked
to the exact step whose handler reads/applies it** (the `step` column IS the linkage — there is no
separate mapping table to drift out of sync with it). Ordered here to match the pipeline's own
1→7 reading order, not the DB's per-step ordinal.

### `hib.set` (Step 1) — 7 rules

1. **`presumptive-candidate`** — *Every human mentioned — named or collective, major or minor,
   however briefly — is a presumptive candidate: anyone who acts, undergoes an act, thinks,
   speaks, refrains from acting, or is simply named as present. This holds even where the act
   looks purely outward, administrative, locational, or incidental — the inner-being content may
   be hidden behind the act, with only the act stated in the text.* — `WA-passage-read-guidance-
   v1.5` step 2 note f. Not code-enforced (a reading judgement).
2. **`non-human-scope`** — *HIB = Human Inner Being. A non-human being can NEVER itself be
   registered as a HIB, by definition — not conditionally, not when related to a human. A
   non-human being (an animal in a symbolic vision, an angel, a voice or other physical medium)
   may only appear as a source/target/related-object PARTY within a human HIB's own operation
   (`operation_party.kind='non_human'`) — never as its own `hib` row, phenomenon, or operation.
   Where a vision depicts a human king/kingdom in animal or symbolic form and the text itself
   resolves that image (e.g. Dan 8:20-23), the HIB is the resolved HUMAN referent, registered from
   its first (symbolic) appearance onward — not the animal/image itself as a separate entity.
   Superseded 2026-08-06 (same day as the first wording): the original text still allowed a
   non-human being "in scope" as its own HIB when related to a human (e.g. an angel) — corrected
   directly by the researcher: "a non human by definition cannot be a HIB."* — `WA-passage-read-
   guidance-v1.5` step 2 notes b, d. Not code-enforced.
3. **`collective-stays-collective`** — *A tribe, nation, "youths", "gentiles" etc. is recorded as
   ONE HIB representing the collection — not decomposed into individuals; any later operation
   involving it is a movement to/from a collection, not an individual.* — step 2 note c. Not
   code-enforced.
4. **`referential-named-not-skipped`** — *Where a party is unnamed but implied by the verse or
   wider passage, name it as a referential HIB; never assert an inferred identity as settled
   fact.* — step 2 note e. Not code-enforced.
5. **`referent-crux-resolution`** — *Where a pronoun or unnamed party is genuinely ambiguous
   (several readings all grammatically live), enumerate every live reading, give the textual
   grounds for each, adopt one explicitly (stating whether this is a directed/researcher call or
   this pass's own default), and keep the rejected alternatives on record.* —
   `debate-analytic-process-digest-20260805.md` Step 1 (T4 folded in). Enforced: schema
   `hib_referent_option`.
6. **`six-type-scheme`** — *Every HIB is typed along two axes: plurality (individual | collection)
   × specificity (named | unnamed | implicit) = six types: `named_individual`, `unnamed_individual`,
   `named_collection`, `unnamed_collection`, `implicit_individual`, `implicit_collection`.* —
   `nahum-1-inner-being-training-20260803.md` (researcher's own prior training pass). Enforced:
   `cfg_enum 'hib_kind'` + `operations.py:_valid_hib_kinds`.
7. **`db-compare-adjudicate`** — *Read the verses in scope; compare the fresh reading against
   what's already in the DB; validate the list against the DB; where the fresh reading differs,
   adjudicate and correct the DB — not blind re-derivation.* — researcher direction, 2026-08-06.
   Enforced: `operations.py:_reconcile`.

### `passage.build` (Step 2) — 6 rules

1. **`input-scope-is-the-passage`** — *A passage is the debate's own input scope, registered
   verbatim — never sub-divided by algorithm.* — researcher direction, 2026-08-06, following the
   HIB-distribution visualization. Enforced: `passage.py:build`.
2. **`story-synthesis-required`** — *Step 2's real output is a high-level story synthesis for the
   scope, read in light of the identified HIBs — not a derived boundary.* — researcher direction,
   2026-08-06. Enforced: schema `passage.story_summary`.
3. **`story-organized-by-hib`** — *The story synthesis is told through the passage's own cast, not
   as a generic plot summary — the dominant HIB's own arc as the spine, others introduced as they
   bear on it. A story that reads identically with the HIB list deleted has not done this step's
   job.* — researcher direction, 2026-08-07. Not code-enforced (a writing-quality judgement).
4. **`feasibility-self-assessment`** — *Before registering a passage, self-assess whether the
   scope can be read as a whole without quality loss; if not, the debate is skipped with a message
   to revise the input scope, not silently sub-divided.* — researcher direction, 2026-08-06.
   Enforced: `passage.py:build` (`scope-too-complex` refusal).
5. **`one-passage-per-verse`** — *A verse belongs to at most one live passage at a time.* — app
   convention (DB-enforced: `verse_passage.verse_id` unique). Enforced: schema unique constraint +
   `passage.py:build`'s overlap check.
6. **`legacy-superseded-unconditionally`** — *A legacy (pre-redefinition) passage overlapping a
   newly-registered scope is superseded wholesale — "not reconciling the old with the new."* —
   researcher direction, 2026-08-05/06. Enforced: `passage.py:build`.

### `phenomenon.set` (Step 3) — 9 rules

1. **`phase-separation`** — *The phenomena register (Phase 1) must be completed for the WHOLE
   passage before any operation (Phase 2) is written for ANY verse in it — not interleaved
   verse-by-verse. Running Phase 2 immediately after Phase 1 verse-by-verse reopens the same
   drift, since operation-writing momentum can bleed back into how the next verse's phenomenon
   gets identified.* — `WA-passage-read-guidance-v1.5` Phase 1/Phase 2 structure + its own
   2026-08-02 change-control note (the direct fix for the Amos 1-3 drift). Enforced:
   `operations.py:phenomenon_set` (`passage.phenomena_complete_at` gate) + `operation_set`
   (refuses while NULL).
2. **`hib-first-traversal`** — *Work HIB-by-HIB, not verse-by-verse: start with the passage's most
   dominant HIB (highest verse-count cross-checked against the story's own throughline), read
   every verse that HIB appears in against its own `verse_lexical` row (full range, not the story
   or the printed gloss), complete that HIB's full phenomena list, then move to the next HIB. Stay
   inside phenomenon-only territory throughout — no reasoning yet about source/target or cross-HIB
   movement (see `operation.set`'s `hib-fanout-dimensions` rule).* — researcher direction,
   2026-08-07. Not code-enforced (a traversal-discipline judgement).
3. **`hidden-behind-act`** — *A phenomenon may be hidden behind a stated act or a refrained-from
   act, with only the act recorded in the text — naming what the act is taken to evidence is
   exactly this step's job.* — step 3 note e. Not code-enforced.
4. **`warrant-required`** — *For every phenomenon isolated, record the specific textual warrant
   that grounds it (the verb, clause, or stated silence) and whether it is stated or inferred —
   its own register entry, written before and independently of any operation.* — step 3b.
   Enforced: schema `phenomenon.textual_warrant`/`status`.
5. **`not-literary-pattern`** — *A genuine literary/structural/genre observation is not a
   phenomenon — log it once as an emergent question (Step 6) instead, never built into the
   phenomena register.* — `WA-interpretation-questions-v1.4` Part B.12; `WA-passage-read-
   guidance-v1.5` step 6 note c. Not code-enforced.
6. **`control-total`** — *Every HIB crossed with every verse it appears in, in this passage,
   equals the exact number of phenomena-register entries (including explicit "silent" entries)
   Step 3 must produce before it can be considered done — known in advance, not dependent on
   trusting the pass to remember to cover everything.* — `debate-analytic-process-digest-
   20260805.md` Step 3 "how this gets controlled"; `b3-b5-operations-schema-design-20260805.md`.
   Enforced: `operations.py:phenomenon_set` (`verse_hib` pair-set vs live `phenomenon` pair-set
   comparison).
7. **`silence-is-a-finding`** — *"No phenomenon found, silent" is a valid RESULT of running the
   phenomenon check on a human-bearing clause, not an omission — and not a valid substitute for
   running the check.* — `WA-interpretation-questions-v1.4` Part B.4; step 2 note f. Enforced:
   schema `phenomenon.status='silent'`.
8. **`hib-still-warranted`** — *Once a HIB's phenomena list is complete across the whole passage,
   review whether it still genuinely warrants being a HIB at all — if there is no inner-being role
   or effect anywhere, and no reasonable basis to infer one, go back and correct `hib.set`
   (remove, with reason) before treating this HIB's phenomena as final. Distinct from
   `silence-is-a-finding`: a HIB with some or all silent entries is not automatically suspect —
   silence is a legitimate result. This rule is for a HIB that, on full review, was never a
   genuine candidate in the first place.* — researcher direction, 2026-08-07. Not code-enforced
   (a judgement call, attestation-gated instead — see quality checks).
9. **`full-lexical-weight-in-description`** — *A phenomenon's description must draw on the word's
   actual full lexical range (the whole `meaning_tree` entry for its governing Strong's code, per
   T2) — not a brief, generic, or stereotyped label. The specific sense operative in THIS context,
   in its own fullness, is where the phenomenon's real content resides; flattening it into a
   stock gloss compromises that content. Context-specific, every time — never a reusable stock
   phrase.* — researcher direction, 2026-08-07. Not code-enforced (attestation-gated).

### `operation.set` (Step 4-5) — 9 rules

1. **`operation-from-phenomenon-only`** — *An operation may only originate from an already-
   registered phenomenon — never identify a fresh phenomenon while writing one. If writing an
   operation reveals no genuine phenomenon underlies it, the Step 3 entry was mis-identified — go
   back and correct it; do not paper over the mismatch.* — `WA-interpretation-questions-v1.4`
   Part B.12. Enforced: schema `operation.phenomenon_id NOT NULL` + `operations.py:operation_set`.
2. **`four-parts`** — *Every operation has: process (a state/status, or a movement — come from /
   go to / impact on / emerge / go away / become evident); source; target; and an action-type
   label. Source and target may be singular, multiple, mixed, or non-existent.* —
   `WA-passage-read-guidance-v1.5` step 1 note a. Enforced: schema `operation` + `operation_party`.
3. **`source-vs-enablement`** — *Keep source of the interior state and source of enablement to act
   distinct — a non-human being may be the stated source of an outcome or an enablement without
   the text sourcing the actor's own disposition; extending sourcing from outcome to interior is
   an interpretive step to flag, never to assume.* — `WA-interpretation-questions-v1.4` Q4 / Part
   B.5. Enforced: schema `operation_party.enablement_only`.
4. **`action-type-is-a-label`** — *The action-type is a short, natural, verb-based tag (e.g.
   "gave", "summoned/complied", "worshiped") — a label for cross-passage/cross-book comparison,
   not a taxonomy; no controlled vocabulary is being built.* — Q11 / Part B.10. Enforced: schema
   `operation.action_type` (free text).
5. **`divine-mirroring-anchored`** — *Record a human/divine operation comparison (juxtaposition,
   difference, inversion) only where the text's own juxtaposition or wording anchors it — a
   merely plausible resemblance is logged as an emergent question, never asserted or
   theologically elaborated.* — Q12 / Part B.11. Not code-enforced.
6. **`decision-enum`** — *decision = retain | set_aside | retain_referential | recorded_silence.*
   — `WA-interpretation-questions-v1.4` Part C section 3. Enforced: `cfg_enum
   'operation_decision'` (4 active values) + `cfg_column.expectation` + the code's own
   `invalid-decision` check, all confirmed live — §6 item 1 below.
7. **`hib-can-be-party-in-another-hibs-operation`** — *A HIB can be a party within another HIB's
   own operation (e.g. a king acting against Daniel) — `operation_party.kind='human'` with
   `detail` naming the other HIB is how this is recorded; no separate mechanism or schema change
   is needed, `kind='human'` already covers it. This is distinct from a non-human party
   (`kind='non_human'`), which never gets its own hib/phenomenon/operation rows at all.* —
   researcher direct correction, same session as `dan8-debate-run-failure-review-20260806.md`.
   Enforced: schema `operation_party.kind='human'`.
8. **`hib-fanout-dimensions`** — *Fanning out from the focused HIB to the rest of the passage's
   cast has three distinct dimensions: (A) another HIB as source/target within the focused HIB's
   own operation; (B) the mirror once focus switches to that other HIB, checked for consistency,
   not re-derived; (C) movement/process BETWEEN two different HIBs' already-registered phenomena/
   operations, which belongs to `closing.set`'s `passage_linkage` (Q7), not to `operation.set`
   itself. Only (A) and (B) are this step's job.* — researcher direction, 2026-08-07. Not
   code-enforced.
9. **`full-lexical-weight-in-observation`** — *The same discipline as `phenomenon.set`'s
   `full-lexical-weight-in-description` rule, applied to an operation's `observation_text`/
   `description_text`: draw on the governing word's full lexical range, in this exact context,
   not a brief generic label. Distinct from `action_type` (a short label, deliberately —
   `action-type-is-a-label`) — observation/description text is where the full weight belongs.* —
   researcher direction, 2026-08-07. Not code-enforced (attestation-gated).

### `closing.set` (Step 6) — 6 rules

1. **`linkages-q7`** — *What linkages run to other operations in the passage? Where a linkage is
   absent, surface the absence; do not pass over it silently. A Q7 linkage connects two specific,
   already-registered phenomena/operations to each other — it is not licence to narrate a pattern
   across a whole chapter range.* — `WA-interpretation-questions-v1.4` Part A Q7 / Part B.12 /
   Part C item 4. Enforced: schema `passage_linkage`.
2. **`insufficiencies-register`** — *Where required data (e.g. name etymologies) is absent from
   the base extract, name it as an insufficiency; do not substitute remembered or external
   knowledge.* — Part B.7 / Part C item 5. Enforced: schema `passage_insufficiency`.
3. **`emergent-questions-log`** — *Interpretive forks and genuine literary/structural observations
   are carried forward here. An interpretive fork is NOT a researcher decision awaiting a ruling —
   it is named where it bites, weighed against each new data point as the corpus grows, and
   answered (or left open) by what the accumulating evidence actually shows, not settled in the
   abstract before the evidence is in. "The researcher should decide" is reserved for genuine
   resourcing/data-curation choices this instrument cannot make for itself, not for interpretive
   questions the study itself exists to answer. Not merged with other passages' logs.* — Part A
   Q10 / Part B.8-B.9 / Part C item 6. Enforced: schema `passage_emergent_question`.
4. **`debate-quality-validation`** — *Once the phenomena register and operations are assembled: a
   re-examination, for each phenomenon or a representative sample spanning the range, of whether
   it is genuinely an inner-being phenomenon (not a textual/structural pattern mislabeled as one),
   whether its Phase 1 justification actually warrants it, and whether its Phase 2 operation
   tracks faithfully back to it. CORRECT ANY FAILURE FOUND before the debate is considered filled,
   rather than only noting it for later.* — Part C item 7. Enforced: schema
   `passage_validation_note` (`corrected` flag).
5. **`multi-chapter-vigilance`** — *Where a debate document spans multiple chapters, this
   validation pass should pay particular attention to phenomena/justifications that read as
   though they are describing the passage's own literary architecture rather than a specific
   inner being's own state — the exact failure mode `phenomenon.set`'s `phase-separation` rule
   exists to prevent, and this pass is the last check that it did not recur.* —
   `WA-passage-read-guidance-v1.5` step 6 note b. Not code-enforced (moved here from
   `phenomenon.set` 2026-08-07 — its actual home, per its own text, now that `closing.set` has
   rows to move it to).
6. **`open-decisions`** — *Next steps / open decisions the passage's own analysis surfaces,
   recorded as a single evolving summary field, not a repeating structured list.* — Part C item 8
   (field shape: `b3-b5-operations-schema-design-20260805.md`). Enforced: schema
   `passage.open_decisions_note`.

**Total: 7 + 6 + 9 + 9 + 6 = 37 — matches the live count exactly.** Nothing is unaccounted for;
nothing is double-counted; every rule names the one step whose handler applies it.

---

## 5. Approvals — reviewed 2026-08-07 against live `cfg_*`, none carried forward

Every item this section named as "pending" was checked directly against the live DB, not assumed
from its own prior wording. **All 14 are confirmed applied — nothing is actually pending.** This
section's own "pending" framing had simply never been updated after BUILD.md §71 answered and
applied them 2026-08-06; corrected here.

| item | confirmed live | how checked |
|---|---|---|
| `closing.set` `cfg_step` insert | ✅ active | `cfg_step WHERE work_package='operations-ingest' AND step='closing.set'` |
| `closing.set` × 5 `cfg_write_grant` inserts | ✅ all 5 active | `cfg_write_grant WHERE writer='closing.set'` → `passage`/`passage_linkage`/`passage_insufficiency`/`passage_emergent_question`/`passage_validation_note` |
| `hib_kind` × 6 `cfg_enum` values | ✅ all 6 active | direct query, §4 above |
| `hib.kind` `cfg_column.expectation` → `enum.hib_kind` | ✅ live | direct query, §3 Step 1 |
| `retention.report/stuck_nonchained` `cfg_report_section` | ✅ active | direct query |

The Step 2 rebuild's own separate retirement batch (4 settings + 2 enum values) is not part of
this list — superseded by direct hard-delete, its 6 `configmaint.propose` escalations answered
`reject` as redundant at the time, not left pending either.

**`configmaint.validate` clean** as of this review (repeated live throughout 2026-08-07's own
work, §73/§74) — no open coherence errors, no un-actioned advisory findings.

**3 stray escalations found and closed in this same review** (#550-552) — all residue from this
session's own deliberate testing (the `cfg_method_rule`/`configmaint.propose` write-grant lesson
already understood, §73; before/after evidence for the `closing.set` per-item-type filtering fix,
§74), not live issues. Answered `reject` with the specific reasoning recorded on each.

---

## 6. Design questions — reviewed 2026-08-07, all 3 resolved, nothing left open

1. **`operation.decision` enum-ification — RESOLVED, doc was stale.** Checked live: `cfg_enum
   'operation_decision'` already has all 4 values active (`retain`/`set_aside`/
   `retain_referential`/`recorded_silence`), `cfg_column.expectation` for `operation.decision` is
   already `enum.operation_decision`, and `handlers/operations.py:operation_set`'s
   `invalid-decision` check (reading the enum live via `_valid_enum`) is therefore already active,
   not skipped. Built at some point after this document's first draft, never reflected here until
   now. `operation.action_type` deliberately stays free text (`action-type-is-a-label` rule,
   Part B.10) — that half was never meant to be enum-ified.
2. **What an operator does when a scope is refused as `scope-too-complex` — RESOLVED, researcher's
   own direct answer: unlikely to be an issue.** Not built or coded against — a judgement, not a
   mechanism, per the same reasoning `feasibility-self-assessment` already rests on (the refusal
   itself already works correctly and safely regardless: nothing written, clear message, narrow
   via `-Range` and resubmit). No further design or build follows from this.
3. **Steps 6/7's full analytical write-up — RESOLVED, no longer open.** Split into their own
   Step 6 (`closing.set`) and Step 7 (`build_debate_report.py`) sections in §3, each now at the
   same depth as Steps 1-5: Controls in order, DB writes column-level, Outputs, Unlocks — nothing
   deferred. Also corrected: Step 7 was mislabeled "Step 6" in the pipeline map (§1) and this
   document's own prose, in an order that contradicted what's actually built and running — the
   report is generated LAST, after `closing.set`, from the complete DB state, exactly as
   `Debate-Run.ps1` already executes it; the map now reads `closing.set`=6, report=7. §2.4's report
   fact-provenance preference is satisfied by design, not by a further build: the report is 100%
   DB-sourced (every section is a live query, nothing is asserted from memory or invented) and its
   own header already states this plainly ("Generated from `iba.db`... never hand-edit") — there is
   no memory-sourced content in this report for a provenance marker to distinguish FROM.

**Nothing else carried forward.** The previous revision's gap-tolerance-parameter and
`passage.release`-mechanism items (patches to the retired HIB-continuity algorithm) are moot, not
merely resolved (§3 Step 2); `cfg_quality_check` enforcement wiring is complete for all 17 active
checks across all 5 steps (§4); the Step 3 citation error is fixed (§3). All 3 items above are
resolved — none are carried into a future revision.
