# Escalation deep history

## #1692 — Design: cluster-reading trace table
type=task source=researcher

**v1** (2026-09-12T04:19:21Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Design: cluster-reading trace table
> **comment (set this version):** Split out of #1682 (iba/docs/1682-cluster-reading-data-model-v1-20260911.md §2) for focused design. A real defect surfaced while drafting this, not yet resolved: the H_guilt/G1777 example (Matt 5:22, 'liable', three clauses) produces THREE trace rows with IDENTICAL verse_reference/span_surface/span_morph -- the doc's proposed UNIQUE(family_key, source_stage, strong, verse_reference, span_surface, span_morph, traced_observation_id) constraint would wrongly collapse these three genuinely distinct occurrences into one row. iba.db's own span table carries a position column for exactly this reason -- trace likely needs a position/ordinal value copied in too (still a VALUE, not an id, consistent with the store-by-value decision), or the uniqueness constraint needs rethinking entirely. Other open questions: (1) is one polymorphic trace table (verse-grounded OR observation-grounded, via a CHECK) right, or should verse-traces and observation-links be two separate tables given they represent genuinely different kinds of grounding? (2) is the full denormalization list (strong, verse_reference, span_surface, span_morph, cluster_code, family_key) complete, or missing something (e.g. the verse's own text)? (3) does source_stage duplicate observation.stage unnecessarily, or is it needed because a later stage's trace can point at an earlier stage's verse citation directly (not just its own)?
> **context (set this version):** Parent: escalation #1682. Data model doc: iba/docs/1682-cluster-reading-data-model-v1-20260911.md.

**v2** (2026-09-12T06:16:27Z, Claude) state=in-progress next_action=review assigned_to=Researcher
> **comment (set this version):** Renamed per your response: trace -> IB_node (a node, point of connection in a web of relationships -- each column is a 'cord' -- not a pure FK index, per your framing). span_surface/span_morph -> surface/morph_code (matching the source span table's own column names exactly). The known uniqueness-constraint defect (H_guilt/G1777's 3 identical-looking Matt 5:22 spans) is unchanged, still open on this escalation, and now explicitly cited from the main data-model doc's own IB_node section as 'not yet safe to build as-is.'

**v3** (2026-09-12T16:50:48Z, Claude) state=in-progress next_action=review assigned_to=Researcher
> **comment (set this version):** Consolidated per your instruction (matching #1691's new structure): full column list, LLM-session rules (none -- IB_node never exists at generation time, entirely derived from what the LLM records on each observation), and table-update-procedure rules (denormalize at write time, resolve verse_reference fresh against iba.db, assign id). The known uniqueness/seq defect from the first round is unchanged and still the real blocker -- restated clearly as blocking before this table is safe to build.
> **context (set this version):** Full detail: iba/docs/1692-ib-node-finalization-v1-20260912.md

**v4** (2026-09-12T17:54:57Z, Claude) state=in-progress next_action=review assigned_to=Researcher
> **comment (set this version):** Table name RESOLVED this round: ib_node, confirmed by researcher directly (also resolves #1691's matching open item). No other content changes to this escalation's own open items (uniqueness/seq defect, polymorphic-vs-two-tables, denormalized field completeness all still open).
> **context (set this version):** Doc updated: iba/docs/1692-ib-node-finalization-v1-20260912.md

**v5** (2026-09-13T15:32:05Z, Claude) state=in-progress next_action=review assigned_to=Researcher
> **comment (set this version):** DB fork applied: ib_node confirmed as targeting iba.db -- this doc's design was already fully consistent (verse_reference already resolved against iba.db.verse.reference, all FKs already same-database), no column changes needed. Explicit banner added for consistency with #1690/#1691/#1693. No conflicts found in this document.
> **context (set this version):** Doc updated in place: iba/docs/1692-ib-node-finalization-v1-20260912.md (status banner only).

**v6** (2026-09-13T16:03:55Z, Claude) state=in-progress next_action=review assigned_to=Researcher
> **comment (set this version):** Cross-ref note added per new escalation #1697 (iba.cluster.status lifecycle, same sign-off pack): ib_node has no direct gating role -- rows are derived from ib_observation at write time, not independently staged per cluster. Noted for completeness, nothing else changes.
> **context (set this version):** Doc updated in place: iba/docs/1692-ib-node-finalization-v1-20260912.md (status banner).

researcher comments

ib-node is likely the most important table in the entire study.  This node table is the nerve of all observations, all findings, the knowledge web of the study. it ties together, and allows discovery through a network of relations. given that the inner being is one large system of inter connected behaviours and operations the ib_node is the hub of the interconnected reference points.

The design of the ib_node, and the load/reconcile pass #1693 must ensure the integrity of this neural network. everything can relate to anything, but the relation must be evidence based, supported by observations, and must be meaningful. this place a major responsibility on #1693 to record correctly, maintain oppropriately, verify and validate on every turn, and self check as a matter of primary accountability.

each row in the node answer to: what other elements of this study is touched or affected by the observation. This relation is signalled by a column reference to that element: Strong, verse, span, morph, subgroup, cluster, catalogue question, another observation. the element column must be completed if the observation supports it. it must not be completed if the specific observation does not support it.

an observation can have multiple node rows.

it is expected that on the completion of a sub-group reading session, every strong, and every verse in the sub group membership will have at least 1 row in ib_node. every observation in every stage (subgroup, reading, observation, synergy) must have at least one row, and could have multiple rows.

llm does not have to 'find' the related item, it must surface the relation and allow load/reconcile pass to validate the existence of the item, and update ib_node.

llm must verify that each strong and each verse in in the subgroup have been answered to

next, I will work through C:\Bible_study_projects\iba\docs\1692-ib-node-finalization-v1-20260912.mdS