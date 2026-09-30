# L1 sweep — pre-launch state & rollback (fallback reference)

> **Fallback snapshot · 2026-06-08 · CC.** Captures the exact state before the all-clusters L1 angle-sweep
> begins, so we can roll back cleanly if a systemic failure appears. Read this first if anything goes wrong.

---

## 1. State of play (2026-06-08)

- **Schema:** v3.29.0 (M55 applied; morph_code/stem/sense fields exist).
- **Git:** branch `main`, last commit `0ae1124` (strategy: L1 sweep all clusters before synthesis). All work
  pushed to `github.com/lcilliers/Bible_Projects`.
- **Prototypes validated (read-only):** morph extraction (100% M01), meaning run (ya.re stem→branch),
  P1 keywords (85/85 self-check), scenario typing (S0–S6), keyword digestion. Scripts:
  `_prototype_step_morph.py` · `_prototype_meaning_run.py` · `_prototype_p1_keywords.py` ·
  `_assess_p2_verse_scenarios.py` · `_apply_t2_soft_delete.py`.
- **T2 cleanup:** 480 active (106 never-co-occur soft-deleted, reversible).
- **DB write state:** `wa_verse_records.morph_code`/`stem` are **0% populated** (about to backfill).
  M01 has **no L1 meaning writes** (the failed first L1 was reverted). `verse_context` L1 fields NULL.
- **HELD:** full L2 synthesis (verse read + DB writes) is held until the cross-cluster roll-up is read.
  V3_2 full execution parked.

## 2. Backups (fallback DB copies)

| File | When | Marks |
|---|---|---|
| `backups/bible_research_pre_l1_sweep_20260608.db` | **this launch** | before any sweep write |
| `backups/bible_research_pre_t2_softdelete_20260608.db` | earlier today | before T2 soft-delete |
| `backups/bible_research_pre_v3_2_20260608.db` | earlier | before M55 + dedup |
| `backups/bible_research_pre_L1_M01_20260608.db` | earlier | before the failed first L1 |
| NAS daily | 18:00 / 18:30 | DB + full mirror (`\\LSUK-SYNRACK\…`) |

## 3. The sweep plan — layers × batches × review points

**Layers (angles, run one at a time across clusters):**
- **L0 morph backfill** — one-time DB write (`morph_code`/`stem` from STEP). *The only structural write of
  the sweep; everything after is read-only reports until synthesis.*
- **A morph/stem** · **B sense-branch + meaning run** · **C keyword + self-check** · **D keyword digestion**
  · **E scenario typing** · **F span/qualifier-attach** — all **read-only**, emit per-cluster reports +
  feed the **cross-cluster roll-up**.

**Batches:** clusters processed in groups (default ~8–10, or by synergy group), validated cluster-by-cluster
within L0.

**Review points:** after the L0 M01 validation; after L0 completes; after each read-only layer's roll-up.
A review point inspects the report for systemic failure before the next batch/layer.

## 4. Rollback procedure

- **Undo a morph backfill (or any sweep write):** restore the pre-sweep DB —
  `cp backups/bible_research_pre_l1_sweep_20260608.db database/bible_research.db`. (morph_code/stem are
  additive columns, so a targeted `UPDATE … SET morph_code=NULL, stem=NULL` also reverts without a full
  restore.)
- **Undo code/report changes:** `git revert <commit>` or check out `0ae1124`.
- **Nothing in the read-only layers (A–F) writes to the DB** — those produce only `.md` reports; deleting the
  report files is the only undo needed.
- The **synthesis (L2) is the only writer** after L0, and it is HELD pending the roll-up review — so no
  irreversible analytical writes happen during the sweep.

## 5. Invariants to watch (systemic-failure guards)

1. **Reference match-rate** on the morph backfill (STEP ref ↔ `wa_verse_records.reference`) must be ~100%;
   a low rate = a matching bug → STOP and fix before scaling.
2. **Stem decode** sanity (verbs get a stem; nouns don't) per batch.
3. **No double-writes:** a verse-occurrence gets one morph (the term's own span).
4. Each read-only layer's totals reconcile to the cluster's known verse/term counts.
