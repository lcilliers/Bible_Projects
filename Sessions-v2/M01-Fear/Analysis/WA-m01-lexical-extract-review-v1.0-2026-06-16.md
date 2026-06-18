# M01 Lexical Extract — First Review

**File:** WA-m01-lexical-extract-review-v1.0-2026-06-16.md
**Date:** 2026-06-16
**Prefix:** WA
**Document type:** Internal analysis (reusable; markdown)
**Source data reviewed:**
- `wa-ve-lexical-extract-M01-20260616-b1of3.json` (batch 1 of 3)
- `wa-ve-lexical-extract-M01-20260616.json` (full M01)

**Previous outputs:** None — this is the first written output of the new terms of reference. Supersedes nothing.

**Change control:** v1.0 — initial version. Captures the chat observations on batch 1 plus the additional scrutiny of the full M01 file.

> Note on terms of reference: the previous analytical constructs are set aside. This document reads the lexical layer for what it says about the inner being and flags issues; it does not re-impose the prior cluster/dimension framework. Where the legacy taxonomy still appears *inside the data* (M-codes, T-codes), that is noted as a finding, not adopted as a framework.

---

## 1. What these files are

Two JSON files, same schema (`ve_lexical v2_engine_iter1 + verse_morphology measure layer, schema 3.34.0`). Each is a lexical analysis whose stated primary goal is to show what each verse says about the characteristics of the inner being, recorded **per term-in-verse**.

| | Batch 1 (`-b1of3`) | Full M01 |
|---|---|---|
| Cluster | M01 — "Fear, Dread and Terror" | M01 — "Fear, Dread and Terror" |
| Verses | 350 | 922 |
| Occurrences | 391 | 1,036 |
| Testament | OT only | OT 763 / NT 159 |
| Language | Hebrew only | Hebrew 845 / Aramaic 18 / Greek 173 |
| Distinct Strong's | — | 85 |

The `field_note` is load-bearing: lexical fields are **mechanically derived** ("01b v2"), and `UNRESOLVED` means *expected-but-undetermined* — the engine looked for a value and could not settle one. This is a first machine pass, not validated reading.

**Batch relationship (verified):** all 350 batch-1 verses are present in the full file. Batch 1 is a clean OT/Hebrew-only subset — the batching appears to cut by testament/language with the Hebrew OT head first, though the exact cut rule is not stated in the file and is *not confirmed*.

---

## 2. Structure / schema

Top level: `{ meta, data }`. Each `data` record is a **verse** (reference, OSIS id, testament, full verse text) holding one or more `term_occurrences`. In the full file, 96 of 922 verses carry more than one occurrence.

Each occurrence has three parts:
- `term` — strong, translit, gloss, language
- `verse_report` — target_word (the translated word), morph, stem
- `lexical` — the inner-being analysis block

Lexical fields and their coverage across the full 1,036 occurrences:

| Field | Coverage | Notes |
|---|---:|---|
| sense | 100% | the contextual sense in this verse |
| lemma_meaning | 100% | lexicon gloss range |
| type | 100% | action / status / quality |
| faculty | 100% | almost always "affect" |
| compound | 80.4% | co-occurring terms with roles |
| how | 72.8% | the triggering/attendant action |
| experiencer | 66.3% | self / other / other (addressed) |
| divine_involvement | 31.9% | present / agent-subject |
| object | 28.9% | what the fear is directed at |
| object_type | 26.1% | thing-abstract / person / God |
| immediate_response | 17.7% | |
| relational | 16.9% | |
| cause | 14.8% | but almost never *resolved* — see §6 |
| intensity | 12.8% | |
| location | 10.8% | somatic seat |
| origin | 1.5% | |

---

## 3. Observation (what the data plainly contains)

- Everything in batch 1 is OT/Hebrew; the full file adds NT/Greek and a small Aramaic set.
- `type` splits three ways across the full corpus: action 650, status 302, quality 81, plus 3 UNRESOLVED — fear as an event, a state, or a settled trait.
- `faculty` is "affect" on 982 of 1,036; the remaining 54 carry blends (affect+perception 28, affect+cognition 13, affect+memory 8, affect+volition 4, one triple).
- `experiencer`: other 396, other (addressed) 184, self 107, absent 349.
- `divine_involvement`: present on 331; God as agent/subject on 44.
- `location` (somatic seat): heart 70, soul 26, flesh 11, UNRESOLVED 21.
- The four core fields are populated on 100% of occurrences; verse text is present in full for every record.

**Integrity positives:** 0 duplicate verse references; batch 1 fully contained in full; core fields complete.

---

## 4. Interpretation (held lightly — this is a mechanical layer)

The schema reads as a set of slots that let each verse speak about the inner being through a consistent grammar: **who** holds the state (experiencer), **what kind** of inner motion it is (type, faculty), **toward what** (object, object_type), **how triggered** (how, cause), **how strong** (intensity), **where seated** (location), and **how God stands to it** (divine_involvement). That maps cleanly onto the inner-being question and is a workable backbone.

But two patterns warn against treating the contents as findings yet:
- `lemma_meaning` defaults to `frightening(DANGER)` on a large share of records — an engine fallback, not a per-verse reading.
- `cause` is almost never resolved (§6).

So the layer currently supports describing the **shape and vocabulary** of fear far better than it supports any **causal or relational claim** about it.

---

## 5. Reflection (consequences and affected perspectives)

- **Reverence and dread sit in one cluster.** A keyword scan finds ~48 reverence-leaning senses (awe, awesome, revere, reverent) alongside terror, dread, panic, horror. The reverence-vs-dread line is exactly where reading communities differ most, and the data does not currently draw it. `lemma_meaning` sometimes lumps "fearing, reverent, afraid" into one string, which can collapse the distinction silently.
- **Most fear here is not first-person.** "Self" is the minority experiencer (107); the bulk is fear reported of others, or commanded/addressed to others — likely the "fear not" imperative form. This shapes any claim about fear as *felt* inner experience.
- **The legacy taxonomy is still embedded** in `compound` tags and `meta.cluster`. The data carries the old scaffolding; the new terms of reference do not. A deliberate decision is needed before those tags quietly steer new analysis.

I would resist the tempting early conclusion that "OT fear is mostly affect directed at danger" — that reading is partly an artifact of engine defaults (`faculty=affect`, `lemma=frightening(DANGER)`), not yet a grounded finding.

---

## 6. Additional observations from deeper scrutiny

**6.1 `cause` is a near-total blind spot.** Resolved on only **12 of 1,036** occurrences (1.2%); UNRESOLVED on 141; absent on 883. Whenever the engine flags cause as expected, it almost never determines it. If "what arouses fear" is part of the inner-being question, this is the single largest gap and needs dedicated, verse-by-verse discovery — the mechanical layer will not supply it.

**6.2 Cluster-membership purity question — `anankē` (G0318, "necessity").** Nine occurrences, senses split between fear-adjacent (distress, affliction, hardships — 5) and constraint/obligation (necessity, compulsion, under compulsion — 4). The "necessity/compulsion" uses are not fear/dread/terror; the term appears to have been pulled into the cluster on a minority sense. `ademoneo` (G0085, "be distressed") and `kera` (H3735) are milder cases of the same pattern. This is a concrete candidate for boundary review.

**6.3 `faculty` barely discriminates — except where it blends.** "Affect" on 95% of records is near-tautological for a fear cluster. The analytically interesting signal is the ~5% of blended cases where fear couples with perception, cognition, memory, or volition. The constant value is low-information; the blends are where to look.

**6.4 `type` shape is stable but leans differently across testaments.** OT: action 556 / status 242 / quality 64. NT: action 94 / status 60 / quality 17. The NT carries proportionally more "status" (state) and less "action" — a possible OT-event vs NT-state lean. Hold lightly: NT n is small and the layer is mechanical.

**6.5 `divine_involvement` is proportionally an OT feature.** Present on 331 overall; God as agent/subject on 44 (OT 38, NT 6). The interface between the fearing inner being and God is more frequently marked in the OT data.

**6.6 `location` — the heart dominates as the seat of fear.** Of 112 populated, heart 70, soul 26, flesh 11. Directly relevant to the spirit-soul-body question, but only ~11% coverage — usable as illustration, not yet as a pattern.

**6.7 Enrichment density is uneven.** Per occurrence, populated optional fields: 0 fields → 12 occ; 1 → 80; 2 → 192; 3 → 251; 4 → 180; 5 → 151; 6 → 105; 7 → 51; 8 → 14. Most records carry 2–5 optional fields; a handful are bare or very rich.

**6.8 Fear is densely networked with other inner-being states.** `compound` partner tags (legacy codes) span a wide field: T2 (qualifiers) 489, M01 (self) 232, then M23 73, M47 66, M25 61, M15 57, M41 52, M05 51, M33 49, M26 48, M44, M22, M04 (joy) 32, M24, M30, M10 (sin) 30, M03 (grief) 29, M08 (pride) 29, and more. Fear co-occurs across grief, joy, love, pride, sin, wisdom, and righteousness — it does not sit in isolation.

**6.9 Cross-pipeline inconsistency — book abbreviations.** This extract uses STEP-style codes (`Phili`, `Phile`, `1Jo`, `Jude`) that **differ from the Session A v8 import spec** (Php, Phm, 1Jn, Jud). It also carries OSIS ids (`Gen.3.10`). If references from this lexical layer are ever matched against import-spec book codes, they will not join. Flag for reconciliation. (This is a different pipeline stage — schema 3.34.0 — so the divergence is unsurprising but consequential.)

---

## 7. Where the data is insufficient or a perspective is missing

- `cause` is effectively absent — the largest substantive gap (§6.1).
- `location` (the spirit-soul-body seat) is thin (~11%) — illustrative only.
- The fields are unvalidated mechanical output; nothing here has been checked against the verse by a reader.
- The batching rule is not stated in the file (inferred, not confirmed).
- Reverence vs dread is undrawn within the cluster, despite the data likely being able to hold the distinction.

---

## 8. Open interpretive choices (for the researcher)

1. **Unit of analysis** — the verse (922) or the term-occurrence-in-verse (1,036)?
2. **Residual M-/T-codes in `compound`** — honour, strip, or hold aside?
3. **`UNRESOLVED`** — treat as a gap to flag for discovery, or as a meaningful "undetermined" category?
4. **Task with this layer** — validate/correct the mechanical pass against the verses, or read it as-is?
5. **`anankē` and similar minority-sense members** — review cluster boundaries now, or after the read?

---

*End of v1.0.*
