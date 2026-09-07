# wa-cluster-M26-dir-006-BG-cleanup-v1-20260510

**Directive ID:** DIR-M26-20260510-006  
**Prepared by:** Claude AI  
**Date:** 2026-05-10  
**Cluster:** M26 — Righteousness and Justice  
**Sub-groups in scope:** M26-B, M26-E, M26-F, M26-G  
**Governed by:** wa-directive-instruction-v1_4-20260506 §11  
**Source:** WA-M26BG-vsg-actions-v1_0-20260510.md  

---

## DIRECTIVE ID

DIR-M26-20260510-006

---

## MOTIVATION

Following the M26-A1 and M26-A2 restructuring (DIR-003 through DIR-005), a verse-by-verse reading of all remaining M26 sub-groups (B through G) against the current A1 and A2 VSG structures was completed. The finding is that M26-B through M26-G were built with more analytical care than the A1/A2 groups — their VSG structures are largely sound and require no wholesale restructuring.

The actions in this directive are therefore targeted:

1. **Status corrections** — several ungrouped verses are status P (pending) but were determined no_inner_being; they require status = SA with reason set.
2. **BOUNDARY relocations** — a small number of already-SA verses with no group need their sub-group confirmed as BOUNDARY rather than their origin sub-group.
3. **One reassignment within M26-B** — Ecc 12:10 (yo.sher) sits in the wrong VSG.
4. **Two verse assignments** — two ungrouped logizomai verses belong in VSG 3410-001.
5. **Cross-link documentation** — a substantial analytical cross-link registry between M26-B/G VSGs and M26-A1/A2 VSGs has been produced (see WA-M26BG-vsg-actions-v1_0-20260510.md) for CC to record as VSG linkages once schema supports it.

Note on F01: All 56 ungrouped H6186B verses in M26-F are already status SA with reason `no_inner_being` — no status change needed. Their sub-group placement may remain in M26-F as set-aside verses. No BOUNDARY move required for these unless the programme's set-aside policy requires relocation.

---

## SCOPE

**Tables:** `verse_context` — UPDATE status, set_aside_reason, verse_context_group_id  
**Sub-groups:** M26-B, M26-E, M26-F, M26-G  
**No new VSGs required** — all actions use existing groups  

---

## PHASE 1 — Status corrections (P → SA)

These ungrouped verses are currently status P (pending — relevant but unassigned). Close reading confirms they are not inner-being verses. Set `status = 'SA'` and `set_aside_reason = 'no_inner_being'`.

| vr_id | ref | sub-group | term | current status | reason |
|------:|-----|-----------|------|---------------|--------|
| 45950 | Job 33:23 | M26-B | H3476 yo.sher | P | "An angel to declare to man what is right" — mediatorial declaration; the yo.sher qualifies the angelic declaration, not a human inner state. |
| 145645 | Mat 27:3 | M26-E | G2632 katakrinō | P | "Judas saw that Jesus was condemned" — narrative event; the condemnation is of Jesus, not a description of anyone's inner moral state. |
| 145640 | Mar 14:64 | M26-E | G2632 katakrinō | P | "They all condemned him as deserving death" — judicial verdict narrative against Jesus. |
| 145632 | 2Pe 2:6 | M26-E | G2632 katakrinō | P | "Condemned Sodom and Gomorrah to extinction" — historical divine judgment of cities, not inner-being condemnation. |

**SQL pattern:**
```sql
UPDATE verse_context
SET status = 'SA', set_aside_reason = 'no_inner_being'
WHERE id IN (45950, 145645, 145640, 145632);
```

---

## PHASE 2 — One verse reassignment within M26-B

| vr_id | ref | term | current VSG | destination VSG | reason |
|------:|-----|------|-------------|-----------------|--------|
| 232246 | Ecc 12:10 | H3476 yo.sher | `1211-002` (uprightness as path) | `1211-003` (uprightness in speech) | "Uprightly he wrote words of truth" — the yo.sher qualifies the act of writing/speaking truthfully, not a life path. 1211-003 describes "uprightness expressed in speech — words as disclosure of inner integrity." |

**SQL pattern:**
```sql
UPDATE verse_context
SET verse_context_group_id = (
    SELECT id FROM verse_context_group WHERE group_code = '1211-003'
)
WHERE id = 232246;
```

---

## PHASE 3 — Two verse assignments to VSG 3410-001

These two ungrouped logizomai verses belong in VSG 3410-001 (inner reasoning and reckoning — the cognitive inner act of considering and concluding).

| vr_id | ref | term | current status | destination VSG | reason |
|------:|-----|------|----------------|-----------------|--------|
| 101925 | 1Pe 5:12 | G3049 logizomai | SA (ungrouped) | `3410-001` | "As I regard him, a faithful brother" — personal inner assessment of another's character; fits the cognitive inner act of considering/estimating. |
| 101959 | Rom 9:8 | G3049 logizomai | SA (ungrouped) | `3410-001` | "Children of promise are counted as offspring" — divine reckoning/counting; fits the crediting/accounting dimension of 3410-001. |

**Note:** These verses are currently status SA. Assigning them to a group requires resetting `status = 'G'` and clearing `set_aside_reason` as well as setting `verse_context_group_id`.

**SQL pattern:**
```sql
UPDATE verse_context
SET status = 'G',
    set_aside_reason = NULL,
    verse_context_group_id = (
        SELECT id FROM verse_context_group WHERE group_code = '3410-001'
    )
WHERE id IN (101925, 101959);
```

---

## PHASE 4 — Verification queries

**1. Confirm Phase 1 status updates:**
```sql
SELECT id, verse_ref, status, set_aside_reason
FROM verse_context
WHERE id IN (45950, 145645, 145640, 145632);
```
Expected: all 4 rows with `status = 'SA'`, `set_aside_reason = 'no_inner_being'`.

**2. Confirm Phase 2 reassignment:**
```sql
SELECT vc.id, vc.verse_ref, vcg.group_code
FROM verse_context vc
JOIN verse_context_group vcg ON vcg.id = vc.verse_context_group_id
WHERE vc.id = 232246;
```
Expected: `group_code = '1211-003'`.

**3. Confirm Phase 3 assignments:**
```sql
SELECT vc.id, vc.verse_ref, vc.status, vcg.group_code
FROM verse_context vc
JOIN verse_context_group vcg ON vcg.id = vc.verse_context_group_id
WHERE vc.id IN (101925, 101959);
```
Expected: both rows with `status = 'G'`, `group_code = '3410-001'`.

**4. Confirm no remaining ungrouped P-status verses in M26-B through M26-G:**
```sql
SELECT vc.id, vc.verse_ref, mt.strong, cs.subgroup_code
FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
WHERE mt.cluster_code = 'M26'
AND cs.subgroup_code IN ('M26-B','M26-C','M26-D','M26-E','M26-F','M26-G')
AND vc.status = 'P'
AND vc.verse_context_group_id IS NULL;
```
Expected: 0 rows.

---

## ADDITIONAL NOTE — Cross-link registry

The verse-by-verse analysis produced a comprehensive cross-link registry documenting where M26-B through M26-G VSGs analytically correlate with M26-A1 and M26-A2 VSGs. This is not a DB write in this directive — it requires schema support for VSG-to-VSG linkage (the multi-term VSG schema change already in progress).

The full cross-link registry is in `WA-M26BG-vsg-actions-v1_0-20260510.md`. Key relationships for future DB recording:

| M26-B/G VSG | Links to A1/A2 VSG | Relationship |
|-------------|-------------------|--------------|
| 1211-001 (heart quality) | A2-M26-A2-014 | Uprightness of heart ↔ relational orientation toward God |
| 1211-002/003 (path/speech) | A2-M26-A2-017 / A2-M26-A2-011 | Uprightness path ↔ righteousness path; upright words ↔ speech as expression |
| 1212-001 (judicial equity) | A1-M26-A1-002 | Divine equity in judgment ↔ God's righteous judgments |
| 1214-001 (uprightness refused) | A2-M26-A2-004 / A2-M26-A2-003 | Uprightness absent/refused ↔ far from righteousness / distortion |
| 1218-001 (messianic uprightness) | A1-M26-A1-007 | Scepter of uprightness ↔ Messianic righteousness |
| 947-001 (can man stand before God?) | A2-M26-A2-002 | OT question ↔ Ezekiel precarious standing — same problem |
| 3194-001 (divine justification) | A1-M26-A1-004 | Justification ↔ God's righteousness acting to save |
| 3410-001 (faith credited) | A2-950-001 | Rom 4 reckoning ↔ righteousness received through faith — same theological territory |
| 1225-001 (acting wickedly) | A2-M26-A2-003 / A1-M26-A1-006 | Wickedness ↔ distortion of righteousness / human unrighteousness exposed |
| 3208-001 (accountability) | A1-M26-A1-006 | Universal accountability ↔ standard exposing all human unrighteousness |

---

*DIR-M26-20260510-006 | Prepared by Claude AI | 2026-05-10 | Cluster M26 | wa-directive-instruction-v1_4-20260506 §11*  
*Source: WA-M26BG-vsg-actions-v1_0-20260510.md*
