# Escalation deep history

## #1690 — Design: cluster-reading family table
type=task source=researcher

**v1** (2026-09-12T04:19:07Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Design: cluster-reading family table
> **comment (set this version):** Split out of #1682 (iba/docs/1682-cluster-reading-data-model-v1-20260911.md §2) for focused, one-component-at-a-time design, per researcher instruction this chat turn. Open questions specific to family: (1) is a strong's family membership permanent, or does it need versioning/history if M10's families are ever re-derived (currently a one-shot LLM pass, process b)? (2) family_label is always null in the real data -- keep as a column for later, or drop? (3) is family always scoped to exactly one cluster, or could the same family concept ever span clusters? (4) should 'one strong belongs to exactly one family per cluster' (process b's own rule) be a structural DB constraint from day one, or left to load-time discipline? (5) does SUNDRY (the mandatory catch-all for earmarked/no-further-analysis strongs) deserve any different structural treatment from an ordinary family, given the spec's own rule that its members get no further reading?
> **context (set this version):** Parent: escalation #1682. Data model doc: iba/docs/1682-cluster-reading-data-model-v1-20260911.md.

**v2** (2026-09-12T06:16:03Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **context (set this version):** Cross-ref: #1683 (same underlying cluster_subgroup/M10 data).
> **resolution (set this version):** Reframed per your naming response: family does not become a new table, it reverts to the EXISTING cluster_subgroup + mti_term_subgroup pair (no competing term needed). Checked live and this surfaced a real blocker: cluster_subgroup already has 34 rows for cluster_code='M10' (M10-A..X, M10b-A..F, M10c-A..E, from the OLD characteristic-based method) with 125 active mti_term_subgroup memberships -- the exact same data escalation #1683 asks about. If the new gloss-based families (H_guilt, B_sin, ...) are written into cluster_subgroup under M10, they land in the same table as those 34 legacy rows with no structural marker distinguishing 'which method produced this' beyond subgroup_code naming pattern. Recommendation: #1690 is now blocked on #1683, not parallel to it -- resolve what happens to the legacy 34 rows before deciding how/whether new families get written there. Full detail: iba/docs/1682-cluster-reading-data-model-v1-20260911.md §2.

**v3** (2026-09-12T08:11:21Z, Claude) state=re-assigned next_action=review assigned_to=Researcher
> **comment (set this version):** Column-by-column design for the fresh cluster_subgroup/mti_term_subgroup, built off the exact DDL of the tables being renamed to zz_legacy_*. Two real changes from the old shape, not just naming continuity: (1) label is NOT NULL -- process (b) currently leaves family_label always empty, a real gap that needs closing in the generation script, not just a naming pick; (2) mti_term_subgroup's UNIQUE constraint tightens from (mti_term_id, cluster_subgroup_id) to mti_term_id alone, structurally enforcing 'one strong, one family' -- answers open question 4 directly. FLAG signpost mechanism proposed: subgroup_code='FLAG' as a family belonging to the SAME cluster being read (e.g. M10's own FLAG bucket), never a placement under the separate cluster_code='FLAG' cluster -- stated plainly since it's a real reading, not obvious from the column shape, please confirm or correct.
> **context (set this version):** Full detail: iba/docs/1690-cluster-subgroup-family-columns-v1-20260912.md

**v4** (2026-09-12T16:50:51Z, Claude) state=re-assigned next_action=review assigned_to=Researcher
> **comment (set this version):** Restructured to match #1691/#1692's LLM-session/table-update-procedure split. Two things resolved this round: label's NOT NULL gap now explicitly named as a process-(b) generation-script fix (not a schema question), and mti_term_subgroup's uniqueness constraint tightened to UNIQUE(mti_term_id) alone -- answers the original 'should one-strong-one-family be structural' question with yes. FLAG signposting mechanism (subgroup_code=FLAG under the SAME cluster, not the FLAG cluster) restated as my reading, still not confirmed by you.
> **context (set this version):** Full detail: iba/docs/1690-cluster-subgroup-family-columns-v1-20260912.md

researcher comments

cluster reading the determine cluster subgroups (previous family):

strong membership to a cluster may change, and this could affect subgroup membership.  this means that that a subgroups may change, and especially membership of a sub group.  This has wide implications:
a) when a new strong is added to the base data, it must be assigned a cluster, and this must flag the cluster as changed and in need for rerunning the subgroup determination.
b) if a strong is reallocated to a new cluster then it the impact may affect both the source and destination subgroup.  This must be flagged so the impact can be determined to know which cluster sub group membership must be revisited.
c) check the cluster table to check if there is a status or other appropriate field that can be used for the flag.
d) the flag on cluster will trigger a manual resubmission of the of the cluster subgroup generation. the change of strong may, or may not make any difference to the subgroup determination.  the impact must be assessed to determine if any of tha analytic procedures must rerun.  The impact is determined by a new routine to assess impact by considering any existing observations related to the strong and recommending a course of action to take any changes into account.

subgroup label is a required field.

sub groups are scoped to a cluster. it is not impossible, but unlikely that a subgroup in one cluster is the same as in another.  This applies except for FLAG. 

Each cluster may have a FLAG subgroup. This subgroup is used for strongs that have errors, clearly belongs to another cluster, or must be re-allocated to a T code.  Corrective action for FLAG sub group on a cluster is to re-allocate the strongs or resolve the issue.  The FLAG cluster strongs are never included in the next reading action for sub group.  The FLAG subgroup membership, and reason for the assignment must be included in the output json of the subgroup determination

The tables for recording the Database records for sub group determinination is in the bible_research_db and include new cluster_subgroup, and Cluster_subgroup_strong tables.  both is new tables.  The old cluster_subgroup tables should already have been renamed, or the renaming must take place before any table creation takes place.  I need to review the columns for each table in detail in iba/docs/1690-cluster-subgroup-family-columns-v1-20260912.md
