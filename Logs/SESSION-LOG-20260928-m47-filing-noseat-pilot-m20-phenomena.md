# Session log — 2026-09-28 — M47 filing, no-seat pilot, M20 phenomenon-level reading

**Scope:** startup; M47 files moved to `_analytics/Clusters` and a cluster-folder rule put into config; no-seat pilot on M02 and M20; the researcher widened the aim to phenomenon-level reading; M20 v2 written.

## 1. Escalations touched

| # | Outcome |
|---|---|
| #1882 | Raised (configmaint.propose, cluster-folder rule). The researcher's v2 comment said "proceed to create a sub folder for each cluster". **Superseded** by #1884 because the value changed. |
| #1883 | Raised (pilot: seat-sense check, scale-up). Researcher v2: "the concept of M47 seat is perhaps to narrow…". Claude handed it back ready_for_approval with the modes consideration. **Completed** by the researcher. §6.3 (seat-sense check) was never ruled on, and is carried in #1885 v1. |
| #1884 | Raised (revised cluster-folder rule), set ready_for_approval, researcher **approved** ("approve to finalise"), applied, **completed**. |
| #1885 | Raised (M20/M02 v2 phenomenon-level re-read, with the researcher's direction quoted verbatim). M20 v2 delivered; set **ready_for_approval → Researcher** for review before M02. |
| #1881 | Not touched. Still open (session.close stale transcript). This session's report used the correct transcript. |

## 2. Files created or changed

- **Moved (git mv):** all M47 files from `outputs/markdown/` and `research/investigations/` → `_analytics/Clusters/M47 - inner-seat/` (renamed from `M47 - heart-soul-mind-spirit`); prior versions → its `archive/`.
- **Created:** 92 cluster folders under `_analytics/Clusters/`.
- **Handoff:** `M47-handoff-batches-C-to-H-v11` then `v12` (paths corrected; v10 and v11 archived).
- **M47 folder:**
  - `wa-cluster-M47-noseat-decisions-v1-20260928.md` (A2–A4 rulings recorded)
  - `wa-cluster-M47-noseat-pilot-index-v1-20260928.md`
  - `wa-cluster-M47-ib-operation-modes-consideration-v1-20260928.md`
- **M02 folder:** `wa-cluster-M02-noseat-observations-v1-20260928.md` and `wa-cluster-M02-noseat-verses-v1-20260928.csv`.
- **M20 folder:**
  - `wa-cluster-M20-noseat-observations-v1-20260928.md` and `…-noseat-verses-v1-….csv`
  - **`wa-cluster-M20-phenomena-v2-20260928.md`** and `wa-cluster-M20-phenomena-ledger-v1-20260928.csv`
- **Config:** `cfg_setting report.cluster_folder_naming_convention` (new). `outputs/configs/CONFIG-REPORT-v536` was regenerated.
- **Docs:**
  - `iba/app/GOVERNANCE.md` §83 (new)
  - `docs/file-organisation-rules.md` §3.0 replaced by a pointer
  - `CLAUDE.md` §2 and §10 `Sessions-v2` lines marked superseded
  - `_analytics/Clusters/Cluster_README.md` marked superseded
- **Reports:**
  - `research/discovery/spine-check-v33-20260928.md` (0 FATAL)
  - `outputs/escalation/escalation-list-v132`
  - `outputs/escalation/1882-` and `1883-escalation-history-v1-20260928.md`
  - `iba/app/reports/session-close-v14/v15`
- **Memory:** `project_m47_cross_cluster_batches` updated; `feedback_phenomenon_level_emergent_reading` and `project_cluster_folder_rule` added.

## 3. Decisions

**Researcher's own decisions:**
- Filing goes to `_analytics\clusters` with a subfolder for each cluster, and the M47 files move there.
- Filing rules belong in config.
- The inner-being definition is taken from config.
- Read directly from the tables.
- The body-seat list is not relevant.
- Pilots are M02 and M20; T-codes are secondary.
- Cross-correlation builds on the M47 work, and bible_research.db is not used.
- One md per cluster.
- The seat concept is too narrow: go to phenomenon level, with phenomena emerging from the verses, not a tick box, not brushing over detail (#1883 v2 and chat).
- Approved #1884 and #1883.
- Session close before continuing.

**Claude's own calls, self-correctable and recorded:**
- Kept file names on the move and bumped the handoff.
- Raised the revised value fresh as #1884, because a resumed propose applies whatever value it is given.
- The folder name form, `{code} - {short name}`, was later approved in #1884.
- Read "what does it do" (the second one) as "what it leads to", flagged in M20 v2 §0.
- Hiding from God and Job's longing to be hidden emerged as separate phenomena.

## 4. Open items carried forward

- **Researcher:**
  - #1885: review M20 v2, and decide on the proposed two-unit approach for M02.
  - #1883 §6.3: the seat-sense check was never ruled on.
- **Claude, after the #1885 review:** M02 phenomenon-level reading, unit 1 (human anger).
- **Not done:** loose pre-rule files at the `_analytics/Clusters` root are not yet moved into cluster folders. Pointers for revisits: Jon 4 and Job 3/14 → Batch G §16; 1Ki 21:5 and 1Sa 1:15 → Batch F.
- #1881 remains open.

## 5. Git

- Commits this session: `6c4fbf32` (filing, config rule, pilot) and `fe3fc878` (M20 v2), both pushed.
- This log is committed with the session-close changes in the next commit. Its hash and push are shown in the chat close-out; see `git log`.
