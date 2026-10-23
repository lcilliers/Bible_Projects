# Session log — 2026-10-23 — #2166 closed, the prose patch apply back as a step (#2212)

Session id: `fdbef305-1bb6-457b-888d-80a491479be6` (standard mode). Close report:
`iba/app/reports/session-close-v174-20261023.md` (and its re-runs). Compliance file:
`Logs/compliance/COMPLIANCE-20261023-fdbef305.md`.

## 1. Scope

2026-10-23, standard mode, study active. Start-up, then two escalations chosen by the researcher:

- **#2166, a cheaper review than a DB-wide cluster check:** closed on the researcher's word.
- **#2212, prose patches name a retired apply script:** the three prose steps that write a
  `PROSE` patch had nothing to apply it. The researcher chose option A and approved the build.
  `Prose.ps1 -Step ApplyPatch` is now live (BUILD.md sec 400).

## 2. Escalations

- **#2166:**
  - v2: put for approval (close, nothing built);
  - v3: approved by the researcher and completed.
- **#2212:**
  - v2: in progress;
  - v3: options A and B put to the researcher;
  - v4: the researcher chose A;
  - v5: the finished build put for approval;
  - v6: approved by the researcher;
  - v7: completed, verified live;
  - v8: correction recording the researcher's developer-mode instruction verbatim.
- **#2241, #2242, #2243:** raised by `configmaint.propose` (the `prose.apply_patch` step, the
  `prose.flag_fix_apply` text, the `prosestore` purpose):
  - v2: put for approval;
  - v3: approved by the researcher;
  - v4: applied and completed.
- **#2244:** raised by test 8b's designed refusal; resolved as a test artefact (v2).
- **#2245:** raised: SC16 counts deliberate test refusals as failures (for the researcher).
- **#2240:** raised by the code when `Escalation.ps1 -Action History -Id 729` crashed on an id that
  does not exist; left open with Claude.

## 3. Files

- `iba/app/lib/prosestore.py` (changed: `apply_patch`, `run_apply_patch`)
- `iba/app/handlers/prose.py` (changed: `apply_patch` handler, messages)
- `iba/app/ps/Prose.ps1` (changed: `-Step ApplyPatch`, `-PatchFile`, `-DryRun`)
- `iba/app/USER-GUIDE.md` (changed: sec 11)
- `iba/app/BUILD.md` (changed: sec 400)
- `iba/app/reports/prose-functionality-test-plan-20260826.md` (changed: test 8)
- `iba/app/tools/temp_2212_apply_patch_test.py` (new)
- `iba/docs/ps tools worksheet.xlsx` (changed: Prose tab)
- `outputs/escalation/2212-plan-v1-20261023.md` (new)
- `outputs/escalation/2212-apply-patch-test-results-v1-20261023.md` (new)
- `Logs/compliance/COMPLIANCE-20261023-fdbef305.md` (new)
- Tool reports written this session under `outputs/escalation/`, `outputs/configs/` and
  `iba/app/reports/`.

## 4. Decisions

- Researcher: #2166 closed, "#2166 I think this can be closed, the new method is exactly the
  solution." Recorded in #2166 v3.
- Researcher: #2212 option A, "Option A - the patch was closed in error." Recorded in #2212 v4.
- Researcher: the build in standard mode with config through approval, "you do not need developer
  mode - prepare the changes and present them to me for approval." Recorded in #2212 v8 and
  `iba/app/BUILD.md`.
- Researcher: "Approved: #2212 and config proposals #2241, #2242, #2243." Recorded in #2212 v6,
  #2241 v3, #2242 v3, #2243 v3; applied to `cfg_step` and `cfg_utility`.
- Claude, self-correctable: #2244, raised by a deliberate test refusal, closed as a test artefact.
  Recorded in #2244 v2.

## 5. Open items

- **#2245** (researcher): whether SC16 should skip deliberate test refusals.
- **#2240** (Claude): `Escalation.ps1 -Action History` on an id that does not exist is logged as a
  crash, where it should be a plain refusal.
- Parked items held by Claude, untouched: #2171, #2172, #2207, #2235.
- Open for the researcher, untouched: #2161, #2205, #2238.

## 6. Git

- Branch: `main`.
- Session commit: `aaf234a4f12e2c0d1a2d9479ccabb6f86f6086de` ("session 20261023: #2212 the prose
  patch apply back as a registered step ...").
- Push output: `To https://github.com/lcilliers/Bible_Projects.git` /
  `31114927..aaf234a4  main -> main`.
- This section is committed alone as "session 20261023: session log git confirmation".
