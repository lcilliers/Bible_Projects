---
name: project_faculty_not_gripped_audit_20260624
description: "AUDIT->RESOLVED (2026-06-24): faculty was NOT gripped (English-gloss-STEM, 36% coverage, missed trust, taxonomy unsettled); RE-FOUNDED on a curated Strong's-lemma->faculty MAP (lemma_faculty_map 1717 terms, taxonomy=10), re-derived across ALL clusters (backup ve_lexical_faculty_backup), engine wired to the map; trust now caught; sweep unblocked"
metadata: 
  node_type: memory
  type: project
  originSessionId: c0477a92-7d79-40d5-89c9-c0bc761a3d86
---

Researcher asked (before sweeping the collection layer): "did we really get the grips with faculty?" Empirical audit answer: **NO — partially. Faculty is the least-gripped lexical field and it GATES the collection layer (bivalent + characteristic calls), so do NOT sweep until re-founded.**

**Evidence (live DB + derivation code):**
1. Coverage: faculty on **45% of term-in-verse units / only 36% of clustered terms** (867/2396; 1529 none). Many no-faculty terms are correct (states/acts/things). BUT genuine faculty-bearers MISSED — **trust: both ba.tach (117 occ) AND pisteuō (212 occ) = ZERO faculty.**
2. Root issue — how live faculty was derived: `v2_engine_iter1`, **R1 only**, via `faculty_from_text(term's GLOSS)` in `scripts/_ve_engine_v2.py` = **English word-STEM matching on the term's medium_def gloss.** Half-right (de-circularised to the term's OWN meaning, not verse text — so mostly per-term-stable) BUT still English-stem, NOT the canonical Strong's-lemma map (01b Q6 + P2 forbid English-string matching). A lemma-based `FACULTY_LEMMA` (Strong's→faculty) EXISTS but is the R2/co-occurrence path and was **NOT applied**. "trust" isn't a stem → untagged. Coverage gaps = the stem-list's incompleteness.
3. My earlier "faculty = pure lemma-constant (0% variation)" was OVER-GENERAL (from M10/M11): across all clustered terms it varies for **16%** (gloss-driven sub-sense). 
4. Taxonomy unsettled: live data has **7** (affect/cognition/perception/volition/moral_evaluation/conscience/memory); the T3 framework + rederive script define **10-11** (+creativity/agency/relational_capacity/conscientiousness — defined but ABSENT in data).
5. Three things conflated: faculty (term's OWN, R1) vs co-occurring faculty (R2, a neighbour's — belongs in compound/binding, NOT the term's) vs constitutional SEAT/location (item 5, where).

**GRIP PATH (before sweep):** (1) settle the taxonomy (7 vs 10-11 — researcher decision, define each); (2) re-found R1 on a **curated Strong's-lemma→faculty map** (P2-compliant), replacing English-gloss-stem matching — complete + principled (trust→affect+volition etc.); (3) separate faculty / co-faculty(R2→binding) / seat; (4) re-derive faculty (whole-verse reset P6), validate coverage; (5) THEN re-run the collection generator + sweep. Doc: `outputs/markdown/validation/wa-faculty-audit-have-we-got-the-grips-v1-20260624.md`. Cf. [[project_location_seat_engine_fixed]] (the seat-map = the location field, distinct from faculty — same English-vs-lemma lesson), [[project_extended_lexical_model_refinement]] (the collection layer this gates), [[project_superstructure_eisegesis_validation_20260624]] (faculty-as-lemma-constant context).

**RESOLUTION (2026-06-24, same day):** RE-FOUNDED faculty on a curated Strong's-lemma→faculty MAP (P2-compliant), built into the engine, re-derived across ALL clusters.
- Classified all 1717 content terms (T2/FLAG auto-excluded) by the principled method (faculty = the inner capacity the term's MEANING operates; "none" for states/things/persons/acts). Stored in **`lemma_faculty_map`** table.
- **Taxonomy settled from the evidence = 10**: core 7 (perception/cognition/memory/affect/volition/moral_evaluation/conscience) + **agency + relational_capacity + creativity** (each genuinely operated by some characteristic); **conscientiousness flagged but never needed**.
- Re-derived faculty ve_lexical across all clustered units: diff vs old = same 31493 / +2414 gaps filled / −4145 homograph removed / 4896 corrected (~27% fixed); 26386 rows; **old 29031 backed up to `ve_lexical_faculty_backup`** (reversible). trust now caught (ba.tach→volition; pisteuō→affect+volition); truth correctly none.
- **Engine wired**: `_ve_engine_v2.py` faculty R1 now reads `lemma_faculty_map` (gloss-stem kept only as fallback for unmapped terms) → regens stay consistent. Re-derive script `scripts/_apply_faculty_map_rederive_20260624.py`; map build in `research/VE-lexical/faculty-map-build/`.
- Validated downstream: re-ran the collection generator → **ba.tach trust = bivalent-faculty** (was expression); bivalent detection M19 2→6, M14 1→5, M16 0→10, M20 4→7.
- **OPEN follow-ons:** (a) narration `l2_meaning` is now STALE for ~11k changed-faculty units (faculty feeds it) → whole-verse narration regen owed; (b) the map is a first-pass (235 low-confidence calls) → researcher review of `lemma_faculty_map`; (c) decide `conscientiousness` in/out; (d) faculty is now sound → the collection-layer SWEEP across all clusters is unblocked.
