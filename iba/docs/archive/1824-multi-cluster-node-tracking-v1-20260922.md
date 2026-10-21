# Multi-cluster membership tracking in `ib_node` — findings + design options

**Escalation:** #1824 (continuation of BUILD.md #316's own flagged open question). **Status:** investigation + design options, NOT built — awaiting a decision before any schema/code change.
**Author:** Claude, 2026-09-22.

## 1. What the researcher asked, verbatim

*"the cluster marker is mechanism to ensure that all verses are covered and all M-codes are being dealt with in an orderly fashion. it helps with completeness, and also 'like' verses. However 50% of verses have multi cluster implications. the multi cluster membership must be captured in the nodes so the observations associated with multiple clusters must be clearly trackable in the nodes."*

Direct continuation of the correction BUILD #316 already made (M0.6.5/M0.6.6/D7.7.1 now answered for every M-code word, not just home) — and of the open question that fix deliberately left unresolved: once a non-home word gets an answer, which cluster(s) should that finding be trackable under?

## 2. Verified, not assumed

- **The "50%" figure is real, and actually higher: 66.7%.** Checked live: of 24,649 verses that carry at least one M-code strong, 16,442 (66.7%) carry M-code strongs from more than one distinct cluster. Distribution: 8,207 single-cluster verses; 7,249 two-cluster; 4,916 three-cluster; the rest (4,270) span 4–10 clusters in one verse.
- **Multiplicity is purely at the VERSE level, never the STRONG level.** Checked `cluster_strong`: zero strongs belong to more than one M-code cluster simultaneously. A verse's multi-cluster nature comes entirely from containing several *different* strongs, each itself singly-owned by its own cluster (e.g. `2Cor.8.8`: `G4710`→`M67`, `G1381`→`M35`, `G0026`→`M51`, `G1103`→`M61` — four single-owner strongs, one multi-cluster verse).
- **The schema constraint**: `ib_node.cluster_code` is `TEXT NOT NULL` — one value per row, no existing multi-valued field.

## 3. The actual gap, precisely

Since BUILD #316, `M0.6.5`/`M0.6.6`/`D7.7.1`/`M0.7` are all answered for every M-code word in a verse — but every resulting node is still filed under the *answering pass's own* `cluster_code`, unchanged. Concretely: when `M67`'s pass answers `M0.6.6` about `G1381` (home cluster `M35`), that finding is written with `cluster_code='M67'`. Query `ib_node WHERE cluster_code='M35'` and it's invisible — even though it's a real, substantive finding about `M35`'s own word.

`M0.1`/`M0.5` already solved a *narrower* version of this via `_effective_cluster_code()` — remapping a word-level fact to the word's own home cluster, always. That's a single reassignment (right home found, wrong pass loses the citation) — not multi-cluster tracking. It doesn't fit `M0.6.6` at all: a whole-network answer is inherently about *every* cluster present in the verse at once, not one "true" owner.

## 4. Design options

### Option A — remap like `M0.1`/`M0.5` (single reassignment)
Extend `_effective_cluster_code()` to also remap `M0.6.5`/`M0.6.6`/`D7.7.1`/`M0.7`. Cheapest, no schema change. **Rejected as insufficient**: only tracks ONE cluster per node, contradicting "trackable in the nodes" for verses that are multi-cluster by nature — and actively wrong for `M0.6.6`, which is a genuinely multi-cluster fact by its own question text ("every M-code characteristic present in this verse together").

### Option B — one extra `ib_node` row per relevant cluster, same observation (recommended)
No schema change — `ib_node` already supports many rows per observation (that's its whole design, `UNIQUE(observation_id, seq)`). When an observation is relevant to more than one cluster, write an additional node row per relevant cluster, all pointing at the same `observation_id`:
- `M0.6.5`/`D7.7.1` (single-word relational/operation facts): 2 clusters relevant — the answering pass's own, and the word's own home cluster (when different). A query for either cluster's own node set finds it.
- `M0.6.6` (whole-network synthesis): every cluster actually present in the verse is relevant — one extra node row per distinct cluster present, all citing the same observation.
- `M0.1`/`M0.5`/`M0.7` stay as they are (`M0.1`/`M0.5` already correctly single-owner via remap; `M0.7` is genuinely single-word, no multi-cluster case applies the same way).

This is a real, if moderate, `record_one_observation()` change (write N node rows instead of 1 for these three question types, N = count of distinct relevant clusters), and needs its own live validation before trusting it — same discipline every other Stage 1 change this session went through.

### Option C — new multi-valued column (e.g. `ib_node.also_relevant_clusters` JSON array)
A real schema migration + `cfg_column` registration, keeping `cluster_code` as "who wrote it" and adding a separate field for "who else this is relevant to." More explicit than Option B but adds a second place to keep in sync, and every downstream consumer of `ib_node` (subgroup allocation, completeness checks, Stage 3/4) would need updating to actually look at the new field — Option B needs none of that, since it just adds more rows to a shape those consumers already query.

## 5. Recommendation

**Option B.** No schema change, no new column to keep in sync, and every existing `WHERE cluster_code=?` query anywhere downstream (`clusterstatus.verse_reading_completeness`, Stage 3/4's own subgroup-scoped reads) automatically starts seeing these findings correctly the moment the extra rows exist — nothing else has to change to consume it. The cost is real but contained: `record_one_observation()`'s node-writing loop needs to know, for `M0.6.5`/`D7.7.1`/`M0.6.6` specifically, the full set of clusters a given occurrence is relevant to (trivial for the first two — the pass's own + the word's own home cluster; for `M0.6.6`, every distinct cluster present in the verse, already computable from `roles_in_verse`).

Not built — this needs a decision on Option B vs. C (or a different shape entirely) before touching `recordingpass.py` again.
