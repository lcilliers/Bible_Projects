# H2 anomalies — 16 delete-marked terms that are members of an active cluster

> Surfaced 2026-06-15 by the new `_check_softdelete_integrity.py`. After reconciling the 1,180 safe `status='delete'` terms, **16 remain** because they are delete-marked **yet assigned to an active M-cluster** — so the reconcile deliberately left them for your call rather than blindly removing them from a live cluster.

## The 16 (all have **0 active verses, 0 active findings** — empty stubs)
All are *suffering / weakness / grief* terms, almost certainly marked `status='delete'` when **registry 214 'suffering' was excluded** (D1), but they also carry an active cluster code:

| cluster | terms (mti id · strongs · gloss) |
|---|---|
| **M24** (Weakness) | H6039 affliction · H2470A/H *be weak* (×2 each, owner + dup) · H4251 suffering (×2) · G3804/G2552/G3805 suffering · G4777 suffer-with · G3958 to suffer |
| **M21** | H2470B *to beg* (×2) |
| **M03** (Grief) | G3077 grief |
| **M34** | G2553 to endure |

Several are OWNER + `reg=None` duplicate pairs (the OT-DBR-009 pattern again).

## Decision
These are **empty** (no verse/finding evidence) and **delete-marked**, but tagged to live clusters. Two coherent options:

- **A — complete the delete** (set `delete_flagged=1`). They are empty stubs already marked for deletion; removing them strips no evidence from M24/M21/M03/M34 (0 verses, 0 findings). If 'suffering' is later wanted as a real characteristic, it should be built from actual verse evidence, not resurrected empty stubs. `**Decision:** ____`  — *recommended*
- **B — clear the stale status** (set `status` back to `extracted`/NULL, keep them as cluster members). Choose this only if these specific term-slots should remain in M24/M21/etc. despite having no verses. `**Decision:** ____`

Once marked, the fix is one targeted update on these 16 ids (no cascade needed — they have no downstream). `_check_softdelete_integrity.py` will then read fully clean.

## Note on the H2 reconcile already applied
The 1,180 safe terms (delete-marked, NULL/T2 cluster, prior-decided deletes) were cascaded to `delete_flagged=1` this session. Reversal if ever needed: `UPDATE mti_terms SET delete_flagged=0 WHERE status='delete' AND (cluster_code IS NULL OR cluster_code='T2')` (+ their cascaded downstream) — but they were already marked for deletion, so this completes a pending decision rather than making a new one.
