# Full-app schema remediation — design + execution record (2026-08-07)

> Supersedes the framing (not the findings) of `debate-schema-traceability-gap-findings-20260807.md`
> — that report scoped to the 10 debate tables; the researcher's follow-up direction (a-l, chat
> 2026-08-07) widened this to the whole app and named a root-cause question ("making a deliberate
> choice to build not fit for purpose tables... is incompetent") this document answers directly,
> then executes against. Pre-change snapshot:
> `iba/app/db/snapshots/iba-20260807T155245Z-schema-remediation-pre-fk-retrofit-20260.db`.

## Root cause (not "a design tradeoff" — a build/config conformance bug)

`lib/db.py:build_data_tables()` is this app's own **standard, generic, config-driven table
builder** — it reads `cfg_column` (including `cfg_column.fk`) and `cfg_unique` for every table in
`cfg_table` and emits real `FOREIGN KEY` constraints and composite `UNIQUE` constraints
automatically. Tables built this way (`word_strong`, `strong_verse`, `span`, `span_candidate`,
`strong_lexicon`, `strong_sense`, `passage`, `verse_passage`, `cfg_report*`, `escalation`,
`validation_result`, `candidate_seed`, `strong_lsj_parsed`, `strong_mounce_parsed`,
`strong_related`) **do** carry real FKs today — confirmed by `PRAGMA foreign_key_list`.

The debate tables (`hib`, `hib_referent_option`, `verse_hib`, `phenomenon`, `operation`,
`operation_party`, `passage_linkage`, `passage_insufficiency`, `passage_emergent_question`,
`passage_validation_note`) and two lexicon tables (`verse_lexical`, and — not even `cfg_column`-
declared — `strong_meaning_parsed`/`strong_meaning_tree`'s `strong_variant` column) were instead
built by **bespoke, hand-written migration scripts** (`build_operations_schema.py` etc.) that
wrote raw `CREATE TABLE` DDL directly, bypassing `build_data_tables()` entirely — while still
inserting the *correct* `cfg_column.fk` / `cfg_unique` metadata rows that `build_data_tables()`
would have read correctly, had it been used. `build_operations_schema.py`'s own docstring cites
"`verse_lexical`'s own precedent" as justification for skipping FK constraints — but `verse_lexical`
is itself one of the non-conformant tables, so the precedent cited was already a bug, and this
migration repeated it.

**This is the precise, evidenced form of the researcher's "incompetent" charge**: the config layer
was never wrong — `cfg_column.fk` mostly already declares the right relationships. The failure is
that the tables were never actually built the way the app's own established, config-driven
convention requires. Confirming these tables "fulfil the control mechanism of the debate" (as prior
work did) while they silently diverge from the app's own generic builder is exactly the gap named.
**The fix is therefore mechanical, not a from-scratch design exercise**: rebuild the non-conformant
tables to match what `build_data_tables()` already would have produced from current config, after
closing the two places config itself is incomplete (below).

## Answer to (g) — the JSON payload is not a second database; the missing constraints are

`handlers/operations.py`'s `PayloadPath` JSON files are a **batch input artifact**, not a store of
state — after a call the DB is the sole record; the same one-shot-input shape the main Bible-study
programme's `apply_session_patch.py` already uses, and the shape every other write step in this app
uses (`ctx.params["PayloadPath"]`). That part is not duplicated control.

What **is** real duplication: `_reconcile()` re-derives, in hand-written Python, integrity guarantees
that a correctly-built DB would give for free — natural-key uniqueness (no two live `hib` rows with
the same `label`; no two live `phenomenon` rows for the same `(passage_id, verse_id, hib_id,
ordinal)`) is currently enforced **only** by Python dict-keying at call time, because the `UNIQUE`
constraints `cfg_unique` already declares were never actually built into the tables. If `_reconcile`
had a real bug, or if any table were ever written to outside `operations.py` (a future report
script, an ad-hoc fix), nothing in the DB would catch a duplicate or a dangling reference. Once the
retrofit below lands, `_reconcile()`'s job shrinks to what it actually needs to do — deciding
whether a content-level *change* is justified and recording why — while SQLite itself guarantees
the structural integrity (existence, uniqueness) that Python was carrying alone. **Recommendation,
not a removal**: keep the JSON-payload/reconciliation pattern (it is the only place "why did this
change" is captured at all — see the note-column gap below), but stop asking it to be the *only*
thing standing between the DB and a duplicate or a dangling FK.

## The concrete fix

### 1. New app-wide mechanism: `cfg_index` (closes a gap in `build_data_tables()` itself)

`build_data_tables()` emits FK and UNIQUE constraints from config but has **no mechanism at all**
for plain (non-unique) secondary indexes — confirmed: no `cfg_index` table exists anywhere in the
app, and no table in the whole DB has an index on a bare FK column. SQLite does not auto-index FK
columns. Every one of the 32 data tables is exposed to the same "every JOIN on an FK column is a
full table scan" problem Finding 1 named for the debate tables specifically — it's just invisible
today at `span`'s 370k rows because SQLite is fast, not because it's indexed. Per the researcher's
own point (e) — record counts will increase exponentially — this needs to be a durable, config-
governed mechanism, not a one-off `CREATE INDEX` script for the debate tables alone (that would
repeat the exact mistake being fixed: a rule that exists in code/one migration but not in config).

**Built:** `cfg_index(table_name, name, col, ordinal)` — one row per (index, column-in-index),
mirroring `cfg_unique`'s shape exactly. `build_data_tables()` extended to emit
`CREATE INDEX IF NOT EXISTS "{name}" ON "{table}" ({cols})` for every named index after the table
DDL. Registered: one index per FK column across every table in `cfg_column.fk` app-wide (not just
the debate tables) — the same "close it everywhere, not just where it was noticed" standard this
session's other memory entries already hold this app to.

### 2. Two config gaps closed before rebuilding

- `strong_meaning_parsed.strong_variant` / `strong_meaning_tree.strong_variant`:
  `cfg_column.fk` set to `strong.strongNumber` (matching `span.strong_variant`'s existing
  convention) — these were never declared at all, not even in metadata.
- `operation_party`: new column `hib_id INTEGER` (nullable — a party can be `self`/`non_human`/
  `object_situation`/`none`, which has no HIB to link), `fk='hib.id'`. `detail` stays as-is (a
  human-readable gloss alongside the real FK, not replaced by it — kept per Finding 2's own
  recommendation: free text remains useful context, it just stops being the *only* record of the
  relationship). Existing rows: back-filled where `detail` exactly matches a live `hib.label` (3
  rows, per Finding 2); the remaining `kind='human'` rows are left `hib_id=NULL` — inventing a link
  the original analytical pass didn't make explicit would be a fabrication, not a fix; a genuinely
  unmatched party is exactly what T4-style referent uncertainty in this study looks like, no
  different in kind from an entry the study leaves openly unresolved elsewhere.

### 3. Tables rebuilt to match config (dependency order: parents before children)

`verse`, `passage` (already conformant, unchanged) → `hib` → `hib_referent_option`, `verse_hib` →
`phenomenon` → `operation` → `operation_party` → `passage_linkage`, `passage_insufficiency`,
`passage_emergent_question`, `passage_validation_note` → `verse_lexical` →
`strong_meaning_parsed`, `strong_meaning_tree`.

Method per table (SQLite has no `ALTER TABLE ... ADD CONSTRAINT`): rename the live table aside,
`CREATE TABLE` fresh from `build_data_tables()`'s own DDL generator (so the rebuilt table is
provably identical to what config declares — no hand-written DDL a second time), copy every row
across unchanged, `PRAGMA foreign_key_check` the rebuilt table, compare row counts old vs. new,
only then drop the renamed-aside original. Wrapped one table at a time in its own transaction —
never all tables in one transaction, so a failure on table N leaves 1..N-1 already verified-good
rather than rolling back silently.

### 4. Cascade/guard rules — generalised, not hib-only (item h)

`handlers/passage.py` already has the right pattern (a passage's removal/supersession cascades a
soft-delete to its `verse_passage` children — confirmed in code, `passage.py:167-168,174-176`).
`hib.set` was the one writer missing it. **Fixed the same way, not a bespoke rule**: `hib.set`'s
removal path now checks for live `phenomenon` rows referencing the `hib_id` being removed and
refuses (`hib-has-dependent-phenomena`) rather than silently soft-deleting the HIB out from under
already-written analytical work — mirroring `operation.set`'s own "refuse outright, never partial"
convention. Audited every other writer for the same class of gap:

- `phenomenon.set` / `operation.set` / `closing.set`: already correctly gated (Findings report
  confirmed `phenomenon.set` re-opens `phenomena_complete_at`; `operation.set` refuses until that
  gate is set; `closing.set` refuses until every phenomenon has an operation) — no change needed.
- `passage.py`: already cascades `verse_passage` — no change needed.
- `candidate.py` (`candidate_seed`): single-row soft-delete, no children — no cascade needed.
- `raw.py` (`verse`/`span`/`strong_verse`/`word_strong`): no soft-delete/removal path at all in
  this handler (ingest-only) — out of scope for a cascade rule.
- `registry.py` (`word_registry`): no removal path exposed — out of scope.

## What this does NOT change

- `cfg_*` config tables themselves (23 tables) are **not** in this retrofit. They're the governance
  layer, not the analytical data; several (`cfg_write_grant.table_name`, `cfg_report_csv_table`)
  legitimately reference not-yet-built tables during a proposal's pending window, which a hard FK
  would break. Their referential integrity is already served by `lib/cfgquality.py`'s
  orphan-detectors (`find_orphan_configs`, `find_unknown_write_grant_writers`, etc.) — a different,
  already-fit-for-purpose mechanism for a different kind of reference (config-to-code, not
  row-to-row). Named here so it's a recorded scoping decision, not a silent omission.
- The reconciliation/quality-check gate logic in `operations.py` is unchanged in shape — see (g)
  above; only the DB constraints underneath it changed.

## Verification standard applied

Every step below is checked, not assumed: `PRAGMA foreign_key_check` on every rebuilt table (must
return zero rows), row count before == row count after per table, `configmaint.validate` clean
afterward, a live `Debate-Run.ps1`-shaped read/write smoke test against the rebuilt tables.
