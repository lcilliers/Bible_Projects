# Book lexical-rework readiness assessment — AUTHORITATIVE (v1, 2026-07-12)

> A **formal, repeatable pre-flight** that MUST pass in full before a book's lexical re-read begins (Stage 0 passage-build → Stage 2 lexical read of the authoritative cycle). It answers one question per book: *is the data, model, tooling and measurement in the state the corrected re-read requires — so the read starts on clean, traceable, fully-seeded ground?* **Read-only** (no DB writes). Runner: `scripts/_check_book_lexical_readiness_v1_20260712.py --book <id|code>`. Subordinate only to the researcher's direction.
>
> **Provenance / sources this rests on:** the authoritative integrity set **I1–I11** (`wa-db-integrity-definition-authoritative-v1-20260711.md`); the cycle (`wa-characteristic-role-lexical-cycle-authoritative-v1-20260708.md`, §4A Stage-0 · §5 read preconditions · §7A/§7C); passage-rule-v2 (`wa-passage-completeness-rule-v2-20260708.md`); the seed model (`_apply_stamp_char_candidate_on_master_v1_20260708.py` + `research/discovery/lemma-inventory-master-*.json`); the bypass-FK model (memory `reference_file_index_legacy_use_bypass_fks`); the measures runner (`_check_reread_measures_v3_20260709.py`). Proven end-to-end on Psalms.

## 0. The governing idea — preconditions vs read-outputs

The re-read **consumes** a seeded, integrity-clean substrate and **produces** the lexical ledger. So the checks split in three, and readiness is judged accordingly:

- **PRECONDITION** — must be green (or explicitly waived by the researcher) **before** reading. A red here blocks the start.
- **READ-OUTPUT** — is *produced by* the read; pre-read it is legitimately **empty/incomplete**. It is checked only to confirm it is *correctly* empty (not half-written), and to anchor the baseline. An empty read-output is **not** a readiness failure. (This is the formal home of the researcher's rule "it is OK if ib-char is empty.")
- **ANCHOR** — the baseline measurement, captured once so improvement is provable.

Overall verdict: **READY** = all PRECONDITION checks green + read-outputs correctly-empty + baseline filed · **READY-WITH-DEBT (amber)** = only *repairable* preconditions outstanding (e.g. candidate-without-verse-record → engine onboarding) with a named repair path · **NOT READY (red)** = any structural/traceability break, or ambiguity in scope.

## 1. Scope & unit

- Identify the book by `verse.book_id` (e.g. Proverbs = 20) and its `segment_unit.book` 3-letter code (e.g. `Pro`). Every check is scoped to that book.
- The **master span** `verse_span_index.id` is the hub; **every check keys on the span id, never on the Strong's** (a Strong's repeats within a verse and across the corpus).

## 2. The checks

### §A. DB integrity & bidirectional traceability — run I1–I11, per book *(PRECONDITION, except the read-outputs noted)*

Reuse the authoritative invariants verbatim (do not reinvent). Classify each:

| I# | invariant (short) | class | readiness expectation pre-read |
|---|---|---|---|
| **I1** Referential | every active `ve_lexical.verse_span_id` / `verse_context_id` and every `wa_verse_records` FK resolves | PRECONDITION | 0 dangling |
| **I2** Master-index coverage | every candidate char-span's `(verse, base-Strong's)` has ≥1 active `wa_verse_records` | PRECONDITION (the **big gate**) | 0 uncovered — else the **gate-1 debt** (amber; repair via engine onboarding) |
| **I3** Traceability (bidirectional) | char→span→verse; verse→passage; passage→verses; verse→passage→lexical — all by index/FK, never text-scan | PRECONDITION | 0 breaks (I3-passage waits on §D if passages not yet built) |
| **I4** Passage membership | every char-bearing verse has a `passage_id` → `passage` row (single-verse allowed) | PRECONDITION (Stage 0 — see §D) | 0 orphans **once Stage 0 has run**; "not built yet" = expected, reported as status |
| **I4b** Read completeness | a verse-record verse with a `char_candidate` span but no lexical = a skipped read | READ-OUTPUT | pre-read this is the *whole book* — informational only |
| **I5** Ledger completeness | every char span carries its full genre-mandatory ledger, `none` explicit | READ-OUTPUT | expected incomplete = the baseline gap |
| **I6** Role screen | `role` stamped with provenance; **no God-bearer characteristic**; no unroled candidates | PRECONDITION (role-decidedness + isolation of undecided) | unroled candidates = 0; God-bearer screen applies during read |
| **I7** Char-model linkage | every char span links `verse_span_index.ib_char_id → ib_characteristic` | READ-OUTPUT | **null pre-read is correct** (built by the read; M66) |
| **I8** Soft-delete consistency | `delete_flagged` consistent; no active row depends on a soft-deleted parent; pair endpoints reference live spans | PRECONDITION (**isolation**) | 0 active-on-deleted |
| **I9** Provenance | provenance stamps present + consistent per dataset | PRECONDITION | 0 missing/mismatched on existing data |
| **I10** Candidate flag | every `role='characteristic'` span has `char_candidate=1` | PRECONDITION | 0 violations |
| **I11** Char-on-master | every char span has `verse_span_index.characteristic` populated (from sense 101) | READ-OUTPUT | empty pre-read is correct (produced by the read) |

**"Integrity-clean" = all PRECONDITION invariants pass.** Read-output invariants are reported for transparency and to seed the baseline, never counted as readiness failures.

### §B. Isolation of superseded data *(PRECONDITION)*

Everything from a prior/abandoned cycle must be **suitably isolated so it cannot interfere** with the new read:
- Prior `ve_lexical` rows for the book are either soft-deleted (`delete_flagged=1`) or will be cleanly replaced by the apply-path (`_apply_reread_lexical` soft-deletes prior active rows per span before insert) — confirm no *active* legacy rows carry a stale provenance that the read would double-count.
- `ve_lexical_legacy` and any `*_legacy` / defunct index (`verse_evidence_index.lexical`) hold **0** live-resolving rows for the book (they are archives, must not be joined).
- No active row depends on a soft-deleted parent (I8).

### §C. Seed sanity — "does the seed look right?" *(PRECONDITION)*

The seed is the candidate-characteristic layer on the master (`verse_span_index.char_candidate` / `char_candidate_tag`, stamped by `_apply_stamp_char_candidate_on_master_v1` from `lemma-inventory-master-*.json`).
- **Coverage looks sane:** count candidate spans; distribution of `char_candidate_tag` provenance present (registry / IB-gloss); ratio of candidate:total spans in a plausible band for the genre (compare to Psalms).
- **Role-decidedness:** **no undecided candidate spans** — every candidate has a decided `role`. `role IS NULL` on a candidate = a gap to close before reading.
- **Live role model only:** `role ∈ {characteristic, standalone}` (+ pair-derived qualifier at read-time). **Retired roles (`qualifier`, `process-qualifier` as *stamped* roles) must be migrated** — their presence means the seed predates the current model.
- **Every verse-record span has a char where expected** (the researcher's phrasing): cross-check that spans carrying a verse-record and a candidate flag are consistent (feeds I2/I4b).
- **OT-DBR-009 sweep:** confirm core IB terms for the book (e.g. wisdom/folly/knowledge for Proverbs) were not over-deleted from `mti_terms`/cluster; a missing anchor term = seed hole (memory `project_otdbr009_overdeleted_core_ib_terms`).

### §D. Terms, verses & passages *(PRECONDITION; passages = Stage 0)*

- **Terms & verses present (I2 detail):** every candidate characteristic's `(verse, base-Strong's)` resolves to a term in `mti_terms` **and** an active `wa_verse_records`. Missing term or record = the **gate-1 debt**; repair via the engine onboarding / per-book corrective path **before** reading. This is the single most common blocker.
- **Passages — a PRECONDITION built in Stage 0, not inside the read.** Per passage-rule-v2 + cycle §4A, *"the whole-book passage layout is built before any lexical read; no verse is read outside a passage."* The book is read **by passage, never whole-chapter**. Therefore the readiness report records passage **status**:
  - *Built & clean* → I4 passes (every char-verse has a passage, forward+backward maximal-run membership; single-verse passages allowed). ✔ ready on this axis.
  - *Not yet built* → **expected**; passage-build is the **first executable pipeline action**, hard-gated on §D I2 being green (you cannot build passages correctly while candidates lack verse-records). Reported as amber "Stage 0 pending", not red.
  - *Partially/inconsistently built* → **red** (dangling `passage_id`, char-verses with no passage while others have one).
  - **Answer to the standing question** *(precondition vs pipeline step)*: passage-build is **Stage 0 of the pipeline**, but its own precondition (I2) is a **readiness gate**. So: readiness enforces I2; passage-build then runs as the first pipeline stage. Readiness does not require passages to pre-exist — it requires the *ground for building them* to be clean.

### §E. Config & tooling *(PRECONDITION)*

- `verse.genre` set for all the book's verses (drives the genre-aware mandatory ledger M and G0). Record the genre.
- Mandatory ledger set M selected for that genre and wired into the measures runner (`_check_reread_measures_v3` selects M by genre).
- The reusable re-read machinery is present and **book-parameterised** (or the known small tweak is noted): `_reread_ledger_lib.py` (⚠ output dir hard-coded to `verse-analysis/psalms/_read/` — parameterise per book), `_reread_finish_v1` (`--book`/`--book-id`), `_apply_reread_lexical_v1` (book-agnostic, driven by the JSON), `_reread_worklist_v1` (book-general), `_check_reread_measures_v3` (book-general).
- DB backup current before any subsequent write phase.

### §F. Baseline anchor *(ANCHOR)*

Run `scripts/_check_reread_measures_v3_20260709.py --book <id> --label baseline` and file the result as the book's baseline (the number to beat). Confirms the runner executes on the book and captures the start point for the G8 delta.

## 3. Entity coverage — "did I leave anything out?"

The researcher's list — **MTI-terms, master (`verse_span_index`), verse-inventory (`wa_term_inventory`), verse-record (`wa_verse_records`), passages (`passage`), ib_characteristic, cluster assignment, ve_lexical, seed-builder JSON** — is covered above. **Added (recommended) for completeness:**
- **`word_registry`** — the hub the bypass FKs (`word_registry_fk`, `owning_registry_fk`) point to; needed to close FK traceability (§A I1).
- **`verse`** itself — carries `passage_id`, `genre`, `process_marker` (the anchor for §D/§E/§B).
- **`segment_unit` / `segment_unit_verse`** — the §15 reading units + digestion granularity (relevant where the book is read by segment, e.g. Proverbs; feeds the F-frame split decision).
- **`verse_context`** — `ve_lexical.verse_context_id` resolves here (part of I1).
- **`mti_term_cross_refs` / `mti_term_flags`** — only if a term-integrity anomaly is suspected (not a standing check).

## 4. The runner & the report

- **Runner:** `scripts/_check_book_lexical_readiness_v1_20260712.py --book <id|code>` — read-only; runs §A–§F, prints each check's status (green/amber/red) with counts, and an overall verdict. Also serves as the per-book `_check_book_integrity_v1` the integrity doc (rule 3) asked for.
- **Report:** file a per-book readiness snapshot `verse-analysis/<book>/_reread/wa-<book>-readiness-REPORT-vN-YYYYMMDD.md` with the verdict, each check, and the named repair path for any amber. **The researcher signs off this report before Stage 0 begins.**

## 5. The one-line definition of "ready"

> A book is **ready** for its lexical re-read when every PRECONDITION check (§A integrity incl. isolation & traceability, §B isolation, §C seed sanity, §D terms/verses + I2, §E config/tooling) is green or researcher-waived, the read-output invariants (I5, I7, I11, I4b) are *correctly empty*, and the §F baseline is filed — at which point Stage 0 (passage-build) may start.

*Filed 2026-07-12. v1 — open to researcher correction; version-bump on change. Read-only assessment; performs no writes.*
