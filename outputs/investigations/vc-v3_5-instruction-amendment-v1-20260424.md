# VC Instruction v3_5 — Amendment Draft (post VC-7 pilot)

**Author:** Claude Code
**Date:** 2026-04-24
**Supersedes target:** `wa-versecontext-instruction-v3_4-20260424.md`
**Status:** Draft — awaiting researcher approval
**Trigger:** VC-7 pilot on registry 134 (renewal) surfaced two systemic issues that require instruction changes before programme-wide roll-out to the 180 `Verse Context Reset` registries.

---

## 1. Why v3_5 is needed

The pilot applied VCNEW + VCREVISE + VCSBFLAGS under v3_4 contracts. All three patches validated and applied, but two silent data-handling issues emerged:

- **Issue A — pre-seed skeleton collision.** AI produced VCNEW `insert` ops for verses it considered fresh, but those `verse_record_id` values already existed as NULL-skeleton rows (pre-M37 legacy seed). Under strict applicator behaviour the INSERT would hit the (`mti_term_id`, `verse_record_id`) uniqueness constraint. Resolved at DB level via M39 (delete 22,333 strict NULL skeletons). No instruction change for *this* pattern — it is now extinct.
- **Issue B — UPDATE silent-success when row absent.** VCREVISE declared 8 `update` ops to backfill `set_aside_reason` on mti=1098 NULL-skeleton rows. M39 deleted those rows before VCREVISE ran; the 8 UPDATEs matched 0 rows and the applicator reported success. The researcher's explicit set-aside decisions were silently lost and had to be recovered via a follow-on VCRECOVERY patch (8 `insert` ops).

Issue B is not a one-off. Any VCREVISE `update` op that targets a non-existent row under the new skeleton-free model will fail silently. v3_5 must make the rule unambiguous, and the applicator must fail loudly.

---

## 2. Concrete amendments to v3_4

### 2.1 §3.2 — set-aside record rule

**Old (v3_4):** "When a verse has no inner-being engagement, record a verse_context row with `is_relevant=0` and a `set_aside_reason`."

**New (v3_5):** Unchanged in principle, but the *operation* that produces the row depends on whether a row exists:
- No row exists for `(mti_term_id, verse_record_id)` → emit `insert`
- Row exists → emit `update`

The AI determines this from the per-term `.md` header, which v3_5 will extend to list pre-existing `verse_context` row counts per verse (see §4 below).

### 2.2 §6.1 — posture rules

**Old (v3_4):**
- FRESH: no prior verse_context rows → all ops are `insert`
- REFRESH: prior rows exist → operations are `update` on existing rows, `insert` for new

**New (v3_5):** Per-verse rule instead of per-term posture:
- For each verse classified, check the per-term `.md` for `existing_verse_context_row = yes|no`
- If `no` → emit `insert` (regardless of posture)
- If `yes` → emit `update` (regardless of posture)
- Term-level FRESH/REFRESH posture is retained as a narrative hint only (informs AI about how much context to read), no longer controls operation type.

### 2.3 §7.8 — patch application sequence

**Old (v3_4):** Prescribed order VCNEW → VCREVISE → VCSBFLAGS → VCSDPOINTERS.

**New (v3_5):** Same order. Addenda:
- Under no-skeleton model, VCNEW carries `insert` exclusively (new verse_context rows + new verse_context_group rows).
- VCREVISE carries `update` exclusively. If a VCREVISE patch contains `update` with no matching row, the applicator must fail the op and surface the discrepancy.

### 2.4 §7.9 — four-patch catalogue

**Old (v3_4):** VCREVISE `match` clause targets existing rows by `(mti_term_id, verse_record_id)` or by `(mti_term_id, group_code)` for group updates. Silent match-fail possible.

**New (v3_5):** Add a hard self-check to the catalogue:
> VCREVISE ops must fail if the match clause resolves to zero rows. The applicator MUST reject such operations; the AI patch author MUST re-classify the failing verse into VCNEW if the row truly does not exist.

### 2.5 New §3.2b — "no row = not yet analysed"

Under the skeleton-free model, absence of a `verse_context` row for `(mti_term_id, verse_record_id)` is a meaningful state: **the verse has not been analysed for this term.** It is NOT equivalent to "set-aside with no reason." Coverage metrics must count classified + explicit-set-aside rows only; absent rows are "pending."

### 2.6 Change-note entries

Add two items to the v3_5 change note:
- A-06 (new): VCREVISE `update` ops must refuse silent 0-row matches. Operation type is determined by row presence, not by posture.
- A-07 (new): M39 executed on 2026-04-24 — removed 22,333 strict NULL-skeleton verse_context rows. Pre-M37 skeleton model is now obsolete; the skeleton-free model is the contract going forward.

---

## 3. Applicator hardening (coordinated with v3_5)

See `applicator-hardening-rowcount-v1-20260424.md` for the ticket. Summary:
- `_apply_versecontext_term_updates` and related helpers must check `cursor.rowcount` after each UPDATE and fail the op if rowcount == 0.
- Failure behaviour: apply rollback for the whole patch, emit a clear error identifying the op_id and match clause. Follows REPAIR failure protocol in `wa-patch-instruction [current]` §5.

---

## 4. Per-term `.md` renderer change

`scripts/build_session_a_prose.py` must emit, in the per-term header, a new field:

```
existing_verse_context_rows: {count}  # integer; 0 means no row exists for any verse of this term
verses_with_existing_vc_rows: [verse_record_id, ...]  # list
```

This gives the AI classifier the deterministic per-verse signal needed to choose `insert` vs `update`. Under the skeleton-free model the count is usually 0 for FRESH terms, low for REFRESH.

---

## 5. Rollout

1. Merge v3_5 as supersede of v3_4.
2. Apply applicator hardening (rowcount check).
3. Update `build_session_a_prose.py`; regenerate per-term `.md` as needed (no md_version bump required if only the header enriches — confirm with researcher).
4. Start programme roll-out across the 180 reset registries under v3_5.

---

## 6. Open questions for researcher

- Confirm that the 2 out-of-vocab `set_aside_reason` values (`"Material goods/property -- set aside"` 17 rows; `"avf_homograph"` 1 row) should be normalised in a separate REPAIR patch, not as part of v3_5 roll-out.
- Confirm that header-only renderer changes do NOT constitute an md_version bump.
- Confirm §6.1 posture demotion from control to hint is acceptable, or whether posture should remain as gatekeeper with the row-presence check added on top.
