# Unclustered-terms remediation plan

**Type:** living working plan · **Doc version:** 9 · **Created:** 2026-06-01 · **Last updated:** 2026-06-01

> **⚠ CRITICAL (2026-06-01): deletion streams HALTED. See the clear findings statement → [findings-deleted-terms-integrity-20260601.md](findings-deleted-terms-integrity-20260601.md).**
> In short: my evidence guard used `mti_term_id` (documented 98%-complete, 5,249 legacy NULLs) instead of the complete `term_id` (99.99%), so it judged terms with legacy-imported live verses as "empty / safe to delete." Acting on that, today's writes **buried 36 real-evidence terms (1,625 live verses)** including G3958 (you confirmed via STEP). No verse rows were touched → reversible. The 05-28 backup is the exact pre-today state. No reversal/reinstatement performed; awaiting direction.
**Versioning:** version tracked in this header; full history + rollback in git (living-doc policy, `docs/file-organisation-rules.md` §2.3a).
**Supersedes:** the plan-mode scratch file `~/.claude/plans/leave-the-clusters-all-misty-russell.md` (auto-named, no metadata — not a project document). **This is the canonical plan to work from.**

## Context — why

Base-up integrity validation (after cluster-status work was found to be built on an unverified data foundation; all clusters are currently `Analysis - In Progress`). Researcher target end-state: **every term not attached to a cluster must be either (a) soft-deleted with a valid reason, or (b) flagged as an error needing investigation** — nothing live-but-unaccounted, nothing deleted-without-reason.

"Not attached to a cluster" = `mti_terms.cluster_code IS NULL` (`FLAG` and `T2` are registered groupings in the `cluster` table, so they count as *attached*). Grounded in the **documented schema design**, not inference:
- soft-delete requires a recorded reason and is never a physical delete (`wa-patch-instruction §5.4`); the reason field for a term is `exclusion_reason`.
- `occurrence_count` is a STEP **token count, not a verse count** (`docs/field-data-flow-mapping.md`).
- `term_fetch_log.verse_count_*` and `word_registry.phase1_verse_count` are **extraction-time snapshots**, not live counts (`docs/database-table-analysis.md`).

## Supporting reports & scripts (cross-references)

Reports (this folder, `research/investigations/`):
- [cluster-analysis-complete-validation-20260531.md](cluster-analysis-complete-validation-20260531.md) — AC-gate validation that reset all 17 clusters to `Analysis - In Progress` (base-up context).
- [repair-delete-flag-desync-20260601.md](repair-delete-flag-desync-20260601.md) — **Stream C**: 671 flagged, 8 held.
- [unclustered-no-reason-terms-bd-detail-20260601.md](unclustered-no-reason-terms-bd-detail-20260601.md) — **B+D detail** listing (gloss + active verse counts; 21 suspect at top).
- [repair-bd-noreason-backfill-20260601.md](repair-bd-noreason-backfill-20260601.md) — **B+D backfill**: 2,131 updated, 21 held.
- [unclustered-outstanding-items-20260601.md](unclustered-outstanding-items-20260601.md) — **all 313 remaining outstanding terms** in one listing (B/C/D/E/F; gloss + active verse counts + reason + registry; suspect-first) for read-through.
- [g3958-span-survival-test-20260601.md](g3958-span-survival-test-20260601.md) — **G3958 test**: shared-span survival assumption refuted; orphaned-live-verse fault exposed.
- [deleted-but-live-terms-20260601.md](deleted-but-live-terms-20260601.md) — **scope scan**: 37 fully-deleted strongs / 1,626 live orphaned verses + 7 unregistered `term_id`s.

Scripts (`scripts/`, read-only by default; writes need `--apply`):
- [inspect_bd_noreason_terms_v1_20260601.py](../../scripts/inspect_bd_noreason_terms_v1_20260601.py) — builds the B+D detail listing.
- [_repair_delete_flag_desync_v1_20260601.py](../../scripts/_repair_delete_flag_desync_v1_20260601.py) — Stream C flag-apply (guarded).
- [_repair_bd_noreason_backfill_v1_20260601.py](../../scripts/_repair_bd_noreason_backfill_v1_20260601.py) — B+D backfill (guarded).
- [inspect_unclustered_outstanding_v1_20260601.py](../../scripts/inspect_unclustered_outstanding_v1_20260601.py) — builds the single outstanding-items listing (read-only).
- [_repair_flag_f_live_v1_20260601.py](../../scripts/_repair_flag_f_live_v1_20260601.py) — F-live → `cluster_code='FLAG'` (guarded; applied 2026-06-01).
- [inspect_g3958_span_test_v1_20260601.py](../../scripts/inspect_g3958_span_test_v1_20260601.py) — G3958 shared-span survival test (read-only).
- [inspect_deleted_but_live_terms_v1_20260601.py](../../scripts/inspect_deleted_but_live_terms_v1_20260601.py) — corpus scan for deleted-but-live terms (read-only).

## Current status (read-only assessment, 2026-06-01)

3,378 terms have `cluster_code IS NULL`:

| Cat | Meaning | Count | End-state |
|---|---|--:|---|
| A | soft-deleted **with** reason | **3,065** | ✅ OK / accounted (incl. 671 Stream-C flags + 2,131 B+D backfill) |
| B | soft-deleted, **NO reason** | **18** | ❌ held — active evidence (suspect review) |
| C | decided + reason, flag NOT applied (desync) | **64** | ⚠ 8 active-evidence held + 56 `status='excluded'` |
| D | decided, **NO reason**, flag NOT applied | **3** | ❌ held — active evidence (suspect review) |
| E | `candidate_delete` (undecided) | 22 | decision needed |
| F | live `extracted`, unclustered | ~~206~~ → **0** | ✅ **moved to `cluster_code='FLAG'` 2026-06-01** (researcher direction; reassignment, no deletion) |

**Binary (after F→FLAG): 107 still need attention** (B 18 + D 3 + C 64 + E 22) — all held pending the delete-cascade decision in the next section. The 206 F-live are now *attached* (FLAG), so `cluster_code IS NULL` drops 3,378 → 3,172.

*(Progression: start 263 → Stream C +671 → B+D backfill +2,131 → 3,065 resolved; F 206 → FLAG. Assessment query reproducible via the validation artefacts in `research/investigations/`.)*

## Researcher direction 2026-06-01 — disposition of the 313

> "1,2,3,4 can all be processed as deleted and reasons are evident from the data. F live should all be added to the cluster flagged. We will then process the cluster flagged as a separate exercise."

(1–4 = categories B, D, C, E in the read-through listing [unclustered-outstanding-items-20260601.md](unclustered-outstanding-items-20260601.md).)

**Done — F → FLAG (206).** `scripts/_repair_flag_f_live_v1_20260601.py --apply`. Pure `cluster_code` reassignment NULL → 'FLAG'; **no `verse_context`/verse rows touched**; all 143 evidence-bearing F-terms stay live. To be processed as a separate exercise.

**Held — the 107 deletes (B/D/C/E).** Corrected data-level impact (the 3,271 figure first reported was a categoriser bug counting resolved category-A as F; real F = 206):

| Bucket | Terms | With active evidence | Delete would cascade |
|---|--:|--:|---|
| E candidate | 22 | **0** | nothing — clean |
| B | 18 | 18 | 223 verse_context |
| D | 3 | 3 | 4 vc + 7 verses |
| C | 64 | 63 | 1,101 vc + 1,856 verses |
| **Total** | **107** | **84** | **1,328 verse_context + 1,863 verse records** |

**Two open points before any delete is written:**
1. **Cascade (the thambos/cha.lah lesson).** 84 of the 107 carry live evidence. Soft-deleting the *term* alone orphans its classifications; a clean delete must also soft-delete those **1,328 verse_context + 1,863 verse records** (same reason). That removes real analytical content — not a tidy-up — so it needs explicit confirmation, not inference from "reasons evident."
2. **Reasons.** C's 64 already carry an `exclusion_reason` (kept as-is). B 18 + D 3 + E 22 = **43 have none**. Per the no-invented-reasons rule I will not fabricate per-term rationales; proposed uniform meta-reason: `Researcher disposition 2026-06-01: excluded as non-cluster term (review of unclustered listing)`. Awaiting confirmation of the wording.

Once both are confirmed: guarded single-transaction script, dry-run → `--apply`, rowcount asserted, held-set reported. E (clean) can run independently of the 84 if preferred.

## Remediation streams (staged, investigation-first; surface — do not act without per-stream approval)

**Stream C — desync (735): the only mechanical, low-risk fix.** These already carry a valid `exclusion_reason`; only the flag is missing. Apply `delete_flagged=1` **only where evidence-safe** (no active `verse_context`, no active verse records). Guard + dry-run already built in `archive/scripts/_repair_delete_flag_desync_v1_20260601.py` (archived this session; restore to `scripts/` when this stream is run). Of the 679 `status='delete'` reasoned cases, **671 were evidence-safe; 8 held** (the `cha.lah`/`cha.nan` family carry active verse-context — they need a delete-decision review, not a flag).

**Stream B+D — deleted/decided without a reason (2,152): INVESTIGATE, do not auto-fix.** We cannot invent reasons.

**Detail listing (2026-06-01):** [unclustered-no-reason-terms-bd-detail-20260601.md](unclustered-no-reason-terms-bd-detail-20260601.md) — every B+D term with gloss + active verse counts. **Key finding: only 21 of the 2,152 carry live verse evidence** (active verse-records OR active verse-context > 0); the other **2,131 are empty** (zero active verses/classifications). So the problem splits:
- **21 suspect** — deleted with no reason yet still carry evidence (the `cha.lah`-type risk). These need per-term review: reinstate, or delete with a proper reason. Listed at the top of the detail file.
- **2,131 empty — DONE 2026-06-01 (researcher direction):** backfilled `delete_flagged=1` + `exclusion_reason='Bulk deleted, decision not recorded'`. Evidence-safe guard auto-held the 21; no `verse_context`/verse rows touched. Script `scripts/_repair_bd_noreason_backfill_v1_20260601.py`; report [repair-bd-noreason-backfill-20260601.md](repair-bd-noreason-backfill-20260601.md). (The reason is a meta-record — it does not invent an analytical rationale; it states truthfully that the original deletion decision was bulk and undocumented, so these terms can be revisited if ever needed.)

### Worked example — H8001 *she.lam* (Aramaic "peace")

Investigated as a test of the "empty" profile (full trace: term verbatim + fetch log). H8001 **was** extracted (Session-A file `01-wa-117-peace-data-part1-20260317-v1.json`, registry 117 *peace*). Its DB `occurrence_count = 4` (NOT ~240 — that figure is **H7965** Hebrew *shalom*, the cognate this term derives from). Its 4 occurrences are the Aramaic epistolary greeting *"peace be multiplied"* (Dan 4:1, Dan 6:25, Ezr 4:17, Ezr 5:7) — stored as 8 records (OWNER-ish + XREF copies), **all `delete_flagged=1`**. It is an XREF term marked `status='delete'` in both peace registries with no reason. **Conclusion:** a defensible exclusion (greeting-formula cognate of H7965, no inner-being content) that was simply missing its reason — exactly the "empty / backfill" case, now covered. Not lost evidence.

Categorisation by pattern (duplicate / bleed / negation) can refine the 2,131. **No writes until reviewed.**

**Stream E+F — live/undecided unclustered (228): per-term disposition.** For each: route to a cluster, delete-with-reason (bleed), or flag as error. F's 206 live `extracted` terms — first check whether their owning registry has been clustered at all (un-clustered registry = expected-pending; clustered registry = genuine fall-through).

**Stream A (263): no action** — already compliant.

## Critical guard (the thambos / cha.lah lesson)

No term is soft-deleted while it still carries active `verse_context` or active verse records. Every deletion stream applies the evidence-safe guard and reports held-back terms. Reason is always required and retained. (Also: the "active verse count" the `cha.lah` case exposed is unreliable because `wa_verse_records.mti_term_id` ownership ≠ `verse_context` classifications — use active `verse_context` as the evidence signal, not owned verse-records.)

## Verification

- After Stream C apply: category C falls by the flagged count; active `verse_context` / verse rows for flagged terms unchanged (0 touched); held-back list = the evidence-bearing terms.
- Re-run the assessment; the binary moves only by the flagged count, only out of C.
- B+D, E+F counts unchanged until their separately-approved streams run.

## Not doing without separate approval

Stream B+D writes, Stream E+F dispositions, and any reversal of an existing delete — each surfaced, none actioned. The only pre-cleared action is the **evidence-safe Stream C flag-apply** (671 terms).

## Decision log
- _2026-06-01:_ plan migrated from plan-mode scratch file to this compliant living doc.
- _2026-06-01:_ **Stream C applied** (researcher-approved). Set `delete_flagged=1` on the **671** evidence-safe `status='delete'` terms; each retained its existing `exclusion_reason`. Verified shift: A 263→934, C 735→64; B/D/E/F unchanged; no `verse_context`/verse rows touched. **8** active-evidence terms held (cha.lah/cha.nan — need delete-decision review); **56** `status='excluded'` reasoned-but-unflagged left for a separate call. Report: [repair-delete-flag-desync-20260601.md](repair-delete-flag-desync-20260601.md).
- _2026-06-01:_ **B+D detail listing produced** (`unclustered-no-reason-terms-bd-detail-20260601.md`, via `scripts/inspect_bd_noreason_terms_v1_20260601.py`). Of 2,152, only **21 carry live verse evidence** (suspect — per-term review); **2,131 are empty** (missing reason only).
- _2026-06-01:_ **B+D backfill applied** (researcher direction) — 2,131 evidence-safe terms set `delete_flagged=1` + `exclusion_reason='Bulk deleted, decision not recorded'`; 21 held (active evidence). Verified: A 934→3,065, B 1,587→18, D 565→3; C/E/F unchanged; no verse rows touched. *(Apply hit a transient DB lock from an abandoned 40-min background query holding a read lock — killed it, then the write committed.)* H8001 *she.lam* recorded as the worked example.
- _2026-06-01:_ **Researcher direction received** — categories 1–4 (B/D/C/E) to be deleted (reasons evident from data); F-live to FLAG. **F → FLAG applied** (206 terms, `scripts/_repair_flag_f_live_v1_20260601.py`; cluster_code NULL→'FLAG', no evidence touched). Corrected the earlier F=3,271 mis-count (categoriser bug: resolved category-A counted as F; real F=206). Surfaced that **84 of the 107 deletes carry active evidence** (1,328 vc + 1,863 verses) — held pending explicit cascade confirm + reason wording. E's 22 are evidence-free (clean).
- _2026-06-01:_ **G3958 span-survival test** ([g3958-span-survival-test-20260601.md](g3958-span-survival-test-20260601.md)) — assumption that a deleted term's evidence survives under a co-occurring active term is **refuted**: 8/41 verses have no active related term, and the 33 "covered" carry different meanings (verse-presence ≠ meaning-preservation). Exposed that G3958's 41 active verses are orphaned (`mti_term_id` NULL).
- _2026-06-01:_ **Scope scan** ([deleted-but-live-terms-20260601.md](deleted-but-live-terms-20260601.md)) — **37 fully-deleted strongs hold 1,626 live orphaned verses**; 7 unregistered `term_id`s hold more. Real inner-life families (suffering/grief/toil/affliction/voice/joy/anger) sit in the deleted pile.
- _2026-06-01:_ **B+D backfill found FLAWED.** Its `mti_term_id` evidence guard was blind to orphaned `term_id`-linked verses; it mislabelled **103 corpus-live strongs / 3,605 active verses** (incl. heart H3820A/H3824/G2588, soul H5315 family) as "Bulk deleted, decision not recorded". No verse rows touched → reversible. **Deletion streams HALTED.**
- _2026-06-01:_ **Span terms → FLAG (researcher direction).** No reversal taken (most deletes correct). Pushed every not-really-clustered term with ACTIVE span (span_strong_match=1 AND verse record df=0) to `cluster_code='FLAG'`, `delete_flagged=0`, `exclusion_reason=NULL` — **108 Strong's / 207 rows, 66 rescued from delete** (the 37 deleted-but-used + the 107-remainder-with-span, unified). No verse rows touched. Set-aside/relevance call deferred to FLAG processing. G3958 verified rescued. **Note:** rescued rows retain their old `status` (e.g. 'delete'), now stale vs df=0 — to be normalised in FLAG review unless researcher wants it sooner. Script `_repair_span_terms_to_flag_v1_20260601.py`; report [repair-span-terms-to-flag-20260601.md](repair-span-terms-to-flag-20260601.md). Deleted terms with NO active span stay deleted (1,109 used-but-records-deleted + 152 never-used; see [undelete-candidates-20260601.md](undelete-candidates-20260601.md)).
- _2026-06-01:_ **Diff vs 2026-05-28 backup** ([mti-diff-vs-backup-20260601.md](mti-diff-vs-backup-20260601.md)) — today's deletion writes: **1,233 rows newly `delete_flagged` 0→1** (Stream C 671 + backfill D-portion 562); **2,131 rows reason-stamped** (562 were live in backup); 206 cluster (F→FLAG). 0 rows only-in-live, 0 other-reason changes → the backup is the **exact, complete pre-today state**. Clean surgical restore available (revert `delete_flagged`+`exclusion_reason` from backup; keep F→FLAG).
- _Next (awaiting researcher direction):_ (a) **surgical restore** from 05-28 backup to undo Stream C + backfill (both used the flawed `mti_term_id` guard), keeping F→FLAG; (b) re-found the evidence guard on the `term_id` link; (c) re-run the unclustered assessment on the trustworthy signal; (d) reinstate + re-cluster the wrongly-deleted real terms (G3958 first); (e) only then revisit any genuine deletes. **The earlier "107 deletes / cascade" question is withdrawn pending re-validation.**
