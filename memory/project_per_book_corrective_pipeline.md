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

**Psalms is the FIRST book complete through (a)-(e)** (2026-07-06). Findings that validate the redo: only **43%** of prior roles survived reassessment (41.8% wrong, 15.3% had no role); Gate-1 found **97 characteristic strongs unregistered** — the core IB vocabulary (**prayer H8605, wisdom H2451, salvation H3468, to-pray H6419, blessedness H0835, to-long-for H6165**) was simply missing. Provenance stamps: role = `role-reassess-2026`; gate1 = `gate1-psalms-2026`. Reports in `verse-analysis/_gate1-recovery/`. Related: [[project_ve_lexical_is_verse_first]], [[feedback_term_coverage_cascade_is_index_not_census]], [[project_poetic_chapter_driven_method]].
