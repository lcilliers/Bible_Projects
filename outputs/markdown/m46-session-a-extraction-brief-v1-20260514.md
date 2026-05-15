# M46 — Session A extraction brief (Action Group 5, D5)

**Date:** 2026-05-14
**Source directive:** [Sessions/Session_Clusters/M46/WA-M46-cc-instructions-v1-20260514.json](../../Sessions/Session_Clusters/M46/WA-M46-cc-instructions-v1-20260514.json) — action_group_5
**Status:** queued — not yet executed. Pipeline is independent of groups 1–4 (already applied).

---

## What needs to happen

Eight new terms representing the primary OT and NT vocabulary for the state of being rich/poor and the condition of wealth need to be extracted via the Session A pipeline (STEP Bible → mti_terms → wa_verse_records → M46 assignment), per CLAUDE.md §2 (Data Foundation Pipeline) and §7 (Word Study Pipeline).

These 8 terms are **NOT in mti_terms today** (verified by the pre-flight pass for groups 1–4). They are not exclusions — they were simply never assessed. Standard Session A workflow applies.

---

## Terms — Tier 1 (HIGH priority: core NT wealth/poverty vocabulary)

| # | Strong's | Translit | Gloss | Occ. | Key verses |
|---|---|---|---|---:|---|
| 1 | G4145 | plousios | rich | ~28 | Rev 3:17 · Luk 12:16 · Luk 18:23 · Jas 2:6 · 1Tim 6:17 · 2Cor 8:9 |
| 2 | G4149 | ploutos | wealth, riches | ~22 | Rom 11:33 · Eph 1:18 · Eph 3:8 · Col 1:27 · Rev 5:12 · Jas 5:2 |
| 3 | G4147 | ploutēō | to be rich, become rich | ~12 | Luk 12:21 · 1Tim 6:9 · 1Tim 6:18 · Rev 3:17 · Rev 18:3 |
| 4 | G4148 | ploutizō | to make rich, enrich | ~3 | 2Cor 6:10 · 2Cor 8:9 · 1Cor 1:5 |
| 5 | G4434 | ptōchos | poor, destitute | ~34 | Mat 5:3 · Luk 4:18 · Jas 2:2-6 · 2Cor 8:9 · Gal 4:9 |

## Terms — Tier 2 (MEDIUM priority: OT core)

| # | Strong's | Translit | Gloss | Occ. | Key verses |
|---|---|---|---|---:|---|
| 6 | H6239 | o.sher | riches, wealth | ~37 | Pro 3:16 · Pro 8:18 · Pro 11:28 · Pro 13:8 · Pro 22:4 · Ecc 4:8 · Ecc 5:13-14 |
| 7 | H6223 | a.shir | rich person | ~23 | Pro 10:15 · Pro 14:20 · Pro 18:11 · Pro 22:2 · Pro 28:6 · Ecc 5:12 |
| 8 | H6238 | a.shar | to become rich | ~17 | Pro 10:4 · Pro 13:7 · Pro 21:17 · Pro 23:4 · Pro 28:20 · Hos 12:8 |

---

## Pipeline (per CLAUDE.md §2)

For each English head-word that subsumes these Strong's (likely "wealth", "rich", or "abundance"):

1. **Register the word** (if not already in `word_registry`):
   ```bash
   python -m engine.engine --register --word="wealth" --source="M46 extraction D5"
   ```
   Confirm: is "wealth" / "rich" / "abundance" already a registered word? `python -m engine.engine --db-status` or grep `word_registry`. If yes, skip to step 2.

2. **STEP Bible discovery**:
   ```bash
   python scripts/word_study_extract.py --word wealth --anchors G4145,G4149,G4147,G4148,G4434,H6239,H6223,H6238
   ```
   Produces `research/discovery/{nnn}_wealth_step_data_{YYYYMMDD}.json`.

3. **Audit and populate**:
   ```bash
   python -m engine.engine --mode=audit_word --registry={N}
   ```
   Runs WR-01..WR-20; new mti_terms rows created with `cluster_code=NULL` initially.

4. **Assign to M46**:
   For each newly-created `mti_term`, update `mti_terms.cluster_code='M46'`. Can be a small REPAIR patch or direct UPDATE per the established term-rebind pattern.

5. **Phase 2 (UT review)**: AI reads new verses and authors a VCNEW patch per the cluster instruction §5.

---

## Notes

- **Cross-registry concern**: some of these terms may already be Strong's-extracted under other registries (e.g., G4145 plousios may have been pulled under a different English head-word if "rich" was registered as a separate word). Step 1's existence check should catch this — if any of the 8 terms turn out to already exist in `mti_terms`, the operation collapses to a simple `cluster_code='M46'` UPDATE (no STEP fetch needed).
- **Volume**: total ~176 occurrences across the 8 terms. Tier 1's G4434 ptōchos (~34) and Tier 2's H6239 o.sher (~37) are the heaviest. After extraction, expect M46 to grow from 11 → 19 active terms.
- **No M46 phase regression**: M46 is currently at `Data - In Progress` post-reallocation. Adding new terms post-Phase-2 is permissible (treated as later-arrivals), but AI would need to run Phase 2 (UT review) on the new terms before Phase 3 can include them. Alternatively, extract first and let AI's Phase 3 incorporate the full term set.
- **Recommended sequence**: complete the Session A extraction + M46 assignment before AI re-enters Phase 3 for M46. This avoids partial-data Phase 3 work.

---

*Brief produced by CC. Pipeline execution is a researcher-initiated task (involves STEP server, engine register/audit). Not auto-run from this brief.*
