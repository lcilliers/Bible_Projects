# Session Log — 2026-09-01 — Catalogue Scope/Source work, obs_catalogue.update tool built, config gaps found and fixed

**Scope:** Continuation session (new conversation after `/clear`). Built the tier-catalogue-to-
IBA-raw-data mapping (corrected after a real miss, twice), built and registered a new
`obs_catalogue.update` write tool with schema migration, classified all 126 live tier questions by
Scope focus (iterated three times on researcher correction), wrote it live into
`wa_obs_question_catalogue.scope`, started the `source`-column work, and produced a full
cross-database inventory of every characteristic/phenomenon-related table plus the programme's own
definition and Model A's real cluster-assignment algorithm. Along the way: found and fixed two
real code bugs in `configmaint.py`/`cfgreport.py`, added retry resilience to the new write tool,
made and caught a real mistake of my own (a resume call with the wrong payload that silently
no-opped), and fixed a repeated process gap (proposals left at `review` instead of pushed to
`ready_for_approval`).

## Escalations touched

| # | Outcome | Notes |
|---|---|---|
| #1007 | **Open** — `review`, assigned Researcher | Main working escalation, v9→v20 this session. Every deliverable below logged against it as produced (a gap from earlier in the day, corrected mid-session per researcher: "you have not added any of your work in the 1007 escalation"). Also corrected a `comment`/`context` field-spec violation on my own v9/v10 updates (links belonged in `context`, cumulative, not buried in `resolution` prose) — fixed going forward via a v11 `context` entry; historical rows are immutable so not rewritten. |
| #1316 | **Open** — `review`, assigned Researcher | Applied (for real, after a first resume attempt used the wrong payload from memory and silently matched zero rows). Verified live. Sitting at `review` because only the researcher can issue the actual close (D25 authority check — tied to whoever a `ready_for_approval` last targeted, not current assignment). |
| #1364 | Completed (self_correctable) | `configmaint.propose`'s approved-resume path had no validation at all, unlike the fresh-proposal path — a malformed resumed payload crashed raw instead of returning a routed `fail()`. Fixed: same `_check_proposal()` gate now runs on both paths. Verified against a scratch DB copy reproducing both of my own real bad calls. |
| #1365 | Completed (self_correctable) | `report.schema_overview`'s utilities table crashed on any `cfg_utility.module = NULL` row (my own bad insert, root-caused as #1364). Fixed: guarded `module`/`file_path` like the other columns already were. Verified live against the real bad row. |
| #1366 | **Open** — `review`, assigned Researcher | Fix `cfg_utility.module` NULL→`schema_overview`. Proposed, pushed to `ready_for_approval`, approved, applied. First apply attempt used the wrong `-Where`/`-Set` (typed from memory, not pulled from the escalation's stored `context`) and silently no-opped while reporting `ok` — caught by checking the actual row afterward, corrected, re-verified live. Sitting at `review`, only the researcher can close (D25). |
| #1367 | Completed (self_correctable) | `configmaint.report` crashed on a locked `cfg_table.csv` (Excel had it open). Not a new defect — same already-diagnosed, by-design retry-then-surface pattern as #1320/#1351/#1356. No code change. |
| #1368–1370 | Completed (self_correctable) | Auto-raised from my own deliberate tests of `obs_catalogue.update`'s validation (obs_id-in-Set, unknown column, nonexistent obs_id) — all three rejected correctly as designed, not defects. |
| #1371, #1372 | Completed (self_correctable) | `database is locked` crashes hit while bulk-testing the new tool. Root-caused and fixed within the same build: added a bounded 3-attempt/0.3s retry to `cataloguewrite.run_update`, same pattern as `reportkit.archive_before_write` (#1320). |
| #1373 | **Open** — `review`, assigned Researcher | `cfg_escalation_requirement.check_kind` has 3 live values with no matching `cfg_enum` row (almost certainly the D25 mechanism). Not a simple add-3-values fix — the enum already has an unused `requires_prior_...` row suggesting a `prior`→`current` rename that never landed. Converted from `self_correctable` to `decision_required` (my own follow-up caught that the conversion hadn't actually reassigned it — fixed that too). Genuine open question for the researcher, not drafted as a ready proposal. |
| #1374 | Withdrawn | Superseded before the researcher acted on it — researcher said the old `scope`-column meaning was "of no real value," so the dual-meaning documentation this proposed was wrong; withdrew and re-proposed as #1375. |
| #1375 | **Open** — `review`, assigned Researcher | Replace `cfg_column.use` for `wa_obs_question_catalogue.scope` with the Scope-focus classification only, dropping the old universal/leviticus description entirely. Proposed, pushed to `ready_for_approval`, approved, applied correctly (pulled the exact stored `context` payload this time, not from memory), verified live. Sitting at `review`, only the researcher can close (D25). |

## Files created / changed

- **`iba/app/migration/add_obs_catalogue_source_last_modified_and_update_tool_v1_20260831.py`** (new) — adds `wa_obs_question_catalogue.source`/`.last_modified` (bible_research.db DDL) and bootstraps the `catalogue-update` work package/step/write-grant/utility rows. Applied, idempotent (re-run clean).
- **`iba/app/lib/cataloguewrite.py`** (new) — `run_update()`, the validated partial-UPDATE logic behind the tool; includes the lock-retry fix from #1371/#1372.
- **`iba/app/handlers/catalogue.py`** (new) — thin dispatcher adapter registering `obs_catalogue.update`.
- **`iba/app/ps/Catalogue-Update.ps1`** (new) — the PS wrapper (`-ObsId`, `-Set`).
- **`iba/app/handlers/configmaint.py`** — resume/apply branch of `propose()` now runs `_check_proposal()` before `_apply()` (root fix, #1364).
- **`iba/app/lib/cfgreport.py`** — `_utilities_table()` guards `module`/`file_path` against NULL (root fix, #1365).
- **`iba/app/BUILD.md`** — §216 added, documenting the schema/tool build in full.
- **`iba/docs/ps tools worksheet.xlsx`** — new `Catalogue-Update` tab + `Index` row (checked not locked in Excel before writing).
- **`database/bible_research.db`** — schema: `wa_obs_question_catalogue.source`/`.last_modified` added. Data: `scope` written for all 126 live T-coded rows (Scope-focus bucket, verified exact match to the doc); `source` written for one test row (`obs_id=224`); `catalogue_version`/`last_modified` auto-stamped on every written row.
- **`Workflow/Catalogue/tier-catalogue-iba-raw-data-mapping-v2-20260831.md`** (live; v1 archived) — for each of the 126 tier questions, whether/how it's answerable from IBA raw data. v1 scored 5 Yes/7 Partial/114 No, requiring a pre-classified field; corrected in v2 after the researcher caught that this missed the whole verse-text/lexical-gloss reading layer — 43 questions moved No→Partial. New totals 5/50/71.
- **`Workflow/Catalogue/tier-catalogue-scope-focus-v3-20260831.md`** (live; v1, v2 archived) — the 126 tier questions grouped by Scope focus (HIB characteristic [3 sub-buckets: word/term-lexical, characteristic-behaviour, characteristic-relational], The HIB, Verse-context, Other non-human beings, The verse, Science). Iterated 3 times on researcher correction: v1→v2 restricted to T-codes, split HIB-characteristic into 3, moved 38 questions to The HIB (faculties/constitutional-architecture); v2→v3 moved T6.4 to lexical, isolated a new 41-question Verse-context bucket by literal wording signal.
- **`Workflow/Catalogue/word-term-lexical-source-v1-20260831.md`** (live, **not yet applied to the DB**) — proposed `source` values for the 16 `Word/term (lexical)` questions, each a direct "derived from…" statement grounded in the raw-data mapping. Awaiting researcher review before writing.
- **`Workflow/Catalogue/characteristic-tables-cross-db-inventory-v2-20260901.md`** (live; v1 archived) — every characteristic/phenomenon-related table in both databases: three distinct, unbridged models (bible_research.db's `characteristic` catalog; `ib_characteristic`'s meaning-keyed book index; `iba.db`'s live `hib`/`phenomenon`/`operation` debate pipeline — "what IBA calls a phenomenon") plus a fully-retired "dimension" layer. v2 adds the programme's own working definition (traced to `programme_prose`), a growing terminology glossary, Model A's actual cluster-assignment algorithm (traced to `clusterassign.py` and its session log — gloss-only precedent matching, HIGH/MEDIUM/LOW tiers, the T3 edge rule), and the researcher's own account of why each model stalled.
- Various auto-generated `CONFIG-REPORT.md`/escalation-list/CSV archive artifacts — routine byproducts of the `configmaint`/`Escalation.ps1` runs this session, not hand-authored.

## Decisions

**Researcher's own decisions:**
- Approved #1366 and #1375's exact proposed changes.
- Corrected the raw-data mapping's methodology (v1→v2: credit reading the base extract, not just pre-classified fields).
- Corrected the Scope classification twice (v1→v2: restrict to T-codes, split HIB-characteristic 3 ways, reclassify faculty/constitutional questions to The HIB; v2→v3: T6.4 to lexical, isolate Verse-context).
- Directed writing the Scope-focus classification into the live `scope` column, then directed replacing (not dual-documenting) its `cfg_column.use` text.
- Provided the programme definition source, the cluster-assignment-logic pointer, and the model-by-model methodology commentary for the characteristic-tables inventory.
- Directed this session log + close.

**Self-correctable fixes Claude made and closed directly** (no researcher decision needed): #1364, #1365, #1367, #1368–1370, #1371–1372.

**Left for the researcher, not self-closed:** #1373 (a genuine open design question, not drafted as a ready proposal); #1316/#1366/#1375 (applied and verified, but the actual close-out action is gated to the researcher by D25, not a judgement call I'm deferring).

**A real mistake, corrected in the open, not smoothed over:** the first #1366 apply used a resume payload typed from memory instead of the escalation's actual stored `context` — it matched zero rows and reported `ok` while fixing nothing. Caught by checking the row, not by trusting the status; the fix (verify the actual row after every apply, always pull stored `context` verbatim on resume) is now standing practice for the rest of the session.

**A repeated process gap, also corrected:** proposals were being left at `review` after raising instead of pushed to `ready_for_approval` — the researcher noted they'd started ignoring items at the ambiguous state as a result. Fixed for the two open items at the time (#1366, #1375) and adopted as standing practice going forward.

## Open items carried into next session

- **#1007** — main thread stays open. Next concrete step: the `word-term-lexical-source-v1` proposal (16 rows) awaiting review before `obs_catalogue.update` writes it. After that, the same `source`-proposal pattern needs repeating for the remaining Scope buckets (characteristic-behaviour, characteristic-relational, The HIB, Verse-context, Other-non-human-beings, Science) — one bucket-doc at a time, per the plan noted in the word-term-lexical doc itself.
- **#1373** — needs the researcher's actual decision (rename the stale enum row vs. add-and-retire) before a proposal can be drafted.
- **#1316, #1366, #1375** — applied and verified; need only the researcher's own close (`-NextAction noted -State completed`), not further Claude work.
- **`characteristic-tables-cross-db-inventory-v2`** — deliberately left at the observation stage per the researcher's own framing; no next step assigned yet, awaiting further direction on how (or whether) the three models get reconciled.

## Git state

Branch `main`, commit `b36b3dbf3780af9c510cb807c6307e74ac492416`, pushed clean:

```
$ git push
To https://github.com/lcilliers/Bible_Projects.git
   836d4c9f..b36b3dbf  main -> main

$ git status
On branch main
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean
```

55 files changed (11,852 insertions, 11 deletions) — the bulk is the new catalogue tool code, the
Catalogue mapping/Scope/inventory deliverables, and auto-generated report/CSV archive artifacts
from the `configmaint`/`Escalation.ps1` runs this session, not hand-authored content.
