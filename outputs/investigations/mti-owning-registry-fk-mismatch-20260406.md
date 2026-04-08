# mti_terms.owning_registry_fk Mismatch Investigation

> Generated: 2026-04-06
> Scope: 58 mti_terms rows where owning_registry_fk ≠ OWNER wa_term_inventory registry
> Purpose: Root cause analysis before remediation

---

## Finding Summary

58 mismatches fall into **two distinct mechanisms**, not three. Mechanism 3 (XREF confusion) is the primary cause. Mechanism 2 (registry restructuring) is a secondary cause. Mechanism 1 (data entry error) is not evidenced.

---

## Mechanism Analysis

### Mechanism 2 — Registry restructuring (22 terms)

**Pattern:** `mti_terms.owning_registry_fk = 154 (stupor)` but OWNER in `reg 151 (sorrow)`

**Evidence:**
- Registry 154 (stupor) is `phase1_status = Excluded`
- It has 0 file_index entries, 0 OWNER terms — completely empty
- Notes field: *"Originally mislabelled as stupor. Data files were sorrow. All data re-linked to word_registry.id=151 (sorrow) on 2026-03-19. This row is a data entry error and is now redundant."*
- All 22 terms have `owning_registry` text = `'154'` — the text was never updated either
- The wa_term_inventory OWNER rows were re-linked to reg 151, but `mti_terms.owning_registry_fk` was not updated

**Conclusion:** Registry merge on 2026-03-19 moved wa_term_inventory but left mti_terms pointing at the defunct registry. Clear Mechanism 2.

**Scope:** Exactly 22 terms. Isolated to the 154→151 merge. No other excluded registries show this pattern.

### Mechanism 3 — XREF terms with FK pointing to XREF registry instead of OWNER registry (36 terms)

**Pattern:** `mti_terms.owning_registry_fk` points to a registry where the term has an **XREF** row, while the **OWNER** row is in a different registry.

**Evidence:**
- All 36 terms have an XREF row in the FK registry — confirmed by query
- The `owning_registry` text field agrees with the OWNER registry (not the FK) in all 36 cases
- This means: the text field was set correctly at registration, but the FK was set to the wrong registry

**Sub-patterns:**

| FK points to | OWNER is in | Count | Interpretation |
|---|---|---|---|
| 112 (mind) | 20 other regs (conscience, counsel, desire, intention, memory, purpose, reasoning, repentance, self-control, thought, heart) | 20 | mind has XREF copies of terms owned by many C02/C01 registries |
| 197 (authority) | 177 (worth), 187 (strength), 196 (power), 199 (dominion) | 16 | authority has XREF copies of C20 cluster terms |

**Root cause:** When `mti_terms` was populated, `owning_registry_fk` was set based on which registry the term was *first encountered in* or *most associated with*, rather than which registry holds the OWNER `wa_term_inventory` row. The XREF architecture (OWNER/XREF split) was implemented later, and `owning_registry_fk` was not reconciled to match the OWNER path.

**Confirmation:** The `owning_registry` text field stores the correct OWNER registry number in all 36 cases — the text was set from the wa_term_inventory path, but the FK was set independently (possibly from mti_term_cross_refs or from the original STEP import context).

### Mechanism 1 — Data entry error: NOT evidenced

No terms show a pattern consistent with random data entry error. All mismatches fall cleanly into Mechanism 2 (22 terms, one known merge) or Mechanism 3 (36 terms, XREF FK mismatch).

---

## Impact on Dimension Index

The `populate_dimension_index.py` script joins `mti_terms → word_registry` via `owning_registry_fk`. This means:
- 22 groups appear under the defunct reg 154 (stupor) instead of reg 151 (sorrow) — but reg 154 is excluded, so these groups may be **missing from the dimension index entirely**
- 36 groups appear under the XREF registry instead of the OWNER registry — wrong cluster assignment, wrong registry attribution

---

## Remediation

**Fix:** Update `mti_terms.owning_registry_fk` to match the OWNER `wa_term_inventory → wa_file_index → word_registry` path for all 58 terms. This is the authoritative ownership chain.

**Safety:** The `owning_registry` text field already contains the correct value in 36/58 cases. For the 22 stupor→sorrow cases, the text also needs updating from '154' to '151'.

**Post-fix:** Repopulate `wa_dimension_index` to pick up corrected registry/cluster assignments.
