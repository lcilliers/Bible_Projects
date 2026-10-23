# Session log — 2026-10-23 — #2240 history crash, #2205 spine gaps, #2246 thread audit T-d, #2247 batch A reading

Session id: `0e1dad0b-9f09-4558-ae0f-a900ebc06b67` (standard mode). Close reports:
`iba/app/reports/session-close-v176-20261023.md` (first close) and
`iba/app/reports/session-close-v178-20261023.md` (second close), with their re-runs. Compliance
file: `Logs/compliance/COMPLIANCE-20261023-0e1dad0b.md`.

## 1. Scope

2026-10-23, standard mode, study active. Start-up, then the escalations chosen by the researcher.

**Before the first close:**
- **#2240, escalation.history crashed on #729:** an id with no escalation row is now a usage error,
  not a crash (BUILD.md sec 401).
- **#2205, six spine gaps not verified against STEP:** verified with STEP running; all six are gaps
  by design.
- **#2246, thread audit T-d flags open catch-up items as stale:** raised when the five T-d items
  (OT-108.3, .4, .5, .6, .8) were checked and found open by design. The researcher chose option A
  and approved the build (BUILD.md sec 402).

**After the first close:**
- **#2247, OT-108.3 read through the reading process:** M64 Will & Resolve, in four word-family
  batches. Batch A, the choose words (reading `m64-choose`, 185 verses), passed all three gates and
  was published. Batches B, C and D remain.
- **On the way:**
  - #2248: `Reading.ps1 -Home` could not bind (BUILD.md sec 403).
  - #2250: gate 2 now accepts an item read in part (BUILD.md sec 404).
  - #2249 and #2251: `governance.narrative_home` no longer names the retired Strand-Reading.
  - #2252: `Reading.ps1 -Step Publish` broke on the copy report (BUILD.md sec 405).

## 2. Escalations

- **#2240:** v2: resolved self-correctable, completed.
- **#2205:**
  - v2: in progress;
  - v3: verification put for approval;
  - v4: approved by the researcher and completed.
- **#2246:**
  - v1: raised (in progress, Claude);
  - v2: options A, B and C put to the researcher;
  - v3: the researcher chose A;
  - v4: the finished build put for approval with test results;
  - v5: approved by the researcher and completed.
- **#2247:**
  - v1: raised, the task anchoring the OT-108.3 reading;
  - v2: plan put for approval;
  - v3: decisions 1a and 2a approved, with the researcher's concern quoted verbatim;
  - v4: batch A gate 1;
  - v5: batch A gates 2 and 3.
  It stays in progress for batches B to D.
- **#2248:** raised and resolved self-correctable (v2), completed.
- **#2249:**
  - v1: raised;
  - v2: put for approval;
  - v3: approved by the researcher;
  - v4: completed, applied through #2251.
- **#2250:**
  - v1: raised;
  - v2: options put for approval;
  - v3: option A chosen;
  - v4: the finished build put for approval with test results;
  - v5: approved by the researcher and completed.
- **#2251:** raised by `configmaint.propose`:
  - v2: put for approval;
  - v3: approved by the researcher;
  - v4: applied and completed.
- **#2252:** raised and resolved self-correctable (v2), completed.
- **#2218 (OT-108):**
  - v18: the three-gates note on items 3, 4, 5, 6 and 8.
  - Later versions:
    - items OT-108.19 to .24 added;
    - batch A's touched responses on OT-108.3, .4, .5, .7, .8 and .20, .22, .23;
    - OT-108.21 withdrawn.
- **Other threads touched by batch A** (touched, read in part): OT-92.1, OT-92.3, OT-03.1, OT-05.29,
  OT-103.4, OT-103.8, OT-103.9, OT-103.12, OT-103.25, OT-103.39.

## 3. Files

- `iba/app/handlers/reports.py` (changed: `escalation_history` catches the unknown-id error)
- `iba/app/lib/threadaudit.py` (changed: `_worked_at`, T-d date rule)
- `iba/app/lib/reading.py`:
  - changed for #2250: `touched` settle, `_reaches_past`, `_read_in_part`, `gate2_gaps(cfg, ...)`;
  - changed for #2252: the copy report captured in `publish`.
- `iba/app/ps/Reading.ps1` (changed: `-HomeCluster`, alias `-Home`)
- `iba/docs/ps tools worksheet.xlsx` (changed: Reading tab G4)
- `iba/app/USER-GUIDE.md` (changed: sec 8.2)
- `iba/app/BUILD.md` (changed: sec 401 to sec 405)
- `.claude/commands/start-project.md` (changed: step 5, T-d wording)
- `iba/app/tools/temp_2246_td_test_run.py`, `iba/app/tools/temp_2250_reading_partial_test_run.py`
  (new)
- `outputs/escalation/`:
  - `2246-thread-audit-td-review-v1-20261023.md`
  - `2246-td-test-results-v1-20261023.md`
  - `2247-ot108-3-reading-plan-v1-20261023.md`
  - `2250-gate2-partial-items-review-v1-20261023.md`
  - `2250-reading-partial-test-results-v1-20261023.md`

  (all new)
- `outputs/reading/m64-choose/`: the gap JSON, the collation, the three synergy fills and the
  account v3 (new)
- `outputs/verse-scope/ot108-3-item-20261023.json`, `outputs/verse-collate/ot108-3-item-20261023.md`
  and `.json` (new)
- Narrative register exports, republished by Apply: `narrative-claim-register.md`,
  `narrative-claim-changes.md`, `narrative-citation-index.md`.
- Chapters 10.7, 11 and 13.1, copied to the learning4comfort inbox by Publish.
- `Logs/compliance/COMPLIANCE-20261023-0e1dad0b.md` (new)
- `_analytics/cross-cluster-web/open-threads-register-*.md` (regenerated)
- Tool reports written this session under `outputs/escalation/`, `outputs/configs/`,
  `research/discovery/` and `iba/app/reports/`.

## 4. Decisions

- Researcher: take up #2240 first, "Take up #2240 (escalation.history crash on #729) first."
  Carried out and recorded in #2240 v2.
- Claude, self-correctable: #2240, the History handler catches the unknown-id error as the step's
  other usage slips are caught. Recorded in #2240 v2 and `iba/app/BUILD.md`.
- Researcher: "Approved: close #2205 as verified." Recorded in #2205 v4.
- Researcher: the five T-d items to be verified and closed; verified open, not closed. Recorded in
  #2246 v1.
- Researcher: "Option A.  These open items must be read and pass all three gates." Recorded in
  #2246 v3 and #2218 v18.
- Researcher: "Approved: #2246 T-d change." Recorded in #2246 v5 and `iba/app/lib/threadaudit.py`.
- Researcher: OT-108.3 through the new tool; decisions 1a (four batches) and 2a (OT-108.18 in
  batch C), "I approve 1a and 2a". Recorded in #2247 v3.
- Researcher: "proceed as suggested", read as #2250 option A and approval of the #2249 wording.
  Recorded in #2250 v3 and #2249 v3.
- Researcher: "Approved: #2250 read-in-part change and #2251 narrative_home wording. Proceed with
  batch A gate 2." Recorded in #2250 v5, #2251 v3 and `cfg_setting` governance.narrative_home.
- Claude, self-correctable: #2248, `Reading.ps1` `-HomeCluster` with alias `-Home`. Recorded in
  #2248 v2 and `iba/app/ps/Reading.ps1`.
- Claude, self-correctable: #2252, Publish captures the copy report. Recorded in #2252 v2 and
  `iba/app/lib/reading.py`.
- Claude, execution within the approved rules: OT-108.21 withdrawn and its four seeking drafts set
  silent, since its verses lay wholly inside the reading. Recorded in #2247 v5.

## 5. Open items

- **#2247** (Claude): batches B (willing), C (plan, devise and purpose, with OT-108.18) and D
  (dedicate) of OT-108.3.
- **OT-108.24** (Claude, or the researcher for C-345): tell held claims C-343, C-344 and C-345 in
  10.7, or withdraw them.
- **OT-108.19** (researcher's ruling): whether G1586, G1588 and G1589 are read with M64 (47 NT
  verses).
- **OT-108.20, .22 and .23** (Claude, later readings): the thanksgiving, fear and anger drafts held at
  batch A's gate 2.
- **OT-108.4, .5, .6, .8** (Claude): the M72, M08, M09 and M18 October files, to be read through the
  three gates.
- **#2245** (researcher): whether SC16 should skip deliberate test refusals.
- Parked items held by Claude, untouched: #2171, #2172, #2207, #2235.
- Open for the researcher, untouched: #2161, #2238.

## 6. Git

**First close:**
- Branch: `main`.
- Session commit: `8acded5650c8df8c6b94fd556a8092f1e79dd0c1` ("session 20261023: #2240
  escalation.history treats an unknown id as a usage error ...").
- Push output: `To https://github.com/lcilliers/Bible_Projects.git` /
  `6d849484..8acded56  main -> main`.
- Git confirmation commit: `f35003ffce0ad4623ba59c32b951d54b6cd9b17f`, pushed
  `8acded56..f35003ff  main -> main`.
