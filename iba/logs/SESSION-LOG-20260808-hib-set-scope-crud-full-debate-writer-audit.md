# SESSION LOG — 2026-08-08 — `hib.set` scope/CRUD redesign, extended to a full-CRUD audit of every debate writer, a real data-integrity bug found and repaired

Continuation of the prior day's `Debate-Run.ps1`/`hib.set` work (§78-81 lineage). This session
started as a Dan 2 Step 1 (HIB) run, surfaced a real design problem in `hib.set` itself, and grew —
on direct researcher instruction — into a full-CRUD audit and repair of all five debate writers.

## What happened, in sequence

1. **Attempted Dan 2's Step 1 HIB read**, drafted by hand against the lexical
   (`dan-2-hib-step1-draft-20260808.md`), then asked to reconcile the session's own work against
   `debate-pipeline-technical-reference-20260806.md` — confirmed aligned on the analytical method,
   but the reconciliation itself surfaced that hand-building `hib.set`'s payload required
   reconstructing the ENTIRE book's HIB register (union verse sets, ascending order, repeating every
   untouched Dan 1/8 HIB verbatim) just to add Dan 2's own content.

2. **Researcher's four corrections, worked through plan mode, several rounds:** (a) no
   separate "identify then mechanically build" step — one governed step only; (b) confirm
   `cfg_step.scope='book'` isn't itself forcing book-wide reads — checked directly against
   `run.py`: it's read once at dispatch and never branched on again, inert metadata; the real
   cause was hard-coded SQL inside `hib_set` itself (`WHERE book=?`, no chapter filter),
   inconsistent with `phenomenon.set`/`operation.set`/`closing.set`, which are all genuinely
   passage-scoped; (c) full CRUD required, "a new run does not mean soft delete all the HIB
   entries and recreate"; (d) no intermediate mechanically-generated JSON — once (a)-(c) hold,
   there's nothing left to build in a separate pass. Full design record:
   `PLAN-revise-hib-set-scope-and-crud-v1-20260808.md` (plan-mode artifact).

3. **`hib.set` revised in place** (same `cfg_step` row, rewritten payload contract and body):
   payload now scope-only (`-Chapters`/`-Range`'s own verses, never book-wide); new
   `out-of-scope-verse` control; matching stays book-wide BY LABEL (so "Daniel" extending from
   Dan 1 into Dan 2 resolves to the SAME row) but the reconciliation completeness check is
   scope-limited (a book HIB with no footprint in this call's scope is never pulled in); real
   per-verse CRUD on `verse_hib` (insert only new links, delete only genuinely dropped ones);
   `first_verse_id` recomputed by canonical `(chapter, verse)` order, never array position
   (`verse.id` confirmed to have no relationship to reading order). New `hib_change_detail` audit
   table (later renamed, see below), mirroring `cfg_change_detail`'s shape.

4. **Verified live**, not assumed: Dan 1 scope-only resubmit → `8 unchanged, 0 new, 0 corrected,
   0 removed in this scope`, Dan 8's HIBs never mentioned, 0 audit rows written. Dan 2 scope-only
   payload (5 extends of existing Dan 1/8 HIBs, 6 new) → ids `47/48/52/53/54` preserved (no
   duplicates), 115 verse-links added, Daniel's live `verse_hib` count = 69 = 33 pre-existing + 36
   new, exact match. **Bonus finding**: the new canonical-order recompute caught and
   self-corrected a real pre-existing bug — Daniel's stored `first_verse_id` was `Dan.8.1`, not
   `Dan.1.6` (an artifact of the old "payload's first array element" logic) — one `hib` `update`,
   logged with full before/after.

5. **Researcher directed "proceed with fixing the CRUD" the same session** (escalation
   `MANUAL-20260808_042042_515014`, "full CRUD is required for all table update controls") —
   extended the treatment to every remaining debate writer, not just `hib.set`. Renamed
   `hib_change_detail` → `debate_change_detail` before extending it (about to hold rows for every
   writer, not just `hib.set` — same rename-on-outgrown-name precedent as `span_reading` →
   `verse_lexical`); gained a `writer` column (`run_id` alone can't identify which step made a
   given row, since `Debate-Run.ps1` reuses one `run_id` across its whole sequence); logging
   centralised into `lib/debateaudit.py:log_change`, called by all 5 writers.

6. **`passage.build`/`phenomenon.set` audited first, found already correct** — both already
   updated existing rows in place on a correction (from earlier fixes, §78/§80 lineage); only
   needed the audit trail added, no logic change.

7. **`operation.set`: `operation` already correct; `operation_party` upgraded** from
   soft-delete-and-reinsert-under-a-changed-parent (the exact §33-flagged exception) to real
   per-row CRUD by ordinal position. **A real counting bug caught by the isolated-copy test
   before it shipped**: `n_party` incremented unconditionally at the end of every position's loop,
   including untouched ("same") positions — a hand-verified 1-party edit reported "3 party
   record(s) written" against only 1 real audit row. Fixed; re-verified exact match.

8. **`hib_referent_option` upgraded the same way** (positional CRUD by `ordinal`) — verified
   live-copy: insert 2 options for Belshazzar (previously option-less) → edit one, drop the
   other → the kept option's id preserved, the dropped one correctly soft-deleted, exactly 1
   update + 1 delete logged.

9. **`closing.set`: a real bug found, not just a missing audit trail.** All four list tables
   (`passage_linkage`/`passage_insufficiency`/`passage_emergent_question`/`passage_validation_note`)
   were soft-deleting and reinserting under a NEW id for `changed` items — the same antipattern
   the other three writers already had fixed, missed because §33's original sweep only reached
   the operations-schema writers. Rewritten to real per-ordinal CRUD. Verified live (Dan 1's real
   closing content, all correctly unchanged) and isolated-copy (a real linkage-note correction:
   id preserved, exactly one `update` row logged).

10. **A separate, real gap found while testing:** `Operations-Ingest.ps1` never had `closing.set`
    in its own `-ValidateSet`, even though `cfg_step` had it registered and `Debate-Run.ps1`
    reached it fine (calls the dispatcher directly, bypassing this wrapper's validation).
    `closing.set` was unreachable via direct/manual invocation this whole time. Fixed — added to
    `-ValidateSet`, `.DESCRIPTION`, a new `.EXAMPLE`; verified live.

11. **A real, pre-existing data-integrity bug found as a side effect of the `operation.set` no-op
    regression test — reported, not silently patched.** All 17 of Dan 8 passage 37465's
    `phenomenon` rows for "Daniel" referenced `hib_id=22`, a soft-deleted row — not the live
    Daniel (`hib_id=47`). Residue from an older `hib.set` correction, before the 2026-08-07
    update-in-place fix, that changed Daniel's id without repointing the phenomena already
    written against the old one. Dan 1 had no equivalent issue; `operation_party.hib_id` had zero
    orphaned references anywhere. Escalation `MANUAL-20260808_052156_904168` raised with the
    finding and a recommended fix — **not applied without the researcher's decision**, since this
    touches real analytical content, not just mechanism.

12. **Config housekeeping, same session:** `lib/debateaudit.py` registered in `cfg_utility` and
    marked `config_exempt` (pure DB-write helper, no `cfg.setting()`/`cfg.enum()` usage by
    design); `GOVERNANCE.md` §34 added (the shared audit table, the id-preservation rule extended
    to child tables); resolved two `configmaint.validate` stale-doc advisories along the way
    (coarse mtime comparison, not real gaps).

13. **Escalation `MANUAL-20260808_052156_904168` answered `approve`, "repair now."** Applied via
    `migration/repair_dan8_daniel_phenomenon_hib_id_20260808.py` — idempotent, audited (17 rows
    repointed 22→47, each logged to `debate_change_detail` under
    `writer='repair.dan8_daniel_hib_id'`; re-run confirmed no-op). Verified: all 8 Dan 8 HIBs,
    Daniel included, now resolve to live `hib` rows with no exceptions.

14. **`Escalation.ps1 -Action List` confirmed 0 open** at the close of this session — every
    escalation raised (2 substantive, 3 `configmaint.validate` advisories along the way) answered
    and, where applicable, actually acted on, not just marked answered.

## Explicitly not done, not defaulted on

- **No live production data was ever touched by a correction test** — every non-trivial CRUD
  verification (insert, update, delete, the Belshazzar referent-option cycle, the closing.set
  linkage edit) ran against an isolated scratch copy of `iba.db`, discarded after use. Only safe
  no-op regressions (content matches exactly → zero writes, by construction) ran against live
  data.
- **The orphaned-hib_id repair was not applied on discovery** — reported as its own escalation,
  separate from the CRUD-mechanism work, and only applied once explicitly answered `approve`.
- **Dan 2's actual Step 1 HIB payload was not re-submitted this session** — the draft
  (`dan-2-hib-step1-draft-20260808.md`) and the six flagged judgment calls (JC1-JC6) it carries
  are still open; this session's work was entirely about the mechanism `hib.set` runs on, not
  about closing out Dan 2's own analytical content. That's next.

## Files touched

`handlers/operations.py` (`hib_set` rewritten; `phenomenon_set`/`operation_set`/`closing_set` gain
`_log_change` calls; `operation_set`'s `operation_party` and `hib_set`'s `hib_referent_option`
block rewritten to positional CRUD), `handlers/passage.py` (`_log_change` calls added;
`_retire_legacy_passage` helper factored out), `lib/debateaudit.py` (new, shared audit-log
function), `ps/Operations-Ingest.ps1` (`hib.set` now scope-required; `closing.set` added to
`-ValidateSet`/docs). New migrations:
`migration/build_hib_change_detail_table_20260808.py`,
`migration/rename_hib_change_detail_to_debate_change_detail_20260808.py`,
`migration/add_debate_change_detail_writer_column_20260808.py`,
`migration/repair_dan8_daniel_phenomenon_hib_id_20260808.py`. Docs updated in the same unit of
work: `BUILD.md` §81/§82, `GOVERNANCE.md` §34. Config: 5 `cfg_write_grant` rows (one per writer →
`debate_change_detail`), `cfg_utility.debateaudit` registered + marked exempt — all via
`configmaint.propose`, approved per row. Payloads/reports:
`staging/operations/dan-1-hib.set.json` (rewritten scope-only), `staging/operations/
dan-2-hib.set.json`, various `-noop-test.json`/isolated-copy scratch payloads (not committed —
scratch-directory artifacts), `hib-set-reconciliation-*`, `phenomenon-set-reconciliation-*`,
`operation-set-reconciliation-*`, `closing-set-reconciliation-*` (2026-08-08 dated, various `-vN`).

## Next

Researcher directed: clear, then proceed with Dan 2 — the actual analytical debate work this
session's mechanism fix now underpins. `dan-2-hib-step1-draft-20260808.md`'s six flagged judgment
calls (JC1-JC6) are the starting point once resumed. That is the next unit of work, not part of
this one.
