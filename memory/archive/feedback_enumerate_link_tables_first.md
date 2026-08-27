---
name: feedback_enumerate_link_tables_first
description: "Before concluding a record is unlinked/orphaned/unmapped, enumerate EVERY junction/link table that references it — linkage often lives in subsidiary tables, not the obvious column."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: eae3184c-630b-48c2-9ac1-b0b494ccf689
---

Before declaring any record "unlinked", "orphaned", "no mapping", or a deletion/set-aside candidate, **enumerate every junction/link table that could reference it** (scan `sqlite_master` for tables whose columns include its id / strongs / question / catalogue / cluster / finding_id, etc.) and check each. The linkage is frequently in a subsidiary table, not the column you first look at.

**Why:** On 2026-06-01 I assessed Session B/D pointers as largely "no term/cluster mapping" because `wa_session_b_findings.term_id` was empty — but I missed `wa_finding_catalogue_links` (2,632/2,883 findings linked to tier/observation-catalogue questions), `finding_citation` (75k structured citations for the `cluster_finding`/`cluster_observation` layer), and the whole cluster-analysis finding layer. My "no-link / set-aside" set of 261 (then 1,014) was contaminated with tier-adopted findings; the genuinely orphaned set was only 30 findings + 72 flags. The researcher caught it by asking "are you sure there are no subsidiary tables?".

**How to apply:** dump all tables + columns + row counts first; treat a record as orphaned ONLY when NO link table references it. Relates to [[feedback_evidence_signal_completeness]] (same failure shape: concluding "empty/absent" from one field instead of the full picture) and [[feedback_integrity_and_intent_first]].
