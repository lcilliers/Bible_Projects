# Passage determination rule (reading-unit build) — REUSABLE per book (v2)

> **Supersedes `wa-passage-completeness-rule-v1-20260707.md`.** v1 scoped passages by **verse-record**; v2 scopes them by **candidate characteristic** (the seed on the master), because the candidate characteristic — not the verse-record — is what makes a verse IB-relevant and therefore worth reading. This is **Stage 0** of the authoritative cycle (`wa-characteristic-role-lexical-cycle-authoritative-v1-20260708.md`): no verse is read outside a passage, and the whole-book passage layout is built **before** any lexical read. The consecutive-run grouping, the integrity gate, and passage-via-`verse.passage_id` propagation from v1 are unchanged. Set 2026-07-08.

## Principle
- A passage is a **reading unit**: the frame in which a candidate characteristic is read, i.e. the verse together with the adjacent verses that also carry inner-being content.
- **The candidate characteristic span is the heart of the passage.** IB-relevance is decided by `verse_span_index.char_candidate = 1`, *not* by the verse-record. A verse with **no** candidate characteristic carries no IB content to read — it is correctly **outside every passage and is never read**. We do not read whole chapters; we read candidates in context.
- **The verse-record is the entry point and the confirmed anchor, not the scope test.** Reading a book *starts* at its first verse-record verse (a registered IB occurrence); the passage then *grows* by candidate adjacency.
- **Single-verse passages are allowed (researcher decision 2026-07-11).** A maximal run may be **one verse** — when a characteristic-bearing verse has no adjacent characteristic-bearing verse, it stands as its **own single-verse passage** (`verse_count=1`, anchor = itself) rather than being forced into an unrelated neighbour. This also covers the **emergent-char case**: when a read surfaces a characteristic in a verse that carried no candidate at up-front build time (so it was outside every passage), that verse is given a single-verse passage on the per-book close, restoring the `verse → passage → lexical` chain. (First applied: 16 Psalms verses, `source='single-verse-emergent-char-2026'`, 2026-07-11.)

## The integrity invariant (non-negotiable)
- **Every `char_candidate` master span MUST have a corresponding active `wa_verse_records` (with its term and relations).** A candidate characteristic in the master **without** a verse-record is a **DB integrity violation** — not a coverage choice.
- When such a candidate is encountered, **stop and restore integrity first**: process the missing verse-record and *all* its relations (term registration in `mti_terms`, `verse_span_id`/`verse_id`/`mti_term_id` links, ownership) via the engine onboarding / per-book gate-1 corrective path. Only once the verse-record exists does that candidate's passage proceed to the read.
- Consequence: after repair the two populations are coextensive — seeding from verse-records and growing by candidate adjacency reaches every candidate. Any residual candidate-without-record is a violation to fix, never a run to silently skip or silently read.

## Scope (per book)
Verses where **`passage_id IS NULL`** AND the verse carries at least one **candidate characteristic** span (`verse_span_index.char_candidate = 1`). Each such verse must additionally satisfy the integrity invariant (an active verse-record for its candidate term); a violation is repaired before the verse is passaged.

## Procedure — deterministic, computed for the whole book up front
The passage ↔ verse-record ↔ master relationship is **deterministic** once `char_candidate` is stamped, so **all passage start/finish points for a book are designed before any lexical read begins**:

1. Sweep the book in canonical verse order. **Begin at the first verse carrying a verse-record** (the confirmed IB anchor / entry point).
2. **Grow the passage through consecutive adjacent verses that carry a candidate characteristic** — pre and post — for as long as the neighbour also carries a candidate. The first verse with **no** candidate closes the passage. A passage is therefore a **maximal run of consecutive candidate-bearing verses**; its first verse is the anchor.
3. For every candidate span drawn into the passage, **assert the integrity invariant**: it must have an active verse-record. If not → restore the verse-record + relations first (integrity gate above), then continue.
4. **Record the passage** (`passage` row: anchor = first verse, `start_*`/`end_*`, `ref`, `verse_count`, `source` tag e.g. `passage-build-2026`); set `verse.passage_id` for every verse in the run and `verse.is_passage_anchor` on the anchor.
5. Move to the **next unpassaged verse-record verse** and repeat until the book's candidate-bearing verses are all passaged.
6. **Only after a passage is recorded** does the read pull the **morphology for the entire passage** and begin the lexical process (Stage 2 of the cycle).

## What gets written / what does not
- **Write:** `passage` table (insert rows with a `source` tag marking the build); `verse.passage_id` for every scope verse; `verse.is_passage_anchor` on each anchor.
- **Do NOT write here:** `ve_lexical`, `wa_verse_records`, `verse_span_index` — the schema is **normalized**: none carry a passage column; they track the passage via `verse.passage_id` and propagate automatically. (Verse-record *creation* to satisfy the integrity invariant is a separate, gated onboarding step, not a passage write.)

## Governance
- **Integrity-gated:** backup → `_check_integrity_controls --snapshot` pre → apply → snapshot post → `--compare` (expect only `passage` / `verse.passage_id` / `is_passage_anchor` deltas, plus any deltas from verse-record repairs done under the invariant; no *new* invariant breach).
- **Re-check:** after applying, **0** candidate-bearing verses may remain with `passage_id IS NULL`, and **0** `char_candidate` spans may remain without a verse-record.
- **Per book only.** No cross-book operation.

## Cross-reference
- Cycle: `wa-characteristic-role-lexical-cycle-authoritative-v1-20260708.md` — this rule is its **Stage 0**; the cycle's DB-updates/integrity section states the same invariant.
- Linkage: `verse-analysis/_reports/wa-verse-passage-lexical-master-term-record-linkage-map-20260708.md` — the join keys this rule relies on.

*Recorded 2026-07-08. Tool: extend `scripts/_apply_passage_completeness_v1_20260707.py` for the candidate-driven scope (dry-run first), or a v2 successor.*
