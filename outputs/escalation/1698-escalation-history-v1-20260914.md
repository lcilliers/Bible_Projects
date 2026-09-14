# Escalation deep history

## #1698 — Synthesis stage is cross-cluster: cluster_code gap
type=issue source=Claude

**v1** (2026-09-14T03:54:43Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Synthesis stage is cross-cluster: cluster_code gap
> **comment (set this version):** Researcher's own words, this chat turn: 'stage e (synthesis) is in essence cross cluster and sub_group analysis, its naming convention is not yet stable.' This corrects #1691 v13's own description (cross-family, not subgroup-scoped -- understated the scope to within one cluster). Two real, unresolved consequences: (1) ib_observation.cluster_code (#1691 sec1) is NOT NULL and singular -- a synthesis row spanning multiple clusters has no single owning cluster to put there. (2) #1697's cluster.status='ready_for_synthesis' precondition (#1693 sec0) is a single-cluster check -- if synthesis genuinely spans clusters, its real precondition is 'every involved cluster is ready', not one cluster's own status. Also confirms the stage's actual DB value name (synthesis vs synergy) is deliberately not yet settled. Neither consequence is designed here -- needs the researcher's own decision on both the cluster_code shape and the multi-cluster precondition.
> **context (set this version):** Parent: #1691/#1693/#1697 (same sign-off pack). Cross-ref added at #1691 sec9 item9 and #1693 sec0, not duplicated there.

**v2** (2026-09-14T04:03:03Z, Researcher) state=in-progress next_action=revise assigned_to=Researcher
> **comment (set this version):** Researcher, this chat turn: overall assessment in line. (a) cluster_code is not required -- agreed, changed to NULL for stage='synthesis'; the actual cluster(s) referenced are recorded via ib_node rows instead (one per cluster). (b) 'synthesis' as the term for this cross-cluster/cross-subgroup stage can stick for now -- researcher notes they may still say 'synergy' or another word in chat from memory, not a re-opening of the naming question. Item (ii) -- #1697's single-cluster cluster.status precondition vs a genuinely cross-cluster synthesis run -- NOT yet addressed, still open.
> **context (set this version):** Doc updated in place: iba/docs/1691-ib-obs-finalization-v1-20260912.md (section1 cluster_code column, section9 item9).
