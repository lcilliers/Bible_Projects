---
name: project_per_book_corrective_pipeline
description: The live corrective per-book pipeline (a-e); Psalms is the first book complete.
metadata:
  type: project
---

After the integrity investigation (2026-07-05/06) established the book-study was **not done properly** — the book-reading phase added ZERO verse-records across all 66 books, and the coverage gate was circular (checked the seed, not the text) — the researcher set a **corrective per-book pipeline**, run strictly one book at a time, original working order (Psalms first):

- **(a)** scope one book;
- **(b)** confirm/rework the **reading units** and capture them with forward+backward **indexed FK links** (no text-scanning) — for Psalms the reading unit = the **chapter**, lexical unit = the **verse**; fix FKs (`wa_verse_records.verse_span_id` added + indexes). **Do not re-constitute passages if nothing is wrong** — re-linking would force re-assessment of everything;
- **(c)** re-assess the **role dimension** — every real-strong span is read IN CONTEXT and set to one of three, in strict order: **characteristic → qualifier → standalone** (decided by the word's meaning-in-context, never by a term list). See [[feedback_characteristic_list_validates_not_imputes]];
- **(d)** **Gate-1 completeness** for characteristic spans only: term registered in `mti_terms`, verse-record present, links intact (Psalms occurrences assembled from the in-DB index — no STEP needed; full programme-wide STEP onboarding of new terms is deferred by-book debt);
- **(e)** full-integrity validation (no orphans, links resolve, no active duplicates).

**Psalms Steps 1–2 (linkage + role, 150/150) are DONE and correct** (2026-07-06). Only **43%** of prior roles survived reassessment (41.8% wrong, 15.3% had no role) — validates the redo. Role provenance = `role-reassess-2026`. **BUT Step (d) Gate-1 was done via a NON-COMPLIANT BYPASS and REJECTED by the researcher** — I bypassed the established onboarding chain (`word_registry → wa_file_index → wa_term_inventory → wa_verse_records(ALL occurrences) → verse_context → mti_terms(owned+clustered) → mti_term_subgroup`) with sentinel file_index / thin mti / characteristic-only verse-records. **Gate-1 must be ROLLED BACK (stamps `gate1-psalms-2026`) and redone via the engine (`REGISTER → NEW_WORD --fetch-step → VC → cluster`).** Key correction: `wa_verse_records` holds EVERY occurrence of a registered term, not a characteristic subset (role lives on ve_lexical). **Full state + next step in files, NOT memory:** `verse-analysis/_reports/wa-session-log-20260706-psalms-corrective-and-gate1-rework.md` + `verse-analysis/_gate1-recovery/wa-established-onboarding-architecture-and-compliance-plan-20260706.md`. Related: [[project_otdbr009_overdeleted_core_ib_terms]], [[reference_file_index_legacy_use_bypass_fks]], [[feedback_term_coverage_cascade_is_index_not_census]], [[project_poetic_chapter_driven_method]].
