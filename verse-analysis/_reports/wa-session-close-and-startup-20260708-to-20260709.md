# Session close (2026-07-08 eve) + startup for 2026-07-09 morning

> Written so tomorrow starts from facts, not re-discovery. Everything below is committed; DB untouched tonight beyond read-only measures.

---

## PART 1 — What this session did (all committed)

**Theme: finish the lexical-generation instruction, consolidate dimension authority, clean the instructions folder, and set up the Proverbs re-read with a measurable success bar.**

1. **Lexical cycle instruction finalised** — `Workflow/Instructions/wa-characteristic-role-lexical-cycle-authoritative-v1-20260708.md`
   - **§4A Stage 0** (passage prerequisite; candidate-characteristic = passage heart; whole-book layout precomputed).
   - **§7A** DB-updates ledger + the **integrity invariant: a `char_candidate` span with no verse-record is a DB integrity violation — repair the verse-record + relations first.**
   - **§7B** transition (`role_provenance='read-2026'` marks read-derived vs legacy backfill).
   - **§7C** explicit pipeline chain + per-intervention DB writes + completion defined/verified at verse/passage/book levels.
   - **§3A** derivation principles P0–P8 + mandatory discovery-lookout (folded from the closed reset doc).
   - §3 now **cites the VE-lexical catalogue** as the authoritative dimension source.
   - Decisions 1–3 resolved: verse_evidence_index deprecated for lexicals; role_provenance adopted; passage scope = candidate (not a union).

2. **Passage rule → v2** — `wa-passage-completeness-rule-v2-20260708.md` (candidate-driven; v1 archived, superseded banner).

3. **Dimension authority consolidated (option A)** — the **VE-lexical catalogue** (`Workflow/Catalogue/wa-ve-lexical-catalogue-v1-20260702.md`) is the single authority; gained a **ve_nr master list §9 (101–116)** completing it with `specifier(110)` + `locus(116)`. `wa-lexical-analysis-rules-reset-v1` **CLOSED & archived** (principles → cycle §3A; items → catalogue). `wa-synthesis-B-spec-reset-v1` **kept** (stale but relevant).

4. **Instructions folder cleaned** — Batch A (12 self-declared-superseded) + Batch B (20 pre-RESET pipeline) archived to `Workflow/Instructions/archive/`. Active folder now **13 docs** (Batch C: live method + operational infra). Register: `outputs/markdown/wa-instructions-archival-proposal-20260708.md`.

5. **Proverbs digestion analysis** — `wa-proverbs-segment-vs-candidate-digestion-analysis-20260708.md`. Finding: segments are **not** over-padded (only 9% non-char, median 2 verses). The real problem is **char-density in the 6 F-frame segments (Prov 10–15, 72–129 char-spans each)**. Candidate-driven passages would be **worse** (mean 20 char-spans/unit). Fix = split the F-frames into per-proverb units; keep D/S/C/T; keep cohesive D-lectures whole.

6. **Success criteria + quantified gates** — `wa-proverbs-reread-success-criteria-20260708.md`. Nine gates G0–G8 (queries + pass values) plus a scored **read-back audit** (25 units, ≥90% sound, zero fidelity failures). Success = all gates pass + audit clears + positive delta.

7. **BASELINE captured** — `wa-proverbs-reread-BASELINE-20260708.md`. Current state scores **2 of 9 gates** (G4 distinctions ✅, G7 uncertainty ✅). To close: G0 (36 units over budget), G2 (1,139 chars with no operation), G3 (21,823 ungrounded values), G5 (103 units read in isolation), G6 (438 verses no discovery), G1 (40 undecided). Measurement script: `scripts/_check_proverbs_reread_measures_v1_20260708.py` (reusable — re-run after the read for the delta).

**Commits:** `030e714e` (§7C) · `1695e4e6` (7C detail) · `eb2a0db2` (Batch A) · `a98d7be6` (dimension authority + reset close) · `c70f36a9` (Batch B) · + tonight's baseline/criteria commit.

---

## PART 2 — Startup for tomorrow morning (the Proverbs re-read)

**Goal: re-read Proverbs to the new standard, moving the baseline gates to pass and demonstrating improvement.**

### FIRST — one decision to confirm before any DB write
The digestion fix was **proposed but not yet approved**: *split the 6 F-frame segments (Prov 10–15) into per-proverb units; keep D/S/C/T intact; keep cohesive D-lectures whole.* Confirm this, then I run it **as a dry-run first** (show the proposed unit layout for 10–15), backup + integrity-gated, before applying.

### THEN — the ordered plan
1. **Stage 0 — segmentation reset** (per book, precomputed): apply the F-frame split; every reading unit ≤ ~12 char-spans (G0). Backup → integrity snapshot → apply → compare.
2. **Integrity invariant sweep**: Proverbs has **1 fully-unbacked candidate verse** + **~179 span-link gaps** (verse has a record, not linked to the exact span). Resolve these (verse-record/link repair) before/at the read — a `char_candidate` without a record is a violation, not a skip.
3. **Re-read, chapter by chapter**, term-driven, each candidate char worked across the dimensions (catalogue), with: resolution states on every value (G3), operation read for every characteristic (G2), cross-verse links inside cohesive units (G5), discovery-lookout on every verse (G6), read-back for sensibility (audit). Stamp `role_provenance='read-2026'`, `ve_lexical.source_provenance='reread-pro-2026'`, `verse.process_marker='reread-pro-2026'`.
4. **At each chapter close and book close**: run `_check_proverbs_reread_measures_v1_20260708.py` — drive gates to pass; fix, don't move on.
5. **Book close**: run the 25-unit read-back audit; compute the G8 delta vs baseline.

### Authoritative docs to read first
- Cycle: `wa-characteristic-role-lexical-cycle-authoritative-v1-20260708.md` (esp. §3A, §4A, §7A–C).
- Dimensions: `Workflow/Catalogue/wa-ve-lexical-catalogue-v1-20260702.md` (§9 master list).
- Method for discourse books: `wa-verse-analysis-method-v1-20260702.md` **§15 segmentation-first** (Proverbs is a §15 book — the unit is the segmentation unit, NOT the term-driven passage).
- Passage rule (context): `wa-passage-completeness-rule-v2-20260708.md`.
- Success bar: `wa-proverbs-reread-success-criteria-20260708.md` + `...-BASELINE-20260708.md`.

### Open reminders
- Segment-vs-passage: for Proverbs (discourse) the unit stays **segmentation**, not candidate passages (analysis showed passages would be worse). Confirmed direction; the F-frame split is the refinement.
- The measures script measures **active current state** (provenance-agnostic) so the same run gives before/after.

*Filed 2026-07-08 eve. Resume at PART 2 → FIRST.*
