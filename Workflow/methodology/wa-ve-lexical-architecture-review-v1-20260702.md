# ve_lexical — architecture review (redundancy & performance) — v1, 2026-07-02

> Requested by the researcher after the ruthlessness first-tier story was accepted: *"my impression is that there are a huge number of duplications or unnecessary records… look at database design for the lexicals to optimise it, reduce redundancy, and improve performance."* All figures are read live from `database/bible_research.db` (2026-07-02).
>
> **STATUS 2026-07-02 — Phase 1 EXECUTED (researcher approved a+b).** M63 / schema **3.37.0**: 507,651 legacy rows moved to `ve_lexical_legacy`; `ve_lexical` now **1,990 live rows**; duplicate index `ix_velex_vc` dropped; VACUUM reclaimed **129 MB** (769.7 → 640.5 MB). Script: `scripts/_apply_ve_lexical_phase1_archive_legacy_20260702.py`. **Phase 2 held** (pair-table normalisation + `from_span`/`to_span` FK-ising) until the model is proven across ~10 terms / both genres.

## 0. Verdict in one line
The impression is **correct**, but the redundancy is **not in the live model** — it is **legacy accretion**. The live lexical (`lexical-model-2026`) is **1,007 rows**; it shares one physical table with **424,408 rows of pre-reset legacy** that the new model never reads. The table is **99.76 % dead weight** to current work.

## 1. What is actually in the table (live figures)

| Slice | Active rows | Share |
|---|--:|--:|
| **Live model** (`source_provenance='lexical-model-2026'`) | **1,007** | 0.24 % |
| Legacy `v2_engine_iter1` (+ remap/ruleb variants) | 345,579 | 81.2 % |
| Legacy `audit` (lexical_note/sense/type triples) | 40,467 | 9.5 % |
| Legacy `faculty-verse-explicit-v1` | 20,447 | 4.8 % |
| Legacy `*_read_api` (object_type/cause/divine/location) | 17,915 | 4.2 % |
| **Total active** | **425,415** | 100 % |
| (soft-deleted, still on disk) | 84,226 | — |
| **Grand total rows** | **509,641** | — |

DB file is **769.7 MB** (was ~165 MB in April — the morphology + legacy lexical layers drove the growth).

The catalogue (`wa-ve-lexical-catalogue-v1` §7) already rules that legacy is **"left in place, not migrated, not retired… removed later with the rest of the redundant material,"** and that the new model is selected by `pair_kind IS NOT NULL` / `source_provenance='lexical-model-2026'`. So the legacy is *correct to exist* — but it does not need to sit in the **hot** table.

## 2. Findings, most-impactful first

### F1 — 99.76 % of the table is cold legacy in the same heap as the live model  **(highest value)**
Every scan, every index page, every `VACUUM` on `ve_lexical` carries 424k legacy rows past 1k live ones. The read filter (`source_provenance=…`) works, but it is a full-table filter each time because provenance is **not indexed**.
- **Fix:** move legacy to an archive table `ve_lexical_legacy` (same columns), leaving `ve_lexical` = live model only. Retains provenance (per §7), shrinks the live table ~420×. Reversible (it is a move, not a delete). This is the single change that answers the researcher's concern.

### F2 — duplicate index on `verse_context_id`
`ix_ve_lexical_vc` **and** `ix_velex_vc` are **both** `ON ve_lexical(verse_context_id)` — identical. One is pure waste (write cost + disk on every insert).
- **Fix:** drop `ix_velex_vc`. Trivial, zero-risk.

### F3 — deprecated `related_tier` column carries 317,718 values, all legacy
`related_tier` (T0–T7) is deprecated (catalogue §4). 317,718 active non-null values, **none in the live model**.
- **Fix:** once legacy is archived (F1), the column leaves the live table automatically. No separate action.

### F4 — `from_span` / `to_span` are TEXT, not foreign keys
Live pairs store `from=H6973@Exo 1:12`, `to=H6531` — a lemma+ref **string**. This cannot be joined, cannot be validated against `verse_span_index`, and stores a ~15-char text where an integer FK would do. The pair endpoints are exactly the spans we already index in `verse_span_index`.
- **Fix:** add `from_span_id` / `to_span_id` INTEGER → `verse_span_index(id)`; keep the text as an optional human label. Makes pairs joinable (needed for the cross-term/cohabitation layer, which walks pair endpoints across terms).

### F5 — derivable D1 values duplicate the measure layer
`sense` (=`verse_span_index.surface`) and `type` (=derived from `pos`) are stored per span but are **recomputable from the measure layer** (`verse_span_index` / `verse_morphology` / `lexicon`). 394 sense values verbatim-equal their span surface.
- **Trade-off, not a defect:** storing them makes the lexical a self-contained snapshot (one read, no join). Cost is ~40 % of the live rows (394 of 1,007). **Recommendation: keep** sense/type — they are the stable D1 anchor and the cost is tiny — but *stop* re-storing anything else that is a pure morphology echo. Flag this as a rule, not a migration.

### F6 — EAV row-per-value is fine now, will need a child table at scale
The live model is a classic EAV: one row per (span, dimension-value), ~5.1 rows/span, `value`/`notes`/`from/to`/`pair_kind` overloaded into one row shape that means different things per `ve_nr`. At 197 spans this is 1,007 rows. At corpus scale (~300k content spans) it projects to **~1.5 M live rows**, and the single flat shape makes per-span fetch and integrity constraints awkward.
- **Future (not now):** split into (a) `span_lexical` — **one row per span**: sense, type, role, gate, genre, resolution (the 1:1 facts); and (b) `span_pair` — **N rows per span**: the PAIR/EVENT items (source/seat/bearer/target/manner/effect/coupling) with `from_span_id`/`to_span_id` FKs; notes stay a small child. This removes the overloaded-row smell and gives the cross-term layer a clean join surface.
- **Do NOT do this yet** — the model is proven on one term. Locking a normalised shape before the item set stabilises would be rework paid twice. Revisit after ~10 terms across genres.

## 3. Recommended plan (phased)

**Phase 1 — now, low-risk, high-value (answers the concern):**
1. Create `ve_lexical_legacy`, move all non-`lexical-model-2026` rows into it (backup + dry-run + row-count verify).
2. Drop the duplicate index `ix_velex_vc`.
3. Add an index on `source_provenance` (or, post-move, it's moot — the live table is all one model).
4. `VACUUM` to reclaim the freed pages.
- Result: `ve_lexical` = ~1k live rows; every live query is effectively instant; the 769 MB file shrinks materially (legacy + deleted rows compacted).

**Phase 2 — deferred until the model is proven across ~10 terms / both genres:**
5. Add `from_span_id`/`to_span_id` FK columns; backfill from the text form.
6. Normalise into `span_lexical` (1/span) + `span_pair` (N/span) + `span_note`; retire the flat EAV shape for the live model.

**Not recommended:** deleting legacy outright (§7 says retain), or normalising now (premature).

## 4. What I did NOT change
Nothing. This is analysis. Phase 1 is safe and reversible and I recommend it, but it is a schema/data move and awaits your go-ahead per the interaction protocol. Phase 2 should wait until more terms are through the pipeline.

## 5. Open question for you
Two decisions:
- **(a)** Run **Phase 1** now (archive legacy + drop the dup index + vacuum)? It is the change that makes the "huge number of unnecessary records" go away without losing anything.
- **(b)** Hold **Phase 2** (the pair-table normalisation) until the model is proven — agreed, or do you want the FK-ising of `from_span`/`to_span` (F4) brought forward because the cross-term/cohabitation layer needs it?
