# WA-M32-B-group-mapping-applied-v1-20260508

> Application report for `DIR-20260508-003` (dir-004) — M32-B group-verse mapping.
> Cluster: M32 — Conscience and Self-Awareness
> Sub-group: M32-B — Self-Awareness / Inner Attention
> Applied: 2026-05-08 (UTC)
> Outcome: **COMPLETE** — all halt conditions clean.

---

## Summary

| | |
|---|---|
| Old group retired | 1776 (`3578-001`) — soft-retired (`delete_flagged=1`); now empty |
| New groups inserted | 2 — `3578-A` (id=3605), `3578-B` (id=3606) |
| `verse_context` rows reassigned | 7 |
| Anchors set | 2 (one per new group) |
| `wa_session_b_findings` for term 3578 | 0 → 0 (unchanged ✓) |

---

## Q1 — New groups exist

| id | group_code | mti_term_id | description (excerpt) |
|---|---|---|---|
| 3605 | 3578-A | 3578 | "The active exercise of the inner-attending faculty — deliberate inner attention directed at a matter, person, or one's own past, sustained with purpose, and productive of learning, repentance, or accurate testimony" |
| 3606 | 3578-B | 3578 | "The failure, refusal, or social suppression of the inner-attending faculty — the characteristic named by its non-engagement: the person who does not take something to heart, whose attention has collapsed, or who is counselled not to attend" |

---

## Q2 — Verse assignments and anchors

| vr_id | Reference | Group id | Group code | is_anchor |
|---|---|---|---|---|
| 132801 | Jer 31:21 | 3605 | 3578-A | **1** ✓ |
| 132802 | Pro 24:32 | 3605 | 3578-A | 0 |
| 132803 | Psa 13:2 | 3605 | 3578-A | 0 |
| 132804 | Psa 48:13 | 3605 | 3578-A | 0 |
| 132800 | Exo 7:23 | 3606 | 3578-B | **1** ✓ |
| 132798 | 1Sa 4:20 | 3606 | 3578-B | 0 |
| 132799 | 2Sa 13:20 | 3606 | 3578-B | 0 |

7 rows total · 4 in 3578-A · 3 in 3578-B · 2 anchors (one per group).

---

## Q3 — Old group 1776 empty

Active `verse_context` rows in group 1776: **0** (expected 0)

`verse_context_group.delete_flagged` set to 1 with retire-note appended:
> RETIRED 2026-05-08 (DIR-20260508-003): split into 3578-A and 3578-B per Phase 6 conglomerate review.

---

## Q4 — Legacy findings unchanged

`wa_session_b_findings` row count for `term_id=3578`: **0** (baseline 0; no change).

---

## Notes

- Pre-flight verified group 1776 had exactly 7 active vc rows for mti=3578 before any write.
- Pre-existing anchor on vr=132800 (Exo 7:23) was retained — it happens to be the directive's chosen 3578-B anchor, so no anchor toggle was needed there.
- Soft-retire chosen over hard delete (per directive's guidance "either is acceptable; the group must not retain verse_context rows pointing to it"). The retired group remains queryable for audit via `delete_flagged=1`.
- Companion DIR-20260508-002 (M32-A mapping) was applied in the same script run; its outcome is recorded in the script log: group 1643 description refined, vr=1178 and vr=1179 anchors cleared, vr=1177 and vr=82337 anchors retained.

Phase 7 for M32 is now complete. Phase 8 (catalogue pass) can begin.

---

*WA-M32-B-group-mapping-applied-v1-20260508*
*Cluster: M32 — Conscience and Self-Awareness*
*Companion patch script: scripts/_apply_m32_dir003_dir004_v1_20260508.py*
