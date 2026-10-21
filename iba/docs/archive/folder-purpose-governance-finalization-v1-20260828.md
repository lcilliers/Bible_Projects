# Folder-purpose governance — finalization & ready-for-approval (v1)

> Closing report for escalation #971's main build phase (`folder-purpose-governance-plan-v5-
> 20260828.md` and the work that followed it, same day). Written per the researcher's instruction:
> *"prepare the current proposal for finalisation and ready for approval to process all the
> underlying builds... very large and need careful back checking to ensure everything is covered
> and any open items are properly spawned into separate escalations to ensure that it is not
> missed."* This document is the back-check: a complete inventory of what was built, what's
> verified, and every open item's own tracked escalation — nothing left as a loose note in chat or
> a BUILD.md aside.

## 1. What was built (verified working, live)

| Piece | What | Verified |
|---|---|---|
| `folder_purpose` table | 793 rows, one per folder, full census | `type`/`status` complete on all 793 (0 missing) |
| Method A (`-Action Seed`) | Reconciles against the live tree | Run repeatedly this session, idempotent |
| Method B (`-Action CrossCheck`) | Syncs `governed_by_setting` from `cfg_setting` + every per-module table shaped like it (`cfg_prose`, `cfg_passage`, discovered live) | 23 rows governed, 0 anomalies on the last run |
| Method C (`-Action Set/List/Show`) | Hand-editor for `type`/`status`/`usage_description` | Used to classify the 5 rows Method D left uncertain |
| Method D (`-Action AutoAssess`) | Fills `type`/`status` from Methods A/B's own facts, never guesses `mixed`/`reallocate` | 766/774 filled automatically; last 5 reviewed by hand |
| `manifest.py` wiring | Reads `folder_purpose.manifest_category`/`manifest_currency` first, hardcoded rules as fallback | `file_manifest`'s `other` bucket: 9,064 → **170** (98% reduction) |
| `path-audit` utility | Project-wide hardcoded-location-literal scanner, excludes only `cfg_utility.inactive=1` scripts | 84 → 83 scripts (after retiring one dead one), final: **16 findings, 2 files**, all reviewed |
| Config fixes | `cfg_prose.prose.edit_file_dir` corrected; 4 new `cfg_prose.*_output_dir` settings registered | Applied, `configmaint.validate` clean of both |
| Script fixes | `prosestore.py`'s 4 remaining hardcoded constants converted to cfg-driven accessors; `word_strong_span_report.py` retired (`inactive=1`) rather than patched (dead code) | Re-scanned, both confirmed |
| `file_manifest` + `folder_purpose` `cfg_table`/`cfg_column` registration | Closed a real `governance.tables` compliance gap found mid-build | Registered, `configmaint.validate` clean |
| `configmaint.validate` — location check | New standing check: every location-shaped config value must resolve to a real folder | Live, catches drift automatically going forward (proved on `prose.edit_file_dir` and `prose.patch_output_dir`, both real) |
| `filing` behaviour class + 5 rules | Naming shape, snapshot-vs-living, archiving trigger, Claude Code obligations, tool-report-vs-deliverable-document | Registered |

**`configmaint.validate` is clean** as of the last run this session — no orphans, no unresolved
locations, no stale docs, no coherence errors.

## 2. Full escalation inventory (#970–#992) — nothing untracked

**Completed (15):** #970, #972, #973, #974, #975, #978, #979, #980, #981, #982, #983, #984, #987,
#988 — CLI-crash self-corrections and researcher-approved config/data fixes, all closed.

**Withdrawn as duplicates (3):** #986, #990, #991 — all the same `prose.patch_output_dir` finding
`configmaint.validate` kept re-raising on successive runs; consolidated into #989 rather than left
as 4 near-identical items.

**Still open, each with its own tracked escalation — this is the "spawned, not missed" list:**

| # | What it's for | State | Assigned |
|---|---|---|---|
| **#971** | This mechanism itself — final sign-off | re-assigned | Researcher |
| **#972** | (completed, ready_for_approval — awaiting your acknowledgement to close) | completed | Researcher |
| **#976** | 2 candidates: plan-doc-series refiling scope/timing; `_analytics/Bible_Books` vs `_analytics/bible_books` casing | in-progress | Researcher |
| **#977** | **Unresolved — see §3 below.** Your "revise" instruction on the enum-registration fix, not yet actually answered | in-progress | Claude |
| **#985** | GOVERNANCE.md brought current — ready for your acknowledgement | re-assigned | Researcher |
| **#989** | Prose output locations need to be book/cluster-aware, not flat — approved by you this round as the container for that follow-on work, not yet started | raised | Researcher |
| **#992** | `filingkit.versioned_path()` + naming-drift check — carried from #863/#971 Part A, never had its own escalation until this back-check caught it | raised | Researcher |

## 3. #977 — genuinely still open, needs your decision (not resolved by guessing)

Your comment: *"not approved. hard coded with configs to set rules in against governance -
revise."* I asked a clarifying question in chat; the conversation moved to the prose/folder_purpose
work before you answered it, so it's still sitting open. Restating it plainly here so it isn't lost
in the finalization: does "hard coded with configs" mean —

**(a)** the `folder_purpose_type`/`folder_purpose_status` `cfg_enum` *values* themselves
(`archive`/`operations`/`results`, `authoritative`/`mixed`/`reallocate`/`stale`/`deleted`) should
have gone through `Config-Maintenance.ps1 -Step Propose` rather than the direct migration-bootstrap
pattern (`folder_purpose_build_v1_20260828.py`) — the same pattern `bootstrap_file_manifest.py` and
every other new-module registration in this codebase uses; or

**(b)** the validation *rule itself* — "a `folder_purpose` row's `type`/`status` must match the live
`cfg_enum`" — needs its own visible governance entry (a `cfg_behaviour_rule` or a `GOVERNANCE.md`
line), not just a bare `cfg.enum()` call sitting inside `folderpurpose.py` with no governance-facing
documentation;

or something else entirely. Whichever it is, it's a real fix, not guessed at here — waiting on your
read before I touch it again.

## 4. What's explicitly NOT done, and where it's tracked

- **#976** — no physical file has moved yet (plan-doc refiling, casing fix) — deliberately, per the
  original phased design (planning vs. execution split).
- **#989** — prose output locations are still flat (Programme-only in practice); not redesigned.
  `prose.patch_output_dir` stays at its current (admittedly wrong for non-Programme books) value.
- **#992** — `filingkit.versioned_path()` doesn't exist yet; `oneoff_path()` is still the only
  caller with real versioning/archiving.
- **#977** — the enum-registration question above.
- `docs/`'s own 36-flat-file pattern (#971's original item 1) — `folder_purpose` now has a row for
  `docs/` like any other folder (`type`/`status` filled by Method D), but no physical
  reorganisation has happened — same "planning done, execution not" split as #976, and would fold
  into that escalation's worklist rather than needing a fifth one.

## 5. Requested: approval to close this batch

Everything in §1 is built, wired, and verified live. §2's table is the complete map of what's still
open and where. Nothing found during this build was left as a bare comment or a chat aside without
a tracked escalation — that was the point of this pass. Ready for your review; once #971/#972/#985
are acknowledged closed, the natural next steps are the four spawned escalations in whatever order
you want to take them (#976 execution, #977's decision, #989's redesign, #992's build) — each
already has enough context recorded to pick up cold.
