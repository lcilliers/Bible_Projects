# Session Log — 2026-09-13

**Scope:** Session-start orientation, then a full working session on the cluster-reading design
pack (#1682/#1690–1693): discovered and applied a database-location fork (all new analytics tables
move from `bible_research.db` to `iba.db`), resolved a knock-on catalogue-migration gap and a
cluster-status lifecycle design, and closed out #1690 as the first of six escalations in a
researcher-defined sign-off pack.

## 1. Session start

Ran the `start-project` procedure: git clean, STEP already up, IBA bootstrap READY, spine check 0
FATAL, 30 open escalations. No uncommitted session logs found at start.

## 2. Escalations touched, by id, with outcome

| # | Outcome this session |
|---|---|
| **#737** | Updated (v15) — flagged that this session's DB-fork finding inverts its original premise (debate/passage-control migrating OUT of `iba.db`); deliberately left open, not realigned, per the researcher's own sequencing decision (option (a): build the new analytics tables in `iba.db` now, revisit #737 once that build is stable). |
| **#1682** | Updated repeatedly (v14→v18) — parent/shared-reference doc for the whole pack. Recorded the DB fork, the 6-escalation sign-off pack declaration, and a pack-readiness tracker table (now shows 1 of 6 ready). |
| **#1683** | Updated (v10) — flagged that the legacy-table rename plan it covers was pure same-database collision-avoidance, now moot since the fresh tables target a different database; the rename is a free-standing disposition question on its own timeline, not a build precondition. |
| **#1690** | Updated repeatedly (v5→v12) — DB fork applied (target `iba.db`, `mti_term_id`→`strong`/`iba.strong`), FLAG subgroup mechanism confirmed, subgroup-level `status` lifecycle enum proposed and approved (§3a), full process-(b) governing rules (a–g) recorded verbatim, cluster/subgroup status rollup reconciled. **Moved to `ready_for_approval` then `approved`/`completed` (v11/v12)** — first of the six pack items signed off; resolution explicitly notes build execution still waits on the other five. |
| **#1691** | Updated repeatedly (v7→v13) — DB fork applied, a new cross-database gap found (`wa_obs_question_catalogue` FK) and spun out to #1696, `window`/`tag`/`stable_key` resolutions folded in from earlier in the session, cluster/subgroup status rollup reconciled. Still `in-progress`. |
| **#1692** | Updated (v4→v6) — confirmed already fully `iba.db`-consistent (no column changes needed), status-rollup note added for completeness. Still `in-progress`. |
| **#1693** | Updated repeatedly (v6→v9) — DB fork applied, run structure (§0) documented, same/broaden/new partially resolved, two-level status check/advance logic (subgroup-grain for reading/answer, cluster-grain for process b/synthesis, plus rollup recompute) added. Still `in-progress`. |
| **#1695** | Raised — "Design: cluster-reading synergy stage," parked until the build/test of the system through (not including) the synergising stage is complete, per the researcher's own suggestion. |
| **#1696** | Raised, then updated (v2) — "Migrate `wa_obs_question_catalogue` to `iba.db`," full doc written referencing live-checked active routines (`cataloguewrite.py`/`cataloguereport.py`/`handlers/catalogue.py` + their `cfg_step`/`cfg_write_grant` rows) and 6 closed escalations (#1007, #1370, #1444, #1524, #1018/#1445, #1024/1025/1030–1037) with their specific relevance. Part of the sign-off pack. |
| **#1697** | Raised, then updated (v2) — "`iba.cluster.status` lifecycle enum + gating rule," 8-value enum in the researcher's own order, reassignment-reset rule, and (after reconciliation with #1690 §3a) a 4-part gating rule distinguishing direct cluster-grain transitions from the subgroup-status rollup. Part of the sign-off pack. |

## 3. Files created or changed

- `iba/docs/1682-cluster-reading-data-model-v1-20260911.md` — DB fork banner, §2.1a (legacy rename plan superseded), §2.2/§6/§7 corrected, sign-off pack declaration + readiness tracker.
- `iba/docs/1690-cluster-subgroup-family-columns-v1-20260912.md` — DB fork, `strong` FK replacing `mti_term_id`, FLAG mechanism, new §3a (subgroup status), process-(b) rules a–g, status-rollup reconciliation.
- `iba/docs/1691-ib-obs-finalization-v1-20260912.md` — DB fork, new §7a (catalogue gap → #1696), staging/tag confirmations, status-rollup reconciliation.
- `iba/docs/1692-ib-node-finalization-v1-20260912.md` — DB fork confirmation, status-rollup note.
- `iba/docs/1693-table-update-procedure-finalization-v1-20260912.md` — DB fork, new §0 (run structure), §3 same/broaden/new partial resolution, two-level status logic.
- `iba/docs/1696-obs-catalogue-migration-to-iba-v1-20260913.md` — new.
- `iba/docs/1697-cluster-status-lifecycle-v1-20260913.md` — new.
- `outputs/escalation/escalation-list-v78-20260913.md` — generated (`Escalation.ps1 -Action List`); prior version archived.
- `research/discovery/spine-check-v12-20260913.md` — generated (`Spine-Check.ps1`, 0 FATAL); prior version archived.
- `research/discovery/spine-check.md` — updated pointer.
- `outputs/escalation/1690-escalation-history-v1-20260913.md` — present in working tree (escalation deep-history export the researcher referenced mid-session); included in this commit for completeness.

## 4. Decisions made

**Researcher's own decisions (not self-correctable):**
- DB fork: all new cluster-reading analytics tables (`cluster_subgroup`, `cluster_subgroup_strong`, `ib_observation`, `ib_node`) target `iba.db`, never `bible_research.db` — following from the FK-enforcement finding (SQLite doesn't enforce cross-database FKs).
- #737 stays open, not realigned, pending a stable IBA analytics build (option (a) over option (b)).
- `wa_obs_question_catalogue` migrates into `iba.db` — new escalation #1696 raised for it, folded into the sign-off pack.
- `iba.cluster` gets a `status` column, 8-value enum in the researcher's own specified order and wording, with the reassignment-reset rule — #1697.
- `cluster.status` is a rollup over `cluster_subgroup.status`, not an independent gate, for the subgroup-scoped stages (reading/answer); synthesis is the exception (cross-family, genuinely cluster-grain).
- Full process-(b) LLM-session governing rules (a–g): full-cluster read before assignment, meaning-based grouping, 10-subgroup cap (FLAG excluded), essence-true labels, valid singleton subgroups, precise FLAG conditions, `placement_note` not FLAG-only.
- #1690 approved as the first of six sign-off-pack items ready for build; build execution itself held until all six are ready.

**Self-correctable (fixed directly, not escalated):**
- Stale cross-references to `mti_term_subgroup`/`mti_term_id`/`mti_terms.id` left over from before the rename/fork, corrected throughout #1690/#1691/#1693 once found.
- A column-usage table row in #1690 that had conflated `cluster_subgroup.status` with `iba.cluster.status` — corrected once the confusion was pointed out.

## 5. Open items carried into next session

- **Sign-off pack: 1 of 6 ready** (#1690). #1691, #1692, #1693, #1696, #1697 still need review/approval before any build executes — tracked in #1682's own readiness tracker table.
- #1691 §7a / #1696: exact plan for how `wa_obs_question_catalogue`'s messy lifecycle state (239/424 active, markers disagreeing) travels into `iba.db` — not decided.
- #1693 §3: the actual same/broaden/new similarity-matching algorithm for `ib_observation` — still the single biggest undesigned piece.
- #1692 §4: `ib_node`'s `seq`-uniqueness defect — still blocking before that table is safe to build.
- #1697 §5: exact `cfg_enum` value spellings, what "ready for observations" precisely gates, initial backfill values for the 100 live `iba.cluster` rows.
- #1683: whether the legacy `bible_research.db` characteristic/subgroup tables still get renamed to `zz_legacy_*`, now that it's a free-standing disposition question rather than a build precondition.
- #1695: synergy-stage (process e) design, explicitly parked until the rest of the pipeline is built and tested.

## 6. Git state

Full diff staged and committed this unit of work — see commit below for the actual hash and push
confirmation.
