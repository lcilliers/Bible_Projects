# Applicator Hardening — UPDATE rowcount check

**Author:** Claude Code
**Date:** 2026-04-24
**Scope:** `scripts/apply_session_patch.py` — VC-2 helper and parallel UPDATE paths
**Severity:** HIGH — causes silent data loss across VC / Session B / Session D patch types.
**Status:** Design draft — awaiting researcher approval before implementation.

---

## 1. The bug

When an UPDATE operation's `match` clause resolves to zero rows, the SQL executes successfully with `cursor.rowcount == 0`. The current applicator increments the success counter regardless of rowcount, prints a success line (`verse_context UPDATE id=?`), and moves on. No error is surfaced.

**Impact:** Any declared classification that targets a row the applicator cannot find is silently dropped. The patch appears fully applied; the patch archive misleads future audits.

**Discovered in:** VC-7 pilot, 2026-04-24. VCREVISE OP-003..OP-010 targeted 8 mti=1098 NULL-skeleton rows that M39 had already deleted. Applicator reported `vc_updated: 12` (the SQL count, not the rowcount); actual rows updated: 4. Eight classifications lost. Recovered via follow-on VCRECOVERY patch — but only because the discrepancy was noticed during post-patch validation.

---

## 2. Known paths to harden

Grep `conn.execute("UPDATE ..."` in `apply_session_patch.py` and audit each call for rowcount-check:

| Helper / path | Tables | Notes |
|---|---|---|
| `_apply_versecontext_term_updates` | verse_context, verse_context_group | Direct cause of the pilot bug. |
| `update_mti_status`, `bulk_update_mti_status`, `bulk_*` family | mti_terms | Often targets many rows at once; rowcount==0 still meaningful. |
| `update_evidential_status` | wa_term_inventory | Per-term update; rowcount==0 = term missing. |
| `update_registry` | word_registry | id-keyed; rowcount==0 = wrong registry id. |
| Generic `update` on verse_context / verse_context_group | those tables | Called by VCREVISE/VCGROUP/VCVERSE. |

---

## 3. Proposed fix

Introduce a helper at the UPDATE site:

```python
def _exec_update_strict(conn, sql: str, params: tuple, op_id: str) -> int:
    cur = conn.execute(sql, params)
    if cur.rowcount == 0:
        raise ApplicatorError(
            f"{op_id}: UPDATE matched 0 rows — match clause resolved to nothing. "
            f"Expected at least 1 row. Check target IDs and DB state."
        )
    return cur.rowcount
```

Replace direct `conn.execute("UPDATE ...")` calls inside each UPDATE-emitting op handler with this helper. For bulk updates, the count must be ≥ the count the patch's `_patch_summary` claims (or, minimally, > 0 if the summary is unreliable).

---

## 4. Failure behaviour

On rowcount=0 error:
1. Applicator rolls back the enclosing transaction (already the default — the full patch does not land).
2. Emits a REPAIR failure patch per `wa-patch-instruction [current]` §5 protocol:
   - `PATCH-{date}-{nnn}-REPAIR-FAILURE-V1`
   - One `registry_note` op recording the failing op_id, match clause, and rowcount=0 reason.
3. Preserves current `session_b_status` / `verse_context_status` (no advance).
4. Reports to researcher.

---

## 5. Open questions

- Should bulk_* updates tolerate rowcount=0 as "nothing to do" (idempotent) or fail strictly? Recommendation: strict. A bulk update producing 0 rows is almost always a typo in the match clause.
- Should VCSBFLAGS `insert` into wa_session_research_flags be affected? No — INSERTs are not subject to rowcount=0 semantics in the same way (INSERT either succeeds or fails on constraint).
- How to audit past patches for this class of silent loss? Scan `archive/patches/` for VCREVISE and Session B/D UPDATE ops, simulate match clauses against current DB state, and report any that would have matched 0 rows. Out of scope for this ticket; tracked as a follow-up.

---

## 6. Acceptance

- All existing VC patch tests still pass.
- New test: a VCREVISE-shaped patch with one UPDATE targeting a non-existent (mti_term_id, verse_record_id) tuple fails with a clear error, transaction rolls back, no rows change.
- Post-apply, a REPAIR-FAILURE patch exists in the archive reflecting the failure.

---

## 7. Linked deliverables

- VC instruction v3_5 amendment: `vc-v3_5-instruction-amendment-v1-20260424.md` (§2.4 references this ticket).
- No schema change required.
