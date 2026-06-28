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
