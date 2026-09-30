# FLAG rescue — rebuilt from source, validated against 06-01 (2026-06-03)

Redo of the 06-01 deleted-terms / FLAG disposition **from source** on the recovered
**clean May-28 baseline**, using the 06-01 work as a validation cross-check (researcher
direction 2026-06-03). All read-only; **nothing applied**. Truth model per
[findings-deleted-terms-integrity-20260601.md](findings-deleted-terms-integrity-20260601.md) §6.

## Truth model (researcher, 2026-06-01)
Each Strong's once; each verse once; truth = the term is **genuinely used** in the verse
(`span_strong_match=1`), judged on the complete **`term_id`** signal — never `mti_term_id`
(98%, 5,249 legacy NULLs; the weekend mistake that buried 36 real terms). `delete_flagged`
is a *derived* result, never an input. Not clustered **and** has active span ⇒ **FLAG**
(holding pen for relevance review); no active span ⇒ stays deleted.

> "Active span" = `span_strong_match=1` on a **live** verse record (`delete_flagged=0`).
> A term whose only usage sits on deleted verse records is not actively evidenced → not rescued.

## Triangulation — three independent computations agree

| Quantity | My recompute (clean) | Script dry-run (clean) | 06-01 recorded |
|---|--:|--:|--:|
| distinct Strong's | 3,965 | — | 3,965 ✓ |
| CLUSTERED (live M) | 1,626 | — | 1,632 † |
| DELETE — no usage (any-span) | 226 | — | 226 ✓ |
| **Step 1: F-live → FLAG** | 206 strongs | **206 rows** | **206** ✓ |
| **Step 2: span → FLAG (after step 1)** | 108 strongs / 207 rows | **108 / 207** | **108 / 207** ✓ |
| — of which rescued-from-delete | **56** | **56** | 66 ‡ |

† **6-term difference, definitional:** 06-01 marked a Strong's CLUSTERED if *any* row carried an M-code (incl. deleted rows); I require a **live** M-row. 6 strongs have an M-code only on a deleted row. The stricter (live) definition is truer to "attached". *Edge case — flag for confirmation.*

‡ **10-term difference, and this is the headline:** the 06-01 "66 from-delete" was computed on a DB **already corrupted** by the flawed Stream-C/backfill (which had newly delete-flagged ~562 rows). On the clean baseline only **56** of the 108 targets are genuinely deleted. **56 is the correct number; the weekend's 66 was inflated by its own error.** This is the concrete proof that rebuilding from the clean baseline is more correct than replaying the recorded figures.

The **set** of rescued terms (108 strongs / 207 rows) reproduces **exactly** — the target is robust.

## Sequence (validated — order matters)
1. **F-live → FLAG** — `_repair_flag_f_live_v1_20260601.py --apply` → 206 rows (cluster_code NULL→'FLAG'; live, non-deleted; no verse rows touched).
2. **span → FLAG** — `_repair_span_terms_to_flag_v1_20260601.py --apply` → 108 strongs / 207 rows (active-span, not in live M, not already FLAG; sets cluster_code='FLAG', delete_flagged=0, exclusion_reason=NULL). Must run **after** step 1 (so the 206 F-live strongs are already FLAG and excluded — this is what makes step 2 land at 108, not 250).

**Final state:** **314 distinct Strong's** into FLAG (206 ∪ 108), `delete_flagged=0`. FLAG live grows from 126 → ~440 rows. This is the post-rescue `mti_terms.cluster_code` state the `cluster_link` population depends on.

## Caveats / notes
- The span script **writes its report file even in dry-run** (not truly read-only); the 06-01 report was clobbered by my dry-run and **restored from git**. Apply-time it rewrites it dated `20260601` — should be re-dated, but cosmetic.
- Rescued rows keep their stale `status` (e.g. 'delete') while `delete_flagged=0` — to be normalised during FLAG relevance processing (as 06-01 noted), not now.
- `mti_terms` dedup (OT-DBR-009, ~7,581 rows / 3,965 strongs) is **out of scope** here.

## Deferred (NOT part of this step)
The **delete** side — 226 truly-unused + the live-unclustered-no-active-span terms, plus any verse-record cascade — stays held, exactly as the 06-01 plan held it. FLAG-first only, to unblock `cluster_link`.

## Decision needed before any `--apply`
1. Approve the FLAG rescue on the clean baseline with the **fresh** numbers (206 + 108/207, 56-from-delete) — **not** the 06-01 recorded 66.
2. Confirm the two definitional points: (a) CLUSTERED = live M-row only (the 6-term edge); (b) FLAG basis = **active**-span (live verse record), not any-span.
3. Pre-write: take an off-Drive DB backup first.

**Nothing applied. Awaiting go.**
