# Session A — Term `G1382` *dokimē* — test

**Registry:** 020 character  
**mti_term_id:** 728  
**Language:** Greek  
**md_version:** `v1`  ⚠ the patch's `_patch_meta.input_versions[728]` must equal `1` at submission time or the applicator will reject it as stale (A-03 version gate).  
**Generated:** 2026-04-26 09:03  
**Current vc_status:** `not_done`  
**Existing verse_context rows:** 6 active (of 6 verses for this term).  ⚠ Per-verse: emit `insert` for verses with no active row; emit `update` for verses with an active row being revised. See v3_5 §2.1–§2.4 and §6.1. The per-verse state is shown in the Verses section below.  
**Source:** `data/bible_research.db` (deterministic render, no analytics)  
**Governing instruction:** wa-versecontext-instruction [current]  
**Produced by:** `scripts/build_session_a_prose.py --term`

---

## About this document

This document is the Session A input for **Verse Context classification** of
a single OWNER term — `G1382` *dokimē* (test) from registry
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


### G1382 · *dokimē* · test

- **Language:** Greek
- **mti_term_id:** 728
- **STEP gloss:** test
- **Word-analysis gloss:** test
- **Mounce short def:** character, test, proof
- **Occurrence count:** 7

**Parsed senses:**

- `1` character, test, proof 
trial, proof by trial, 2Cor. 8:2; the state or disposition of that which has been tried and approved, approved character or temper, Rom. 5:4; 2Cor. 2:9; Phil. 2:22; proof, document, evidence, 2Cor. 8:2; 13:3*

**Related words:**

- `G1381` *dokimazō* — to test
- `G1383` *dokimion* — testing
- `G1384` *dokimos* — tested

**Root family:**

- `DOKIM` (Greek) — test — Backfilled 2026-04-09 from wa_term_related_words clustering

**Data-quality flags (informational):**

- `NO_WORD_ANALYSIS` — meaning field is null for G1382. STEP returned no word analysis block for this term.
- `PROSE_ONLY_MEANING` — Meaning for G1382 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
- `VERSE_EVIDENCE_CONCENTRATED` — Low occurrence count: 7. Statistical patterns unreliable with fewer than 20 occurrences.


---

## 3. Verses

The complete verse corpus for each OWNER term. This is the object of
classification. Every active verse (`delete_flagged = 0`) must be assessed
against the governing filter. Any existing `verse_context` state is shown
per verse as **Prior classification** — review, and revise only where
clearly warranted (VC Instruction §6.2 Step 2).


### G1382 · *dokimē* — 6 active verse(s)

- **mti_term_id:** 728
- **Language:** Greek
- **Gloss:** test
- **Total verses:** 6 (6 active, 0 delete_flagged)
- **Prior verse_context groups:** 1 active

**Existing verse_context groups for this term:**

| group_code | description | state |
|---|---|---|
| `728-001` | Term names the proven character that emerges from testing — the demonstrable inner quality of the person revealed through trial, obedience, and faithful conduct | active |

**Verses:**

**vid=14427** — `Rom 5:4`
*target word in verse:* `produces character`

> Rom 5:4 and endurance produces character , and character produces hope ,

_Prior classification: **relevant** · **anchor** · group=`728-001`_


**vid=14424** — `2Cor 2:9`
*target word in verse:* `test`

> 2Cor 2:9 For this is why I wrote , that I might test you and know whether you are obedient in everything .

_Prior classification: **relevant** · related · group=`728-001`_


**vid=14425** — `2Cor 8:2`
*target word in verse:* `test`

> 2Cor 8:2 for in a severe test of affliction , their abundance of joy and their extreme poverty have overflowed in a wealth of generosity on their part.

_Prior classification: **relevant** · related · group=`728-001`_


**vid=14426** — `2Cor 9:13`
*target word in verse:* `approval`

> 2Cor 9:13 By their approval of this service , they will glorify God because of your submission that comes from your confession of the gospel of Christ , and the generosity of your contribution for them and for all others,

_Prior classification: **relevant** · related · group=`728-001`_


**vid=14423** — `2Cor 13:3`
*target word in verse:* `proof`

> 2Cor 13:3 since you seek proof that Christ is speaking in me . He is not weak in dealing with you, but is powerful among you .

_Prior classification: **relevant** · related · group=`728-001`_


**vid=145488** — `Phili 2:22`
*target word in verse:* `proven worth`

> Phili 2:22 But you know Timothy’s proven worth , how as a son with a father he has served with me in the gospel .

_Prior classification: **relevant** · **anchor** · group=`728-001`_



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
| `G1383` | dokimion | testing | Greek |
| `G1384` | dokimos | tested | Greek |

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
`mti_term_id = 728`. On apply, Claude Code flips
this term's `mti_terms.vc_status` to `complete` and re-derives the
owning registry's `verse_context_status` from the aggregate of all
its OWNER + XREF-via-OWNER term statuses (VC-2 in the applicator;
alignment analysis v4 §8.2).

*End of Session A prose for term G1382
(020 character).*
