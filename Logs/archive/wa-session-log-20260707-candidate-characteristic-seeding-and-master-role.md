# Session log — 2026-07-07 — candidate-characteristic seeding + master-index role column

> Session began with "go back to previous session" (resume the Proverbs ch-by-ch role reassessment) and turned into a substrate/architecture rethink that produced (a) a **role column on the master index**, and (b) a **candidate-characteristic seed** for the whole OT, built from the registry word-list + curated synonyms + an inner-being judgement pass. Tomorrow: begin the **lexical process on the seed spans that have no lexical**.

---

## 1. Where it started (and why it pivoted)
Resumed the paused per-book corrective pipeline. Proverbs **ch1–6 role reassessment was LIVE**; ch7 was authored (`pro007-roles.json`) and dry-run — **held, never run live**. Reviewing ch7 exposed that the standalone/qualifier boundary was unresolved, which opened a deeper question: **is the substrate we're re-reading even sound?**

Investigation (all read-only, evidenced):
- **62% of the OT has no lexical at all** — of 232,877 OT real-strong spans, only 37.7% carry a role; 62.0% (144,287) have no `ve_lexical`; 0.3% have a lexical but no role.
- Existing roles are **~50% wrong** (ch7 corroborated) and vocabulary-inconsistent (`qualifier` vs `process-qualifier`, plus a Leviticus free-text taxonomy).
- **905 Psalms verse-records** are unlinked to the master index (`verse_span_id` NULL) — the load-bearing link that broke.
Conclusion (researcher): stop re-reading a substrate that is incomplete + wrong; fix the foundation first.

## 2. Master index — understood, then extended
- `verse_span_index` = the **term-verse-span master**, built 1:1 from `verse_morphology` (one row per Hebrew word), maintained by initial rebuild + incremental append. Each row is uniquely keyed by `id` (or `verse_id,word_index`); the **strong is NOT unique** (repeats within a verse and corpus). Links (`wa_verse_records`, `ve_lexical`) point INTO it via `verse_span_id`; no junction table; the `mti_terms` tie is by strong-string and partial.
- The master had **no notion of "characteristic"** — that lived only in `ve_lexical` role (`ve_nr=115`), discoverable only by join.
- **Decision + build (M64):** added `role, role_provenance, role_set_at, role_source_ve_id` columns to `verse_span_index`; backfilled verbatim from the active `ve_nr=115` roles (87,834 filled, 16 conflicts flagged CONFLICT). Schema **3.37.0 → 3.38.0**. These roles are the *existing, known-imperfect* ones, imported for analysis, **not trusted**. Backup: `backups/bible_research.pre-role-master-20260707T170834Z.db`.

## 3. Role model — simplified (agreed)
A word that **elaborates / qualifies / is an object or source** is **not a characteristic and needs no role** — it is fully described by its **dimension** (D5 target/object with object-type, D2 source, D3 seat/bearer, D6 manner, …). So:
- **role = { characteristic, standalone, uncertain }** — "qualifier" as a role is **retired**.
- Relational person/thing words are carried by their dimension pair, not a role.
- Two orthogonal axes: *is the lemma a characteristic?* (lemma-level) vs *does this occurrence fill a dimension of a characteristic?* (per-verse). A word can be both.
See `wa-master-index-role-column-design-and-debate-20260707.md`.

## 4. The candidate-characteristic seed (the session's main product)
Purpose: **isolate the lemmas that COULD be a characteristic**, to seed the verse-level lexical process (which reads verse + passage and confirms/demotes + captures dimensions). The seed is **over-inclusive** (a candidate may be an object/standalone in a given verse) and **non-exhaustive** (the read may still surface misses).

Built in layers (dead-ends recorded honestly):
1. **Lemma inventory** — grouped all master lemmas excluding particles → `research/discovery/lemma-inventory-master-no-particles-20260707.json` (11,804 lemma entries; OT Hebrew 6,677 + Aramaic 636).
2. **✗ strongs_list route — REJECTED** (matched every co-occurring strong; LORD→lust).
3. **✓ Registry direct match** — lemma gloss == registry English word (221 words) → **748** lemmas.
4. **✗ 277 `characteristic` table — REJECTED** (phrasal short_names → incidental-word noise: dwell→Security, ear→Attention).
5. **✓ Curated synonyms** — `research/discovery/registry-synonyms-curated-20260707.json` (reviewable) → **+414** (total 1,162 all-lang; 638 OT).
6. **✓ IB-judgement pass** over the 6,675 unmatched OT lemmas — broad semantic net (269 flagged) → manual accept/reject → **+186** IB additions (74 rejected non-IB, 9 prefix-artifacts removed). Files: `ib-judgement-accepted-20260707.md`, `ib-judgement-rejected-20260707.md`.

**Result: 824 OT candidate-characteristic lemmas** (`char_matched` = registry, `ib_candidate` = judged). In the master these mark **25,155 seed spans (10.8%)** across **12,672 verses (63.3%)**. ~36.7% of OT verses carry no candidate (genealogies, itineraries, ritual lists — correctly empty).

## 5. DB / code state
- **DB:** M64 role columns + backfill LIVE (schema 3.38.0). Integrity intact (325,474 master rows). ch7 NOT run (still dry-run only). No role reassessment beyond ch1–6.
- **Scripts:** `_apply_add_role_to_master_index_v1_20260707.py` (M64). Analysis scripts in scratchpad (seed build, matches, IB judgement) — the durable outputs are the JSONs/mds below.
- **Data artifacts (`verse-analysis/psalms/_model/`):** `lemma-inventory-master-no-particles-20260707.json` (the seed), `registry-synonyms-curated-20260707.json`, `ib-judgement-accepted/rejected-20260707.md`, `ot-lemmas-unmatched-20260707.md`.
- **Design/analysis (`verse-analysis/_reports/`):** `wa-master-index-role-column-design-and-debate-20260707.md`, `wa-ot10-morphology-and-16dim-derivability-20260707.md`, `wa-characteristic-table-full-dump-277-20260707.md`, this log.

## 6. ★ Starting point for TOMORROW (2026-07-08)
**Goal: begin the lexical process on the OT candidate-characteristic spans that have no lexical.**

Concrete first steps, in order:
1. **Push the seed onto the master** — flag the 25,155 seed spans (e.g. `role='characteristic-candidate'` provisional, distinct from the backfilled real roles) so the worklist is queryable and forward/back-trackable. *(A dedicated `_apply_*` script; integrity-gated; NOT yet done.)*
2. **Scope the worklist** — seed spans with **no lexical** (subset of the 144,287 no-lexical OT spans). That is the day's target set.
3. **Design + pilot the seeded lexical read** on ONE book/chapter (recommend a prose chapter, since prose is the untouched bulk): read verse + passage → for each candidate span, **confirm** it's the operative characteristic or **demote** it (object/standalone), and **capture its dimensions** (D1 mechanical from morphology; source/target/seat per-verse). Morphology can generate D1 + the 8 reliable dimensions; **role is NOT derivable from morphology** — it needs the read (see the 16-dim derivability table).
4. Read back, adjust the synonym dict / candidate set if the pilot reveals gaps, then scale.

**Do NOT** resume Proverbs ch7 role reassessment on the old basis — the role model changed (qualifier retired). Any prior role work is legacy pending the new model.

## 7. Open items / caveats
- Candidate seed is **approved** but the synonym dict + IB accept-list are **reviewable** — veto anything (`ib-judgement-*` files).
- The backfilled master roles are the **old, ~50%-wrong** ones — a working surface, not truth; the seeded read overwrites them.
- 905 Psalms unlinked verse-records + 16 CONFLICT role spans remain as tracked residuals.
- Leviticus free-text role taxonomy sits in the backfill unnormalised.

*Filed 2026-07-07. DB M64 live + backed up. Resume at §6 step 1.*
