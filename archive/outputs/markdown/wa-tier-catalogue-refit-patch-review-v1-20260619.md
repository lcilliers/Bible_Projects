# Tier-catalogue refit — patch review (awaiting approval) · 2026-06-19

**Instruction source:** [wa-tier-catalogue-cc-update-v1_0-20260619.md](../../Workflow/Tiers/wa-tier-catalogue-cc-update-v1_0-20260619.md)
**Patch built:** [`Sessions/Patches/wa-tier-catalogue-refit-update-v1-20260619.json`](../../Sessions/Patches/wa-tier-catalogue-refit-update-v1-20260619.json) (173 ops)
**Builder (read-only):** `scripts/build_tier_catalogue_update_patch_20260619.py`
**Target:** `wa_obs_question_catalogue` · **Status: NOT applied** (per GR-PROG-005/GR-PROC-004 — review first).

## What the patch does

| Op class | Count | Effect |
|---|---|---|
| TEXT-UPDATE (keep) | 126 | `question_text` ← de-biased v2_1 rewrite |
| SOFT-DELETE (obsolete) | 47 | `deleted = 1` + fold target in `review_note` |
| **total** | **173** | active tiered **173 → 126**; no insert, no renumber, no hard delete |

## Validation (all green)

- Doc parsed exactly **126 + 47 = 173**; sets disjoint; **A∪B == the 173 active DB codes** (none missing, none extra).
- All 47 fold-targets are keep-codes; no duplicate `question_code`.
- **Simulated full apply (rolled back):** all 173 ops matched **exactly one row**; post-state active tiered = **126**; 47 carry the fold note; the 5 flagged keep-codes (T2.1.1, T2.1.2, T1.7.2, T2.9.1, T2.10.1) carry the new text.
- `apply_session_patch.py --dry-run` (structural) passes.

## Two points for your confirmation

1. **Fold provenance → `review_note`.** No dedicated `folded_into` column exists. The instruction allowed holding the mapping in the doc only; I went further and recorded it per-row as `review_note = "folded_into=<primary> · tier-catalogue v2_1 refit 2026-06-19 · <reason>"`, so the fold is reversible and self-documenting in the DB. Say if you'd rather leave `review_note` untouched.
2. **2 no-op text-updates** — T6.5.2 and T7.1.3 already hold the rewritten text (their UPDATE changes nothing). Harmless; flagged for transparency.

## Mechanism note

`apply_session_patch.py` previously supported only `insert` on this table. I added an `update` handler
(match on `question_code`, strict 0-row rejection) mirroring the existing `verse_context` update path.

## To apply (on your go-ahead)

```
python scripts/apply_session_patch.py Sessions/Patches/wa-tier-catalogue-refit-update-v1-20260619.json
```
(auto-backs-up the DB first). Then I re-run the post-run verification (queries 1–5 in the instruction) and report.
