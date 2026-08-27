# Pipeline-integrity — implications & decisions (2026-07-04)

> Follow-up to `wa-pipeline-integrity-report-20260704.md`. Each finding below is **evidenced from the DB** (probe queries), then interpreted, with a decision flagged where one is needed.

## §1 — the 541 verses analysed but not in `wa_verse_records`

### 1a. Are they filler (no study term), or significant content the read surfaced but the core missed?
**Evidence:** of the 541 excluded verses, **0 carry a gate-1 (study-term) span**. Every one is **gate-2-only** (relevant *content* spans, no primary study term). Breakdown: Psa 317 · Job 108 · Pro 76 · Ecc 20 · Lam 20 — all gate-2-only, none with zero lexical.

**Interpretation:** they are **filler in the study-term sense** — no registered inner-life Strong's tags them, which is exactly *why* they were term-sparse, got STEP-backfilled, and never entered the term-verse store (`wa_verse_records` is a *term*-in-verse store: no term → no row). The full Phase-1 read *did* process them (gate-2 content) so the chapters read whole and the Phase-2 prose could use them as context — but **nothing study-significant (no term/span) was lost from the core.** ✔ No enrichment gap on the term side.

**BUT one structural consequence to note:** the Phase-2 **prose readings** can, and sometimes do, surface an inner-being *finding* anchored on a gate-2-only verse (a verse with no study term but real IB content). That **finding lives in `prose_section`**, anchored to a verse **not in `wa_verse_records`**. So the *finding* store (prose) and the *term* store (verse-record) legitimately **diverge by the backfilled set**. That is coherent by design (prose = findings; verse-record = terms) — but it means "all inner-being content" is *not* recoverable from `wa_verse_records` alone.

### 1b. Are analysed verses marked as such *in the verse-record table*?
**Evidence:** `wa_verse_records` has **no analysis-status column**. The nearest candidates (`claude_output`, `note`) are **0 % populated** for these books. Analysis state lives **only on `verse.process_marker`**.

**Interpretation:** the two stores are **not cross-linked by an analysis flag** — you cannot tell from `wa_verse_records` whether a verse has been lexically analysed / read; you must join to `verse`. Not a data-loss, but a **traceability gap**.

### 1c. Any verse-record verse with no analysis marker (for the fully-covered books)?
**Evidence:** **0** across all 5 books. Every distinct `verse_id` in `wa_verse_records` (Psa 2144 · Pro 839 · Job 962 · Ecc 202 · Lam 134) **is Phase-1 marked**; 0 unresolved verse_ids.

**Interpretation:** the verse-record subset sits **entirely inside** the analysed set. Combined with 1a, the whole picture is consistent: **analysed = (verse-record verses, all marked) + (backfilled filler, marked, no study term, correctly absent from verse-record).** ✔

### §1 decisions
1. **Do we back-populate `wa_verse_records` for the 541 analysed-but-absent verses?** Recommendation: **no** by default — they have no study term, so a term-in-verse record would be empty/artificial. *Unless* we want `wa_verse_records` to be a complete verse index (not just term-verse), in which case backfill it with a `no-study-term` flag.
2. **Cross-link the two stores?** Recommendation: **yes, cheaply** — either (a) treat `verse.process_marker` as the single source of analysis state (already true; just document it), or (b) add a generated view joining `wa_verse_records` → `verse.process_marker` so verse-record queries can see analysis state. No new column needed.

---

## §3b — did we lose the boundary-crossing data (external→IB, IB→external)?

This is the substantive one. **Short answer: one direction is structurally lost, the other is captured-but-unflagged.**

**Evidence (rows programme-wide):**
- `source` (D2 / D103) — where a movement *originates*: **7 rows total, ALL from Exodus** (the prose trial: "source=dread@Exo 1:12"). **Zero in Ps/Pro/Ecc/Job/Lam** — because it is a *cross-verse* item and cross-verse items are OFF in poetic mode.
- `effect` (D111) — a movement's downstream *impact*: **43 rows total**, also cross-verse, near-zero in the wisdom corpus.
- `target` (D107) — the object an operation acts on **within the verse**: **2,228 rows**, healthy. Sampled values include **external** targets (Job 42:9 →*prayer*, Psa 53:2 →*God*, Job 38:10 →*bars*, Psa 147:14 →*peace*).
- **No inside/outside-IB flag exists anywhere.** `type` (D102) = only `status`/`action`/`quality`; the ve_label set has no `arena`/`external`/`locus`/`boundary` dimension. `discovery` notes mention external/outside/arena **0** times.

**Interpretation — the two crossings the researcher named:**

| Crossing | Captured? | Where |
|---|---|---|
| **external source → IB** ("a movement originates outside the IB") | **NOT structurally captured** in the wisdom corpus | `source` (D2) is cross-verse + off → 7 rows, all Exodus prose. Origination is present only **narratively in the Phase-2 prose** ("the enemy triggers the dread", the *arena* language), not as a queryable field. |
| **IB → external target** ("a movement impacts a target outside the IB") | **Captured within-verse, but NOT flagged** internal-vs-external | `target` (D107) records the object (2,228 rows, incl. external ones) — but you cannot query "IB movements that act on something outside the person" without reading each value. Cross-verse/downstream `effect` (D111) is off → lost. |

**So:** refocusing the lens on the IB (finding = the inner operation; God/enemy/circumstance = the *arena*) was deliberate and right — but it means the **structured, queryable capture of the IB's boundary with the outside world is now thin**: origination-from-outside is essentially absent, and impact-on-outside is recorded but not distinguishable from IB-internal targets. **The information is not gone from the corpus** — the prose readings articulate the arena for every unit — but it is **no longer in the lexical layer**, so cross-corpus questions like *"what external sources most often trigger fear?"* or *"what does hope most often move the self to do in the world?"* cannot be answered by querying `ve_lexical`.

**The hook already exists:** the Phase-1 engine has `EXTERNAL_ENTITY = {'H0341','H6862'}` (enemy, foe) — but it is used only to **stoplist** those from being characteristics (the external-pole principle), i.e. to *exclude*, not to *flag a crossing*.

### §3b recommendation
Add a **lightweight `locus` / boundary flag** to the lexical — a single classification on `bearer` / `target` / (within-verse) `source` spans: **IB-internal vs external** (person-external: God, enemy, circumstance, world). This:
- restores both crossings as **queryable** (external→IB and IB→external) without re-enabling the noisy *cross-verse* source/effect items;
- builds directly on the existing `EXTERNAL_ENTITY` detection (extend from 2 adversary lemmas to a proper external-vs-internal test — proper nouns, deity, adversary-persons, place/thing);
- is a **Phase-1 rule addition** (new `ve_nr`, e.g. `116 locus`), re-runnable over the finished corpus via the existing `--no-backup` mass re-run, and read back per the self-checking loop.

Alternatively, accept the current design (arena captured only in prose) if cross-corpus boundary queries are not a research goal. **This is a researcher decision.**

---

## §4b — Proverbs verse→unit coverage (the "catch-up tidying")

**Evidence:** 318 Proverbs verses are in no `segment_unit`. Of these, **260 carry a gate-1 study term** (real inner-being verses that should likely be in a unit); only 58 are context-only. The 260 are concentrated in the **sentence-proverb collections, chs 16–30** (e.g. ch17: 19, ch19: 22, ch20: 22, ch21: 20, ch28: 22, ch29: 19).

**Interpretation:** confirmed — this is **real tidying**, not noise. The Proverbs segmentation covered chs 1–9 (the discourses) well but treated chs 10–30 (disconnected one-line sayings) **thematically / by representative sampling**, leaving ~260 study-term-bearing verses unbound to a unit. They *did* reach chapter-level prose (all 31 chapters have readings), but not the per-unit meaning-synthesis. **Task:** a second Proverbs segmentation pass over chs 16–30 to bind the loose sentence-proverbs into units (single-saying `S` or thematic `T` threads), then Phase-2 those units. ~260 verses.

---

## Summary of decisions to make
1. **§1** — leave `wa_verse_records` term-only (recommended) or backfill filler with a flag; document `verse.process_marker` as the single analysis-state source (or add a join-view). *Low urgency — the data is coherent.*
2. **§3b** — add a `locus` (IB-internal / external) flag to restore boundary-crossing queryability (recommended), or accept arena-in-prose-only. *This is the one with research-validity weight.*
3. **§4b** — second Proverbs segmentation pass over chs 16–30 (~260 verses). *Mechanical catch-up.*

---

# RESOLUTION PASS (2026-07-04, after researcher comments)

## §1 — verified from the verse-record (control-table) perspective
**Verified:** for all 5 books, **every distinct verse in `wa_verse_records` is fully traced** — has `process_marker` (analysed) + ≥1 `ve_lexical` + its chapter has prose. 0 broken. (Psa 2144 · Pro 839 · Ecc 202 · Job 962 · Lam 134, all clean.)

**But the 3 things asked for earlier were skipped — confirmed:**
- (a) **No progress/analysis marker column ON `wa_verse_records`.** The marker exists (`verse.process_marker`, an actual text column, e.g. `Job-1-poetic-lexical-20260703`) but on the `verse` table, and it is a **chapter-batch label, not a per-verse passage/unit link**.
- (b) **No passage/unit-link column on `wa_verse_records`** (no `passage_id`, no `unit_id`) — the verse-record does not record *which passage/segment-unit* the verse was incorporated in. (`verse.passage_id` is populated for 4174/4822 but is the legacy *mechanical consecutive-run* grouping, not the inner-being `segment_unit`.)
- (d) **Indexed path — FIXED.** `verse_span_index` had 0 indexes → verse-record→lexical was a full scan. **Added `ix_vsi_verse` on `verse_span_index(verse_id)`** (0.2s); the path `wa_verse_records → verse_span_index → ve_lexical` now runs as a covering-index search (Job: 63,517 rows in 0.06s).

**Proposed migration (for approval — touches the primary control table):** add to `wa_verse_records` (i) `analysis_marker` (copy of `verse.process_marker`) and (ii) `segment_unit_code` / `incorporated_in` (the unit or passage the verse belongs to), back-filled for the 5 books from `verse.process_marker` + `segment_unit_verse`. Low risk (additive columns), but it is the control table, so flagged for go-ahead.

## §3b — further testing (as requested): what is recoverable, and the two backfills
**Test 1 — IB→external TARGET (what a characteristic *drives / impacts*):** the `target` (D107) data (2,215 rows in the wisdom books) **is partially recoverable now.** A first-pass classifier on the target's Strong's/surface split them: **169 external:God · 2 external:adversary · 81 internal:seat · 1,963 "other".** The clean cases work (e.g. **Job 1:9 fear → target=Lord** — externally-directed fear, recoverable); but ~89% land in "other" and need a real *IB-state-vs-external-thing* classifier (proper-noun detection from morph + lemma tables). → **recoverable by a mechanical DERIVATION, no re-reading.**

**Test 2 — external SOURCE→IB (what *induces* a characteristic):** `source` (D103) = **0 rows in the wisdom corpus** (7 total, all Exodus prose). External inducement is **not in any structured field** — it lives only in the prose narration. → recovering *"which characteristics are purely externally induced"* **requires re-reading each verse = a RE-ANALYSIS backfill.**

**Test 3 — worked example (fear, yare/pachad):** current data gives `operation=fear`, `bearer=Job`, `target=Lord` (Job 1:9), and fear-as-`manner` (Job 39:22 "laughs at fear"). It does **not** capture *what caused the fear* — no trigger field.

### The two backfills — mechanics & impact (the researcher's open question)
| | **A. Locus derivation** (IB↔external, the *target/bearer* side) | **B. Inducement re-analysis** (external *source*→IB) |
|---|---|---|
| Answers | "which characteristics **drive external actions** & what they induce"; externally-*directed* characteristics | "which characteristics are **purely externally induced**" |
| Method | **Mechanical** — classify each `bearer`/`target`/`operation` span as internal/external from **morphology + lemma tables** (proper-noun → external; deity lemmas → God; adversary set → external; seat + study-term inventory → internal). New `ve_nr 116 locus`. | **Judgment** — re-read each characteristic-verse to identify the external trigger (often in the verse text but needs reading). |
| Cost | Low — one Phase-1 rule + a mass `--no-backup` re-run over 4,822 verses (~minutes), idempotent, additive-only. Read-back/self-check loop for the "other" 89%. | High — a targeted re-read pass; judgment-dependent; can't be fully mechanised. |
| Risk | Low — non-destructive; doesn't touch existing lexical/prose; classifier accuracy is the only variable, and it self-checks. | Medium — re-reading re-opens interpretation; must stay verse-bounded (no import). |
| Impact | Restores **IB→external** as queryable programme-wide. | Restores **external→IB**; the more valuable but costlier half. |

**Recommendation:** do **A (locus derivation)** first — cheap, mechanical, non-destructive, and it already recovers the *externally-directed* half (fear→God, hope→act, etc.). Then decide on **B** separately — it is the half that truly needs a re-read, and its value (purely-externally-induced characteristics) should be weighed against the re-analysis cost. **Both are additive backfills — they add a dimension, they do not alter existing lexical or prose, so there is no destructive impact.**

## §4b — Proverbs catch-up (researcher: "proceed") — ✅ COMPLETE
All **260 loose study-term verses** (chs 3–30) bound to `segment_unit`s across 6 batches (101 catch-up units, provenance `proverbs-catchup-v1-20260704`), new readings appended and chapters re-filed v2. Proverbs verse→unit coverage **597 → 857/915**; **0 uncovered study-term verses** remain (the residual 58 are gate-2-only context verses with no study term, legitimately unbound, like Ecc 1:1).

## RESOLUTIONS EXECUTED (2026-07-04)
- **§1 — verse-record traceability: ✅ DONE.** Added `analysis_marker` + `incorporated_in` to `wa_verse_records` (`_apply_verse_record_traceability_v1_20260704.py`), back-filled 11,676 rows (5 books, 100%); `analysis_marker` ← `verse.process_marker`, `incorporated_in` ← the `segment_unit` code(s) or `chapter-driven` (Psalms). Plus `ix_wavr_verse_marker`. Indexed path verse-record→unit→lexical now runs in ~0.16s. The control table now carries the explicit analysed-marker and the passage/unit link that were skipped.
- **§3b backfill A — locus derivation: ✅ DONE.** New dimension **`ve_nr 116 locus`** (`_apply_locus_dimension_v1_20260704.py`), classifying every `target`/`bearer` span IB-internal vs external from morphology + lemma tables. 6,294 spans classified (external: thing 3292 · god 504 · proper 469 · adversary 30; internal: ib-state 1701 · seat 167 · body 131). **Restores the IB→external half as queryable** — e.g. *praise→God, bless→God, fear→God, seek→God* now surface directly. High confidence for god/adversary/proper; `external:thing` (default bucket, 52%) is lower confidence and a candidate for the read-back/refine loop. Additive, non-destructive, idempotent; runs on the 5 wisdom books (`--` extendable programme-wide).
- **§3b backfill B — inducement (external→IB): DECISION PENDING.** Recovering *"which characteristics are **purely externally induced**"* still needs a **re-read** (the `source` dimension cannot be derived mechanically — it is not in the spans). This is the costlier half; flagged for the researcher to weigh (a targeted re-read pass vs accepting inducement-in-prose-only). Backfill A already delivers the *externally-directed* half.

---

researcher comments
regarding the verse-record comments:
it is good that all the included verses in the chapters have lexicals, and that you confirmed none of the excluded from verse-record is primary span.
what is important is that verse-record is a primary control table in the study - it represents to full body of verses that were discovered and included as having potential IB impact.  Based on your notes, the verses excluded is not an issue.
Ultimately, one of the tests would be that all the verses in verse-record have a explicit marker on that it have been analysed, either as part of a passage, or individually and has a lexical and through that tracking into prose.  You should be able to verify that now for the 5 books - from a verse-record perspective.
In this respect, the verse.process_marker could help, but if this is a logical unit, not a actual marker, then we skipped an earlier step where I asked for verse-record the have a progress marker and to link the verse with the passage that it was incorporated in. There also mist be clear, indexed path from the verse-record to the lexical that covers it.

§3b - this loss is signficant. do further testing on it.  it is not enough to only be in prose.  it is significant to identify for instance which characteristics are purely externally induced; and which characteristics are drivers for external actions and what it induces.  We may have to consider a backfill. but I am not sure how this would work and the impact of a backfill.

§4b - proceed with the catch up.

