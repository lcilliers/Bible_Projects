# Book lexical-rework readiness assessment — AUTHORITATIVE (v2, 2026-07-14)

> A **formal, repeatable pre-flight** that MUST pass in full before a book's lexical re-read begins. It answers one question per book: *is the data, model, tooling and measurement in the state the corrected re-read requires — so the read starts on clean, traceable, fully-seeded ground?* **Read-only** (no DB writes). Runner: `scripts/_check_book_lexical_readiness_v1_20260712.py --book <id|code>`. Subordinate only to the researcher's direction.
>
> **★ v2 (2026-07-14) — the VERSE-COVERAGE gate (from the Proverbs book-close retrospective).** v1's **I4 checked only *candidate*-verses** ("0 candidate-verses unpassaged"). That is a hole: a book verse can carry an **old-model `role='characteristic'` span with `char_candidate=None`** (a seed-missed char) yet **not** be a candidate-verse, so I4 passes while the verse sits **outside the passage structure** (`passage_id IS NULL`). A passage-driven read then **silently skips it**. In Proverbs, **116 of 915 verses were `passage_id=NULL`** (24 with real IB content) — undetected until book-close. **v2 strengthens I4 to cover EVERY verse of the book** (candidate-verse OR old-model-char-verse OR explicit skip-list), and makes **"complete" a VERSE-level definition, never passage-level** (§6). Memory: `feedback_read_completeness_is_verse_level_not_passage_level`; retrospective: `verse-analysis/proverbs/_reread/wa-proverbs-reread-RETROSPECTIVE-20260714.md`.
>
> **Refined 2026-07-12 (researcher direction, same day, pre-use):** baked in (1) the **registry path** architecture decision + registry-selection rule (§2.0); (2) the **corrected role model** — seed-candidate vs lexical-assigned role, `qualifier` is VALID, the two defect rules D1/D2 (§2.1); (3) the **staged dependency sequence** the rework must follow (§2.2). These supersede the first draft's retired-role / candidate=role assumptions.
>
> **Sources:** integrity set I1–I11 (`wa-db-integrity-definition-authoritative-v1-20260711.md`); the cycle (`wa-characteristic-role-lexical-cycle-authoritative-v1-20260708.md`); passage-rule-v2 (`wa-passage-completeness-rule-v2-20260708.md`); the seed model (`_apply_stamp_char_candidate_on_master_v1_20260708.py` + `research/discovery/lemma-inventory-master-*.json`); the term-add pipeline (`wa-term-add-update-AUTHORITATIVE-pipeline-v1-20260711.md`); the bypass-FK model (memory `reference_file_index_legacy_use_bypass_fks`). Proven on Psalms.

## 0. The governing idea — preconditions vs read-outputs

The re-read **consumes** a seeded, integrity-clean, fully-onboarded substrate and **produces** the lexical ledger + the actual roles. So checks split three ways:

- **PRECONDITION** — must be green (or researcher-waived) **before** reading. Red here blocks the start.
- **READ-OUTPUT** — *produced by* the read; pre-read it is legitimately **empty/incomplete** (checked only to confirm it is *correctly* empty, and to anchor the baseline). An empty read-output is **not** a readiness failure — the formal home of "it is OK if ib_char is empty".
- **ANCHOR** — the baseline measurement.

Verdict: **READY** = all PRECONDITION green + read-outputs correctly-empty + baseline filed · **READY-WITH-DEBT (amber)** = only *repairable* preconditions outstanding, with a named repair path · **NOT READY (red)** = any structural/traceability break or scope ambiguity.

## 1. Scope & unit

- Identify the book by `verse.book_id` and its `segment_unit.book` 3-letter code. Every check is scoped to that book.
- The **master span** `verse_span_index.id` is the hub; **every check keys on the span id, never on the Strong's**.

## 2. Baked-in rules (researcher-set)

### 2.0 Architecture decision — the REGISTRY PATH (chosen 2026-07-12)

Every characteristic word **must be a registered term**. The old term-backbone (`word_registry → mti_terms → wa_verse_records → verse_span_index`) is authoritative and must match the reading — we do **not** relax the registry requirement for emergent/seed-missed chars. Consequently, a candidate characteristic whose word is unregistered, or which lacks a verse-record, is **onboarded via the engine** before the read (per `wa-term-add-update-AUTHORITATIVE-pipeline-v1`).

**Registry-selection rule (mandatory):** when onboarding a term, selection must **first** associate it with a **relevant existing registry** (an existing `word_registry` word whose sense the term belongs to). Only **rarely**, where no existing registry fits, create a **new registry** of your choice. Prefer association; treat new-registry creation as the exception and note the justification.

### 2.1 The role model (corrected — authoritative)

Two **distinct** master fields, assigned at **different stages by different processes**:

- **`char_candidate`** (+`char_candidate_tag`) — set by the **seed** (`_apply_stamp_char_candidate`). It marks a *potential* candidate. If a span is not seeded it is **left blank**. This is Axis-A (lemma), corpus-wide.
- **`role`** — the **actual** role, assigned **by the lexical read**: one of `characteristic`, `qualifier`, `standalone`. **All three are VALID** (`qualifier` is NOT retired). `process-qualifier` is a qualifier sub-form.

**The candidate flag and the actual role MAY differ** — a seeded candidate can read as `standalone`; a span not seeded may still read as a characteristic (emergent — then stamp it a candidate + feed the seed extension). **Do not** treat `role=characteristic` without `char_candidate=1` as a defect per se.

**Defect rules (integrity, enforced):**
- **D1 — role backfill.** A span with an **active `ve_lexical` but `role IS NULL`** is a **defect**: the role must be **back-filled from the lexical** (the lexical determines the role). Target = 0.
- **D2 — lexical only on characteristics.** **There must be no `ve_lexical` for a master span whose role is not `characteristic`.** A `ve_lexical` on a `standalone`/`qualifier`/`process-qualifier`/NULL-role span is a defect (either the role is wrong → backfill, or the lexical should not exist → the corrected read rebuilds the layer for characteristics only). Target = 0.
  - ⚠ **Tooling conformance note:** the current `scripts/_reread_ledger_lib.py` writes *reduced* ledgers for `qualifier`/`standalone` spans. To satisfy D2 the re-read apply-path must write `ve_lexical` **only** for `characteristic` spans (qualifiers live as pair endpoints *within* a characteristic's lexical; standalones carry none). Reconcile the ledger-lib to this rule before a book's read is accepted, or D2 will remain non-zero post-read.

### 2.2 The staged dependency sequence (do things in this order)

The rework has a strict dependency chain; each stage's precondition is the prior stage's completion. Readiness gates **stages 0–3**; the read is stage 4; integrity is stage 5. **Stage the execution in segments and do not run a stage until its predecessor is green.**

| stage | action | depends on | gate to advance |
|--:|---|---|---|
| **0** | **Seed** — `char_candidate` stamped (potential candidates), corpus-wide | — | seed present (§C) |
| **1** | **Registry + term** — every candidate's word is a **registered term** (existing-registry-first; new rarely), onboarded via the engine | stage 0 | 0 candidate base-Strong's missing from `mti_terms` |
| **2** | **Verse-record** — every candidate `(verse, term)` has an active `wa_verse_records` | stage 1 | I2 = 0 uncovered |
| **3** | **Passages** — build **candidate-driven v2 passages** for the whole book (read is by passage, never whole-chapter) | stage 2 (integrity invariant: every candidate has a verse-record) | I4 = 0; 0 candidate-verses unpassaged |
| **4** | **Lexical read** — per passage: read → assign `role` → write `ve_lexical` **for characteristics only** → back-fill `role` on master | stage 3 | the read (out of readiness scope) |
| **5** | **Integrity** — I1–I11 + D1 + D2 all pass | stage 4 | book-close acceptance |

Readiness = **stages 0–3 green**. Stages 4–5 are the read and its acceptance.

## 3. The checks

### §A. DB integrity & bidirectional traceability — I1–I11 + D1/D2, per book

Reuse the authoritative invariants; classify per §0. **Corrected classifications** in bold.

| I# | invariant (short) | class | pre-read expectation |
|---|---|---|---|
| **I1** Referential | every FK resolves | PRECONDITION | 0 dangling |
| **I2** Master-index coverage | every candidate `(verse, base-Strong's)` has an active `wa_verse_records` | PRECONDITION (**stage 1–2 gate**) | 0 uncovered — else onboard (registry path) |
| **I3** Traceability (bidirectional) | char→span→verse; verse→passage; passage→verses | PRECONDITION | 0 breaks |
| **I4** Passage membership (**v2: ALL verses**) | **every VERSE of the book** has a `passage_id` OR is on the explicit skip-list — *not* only candidate-verses (a verse carrying an old-model `role='characteristic'` / `char_candidate=None` span must be passaged too) | PRECONDITION (**stage 3, verse-coverage gate**) | **0 verses `passage_id IS NULL` and not skip-listed**; "not built" = expected status |
| **I4b** Read completeness | verse-record verse with candidate span but no lexical | READ-OUTPUT | whole book pre-read; informational |
| **I5** Ledger completeness | full genre-mandatory ledger, `none` explicit | READ-OUTPUT | expected incomplete = baseline gap |
| **I6** Role screen | role stamped; no God-bearer characteristic | *(role decidedness is a READ-OUTPUT — the read assigns role)* **INFO** | undecided candidates are fine pre-read; God-bearer screen applies during read |
| **I7** Char-model linkage | `ib_char_id → ib_characteristic` | READ-OUTPUT | **null pre-read is correct** |
| **I8** Soft-delete consistency | no active row on a soft-deleted parent | PRECONDITION (isolation) | 0 |
| **I9** Provenance | stamps present + consistent | PRECONDITION | 0 mismatched on existing data |
| **I10** Candidate/role relation | *(per §2.1 candidate and role MAY differ)* | **INFO** | `role=characteristic` without `char_candidate` is **not** a defect; emergent chars are stamped + seed-fed |
| **I11** Char-on-master | `verse_span_index.characteristic` populated | READ-OUTPUT | empty pre-read is correct |
| **D1** Role backfill | active `ve_lexical` ⇒ `role` not null | PRECONDITION | **0** — lexical-bearing spans with null role must be back-filled |
| **D2** Lexical only on characteristic | active `ve_lexical` ⇒ `role='characteristic'` | PRECONDITION (**changeover**) | 0 at book-close; pre-read the old-model debt is measured — the corrected read (characteristic-only ledger) + old-lexical soft-delete brings it to 0 |

"Integrity-clean" = all PRECONDITION invariants pass. READ-OUTPUT / INFO items are reported for transparency and to seed the baseline, never counted as readiness failures.

### §B. Isolation of superseded data *(PRECONDITION)*

Prior-cycle records must be isolated so they cannot interfere: prior `ve_lexical` soft-deleted or cleanly replaced by the apply-path (which soft-deletes prior active rows per span before insert); `*_legacy` / defunct indexes hold 0 live-resolving rows for the book; no active row depends on a soft-deleted parent (I8). **D2's old-model lexicals on non-characteristic spans are part of this changeover** — soft-deleted as the read rebuilds the characteristic-only layer.

### §C. Seed sanity — "does the seed look right?" *(PRECONDITION, stage 0)*

- Coverage sane: candidate count + `char_candidate_tag` provenance present; candidate:total ratio in a plausible band for the genre.
- **Every candidate's word is a registered term** (§2.0 registry path): candidate base-Strong's with no active `mti_terms` row = the **stage-1 onboarding list** (existing-registry-first). **The check is existence only — a term merely needs to HAVE a registry.** The specific term↔registry allocation is scaffolding, ignored downstream; never re-home/reconcile it (see `wa-term-add-update-AUTHORITATIVE-pipeline-v1`).
- OT-DBR-009 sweep: core IB terms for the book not over-deleted from `mti_terms`/cluster.
- *(Role decidedness is NOT a seed check — role is assigned by the read, §2.1.)*

### §D. Terms, verses & passages *(PRECONDITION; stages 1–3)*

- **Terms & records (I2):** every candidate `(verse, base-Strong's)` resolves to a registered term **and** an active `wa_verse_records`. Gaps = the stage-1/2 onboarding work (registry path). This is the single most common blocker.
- **Passages (I4, stage 3):** built **before** the read, candidate-driven (passage-rule-v2), whole-book, gated on I2. Reported as status: *built & clean* (I4 passes) / *not yet built* (expected — the next action once I2 is green; amber) / *partial* (red). Read by passage, never whole-chapter.
- **★ Verse-coverage gate (v2, MANDATORY, stage 3):** after passages are built, assert **`verses-in-passages + explicit-skip-verses = book verse total`.** Enumerate every `verse.passage_id IS NULL` verse for the book; each must be **either** absorbed into a passage **or** placed on the book's **skip-list** with a one-line reason (concrete maxim / imagery / title / reward-outcome / personified-action — the non-IB categories). **Any `passage_id=NULL` verse not skip-listed is a coverage HOLE that blocks the read** — a passage-driven loop cannot see it (passage ids do not track verse order, so "resume at max id + 1" misses orphans). *This is the gate that would have caught the Proverbs 116-orphan gap at book-start instead of book-close.* The skip-list is filed alongside the readiness report and re-verified at book-close (verse-coverage = 100%).

### §E. Config & tooling *(PRECONDITION)*

- `verse.genre` set for all the book's verses (drives M ledger + G0).
- Mandatory ledger set M selected for the genre and wired into the measures runner.
- Reusable re-read machinery present + book-parameterised: `_reread_ledger_lib.py` (⚠ output dir Psalms-hard-coded; **and must conform to D2** — characteristic-only lexicals), `_reread_finish_v1`, `_apply_reread_lexical_v1`, `_reread_worklist_v1`, `_check_reread_measures_v3`. Onboarding: `_apply_gate1_term_onboard_v1` / `_run_gate1_onboard_batch_v1`. Passages: a **v2 candidate-driven builder** (must exist; v1 `_apply_passage_completeness` is misaligned).
- DB backup current before any write phase.

### §F. Baseline anchor *(ANCHOR)*

Run `_check_reread_measures_v3 --book <id> --label baseline`; file the result as the number to beat.

## 4. Entity coverage

Researcher's list (MTI-terms · master `verse_span_index` · verse-inventory `wa_term_inventory` · verse-record `wa_verse_records` · passages · ib_characteristic · cluster assignment · ve_lexical · seed JSON) + added: **`word_registry`** (registry-path hub), **`verse`** (passage_id/genre/process_marker/role-bearing via spans), **`segment_unit`(+`_verse`)**, **`verse_context`** (`ve_lexical.verse_context_id`).

## 5. Runner & report

- **Runner:** `scripts/_check_book_lexical_readiness_v1_20260712.py --book <id|code>` (read-only; §A–§F; green/amber/red + verdict; doubles as per-book `_check_book_integrity_v1`). **v2: includes the verse-coverage gate** (`--coverage` for the gate alone) — reports `verses total / in-passages / passage_id-NULL / skip-listed / HOLES`, red if any hole.
- **Report:** `verse-analysis/<book>/_reread/wa-<book>-readiness-REPORT-vN.md` — verdict + each check + named repair path per amber. Researcher signs off before Stage 0-onward execution.

## 5b. Content-validity gate — REQUIRED post-read (added v3, 2026-07-14)

**Why this exists.** §5's readiness runner and the verse-coverage gate test **completeness + integrity only** — is every verse read, every FK valid, every span wired. They pass a book that is fully read but internally **inconsistent**. On Psalms they went green while `type(102)` recorded the reading-order not the text, `locus(116)` used a blanket early convention, coupling/locus were transposed in 666 spans (DQ-01), and identical readings got contradictory `direction` tags (DQ-05). **A completeness gate cannot see a validity failure — a book can be 100% complete and uniformly wrong.** Calling the old battery "readiness/success gates" over-implied assurance it never gave.

**The gate.** `scripts/_check_lexical_content_validity_v1_20260714.py --book <id>` (read-only). Three checks, each mapping to a failure the completeness gates missed:

- **V1 value-domain** — controlled dims (`locus`/`direction`/`role`/`device`) must hold in-vocabulary values. *Catches DQ-01 (off-enum locus) — would have flagged the 713 transposed values instantly.*
- **V2 vocabulary drift** — controlled dims must not track chapter position (uses `_check_dimension_band_drift_v1`). `type` drift = RED (a-priori confirmed: a value cannot be truly absent from 25 consecutive chapters); other drift = AMBER (review: text-silence vs reader-drift). *Catches type/locus drift.*
- **V3 tag consistency** — identical `(lemma, operation)` readings must not get contradictory `direction`. *Catches DQ-05.*

RED blocks; AMBER requires researcher review. Full reliability model: `outputs/projections/WA-dimension-reliability-register-v1-20260714.md` (two axes — **stability** + **provenance**; `direction`/`device` pass both, `type` fails stability, `effect`/`intensity`/`specifier` fail provenance).

## 6. One-line definition of "ready" — and of "complete"

> **Completeness ≠ validity.** A book being *ready* (below) and fully *read* (verse-coverage green) means the work was **done and wired** — it does **not** mean the reading is **sound**. A book is **done** only when **both** the completeness gates **and** the content-validity gate (§5b) are green (or ambers researcher-waived). Never report a book as reliable on the strength of the readiness gates alone.
>
> A book is **ready** when stages 0–3 are green — seed present (§C), every candidate word registered + recorded (§D I2, registry path), passages built (§D I4) **AND the verse-coverage gate passes (every verse passaged or skip-listed — §D)** — every PRECONDITION invariant (I1, I3, I8, I9, D1, D2-at-changeover) passes or is researcher-waived, the READ-OUTPUT invariants (I4b, I5, I6, I7, I10, I11) are *correctly empty*, and the §F baseline is filed — at which point stage 4 (the lexical read) may start.
>
> **"Complete" is VERSE-level, never passage-level (v2):** a book's read is finished only when **every verse is covered** — read (carries a read-2026 char) or explicitly skip-listed. "N/N passages read" is *not* completeness; passages may cover fewer verses than the book has (Proverbs: 701 passages covered 799 of 915 verses).

*Filed 2026-07-12; refined same day per researcher direction (§2 baked-in rules). **v2 2026-07-14 — verse-coverage gate (strengthened I4 → all-verses) + verse-level "complete", from the Proverbs book-close retrospective; supersedes v1 (archived).** Read-only assessment; performs no writes.*
