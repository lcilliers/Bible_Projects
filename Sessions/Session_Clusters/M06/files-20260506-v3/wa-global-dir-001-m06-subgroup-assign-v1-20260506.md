# Directive DIR-20260506-001 — Record M06 sub-group assignments and reassign two terms

> Produced by: wa-directive-instruction-v1_3-20260422 · wa-global-rules-all-v2-20260427
> Registry: global
> Produced date: 2026-05-06
> Researcher approval: PENDING

---

## Motivation

The M06 cluster (Hate, Contempt and Hostility) has been reviewed through a complete control read of all 36 term definitions and group descriptions in this session (obslog: wa-obslog-M06-m06-method-v1-20260506.md, Exchange 10–11). The researcher has approved a seven-sub-group internal structure for M06: M06-A (Hatred), M06-B (Contempt), M06-C (Abhorrence), M06-D (Cruelty/Ruthlessness), M06-E (Reproach/Received condition), M06-F (Hostility/Enmity), M06-G (Malice), plus a BOUNDARY designation for four terms with edge-of-scope characteristics.

Two terms — H6887E tsa.rar (to rival) and H7520 ra.tsad (to watch with envy) — have been reassigned out of M06. Their primary inner-being content is envy/jealousy rather than hate/contempt/hostility, and their placement in M06 was a boundary decision that is now corrected.

No field currently exists in the database to record sub-group labels within a cluster. CC must inspect the schema and determine the appropriate implementation — either an existing field that can carry this label, or a new column or table if none is suitable. No analytical records (verse context, groups, dimensions) are affected; this is a labelling and cluster-assignment operation only.

The sub-group structure is needed so that the next analytical layer can read the verses per sub-group, one at a time, with a distinct dataset for each sub-group produced by CC.

---

## Scope

**Operation A — Sub-group labelling (34 terms remaining in M06):**

Table to be determined by CC inspection. CC identifies the table and field appropriate for recording a sub-group label at the (cluster × term) level. If no suitable field exists, CC proposes a schema addition (add column or create table) and halts for researcher approval before proceeding with the data write.

Terms and their required sub-group labels:

| Strong's | Gloss | Sub-group label |
|---|---|---|
| H8130 sa.ne | to hate | M06-A |
| H8131 se.na | to hate | M06-A |
| H8135 sin.ah | hating | M06-A |
| H7852 sa.tam | to hate | M06-A |
| H4895 mas.te.mah | hatred | M06-A |
| H0959 ba.zah | to despise | M06-B |
| H5006 na.ats | to spurn | M06-B |
| H0937 buz | contempt | M06-B |
| H7590 shut | to despise | M06-B |
| H0963 biz.za.von | contempt | M06-B |
| H5007B ne.a.tsah | contempt | M06-B |
| H8581 ta.av | to abhor | M06-C |
| G0948 bdelussomai | to abhor | M06-C |
| H1860 de.ra.on | abhorrence | M06-C |
| H8263 she.qets | detestation | M06-C |
| H8374 ta.av | to loathe | M06-C |
| H0394 akh.za.ri | cruel | M06-D |
| H0393 akh.zar | cruel | M06-D |
| H0395 akh.ze.riy.yut | cruel | M06-D |
| H6184 a.rits | ruthless | M06-D |
| H2781 cher.pah | reproach | M06-E |
| H8103 shim.tsah | derision | M06-E |
| G5195 hubrizō | to mistreat | M06-E |
| H8146 sa.ni | hated | M06-E |
| H5007A ne.a.tsah | contempt | M06-E |
| H0340 a.yav | be hostile | M06-F |
| H3401 ya.riv | opponent | M06-F |
| G0476 antidikos | opponent | M06-F |
| H7009 qim | adversary | M06-F |
| H7589 she.at | scorn | M06-G |
| H2778A cha.raph | to taunt | BOUNDARY |
| H0887 ba.ash | to stink | BOUNDARY |
| G0865 afilagathos | hating good | BOUNDARY |
| H7850 sho.tet | scourge | BOUNDARY |

**Operation B — Cluster reassignment (2 terms):**

Table: whichever table records the cluster assignment for terms — likely `mti_terms.cluster_assignment` or equivalent. CC confirms the field name.

| Strong's | Gloss | Current cluster | Required update |
|---|---|---|---|
| H6887E tsa.rar | to rival | M06 | Remove from M06. If an envy/jealousy cluster exists, assign there. If not, record a pending note: 'envy/jealousy — pending cluster assignment' in an appropriate notes field. Do not leave without a record of the intended destination. |
| H7520 ra.tsad | to watch with envy | M06 | Same as above. |

No verse records, group records, dimension records, or prose records are to be altered. No physical deletions per wa-patch-instruction [current] §5.4.

---

## Outcome required

After execution:

1. **Sub-group labels recorded:** For each of the 34 terms listed in Operation A, the sub-group label (M06-A through M06-G or BOUNDARY) is stored in the database at the (cluster × term) level, queryable by CC. The field and table used are reported in the completion confirmation.

2. **Cluster reassignment complete:** H6887E tsa.rar and H7520 ra.tsad are no longer assigned to M06. Their cluster field either shows the envy/jealousy cluster or carries a pending-assignment note. They are not left in M06.

3. **No verse, group, dimension, or prose records altered.** Row counts on `verse_context`, `verse_context_group`, `wa_dimension_index`, and `prose_section` are unchanged.

4. **Sub-group counts queryable:** A count query against the sub-group label field returns: M06-A = 5, M06-B = 6, M06-C = 5, M06-D = 4, M06-E = 5, M06-F = 4, M06-G = 1, BOUNDARY = 4. Total M06 terms after reassignment = 34.

---

## Completion confirmation

CC returns the following:

**1.** The field name and table used to record sub-group labels, or — if a schema change was needed — the DDL applied and the field/table created. If CC halted to request researcher approval for a schema change, state this clearly and do not proceed with data writes until approval is given.

**2.** Sub-group count query result. CC runs a query against the sub-group label field and returns the counts per label. Expected result:

| Sub-group label | Count |
|---|---|
| M06-A | 5 |
| M06-B | 6 |
| M06-C | 5 |
| M06-D | 4 |
| M06-E | 5 |
| M06-F | 4 |
| M06-G | 1 |
| BOUNDARY | 4 |
| **Total** | **34** |

**3.** Cluster reassignment confirmation. CC returns the current cluster field values for H6887E tsa.rar and H7520 ra.tsad after the update. Expected: neither shows M06.

**4.** Row-count checks confirming no verse, group, dimension, or prose records were altered. CC selects the appropriate counts.

---

## Notes

This directive is part of the M06 methodology session. After CC returns the completion confirmation and it is reviewed, the researcher will attach a new dataset per sub-group. The next analytical step (Layer 5) reads through all verses per sub-group, one sub-group at a time, starting with M06-A (Hatred).

The previous draft directive (WA-M06-subgroup-directive-v1-20260506.md) was produced before the directive instruction was available. That file is superseded by this directive and should not be submitted to CC.

---

*wa-global-dir-001-m06-subgroup-assign-v1-20260506.md | DIR-20260506-001 | Produced under wa-directive-instruction-v1_3-20260422*
