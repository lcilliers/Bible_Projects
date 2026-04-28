# Session A — Term `G0861` *aftharsia* — incorruptibility

**Registry:** 092 integrity  
**mti_term_id:** 935  
**Language:** Greek  
**md_version:** `v1`  ⚠ the patch's `_patch_meta.input_versions[935]` must equal `1` at submission time or the applicator will reject it as stale (A-03 version gate).  
**Generated:** 2026-04-25 16:06  
**Current vc_status:** `not_done`  
**Existing verse_context rows:** 6 active (of 6 verses for this term).  ⚠ Per-verse: emit `insert` for verses with no active row; emit `update` for verses with an active row being revised. See v3_5 §2.1–§2.4 and §6.1. The per-verse state is shown in the Verses section below.  
**Source:** `data/bible_research.db` (deterministic render, no analytics)  
**Governing instruction:** wa-versecontext-instruction [current]  
**Produced by:** `scripts/build_session_a_prose.py --term`

---

## About this document

This document is the Session A input for **Verse Context classification** of
a single OWNER term — `G0861` *aftharsia* (incorruptibility) from registry
092 integrity. It contains the STEP-sourced data for this one term only.
Per alignment analysis v4 §7 and §8, the term is the atomic unit of VC
classification; this document presents the term in the scope the method
actually operates on.

Read the VC instruction in full before beginning. This document is the
**data**; the instruction is the **method**. The `.md` carries no analytical
content from downstream stages (no Session B findings, no dimensional
placements, no Session C prose, no Session D synthesis).

### Prior-state posture (this term)

This term has **2 active** prior `verse_context_group`
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


### G0861 · *aftharsia* · incorruptibility

- **Language:** Greek
- **mti_term_id:** 935
- **STEP gloss:** incorruptibility
- **Word-analysis gloss:** incorruptibility
- **Mounce short def:** imperishableness, immortality
- **Occurrence count:** 8

**Parsed senses:**

- `1` imperishableness, immortality 
incorruptibility, imperishableness 1Cor. 15:42, 53, 54; immortality, Rom. 2:7; 2Tim. 1:10; soundness, purity; ἐν ἀφθαρσιᾳ, purely, sincerely or constantly, unfailingly, Eph. 6:24

**Related words:**

- `G0862` *afthartos* — incorruptible
- `G5349` *fthartos* — perishable

**Root family:**

- `AFTHARS` (Greek) — incorruptibility — Backfilled 2026-04-09 from wa_term_related_words clustering

**Data-quality flags (informational):**

- `NO_WORD_ANALYSIS` — meaning field is null for G0861. STEP returned no word analysis block for this term.
- `PROSE_ONLY_MEANING` — Meaning for G0861 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
- `VERSE_EVIDENCE_CONCENTRATED` — Low occurrence count: 8. Statistical patterns unreliable with fewer than 20 occurrences.


---

## 3. Verses

The complete verse corpus for each OWNER term. This is the object of
classification. Every active verse (`delete_flagged = 0`) must be assessed
against the governing filter. Any existing `verse_context` state is shown
per verse as **Prior classification** — review, and revise only where
clearly warranted (VC Instruction §6.2 Step 2).


### G0861 · *aftharsia* — 6 active verse(s)

- **mti_term_id:** 935
- **Language:** Greek
- **Gloss:** incorruptibility
- **Total verses:** 6 (6 active, 0 delete_flagged)
- **Prior verse_context groups:** 2 active

**Existing verse_context groups for this term:**

| group_code | description | state |
|---|---|---|
| `935-001` | Term names the eschatological transformation of the person — the putting on of incorruptibility and immortality at resurrection | active |
| `935-002` | Term names incorruptibility as the quality of inner love and the inner orientation of those who seek God's glory | active |

**Verses:**

**vid=28148** — `Rom 2:7`
*target word in verse:* `immortality`

> Rom 2:7 to those who by patience in well-doing seek for glory and honor and immortality , he will give eternal life ;

_Prior classification: **relevant** · **anchor** · group=`935-002`_


**vid=28143** — `1Cor 15:42`
*target word in verse:* `imperishable`

> 1Cor 15:42 So is it with the resurrection of the dead . What is sown is perishable ; what is raised is imperishable .

_Prior classification: **relevant** · **anchor** · group=`935-001`_


**vid=28144** — `1Cor 15:50`
*target word in verse:* `imperishable`

> 1Cor 15:50 I tell you this , brothers : flesh and blood cannot inherit the kingdom of God , nor does the perishable inherit the imperishable .

_Prior classification: **relevant** · related · group=`935-001`_


**vid=28145** — `1Cor 15:53`
*target word in verse:* `imperishable`

> 1Cor 15:53 For this perishable body must put on the imperishable , and this mortal body must put on immortality .

_Prior classification: **relevant** · **anchor** · group=`935-001`_


**vid=28146** — `1Cor 15:54`
*target word in verse:* `imperishable`

> 1Cor 15:54 When the perishable puts on the imperishable , and the mortal puts on immortality , then shall come to pass the saying that is written : “ Death is swallowed up in victory .”

_Prior classification: **relevant** · related · group=`935-001`_


**vid=28147** — `Eph 6:24`
*target word in verse:* `incorruptible`

> Eph 6:24 Grace be with all who love our Lord Jesus Christ with love incorruptible .

_Prior classification: **relevant** · **anchor** · group=`935-002`_



---

## 4. Other terms in this registry

A pointer-only list of the other terms in this registry, so that
wrong-face set-asides can reference them accurately (VC Instruction §3.6).
**Do not classify these terms here** — each is handled in its own Session A
per-term document.


### Other OWNER terms

| Strong's | Translit. | Gloss | Language |
|---|---|---|---|
| `H8538` | tum.mah | integrity | Hebrew |
| `H8538` | tum.mah | integrity | Hebrew |
| `H8538` | tum.mah | integrity | Hebrew |
| `H8549G` | ta.mim | unblemished | Hebrew |
| `H8549G` | ta.mim | unblemished | Hebrew |
| `H8549G` | ta.mim | unblemished | Hebrew |

### XREF terms (OWNER elsewhere)

| Strong's | Translit. | Gloss | OWNER registry | OWNER word |
|---|---|---|---:|---|
| `H0518H` | im | if: surely no | — | if: surely no |
| `H0518H` | im | if: surely no | — | if: surely no |
| `H0518H` | im | if: surely no | — | if: surely no |
| `H0518H` | im | if: surely no | — | if: surely no |
| `H0518H` | im | if: surely no | 28 | if: surely no |
| `H0518I` | im | if: surely yes | — | if: surely yes |
| `H0518I` | im | if: surely yes | — | if: surely yes |
| `H0518I` | im | if: surely yes | — | if: surely yes |
| `H0518I` | im | if: surely yes | — | if: surely yes |
| `H0518I` | im | if: surely yes | 28 | if: surely yes |
| `H0518J` | im | if: until | — | if: until |
| `H0518J` | im | if: until | — | if: until |
| `H0518J` | im | if: until | — | if: until |
| `H0518J` | im | if: until | — | if: until |
| `H0518J` | im | if: until | 28 | if: until |
| `H1932` | hu | he/she/it | — | he/she/it |
| `H1932` | hu | he/she/it | — | he/she/it |
| `H1932` | hu | he/she/it | 86 | he/she/it |
| `H2007` | hen.nah | they [fem.] | — | they [fem.] |
| `H2007` | hen.nah | they [fem.] | — | they [fem.] |
| `H2007` | hen.nah | they [fem.] | 86 | they [fem.] |
| `H3588B` | ki m | that if: except | — | that if: except |
| `H3588B` | ki m | that if: except | — | that if: except |
| `H3588B` | ki m | that if: except | — | that if: except |
| `H3588B` | ki m | that if: except | — | that if: except |
| `H3588B` | ki m | that if: except | — | that if: except |
| `H3588B` | ki m | that if: except | — | that if: except |
| `H3588B` | ki m | that if: except | — | that if: except |
| `H3588B` | ki m | that if: except | 28 | that if: except |
| `H3588C` | ki al ken | for as that: since | — | for as that: since |
| `H3588C` | ki al ken | for as that: since | — | for as that: since |
| `H3588C` | ki al ken | for as that: since | — | for as that: since |
| `H3588C` | ki al ken | for as that: since | — | for as that: since |
| `H3588C` | ki al ken | for as that: since | — | for as that: since |
| `H3588C` | ki al ken | for as that: since | — | for as that: since |
| `H3588C` | ki al ken | for as that: since | — | for as that: since |
| `H3588C` | ki al ken | for as that: since | 28 | for as that: since |
| `H3589` | kid | ruin | — | ruin |
| `H3589` | kid | ruin | — | ruin |
| `H3589` | kid | ruin | — | ruin |
| `H3589` | kid | ruin | — | ruin |
| `H3589` | kid | ruin | 28 | ruin |
| `H3651A` | ken | right | — | right |
| `H3651A` | ken | right | — | right |
| `H3651A` | ken | right | — | right |
| `H3651A` | ken | right | — | right |
| `H3651A` | ken | right | — | right |
| `H3651A` | ken | right | 121 | praise |
| `H3651A` | ken | right | — | right |
| `H3651A` | ken | right | — | right |
| `H3651A` | ken | right | — | right |
| `H4974` | me.tom | soundness | — | soundness |
| `H4974` | me.tom | soundness | — | soundness |
| `H4974` | me.tom | soundness | 90 | soundness |
| `H8535` | tam | complete | — | complete |
| `H8535` | tam | complete | — | complete |
| `H8535` | tam | complete | 90 | complete |
| `H8537` | tom | integrity | — | integrity |
| `H8537` | tom | integrity | — | integrity |
| `H8537` | tom | integrity | 90 | innocence |
| `H8549H` | ta.mim | unblemished: blameless | — | unblemished: blameless |
| `H8549H` | ta.mim | unblemished: blameless | — | unblemished: blameless |
| `H8549H` | ta.mim | unblemished: blameless | 90 | unblemished: blameless |
| `H8549I` | ta.mim | unblemished: complete | — | unblemished: complete |
| `H8549I` | ta.mim | unblemished: complete | — | unblemished: complete |
| `H8549I` | ta.mim | unblemished: complete | 90 | unblemished: complete |
| `H8549J` | ta.mim | unblemished: Thummim | — | unblemished: Thummim |
| `H8549J` | ta.mim | unblemished: Thummim | — | unblemished: Thummim |
| `H8549J` | ta.mim | unblemished: Thummim | 90 | unblemished: Thummim |
| `H8552` | ta.mam | to finish | — | to finish |
| `H8552` | ta.mam | to finish | — | to finish |
| `H8552` | ta.mam | to finish | — | to finish |
| `H8552` | ta.mam | to finish | 147 | sin |

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
`mti_term_id = 935`. On apply, Claude Code flips
this term's `mti_terms.vc_status` to `complete` and re-derives the
owning registry's `verse_context_status` from the aggregate of all
its OWNER + XREF-via-OWNER term statuses (VC-2 in the applicator;
alignment analysis v4 §8.2).

*End of Session A prose for term G0861
(092 integrity).*
