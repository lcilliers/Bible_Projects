# D2b — 343 unlinked verses / 31 Strong's: a decision, not a mechanical backfill

> Surfaced 2026-06-15 while executing D2. After D1 (excluded cascade) + D2a (linked 2,673), **343 active verses across 31 Strong's** remain unlinked. They are **NOT simply "unregistered"** — investigation shows most are **T2 reference terms that were already deliberately soft-deleted** in a prior cleanup. Reviving them to force a link could undo that decision — the exact "quick fix that re-breaks things" pattern we're trying to end. So this needs your call.

## What they are (facts)
All 343 belong to **4 active registries** and are **T2 reference terms** (qualifiers / co-occurring words, not standalone characteristics):

| registry | example Strong's (gloss) | verses |
|---|---|---|
| **R213 'listen'** | H0241G/H/I *ear* · G3775 *ear* · H8086 *hear* · H2796 *craftsman* · G1801 *give ear* | ~290 |
| **R62 'fellowship'** | H2266 *to unite* · H2267 *companion* · H2250 *band* · H4225 *bond* | ~44 |
| **R30 'contrition'** | H3795 · H1793/H1793B *dust* · H4386 | ~10 |
| **R130 'reconciliation'** | G4900 *to meet* | 1 |

Their `mti_terms` state splits three ways:
- **"already soft-deleted"** (e.g. H0241G *ear*, G3775 *ear*, H2266 *unite*, H1793B *dust*) — a row exists, `status='extracted'`, `cluster_code='T2'`, owned by the active registry, but **`delete_flagged=1`** (removed in a prior pass). Their verses were left active and unlinked.
- **"has a `status='delete'` row"** (e.g. H2796, H2795, H2758, H2793H …) — marked for deletion, never soft-deleted.
- **"no row at all"** — H1793 *dust* (R30) only.

## Why this is a decision
These are **T2** — the reference/qualifier layer that, by governing rule, is *never analysed standalone*. The prior soft-deletion of these T2 terms was likely deliberate (a T2 cleanup). Three coherent options — they should be treated **consistently** with how T2 reference terms are handled elsewhere:

- **Option A — soft-delete the orphan verses** (treat them like their already-deleted terms). The terms were removed; their stray active verses should follow, same logic as D1. Net: 343 verses soft-deleted, nothing revived. `**Decision:** ____`
- **Option B — revive the T2 terms + link** (un-soft-delete the rows, create the 1 missing, link all 343). Brings the T2 reference terms back into the data. `**Decision:** ____`
- **Option C — leave as-is** (unlinked, un-morphed). *Not recommended* — leaves exactly the kind of dangling downstream value this whole exercise is removing. `**Decision:** ____`

**My read:** Option A is most consistent — these are T2 reference terms whose canonical rows were already deleted, so the verses are orphans of a completed deletion; soft-deleting them matches D1's principle and the T2-reference rule. But it turns on *why* those T2 terms were deleted, which is your knowledge, not mine.

## Engine side (mechanical, proceeding regardless)
Independent of A/B/C: the create-paths will be made to **check and populate `mti_term_id`** at insert (the D2 "scripts must maintain the field" rule), so unlinked verses are never produced again. That part needs no decision.
