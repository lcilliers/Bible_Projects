# Pointer `cluster_link` redo — scope & sequencing (2026-06-03)

Scoping the "06-01 schema redo" (the audit's `cluster_link` / D2 gap). **Verified against the
live May-28 DB and the actual 06-01 scripts — no writes performed.** Companion to
[wa-db-recovery-assessment-20260603.md](../../outputs/markdown/wa-db-recovery-assessment-20260603.md)
and the [cluster audit](../../Workflow/Programme/Program_reports/wa-programme-cluster-audit-20260603.md).

## Verified finding — the schema redo is NOT a standalone step

The `cluster_link` work is two parts with **different safety and a hard ordering dependency**:

| Part | Script | Safe standalone? |
|---|---|---|
| **Column add** | `_repair_add_pointer_link_columns_v1_20260601.py` | **Yes.** Adds 4 nullable cols (`cluster_link`, `cluster_link_basis`) to `wa_session_b_findings` + `wa_session_research_flags`. Idempotent, dry-run default, doesn't touch `schema_version`, reversible. |
| **Population** | `_repair_populate_…` → `_repair_refresh_…` → `_repair_setaside_orphan_pointers_…` | **No.** Resolves each pointer's link from `mti_terms.cluster_code`. |

**The dependency (verified):** population resolves pointer→cluster from the *current* `mti_terms.cluster_code` assignments, and the refresh script's own docstring states it must run *after* the FLAG triage ("the earlier populate ran BEFORE FLAG terms got real cluster_codes"). The recovered May-28 DB is the **pre-FLAG-rescue** state — confirmed: `mti_terms` FLAG live = **126** vs the **~539** the 06-01 rescue produced. Running population now would:
- resolve fewer FLAG links than intended, and
- the `_repair_setaside_orphan_pointers` step would then **wrongly set aside** pointers that should have linked to FLAG (it set-asides anything with no `cluster_link`).

M-cluster links (the ones that matter for the per-cluster A6/A7 remediation) are unaffected by the FLAG gap, but the FLAG-bound and orphan dispositions would diverge from the intended state. So population must not run on the May-28 term-disposition substrate.

## Verified prerequisite — the 06-01 FLAG rescue is replayable

Both rescue scripts are **fully DB-driven and deterministic** (compute targets from `span_strong_match` and `cluster_code`, not from any lost file), so they reproduce the 06-01 dispositions on the recovered DB:
- `_repair_flag_f_live_v1_20260601.py` — cluster_code NULL + live → FLAG (~206 rows).
- `_repair_span_terms_to_flag_v1_20260601.py` — active-span terms not in an M-cluster → FLAG (108 Strong's / 207 rows, 66 rescued from delete).

## Corrected sequence (for the cluster_link objective)

0. **Pre-write backup** — off-Drive snapshot of `bible_research.db` (the failure domain is gone now that the tree is off Drive, but snapshot anyway). NB engine `EXPECTED_SCHEMA_VERSION` is stale vs DB 3.28.0 → avoid `--migrate`; use the standalone scripts (as 06-01 deliberately did).
1. **Column add** (`_repair_add_pointer_link_columns --apply`) — safe; can run independently. Clears the audit's D2 `ERR: no such column` immediately.
2. **FLAG rescue** (`_repair_flag_f_live --apply`, then `_repair_span_terms_to_flag --apply`) — restores `mti_terms.cluster_code` to the post-rescue state. **Each dry-run first; confirm counts (~206, then ~207/66) before --apply.**
3. **Populate → refresh → set-aside orphans** — now resolves against the correct term state. Dry-run each; expect ~30 orphan findings + ~72 orphan flags at the set-aside step (per the 06-01 script docstring) — confirm before --apply.
4. **Re-run the read-only audit** — D2 resolves; A6/A7 still open (those are the separate per-cluster COMMENT_EVALUATION redo).

## Not yet verified (flagged, not assumed)

The recovery assessment §3 also lists two further 06-01 writes I have **not** yet located/confirmed scripts for — do **not** treat as done:
- **mti_terms dedup** (106 empty dup rows soft-deleted) — OT-DBR-009 territory; script unconfirmed.
- **orphan-VCG dissolution** (125) — a 06-01 variant; `_apply_vcg_dissolution_v1_20260602.py` exists but its scope vs the 06-01 run is unconfirmed.

These need their own verification pass before inclusion. They are downstream of, not blocking, steps 1–3 above.

## Decision needed from researcher
- Approve the corrected sequence (FLAG rescue **before** cluster_link population), or
- Confirm whether to redo the full 06-01 deleted-terms integrity work (the truth-model/undelete analysis behind the rescue) or just replay the two deterministic rescue scripts.

**Nothing above has been executed. Awaiting go before any `--apply`.**
