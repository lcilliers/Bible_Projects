# Session log — 2026-06-01 — deleted-terms integrity & FLAG rescue

**Type:** session log · **Date:** 2026-06-01 · **Focus:** base-up integrity of the term registry; correct disposition of terms not attached to a cluster.

## Summary

Continued the unclustered-terms remediation, which turned into a base-up integrity correction after G3958 exposed that the evidence signal in use was unreliable. Net result: the truth model for term disposition is now defined and documented, the genuinely-used terms wrongly sitting in `delete` were rescued to the `FLAG` holding cluster, and the documentation + this log were updated. No verse records were ever touched.

## What happened (chronological)

1. **F-live → FLAG (206).** Earlier researcher direction: live `extracted` unclustered terms (category F) moved to `cluster_code='FLAG'` for separate processing. Non-destructive reassignment. Script `_repair_flag_f_live_v1_20260601.py`.
2. **G3958 probe.** Researcher asked to test the "shared-span survival" assumption on G3958 (*paschō*, "to suffer"). Found: G3958 had 41 active verses under `term_id` but 0 under `mti_term_id` (orphaned). Researcher confirmed via STEP that G3958 is a **real term wrongly deleted**. Assumption refuted ([g3958-span-survival-test-20260601.md]).
3. **Scope + root cause.** Scan found 37 fully-deleted Strong's holding 1,626 live orphaned verses. Root cause: the evidence guard used `mti_term_id` (documented 98%, 5,249 legacy NULLs) instead of the complete `term_id` (99.99%). Today's two earlier streams (Stream C 671 flags + B+D backfill 2,131) rested on this flawed signal; they buried 36 real-evidence terms (1,625 live verses) and I gave a false "evidence-safe / 2,131 empty" assurance.
4. **Findings statement.** On researcher instruction, produced a clear findings doc separating: (a) pre-existing documented `mti_term_id` gap (not mine), (b) my flawed method, (c) my write actions; with what should have been done and explicit limits ([findings-deleted-terms-integrity-20260601.md]).
5. **Truth model agreed (researcher).** Each Strong's once; each verse once; truth = `span_strong_match=1` (term actually used). Not clustered → has span ⇒ FLAG (relevance review → cluster/set aside); no span ⇒ delete. `delete_flagged` is derived, never input.
6. **No reversal (researcher).** Most deletes are correct; do not reverse en masse. Instead inspect deleted terms for undelete candidates = those with active span. Found 37 (the rest: 1,109 used-but-records-deleted + 152 never-used stay deleted) ([undelete-candidates-20260601.md]).
7. **Span terms → FLAG (researcher direction).** Pushed every not-really-clustered term with active span to `cluster_code='FLAG'`, `delete_flagged=0`, `exclusion_reason=NULL` — **108 Strong's / 207 rows, 66 rescued from delete** (the 37 + the 107-remainder-with-span, unified). Script `_repair_span_terms_to_flag_v1_20260601.py`; G3958 verified rescued. FLAG now ≈539 live rows.

## DB writes this session (all on `mti_terms`; zero verse records touched)
- F→FLAG: 206 rows (`cluster_code` NULL→'FLAG').
- Span-terms→FLAG: 207 rows (`cluster_code`='FLAG', `delete_flagged`=0, `exclusion_reason`=NULL).
- (Earlier, now superseded by the truth model: Stream C 671 flags + B+D backfill 2,131 reason-stamps — left in place per researcher; the genuinely-used among them were pulled back out by step 7.)

## Documentation updated
- `docs/database-table-analysis.md` — added the 2026-06-01 term evidence/disposition model header note; tightened `mti_terms` (delete_flagged not an evidence signal; dedup target OT-DBR-009) and `wa_verse_records` (`span_strong_match`=usage truth; use `term_id` not `mti_term_id` for evidence).
- `research/investigations/unclustered-terms-remediation-plan.md` — living plan to Doc version 9; banner points to findings.

## Open items / notes
- **Stale `status`** on rescued FLAG rows (e.g. G3958 still `status='delete'` while live in FLAG) — to be normalised during FLAG relevance processing.
- **`mti_terms` dedup (OT-DBR-009)** still pending — 7,571 rows vs 3,955 unique Strong's.
- **Verse dedup** — OWNER/XREF duplicate verse rows (e.g. G3958: 123 rows / 41 distinct refs) still to be addressed.
- **FLAG relevance pass** — the staged exercise to disposition FLAG terms (cluster vs set aside) is queued, not started.
- Stream C + B+D backfill remain applied (not reversed) per researcher.

## Next focus
**Session B and Session D pointers** (per researcher) — to begin next session.

## Key artefacts (research/investigations/)
findings-deleted-terms-integrity-20260601.md · term-disposition-by-span-20260601.md · undelete-candidates-20260601.md · deleted-but-live-terms-20260601.md · g3958-span-survival-test-20260601.md · mti-diff-vs-backup-20260601.md · today-writes-severity-20260601.md · repair-span-terms-to-flag-20260601.md
