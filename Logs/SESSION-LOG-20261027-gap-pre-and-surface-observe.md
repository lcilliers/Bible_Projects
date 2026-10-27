# Session log 2026-10-27: 0.GAP pre, thread items, and steps 1 to 3 on the surface

Session id: `4f06a0e3-cc15-446b-bfa7-2bbd21685ff4` (Developer Mode, started 2026-10-26T17:33Z).

## 1. Scope

Developer Mode session. Small cleanups (#2301 snapshot pruning, #2307 closed, #2310 0.GAP pre without document reading and open items showing their subgroups, #2311 the purposeless thread items), then the build of steps 1 to 3 of the analytic process on the surface (#2312: scope, 0.GAP pre pull, Observe), tested on a copy and applied live.

## 2. Escalations

- #2301: updated (v6, v7): stale pre-2273 files and older backups pruned on the researcher's instruction; the 5 run snapshots and the design choice (a), (b) or (c) stay open.
- #2307: resolved (closed, v5) on the researcher's comment: superseded by the bulk document capture.
- #2310: raised, built (4.1 and 4.2), updated (v2 to v4); with the Researcher for approval.
- #2311: raised, completed (v3): option (b) already in place as T6; nothing built; with the Researcher for approval.
- #2312: raised, analysed (v1, v2 files), built (steps 1 to 3), updated (v2 to v5); with the Researcher for approval.
- #2313: raised by the config validation (two migrations outside archive/), resolved self-correctable (v2).
- Thread items: OT-108.4 to OT-108.9 closed; OT-108.35, OT-05.10 and OT-05.56 withdrawn (#2218, #2006).
- Held items acknowledged and untouched: #2171, #2172, #2235, #2260 to #2268, #2275 to #2285, #2296, #2303, #2305.

## 3. Files

- `iba/app/lib/reading.py`, `iba/app/lib/versecollate.py`, `iba/app/lib/observationrecord.py`, `iba/app/lib/recordingpass.py` (steps 1 to 3 on the surface)
- `iba/app/migration/archive/gap_pre_2310_v1_20261026.py`, `iba/app/migration/archive/surface_observe_2312_v1_20261027.py`
- `iba/app/tools/temp_2310_gap_pre_test_run.py`, `iba/app/tools/temp_2312_surface_observe_test_run.py`
- `iba/app/BUILD.md` (sections 422, 423), `iba/app/USER-GUIDE.md`
- `outputs/escalation/2310-gap-pre-open-item-hooks-v1-20261026.md`, `outputs/escalation/2310-nine-open-items-without-verses-v1-20261026.md`, `outputs/escalation/2312-scope-pull-observe-gap-analysis-v2-20261027.md` (v1 archived)
- `Logs/compliance/COMPLIANCE-20261026-4f06a0e3.md`, this log
- Deleted on the researcher's instruction: the pre-2273 snapshot -shm/-wal files and iba.db.pre-2110, pre-2163 and pre-2173 backups in `iba/app/db/`
- Database (`iba/app/db/iba.db`, not in git): cfg writes under runs DEVMODE-2310-GAP-PRE-20261026, DEVMODE-2312-SURFACE-OBSERVE-20261027, DEVMODE-2312-MIGRATION-PATHS-20261027

## 4. Decisions

- Researcher: prune the stale pre-2273 files and the older backups; run snapshots kept. Recorded in #2301 v6.
- Researcher: #2307 superseded by the bulk document capture, option 3. Recorded in #2307 v5.
- Researcher: retire the document read from 0.GAP pre; open items show their subgroups (option B); surface the 9 items. Recorded in #2310 v4 and `cfg_setting` reading.gap_types.
- Researcher: close the 6 cluster thread items, withdraw the 3 escalation ones. Recorded in #2218 v104 and #2006 v88.
- Researcher: option (b) on the purposeless thread items. Recorded in #2311 v3.
- Researcher: a word is the surface with its embedded Strong; the agreed observation definition is used, not reworked; Observe is not synergy; face components are gathered in 0.GAP pre. Recorded in #2312 v5.
- Researcher: build steps 1 to 3 and align the data or set it aside. Recorded in #2312 v5.
- Claude, self-correctable: the two migration files moved to archive/ and their cfg_utility paths corrected. Recorded in #2313 v2 and `cfg_change_detail`.
- Claude, taken for the researcher to correct: required set per surface is role, face and term (silence in its place); an existing node counts by occurrence id or a unique verse, Strong and surface match; the 63 observations with no node are left. Recorded in #2312 v5 and `cfg_method_rule` RS-01, RS-02.

## 5. Open items

- #2312: approval of the build (with the Researcher); Observe not run on a real full scope.
- #2310: approval (with the Researcher).
- #2301: the 5 run snapshots and the design choice (a), (b) or (c) (with the Researcher).
- #2305, #2308: review (with the Researcher). #2276, #2280, #2296, #2262 are partly covered by #2312 and to be checked once it is approved (Claude).
- Older test scripts temp_2273, temp_2304 and temp_2310 not re-run for the new shapes: carried #2312.
- Held items (#2171, #2172, #2235, #2260 to #2268, #2275 to #2285, #2303): unchanged, for the researcher's direction.

## 6. Git

- Branch: `main`.
- Session commit: `0fb3799ff721c5e6d36dd1f9cfd7dc61cfb68f60` "session 20261027: #2310 0.GAP pre drops the document read, open items show their subgroups; ...".
- Push output: `To https://github.com/lcilliers/Bible_Projects.git` / `961081eb..0fb3799f  main -> main`.
