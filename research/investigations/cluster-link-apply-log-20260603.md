# Pointer cluster_link — apply log (2026-06-03)

Executed the `cluster_link` schema + population on the post-FLAG-rescue DB (researcher-approved
2026-06-03). Scope: [pointer-cluster-link-redo-scope-20260603.md](pointer-cluster-link-redo-scope-20260603.md).
Run **after** the FLAG rescue ([flag-rescue-apply-log-20260603.md](flag-rescue-apply-log-20260603.md)),
so population resolved against the correct post-rescue `mti_terms.cluster_code` state.

## Pre-write safety
- Off-Drive backup: `C:\Users\lerouxc\db_recovery\bible_research_pre_clusterlink_20260603.db` (integrity ok).

## Applied (in order)
| Step | Script | Result |
|---|---|---|
| Column add | `_repair_add_pointer_link_columns_v1_20260601.py --apply` | 4 cols added: `cluster_link`, `cluster_link_basis` on `wa_session_b_findings` + `wa_session_research_flags` (nullable, reversible) |
| Populate | `_repair_populate_pointer_cluster_link_v1_20260601.py --apply` | **2,423 pointers linked** (findings 2,037 + flags 386); basis translit 1,806 / strongs 77 / both 540; 1→1,214, 2→762, 3+→447 |
| Refresh | `_repair_refresh_pointer_cluster_link_v1_20260601.py` (dry-run) | **0 changes** — confirms FLAG-first ordering was correct; populate already used final cluster codes, so refresh is a no-op. **Not applied** (nothing to do). |

## Verification
- `cluster_link` resolves on both tables → audit **D2 `no such column` error cleared**.
- Finding cluster_link distribution (top): M04 1,034 · M05 530 · T2 348 · FLAG 303 · M29 291 · M18 250 · M33 143 · M11 112.
- Unlinked (cluster_link stays NULL): 846 findings + 168 flags (orphan candidates → next step).

## HELD — orphan set-aside (awaiting explicit go)
`_repair_setaside_orphan_pointers_v1_20260601.py` dry-run: **30 orphan findings + 72 orphan flags** —
*exactly* the 06-01 researcher-directed numbers. This step dispositions findings
(`status='set_aside_non_evidenced'`) and flags (`resolved=1`), so it is held for explicit
confirmation rather than auto-applied. (Note: 30/72 < the 846/168 NULL above, because the orphan
test also clears anything carrying a verse ref / catalogue link / SD-ref / Session-C chapter, not
just cluster_link.)

## Deferred
Per-cluster A6/A7 COMMENT_EVALUATION remediation (the larger 06-02 redo) is separate and later.
