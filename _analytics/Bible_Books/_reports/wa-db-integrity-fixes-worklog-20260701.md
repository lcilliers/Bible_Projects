# DB integrity fixes — worklog (2026-07-01)

Living register for the DB fixes arising from the ve-lexical baseline verification. Companion to [wa-observation-dimensions-extract-v1-20260701.md](wa-observation-dimensions-extract-v1-20260701.md) (§7).

## DONE (applied + verified, DB backed up per step)
| # | fix | scope | script |
|---|---|---|---|
| 1 | verse_id backfill | 66 active `wa_verse_records` rows linked to master `verse` index | `_apply_backfill_verse_id_active_20260701.py` |
| 2 | stray XREF lexical cleanup | 187 stray `faculty` rows on delete_flagged records soft-deleted | `_apply_cleanup_stray_ve_lexical_on_deleted_records_20260701.py` |

## PENDING — need a decision

### (c) The 8 verse_context ↔ verse_record mti mismatches — NOT a simple relabel
**Root:** these are the **OT-DBR-009 homonym duplication** surfacing. For each mismatched verse_context, a **sibling "correct-mti" verse_context already exists on the same verse_record**. A naive relabel hits a UNIQUE constraint (`verse_record_id, mti_term_id, group_id, cluster_subgroup_id`). Two patterns:

- **Pattern A — spurious duplicate, correct sibling is active & complete (5 cases):** `2Ch 21:7` (H3772H), `Isa 53:9` (H4820), `Job 31:1` (H1285), `Isa 29:17` (H2803J), `Isa 2:22` (H2803J). The correct verse_context is active with a full lexical; the mismatched one is a redundant wrong-homonym copy carrying its own lexical. → **soft-delete the wrong-mti verse_context + its ve_lexical** (no coverage loss).
- **Pattern B — the correct sibling is soft-deleted, the WRONG one is the only active lexical (3 cases):** `Psa 40:17`, `Psa 41:7`, `Psa 52:2` (all H2803I; correct sibling `df=1`, 0 lexical). Here deleting the wrong one loses the only active lexical. → **re-ground the active verse_context to the correct mti** (different group ⇒ no collision) OR un-delete the correct sibling and regenerate.

**Also flagged:** group 521 (H8267 *sheqer*) has verse_contexts mis-linked onto records of *other* terms (Isa 53:9=H4820, Job 31:1=H1285) — a group-level mis-linkage, not just a label.

**Durable fix = resolve the duplicate homonym `mti_terms` entries (OT-DBR-009).** These 8 are symptoms; they will keep surfacing until the dedup is done.

**DECISION NEEDED:** approve the split fix (Pattern A soft-delete, Pattern B re-ground) — it deletes/moves lexical rows, so I want your nod before applying.

### (b) Complete `arar` (H0779) — 3 missing verses (+ `anash` 2Sa 12:15)
**State:** arar has 52 verse-records; **49 complete** (verse_id + verse_context + 476 lexical). **3 missing** — `Deu 28:17`, `Deu 28:18`, `Gen 9:25` — not in the `verse` master index. (`2Sa 12:15` = `anash` H0605, same gap.) **Total to onboard = 4 verses.**

**3-step completion:**
1. **Ingest** — `_apply_ingest_verse_morphology.py --live` creates the 4 `verse` rows, backfills their `verse_id`, and STEP-fetches morphology. **Tightly scoped: exactly these 4** (0 other verses need morphology). *Ready to run.*
2. **Create `verse_context`** for the 4 term-in-verse records — *this is the VC-pipeline step; no one-shot script in hand.* Method to confirm (onboarding VC catch-up vs a targeted insert).
3. **Generate ve_lexical** — `_apply_generate_ve_lexical_v2.py --live --vcids <new ids>`.

**DECISION NEEDED:** proceed with step 1 now? And confirm the method for step 2 (verse_context creation).

### (d) Complete anchors (excluding T2)
- **T2 filter EXISTS:** `mti_terms.cluster_code = 'T2'` (1,301 terms; FLAG = 75). No new filter needed — usable directly by every operation that must exclude T2.
- **Anchorless OWNER terms carrying ve_lexical: 273.** Of these **76 are T2** (excluded) ⇒ **197 non-T2 terms** genuinely need an anchor.
- **But the anchor-selection rule is not mechanical:** anchors are a *subset* of relevant verses (`is_anchor=1` almost always `is_relevant=1`, but 31,862 relevant verses are *not* anchors). A term can have 1–6+ anchors. So "which verse(s) become a term's anchor" is a rule/judgment, not an obvious fill.

**DECISION NEEDED:** what is the anchor-selection rule? (e.g. the OWNER's primary/first occurrence · every `is_relevant` verse · a researcher pick.) Once defined, completing the 197 is mechanical.

## Parked
- **(e) D1–D14 → ve-lexical catalogue design** — drafted in `wa-ve-lexical-dimension-catalogue-design-v1-20260701.md`, **parked** (researcher: until DB fixes done).

---

## Batch 2 — executed 2026-07-01 (afternoon)

| item | outcome | script |
|---|---|---|
| **Passage layer** | ✅ created `passage` table + `verse.passage_id`; **2,245 passages, 4,412 verses linked** (2,086 auto · 96 extended · 63 cross-chapter flagged for review) | `_apply_create_and_populate_passages_20260701.py` |
| **8 mti mismatches** | ✅ **7 fixed** (4 phantom/dup soft-deleted + 34 lexical rows; 3 re-grounded to correct sub-entry) · **1 HELD** = `2Ch 21:7` (covenant H1285 genuinely in verse, no own record — needs a covenant-onboarding decision, deleting would lose coverage) | `_apply_fix_8_mti_mismatches_percase_20260701.py` |
| **arar 4-verse ingest** | ⚠ **PARTIAL** — 4 `verse` rows created + **verse_id backfilled** (all linked). **Morphology BLOCKED: STEP server down (HTTP 000)** → verse_morphology empty → verse_context + lexical cannot generate. Re-run the ingest when STEP is up, then create verse_context + generate lexical. | `_apply_ingest_verse_morphology.py` |

Each backed up pre-run (`backups/bible_research.pre-*`).

## OT-DBR-009 dedup — SCOPED, not executed (major project)
Investigated the root: **1,565 distinct base-strongs have >1 `mti_terms` row** (5,830 rows total) — but **many are legitimate sub-senses, not errors** (e.g. G2372 anger/wrath = 5 rows). Only **118 homonym groups have active `verse_context` on >1 sub-entry** (real entanglement). A **mass dedup is infeasible/unsafe to auto-run** — each group needs a per-case "real duplicate vs legitimate sub-sense" judgement. The 8 mismatches were its acute *symptoms* (now 7 fixed). **Recommendation:** treat OT-DBR-009 as its own scoped project — start with the 118 entangled groups, per-case, with a review sheet. Not attempted in this batch.
