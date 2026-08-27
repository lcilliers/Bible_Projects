# DB integrity & completion — overnight work (2026-07-05)

> Task set by the researcher before sleep: *"ensure that every lexical is properly linked, with a complete record, in the terms table and in the verse-record, and all related fields properly completed. This is not about interpretation — finishing the DB entries that should have taken place. I want a DB that has integrity, complete, not with some records missing."*
>
> I did the safe, determinate completions and stopped short of the destructive ones — with the hard numbers below so you can see exactly why. Backup taken first: `backups/bible_research.pre-lexical-completion-20260705T200843Z.db`.

---

## 1. What I found — the existing curated records are ALREADY complete and cleanly linked

Facts, DB-only:

| Check | Result |
|---|---|
| active `ve_lexical` rows | 404,019 |
| `ve_lexical` rows whose `verse_span_id` does not resolve (orphans) | **0** |
| `ve_lexical` rows with NULL span (Leviticus, keyed by `verse_context_id` instead) | 47 (linked, not orphaned) |
| active `wa_verse_records` | 60,472 |
| `wa_verse_records` NULL on `mti_term_id` / `word_registry_fk` / `verse_id` / `book_id` / `term_id` / `verse_text` / `transliteration` | **0 each** |
| `wa_verse_records` NULL `morph_code` | 93 → **63 backfilled**, 30 unfillable (source also empty) |
| `wa_verse_records` NULL `stem` | 41,352 — but **legitimately empty for non-verbs** (nouns/particles/adjectives have no Hebrew stem); only 42 verb rows were determinately fillable → **42 backfilled** |

**The verse-record and term tables are structurally complete and fully cross-linked.** There is no meaningful "unfinished data entry" in the curated tables. The linkage chain `ve_lexical → verse_span_index → verse → wa_verse_records → mti_terms` has zero broken links.

## 2. What I completed (safe, determinate, reversible)

`scripts/_apply_verse_record_structural_backfill_v1_20260705.py` — filled only NULL fields that had a single authoritative value on the row's own span (unique match), source = `verse_span_index` (linguistic source of truth):
- **63 `morph_code`** values backfilled.
- **42 verb `stem`** values backfilled.
- Total **105 field completions**. No new rows, no interpretation, no propagation of `ve_lexical` values.

That is the **entire** set of entries that could be safely finished. The DB is now as structurally complete as its authoritative sources allow.

## 3. What I did NOT do — and why it would have DESTROYED integrity, not completed it

The literal instruction ("link *every lexical* into the terms table and the verse-record") resolves, against the data, to:
- register **4,392 strong's** into `mti_terms`, and
- add **63,376 (verse, strong) rows** into `wa_verse_records`.

I checked what those are. **They are the entire Hebrew vocabulary**, because the index-driven build lexicalised *every content word* (both gates), not a curated inner-being set. The top of the "missing" list:

`H3068 LORD ×10,313 · H0559 to say ×8,096 · H0776 land ×5,316 · H1121 son ×4,094 · H0430 God ×4,053 · H6440 face ×4,020 · H6213 to make ×3,871 · H5414 to give ×3,783 · H3117 day ×3,747 · H0935 to come ×3,717 · H1004 house ×3,276 · H4428 king ×3,030 · H8085 to hear · H3478 Israel · H7725 to return · H1697 word · H1961 to be · H1696 to speak · H7200 to see · H5971 people · H1980 to go · H1471 nation · H0376 man · H5869 eye …`

Registering *LORD, say, land, son, God, king, day, house, make, give, come, hear, see, go* as inner-being "terms" and "verse-records" would:
1. **Convert the curated tables into a full concordance** — diluting the ~2,400 curated inner-being terms into a ~5,090-entry every-word list, and the 60,472 IB verse-records into ~124,000 every-span rows. The tables would no longer *mean* "the inner-being record."
2. **Propagate the unreliable `ve_lexical` values** we found on Isa 43:1–2 (self-flagged `bearer unreliable`, `forbidden (neg particle)` mis-smeared onto *redeemed*/*created*, coverage holes) into the tables that are supposed to hold integrity.

That is the definition of *complete but not true*. So I stopped.

## 4. The real finding (the root, restated)

The premise that there are "missing entries to finish" **does not hold for the curated tables** — they are complete. The gap is **conceptual, not clerical**:

- `ve_lexical` is a **mechanical full-text decomposition of every word** (5,090 strong's, every content span).
- `wa_verse_records` / `mti_terms` are a **curated inner-being selection** (~2,400 terms).
- **No mechanical rule bridges the two.** Deciding which of the 5,090 vocabulary items are "inner-being related" is exactly the IB-relevance judgement — which is *interpretation*, and which the gate signal cannot supply reliably (Isa 43 showed `redeemed` tagged `2-relevant` while `Fear`/`called` were `1-primary`).

So "finish the entries" cannot be done mechanically without either (a) flooding the curated tables with the whole language, or (b) making the interpretive IB-cut. Neither is a data-entry task.

## 5. The one decision that is genuinely yours (for the morning)

Not something I should choose while you sleep:

**What is the intended relationship between `ve_lexical` (every word) and the curated IB tables (selected terms)?** Three coherent options exist — each a design decision, not a data fix:
1. **Keep them separate by design** — `ve_lexical` is the working span-layer; the curated tables stay curated; a *reviewed* IB-cut promotes selected spans into the verse-record (interpretive, done per book).
2. **Make `wa_verse_records` the full span-record** — accept that it becomes a concordance and re-scope everything downstream to that (large, changes the study's spine).
3. **Treat `ve_lexical` as not-yet-trustworthy** (per method §13, the sanity-check never ran) and rebuild the curated layer from a trustworthy pass rather than linking the current one.

I've left the numbers, the backup, and this decision for you. Nothing destructive was done; the 105 safe completions are applied.

*Filed 2026-07-05 overnight. Backup: `backups/bible_research.pre-lexical-completion-20260705T200843Z.db`. Applied: `scripts/_apply_verse_record_structural_backfill_v1_20260705.py`. Audit numbers reproducible from `ve_lexical` / `wa_verse_records` / `mti_terms` / `verse_span_index`.*
