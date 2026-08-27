# audit_word `--add-terms` — additive onboarding into existing registries

> New engine capability built 2026-07-06 (at the researcher's direction) to resolve the scaling blocker: audit_word could only onboard into NEW/empty registries; adding orphans to POPULATED registries risked whole-registry re-audit + delete-flagging. `--add-terms` makes the core routine take a curated list of terms for an EXISTING registry and onboard **only those**, leaving existing terms untouched.

## How it works (the isolation design)

`--mode=audit_word --registry=N --extract-file=<curated> --add-terms`:
1. **A1** creates a **fresh, isolated `wa_file_index`** row for the batch (`phase='Phase 1 (audit_word add-terms)'`) and scopes the whole audit to that file only.
2. Because every downstream stream (A4 gap, A6 insert, A7 meaning, A8 flag reset, A9 audit) is scoped to `file_ids`, the registry's **existing files/terms are never in scope** → **no DB_ONLY_TERM delete-flagging, no A8 churn**.
3. The new terms still carry `owning_registry_fk = N` (line ~823), so they belong to the registry.
4. **A8b** (new) sets finishing fields on the new terms: `term_owner_type='OWNER'`, `status='extracted'`, `delete_flagged=0` (`cluster_code` left NULL — analytical, assigned per the mapping).
5. **A10** counts over **all** the registry's files (existing + new) so totals stay correct, and **preserves** `phase1_status`/`session_b_status` (no downgrade of an already-worked registry).
6. **WR-02** audit check updated to exempt registries that have additive files (legitimate multi-file).

Files changed: `engine/audit_word.py` (signature, A1, A8b, A10), `engine/engine.py` (`--add-terms` CLI), `engine/audit.py` (WR-02).

## Validation (corruption / H0444, reg 31)

Pre: 17 active inv, 254 verse-records, at-risk verse-free term H7585 (ti 5029).

Result — **clean**:
- **Existing file 77 untouched**: 17 inv, 254 verse-records; H7585 still active OWNER (the delete-flag risk did NOT materialise).
- **New H0444**: `owning_registry_fk=31`, OWNER, `status=extracted`, `delete_flagged=0`, `cluster_code=M10`; 3 verse-records 100% scaffolded (term_inv_id + word_registry_fk + mti_term_id).
- **Registry status preserved**: `phase1_status='Complete'`, `session_b_status='Verse Context Reset'`; counts refreshed to whole-registry 18/257.
- **Integrity compare**: exactly `mti_active +1, inv_owner +1, verse_records_active +3` — **no collateral, no new invariant breach**. A12 clean. WR-02 now PASS.
- VC created for reg 31 (13 rows = 3 new + 10 pre-existing VC-gap fills — benign scaffolding).

## The repeatable batch recipe (per registry)

1. `word_study_extract.py --word <registry-word> --anchors <orphan strongs>`
2. **Curate** the `terms` array to exactly the intended orphan code(s) (handle sub-entry suffixes, e.g. H8668→H8668G IB sense).
3. `--mode=audit_word --registry=N --extract-file=<curated> --add-terms`
4. Set `cluster_code` per the mapping; `_apply_create_vc_for_onboarded.py --registries N`.
5. Integrity snapshot/compare gate around each batch.
6. Subgroup (`mti_term_subgroup`) + ve-lexical/role deferred to cluster rework (B2).

*Filed 2026-07-06. The blocker in `wa-gate1-onboarding-scaling-blocker-and-options-20260706.md` is resolved via Option A (implemented in the core routine, not a side script).*
