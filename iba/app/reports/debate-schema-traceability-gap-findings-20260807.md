# Debate schema — traceability gap findings (2026-08-07)

> Investigation triggered by researcher's own observation (chat, 2026-08-07): "the database schema
> for the debate methods is not complete — no forward/backward traceability, relies on text scan,
> doesn't capture all the data of the debate; HIB must be traceable to a verse and phenomena,
> phenomena must be traceable to an operation; CRUD during a run must update the correct records;
> many-to-many index tables appear missing." This is a live-code + live-DB inspection (PRAGMA,
> `cfg_column`/`cfg_unique`, `handlers/operations.py`), not a doc read. All four claims checked
> against the actual DB and actual writer code, findings below are verified, not inferred.

## What's already there (so the gap is scoped correctly)

The debate core (`hib`, `hib_referent_option`, `verse_hib`, `phenomenon`, `operation`,
`operation_party`) plus the Step-7 closing tables (`passage_linkage`, `passage_insufficiency`,
`passage_emergent_question`, `passage_validation_note`) were built by
`iba/app/migration/build_operations_schema.py` + the Step-7 bootstrap. `cfg_column.fk` **does**
declare every intended relationship (`phenomenon.hib_id → hib.id`, `operation.phenomenon_id →
phenomenon.id`, `passage_linkage.from/to_operation_id → operation.id`, etc.) and `handlers/
operations.py`'s writers (`hib.set` / `phenomenon.set` / `operation.set` / `closing.set`) do
real ID-based JOIN traversal, not string-matching, for everything they touch. The reconciliation
gate (`_reconcile()`) is genuinely good: every pre-existing row must be re-affirmed or explicitly
removed-with-reason on every write, `phenomenon.set` correctly re-opens
`passage.phenomena_complete_at` if a correction/removal makes a previously-complete register
incomplete again, and a reconciliation log is written on every call. So the four claims below are
real gaps *within* an otherwise well-built writer, not "nothing exists."

## Finding 1 — zero enforced FK constraints, zero indexes, on every debate table

Verified via `PRAGMA foreign_key_list()` and `PRAGMA index_list()` against the live `iba.db`:

| table | FK constraints in DDL | indexes |
|---|---|---|
| `hib`, `hib_referent_option`, `verse_hib`, `phenomenon`, `operation`, `operation_party`, `passage_linkage`, `passage_insufficiency`, `passage_emergent_question`, `passage_validation_note` | **0** | **0** |

This is **deliberate, documented** in `build_operations_schema.py`'s own docstring: *"FK
relationships are documented via `cfg_column.fk` metadata only, not declared as SQL FOREIGN KEY
constraints — matching `verse_lexical`'s own precedent... not `passage`'s older, inconsistent
one."* So it was a conscious choice to follow the newer app convention, not an oversight — but the
practical consequence is real: every JOIN in `handlers/operations.py` (e.g. `operation.set`'s
`phenomenon ph JOIN verse v ON v.id=ph.verse_id JOIN hib h ON h.id=ph.hib_id`) runs against
**unindexed** columns, so SQLite does a full table scan on the child side of every join predicate.
At current volumes (47 `hib`, 270 `verse_hib`, 97 `phenomenon`, 97 `operation`, 197
`operation_party` rows) this is invisible; it will not stay invisible as more books are debated.
`cfg_unique` also declares two composite uniques (`verse_hib(verse_id,hib_id)`,
`phenomenon(passage_id,verse_id,hib_id,ordinal)`) that likewise have **no actual UNIQUE index** —
confirmed no duplicates exist today, but nothing in the DB stops one appearing; only the
application-side `_reconcile()` dict-keying currently prevents it, and a bug there would silently
collapse or misattribute rows rather than error.

**Traceability is only actually enforced by hand-written Python in every one of the four writer
functions.** There is no query anyone could run directly against the DB (a report script, an
ad-hoc audit, a future tool) that gets referential integrity for free — every consumer has to
reimplement the same JOIN chain `operations.py` uses.

## Finding 2 — operation parties are captured as free text, not linked to `hib`

This is the sharpest concrete case of "relies on text scan." `operation_party.detail` ("which
human/object, if named") is a plain `TEXT` column with **no FK** — not even in `cfg_column.fk`
metadata, unlike every other relational column in this table group. When an operation's source or
target *is* a HIB that already has its own `hib` row (e.g. "the king" as the target of an
operation, when "the king" is separately registered in `hib`), the link is written as a text
phrase, not `operation_party.hib_id → hib.id`.

Checked directly: of 42 distinct live `operation_party.detail` values (kind='human'), only **3**
match a live `hib.label` string exactly — e.g. `"the kings of Media and Persia"`,
`"the bold-faced king"`. The other 39 are free descriptive phrases (`"the first king, as the
nation of origin"`, `"one of the four kingdoms, his point of origin"`) that don't match any
`hib.label` even as text, let alone as an FK. **There is currently no reliable way — structural or
even textual — to answer "which operations name this HIB as a source/target?"** for the large
majority of rows. This is the direct, verified version of the researcher's "the phenomena must be
traceable to an operation" concern, one level further out: an operation's *parties*, when they are
themselves HIBs, aren't traceable back to the `hib` register at all.

## Finding 3 — HIB removal doesn't cascade or flag downstream `phenomenon`/`operation` rows

`hib_set`'s removal path (`handlers/operations.py:449-454`) soft-deletes `hib_referent_option`,
`verse_hib`, and `hib` for a removed label — and stops there. It does **not** check whether any
live `phenomenon` row already references that `hib_id` (Step 3 work already done against it), and
does not flag, block, or cascade to `operation`/`operation_party` rows further downstream. A HIB
correction made after phenomena/operations have already been written against it silently leaves
those rows pointing at a now-deleted `hib` row, with no report, no escalation, nothing surfaced —
the exact "when CRUD is performed... the correct records must be updated" failure the researcher
named. (Contrast: `passage.build`'s reconciliation was explicitly redesigned, 2026-08-05/06 — see
BUILD.md — so a passage-scope correction "can never orphan a `phenomenon`/`operation`." No
equivalent protection exists for a HIB-level correction.)

## Finding 4 — no note/reasoning column on any of the six core tables

Documented as a known, deferred gap in the same migration docstring: *"changed" items are
soft-deleted-and-reinserted (their note kept in the reconciliation log below, not the row itself —
none of the six tables carry a note column; adding one is future schema work, not required to
close this gap."* Every reconciliation note (why a HIB reading was corrected, why an operation's
decision changed) lives only in a one-off `.md` report file per run
(`iba/app/reports/*-reconciliation-*.md`), never in the DB itself. This is the "does not capture
all the data of the debate" gap: the *decision history* — why a row is the way it is — is not a
queryable DB fact, only a filesystem artifact scattered across per-run report files.

## Many-to-many junctions — what's genuinely missing vs. what's just unindexed

Re-examined every relationship in the six core + four closing tables against the researcher's "many
to many index tables missing" claim:

- `verse_hib` **is** a real M:N junction (verse ↔ hib) and is structurally fine — its only problem
  is Finding 1 (no unique index, no FK, no index).
- `passage_linkage` **is** a real M:N self-join on `operation` (operation ↔ operation) and is
  structurally fine, same caveat.
- `phenomenon`, `operation`, `operation_party` are genuinely 1:N child tables (one phenomenon has
  one hib/verse/passage; one operation has one phenomenon; operation_party is a child of one
  operation) — these do **not** need M:N junctions, a plain FK is the right shape once Finding 1 is
  fixed.
- The one place a **real M:N junction is actually absent** is Finding 2 above:
  `operation_party ↔ hib` (a party can be, and often is, a previously-registered HIB) currently has
  no linking table/column at all — that is the "missing many-to-many index table."

## What this document is NOT

This is a findings report, not a fix. Per IBA governance (config/schema changes need proposal +
researcher approval, never a silent write — `governance.rules_must_be_config_driven`,
`feedback_iba_config_changes_require_researcher_approval_never_silent`), no DDL or `cfg_*` rows
have been touched. Four separable questions for the researcher's own judgement, roughly in
ascending order of design work required:

1. **Retrofit FK constraints + indexes** on the ten existing tables (SQLite requires a
   `CREATE TABLE ... AS` rebuild + data copy to add FKs after the fact, not an `ALTER TABLE`) —
   mechanical once approved, no design decision beyond "yes, do it."
2. **Add a `hib_id` FK column to `operation_party`**, nullable (a party can be `self`/`non_human`/
   `object_situation`/`none`, which genuinely has no HIB to link), populated going forward and
   back-filled for the 3 exact-match rows found above — the real design question is whether
   `detail` stays as a free-text gloss alongside the new FK, or whether kind='human' should
   eventually *require* an `hib_id` (a stricter rule than exists today).
3. **Add a cascade/guard rule to `hib.set`'s removal path** — block removal of a HIB with live
   dependent `phenomenon` rows outright, or require an explicit acknowledgement/re-reconciliation
   of the dependents in the same payload, mirroring the pattern `passage.build` already uses.
4. **Add a `note`/reasoning column** to each of the six core tables (or a shared
   `debate_note`/audit table) so reconciliation reasoning is a live DB fact, not only a per-run
   report file.
