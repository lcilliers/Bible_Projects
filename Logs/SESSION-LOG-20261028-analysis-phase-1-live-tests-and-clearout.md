# Session log 2026-10-28: Analysis_phase_1 live tests, timed batches, backlog clear-out

Session id: 3ba1bfea-7b08-4bf4-b97f-9ab0f5edfb0a (standard mode; the code changes of the day were made in the researcher's Developer Mode sessions and are listed in section 3).

## 1. Scope

2026-10-27 to 2026-10-28: ran Analysis_phase_1 on Gen 43:27 (new test, then rerun after each code fix), recorded `m21-asking` under the enforced observation rules (34 of 271 verses done, five batches timed), redid the first five trial verses, checked the filing config for cluster files, and cleared approved items from the backlog. The tests failed twice on code defects that were fixed in Developer Mode (#2325, #2327, #2328); #2320 stays open until its readings are published or withdrawn.

## 2. Escalations

- #2320 (Build Analysis_phase_1 to specification v4): updated many times (v9 to v23): the failed and passed Gen 43:27 tests, the approval, the redo of five verses, the timed batches, the close attempt; open, approved, with Claude.
- #2323 (old observations not recognised as errors): updated; completed (v12) after the open points were checked live.
- #2325 (Record: moving a node collides on seq): comment v2 on testing before reporting done; completed in Developer Mode.
- #2327 (existing party or link finding refused): raised (v1); completed in Developer Mode.
- #2328 (reading JSON filed outside the cluster folder): raised (v1); completed in Developer Mode.
- #2301 (named pre-run snapshots): closed (completed, v11) after the live check of backup.rollback_method.
- #2305 (capture of prior reading work): handed over (v22), approved by the researcher (v23), closed (v24).
- #2308 (node reference sweep): completed (v6).
- #2262 (gap analysis counts any observation as read): closed (v8) to match its resolution.
- #2296 (reading recorded per occurrence): completed (v4).
- #2161, #2171, #2172, #2235, #2259, #2268, #2276, #2278, #2280, #2303: read, left as they are (held for the claims phase, #2315, or #2268).

## 3. Files

- Logs/SESSION-LOG-20261028-analysis-phase-1-live-tests-and-clearout.md: this log.
- Logs/compliance/COMPLIANCE-20261027-3ba1bfea.md: the session compliance file with evidence and close dispositions.
- Logs/SESSION-LOG-20261027-analysis-phase-1-description-and-specification.md: two Open items lines changed to name only items still open.
- _analytics/Clusters/M21 - fasting-piety/m21-asking/m21-asking.json and m21-asking-batch-times-v1-20261028.md: the reading index and the batch times (written to outputs/reading/ and moved here by the #2328 fix).
- _analytics/Clusters/M21 - fasting-piety/m21-asking-redo5/m21-asking-redo5.json, m21-gen43-27/m21-gen43-27.json, m21-gen43-27-b/m21-gen43-27-b.json: the other readings of the day.
- Database rows written by the readings: ib_observation 20607 to 20658 and later (81 new Analysis_phase_1 observations in the five timed batches), ib_node rows, ib_observation_change entries.
- Code and config changed in the Developer Mode sessions, not by this session: commits 9bf3615c, e2ff7916, 8f462d7d (reading.py, observationrecord.py, migrations, BUILD.md, USER-GUIDE.md).

## 4. Decisions

- The researcher decided: soft delete is a `deleted` column on ib_observation and ib_node, not status or disposition withdrawn (recorded: #2323 v12).
- The researcher decided: the process fixes errors in existing observations, and the fixes need no separate approval (recorded: #2323 v12).
- The researcher decided: the Gen 43:27 result under the enforced rules is accepted and m21-asking continues (recorded: #2320 v14).
- The researcher decided: the first five trial verses are redone under the enforced rules (recorded: #2320 v16).
- The researcher decided: the 24 recorded verses are not read back (RG-20); the outstanding verses are covered when the process is run for real (recorded: #2320 v23).
- The researcher decided: #2305 is complete as run, with four documents as a stated limit (recorded: #2305 v23).
- Claude closed #2262 and #2296 (self-correctable: state matched to the resolution, design already settled) (recorded: #2262 v8, #2296 v4); closed #2301, #2308 and #2323 after live checks (recorded: #2301 v11, #2308 v6, #2323 v12).
- Claude held further m21-asking batches until #2328 was fixed (recorded: #2328 v1).

## 5. Open items

- #2320: approved, with Claude; cannot close until the readings m21-asking (open), m21-gen43-27, m21-gen43-27-b and m21-asking-redo5 (observed) are published or withdrawn; the researcher decides which, in 4 days (Researcher).
- #2161 and #2259: held for the claims phase and the config follow-up #2315 (Researcher).
- #2268: parked on the researcher's instruction of 2026-10-25 (Researcher).
- #2276, #2278, #2280: wait for the claims read process (Claude).
- #2172 and #2235: held until the #2268 rulings (Researcher).
- #2171: parked until the researcher chooses the next study work (Researcher).
- #2303: returns when the first T-a addition is found in a reading (Claude).
- #2315: stale reading configs, including the filing config conflict (Claude, on hold).

## 6. Git

(written after the first commit)
