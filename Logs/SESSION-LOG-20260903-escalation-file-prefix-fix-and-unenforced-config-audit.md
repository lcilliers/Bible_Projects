# Session log — 2026-09-03 (Developer Mode)

**Scope, one line:** Developer Mode session — started as verse-lexical Window 1 enrichment
design/propose (#1383, spawned from #1376), was interrupted by a researcher-caught escalation-
file naming violation (fixed, 26 files renamed + governance rule recorded), which surfaced a much
larger, sharper finding: 44-48 of 64 active `cfg_behaviour_rule` rows were unenforced, hedged, or
silently orphaned (escalation #1384) — a full audit was run, 8 real mechanical checks were built
and wired into `configmaint.validate`/`CONFIG-REPORT.md`/`start-project`, and every one of the
9 resulting judgement calls was worked through to the researcher's actual decision, not left as a
list.

## Escalations touched

| id | outcome this session |
|---|---|
| **#1383** | Raised fresh (spawned from #1376). Design+propose doc filed for verse-lexical Window 1 enrichment (schema, config, glossary), answering #1379's open decisions A–G with grounded recommendations. `decision_required`, awaiting researcher approval — **paused, not resumed this session** once the naming issue and then the config audit took over. |
| **#1384** | Raised fresh. The unenforced-config audit itself: all 64 active `cfg_behaviour_rule` rows individually investigated, `enforcement_status` column built, 8 mechanical checks built and wired in, all 9 resulting judgement calls resolved per the researcher's direct decisions this chat. `in-progress`, `next_action=review`. |
| **#1385** | Raised fresh. `content_index` redesign needed — the 2026-08-17 prototype wrote 14.1M rows and grew `iba.db` to 8GB; `content_index.rebuild` paused (`cfg_step`/`cfg_work_package` `inactive=1`) referencing this escalation. |
| **#1386** | Raised fresh. Obsidian integration not deployed, crashes; `cfg_behaviour_rule` 15 deactivated referencing this escalation. |
| **#1387** | Raised fresh. `USER-GUIDE.md` rewrite — confirmed stale live (last touched 2026-08-28). |
| **#1007** | Corrected (`-Action Correction`, `v22`): rename mapping recorded for 7 tier-catalogue/scope-focus/word-term-lexical files, without rewriting the large historical narrative. |
| **#1376** | Updated (`v2`): rename mapping recorded for its 2 characteristic-tables-cross-db-inventory files. |
| **#1377** | Corrected twice (`v22`, `v23` — the second a self-correction fixing a misattributed note from the first): rename mapping recorded for 9 glossary/vocabulary files + the live `cfg_column.use` fix. |
| **#1379** | Updated (`v8`): rename mapping recorded for its 6 verse-lexical-enrichment/worked-example/checklist files. |
| **#1380** | Corrected (`v4`): stale path in its own `resolution` text fixed to the renamed filename. |

## Files created or changed

**Escalation-file naming fix (26 files renamed, all references updated):** `Workflow/Catalogue/`
(18 files, incl. 6 archived) and `iba/docs/` (3 files) renamed to carry their governing
escalation's id as a filename prefix; every in-doc cross-reference, `iba/app/BUILD.md`, 2 scripts,
and 5 session logs updated in the same pass; 2 live `cfg_column.use` rows (`bible_research.db`
`wa_obs_question_catalogue.scope`/`.source`) fixed for baked-in stale paths. `cfg_behaviour_rule`
id 64 (`escalation-file-carries-escalation-id-prefix`) recorded as the governing rule — corrected
mid-session, on the researcher's direct correction, from "researcher instruction 2026-09-03" to
"stated 2026-09-01" (the original written statement was searched for across `escalation_history`
and every session log and not found — recorded honestly as such).

**Unenforced-config audit (#1384):** `iba/app/db/iba.db` schema — `cfg_behaviour_rule` +1 column
(`enforcement_status`), `cfg_enum` group `behaviour_rule_enforcement_status` +6 values,
`cfg_column` +1 row; all 64 active `cfg_behaviour_rule` rows' `enforcement_status` populated,
~40 rows' `enforced_by` text rewritten from a hedge to a real determination. `iba/app/lib/
cfgquality.py` +8 functions (`find_unenforced_behaviour_rules`, `find_unpushed_commits`,
`find_ps_scripts_bypassing_runpy`, `find_steps_without_ps_script`,
`find_escalation_file_naming_violations`, `find_hedge_phrases_in_active_config`,
`find_restated_authoritative_content`, `find_query_file_convention_violations`; `difflib` import
added). `iba/app/handlers/configmaint.py` (findings dict +8 entries, success message updated).
`iba/app/lib/cfgreport.py` (findings list +8 entries, mirroring `configmaint.validate` — the two
had drifted apart before, fixed together this time). `.claude/commands/start-project.md` (§4/§5 —
`enforcement_status` counts now surfaced every session, `judgment_call_pending` rows named
specifically). `iba/app/BUILD.md` #221/#222.

**9 judgement calls resolved:** `scripts/SQLite/**` — 8 files renamed/relocated (3 flat
`SQLite_`-prefix files moved into `scripts/SQLite/Research_DB/`, 4 space-violations hyphenated, 1
untitled file named); `cfg_step`/`cfg_work_package` `content-index-rebuild` set `inactive=1`;
`cfg_behaviour_rule` rows 3 (rewritten + built), 14 (rewritten + built + violations fixed), 15
(deactivated), 35 (explained, no change), 42 (corrected framing, kept active), 60 (rewritten — a
genuine self-contradiction removed), 61 (simplified per researcher wording).

## Decisions made

**Researcher's own decisions, this chat:** `scripts/SQLite/{IBA_DB,Research_DB}/` is the
authoritative query-file location (not the flat `SQLite_`-prefix form); `content_index` needs a
redesign, current use paused; `single-authority-pointer-not-copy` should be built without
`content_index` if possible; Obsidian needs its own fix escalation, rule deactivated meanwhile;
`user-guide-updated-same-unit-of-work` is not a commit-timing rule, stays active/enforced
regardless of the rewrite's timeline, "not something that is postponed for a later date";
`inactive-tables-never-active-inputs` simplified — inactive state is never included in a report/
result by default, full stop; direct, sharp feedback that Claude has been repeatedly re-engaging
with inactive/historical state unprompted, wasting time — taken as a behavioural correction, not
just logged.

**Claude self-corrected (execution fixes against already-approved direction):** a naive
`quick_ratio()>0.6` duplicate-content check produced ~19,000 unusable false positives — tuned to
full `ratio()>=0.8` with a `quick_ratio()` pre-filter, retested clean; #1377's `v22` correction
note wrongly credited itself with a `cfg_column` fix that actually belonged to #1007 — caught
re-reading the regenerated report, fixed with a `v23` self-correction; the dual-escalation-tag
naming check (`#1378/#1379`-style headers) initially flagged files correctly renamed under
either number — widened to accept any number named in the header, not just the first regex match.

**Left open, not decided:** the paired judgement call `never-write-via-adhoc-tool`/`writes-must-
be-replayable` — raised in #1384's original comment, not addressed in the researcher's reply this
round; still `judgment_call_pending`. `#1385`/`#1386`/`#1387` — raised, not yet actioned.
`consolidation-doc-must-be-load-bearing-or-retired` — explained in chat/BUILD.md, no config change
requested or made.

## Open items carried into next session

1. **#1383 (verse-lexical Window 1 enrichment)** — design+propose filed, awaiting the researcher's
   decisions on open items A–G. Not resumed after the naming/audit work took over this session.
2. **#1384's remaining judgement calls**, everything not resolved above: the `never-write-via-
   adhoc-tool`/`writes-must-be-replayable` pair specifically.
3. **#1385/#1386/#1387** — content_index redesign, Obsidian fix, USER-GUIDE.md rewrite — all
   raised this session, none started.
4. **The pre-#1007 escalation-file-naming backlog** (~25 files in `iba/docs/`, escalations #669/
   #784/#795/#798/#863/#890/#971/#989 and others) — mechanically confirmed via the new
   `find_escalation_file_naming_violations` check, same scope #976 already deferred pending a
   go-ahead. Not executed.
5. **`Behaviour.ps1`'s `run.py` bypass** — confirmed still live (known since 2026-08-21), not
   fixed this session, now mechanically re-detected every `configmaint.validate` run.
6. **Researcher asked to see the unenforced-config report "in action on the next start-project"**
   — `.claude/commands/start-project.md` is wired for this; not yet exercised in a fresh session.

## Git state

Branch: `main`. Commit: `b859438e` (parent `7a13d4fc`). 145 files changed, 16869 insertions(+),
356 deletions(-). Push initially failed (`Could not resolve host: github.com` — sandbox network
restriction in this environment, not a credentials/permission issue); retried with the sandbox
override and succeeded: `7a13d4fc..b859438e main -> main`. Confirmed via `git status`: `On branch
main. Your branch is up to date with 'origin/main'. nothing to commit, working tree clean`.

