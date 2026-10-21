# Corrected char-arc book re-read — REPEATABLE PROCESS (v1)

> **⚠ SUBORDINATE / WORKED-EXAMPLE NOTES ONLY (2026-07-11).** The single authoritative end-to-end spec is **`wa-characteristic-role-lexical-cycle-authoritative-v1-20260708.md`** — read that, not this, for the method. This doc's reading discipline is already §5 there; it is kept only as Psalms worked-example notes (the issue-prevention table §4 is its remaining unique value). Do not use it as a parallel process.
>
> **Status:** authoritative for *execution*, **subordinate** to `wa-per-book-corrective-method-authoritative-v1-20260707.md` (the b→c→d→e frame set by the researcher). This document does not change that method; it operationalizes its **step (c)** — the role/lexical char-arc read — into a concrete, repeatable pipeline, **proven end-to-end on Psalms** (150/150 psalms + the Book I remediation, all gate-clean, 2026-07-10/11). Where this and the authoritative frame ever conflict, the frame wins.
>
> **Purpose:** so the next book is read the same way, first-time-right, and **every issue hit during Psalms is expressly prevented, not re-encountered.** Read this before starting the char-arc read of any book.
>
> **Evidence base:** `verse-analysis/psalms/_reread/wa-psalms-reread-snapshot-v6-FINAL-20260711.md` (final gate state) + the v1–v5 trail; `wa-psalms-reread-discipline-audit-20260710.md`. Success definition + gates: `verse-analysis/proverbs/_reread/wa-proverbs-reread-success-criteria-20260708.md`. Memory: `project_reread_success_gates_and_scored_audit`.

---

## 0. Where this sits in the per-book method

The authoritative order per book is **b → c → d → e**:
- **(b)** confirm/rework the reading units (passage/verse), tracked in tables, before any reading.
- **(c)** re-assess the **role** and read the **lexical** — **this document.**
- **(d)** Gate-1 completeness (term recorded, verses pulled, links intact — a STEP action).
- **(e)** book-close full-integrity validation.

Do **not** start (c) before (b) is done. Do **not** treat (c) as a substitute for (d)/(e).

---

## 1. The reading lens (never negotiable)

1. **The unit of work is the human inner-being (IB).** Foreground the **operation/mechanics**, never the God-relation as headline. Not "trust in God" but *how trust is grounded and what it produces*; not "the soul's longing" but *how desire consolidates onto one object*. **God is the arena, not the point.** (memory `feedback_lens_is_inner_being_process_not_god_relation`)
2. **Screen 0 (IB-relevance) is the FIRST test on every candidate span** (`wa-ib-relevance-screen-correction-20260709.md`; cycle §5/§11):
   - Human faculty / state / disposition / inner-driven act (the psalmist, the wicked, mankind, the saints) → **characteristic** (full ledger).
   - Wholly God's own attribute / quality / action → **qualifier** (no char ledger; enters a human char as source/target/manner).
   - Outward imagery / cosmic / cultic / place / instrument / label → **standalone**.
   - A wholly-God (hymnic) unit may legitimately carry **no characteristic at all** (e.g. Ps 29, 93, 114 → all-standalone). Reading that honestly is correct, not a failure.
3. **Role order is fixed and relational** (per the authoritative frame): characteristic → else qualifier (it *strengthens an associated characteristic* — its object/manner/instrument/sphere/movement/outcome, decided by morphology) → else standalone (relates to **no** characteristic). **When in doubt, lean characteristic.**
4. **Char-arc passage rule.** Anchor on each surviving **human IB char** and read **its passage** — the run of verses over which that char is introduced, develops, and resolves, together with directly-interrelated chars (shared pairs/couplings/bearer/movement). **Do not sweep whole chapters** or arbitrary verse-blocks. Expect *not* to read every verse. (memory `feedback_read_by_passage_not_whole_chapter`)
5. **Resist grouping.** Each repeated/same-gloss span is **distinct** — read its operation off *its* verse. The difference is the finding. (memory `feedback_resist_grouping_preserve_distinctions`)

---

## 2. The mandatory ledger (genre-aware)

Every **characteristic** carries the full **poetic mandatory set** plus role/discovery/locus:

`M = {101 sense, 102 type, 104 seat, 105 bearer, 106 operation, 107 target, 108 manner, 112 coupling}` **+ 116 locus + 114 discovery + 115 role**.

- `103 source` / `111 effect` are **cross-verse Phase-2** items → **NOT per-span for poetic/wisdom/prophetic** books (they are chapter-level there). Narrative books add `103,111` to M.
- A **qualifier** carries `101 + 103 (source→char, res=span, G9b-safe) + 114 + 115`.
- A **standalone** carries `101 + 114 + 115`.
- **`none` must be written, not omitted** (missing = deliberate). The ledger library enforces this.
- **Bearer (105) of a characteristic is ALWAYS the human** (the psalmist / the wicked / mankind / the saints) — **never God**. See Issue #1.

---

## 3. The pipeline (reusable scripts — do not rebuild)

Per unit (chapter/passage), in order:

| step | tool | guarantee |
|---|---|---|
| build ledger JSON | `scripts/_reread_ledger_lib.py` (the `Reading` class: `ch/qu/st` + `write()`) | full mandatory set per char → **no silent G10 miss** |
| **coverage check** | query: every `char_candidate=1 OR role IN(...)` span present in the JSON | **100% or do not proceed** (Issue #2) |
| apply + gate + close + stamp | `scripts/_reread_finish_v1_20260709.py --chapter N --chars M --msg "..."` | applies via `_apply_reread_lexical_v1` (**delete-flags all prior active `ve_lexical` per span, then re-inserts** → clean replacement, safe re-read); loud `IB-SCREEN WARNING` on any God-bearer char; writes G10/G6 |
| close worklist | `scripts/_reread_worklist_v1_20260709.py --close --chapter N --g10 0 --g6 0` | tracks completion |
| **integrity sweep** | query per unit: `missing-dims / unroled / God-bearer / G9b` | **all must be 0** before commit |
| bank | `git add -A && git commit` (the finisher may self-commit — Issue #7) | incremental, per batch |

### 3a. MANDATORY per-book close steps (never skip — added 2026-07-11)
After a book's units are read, before it is called done, run — and they are enforced as integrity invariants I10/I11/I7 (`wa-db-integrity-definition-authoritative-v1`):
1. **Char-on-master + emergent seed feedback** — `scripts/_apply_charfix_master_v1_20260711.py --book-id N`: stamps `char_candidate=1` on any span that emerged as a characteristic without a seed flag (writes their lemmas to a `char-seed-extension-*` file for the next seed run) **and** populates `verse_span_index.characteristic` (the read char in words, from ve_lexical sense 101). **No characteristic may exist without a candidate flag (I10) or without its char on the master (I11).**
2. **Rebuild the normalised index** — `scripts/_apply_build_ib_char_index_v1_20260711.py --book-id N`: (re)builds `ib_characteristic` (lemma-grain: char_key/key_word/key_span_id/operation/ledger/instance_count) from master+lexical and links every char-span via `verse_span_index.ib_char_id` (I7). **This runs on every book.**
3. **Full integrity check** — I1–I11 must pass (per-book), not just the ledger gates.

- **`Reading` API:** `r = Reading("Psa", book_id, chapter, note=...)`; `r.ch(sid, sense, typ, bearer, op, target, coupling, locus, disc)`; `r.qu(sid, sense, src_char_sid, disc)`; `r.st(sid, sense, disc)`; `r.write()`.
- **Auto-standalone fallback** (for imagery/instrument/label-heavy units): after listing explicit chars + quals, sweep remaining candidate spans → standalone with a **surface-anchored** discovery note. Guarantees coverage while keeping notes honest. Use for hymnic/nature/theophany units (Ps 29/148/150 pattern).
- **Provenance stamped:** `verse_span_index.role_provenance='read-2026'`, `ve_lexical.source_provenance='reread-<book>-2026'`, `verse.process_marker='reread-<book>-2026'`.
- **Batch cadence:** 5–8 units per turn; **coverage-check the whole batch, then apply, then one integrity sweep, then commit.** Bank every batch. (memory `feedback_commit_incrementally`)
- **Measure book-wide** with `scripts/_check_reread_measures_v3_20260709.py --book <Name>` (unit-model aware). Baseline first, re-measure after — delta, not assertion.

---

## 4. Issues encountered on Psalms → EXPRESS prevention rule (do not repeat)

| # | Issue (what happened) | Express rule so it cannot recur |
|---|---|---|
| **1** | **God-bearer false positive / mis-screen.** Bearer strings like "God's servants/people/saints" tripped the `LIKE 'God%'` gate; separately, God-content was mis-called a *characteristic*. | **(a)** The bearer (105) of a characteristic is **always the human** — phrase it "the saints (of God)", "the psalmist", "the wicked", **never "God's X"**. **(b)** If a candidate's true bearer is God, it is **not a characteristic** — re-screen it to **qualifier** (Screen 0). Never dodge the regex by rewording a genuinely God-bearing char. The `IB-SCREEN WARNING` + the God-bearer=0 integrity query are **hard gates**; **never bank a batch with a God-bearer char.** |
| **2** | **Coverage slips** — spans missed in the first build, caught only later. | **100% coverage check is mandatory before apply.** Every `char_candidate=1 OR role IN('characteristic','qualifier')` span for the unit must appear in the JSON. **A partial build is never applied.** The auto-standalone fallback exists so nothing is left unroled. |
| **3** | **G4 flattened reuse** — recurring synonyms / repeated spans read identically. | **Resist grouping.** Each occurrence read off its own verse; **every char gets a verse-specific 114 discovery note** naming what is distinct about *this* occurrence. Read the difference as the finding. |
| **4** | **Discipline drift** — "trust/love in God" written as the headline instead of the operation. | **Foreground the IB operation/mechanics** (grounding, consolidation, self-stilling, entrustment), not the God-relation. Re-read §1.1 before each session; the discipline audit (`wa-psalms-reread-discipline-audit`) is the model self-check. |
| **5** | **Book I predated the IB-screen** → a whole remediation pass (185 God-bearer chars + 300 old-provenance). | **Read first-time-right.** Screen 0 + the God-bearer=0 gate run **at apply on every batch, from the first unit of every book.** No book should ever need a Book-I-style second pass. |
| **6** | **Filename/loop slip** — `_tmp_ps09.py` vs the 3-digit `_tmp_ps009.py` silently skipped Ps 9 in a shell loop. | **Zero-pad chapter to 3 digits** in every builder filename and JSON path (`psalm-0NN`, `_tmp_psNNN`). The batch coverage check is the backstop that catches any silent skip — **always run it over the whole batch.** |
| **7** | **git "nothing to commit"** after a unit. | Not an error — `_reread_finish` may **self-commit**. A redundant follow-up commit correctly sees a clean tree. |
| **8** | **Slow ~670MB DB snapshot** on each `_apply_*`. | The reread apply already passes `--no-backup`; keep it on loop/batch runs (memory `feedback_pre_op_db_snapshots_prune_or_skip`). |
| **9** | **Emergent chars not fed back to the seed** — 403 spans became `role='characteristic'` with no `char_candidate` flag; the "dynamic seed" never grew. | **Invariant I10:** every characteristic is a candidate. §3a step 1 stamps emergents + writes their lemmas to a `char-seed-extension-*` file the seed **must** consume next run. Check `role=characteristic AND char_candidate IS NULL = 0`. |
| **10** | **The read char lived only in the lexical, never on the master** — "the char" was discussed for weeks but never captured in the DB where it belongs. | **Invariant I11:** `verse_span_index.characteristic` (the read char in words) populated for every char-span. §3a step 1. Check `role=characteristic AND characteristic IS NULL = 0`. |
| **11** | **The read never fed the characteristic model** — 2,168 instances unlinked to any normalised characteristic. | **Invariant I7 + §3a step 2:** rebuild `ib_characteristic` and set `verse_span_index.ib_char_id` on **every** book run. Check `ib_char_id IS NULL = 0`. |

---

## 5. What this process does and does NOT prove (hand-off to QA)

- **Proven by the gates (mechanical):** completeness (G10 full ledger, no ZERO-dim), no-operation (G2), discovery-lookout (G6), pair integrity (G9b), nothing-passed-over (G1), IB-screen (0 God-bearer), 100% coverage. Psalms final: **all zero** except G0 (the poetic genre caveat — the gate scores a whole psalm as one passage; the reading itself proceeds by char-arc — by design).
- **NOT proven by the gates — needs the scored read-back audit + researcher review:** correctness, fidelity to the verse, eisegesis, movement-quality, valid-`none`-vs-missed-pair, role-accuracy. **Gates + audit together, neither alone.** (This is the deliberate next phase for Psalms: express the read as *findings* and audit their quality.)

---

## 6. Scaling note (throughput)

Work scales by **candidate span**, not by book — see `verse-analysis/wa-lexical-throughput-analysis-and-acceleration-20260711.md`. Psalms (6,615 spans) is the **densest, worst-case** book (~2× average density); the remaining OT is ~28,600 spans across 38 books, ~4× Psalms, not 65×. The pipeline above is embarrassingly parallel (each unit independent). Any fan-out **must** keep §1's discipline and pass §3's gates + a sampled read-back audit per book, or it regresses to templated reading.

*Filed 2026-07-11. Subordinate to the per-book corrective method. Update this doc (version bump) whenever a new issue is found and prevented — it is the living record of "how we read a book, and what we already learned not to do."*
