# Verse-meaning fan-out index — design + validated proof (master coverage index)

- **File:** wa-verse-meaning-fanout-index-design-v1-20260626.md · **2026-06-26 · Author:** Claude Code.
- **Why:** the verse-record table's multiplicity (XREF copies, deleted homographs, missing units) is causing silent coverage loss (proven at Pro 24:20: "evil" stranded on deleted homograph H7451H). This index is the master, queryable check of verse-meaning completeness, fanning out verse → span → record → lexical → compound with a status at each level.

## 1. Fan-out levels (verse is king; morphology is the span source of truth)
1. **Verse** — unique by reference (`verse` table, 23,593). Active = has ≥1 active study span; flagged otherwise.
2. **Span** — each word-occurrence in the verse (`verse_morphology`) whose Strong's belongs to a **study lemma** (its Strong's family contains a clustered term). Morphology is authoritative (`project_morph_is_source_of_truth`).
3. **Verse-record** — for each span, the `wa_verse_records` matching its Strong's: present? active? on a deleted term?
4. **Lexical** — for each active record's unit (`verse_context` → `ve_lexical`): present? missing?
5. **Compound** — `ve_label='compound'` entries on the unit: present? missing?

## 2. Span status taxonomy (validated)
- `OK` — active record + unit + lexicals (fully analysed).
- `UNIT_NO_LEXICAL` — unit exists but no lexicals.
- `RECORD_NO_UNIT` — active verse-record but no `verse_context` unit (e.g. Exo 32:11 *wrath*).
- `RECORD_ALL_FLAGGED` — record(s) exist but all `delete_flagged`, no active home (e.g. Exo 32:11 *mighty*).
- `STRANDED_DELETED_TERM` — Strong's maps only to a `status=delete` term, never re-mapped to the active sibling (e.g. Pro 24:20 *evil* H7451H → should be H7451A/M27).
- `NO_RECORD` — study-lemma span with no verse-record at all.

## 3. Validated sample
**Pro 24:20** (3 spans): wicked=OK · evil=STRANDED_DELETED_TERM · no=NO_RECORD(function-word leak).
**Exo 32:11** (14 spans): burn-hot/power/hand=OK · wrath=RECORD_NO_UNIT · mighty=RECORD_ALL_FLAGGED · implored/the/brought-out/great=STRANDED · Lord/people/Egypt=NO_RECORD.
**1Cor 16:19** (6 spans): churches/church=OK · with=STRANDED · and/house/Lord=NO_RECORD.

→ The index works and immediately localises the multiplicity damage.

## 4. Known refinement (to include in the full build)
The study-lemma filter (family-has-a-clustered-term) leaks a few genuine function words (`and`, `not`, `Lord`) where a homograph in the family is clustered. Fix: add a **`qualify_basis`** column = `own-clustered` (the span's own Strong's has a clustered mti) vs `family-only` (only a sibling is) vs `stranded-sibling-clustered`. Real gaps (evil) are `stranded-sibling-clustered`; function-word noise is `family-only` and filterable. No span is dropped — just labelled.

## 5. Proposed deliverable (needs go-ahead — DB write)
- **DB table `verse_span_index`** (all-in-DB rule): one row per (verse_id, word_index, strongs) with: reference, verse_active, span surface/pos, qualify_basis, n_records, n_active_records, mti_status, n_units, n_lexical, n_compound, **status**. Drop-able/rebuildable; provenance-stamped.
- **Summary `.md`**: corpus counts per status × testament, top stranded lemmas, verses with the most gaps.
- Builder script `_build_verse_span_index_v1_20260626.py` (read-only except creating/refreshing the one index table).

**Decision needed:** confirm the deliverable = a materialised `verse_span_index` DB table (recommended, queryable, reusable) + summary, and the span scope = study-lemma words (not every word). On your go-ahead I build and run it across all ~23.6k verses.
