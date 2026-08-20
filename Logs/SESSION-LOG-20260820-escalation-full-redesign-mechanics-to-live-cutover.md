# Session log — escalation: mechanics investigation to full redesign, live (2026-08-18 → 2026-08-20)

Three-day arc, one continuous thread: a real data-loss incident on escalation `#715` led to a full
mechanics investigation, three rounds of researcher-reviewed redesign, one failed cutover attempt
(rolled back same day), a governing-principle correction, and a second cutover that succeeded and
is now live and in daily use. Closing this thread at the researcher's request — full detail lives
in the documents/BUILD.md sections named throughout; this is the connecting narrative.

## 1. Trigger — `#715`'s updates silently lost (2026-08-18)

A system crash mid-session. On restart, the researcher reported having typed 30–60 `Escalation.ps1`
commands updating escalation `#715` (an operational-behaviour cfg design discussion) with no trace
of any of it. Investigated rather than assumed:

- Confirmed the DB held exactly **one** answer for `#715` — no more.
- Confirmed the escalation table had **no history/audit mechanism of any kind** — `comment`,
  `next_action`, `answered_by`, `resolution` were single mutable fields, overwritten on every write.
- Confirmed PowerShell's own command history (`PSReadLine`) doesn't capture anything run through the
  Claude Code tool interface — a dead end for recovery.
- Root-caused precisely: once an item reached `in-progress` (which happens on its first answer), a
  2026-08-17 auto-resume fix only covered `on-hold`/`re-assign`, not `in-progress` — every repeat
  `AnswerRun` call after that silently failed with "no pending escalation," nothing persisted.
- Researcher decision: don't chase recovery — redesign the mechanism itself. *"It is not intended
  to log standard method runs... escalation is where errors and issues, and building tasks are
  managed."*

## 2. Full mechanics investigation

[`iba/docs/escalation-system-mechanics-20260818.md`](../iba/docs/escalation-system-mechanics-20260818.md)
— every transaction type, every state, every `cfg_write_grant`/`cfg_escalation` rule, and the honest
finding that only 3 of `cfg_escalation`'s 7 rules were mechanically enforced; the rest self-declared
"session practice only." Also found real, working audit infrastructure elsewhere (`cfg_change_detail`,
277 rows) that was never extended to cover `escalation` itself.

## 3. Three researcher review rounds → plan v3

- **v1** ([archive](../iba/docs/archive/escalation-redesign-plan-v1-20260818.md)): proposed
  `escalation` (current state) + `escalation_history` (append-only) split, column-by-column
  redefinition, revised state machine.
- **v2** ([archive](../iba/docs/archive/escalation-redesign-plan-v2-20260819.md)): the researcher's
  major simplification — *"in principle there are only two transaction types... the resulting state
  is determined by the values in the fields."* Collapsed ten actions to `Raise`/`Update`.
- **v3** ([current](../iba/docs/escalation-redesign-plan-v3-20260819.md)): the two-stage approval
  (`ready_for_approval` → `approved`, producing two real history rows), `re-assign` renamed
  `re-assigned` and made auto-triggered, `reject`'s ambiguity resolved (party explicitly chooses
  `withdraw`/`supersede`), notification resolved as chat-only for now, approval authority resolved
  as contextual (Claude may complete its own low-judgement fixes).

## 4. First cutover attempt — broke live dispatch, rolled back same day

Ran the schema cutover exactly as designed (rename to `escalations_old`, build the new tables,
re-raise the 4 genuinely open items). `configmaint.validate` broke on the very next real dispatch:
the new design had dropped `run_id` (needed to correlate a dispatcher-tied pause to the exact
pipeline execution it belongs to) and retired the `approve`/`hold` vocabulary that 7+ live handlers
branch on directly — neither case had come up across three rounds scoped entirely around the manual
researcher/Claude workflow. Rolled back within the same session, verified restored (722/722 rows,
spot-checked against a pre-migration JSON snapshot), pipeline dispatch confirmed working again
before reporting back. Full record: `BUILD.md` §152.

## 5. The governing correction that unblocked it

Researcher's diagnosis, put to the numbers: `configmaint.propose` (307) + `registry.create` (180) +
`configmaint.validate` (84) = **571 of 723 rows (79%)** were routine pipeline plumbing, not genuine
errors — proven by self-test rows sitting in the same table as real crashes. The actual line:
**config writes are development/design controls and correctly keep a real, gated approval; a
standard operational routine run through an already-approved app script needs no approval
mechanism at all — the engine logs it, only errors escalate.** Applied immediately and concretely to
`registry.create`: its long-questioned per-word Yes/No approval gate is now **retired outright** —
a new word is created and logged straight through (`handlers/registry.py`, `BUILD.md` §153).

## 6. Second cutover — succeeded, live, verified end to end

**Two shapes, two vocabularies, one mechanism** — dispatcher-tied items (config writes,
quality-check findings) keep `run_id` correlation and the unchanged `approve/reject/revise/hold/
noted` vocabulary; manual items use the new `ready_for_approval/approved/reject/revise/noted/
review` vocabulary and the two-stage approval. Both write through one shared full-snapshot
mechanism, so both get real append-only history for the first time. `lib/escalation.py` fully
rewritten, `run.py`'s 3 direct writes + `module_blocking` query updated,
`migration/escalation_redesign_v2_20260820.py` run clean. Live-verified, not just compiled: a real
`configmaint.validate` dispatch paused, answered, produced two real history rows — the exact
capability `#715` lost. `BUILD.md` §154.

## 7. Follow-ups — registered through the new system itself, then closed

Every loose end from the build was raised as its own item through the now-live mechanism
(escalations `#743`–`#750`) — using it to track fixing itself. Worked in the researcher's stated
order:

- **`#745`** — real gap, not cosmetic: `cfg_write_grant` had no row for `escalation_history` at all;
  every write bypassed the grant check. Fixed at the root (`_grant_both()` now checks both tables
  explicitly).
- **`#743`** — building the PS wrapper surfaced that the old `Edit`/`Pause`/`Resume`/`Retract`/
  `Reassign`/`Complete`/`Answer` actions were silently no-op-ing (calling Python verbs the rewrite
  had removed). `Escalation.ps1` fully rewritten: `List`/`AnswerRun` unchanged, `Raise`/`Update`
  new, `History` new. A real bug caught live during the build — `escalation_history.answered_at`
  written `NULL` at Raise — fixed before the researcher could hit it.
- **`#747`** — the deep-history report wired to both the CLI and the PS front door.
- **`#744`** — `USER-GUIDE.md` §4 rewritten wholesale for the live two-vocabulary model.

`BUILD.md` §155.

## Open at close

- **`#746`** — `cfg_escalation`'s 7 rules (still describe the pre-redesign mechanism) — researcher
  reviewing directly before responding.
- **`#748`** — `#735`'s 2 orphan-config findings, orphaned in `escalations_old`, needs a fresh live
  run.
- **`#749`** — formal closure note for `escalations_old #677` (confirmed superseded, never
  formally closed pending the redesign landing — it now has).
- **`#750`** — `cfg_write_grant`'s `(writer='run', table_name='escalation')` row is now dead code.
- **4 carried-over items** (`#736`–`739`, ex-`#650`/`#654`/`#668`/`#725`) — unchanged since the
  cutover, the researcher's own backlog, not part of this thread.

## Files (this session's material changes)

`iba/app/lib/escalation.py` (full rewrite), `iba/app/ps/Escalation.ps1` (full rewrite),
`iba/app/run.py`, `iba/app/handlers/registry.py`, `iba/app/GOVERNANCE.md`, `iba/app/USER-GUIDE.md`,
`iba/app/BUILD.md` (§152–155), `iba/app/migration/escalation_redesign_v1_20260819.py` +
`_ROLLBACK.py`, `iba/app/migration/escalation_redesign_v2_20260820.py`,
`iba/app/migration/fix_escalation_history_write_grant_20260820.py`,
`iba/docs/escalation-system-mechanics-20260818.md`,
`iba/docs/escalation-redesign-plan-v3-20260819.md` (+ v1/v2 archived),
`iba/app/reports/archive/escalation-table-snapshot-pre-redesign-20260819.json` (safety snapshot).
