# FLAG rescue — apply log (2026-06-03)

Executed the validated FLAG rescue (researcher-approved 2026-06-03) on the recovered clean
May-28 baseline. Scope/validation: [flag-rescue-from-source-validation-20260603.md](flag-rescue-from-source-validation-20260603.md).

## Pre-write safety
- Off-Drive backup: `C:\Users\lerouxc\db_recovery\bible_research_pre_flag_rescue_20260603.db` (220 MB, integrity ok).

## Applied (in order)
| Step | Script | Result | Predicted | Match |
|---|---|---|---|:--:|
| 1 | `_repair_flag_f_live_v1_20260601.py --apply` | 206 rows NULL→FLAG | 206 | ✓ |
| 2 | `_repair_span_terms_to_flag_v1_20260601.py --apply` | 108 strongs / **207 rows** / **56** from-delete | 108 / 207 / 56 | ✓ |

Both: `cluster_code='FLAG'`, `delete_flagged=0`, `exclusion_reason=NULL`. **No verse records touched.**

## Post-state (verified)
- `PRAGMA integrity_check` = **ok**
- FLAG live rows: 126 → **539** (corroborates the lost 06-01 session log's "≈539")
- FLAG distinct live Strong's: **433** (≈119 pre-existing + 314 newly added)
- `cluster_code IS NULL` live (F-live) remaining: **0**
- **G3958** (`paschō`, the proof case): rows 4032 & 5932 → `cluster_code='FLAG', delete_flagged=0` ✓

## Known residual (deferred, as planned)
- Rescued rows keep their stale `status` (e.g. G3958 row 4032 `status='delete'` while `delete_flagged=0`) — to be normalised during FLAG relevance processing, not now.
- The **delete** side (226 truly-unused etc.) remains held.
- `mti_terms` dedup (OT-DBR-009) untouched.

## Report-file note
`_repair_span_terms_to_flag` rewrites `repair-span-terms-to-flag-20260601.md` on apply (misdated). The 06-01 historical record was restored from git; the 06-03 apply output saved as `repair-span-terms-to-flag-apply-20260603.md`.

## Next
The post-rescue `mti_terms.cluster_code` state is now correct → the **`cluster_link` schema + population** step (column add → populate → refresh → set-aside orphans) can proceed against valid term assignments.
