# wa-cluster-M32-dir-003-A-mapping-v1-20260508

**DIRECTIVE ID:** DIR-20260508-002
**Cluster:** M32 — Conscience and Self-Awareness
**Sub-group:** M32-A — Conscience
**Phase:** 7 (Group-verse mapping application)
**Date:** 2026-05-08
**Author:** Claude AI (analytical)
**Operator:** CC (database execution)
**Governing instruction:** wa-directive-instruction-v1_4-20260506 §11.4

---

## ELEMENT 1 — MOTIVATION

Source documents:
- `WA-M32-A-group-verse-mapping-v1-20260508.md` — Phase 6 mapping for M32-A
- `wa-obslog-M32-conscience-self-awareness-v1-20260508.md` Phase 6, P6.1

The Phase 6 mapping of M32-A found both existing groups valid. Group 1643 (suneidō) is retained with a refined description acknowledging the moral-complicity (primary) and cognitive-recognition (secondary) poles. Group 364 (sunoida) is retained unchanged. No new groups are created. No set-asides. Anchors confirmed: Act 5:2 for group 1643; 1Cor 4:4 for group 364.

This directive applies the anchor designations and refined description. All verse_context rows are already status G; no verse_context status changes are required.

---

## ELEMENT 2 — SCOPE

### 2.1 Tables touched
- `verse_context_group` — UPDATE description on group 1643; confirm is_anchor flags
- `verse_context` — SET is_anchor=1 on anchor verses (if not already set)

### 2.2 Group operations

**Group 1643 (code: 454-001) — G4894 suneidō**

Operation: UPDATE description

New description:
> Term names a conscious inner awareness — moral complicity or cognitive recognition — that informs volitional response. The moral-complicity pole (shared inner co-knowing of one's participation in a morally charged act) is the primary conscience characteristic; the cognitive-recognition pole (becoming aware of a situation) represents the term's broader semantic range within the same faculty.

Anchor: `verse_context` row where `(vr_id=1177, mti_id=454)` — Act 5:2 — SET `is_anchor=1`
All other verse_context rows for group 1643 (vr_id 1178, 1179): confirm is_anchor=0

**Group 364 (code: 2739-001) — G6083 sunoida**

Operation: no description change required

Anchor: `verse_context` row where `(vr_id=82337, mti_id=2739)` — 1Cor 4:4 — SET `is_anchor=1`

### 2.3 Verse_context rows — M32-A complete list

| vr_id | mti_id | Reference | Group ID | is_anchor target |
|---|---|---|---|---|
| 1177 | 454 | Act 5:2 | 1643 | 1 (anchor) |
| 1178 | 454 | Act 12:12 | 1643 | 0 |
| 1179 | 454 | Act 14:6 | 1643 | 0 |
| 82337 | 2739 | 1Cor 4:4 | 364 | 1 (anchor) |

### 2.4 Scope limits
- No new verse_context_group rows created
- No verse_context status changes (all already G)
- No set-aside operations
- No cluster_subgroup changes
- wa_session_research_flags / wa_session_b_findings: unchanged

---

## ELEMENT 3 — OUTCOME REQUIRED

Post-execution state:

| Group ID | Code | Verse count | Anchor verse | is_anchor=1 count |
|---|---|---|---|---|
| 1643 | 454-001 | 3 | Act 5:2 (vr_id=1177) | 1 |
| 364 | 2739-001 | 1 | 1Cor 4:4 (vr_id=82337) | 1 |

- Group 1643 description updated to refined text above
- Total M32-A verse_context rows: 4
- is_anchor=1 rows in M32-A: 2 (one per group)
- No other tables modified

---

## ELEMENT 4 — COMPLETION CONFIRMATION

CC runs the following and returns results:

**Query 1 — Anchor check:**
```sql
SELECT vc.vr_id, wr.book_name, wr.chapter_num, wr.verse_num,
       vc.mti_id, vc.group_id, vc.is_anchor
FROM verse_context vc
JOIN wa_verse_records wr ON wr.id = vc.vr_id
WHERE vc.mti_id IN (454, 2739)
ORDER BY vc.group_id, vc.is_anchor DESC;
```
Expected: 4 rows; is_anchor=1 on vr_id=1177 and vr_id=82337; is_anchor=0 on vr_id=1178 and 1179.

**Query 2 — Group description check:**
```sql
SELECT id, code, description
FROM verse_context_group
WHERE id IN (1643, 364);
```
Expected: group 1643 description matches refined text; group 364 unchanged.

**Query 3 — Legacy findings unchanged:**
```sql
SELECT COUNT(*) FROM wa_session_b_findings
WHERE mti_term_id IN (454, 2739);
```
Expected: same count as pre-directive baseline.

---

## ELEMENT 5 — NOTES

- Companion document: `WA-M32-A-group-verse-mapping-v1-20260508.md`
- Obslog reference: Phase 6, P6.1
- Pre-flight: confirm vr_id values (1177, 1178, 1179, 82337) resolve to the expected references for mti_id 454 and 2739 in wa_verse_records before any write
- Halt-on-error if pre-flight fails
- After this directive is confirmed, proceed to DIR-20260508-003 (M32-B mapping)

---

*wa-cluster-M32-dir-003-A-mapping-v1-20260508*
*DIR-20260508-002*
*Companion: WA-M32-A-group-verse-mapping-v1-20260508.md*
