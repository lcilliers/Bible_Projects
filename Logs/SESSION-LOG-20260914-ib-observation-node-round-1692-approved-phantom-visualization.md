# Session Log — 2026-09-14

**Scope:** Session-start orientation, then a working session finishing out #1691/#1692/#1693 of
the cluster-reading sign-off pack — resolved `ib_node`'s row shape, element list, and `seq`
uniqueness defect, discovered and closed a real generation-gap (process (b) produces observations
with no DB home), surfaced and partly resolved a new cross-cluster `synthesis` design gap (#1698),
approved and closed **#1692** as the second of six pack items, then built and recorded a phantom
`ib_node` dataset plus an interactive network-visualization artifact as a jump-start for the real
thing (#1699).

## 1. Session start

Ran the `start-project` procedure: git dirty (one pre-existing uncommitted researcher notes file,
flagged, not committed at start), STEP not up — started it, came up within the poll window; IBA
bootstrap READY; spine check 0 FATAL; 32 open escalations (unenforced-config count: 33
`context_delivered`, 3 `partially_enforced`, 2 `buildable_not_built`, 1 `deliberately_deferred`, 0
`judgment_call_pending`, 0 `not_mechanically_checkable`). Live thread: the #1682 cluster-reading
sign-off pack (#1690 approved, #1691/1692/1693/1696/1697 open).

## 2. Escalations touched, by id, with outcome

| # | Outcome this session |
|---|---|
| **#1690** | Not transacted (already `completed`/`approved` from a prior session) — one doc cross-ref note added only (§2 item 1: `placement_note` confirmed-live as also not produced by the real M10 run, same gap as the known `label` gap), no state change. |
| **#1691** | Updated repeatedly (v13→v16) — v12/v13 subgroup/cluster-rollup reconciliation confirmed approved; `stage` corrected to cfg_enum-governed and open to growth; live-checked against an actual M10 process-(b) prototype run and confirmed process (b) already produces real observations (3 strong-scoped, 1 cluster-wide) with no DB home; researcher confirmed the b/c/d/e≡subgroup/reading/observation/synergy mapping (corrects my own prior wrong assumption that "synergy" was a future 4th stage); `stage` gains a new `subgroup` value; `ib_node` row-shape rule sharpened (one observation + one reference per row, one row per item for same-type multiplicity); `placement_note`→`ib_observation` promotion rule recorded; cross-cluster `synthesis` scope gap spun out to new escalation #1698. Still `in-progress`. |
| **#1692** | Updated repeatedly (v6→v13) — guiding-principle framing recorded; single polymorphic table confirmed with the row-shape rule above; `question_code` column added; `cluster_code`/`cluster_subgroup_code` reframed as true per-row references, not fixed home-context copies; stage-terminology mapping resolved; **`seq`'s uniqueness defect fully resolved** (plain per-observation ordinal, `UNIQUE(observation_id, seq)`, value from `span.position` when span-grounded else a plain serial, read in `seq` order) — the last real blocker on this table. **Moved to `ready_for_approval` then `approved`/`completed` (v11→v13)** — second of the six pack items signed off. |
| **#1693** | Updated repeatedly (v9→v10) — guiding-principle cross-ref added (this procedure's own charter); `placement_note` promotion responsibility added (mechanism still undesigned, folded into the existing same/broaden/new gap); cross-cluster `synthesis` precondition gap flagged (not designed, tracked at #1698). Still `in-progress`. |
| **#1698** | Raised, then updated (v2) — "Synthesis stage is cross-cluster: `cluster_code` gap." Researcher resolved item (i): `ib_observation.cluster_code` changed from `NOT NULL` to `NULL` for `stage='synthesis'`, actual clusters recorded via `ib_node` rows instead (one per cluster). Item (ii) — #1697's single-cluster `cluster.status` precondition vs. a genuinely cross-cluster synthesis run — still open. Naming resolved as a working convention: `synthesis` stays the DB/doc term; a stray "synergy" or other word from the researcher in chat refers to the same stage, not a re-opening. Still `in-progress`/`revise`. |
| **#1699** | Raised — "IB Node Web phantom visualization jump-start." Records the phantom `ib_node` dataset, generator script, published network-visualization artifact, artifact-builder script, and durable local copy (see §3), explicitly as a resume point for the real visualization once `ib_node` holds real rows. `raised`/`review`. |

## 3. Files created or changed

- `iba/docs/1690-cluster-subgroup-family-columns-v1-20260912.md` — cross-ref note only (§2 item 1: `placement_note` gap confirmed live), no schema/state change.
- `iba/docs/1691-ib-obs-finalization-v1-20260912.md` — `stage`/`cluster_subgroup_id`/`cluster_code` column comments corrected and extended; §9 items 5, 7, 8, 9, 10 added/resolved (terminology correction, v12/v13 approval, process-(b) observation gap with M10 evidence, cross-cluster `synthesis` gap, `placement_note` promotion rule).
- `iba/docs/1692-ib-node-finalization-v1-20260912.md` — guiding-principle banner added; `question_code` column added; `cluster_code`/`cluster_subgroup_code`/`seq` column comments rewritten; new `UNIQUE(observation_id, seq)`; §2/§3/§4/§5 substantially rewritten (row-shape rule, coverage self-check, `seq` resolution, terminology mapping) — document's own design content now complete.
- `iba/docs/1693-table-update-procedure-finalization-v1-20260912.md` — guiding-principle banner added; §0 cross-cluster precondition gap flagged; §2 table row added for `placement_note` promotion and per-item `ib_node` row creation.
- `_analytics/Clusters/1692-ib-node-phantom-mockup-100-v1-20260914.json` — new. 100 phantom `ib_node` rows + 30 phantom observations, matching #1692's finalized schema exactly. Clearly marked as invented data, not real results.
- `_analytics/Clusters/1692-ib-node-mockup-generator-v1-20260914.py` — new. Seeded/reproducible generator for the above.
- `_analytics/Clusters/1692-ib-node-web-artifact-builder-v1-20260914.py` — new. Builds the published HTML artifact from the JSON; documented as reusable against a real `ib_node`/`ib_observation` export once one exists.
- `_analytics/Clusters/1692-ib-node-web-v1-20260914.html` — new. Durable local copy of the published artifact.
- Published Artifact "IB Node Web" — `https://claude.ai/code/artifact/be22d9dd-30b2-44b7-b760-5bf2b59c9d6b` (interactive force-directed graph, six entity types, filters, search, click-through inspector).
- `_analytics/Clusters/` directory case-drift fixed (`_analytics/clusters` → `_analytics/Clusters`) — found on disk this session (`core.ignorecase` had masked it from git), not attributable to a specific prior action; restored to match every doc/escalation reference written today. Non-functional under git's case-insensitive tracking, but worth noting as unexplained drift.
- `Workflow/Chat_responses/Cluster-read naming conventions` — pre-existing uncommitted researcher notes (not this session's own change, carried from a prior session per the standing "stage the full working-tree diff at close" rule); read before staging — it is the researcher's own source annotations behind naming decisions already reflected in #1690–1693 (IB_obs, IB_node, `cluster_subgroup`, `observation`, `tag`, `verse_reference`, `span.surface` naming, SUNDRY→FLAG, descriptive nomenclature), fully consistent with what's already recorded.
- Escalation/spine-check reports regenerated and archived per normal report rotation: `outputs/escalation/escalation-list-v79-20260914.md`, `outputs/escalation/1691-escalation-history-v4-20260914.md`, `1692-escalation-history-v1-20260914.md`, `1693-escalation-history-v2-20260914.md`, `1695-escalation-history-v1-20260914.md`, `1698-escalation-history-v1-20260914.md`, `1699-escalation-history-v1-20260914.md`; `research/discovery/spine-check-v13-20260914.md` + pointer; prior versions moved to their `archive/` folders.

## 4. Decisions made

**Researcher's own decisions (not self-correctable):**
- `stage` gains a new value for process (b)'s own observations (proposed name `subgroup`, matching the process — not yet finally confirmed as the exact spelling).
- `ib_node` row shape: one observation + one coherent reference per row; multiple items of the same reference type (e.g. several clusters) = one row per item, not one row with several values filled in.
- `placement_note` carrying a genuine observation must be promoted into `ib_observation`/`ib_node` by the load routine — the LLM makes the observation, the load routine records it in the right form and place.
- `seq`'s value source: `span.position` when the row is span-grounded, a plain serial otherwise; the governing read-rule is that multiple `ib_node` rows sharing one `observation_id` are read in `seq` order.
- `ib_observation.cluster_code` changed from `NOT NULL`/singular to `NULL`-able for `stage='synthesis'` — the actual cluster(s) a synthesis observation touches are recorded via `ib_node` rows instead.
- `synthesis` stays the working term for the cross-cluster/cross-subgroup stage (researcher may still say "synergy" or another word from memory in chat; not a re-opening of the naming question).
- **#1692 approved and closed** — second of the six sign-off-pack items ready for build; build execution itself still held until the rest of the pack is also ready.
- Requested the phantom `ib_node` visualization be formally recorded (as #1699) specifically so it can jump-start the real visualization once `ib_node` holds real rows, rather than being a one-off throwaway.

**Self-correctable (fixed directly, not escalated):**
- My own prior-turn error, corrected once the researcher confirmed the b/c/d/e mapping: "synergy" is process (e) (the existing `stage='synthesis'` value), not a future 4th stage beyond it — #1691's doc and its escalation record were both corrected in place.
- `_analytics/Clusters` directory case restored (`clusters` → `Clusters`) to match every reference written this session.

## 5. Open items carried into next session

- **Sign-off pack: 2 of 6 ready** (#1690, #1692). #1691, #1693, #1696, #1697 still need review/approval before any build executes.
- **#1698 item (ii), still open:** #1697's single-cluster `cluster.status='ready_for_synthesis'` precondition doesn't obviously generalize to a genuinely cross-cluster synthesis run — needs the researcher's own decision, not designed here.
- **#1691 §9 item 8:** the exact spelling of the new `subgroup` stage value — proposed, not finally confirmed.
- **#1693 §3:** the same/broaden/new similarity-matching algorithm, and now also the `placement_note`-vs-bookkeeping-note distinction — still the single biggest undesigned piece.
- **#1691 §7a/#1696:** `wa_obs_question_catalogue`'s messy lifecycle state migration into `iba.db` — unchanged, not touched this session.
- **#1695:** the synergy/synthesis-stage (process e) design itself — unchanged, still parked until the rest of the pipeline is built and tested.
- **#1699:** resume by re-running `1692-ib-node-web-artifact-builder-v1-20260914.py` against a live `ib_node`/`ib_observation` export once #1692/#1693 are built and populated — no design decision needed to resume, just real data.

## 6. Git state

- Branch: `main`
- Commit: *(to be filled in after commit — see below)*
- Push: *(to be confirmed after push)*
