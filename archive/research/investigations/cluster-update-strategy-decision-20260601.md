# Cluster update strategy — full v3 re-run vs differential pass (decision)

**Type:** decision doc (for researcher) · **Date:** 2026-06-01 · **Status:** awaiting decision · nothing actioned.

## The question

The FLAG classification JSON (soon) will assign new terms to clusters that have **already been analysed**. We must decide how those additions — together with the still-incomplete elements — get folded in:

- **Option 1 — full v3_0 re-run** of each affected cluster (six phases A–F).
- **Option 2 — differential pass:** a scoped update that processes only the new/changed elements against each cluster's existing analysis.

The differential to absorb is **three streams at once**: (a) new terms (FLAG→cluster), (b) unallocated pointers, (c) unresolved boundaries.

## Scale evidence (why this matters)

| element | volume | source |
|---|--:|---|
| Existing cluster analysis already done | **21,508** `cluster_finding` rows (M10 4,158 · M15 1,724 · M05 1,517 …) | `cluster_finding` |
| (a) New terms incoming (to distribute) | up to **433** FLAG terms (exact per-cluster split pending the JSON) | FLAG triage |
| (b) Unallocated pointers (in-progress clusters) | **88 findings + 203 flags** (M04 alone 53+173; rest mostly 0–11 each) | step (b) review |
| (c) Unresolved boundaries | **39** open `BOUNDARY_DECISION_PENDING`, each belonging to a named cluster (**M01:7, M02:4, M03:28**) | research flags |

The differential (a few hundred items, lopsided toward M04) is **tiny next to the 21,508 findings already validated**. Re-deriving all of that to insert a handful of new terms is disproportionate.

## Recommendation: **Option 2 — differential pass** (with an escalation guard)

**Why:**
1. **Preserves validated work.** A full v3 re-run would re-generate the 21,508 existing findings, risking loss of manual curation and burning large cost to reproduce what's already correct.
2. **The incomplete set is bounded and now identifiable** — we can enumerate exactly the new terms, pointers, and boundaries per cluster.
3. **Cost/throughput** — the researcher is committed to finishing all 46 before Session D; a differential pass is the only realistic way to do that without redoing analysis.

**Escalation guard — when a cluster needs more than a differential:**
- a new term introduces a **characteristic the cluster doesn't yet have** (structural change → needs the relevant v3 design phase, not just placement), or
- the differential is **large / reshaping** (e.g. **M04** — paused mid-Phase-9 with 53 findings + 173 flags + its BOUNDARY backlog; treat M04 as its own fuller pass, not a light differential).

## Differential-pass design (unified — absorbs a + b + c in one cluster visit)

Per cluster, intake its differential bundle and run a **scoped subset of the v3 phases** (term placement → relevance → finding update), leaving existing analysis intact:

1. **New terms (a):** place each into an existing characteristic/sub-group; run VC/relevance on its verses; if it fits no existing characteristic → escalate (guard above).
2. **Pointers (b):** adopt each unallocated pointer into an existing or new finding (the allocation step already designed), cross-reference + close; or set aside.
3. **Boundaries (c):** resolve each boundary attributed to the cluster — route to a cluster, keep as a recorded cross-cluster relationship, or set aside.
4. **Emit** one patch per cluster: new/updated `cluster_finding` + characteristic/sub-group placements + pointer closures + boundary resolutions.

This is **v3 phases scoped to the differential**, not a new methodology — so it stays inside the validated process.

## Open points for the researcher

1. **Confirm Option 2** (differential pass) over a full re-run.
2. **Does v3_0 already support a scoped/increment run**, or should the differential pass be written up as an explicit scoped-mode of v3 (so it's a documented variant, not an ad-hoc deviation)?
3. **M04** — agree to handle as a separate fuller pass rather than a light differential?
4. **Boundaries are already cluster-owned** (correction): each of the 39 names its cluster in its description (M01:7, M02:4, M03:28) — they are Phase-9 *closure-without-exit-decision* terms, not floating items, and there is **no** separate boundaries cluster. No attribution step needed; they feed directly into M01/M02/M03's differential (resolve = route to cluster / keep as recorded cross-cluster relationship / set aside). So boundaries touch only **3** clusters.

## Sequencing implied if Option 2 is chosen
FLAG JSON applied → per-cluster differential bundles assembled (new terms + pointers + boundaries) → differential pass per cluster (small ones first, M04 escalated) → clusters reach completion → Session D.
