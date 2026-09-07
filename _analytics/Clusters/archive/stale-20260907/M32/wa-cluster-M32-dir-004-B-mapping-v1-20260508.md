# wa-cluster-M32-dir-004-B-mapping-v1-20260508

**DIRECTIVE ID:** DIR-20260508-003
**Cluster:** M32 — Conscience and Self-Awareness
**Sub-group:** M32-B — Self-Awareness / Inner Attention
**Phase:** 7 (Group-verse mapping application)
**Date:** 2026-05-08
**Author:** Claude AI (analytical)
**Operator:** CC (database execution)
**Governing instruction:** wa-directive-instruction-v1_4-20260506 §11.4

---

## ELEMENT 1 — MOTIVATION

Source documents:
- `WA-M32-B-group-verse-mapping-v1-20260508.md` — Phase 6 mapping for M32-B
- `wa-obslog-M32-conscience-self-awareness-v1-20260508.md` Phase 6, P6.2

The Phase 6 conglomerate-group review found that the existing group 1776 / 3578-001 contains two structurally distinct inner-being phenomena requiring different anchors. The 7 verses of H7896K shit divide into:
- Active inner attention (4 verses: Psa 13:2, Psa 48:13, Pro 24:32, Jer 31:21) — anchor Jer 31:21
- Absent / refused inner attention (3 verses: Exo 7:23, 1Sa 4:20, 2Sa 13:20) — anchor Exo 7:23

This directive retires group 1776 / 3578-001 and creates two new groups (3578-A and 3578-B), reassigning all 7 verse_context rows accordingly.

---

## ELEMENT 2 — SCOPE

### 2.1 Tables touched
- `verse_context_group` — retire group 1776; INSERT two new groups (3578-A, 3578-B)
- `verse_context` — UPDATE group_id on all 7 rows (mti_id=3578); SET is_anchor on anchor verses

### 2.2 Group retirement

**Group 1776 (code: 3578-001)** — RETIRE
- All verse_context rows currently assigned to group_id=1776 will be reassigned to new groups below
- If the schema supports a status or retired flag on verse_context_group, set it; otherwise the group becomes empty and orphaned (no verse_context rows pointing to it)
- CC to advise if a hard delete or soft-retire is the correct DB operation

### 2.3 New groups to CREATE

**New Group 3578-A**

| Field | Value |
|---|---|
| code | 3578-A |
| mti_term_id | 3578 |
| description | The active exercise of the inner-attending faculty — deliberate inner attention directed at a matter, person, or one's own past, sustained with purpose, and productive of learning, repentance, or accurate testimony |
| notes | Split from group 1776 / 3578-001 (Phase 6 conglomerate review, 2026-05-08) |

**New Group 3578-B**

| Field | Value |
|---|---|
| code | 3578-B |
| mti_term_id | 3578 |
| description | The failure, refusal, or social suppression of the inner-attending faculty — the characteristic named by its non-engagement: the person who does not take something to heart, whose attention has collapsed, or who is counselled not to attend |
| notes | Split from group 1776 / 3578-001 (Phase 6 conglomerate review, 2026-05-08) |

### 2.4 Verse_context row assignments

All rows have mti_id=3578. Current group_id=1776 for all. Reassign as follows:

| vr_id | mti_id | Reference | New group code | is_anchor target |
|---|---|---|---|---|
| 132803 | 3578 | Psa 13:2 | 3578-A | 0 |
| 132804 | 3578 | Psa 48:13 | 3578-A | 0 |
| 132802 | 3578 | Pro 24:32 | 3578-A | 0 |
| 132801 | 3578 | Jer 31:21 | 3578-A | 1 (anchor) |
| 132800 | 3578 | Exo 7:23 | 3578-B | 1 (anchor) |
| 132798 | 3578 | 1Sa 4:20 | 3578-B | 0 |
| 132799 | 3578 | 2Sa 13:20 | 3578-B | 0 |

Total: 7 rows reassigned; 2 anchors (one per new group); 0 set-asides; group 1776 becomes empty.

### 2.5 Scope limits
- No verse_context status changes (all already G)
- No cluster_subgroup changes
- No other mti_terms fields modified
- wa_session_research_flags / wa_session_b_findings: unchanged

---

## ELEMENT 3 — OUTCOME REQUIRED

Post-execution state:

| Group code | Verse count | Anchor verse | is_anchor=1 count |
|---|---|---|---|
| 3578-A | 4 | Jer 31:21 (vr_id=132801) | 1 |
| 3578-B | 3 | Exo 7:23 (vr_id=132800) | 1 |
| 1776 / 3578-001 | 0 | — | 0 (retired / empty) |

- Total M32-B verse_context rows: 7 (all assigned to 3578-A or 3578-B)
- is_anchor=1 rows in M32-B: 2 (one per new group)
- Group 1776 empty or retired

---

## ELEMENT 4 — COMPLETION CONFIRMATION

CC runs the following and returns results:

**Query 1 — New group rows exist:**
```sql
SELECT id, code, mti_term_id, description
FROM verse_context_group
WHERE code IN ('3578-A', '3578-B');
```
Expected: 2 rows with the descriptions above.

**Query 2 — Verse assignments and anchors:**
```sql
SELECT vc.vr_id, wr.book_name, wr.chapter_num, wr.verse_num,
       vc.group_id, vcg.code, vc.is_anchor
FROM verse_context vc
JOIN wa_verse_records wr ON wr.id = vc.vr_id
JOIN verse_context_group vcg ON vcg.id = vc.group_id
WHERE vc.mti_id = 3578
ORDER BY vcg.code, vc.is_anchor DESC;
```
Expected: 7 rows; group codes 3578-A (4 rows) and 3578-B (3 rows); is_anchor=1 on vr_id=132801 (Jer 31:21) and vr_id=132800 (Exo 7:23).

**Query 3 — Old group 1776 empty:**
```sql
SELECT COUNT(*) FROM verse_context WHERE group_id = 1776;
```
Expected: 0

**Query 4 — Legacy findings unchanged:**
```sql
SELECT COUNT(*) FROM wa_session_b_findings WHERE mti_term_id = 3578;
```
Expected: same count as pre-directive baseline.

**Query 5 — Application report:**
CC saves a brief application report to:
`Sessions/Session_Clusters/M32/WA-M32-B-group-mapping-applied-v1-20260508.md`
confirming: rows updated, new group IDs assigned by DB, anchor vr_ids confirmed, old group 1776 row count post-operation.

---

## ELEMENT 5 — NOTES

- Companion document: `WA-M32-B-group-verse-mapping-v1-20260508.md`
- Obslog reference: Phase 6, P6.2
- Pre-flight: verify all 7 vr_id values (132803, 132804, 132802, 132801, 132800, 132798, 132799) resolve to the expected references for mti_id=3578 in wa_verse_records before any write
- Pre-flight: verify group 1776 currently has exactly 7 verse_context rows for mti_id=3578
- Halt-on-error if pre-flight fails
- CC to advise on preferred retire mechanism for group 1776 (soft-delete flag vs. leaving empty) — either is acceptable; the group must not retain verse_context rows pointing to it after this directive executes
- After CC confirms this directive, Phase 7 is complete and Phase 8 (catalogue pass) begins

---

*wa-cluster-M32-dir-004-B-mapping-v1-20260508*
*DIR-20260508-003*
*Companion: WA-M32-B-group-verse-mapping-v1-20260508.md*
