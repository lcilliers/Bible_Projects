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
4. **Master updates:** `ib_char_id` linkage (I7) and char-on-master `verse_span_index.characteristic` (I11) for each characteristic; emergent chars stamped + seed-fed (cycle §7).
5. Move to the next passage.

## Per CYCLE (~12 passages) — the breather + checks

Run BEFORE starting the next cycle; scope to the cycle's passages (and cumulative book state):

- **A. Conformance to the instructions (method adherence).** For the cycle's characteristics: full genre-mandatory ledger present, `none` explicit (**I5 / G10**); Screen-0 held — no God-bearer characteristic (**I6**); every characteristic linked to `ib_characteristic` (**I7**) and its char on the master (**I11**); pairs keyed on span-ids (**I8 / G9**); role back-filled where a lexical exists (**D1**); `ve_lexical` only on `role=characteristic` (**D2**). Plus the **passage-reading-coverage gate** (`scripts/_check_passage_reading_coverage`) — every candidate span in the cycle's passages was read (nothing passed over).
- **B. Quality (scored read-back).** Sample **2–3** of the cycle's passages; score each characteristic **sound / weak / wrong** on fidelity · working-completeness · movement · distinction. Bar: **≥90% sound, zero fidelity failures**. A missed pair on a `none`-call = a fidelity failure.
- **C. Breather.** File a one-line cycle log (passages done, chars read, gate result, any fixes); pause for researcher review. Fix any conformance/quality miss **before** the next cycle — do not carry defects forward.

## Book close (after cycle 59)

Full integrity **I1–I13** + the scored audit over a stratified book-wide sample + the G0–G10 measures (`_check_reread_measures_v3`), then the baseline→delta comparison (Proverbs baseline `wa-proverbs-reread-BASELINE-v2`). Book is "read" only when these pass.

## Governance

- **Integrity-gated writes:** `_apply_reread_lexical` runs on a snapshot; the per-cycle conformance check is pre/post-comparable. Commit per cycle (incremental).
- **No un-written work:** the per-passage write is non-negotiable — a crash never loses more than the current passage.
- **Genre note:** this cadence is method-neutral; the passage *shape* is set by the passage rule (`wa-passage-completeness-rule-v2`, char-continuity for Proverbs).

*Filed 2026-07-13. Cadence set by researcher. Reusable per book; cycle size and count are per-book parameters.*
