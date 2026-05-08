# WA-M06-subgroup-directive-v1-20260506

**Directive ID:** DIR-M06-SUBGROUP-001  
**Date:** 2026-05-06  
**Produced by:** Claude AI — wa-global-rules-all-v2-20260427 · wa-patch-instruction-v2_10-20260427  
**Requires:** Researcher approval before CC executes  
**Session reference:** wa-obslog-M06-m06-method-v1-20260506.md  

---

## 1. Title and identifier

Record M06 sub-cluster groupings (M06-A through M06-G) in the database and reassign two terms (H6887E tsa.rar, H7520 ra.tsad) out of M06 to the envy/jealousy cluster.

---

## 2. What is to be done and why

### Background

The M06 cluster (Hate, Contempt and Hostility) has been reviewed through a control read of all 36 term definitions and group descriptions. The researcher has approved the following analytical structure:

- Seven sub-groups within M06: A (Hatred), B (Contempt), C (Abhorrence), D (Cruelty/Ruthlessness), E (Reproach/Received condition), F (Hostility/Enmity), G (Malice)
- Two terms reassigned out of M06 to the envy/jealousy cluster: H6887E tsa.rar (to rival) and H7520 ra.tsad (to watch with envy). Their primary inner-being content is envy-related; their placement in M06 was a boundary decision now corrected.
- Four boundary/expression terms remain in M06 but are not assigned to a sub-group: H2778A cha.raph (expressive act), H0887 ba.ash (quality term), G0865 afilagathos (character-disorder term), H7850 sho.tet (metaphorical term).

### Purpose

Recording the sub-group structure enables the next analytical layer — reading through the verses per sub-group, one sub-group at a time, with a distinct dataset for each. The researcher will attach a new dataset per sub-group for focused reading.

---

## 3. Operations CC is to perform

CC inspects the database schema and determines the correct tables and field values. The following describes the required outcomes; CC selects the appropriate implementation path.

### Operation 1 — Record sub-group labels for M06 terms

For each M06 term listed below, record the sub-group assignment (M06-A through M06-G, or BOUNDARY). CC determines the appropriate field and table for this — likely a new field on the cluster/term junction, a tag field on `mti_terms`, or a note field. If no suitable field exists, CC proposes a schema addition via a follow-up directive before recording.

| Strong's | Gloss | Sub-group |
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

### Operation 2 — Reassign H6887E tsa.rar and H7520 ra.tsad out of M06

These two terms are currently assigned to M06. Their cluster assignment should be updated to the envy/jealousy cluster. CC determines the correct cluster identifier for the envy/jealousy cluster and updates the assignment accordingly. If no envy/jealousy cluster exists yet, CC records the reassignment as a pending assignment with a note: "envy/jealousy cluster — pending cluster creation."

| Strong's | Gloss | Current cluster | New cluster |
|---|---|---|---|
| H6887E tsa.rar | to rival | M06 | Envy/jealousy cluster |
| H7520 ra.tsad | to watch with envy | M06 | Envy/jealousy cluster |

### Operation 3 — Confirmation query

After completing Operations 1 and 2, CC runs a confirmation query and returns the results. The query should show:

- All 34 terms remaining in M06 with their sub-group assignments
- The 2 reassigned terms with their updated cluster assignment
- Counts per sub-group: M06-A (5), M06-B (6), M06-C (5), M06-D (4), M06-E (5), M06-F (4), M06-G (1), BOUNDARY (4)
- Total M06 terms after reassignment: 34

---

## 4. Expected outcome

- 34 terms remain in M06, each with a sub-group label (M06-A through M06-G or BOUNDARY)
- H6887E tsa.rar and H7520 ra.tsad are no longer assigned to M06; their cluster assignment reflects the envy/jealousy cluster or a pending note
- The sub-group structure is queryable, enabling CC to produce a separate dataset per sub-group for the next analytical layer
- No verse records, group records, or dimension records are altered — this directive is a labelling/assignment operation only

---

## 5. Confirmation CC is to return

CC returns:

1. The method used to record sub-group assignments (field name, table, any schema change made)
2. The confirmation query result showing all 34 terms with sub-group labels and counts per sub-group
3. The updated cluster assignment for tsa.rar and ra.tsad
4. Any exceptions or schema decisions made that the researcher should be aware of

---

## Compliance note

The directive instruction document (wa-directive-instruction [current]) is not present in the current project files. This directive follows the five-element format described in wa-patch-instruction-v2_10 §1.2 and the programme prose. CC should verify format compliance against the authoritative directive instruction before executing, and flag any discrepancy.

Researcher approval is required before CC executes any operation in this directive.

---

*End of directive*
