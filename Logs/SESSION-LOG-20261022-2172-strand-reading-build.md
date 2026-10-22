# Session log — 2026-10-22 — #2172 reading process built (Strand-Reading.ps1); catch-up plan

Session id: `691d410b-cdfa-4fe4-a9ed-d36cfccc293d` (Developer Mode). Close report:
`iba/app/reports/session-close-v161-20261022.md` (and its re-runs).

## 1. Scope

2026-10-22, Developer Mode. The #2172 process steps 1 to 7, planned, built, tested on copies and
made live; then the plan for catch-up B to D, which waits on the researcher's decisions.
- Build plan with five decisions (all approved as option A).
- Built: claims told per block (the narrative held in iba.db, chapter files as exports),
  `iba/app/ps/Strand-Reading.ps1` with eight steps, the close gate, `governance.narrative_home`.
- Tests: 84 of 84 on copies. No strand defined, nothing read (the study is on hold).

## 2. Escalations

- **#2172: updated v15 to v25.** In progress (v15); build plan for approval (v16); approved by the
  researcher (v17); build steps recorded (v18 to v20); the build handed for approval (v21);
  approved by the researcher (v22); catch-up started (v23); catch-up plan for approval (v24);
  the researcher's close-time messages recorded (v25).
- **#2213: raised** (on-hold, for the researcher): 45 in-part tellings with no part recorded.
- **#2214: raised and resolved** (self-correctable): the retired Record step's `cfg_on_fail` row.
- **#2215: raised and resolved** (self-correctable): two `cfg_enum` values missing.
- **#2177: updated v26:** progress on item 1 of "A then 1".
- **#2207: v-updates by validate's advisory tier** (not by Claude).

## 3. Files

- Code: `iba/app/lib/narrativeregister.py`, `iba/app/handlers/narrativeregister.py`,
  `iba/app/ps/Narrative-Register.ps1`, `iba/app/lib/strandreading.py`,
  `iba/app/handlers/strandreading.py`, `iba/app/ps/Strand-Reading.ps1`,
  `iba/app/lib/recordingpass.py`, `iba/app/lib/versemeta.py`, `iba/app/lib/escalation.py`.
- Migrations (run live, in archive/): `iba/app/migration/archive/strand_reading_schema_2172_v1_20261022.py`,
  `iba/app/migration/archive/record_retire_onfail_2172_v1_20261022.py`,
  `iba/app/migration/archive/strand_reading_steps_2172_v1_20261022.py`,
  `iba/app/migration/archive/strand_reading_enums_2172_v1_20261022.py`,
  `iba/app/migration/archive/narrative_home_2172_v1_20261022.py`.
- Test runners: `iba/app/tools/temp_2172_register_test_run.py`, `iba/app/tools/temp_2172_rewrite_test_run.py`,
  `iba/app/tools/temp_2172_strand_test_run.py`, `iba/app/tools/temp_2172_map_handler_test_run.py`.
- Docs: `iba/app/BUILD.md` (sec 386, 387), `iba/app/USER-GUIDE.md` (sec 8), `iba/app/GOVERNANCE.md`
  (sec 6), `iba/docs/2172-strand-reading-test-plan-v1-20261022.md`, `iba/docs/ps tools worksheet.xlsx`.
- Escalation files: `outputs/escalation/2172-process-build-plan-v1-20261022.md`,
  `outputs/escalation/2172-catch-up-plan-v1-20261022.md`.
- Published register files (Export): `_analytics/essay/spirit_soul_body/narrative-claim-register.md`,
  `_analytics/essay/spirit_soul_body/narrative-claim-changes.md`,
  `_analytics/essay/spirit_soul_body/narrative-citation-index.md`.
- Compliance: `Logs/compliance/COMPLIANCE-20261022-691d410b.md`.
- Memory pointer updated: `reference_narrative_passage_table_holds_only_told_passages.md` (narrative held as blocks).

## 4. Decisions

Researcher's decisions:
- The build plan's five points, all option A (strand tables; tellings per block; citated replaces
  analysed; an unclaimed statement becomes a claim or an escalation item; the close gate as a check
  kind): recorded in #2172 v17.
- "proceed to build it properly": recorded in #2172 v19.
- The build of steps 1 to 7, including `governance.narrative_home`, approved: #2172 v22.
- Close now ("session-close"): recorded in #2172 v25.

Claude's self-correctable fixes, made and closed:
- The retired Record step's `cfg_on_fail` row left active: fixed in `iba/app/migration/archive/record_retire_onfail_2172_v1_20261022.py`, #2214 v2.
- Two enum values missing (config_module strand_reading, check kind strand_account_clean): fixed in `iba/app/migration/archive/strand_reading_enums_2172_v1_20261022.py`, #2215 v2.
- EditSection changed a block without publishing the chapter (found in testing): fixed in `iba/app/lib/narrativeregister.py` (BUILD.md sec 386).

## 5. Open items

- **For the researcher:** the five decisions of the catch-up plan, `outputs/escalation/2172-catch-up-plan-v1-20261022.md` (#2172 v24); then Claude runs catch-up B to D in a fresh Developer Mode session.
- **For the researcher:** #2213, the in-part tellings with no part (on hold).
- **Carried:** the 46 current claims no block tells, on #2172 (catch-up D); the six spine gaps not verified against STEP, on #2205.
- **Parked:** #2206 (on hold with #2207); #2177 stays with Claude until the #2172 catch-up is done.

## 6. Git

_(written after the first commit)_
