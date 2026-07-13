# Re-read operating model — cadence, stop points, DB-write timing (v1, 2026-07-13)

> The execution rhythm for the Stage-4 lexical read (per `wa-characteristic-role-lexical-cycle-authoritative-v1`). Set by the researcher 2026-07-13. Reusable per book; numbers below are Proverbs. The **passage** is the read + write unit; the **cycle** (~12 passages) is the stop + check unit.

## The cadence (researcher decision)

1. **Cycle = ~12 passages.** Read ~12 passages, then **stop for a breather** (a checkpoint the researcher can review).
2. **Write to the DB after EACH passage** — not batched to end of cycle. Each passage is read, persisted, and its master updates applied before moving to the next. Work is never held un-written.
3. **After each cycle, check conformance + quality** before starting the next.

**Proverbs: 701 char-continuity passages → 59 cycles** (avg 36 candidate chars/cycle; range 12–66). Passages are taken in **canonical order**. Progress is durable via `verse.process_marker='reread-proverbs-2026'` (a passage is done when its verses carry it), so cycles resume cleanly across sessions.

## Per PASSAGE (the read + write unit)

1. **Pull the passage morphology** — all candidate spans in the passage's verses + their morph (the passage is the reading frame; §5 of the cycle).
2. **Read char-driven** (cycle §5): for each candidate char — Screen 0 (IB-relevance; God = arena not subject) → role (characteristic / qualifier / standalone / undecided) → decompose the characteristics across dimensions 101–116, resolving pairs by reading across the passage; **`none` written explicitly, never omitted**.
3. **Write to the DB** (`_apply_reread_lexical_v1_20260709.py --in <passage.json> --live`): soft-delete prior active `ve_lexical` for those spans, insert the new ledger with **integer span-id pair endpoints**, write back every span's `role` (`role_provenance='read-2026'`), set `verse.process_marker`. (Characteristic-only lexicals — D2.)
4. **Master update (per passage):** char-on-master `verse_span_index.characteristic` (I11) for each characteristic — the apply writes it. Emergent chars stamped candidate + seed-fed (cycle §7). *(NOTE: `ib_char_id` / I7 is NOT a per-passage write — it is a book-scoped **derived rebuild**, run at cycle-close; see below.)*
5. Move to the next passage.

## Per CYCLE (~12 passages) — the breather + checks

Run BEFORE starting the next cycle; scope to the cycle's passages (and cumulative book state):

- **A0. `ib_characteristic` — PHASE 1 (capture meanings), at cycle-close.** `ib_characteristic` is **two-phased**: **Phase 1 captures the meanings from the lexicals** — the meaning-keyed records + the `ib_char_id` link — and is done **incrementally as passages/cycles complete** (NOT a per-passage write, and NOT deferred to book-close). **Phase 2 (derive the FAMILIES) is a book-close step** (see below). Run Phase 1 at cycle-close: `python scripts/_apply_rebuild_ib_char_meaning_keyed_v3_20260711.py --book <id> --live` — it re-derives the meaning records over all read-so-far chars (identity = base-lemma + stem + normalised-ESV), sets `verse_span_index.ib_char_id`, self-validates (0 null / 0 dangling), and leaves `family` NULL (Phase 2's job). This makes I7 green each cycle.
- **A. Conformance to the instructions (method adherence).** For the cycle's characteristics: full genre-mandatory ledger present, `none` explicit (**I5 / G10**); Screen-0 held — no God-bearer characteristic (**I6**); every characteristic linked to `ib_characteristic` (**I7**) and its char on the master (**I11**); pairs keyed on span-ids (**I8 / G9**); role back-filled where a lexical exists (**D1**); `ve_lexical` only on `role=characteristic` (**D2**). Plus the **passage-reading-coverage gate** (`scripts/_check_passage_reading_coverage`) — every candidate span in the cycle's passages was read (nothing passed over).
- **B. Quality (scored read-back).** Sample **2–3** of the cycle's passages; score each characteristic **sound / weak / wrong** on fidelity · working-completeness · movement · distinction. Bar: **≥90% sound, zero fidelity failures**. A missed pair on a `none`-call = a fidelity failure.
- **C. Breather.** File a one-line cycle log (passages done, chars read, gate result, any fixes); pause for researcher review. Fix any conformance/quality miss **before** the next cycle — do not carry defects forward.

## Book close (after cycle 59)

1. **`ib_characteristic` PHASE 2 — derive the FAMILIES.** Now that the whole book's meanings are captured (Phase 1, run each cycle), group the meaning-records into families: `python scripts/_apply_ib_char_family_grouping_v1_20260711.py --book <id> --live`. This is the emergent cross-char structure and belongs at book-close, not per-cycle (families only make sense over the complete set).
2. **Full integrity + measures.** Integrity **I1–I13** + the scored audit over a stratified book-wide sample + the G0–G10 measures (`_check_reread_measures_v3`), then the baseline→delta comparison (Proverbs baseline `wa-proverbs-reread-BASELINE-v2`). Book is "read" only when these pass.

## Read scope — candidates PLUS old-model char-roles (seed-miss catch, learned cycle 1)

The candidate-driven read is only as complete as the seed. **Old-model `role='characteristic'` spans that are NOT `char_candidate=1`** (provenance ≠ `read-2026`) are the signal of a **seed-missed char** — the seed never flagged it, so a candidate-only read skips it. Therefore:
- The read of a passage covers its `char_candidate=1` spans **and** any old-model char-roled span in the same verses; the latter are **emergent** chars — read them, stamp `char_candidate=1`, feed the seed (cycle §4.4).
- The **per-cycle conformance check must flag** any cycle-passage span with `role='characteristic'` and provenance ≠ `read-2026` (stale/old-model residue) → read it before the cycle closes. (Cycle 1: caught prudence/learning/greed, all central, seed-missed.)
- The apply (`_apply_reread_lexical`) now writes `verse_span_index.characteristic` (I11) for characteristic spans (extended 2026-07-13).

## Governance

- **Integrity-gated writes:** `_apply_reread_lexical` runs on a snapshot; the per-cycle conformance check is pre/post-comparable. Commit per cycle (incremental).
- **No un-written work:** the per-passage write is non-negotiable — a crash never loses more than the current passage.
- **Genre note:** this cadence is method-neutral; the passage *shape* is set by the passage rule (`wa-passage-completeness-rule-v2`, char-continuity for Proverbs).

*Filed 2026-07-13. Cadence set by researcher. Reusable per book; cycle size and count are per-book parameters.*
