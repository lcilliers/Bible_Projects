---
name: feedback_remediation_is_analysis_not_reassignment
description: Cluster remediation is ANALYSIS — assess a term/verse's meaning in the cluster's context; where it has meaning in more than one cluster, escalate to a finding in EACH. Not mechanical reassignment; not auditor hacks.
metadata:
  type: feedback
---

**The model (researcher, 2026-06-03/04).** Clusters draw terms whose **content — the term's meaning
within the context of its verse, assessed against the cluster's characteristics and the other members
of the cluster — relates to that cluster.** Membership is meaning-driven, contextual.

**Remediation is ANALYSIS, not reassignment.** The task for each item surfacing under a cluster is to
**assess its meaning in that cluster's context**, not to mechanically move/route/relabel a row, and
not to hack the auditor to make it disappear.

**Terms and verses have meaning in more than one cluster — legitimately.** The **same verse appears in
several clusters.** When an item has analytical meaning in more than one cluster, you **escalate it to
a finding in EACH such cluster** (create a finding per cluster). Where it has no meaning in a given
cluster, it simply isn't that cluster's — it stays the home cluster's, analysed there.

**Worked example (2026-06-04):** registry-117 (Peace) items surfaced under M07 (Shame), M26
(Righteousness), M04 (Joy), M05 (Love), M46 (Abundance) because single peace terms sit, correctly, in
each (e.g. `fimoO` muzzle/silence → Shame; `tse.deq` → Righteousness; `sha.a.nan` secure → Abundance).
The wrong responses: route the findings to M33 (lossy), or refine the auditor to exclude them (hides
real signal). The RIGHT response: analyse each item's meaning in that cluster's context — where it
bears on Shame, escalate to an M07 finding; it remains Peace's too. A peace verse that also speaks to
shame is a finding in both.

**Why:** I kept framing this as reassignment / moving / auditor precision. It is analysis. Supersedes
the movement framing of [[feedback_term_is_the_unit_of_movement]] — moving a genuinely mis-placed term
is a special case; the general activity is **analyse meaning → escalate to findings per cluster**.
Built on [[feedback_two_governing_principles]] (verse meaning is the data and rules all analytics) and
[[feedback_cross_cluster_co_occurrence]].

**How to apply:** use the orchestrator's emitted review sheet (full text per item). For each item,
assess meaning in context; the COMMENT_EVALUATION outcome is `create finding(s)` — one per cluster the
item genuinely speaks to — plus `set aside (non-evidenced for this cluster)` where it doesn't. The
applier is `_apply_comment_findings` (creates `cluster_finding` per cluster + `SD_CLUSTER` reciprocals,
not lossy moves).
