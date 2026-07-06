# Gate-1 orphan onboarding — COMPLETE (2026-07-06)

> All 97 Gate-1 orphan terms resolved via the compliant engine path (`audit_word --add-terms`). Full itemised audit: [`outputs/markdown/gate1-onboarding-audit-report-20260706.md`](../../outputs/markdown/gate1-onboarding-audit-report-20260706.md). This note is the completion summary.

## Outcome

| | count |
|---|---:|
| **Terms onboarded** (stamped `anchor_note='gate1-onboard-2026'`) | **96** |
| — Group C (fresh onboard, existing/new registries) | 80 |
| — Group B (XREF → OWNER promotion) | 8 |
| — Group A (OT-DBR-009 over-deleted; mti+verses re-pulled into same home) | 8 |
| Excluded (proper noun / third party) | 1 (H7854 *Satan*) |
| **Total accounted** | **97** ✓ |

**Additions:** +96 active mti, +87 OWNER inventory, **+2,579 verse-records**, +7,387 verse_context, +1 registry (`salvation`), across **52 registries**.

## Integrity — clean

- **Collateral check: ✅ delta +0** — every pre-existing (non-gate1) active term preserved; no existing registry lost terms. (Baseline = pre-onboarding census from `backups/bible_research.pre-salvation-onboard-20260706T150356Z.db`.)
- `dup_owner_strong` = 1 (unchanged pre-existing baseline G0150); `velex_orphan_vc` unchanged. **No new invariant breach.**
- Audit framework: `scripts/_audit_gate1_additions_v1_20260706.py` (baseline + reconciliation + collateral detector); ledger `outputs/integrity/gate1_onboard_ledger.jsonl`.

## Method

- Core engine capability built: **`audit_word --add-terms`** (isolated-file additive onboarding into populated registries) — see `wa-audit-word-add-terms-mode-20260706.md`.
- Orchestrator: `scripts/_run_gate1_onboard_batch_v1_20260706.py` (extract → curate → `--add-terms` → stamp → cluster → VC; idempotent skip-guard; sub-entry `RESOLVE` map for 16 split lemmas).
- Every run behind the integrity snapshot/compare gate; rolling backups auto-pruned.

## Issues handled during the run (all resolved)

1. **Sub-entry splits** (16 lemmas, e.g. H2342→H2342I anguish, H8668→H8668G, H4148→H4148G) — resolved to the IB sense from `medium_def` glosses (see `RESOLVE` map).
2. **Re-run duplication** (rejoicing/strife/wisdom re-processed done terms) — 60 dup verse-records + 5 inventory removed; added idempotency guard.
3. **Group A** — OT-DBR-009 had deleted mti **and** verses (empty shells). Restored mti + re-pulled verses; the `--add-terms` RESTORE stream un-flagged old duplicate mti (→ 9 dup mti + 1 dup OWNER inventory), all re-flagged; verse `mti_term_id` backfilled (reused-mti path leaves it NULL).
4. **H7854 Satan** — STEP marks it `action=exclude` (proper noun); left un-onboarded per the researcher's "third party" note; empty stub file removed.

## Deferred to cluster rework (by design — the B2 path)

- **`mti_term_subgroup`** (fine subgroup membership) and **ve-lexical / role** for all 96 terms — membership should emerge from the read, not be imputed. `cluster_code` set where clear (NULL for genuinely-uncertain qualifiers); the stamp + ledger guarantee none are silently dropped.
- **`vr_out_of_corpus` = 167** — occurrences in verses not yet in the measure corpus; resolve as each book is role-reassessed under the corrective pipeline.
- **H7854 Satan** — decision pending: leave excluded, or model as a third-party reference some other way.

*Filed 2026-07-06. The Gate-1 completeness gap (the reason the per-book corrective pipeline exists) is closed at the term/verse-record foundation level; role + subgroup reading follows per-book.*
