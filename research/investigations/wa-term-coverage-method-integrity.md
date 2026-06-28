# Term-coverage method integrity — does the registry→terms→related-terms cascade hold?

> **Doc version:** 2 · **Last updated:** 2026-06-28 · finding. Triggered by: why was cruelty/`perek` missed? (see `wa-ruthlessness-investigation.md` §2). **This validates the *method*, not the one item.** v2: researcher comments folded in (§Implication corrected, §Weakness added), coverage audit run (§Audit).

## The question
We expected: **registry word (English) → STEP terms → STEP related-terms** to catch every IB-relevant term. `perek` (ruthlessness) was missed. Is the cascade structurally sound, or does our reliance on STEP's related-graph have a hole?

## The test (empirical, 2026-06-28)
| probe | result |
|---|---|
| Does `perek` H6531 appear as a recorded related-word of *any* studied term? | **0 rows** — total orphan |
| What does our studied "ruthless" term `arits` H6184 relate to (DB)? | `terror` H4637 · `dreadful` H6178 · `tremble` H6206 — **the dread family only** |
| STEP **live** related-words for `arits` | identical — terror / dreadful / tremble. **No cruelty terms.** |
| STEP **live** related-words for `perek` | **`paroketh` H6532 "curtain" — and nothing else.** A same-root **homonym**, not a semantic relative. |

## Root cause — three compounding structural facts
1. **No English seed for cruelty.** The ~215 registry words have no cruelty/ruthlessness/harshness entry. The English list is the **entry gate**; with no seed, the concept's whole sub-field can only be reached by spillover from adjacent concepts.
2. **STEP `relatedNos` is shallow, and sometimes morphological — not a semantic ontology.** It returns ~1–3 terms, one hop. For `perek` the only link is a spelling-homonym (`curtain`); for rare words it is near-empty. It associates; it does not map meaning.
3. **Contextual capture poisons cross-concept discovery.** `arits` is genuinely a cruelty word, but it was pulled under **dread**, and its relations point **back to dread** — not outward to its cruelty neighbours. A term captured under concept X carries X's relations, so it does **not** act as a seed for its own home concept. Cruelty therefore never gets seeded, even though a cruelty word is in the study.

## The integrity verdict
- The cascade is sound for **expanding a seeded concept** (take a registry word, pull its lexical family). That is what it is for, and it works.
- It is **not a discovery mechanism** for concepts the English list omitted, and **not a complete semantic graph.** STEP `relatedNos` has rare-word orphans, homonym links, and single-dimension/contextual linking.
- Therefore **term coverage = closure of (a human-curated ~215-word English list) under (a shallow, leaky association graph).** That set is strictly smaller than "all IB-relevant Hebrew/Greek terms." Blind spots are **guaranteed**, not accidental; `perek` is a proven one.
- **The binding constraint is the human curation of the English word list.** STEP cannot find what the list did not seed, and adjacent-concept spillover is unreliable (homonyms, contextual capture). So the cascade's completeness can never exceed the completeness of the English seed list — and we already know that list has gaps (cruelty; likely violence; possibly others).

## What this does NOT mean
- The cascade is not broken or useless — within a seeded concept it pulls the family well, and the digested cluster work (M01, M06, etc.) remains valuable.
- It means the cascade must be understood as an **index over the corpus, not a census of it.**

## Implication — verse-fanout is a better substrate, but NOT an automatic guarantor (researcher correction)
The verse-fanout enters from **the verse**, where *every term that occurs is present* — independent of the English seed list and the `relatedNos` graph. `perek` is invisible to the cascade but present at the verse (Exo 1:13, Lev 25:43). **But — researcher correction — catching `perek` was a *human* intervention; the verse-fanout did not *automatically* flag it.** The method puts the orphan term in front of a reader; a human still has to notice it. So:
- the registry/STEP cascade is a **partial, leaky index**;
- the verse-fanout reads the **complete substrate**, but coverage still depends on **human attention** — unless a **mechanical audit** does the noticing. That audit is §Audit below (the only way to systematically surface orphans without relying on a human happening to spot one).

## A deeper, irreducible weakness (researcher comment)
An IB phenomenon may **never surface in any verse** (not lexicalised at all). **No method — cascade or verse-fanout — can catch that.** This is a recognised fundamental weakness of the study. The only mitigation is an **open mind**: actively holding that there may be operations of the inner being not represented in the study, and not treating "absent from the corpus" as "does not exist."

## Recommendations (for researcher decision — not actioned)
1. **Re-frame the registry as a *seed list*, not a coverage boundary.** Expect gaps; do not treat "not in the registry" as "not IB-relevant."
2. **Use the verse-fanout as the coverage guarantor** — terms surface at the verse regardless of seed/relatedNos. Untracked-but-present terms (like `perek`) become the signal for registry gaps.
3. **Consider a coverage audit:** sweep the corpus morphology for high-frequency / clearly-IB terms that have **no study identity** (orphans like `perek`, `chamas`) — a finite, mechanical check that surfaces the blind spots the cascade left.
4. Do **not** rely on STEP `relatedNos` to deepen a concept's field — it is too shallow/leaky; deepen via the verse-fanout and the multi-contributor spiderweb instead.

researcher comments:

1 - that is already established that the registry can be incomplete, and that discovery of new items could come via various routes over the life time of the study.
2- the verse-fanout is helpful, but picking up on ruthlessness was a human intervention, verse-fanout did not automatically surface the potential issue.
3 - the coverage audit must use the span-verse-lexical index as the base.  At least this will highlight any span that is IB related that is not included in the study.
4 - There is still a possibility that a IB phenomena is being missed because it has not surfaced in any verse.  This is recognised as a fundamental weakness of the study and the mitigation against it is to have an open mind about an operation in IB that is not present in the study.

Action steps
1 - perform the coverage audit, and report on it in this document.
2 - continue to build out the new registry 216 in a separate md.
3 - bring memory and study instructions up to date

---

## Coverage audit (action 1) — results
**Base:** the span-verse-lexical index (`verse_span_index`), per researcher direction. **Orphan** = a corpus base-Strong's the study has **never seen** (absent from `mti_terms` ∪ `wa_term_inventory` ∪ `wa_term_related_words`).

**Headline counts:**
- Corpus base-Strong's in the span index: **11,702**
- Known to the study (ever seen): **5,409**
- **Orphans (in the corpus, never seen): 7,057 (60%)** — but the bulk are function words, particles, and proper/concrete nouns (land, day, Moses, sword…), legitimately not IB.
- Filtering orphans by **IB-semantic surface forms** (the ESV words they render as) → **60 candidates**, of which ~45 are genuine IB-relevant terms with **no study identity.**

**Genuine IB-orphan candidates, by concept** (verses · Strong's · ESV surfaces):
- **Hatred:** `miseo` G3404 (27v, "hate/detestable") — orphan **even though M06 Hate exists** ⚠
- **Oppression:** `yanah` H3238 (17v, oppress/wrong) · `lachats` H3905 (12v, oppress) · (+ `chamas` violence, from the ruthlessness thread)
- **Stubbornness / rebellion:** H6203 (24v, stiff-necked) · `sarar` H5637 (15v, stubborn/rebellious)
- **Weariness / faintness:** H3021 (24v) · H5848 (13v) · H5889 (12v) · H3543/H3544 (faint/dim) · H5888 · H1809 · G1590 (fainthearted) · G2577 (grow weary)
- **Mockery / scorn:** `laag` H3932 (13v) · H3933 (5v) · `qalas` H7046 (3v) · `empaizo` G1702 (8v)
- **Tenderness / softness:** `rak` H7390 (15v) · `rakak` H7401 (8v) · H2949 (tender care)
- **Arrogance / haughtiness:** H6277 (4v, insolent/haughty) · H3093 (2v, arrogant)
- **Trembling (fear-somatic):** `raash` H7493 (28v, quake/tremble)
- **Abhorrence:** `taab`/`gaal` H1602 (8v, abhor/loathe) · G0655
- **Grief / sympathy:** `nud` H5110 (22v, grieve/sympathy) · H0109
- **Folly / instability:** G0453 (foolish) · G3153 (futility) · G0182 (unstable/restless)
- **Rage / fierce:** H7283 · G5433 · G5467 (fierce)
- **Bitterness:** `laanah` H3939 (8v, wormwood/bitter)
- **Sparing / pity:** H6452 · G5339 (spare/refrain)

**Noise filtered out** (matched the keyword but not IB): "kind/sort/race" terms (G5108, G4169, G1085, H4327…), `magos` G3097 (magician), `tenuphah` H8573 (wave offering).

**Audit findings:**
1. **Dozens of IB-relevant terms have no study identity** — not a one-off; `perek` is one of ~45.
2. **The cascade leaks even within seeded concepts.** M06 (Hate) exists, yet `miseo` G3404 ("to hate", 27v, NT) is an orphan. So the gap is not only "missing concepts" but "missing terms inside present concepts." ⚠ (worth verifying G3404 isn't hiding under another code.)
3. The orphan filter is mechanical and finite — this list is reviewable; it is the safeguard that does the "noticing" so it does not depend on a human happening to spot a term in a verse.

**Next on the audit:** researcher reviews the ~45 candidates → promote the genuine IB-orphans (each via the registry-seed path, now understood). Track in the reg216 build-out doc / a coverage-gap register, not here.

## Researcher comments — recorded & addressed
1. *Registry can be incomplete; discovery via various routes over the study's life is expected.* — Agreed; this doc validates the **mechanism** of the gap and **quantifies** it (45 IB-orphans), it does not claim the incompleteness is news.
2. *Ruthlessness was a human catch; verse-fanout didn't auto-surface it.* — Corrected in §Implication; the mechanical audit (above) is the non-human safeguard.
3. *Audit must use the span-verse-lexical index as base.* — Done (above).
4. *An IB phenomenon may never surface in any verse — fundamental weakness; mitigate with an open mind.* — Recorded in §A deeper, irreducible weakness.

## Action-step status
1. Coverage audit + report here — **DONE** (above).
2. Continue reg216 build-out in a separate md — **NEXT** → `wa-ruthlessness-investigation.md` (awaits the §5 confirmations there: perek→M06, re-home?, violence gap?).
3. Memory + study instructions up to date — **memory: done** ([[feedback_term_coverage_cascade_is_index_not_census]]); **registry-management guide update: queued** (re-frame registry as seed-list; add coverage-audit + newer-constructs catch-up).

researcher observations
That is a really great find.  These 45 terms must find there way into the study.
It is noticable that the majority of the words have a negative/sinful/'bad' connotation; very few positive/'good'/'God-like' terms emerged - this may because all the good words are already covered, or because the verses are predominantly about the 'bad' side of IB.
Is it possible to extract all span from STEP for the whole bible, and do a similar excercise.
Before we proceed with adding the discovered terms, lets try and surface some more.

---

## Whole-Bible span extraction — feasibility & plan (researcher observation 3)
**Is it possible? YES — confirmed 2026-06-28.** STEP's `/rest/bible/getBibleText/{VER}/{ref}` returns full morphology (`<span morph=… strong=…>` per word) for **any** reference, independent of Strong's search. Proven on **Lev 25:44** (not in our corpus): it returned `H5650` (ebed), `H0519` (amah), `H7069` (qanah)… Our span index is term-bounded **only because the morphology-ingest loop iterated over existing `verse` rows** (the ~76% term-pulled subset), not because STEP lacks the rest.

**Why this matters:** the current orphan audit ran against the **partial** corpus. A whole-Bible morphology pull would (a) surface orphan terms that occur **only in never-pulled verses** (currently invisible), and (b) **complete the verse index to the full canon** — closing the 76%-subset gap identified earlier.

**Plan (resumable, idempotent — reuses `_apply_ingest_verse_morphology.py`):**
1. Enumerate the full canonical reference list (~31,102 verses / 1,189 chapters). Pull **per-chapter** via `getBibleText` (~1,189 calls, far fewer than per-verse).
2. Add the ~7,500 missing canonical verses to the `verse` table.
3. Ingest their morphology → `verse_morphology` (circuit-breaker + resume already built in).
4. Rebuild `verse_span_index` over the complete set.
5. **Re-run the orphan audit** against the now-complete morphology → the fuller IB-orphan list.
6. **THEN** triage + add the discovered terms (the 45 + any new) — per researcher: surface more *first*.

**Integrity note:** this changes the corpus baseline (extends `verse` + `verse_morphology` + `verse_span_index`). Recommend a **pilot** first (one book, e.g. the missing verses of a sampled book) to validate the pipeline and show the orphan-delta, then the full run — with a DB backup before the first write.

## Negative-skew observation (researcher observation 2)
The ~45 IB-orphans skew **negative/sinful** (cruelty, violence, oppression, mockery, arrogance, rebellion); few positive/'good'/'God-like' terms. Two hypotheses, not yet resolved:
- (a) **positive concepts are already well-covered** — the study has registries for love/compassion/kindness (M05), mercy, peace, hope, joy, etc., so few positive orphans remain; vs
- (b) **the corpus verses are predominantly about the 'bad' side** of the inner being.
The **complete** orphan audit (after whole-Bible extraction) will test this — a complete orphan set lets us compare the positive/negative balance of orphans against the balance of *known* terms. Recorded for that check; not resolved now.

## Action-step status (updated)
1. Coverage audit (partial corpus) — **DONE**.
2. reg216 build-out — **DEFERRED** behind "surface more first" (whole-Bible extraction → complete re-audit → then add terms).
3. Memory done; registry-guide update queued.
4. **NEXT:** whole-Bible morphology extraction (pilot → full) — awaiting researcher go-ahead on the plan above.

researcher comments:
a) extracting all the verses, and using the span to its full extent sounds very enticing - if we add it to the DB, then we must be very clear to not contaminate our verses that is relevant to the study.  We do not want to expand the dataset to such an extent that it slows down and complicates every search and discovery in the future.  It can however narrow the potential gap of discovery of IB related operations in scripture.
go ahead with pilot, and think through the implication of and volume of the data.

---

## Whole-Bible extraction — PILOT RESULTS (2026-06-28)
Two contrasting books, into a **segregated** table `verse_coverage_morphology` (parsed spans only, no HTML; study tables untouched — non-contaminating by construction). Script: `_apply_pilot_canon_coverage_leviticus_v1_20260628.py`.

| book | canon | in study | missing | coverage spans | new-to-audit orphans* | **IB-semantic** |
|---|---|---|---|---|---|---|
| Leviticus (law/ritual) | 859 | 688 | 171 | 1,496 | 17 | **0** |
| Proverbs (IB-dense) | 915 | 839 | 76 | 551 | 11 | **0** |

*orphan AND appearing only in missing verses (never in any study span).

**Volume:** ~0.09–0.12 MB per book → full-Bible ≈ **65k spans / ~4 MB** in the segregated table (the 677 MB DB is mostly raw HTML in `verse_morphology`, which coverage does NOT store). Negligible; physically separate; study searches never touch it. **Volume concern resolved.**

**Yield — the decisive finding:** the never-pulled verses yield **zero new IB content** in both a law book and an IB-dense book. They are animal taxonomies, ritual/physical-defect laws, concrete nouns (hearth, ostrich, lizard, testicles…). And IB-dense Proverbs was already **92% pulled**. So:
- **The term-pull missed IB *words* (inside pulled verses) — not IB *verses*.** IB content co-occurs with already-pulled terms.
- The real IB-discovery gap is the **~45 term-orphans in the existing corpus** (`perek`, `miseo`, …) — surfaced by the first audit — **not** the missing verses.

**Therefore — implications:**
1. **Whole-Bible extraction is cheap, safe, non-contaminating, and completes the verse index to the full canon** (fan-out reach + a defensible "every verse touched" anchor) — worth doing for **completeness/integrity**, kept in the segregated coverage layer.
2. **But it does NOT meaningfully narrow the IB-discovery gap** — that was the hope; the evidence says the gap is term-identity, not missing verses.
3. **"Surface more first" is largely answered:** the missing-verse route is low-yield; the ~45 already-found term-orphans are essentially the IB-orphan set (modulo the surface-keyword filter's limits + books beyond these two — a fuller run would confirm).

**Pilot data:** Lev + Pro coverage (247 verses, ~2,047 spans) sits in `verse_coverage_morphology` (segregated). Harmless; extends if the full run proceeds, droppable otherwise.

## Decisions
1. **Full whole-Bible coverage extraction** — run it (cheap, for corpus-completeness/integrity), or skip (since IB-yield ≈ 0)? *(My lean: run it once for completeness + a complete orphan audit, then leave the coverage layer segregated.)*
2. **IB-discovery proper:** proceed to the **~45 term-orphans** (the actual gap) — promote via the reg216 seed path / a coverage-gap register?