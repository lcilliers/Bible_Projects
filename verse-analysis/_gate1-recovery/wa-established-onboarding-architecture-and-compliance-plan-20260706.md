# Established onboarding architecture + compliance plan for the 97 Gate-1 orphan terms

> Written after the researcher (rightly) rejected the bypass approach: *"We have religiously maintained the standard… I am not keen to have another half-baked index take over mid-air… look back at what the architecture is, what are all the links, how things fit together."* This document maps the **established** architecture from the actual sources (schema trace + engine code), states exactly where my Gate-1 work deviated, and gives a compliance plan that uses the **existing engine tooling** — not a new method. **Nothing is written to the DB by this document.** Date: 2026-07-06.

---

## 1. The established onboarding chain (evidence-based)

Traced from a fully-onboarded term — **H0056 *to mourn*** (registry 71 "grief", cluster M03):

```
word_registry (English word "grief", no=71)         ← the lexical entry point (REGISTER)
  phase1_status, session_b_status, verse_context_status, cluster_assignment
    └─ wa_file_index (WA-071-grief-data-part1/2/3…)   ← STEP data files, word_registry_fk=71
         └─ wa_term_inventory (one row per file×strong)  ← term_owner_type OWNER|XREF, occurrence_count
              ├─ wa_verse_records (ALL occurrences)       ← 39 occurrences → 38 records
              │     file_id, term_inv_id, word_registry_fk, mti_term_id, verse_id,
              │     verse_span_id, context_before/after, morph, stem …  (100% filled)
              └─ verse_context (per verse)                ← 36 rows, mti_term_id
mti_terms (one row per strong)                        ← owning_registry_fk=71, cluster_code=M03,
  owning_word, word_data_reference(=file_id), status     word_data_ref_fk
    └─ mti_term_subgroup → cluster_subgroup           ← cluster membership (the junction cluster
                                                          rework enumerates from)
```

**The engine creates this atomically** (`engine/new_word.py`, NEW_WORD mode N1–N19):
- **N1–N2**: require a `word_registry` row (created by `register.py` REGISTER); check/clear existing `wa_file_index`.
- **N3–N8**: classify each strong OWNER/XREF (via `mti_terms`), **STEP API fetch + span filter** for all occurrences.
- **N9** write `wa_file_index` · **N10** write `mti_terms` (with `owning_registry`, `word_data_reference`) · **N11** write `wa_term_inventory` (+related words) · **N12+** write `wa_verse_records` for **all** filtered occurrences · **N15–N19** meaning parse, flag engine, audit WR-01–WR-20, field-fill, registry update.
- `GAP_FILL` (`engine/gap_fill.py`) fills missing streams (terms with 0 verse-records, NULL meaning) for already-imported words — idempotent, checkpointed.
- **Verse Context** and **cluster assignment** (`mti_term_subgroup`) are subsequent established stages.

### Two facts this makes explicit (both of which I violated)
1. **`wa_verse_records` = every occurrence of a registered IB term**, not a "characteristic subset." Role (characteristic / qualifier / standalone) is a *separate* layer on `ve_lexical` (ve_nr=115). The verse-record is the term-in-verse **foundation**; the role is the **reading** on top of it.
2. **A term is reached only through a `word_registry` English word** and its file/inventory chain. `term_inv_id` + `word_registry_fk` are populated on **100%** of established records; the bypass-FK rule ("don't *join through* `wa_file_index` for data") means query via `verse_id`/`mti_term_id` — it does **not** mean leave the scaffolding empty.

---

## 2. Where my Gate-1 work deviated (the defect)

| Established requirement | What I did |
|---|---|
| term reached via `word_registry` + `wa_file_index` + `wa_term_inventory` | **skipped** — one sentinel `file_index` row, no registry, no inventory |
| `mti_terms` with `owning_registry_fk`, `word_data_reference`, cluster | **thin** rows — ownership/registry/cluster all NULL |
| `wa_verse_records` = ALL occurrences, full scaffolding | **only Psalms characteristic spans**, `term_inv_id`/`word_registry_fk`/context all NULL |
| `verse_context` per verse | **none** |
| `mti_term_subgroup` cluster membership | **none** |

Net: I created a parallel, half-scaffolded index instead of onboarding the terms. My completeness probe passed only because it checked the *bypass* chain (verse→span→mti), not the established scaffolding.

---

## 3. The 97 orphans are three different cases

| Group | Count | Current state | Proper action |
|---|---:|---|---|
| **A — already OWNER** | 9 | `wa_term_inventory` OWNER row survived; OT-DBR-009 deleted the `mti_terms` row | Restore/reconcile `mti_terms` to the existing inventory+registry; GAP_FILL any missing verse-records; cluster-assign |
| **B — XREF only** | 11 | present as cross-refs in other registries; never made OWNER | Decide home registry; promote to OWNER via onboarding; full chain |
| **C — no inventory** | 77 | truly un-onboarded | Full onboarding: assign/REGISTER a word_registry word, NEW_WORD `--fetch-step`, full chain |

(Membership is by base strong; exact counts to be re-verified per group before execution.)

---

## 4. Compliance plan (uses established tooling only)

**Step 0 — undo the bypass (clean slate).** Roll back the non-compliant Gate-1 artefacts so no half-baked index remains: the 1,081 `note='gate1-psalms-2026'` verse-records, the 80 `anchor_note='gate1-psalms-2026'` `mti_terms` rows, the 17 reactivations, and the sentinel `wa_file_index`. Two ways: (a) restore `backups/bible_research.pre-psalms-gate1-*.db` (contains Steps 1–2 roles, **not** the gate1 records); or (b) a surgical, audited delete script keyed on the stamps. **Recommend (b)** — precise, reversible, leaves the role reassessment untouched and verifiable. *The role reassessment (150/150) is correct and stays.*

**Step 1 — registry assignment (the one real decision).** For each orphan strong, determine the English `word_registry` word it belongs to. Many map to existing registries (H2451 wisdom→"wisdom", H8605 prayer→"prayer" if present); others need a new REGISTER. This is a lexical judgement I will propose per strong for your confirmation — not impute.

**Step 2 — onboard via the engine.** Per registry: REGISTER (if new) → `NEW_WORD --fetch-step` (or bulk GAP_FILL) → creates `wa_file_index`, `mti_terms` (owned), `wa_term_inventory` (OWNER), `wa_verse_records` for **all** occurrences (all books), meaning, flags, audit. This answers the earlier "other verses" question correctly: the engine pulls **every** occurrence, programme-wide, as the standard requires.

**Step 3 — Verse Context** for the new terms (established VC stage).

**Step 4 — cluster assignment** into `mti_term_subgroup` (per the mapping in `wa-psalms-gate1-new-terms-cluster-and-occurrence-gap-20260706.md`, confirmed).

**Step 5 — re-run role** (ve_lexical) so the now-onboarded terms' Psalms spans carry the correct characteristic/qualifier/standalone role on the proper foundation, and validate Gate-1 the established way.

### Reconciling with "by book"
Term onboarding is **programme-wide by design** (a term is one entity across all books; the engine pulls all its occurrences). This does **not** break the by-book *reading* discipline: onboarding builds the term-in-verse foundation everywhere; the **role/analysis reading** still proceeds book-by-book. The two are different layers — which is the distinction I collapsed.

---

## 5. What I need from you before executing
1. **Approve Step 0 rollback** (surgical delete of the bypass artefacts) — yes/no.
2. **Confirm the process** is the engine onboarding path above (REGISTER → NEW_WORD `--fetch-step` → VC → cluster), i.e. these terms become first-class programme-wide, all-occurrence, fully scaffolded.
3. Then I'll bring you the **per-strong registry-assignment proposal** (Step 1) for confirmation, and execute group by group with the engine, validating each against the established audit.

*Filed 2026-07-06. Sources: schema trace of registry 71 / H0056; `engine/new_word.py`, `engine/gap_fill.py`, `engine/register.py`; `wa-registry-management-guide [current]`. No DB writes.*
