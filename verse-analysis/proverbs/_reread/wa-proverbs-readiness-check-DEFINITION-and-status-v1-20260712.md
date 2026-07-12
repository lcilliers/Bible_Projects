# Proverbs lexical rework — readiness check: what's documented + a thorough definition (v1, 2026-07-12)

> Answers two questions before the Proverbs lexical rework starts: **(1) what is already documented** toward "readiness", and **(2) what a *thorough* readiness check should be** — with the live current-state gaps this first pass already surfaced. Read-only; no DB writes. Decision on scope + the open items is the researcher's.

## 1. What is documented today

There is **no single artefact named or structured as a "Proverbs readiness check."** What exists is four `_reread/` docs that together cover *parts* of readiness — mostly the **success/end** definition and the **baseline measurement**, not a **pre-flight** gate:

| doc | what it gives | readiness role |
|---|---|---|
| `wa-proverbs-reread-success-criteria-20260708.md` (+ 2026-07-09 amendment) | Gates **G0–G10**, the 18-dimension model, genre-aware mandatory ledger M, audit rubric, one-line "done" | Defines **success** (the finish line), not readiness (the start line) |
| `wa-proverbs-reread-BASELINE-v2-20260709.md` | Measured current violation-counts (3/9 measurable gates pass + G9b), the completeness gap by dimension, the Strong's-encoded-endpoints finding | The **"before" snapshot** — closest thing to a readiness signal, but it measures *quality gaps*, not *start-preconditions* |
| `wa-proverbs-gates-completeness-gap-and-additions-20260709.md` | Why G9/G10 were added | Supporting rationale |
| `wa-proverbs-segment-vs-candidate-digestion-analysis-20260708.md` | Unit-model decision (keep §15 segments) + the F-frame density problem | A **scoping** pre-condition, partly resolved (see §3) |

**Conclusion:** readiness is *implied* across the baseline + digestion + success docs, but it was never pulled together into an explicit, checkable pre-flight. Your recollection is right to be uncertain — the *baseline run* is documented; a *readiness check* as such is not.

## 2. A thorough readiness check — proposed definition

A readiness check should verify that the **data**, the **model/config**, the **units**, the **measurement**, the **tooling**, and the **scope decisions** are all in the state the corrected re-read requires — i.e. the state Psalms was in when its corrected re-read succeeded (that method is now proven and reusable). Six sections, each a hard pre-condition:

### A. Data & seed integrity (the substrate the re-read consumes)
- Seed spans present and sane: `verse_span_index` for Proverbs carries role-tagged spans (candidate/characteristic/qualifier/standalone).
- **Integrity invariant (cycle §7A):** every characteristic-roled span has a verse record; **a candidate span with no verse-record = DB integrity violation → repair FIRST.** (memory: [[project_lexical_cycle_finalised_and_integrity_invariant]])
- No span-orphans; `morph_code`/`stem` populated (morph is source of truth).
- `ib_char_id` state understood (null pre-read is expected — the re-read populates it).
- **OT-DBR-009 sweep:** confirm core IB terms (wisdom/folly/knowledge/prayer…) were not over-deleted for Proverbs (mti + cluster), as happened elsewhere. (memory: [[project_otdbr009_overdeleted_core_ib_terms]])

### B. Model & config correctness (the rules applied)
- `verse.genre` set for all Proverbs verses (drives the genre-aware M ledger + G0).
- **Role model migrated to the live scheme** — role ∈ {characteristic, standalone}; **qualifier / process-qualifier are RETIRED.** (memory: [[project_candidate_characteristic_seed_and_role_model]])
- Mandatory ledger set M for poetic/wisdom defined & wired into the runner (`101,102,104,105,106,107,108,112`).
- Dimension frame 101–116 + pair/qualifier/event/flag model current; provenance tags to stamp fixed (`role_provenance='read-2026'`, `ve_lexical.source_provenance='reread-proverbs-2026'`, `verse.process_marker='reread-proverbs-2026'`).

### C. Unit / segmentation readiness (how work is bounded)
- Segmentation model decided: **keep §15 `segment_unit` segments; do NOT switch to candidate passages** (digestion analysis: passages are worse for Proverbs). ✔ documented.
- **F-frame split decision confirmed:** the ~6 heavy F-frames (Prov 10–15, 72–129 char-spans) + ~10 long discourses read in **bounded sub-units** (≤~10–12 char-spans/pass, or per-verse). This is the standing open decision ("confirm F-frame split") — must be settled before starting.
- Segment coverage complete (every candidate verse belongs to a unit).

### D. Baseline & measurement readiness (how success is proven)
- Baseline filed ✔ (`BASELINE-v2`) — the number to beat.
- **The runner still runs on Proverbs today** — re-run `scripts/_check_reread_measures_v3_20260709.py` (book-general, unit-model-aware) and confirm it reproduces the baseline (guards against drift since 2026-07-09).
- **Hard prerequisite:** the re-read machinery must write **integer span-id pair endpoints** (current data is Strong's-encoded → G5/G9a/c unmeasurable). Confirm the apply-path does this before starting.
- Audit rubric defined ✔ (sampled read-back; ≥90% sound, zero fidelity failures).

### E. Tooling / infrastructure readiness (the reusable machinery)
- The proven Psalter scripts are present and **parameterised for `book='Pro'`/`book_id=20`** (or a known small tweak, as the base-source generator needed): `_reread_ledger_lib.py` (the `Reading` class guaranteeing the full M set), `_reread_finish_v1_20260709.py`, `_apply_reread_lexical_v1_20260709.py` (delete-flag-prior-then-reinsert = clean replacement), `_reread_worklist_v1`, the integrity sweep.
- DB backup current before any write phase.

### F. Scope & authority confirmation (researcher decisions still open)
- **Exact meaning of "rework the lexicals"** — a full corrected re-read (like the Psalter), or a narrower targeted fix (e.g. only populate the missing dimensions / migrate endpoints)?
- F-frame granularity decision (§C).
- Order: repair integrity + migrate retired roles FIRST, then re-read.

**Readiness = all of A–E green + F decided.** Only then start the per-segment/char-arc re-read.

## 3. Live current-state — what this first pass already found (2026-07-12)

Grounding the above against the DB right now (Proverbs = book_id 20):

- ✔ **Genre:** 915/915 Proverbs verses = `poetic/wisdom`. G0/M precondition met.
- ✔ **Seed present:** `verse_span_index` holds **6,918 Proverbs spans** — role: standalone 3,119 · **characteristic 1,708** (matches baseline) · qualifier 601 · process-qualifier 397 · **None 1,093**.
- ✔ **Lexical data intact:** 24,260 active `ve_lexical` rows — identical to the baseline, so no drift in the substrate.
- ⚠ **GAP — retired roles still present:** 601 `qualifier` + 397 `process-qualifier` spans remain, though the live model retired those to {characteristic, standalone}. Role migration looks outstanding for Proverbs.
- ⚠ **GAP — 1,093 spans with role = None** (undecided) and 1,093 with null `role_provenance`. G1 ("nothing undecided") is not yet met.
- ℹ **`ib_char_id` = null on all 6,918 spans** — expected (the corrected re-read populates it; Psalms has 877 `ib_characteristic` rows, Proverbs 0). Confirms Proverbs has *not* been through the corrected read.
- ℹ **Provenance:** `lexical-model-2026` (4,632) + `role-reassess-2026` (1,193) — not the Psalter's `read-2026`. Consistent with "not yet re-read."
- ℹ **Segments:** `segment_unit` book `'Pro'` = **323 units**, 1,424 verse-links (digestion doc counted 251 *active* — reconcile active-vs-all before starting).
- ⏳ **Not yet re-verified this session:** integrity invariant (candidate-without-verse-record), OT-DBR-009 term-deletion sweep, span-orphan check, and whether the runner + Psalter apply-scripts execute cleanly on book 20. These are the substantive checks a full readiness run must execute.

## 4. Suggested next step

Turn §2 into an **executable readiness script** (read-only) that runs A–E as queries and emits a green/amber/red report — the pre-flight analogue of the baseline runner — then settle the §F decisions. I can build and run that on approval; it would confirm the integrity invariant, the OT-DBR-009 sweep, the role-migration gap, and the tooling parameterisation in one pass, and produce a filed readiness snapshot to sign off before the first write.

*Filed 2026-07-12. Read-only. Builds on the `_reread/` baseline + success-criteria + digestion docs; live probe grounds §3.*
