# Session log — 2026-06-15 · data-integrity remediation + engine hardening

> A long, multi-phase session. Began as the next step of the L1/L2 field work (mode → sense), but a consistency question pulled the thread on a chain of stacked quick-fixes, which became a full data-integrity remediation + engine hardening. All work reversible, committed, and verified. Companion to `wa-sessionlog-20260614-l1l2-field-reliability-and-morph-backfill-v1.md`.

## The arc (how one question unravelled the rest)
"Does each verse have a value for mode, and is it consistent?" → led to: mode is consistent (bedrock), but the **language** field was derived from the **Strong's prefix** (Aramaic-blind) → fixing *that* properly surfaced that **morph was only ever set by a side-backfill, never at verse creation** → which surfaced that **`wa_verse_records.mti_term_id` is written by NO maintained code at all** → which surfaced **excluded registries left with live downstream**, **`status='delete'` rows never soft-deleted**, and finally **`wa_file_index` being a legacy crutch with a half-built FK-bypass**. Each was a quick-fix that made a point-in-time view look right without maintaining the downstream — the researcher's thesis, proven repeatedly.

## What was done

### A. Field-consistency checks (the entry points)
- **Mode (#4)** — confirmed bedrock/consistent. Fixed two residues: **210 Aramaic verb stems** (Heb-only stem map) + 1 Nithpael (`scripts/_apply_aramaic_stem_backfill_v1`); hardened the canonical parser. Visual: `outputs/markdown/wa-mode-field-visual-20260615.md`.
- **Language vs mode** — caught my own checker mis-flagging Greek `ADV`/adjectives as Aramaic; built **canonical `scripts/analytics/morph_util.py`** (one classifier). Then the root: **language morph-authoritative** (`_apply_language_reconcile.py` wired into the morph backfill) — 121 terms Hebrew→Aramaic; `meaning_parser`/`audit`/`new_word` now treat Aramaic as Hebrew-script. **Testament vs books = 0 mismatches.**

### B. Data-integrity remediation (all reversible)
- **D1** — excluded registry ⇒ soft-delete entire downstream: **2,513 rows** across 12 registries (`_apply_excluded_registry_cascade.py`), safe (0 sharing).
- **D2a** — linked **2,673** broken-link verses to their `mti_terms` row (`_apply_link_mti_term_id.py`); resolved 8 OT-DBR-009 `status='delete'` duplicate blockers.
- **Morph cascade** over the 2,673 — done **targeted** after the researcher flagged the cluster-tool as a blunt instrument (added `--strongs` mode; 13 terms not 16 clusters).
- **D2b → A** — 343 orphan verses of already-deleted T2 terms soft-deleted (`_apply_softdelete_orphan_verses.py`, 1,329 rows).

### C. Engine soft-delete hardening (H1–H5)
- **`engine/softdelete.py`** — one shared cascade path (registry/term/verse), reconcile, integrity. Now uses the **bypass FK**, not file_index joins.
- **H3** wired into `audit_word` DB_ONLY_TERM (term delete cascades to verses→context→findings).
- **H2** reconcile (cluster-aware): 1,180 safe delete-marked terms cascaded; **16 anomalies** (empty suffering/weakness terms in active clusters, fallout of the R214 exclusion) resolved via option A.
- **H5** `scripts/_check_softdelete_integrity.py` + an audit-end (A12) warning. It immediately earned its keep, catching invariant breaks the others missed.

### D. H4 — link + morph at the SOURCE
- `get_verse_records[_with_html]` now parse `morph_code`+`stem` at the source (canonical `morph_for_span`); `audit_word` create-path writes `mti_term_id`+`morph_code`+`stem` at INSERT (was **100% unwritten**).
- **Validated** on a live audit of R211 'being': 497 inserted 0 errors, link-at-insert 511/572, A12 caught the residual 61 orphans of a dead term (H7919B), cleaned.

### E. new_word retirement + file_index / bypass-FK (M58, schema → 3.32.0)
- **Finding:** new_word/gap_fill superseded for *auditing* but `audit_word` depended on them for `wa_file_index` creation — retirement was never completed.
- **wa_file_index** is legacy but COMPLETE; the **FK-bypass was half-built** (file_index + mti had registry FKs; the bulk verse/term tables did not).
- **M58 migration:** added `word_registry_fk` to `wa_verse_records`+`wa_term_inventory`, backfilled **61,846 + 6,846** (0 misses). `audit_word` now **creates a file_index stub** on onboarding + writes the bypass FK — removing the manual new-word ordeal. New code never joins through file_index.

## Key observations / governing lessons (banked to memory)
- **morph_code is the source of truth**; stem/language/mode/link all DERIVE from it and must be maintained wherever it changes ([[project_morph_is_source_of_truth]]).
- **Fix the derivation at its source, not the symptom** — caught about to plaster (overwrite a field / patch one checker) when the root was the prefix-derivation bug ([[feedback_no_patch_to_nice_pointintime_result]]).
- **General-use scripts must leave downstream values correct** — the cascade of unmaintained downstream (link, morph, exclusion, status-flag) was the fragility.
- **wa_file_index is legacy/stub only — never join through it; use the bypass FKs** ([[reference_file_index_legacy_use_bypass_fks]]).
- **Adding a new word = treat with care** — onboarding path wired but not validated from scratch.
- Process: NEVER AskUserQuestion; investigate before asking (answer from data); reversible + verified over quick.

## DB state changes (all reversible)
morph stems +211 · language 121→Aramaic · D1 −2,513 (soft) · D2a +2,673 links · morph +~3,400 · D2b-A −1,329 (soft) · H2 −1,180+16 terms (soft) · R211 +497 verses (−61 orphans) · **M58: +word_registry_fk on 68,692 rows · schema 3.32.0**.

## Open / next
- **Sense (#1)** — the next field. Works off the **STEP per-occurrence subgloss** (mechanical floor); the gloss/subgloss tables must be brought into the operation (this session's end-point).
- The **16 H2 anomalies** and **D2b** are resolved; integrity is **0/0/0**.
- Before archiving new_word/gap_fill: one genuine end-to-end new-word run through audit_word.
- Deferred: finish-the-FK-bypass migration A (drop file_index entirely) as its own project; backfill ~80 missing `mti_terms.owning_registry_fk`.
