# Escalation deep history

## #2166 — A cheaper review than a DB-wide cluster check
type=issue source=researcher

**v1** (2026-10-19T04:03:57Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** A cheaper review than a DB-wide cluster check
> **comment (set this version):** Researcher, chat 2026-10-19 (verbatim), on P4 of the #2163 proposal: "P4 seems like a very expensive way to handle a review, not approved, we need to think of a better way."

P4 proposed running Cluster-Assign.ps1 -Step Validate (cluster.validate: a read-only check of all 15,455 strongs) before any promotion, to see whether a sweep would touch other codes. Facts: that validate was run once on 2026-10-18, before the proposal was answered (run RUN-20261018_184531_078-CLUSTER-ASSIGN, report _analytics/Clusters/cluster-assign-v6-20261018.md). The promotion itself did NOT use the DB-wide sweep: it ran the registered word-scoped step strong.reconcile for word 'flesh' only (23 codes).

What a better way could be (to think through, not to build): the review that matters for a word-complex change is word-scoped. strong.reconcile already reconciles only the word's own codes; what is missing is a word-scoped read-only preview of what reconcile would do (promote / exception / no change) before it writes. Design is the researcher's call; nothing is built.
