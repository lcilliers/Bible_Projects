# WA-M39-verification-corrections-applied-v1-20260514

**Directive:** DIR-20260514-005 — verification-corrections + closure
**Cluster:** M39 — Blessing, Favour and Grace
**Applied:** 2026-05-14
**Mode:** LIVE
**Backups:**
- Pre-dir-005 full DB: `backups/bible_research_pre_m39_dir005_20260514_074516.db`
- Pre-vc-subgroup-backfill: `backups/bible_research_pre_m39_vc_subgroup_backfill_20260514_074657.db`
- Pre-vc_status-sync (C2 fix): `backups/row_backups/mti_terms_M39_vc_status_sync_20260514T074718.json`

---

## Operations applied

| # | Operation | Outcome |
|---|---|---|
| 1 | te.ev (mti=633) → cluster reassign to M04 | `mti_terms.cluster_code='M04'`; M39-BOUNDARY placement row soft-deleted |
| 2 | dōron (mti=6837) → promote to M39-A | `mti_term_subgroup.cluster_subgroup_id` updated BOUNDARY→A |
| 3 | shay (mti=2976) → set aside | 3 `verse_context` rows: `is_relevant=0`, `set_aside_reason` populated |
| 4 | shay-specific BOUNDARY characterisation at T1.2.1 | INSERT cf_id=6915 |
| 5 | T5.7.2 coverage gap | 2 INSERTs: M39-A finding (cf len=685); M39-B silent (cf len=186) |
| 6 | dōron supplementary findings at 7 M39-A prompts | 7 APPENDs to existing finding_text (T0.4.1, T1.2.1, T2.3.1, T2.6.1, T3.9.1, T4.2.1, T6.3.1) |
| 7 | T6.7 gap resolution | T6.7.1 [A] gap→finding; T6.7.1 [B] gap→finding; T6.7.3 [CLUSTER] INSERT cf_id=6918 cluster_synthesis |
| 8 | cluster.status flip | `Analysis - In Progress` → **`Analysis Completed`** |

All 8 operations applied in a single transaction. FK check passed.

### CC-level follow-up (not in dir-005, but required by §13.8 validator)

Two integrity fixes applied after dir-005 to satisfy the §13.8 validator gate:

- **VC sub-group backfill** — `_apply_m39_vc_subgroup_backfill_20260514.py` populated `verse_context.cluster_subgroup_id` for **739 rows** (M39-A: 606 · M39-B: 130 · M39-BOUNDARY: 3). My earlier dir-002/003 apply script set `group_id` but missed `cluster_subgroup_id`; backfill derives it deterministically from `mti_term_subgroup` placement.
- **vc_status sync** — `_validate_cluster_completion_v1_20260513.py --fix` advanced 7 terms' `vc_status` from `not_done`/`to_revise` to `vc_completed` (60 backing VC rows).

---

## Validation re-run (§13.8 gate)

```
C1 (VC-coverage gap):     0
C2 (stale vc_status):     0
```

§13.8 satisfied.

---

## Final cluster state

| Field | Value |
|---|---|
| `cluster.status` | **`Analysis Completed`** |
| M39 active terms | 15 (was 16 before dir-005; te.ev moved to M04) |
| M39-A | 12 terms (added dōron) |
| M39-B | 2 terms |
| M39-BOUNDARY | 1 term (shay, set aside per §15.2) |
| `cluster_finding` rows | 384 (was 380 pre-dir-005; +1 shay BOUNDARY, +2 T5.7.2, +1 T6.7.3 [CLUSTER]) |
| Status distribution | 353 finding · 5 cluster_synthesis · 26 silent · 0 gap |
| `wa_session_research_flags` | untouched (table-level row count unchanged) |

---

## Outstanding for M39

None for Phase 10. M39 is ready for **Session C cluster publication** per `wa-sessionc-cluster-overview [current]`.

Two upstream items M39 raised but didn't resolve:

1. **te.ev now resides in M04** with a complete `verse_context_group` row (633-001) and `verse_context` row classified `is_relevant=1`. M04 inherits a ready-to-use term when it begins Phase 4. The `mti_term_subgroup` placement is empty (M04 hasn't created sub-groups yet); M04's own Phase 4 will assign te.ev.
2. **Programme-level lesson** captured in [WA-M39-phase10-input-pack-v1-20260514.md](WA-M39-phase10-input-pack-v1-20260514.md) §4 (feedback to AI) and as a v1_12 candidate: Phase 7 apply scripts must populate **both** `verse_context.group_id` and `verse_context.cluster_subgroup_id`. The dir-002/003 directive text said so; my apply script missed it; the §13.8 validator catches the omission. Recommend adding this to v1_11 §10.4 SCOPE bullet as an explicit reminder.

---

## Schema deviations from dir-005 text (applied per actual schema)

| Directive text | Actual schema | Where |
|---|---|---|
| `wa_obs_question_catalogue.prompt_code` | `question_code` | Ops 4, 5, 7 |
| Op 6: "schema allows one row per (obs_id × cluster_subgroup_id)" | unique constraint is `(obs_id, cluster_code, cluster_subgroup_id, version)` — multiple rows permitted with different `version` | Op 6 (chose to APPEND for cleaner shape) |
| Op 7 Step 4: UPDATE T6.7.3 [CLUSTER] gap row | No such row existed (only sub-group-scope T6.7.3 rows). INSERTed new CLUSTER-scope row instead | Op 7 |

---

## Apply script

[scripts/_apply_m39_dir_005_verification_corrections_20260514.py](../../scripts/_apply_m39_dir_005_verification_corrections_20260514.py)

---

*M39 cluster closure complete. Ready for Session C publication.*
