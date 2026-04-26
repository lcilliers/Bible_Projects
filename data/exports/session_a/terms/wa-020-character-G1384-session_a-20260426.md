# Session A — Term `G1384` *dokimos* — tested

**Registry:** 020 character  
**mti_term_id:** 4842  
**Language:** Greek  
**md_version:** `v1`  ⚠ the patch's `_patch_meta.input_versions[4842]` must equal `1` at submission time or the applicator will reject it as stale (A-03 version gate).  
**Generated:** 2026-04-26 09:03  
**Current vc_status:** `not_done`  
**Existing verse_context rows:** 7 active (of 7 verses for this term).  ⚠ Per-verse: emit `insert` for verses with no active row; emit `update` for verses with an active row being revised. See v3_5 §2.1–§2.4 and §6.1. The per-verse state is shown in the Verses section below.  
**Source:** `data/bible_research.db` (deterministic render, no analytics)  
**Governing instruction:** wa-versecontext-instruction [current]  
**Produced by:** `scripts/build_session_a_prose.py --term`

---

## About this document

This document is the Session A input for **Verse Context classification** of
a single OWNER term — `G1384` *dokimos* (tested) from registry
020 character. It contains the STEP-sourced data for this one term only.
Per alignment analysis v4 §7 and §8, the term is the atomic unit of VC
classification; this document presents the term in the scope the method
actually operates on.

Read the VC instruction in full before beginning. This document is the
**data**; the instruction is the **method**. The `.md` carries no analytical
content from downstream stages (no Session B findings, no dimensional
placements, no Session C prose, no Session D synthesis).

### Prior-state posture (this term)

This term has **1 active** prior `verse_context_group`
rows (0 dissolved). Approach this as a
**RE-EVALUATION** — every prior classification will be reviewed under
the current filter and grouping model; every pre-existing active group
must be retained (with verses), dissolved, or documented-retained at
term close. No silent pass-through. See VC Instruction §6.1
(prior-state posture declaration) and §6.2 Step 6 (re-evaluation
self-check + orphan-group check).

### Method reminder

> **Governing filter (VC Instruction §3).** For each verse, ask:
> *Does this verse, through the use of this term, say something about the
> inner being — the non-physical, internal states, capacities, and
> expressions that constitute a person's invisible life: how a person
> thinks, feels, chooses, relates, and orients themselves toward meaning,
> others, and God?*
> If yes → classify the contextual meaning. If no → set aside
> (`is_relevant = 0`, with a `set_aside_reason` from the controlled
> vocabulary: `no_inner_being` / `physical_only` / `spatial_only` /
> `wrong_face` / `other`).
>
> **Grouping model (VC Instruction §6.2 Step 3 — characteristic-perspective).**
> Groups are formed from the perspective of the inner-being characteristic
> the verse cluster is primarily about — not from the perspective of what
> the term does. For property terms especially, name the characteristic
> being served (seat / channel / expression / mechanism / obstacle /
> counterpart), not just the term's function. Reuse existing groups where
> they fit; create a new group only when the inner-being characteristic is
> materially different, or the same characteristic is engaged in a
> materially different way.
>
> **Anchor designation (VC Instruction §4).** 1–2 anchor verses per group,
> each making the contextual meaning evident without surrounding context.
> Every term must have at least one active anchor (Rule R4).

---

## 2. Meaning

Per-OWNER-term lexical context, STEP-sourced and mechanically parsed. Read
this section before filtering verses — understand what the term means in
its lexical range before assessing each verse's inner-being engagement.


### G1384 · *dokimos* · tested

- **Language:** Greek
- **mti_term_id:** 4842
- **STEP gloss:** tested
- **Word-analysis gloss:** tested
- **Mounce short def:** approved by testing, genuine
- **Occurrence count:** 13

**Parsed senses:**

- `1` approved by testing, genuine 
proved, tried; approved, after examination and trial, Rom. 16:10; Jas. 1:12; by implication acceptable, Rom. 14:18

**Related words:**

- `G0096` *adokimos* — failing
- `G1381` *dokimazō* — to test
- `G1382` *dokimē* — test
- `G1383` *dokimion* — testing

**Root family:**

- `DOKIM` (Greek) — test — Backfilled 2026-04-09 from wa_term_related_words clustering

**Data-quality flags (informational):**

- `NO_WORD_ANALYSIS` — meaning field is null for G1384. STEP returned no word analysis block for this term.
- `PROSE_ONLY_MEANING` — Meaning for G1384 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
- `VERSE_EVIDENCE_CONCENTRATED` — Low occurrence count: 13. Statistical patterns unreliable with fewer than 20 occurrences.


---

## 3. Verses

The complete verse corpus for each OWNER term. This is the object of
classification. Every active verse (`delete_flagged = 0`) must be assessed
against the governing filter. Any existing `verse_context` state is shown
per verse as **Prior classification** — review, and revise only where
clearly warranted (VC Instruction §6.2 Step 2).


### G1384 · *dokimos* — 7 active verse(s)

- **mti_term_id:** 4842
- **Language:** Greek
- **Gloss:** tested
- **Total verses:** 7 (7 active, 0 delete_flagged)
- **Prior verse_context groups:** 1 active

**Existing verse_context groups for this term:**

| group_code | description | state |
|---|---|---|
| `4842-001` | Term designates the person whose inner character has been proved genuine through testing — approved by God and recognisable by the quality of inner disposition and faithful conduct | active |

**Verses:**

**vid=145515** — `Rom 14:18`
*target word in verse:* `approved`

> Rom 14:18 Whoever thus serves Christ is acceptable to God and approved by men .

_Prior classification: **relevant** · related · group=`4842-001`_


**vid=145516** — `Rom 16:10`
*target word in verse:* `approved`

> Rom 16:10 Greet Apelles , who is approved in Christ . Greet those who belong to the family of Aristobulus .

_Prior classification: **relevant** · related · group=`4842-001`_


**vid=145510** — `1Cor 11:19`
*target word in verse:* `genuine`

> 1Cor 11:19 for there must be factions among you in order that those who are genuine among you may be recognized .

_Prior classification: **relevant** · related · group=`4842-001`_


**vid=145511** — `2Cor 10:18`
*target word in verse:* `approved`

> 2Cor 10:18 For it is not the one who commends himself who is approved , but the one whom the Lord commends .

_Prior classification: **relevant** · related · group=`4842-001`_


**vid=145512** — `2Cor 13:7`
*target word in verse:* `test`

> 2Cor 13:7 But we pray to God that you may not do wrong — not that we may appear to have met the test , but that you may do what is right , though we may seem to have failed .

_Prior classification: **relevant** · related · group=`4842-001`_


**vid=145513** — `2Ti 2:15`
*target word in verse:* `approved`

> 2Ti 2:15 Do your best to present yourself to God as one approved , a worker who has no need to be ashamed , rightly handling the word of truth .

_Prior classification: **relevant** · **anchor** · group=`4842-001`_


**vid=145514** — `Jam 1:12`
*target word in verse:* `stood the test`

> Jam 1:12 Blessed is the man who remains steadfast under trial , for when he has stood the test he will receive the crown of life , which God has promised to those who love him .

_Prior classification: **relevant** · **anchor** · group=`4842-001`_



---

## 4. Other terms in this registry

A pointer-only list of the other terms in this registry, so that
wrong-face set-asides can reference them accurately (VC Instruction §3.6).
**Do not classify these terms here** — each is handled in its own Session A
per-term document.


### Other OWNER terms

| Strong's | Translit. | Gloss | Language |
|---|---|---|---|
| `G1381` | dokimazō | to test | Greek |
| `G1382` | dokimē | test | Greek |
| `G1383` | dokimion | testing | Greek |

---

## 5. Pointers

Structural pointers — what other parts of the programme this registry
connects to. Informational only; not required for classification.
No Session D synthesis content here.


### Cross-registry links

_None recorded._

### Terms borrowed as XREF from other registries

_None._

---

## 6. Questions

Open questions from the programme's observation catalogue linked to the
data-quality flags present on this registry. These are for awareness —
classification work may surface answers; many will be addressed in
Session B. Do not try to answer them here.


| obs_id | code | triggering flag | question |
|---:|---|---|---|
| 199 | `Q-COV-05` | `VERSE_EVIDENCE_CONCENTRATED` | Was STEP's verse capture exhausted for this term? Was any pagination or filter step incomplete? |
| 200 | `Q-COV-06` | `VERSE_EVIDENCE_CONCENTRATED` | What do the few verses that exist establish about the term's inner-being contribution? |
| 201 | `Q-COV-07` | `VERSE_EVIDENCE_CONCENTRATED` | Does the narrow verse set concentrate in a particular literary genre, historical period, or speaker? |

---

## Footer — what happens next

A Claude AI Verse Context session produces a `VERSECONTEXT` patch
covering this term (and any others classified in the same session).
The patch must declare `_patch_meta.terms_covered` including
`mti_term_id = 4842`. On apply, Claude Code flips
this term's `mti_terms.vc_status` to `complete` and re-derives the
owning registry's `verse_context_status` from the aggregate of all
its OWNER + XREF-via-OWNER term statuses (VC-2 in the applicator;
alignment analysis v4 §8.2).

*End of Session A prose for term G1384
(020 character).*
