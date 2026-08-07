# SESSION LOG — 2026-08-07 — Full-app schema remediation: real FK/UNIQUE/index constraints,
an app-wide index mechanism, and cascade guards on every reconciling writer

Continuation of the same day's earlier work (`SESSION-LOG-20260807-dan1-clear-for-lexical-redo.md`
— Dan 1 cleared, Dan 8 confirmed untouched, waiting on the researcher's own regenerated lexical
methodology). This session is a separate, later piece of work the same day: a design/build session
on the debate schema's structural integrity, not analytical debate content.

## What happened, in sequence

1. **Researcher's own live discovery, not this app's own tooling:** the debate schema "is not
   complete... does not provide for forward and backward traceability, relies on text scan, does
   not capture all the data of the debate... many to many index tables missing." Investigated
   against the live DB (`PRAGMA foreign_key_list`/`index_list`) and the live writer code
   (`handlers/operations.py`), not doc text — confirmed real: zero FK constraints, zero indexes, on
   all 10 debate tables, despite `cfg_column.fk`/`cfg_unique` already declaring the correct rules.
   Findings filed: `debate-schema-traceability-gap-findings-20260807.md`.

2. **Researcher widened scope (a-l):** every table in the app, not just debate; retrofit real FKs
   app-wide with genuine forward/backward traceability; update configs/schema definitions for every
   change; minimize text-scan/lookups; deploy indexes for scale ("record counts will increase
   exponentially"); fix all joins/CRUD/validations; review whether the JSON-payload reconciliation
   mechanism was itself hiding DB deficiencies; cascade guards on ALL table CRUD, not just `hib.set`;
   re-review for remaining gaps; hold the work to "best efforts... fit for purpose," not a patch;
   update the technical reference, user guide, BUILD, and GOVERNANCE docs.

3. **Root cause found by reading the code, not assumed:** `lib/db.py:build_data_tables()` — this
   app's own generic, config-driven table builder — already emitted real FK/UNIQUE DDL from
   `cfg_column`/`cfg_unique` for every table built through it (confirmed: `word_strong`, `span`,
   `strong_verse`, etc. all had real FKs already). The debate tables and two lexicon tables
   (`verse_lexical`, `strong_meaning_parsed`/`strong_meaning_tree`) were instead built by
   hand-written, one-off migration DDL that bypassed this builder entirely — while still inserting
   the *correct* `cfg_column.fk`/`cfg_unique` rows the builder would have read correctly, had it
   been used. Not a design tradeoff: a build-vs-config conformance bug.

4. **A second, deeper bug found only by trying the fix, not by inspection alone:**
   `build_data_tables()`'s own UNIQUE emission was wrong for any table with a `deleted` column — a
   plain table-level `UNIQUE(...)` collides with this app's own soft-delete-and-reconcile
   convention the first time a row is ever corrected. `passage` had already hand-hit and fixed this
   once (`idx_passage_range_live`, a partial unique index) by bypassing the builder rather than the
   builder knowing the rule. Retrofitting `verse_lexical` hit the live version: 593 natural keys
   already carried one live row plus soft-deleted rebuild-history predecessors — a plain UNIQUE
   would have hard-failed on data already there. Fixed at the root in `lib/db.py:table_ddl()` (new,
   the one place this DDL logic now lives): a partial unique index (`WHERE deleted=0`) for any
   table with `deleted`, plain inline UNIQUE otherwise.

5. **Built `cfg_index`** — a new, app-wide, config-governed mechanism for plain secondary indexes
   (a gap in the builder itself: SQLite doesn't auto-index FK columns, and `build_data_tables()` had
   never had any mechanism for one at all, on any table). `Cfg.indexes()`, an emission step in
   `build_data_tables()`, and `populate_cfg_index_rows.py` (re-runnable) — 42 index definitions
   materialized across 27 tables app-wide, one composite `(fk_col, deleted)` index per live FK
   column, not just the debate tables.

6. **Retrofitted all 13 non-conformant tables**, dependency order, real FK + partial-unique +
   indexes: `hib` → `hib_referent_option`/`verse_hib` → `phenomenon` → `operation` →
   `operation_party` → the four Step-7 closing tables → `verse_lexical` →
   `strong_meaning_parsed`/`strong_meaning_tree`. Method: SQLite has no `ALTER TABLE ... ADD
   CONSTRAINT`, so each table was rebuilt as `{table}__retrofit`, every row copied across, row
   count and `PRAGMA foreign_key_check` verified, then swapped in — one table per transaction, DB
   snapshotted first (`iba-20260807T155245Z-schema-remediation-pre-fk-retrofit-20260.db`). Two
   *expected*, documented exceptions accepted, not gated: 3 `verse_lexical` rows with
   `status='unregistered'` (a real, pre-existing, by-design coverage gap) and 2,380/2,182
   `strong_meaning_parsed`/`strong_meaning_tree` rows referencing a not-yet-onboarded Strong's
   number (bulk reference data ahead of onboarding, same principle as
   `governance.verse_gap_by_design`, table-grain instead of row-grain).

7. **Closed the one genuinely missing many-to-many link** (Finding 2): `operation_party.hib_id`
   (new nullable FK → `hib.id`) — an operation's source/target party, when it IS a previously-
   registered HIB, had only a free-text `detail` gloss (checked live: only 3 of 42 distinct `detail`
   values matched a `hib.label` even as text). Backfilled 4 exact-label matches; `operation.set`'s
   payload contract gained an optional `hib_label` per party, resolved and folded into the
   operation's own reconciliation content so a party-link correction now registers as a real
   `changed` item.

8. **Found and fixed the same orphaning bug in three places, not just `hib.set`** (item h):
   `hib.set`/`phenomenon.set`/`operation.set` each soft-deleted-and-reinserted a `changed` item
   under a brand new id — silently orphaning any already-written downstream row. `passage.py` had
   already hit and fixed the identical problem for its own scope (§67: update in place, same id) —
   never generalised to the debate writers built alongside it. Applied identically to all three:
   `changed` now updates the parent row in place (id preserved); a genuinely new guard refuses a
   `removed` item outright (`hib-has-dependent-phenomena` / `phenomenon-has-dependent-operations` /
   `operation-has-dependent-linkage`) while a live dependent still exists, rather than the old
   silent orphan.

9. **Investigated item (g)** — the JSON-payload mechanism is a batch-input artifact (same shape as
   the main programme's `apply_session_patch.py`), not a second store of state; the real duplication
   was `_reconcile()` re-deriving in Python what a correctly-built DB gives for free. That's what
   this retrofit actually closes — `_reconcile()` keeps doing what only it can do (deciding whether
   a change is justified, recording why); the DB now backs the structural half on its own.

10. **Verified, not assumed:** every retrofitted table's row count unchanged vs. the pre-change
    snapshot; `PRAGMA foreign_key_check` clean on all 13 (documented exceptions aside);
    `configmaint`'s own hard-coherence check (`_validate_live`) clean — including two
    self-inflicted `cfg_index` self-description errors (3-column composite PK, an invalid FK
    target) caught by running the check on this session's own work and fixed before calling it
    done; `operations.py`/`db.py`/`cfg.py` import cleanly; the party-content `None`-vs-`int`
    `hib_id` sort was unit-tested directly. No live `hib.set`/`phenomenon.set`/`operation.set` call
    was made against real Daniel data as part of verification — checked structurally, never by
    writing a fabricated correction into production analytical data.

11. **Requested by the researcher, produced separately:** a full data listing of the `hib` table
    family with the retrofitted linkage chain shown explicitly, so the fix could be checked by eye
    against real data, not just trusted. Confirmed live: 7 of 8 HIBs fully covered through
    phenomenon→operation (1:1, matches the completeness gate); "Daniel" (added a day later than the
    rest) correctly shows 0 phenomena — a real, visible gap, not a hidden one; the new
    `operation_party.hib_id` backfill produced a verifiable mirror pair (Dan.8.24's two HIBs citing
    each other as source/target, now traceable by id both directions); 5 remaining unlinked human
    parties confirmed to be genuine descriptive prose, not exact label matches — correctly left
    unlinked rather than fabricated. Filed: `hib-linkage-verification-20260807.md`.

## Explicitly not done, not defaulted on

- **`cfg_*` config tables (23 of them) were not retrofitted** — a different reference-integrity
  problem (config-to-code, several legitimately reference not-yet-built targets during a pending
  `configmaint.propose` approval), already served by `lib/cfgquality.py`'s orphan-detectors. A
  recorded scoping decision, not an oversight.
- **Pre-existing FK violations in tables this session never touched were surfaced, not fixed:**
  `word_strong` (29), `span` (210,612), `span_candidate` (83,914), `strong_related` (4),
  `escalation` (27) — all pre-dating this session (these tables already had real FKs before today).
  The `span`/`span_candidate`/`word_strong`/`strong_related` scale matches `lib/db.py`'s own
  long-standing comment ("the raw model references before its referent") — reference data ahead of
  onboarding, the same principle accepted for the lexicon tables, at much larger systemic scale.
  `escalation`'s 27 `run_id` orphans look like a smaller, genuinely separate question, not
  investigated further. Named so a future pass starts from a real number.
- **`PRAGMA foreign_keys` runtime enforcement stays OFF, app-wide** — matching the existing
  convention. The retrofitted FKs are declarative/audit-checkable, same as every FK this app
  already had; real-time rejection of a bad reference still comes from each writer's own existence
  checks, unchanged in their own right. Flipping enforcement on is a separate, larger,
  cross-cutting decision this session did not make.
- **The 5 remaining text-only `operation_party` human parties were not force-linked** — genuine
  future work (an explicit `hib_label` added on a future `operation.set` correction), not something
  to guess at from prose.

## Files touched

`lib/db.py` (`table_ddl()` extracted + UNIQUE/index emission fixed), `lib/cfg.py` (`Cfg.indexes()`,
`cfg_index` added to `_VERSION_TABLES`), `handlers/operations.py` (cascade guards + update-in-place
on `hib.set`/`phenomenon.set`/`operation.set`, `operation_party.hib_id` wiring). New:
`migration/build_cfg_index_table.py`, `migration/fix_cfg_column_fk_gaps.py`,
`migration/populate_cfg_index_rows.py`, `migration/retrofit_debate_lexicon_tables.py`. Docs updated
in the same unit of work: `BUILD.md` §79, `GOVERNANCE.md` §33, `USER-GUIDE.md` §12b addendum,
`iba/app/reports/debate-pipeline-technical-reference-20260806.md` (4th pass, plus one corrected
live `cfg_method_rule` row whose text had gone factually wrong the moment the new mechanism was
built). Reports: `debate-schema-traceability-gap-findings-20260807.md`,
`debate-schema-remediation-design-20260807.md`, `hib-linkage-verification-20260807.md`.

## Next

Researcher directed: clear, then run Dan 1 fresh — the actual analytical debate work this design
session's schema fix now underpins. That is the next unit of work, not part of this one.
