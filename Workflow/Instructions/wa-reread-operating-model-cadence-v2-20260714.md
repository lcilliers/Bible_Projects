# Re-read operating model — cadence, stop points, DB-write timing (v2, 2026-07-14)

> The execution rhythm for the Stage-4 lexical read (per `wa-characteristic-role-lexical-cycle-authoritative-v1`). Set by the researcher 2026-07-13; **v2 (2026-07-14) bakes in the Proverbs book-close retrospective learnings** (`verse-analysis/proverbs/_reread/wa-proverbs-reread-RETROSPECTIVE-20260714.md`). Supersedes v1 (archived). Reusable per book; numbers below are Proverbs. The **passage** is the read + write unit; the **cycle** (~12 passages) is the stop + check unit.
>
> **v2 changes (all from the Proverbs retrospective):** (1) **"complete" is VERSE-level, not passage-level** — a book-start verse-coverage pre-flight + a cheap per-cycle verse-coverage assertion (the Proverbs read silently skipped 116 `passage_id=NULL` verses); (2) **ib_char rebuild is batched** — cheap I7 *check* per cycle, full *rebuild* periodically + at book-close (was O(book) × 59); (3) **DB snapshot every N cycles**, not every cycle (~48 GB churn avoided); (4) **book-close is demote-then-measure**; (5) reusable **conformance** and **input-pull** scripts replace inline SQL/verbose pulls; (6) the apply now **auto-flags leftover old-model chars** on read verses.

## The cadence (researcher decision)

1. **Cycle = ~12 passages.** Read ~12 passages, then **stop for a breather** (a checkpoint the researcher can review).
2. **Write to the DB after EACH passage** — not batched to end of cycle. Each passage is read, persisted, and its master updates applied before moving to the next. Work is never held un-written.
3. **After each cycle, check conformance + quality** before starting the next.

**Proverbs: 701 char-continuity passages → 59 cycles** (avg 36 candidate chars/cycle; range 12–66). Passages are taken in **canonical order**. Progress is durable via `verse.process_marker='reread-<book>-2026'` (a passage is done when its verses carry it), so cycles resume cleanly across sessions.

## ★ Book-start pre-flight — verse-coverage gate (v2, MANDATORY)

**Before cycle 1**, confirm the passage structure covers **every verse of the book**. Run the book-readiness runner's coverage gate (`_check_book_lexical_readiness_v1 --book <id> --coverage`):

- Assert **`verses-in-passages + explicit-skip-verses = book verse total`.** Any verse with `passage_id IS NULL` that is not on an explicit skip-list is a **coverage hole** — a passage-driven read will silently skip it. **Block the read until reconciled** (assign orphan verses to passages, or add them to the skip-list with a reason).
- **Why:** the Proverbs read was "701/701 passages" complete yet only **87% of verses** — 116 `passage_id=NULL` verses (24 with real IB content, incl. Agur's contentment prayer 30:7-8) were never pulled, undetected until book-close. Passage ids also do **not** track verse order, so a "resume at max passage-id + 1" high-water mark cannot see orphans.
- **"Book complete" is defined at the VERSE level**, never the passage level. See `wa-book-lexical-readiness-assessment-AUTHORITATIVE` (verse-coverage section) and memory `feedback_read_completeness_is_verse_level_not_passage_level`.

## Per PASSAGE (the read + write unit)

1. **Pull the passage input** — the passage's verses with their **candidate / char-roled / role-bearing spans + morph** (the passage is the reading frame; §5 of the cycle). Use the reusable pull (`scripts/_pull_reread_passage_input_v1.py --book <id> --passages <ids>`), which returns **only** candidate/char/role spans + function-word context, not every token — leaner input, same coverage.
2. **Read char-driven** (cycle §5): for each candidate char — Screen 0 (IB-relevance; God = arena not subject) → role (characteristic / qualifier / standalone / undecided) → decompose the characteristics across dimensions 101–116, resolving pairs by reading across the passage; **`none` written explicitly, never omitted**.
3. **Write to the DB** (`_apply_reread_lexical_v1_20260709.py --in <passage.json> --live [--no-backup]`): soft-delete prior active `ve_lexical` for those spans, insert the new ledger with **integer span-id pair endpoints**, write back every span's `role` (`role_provenance='read-2026'`), set `verse.process_marker`, **and flag any leftover old-model `role='characteristic'` span on the read verses** (spans read but not re-selected) for demotion (see §book-close). (Characteristic-only lexicals — D2.)
4. **Master update (per passage):** char-on-master `verse_span_index.characteristic` (I11) for each characteristic — the apply writes it. Emergent chars stamped candidate + seed-fed (cycle §7).  *(`ib_char_id` / I7 is NOT a per-passage write — it is a book-scoped derived rebuild; see below.)*
5. Move to the next passage.

## Per CYCLE (~12 passages) — the breather + checks

Run BEFORE starting the next cycle; scope to the cycle's passages (and cumulative book state):

- **A0. `ib_characteristic` Phase 1 — cheap I7 CHECK per cycle; full REBUILD periodically (v2).** Phase 1 (meaning-keyed records + `ib_char_id` link) is a book-scoped derived rebuild that is **O(book)**. Running the full rebuild every cycle (Proverbs: 59×) is wasteful. Instead: **per cycle, run the cheap I7 check** (count read-2026 chars with `ib_char_id IS NULL` in the cycle's passages — if >0, run the rebuild; else skip). **Run the full `_apply_rebuild_ib_char_meaning_keyed_v3 --book <id> --live` every ~5 cycles and at book-close.** This keeps I7 green without the per-cycle O(book) cost.
- **A. Conformance to the instructions (method adherence).** Run the **reusable conformance script** (`scripts/_check_reread_conformance_v1.py --book <id> --passages <cycle-ids>` — NOT inline SQL): full genre-mandatory ledger present, `none` explicit (**I5 / G10**); Screen-0 held (**I6**); char-on-master (**I11**); pairs keyed on span-ids (**I8 / G9**); role back-filled (**D1**); `ve_lexical` only on `role=characteristic` (**D2**); every candidate span read (`_check_passage_reading_coverage`, nothing passed over). **Plus (v2) the cheap book-wide verse-coverage assertion** (verses read + skip-listed = book total so far) — catches any orphan before it accumulates.
- **B. Quality (scored read-back).** Sample **2–3** of the cycle's passages; score each characteristic **sound / weak / wrong** on fidelity · working-completeness · movement · distinction. Bar: **≥90% sound, zero fidelity failures**. A missed pair on a `none`-call = a fidelity failure. **Also confirm no empty-`value` content rows** (G7) — the check is "row present AND value non-empty", not just "row present".
- **C. Breather.** File a one-line cycle log; pause for researcher review. Fix any miss **before** the next cycle.

## Book close (after the last cycle) — DEMOTE, then MEASURE (v2)

1. **Demote leftover legacy chars FIRST.** Every old-model `role='characteristic'` span (provenance ≠ `read-2026`) on a **read** verse is a span read-but-not-re-selected → set `role='standalone'`, `role_provenance='read-2026-supersede'`. Also resolve stray `char_candidate=1 / role=NULL` function-word flags. This makes the read layer the sole char authority **before** measuring (else the measures conflate legacy + read and read as false failures).
2. **`ib_characteristic` Phase 2 — derive the FAMILIES.** `_apply_ib_char_family_grouping_v1 --book <id> --live` (book-general; `--book` param). Families only make sense over the complete set.
3. **Full integrity + measures.** Integrity **I1–I13** + the scored audit over a stratified book-wide sample + the G0–G10 measures (`_check_reread_measures_v3 --book <id> --layer read-2026` — the `--layer` scope reports the read layer, not the legacy substrate), then the baseline→delta. **Book is "read" only when verse-coverage = 100% and these pass.** (Note: **G0** over-budget on the old whole-chapter `segment_units` layer is a structural artifact, not a read defect.)

## Read scope — candidates PLUS old-model char-roles (seed-miss catch, learned cycle 1)

The candidate-driven read is only as complete as the seed. **Old-model `role='characteristic'` spans that are NOT `char_candidate=1`** (provenance ≠ `read-2026`) are the signal of a **seed-missed char**. Therefore:
- The read of a passage covers its `char_candidate=1` spans **and** any old-model char-roled span in the same verses; the latter are **emergent** chars — read them, stamp `char_candidate=1`, feed the seed (cycle §4.4).
- The per-cycle conformance check flags any cycle-passage span with `role='characteristic'` and provenance ≠ `read-2026` → read it before the cycle closes.
- **(v2) Verses outside the passage structure (`passage_id IS NULL`) carry old-model char-roles too — the book-start coverage gate (above) catches these**; without it they are never pulled (the Proverbs 116-orphan gap).

## Governance

- **Integrity-gated writes:** `_apply_reread_lexical` runs on a snapshot cadence (**every N cycles, default 5**, v2 — not every cycle; git commits per cycle + the per-passage write cover finer-grained loss). The per-cycle conformance check is pre/post-comparable. Commit per cycle (incremental).
- **No un-written work:** the per-passage write is non-negotiable — a crash never loses more than the current passage.
- **Genre note:** this cadence is method-neutral; the passage *shape* is set by the passage rule (`wa-passage-completeness-rule-v2`, char-continuity for Proverbs).
- **Line endings:** `.gitattributes` normalises `.md`/`.py`/`.json` to LF — no more per-commit CRLF warnings. After any git history rewrite, re-verify upstream tracking (`git rev-list --count @{u}..HEAD`).

*Filed 2026-07-14 (v2). Supersedes v1 (2026-07-13, archived). Cadence set by researcher; v2 learnings from the Proverbs book-close retrospective. Reusable per book; cycle size/count and snapshot cadence are per-book parameters.*
