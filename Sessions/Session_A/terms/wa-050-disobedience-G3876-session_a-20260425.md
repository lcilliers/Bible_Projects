# Session A — Term `G3876` *parakoē* — disobedience

**Registry:** 050 disobedience  
**mti_term_id:** 820  
**Language:** Greek  
**md_version:** `v1`  ⚠ the patch's `_patch_meta.input_versions[820]` must equal `1` at submission time or the applicator will reject it as stale (A-03 version gate).  
**Generated:** 2026-04-25 14:20  
**Current vc_status:** `not_done`  
**Existing verse_context rows:** 3 active (of 3 verses for this term).  ⚠ Per-verse: emit `insert` for verses with no active row; emit `update` for verses with an active row being revised. See v3_5 §2.1–§2.4 and §6.1. The per-verse state is shown in the Verses section below.  
**Source:** `data/bible_research.db` (deterministic render, no analytics)  
**Governing instruction:** wa-versecontext-instruction [current]  
**Produced by:** `scripts/build_session_a_prose.py --term`

---

## About this document

This document is the Session A input for **Verse Context classification** of
a single OWNER term — `G3876` *parakoē* (disobedience) from registry
050 disobedience. It contains the STEP-sourced data for this one term only.
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


### G3876 · *parakoē* · disobedience

- **Language:** Greek
- **mti_term_id:** 820
- **STEP gloss:** disobedience
- **Word-analysis gloss:** disobedience
- **Mounce short def:** disobedience, unwillingness to hear
- **Occurrence count:** 3

**Parsed senses:**

- `1` disobedience, unwillingness to hear 
an erroneous, or imperfect hearing; disobedience, Rom. 5:19; a deviation from obedience, unwillingness to hear 2Cor. 10:6; Heb. 2:2*

**Related words:**

- `G3878` *parakouō* — to ignore

**Root family:**

- `PARAKO` (Greek) — to ignore — Backfilled 2026-04-09 from wa_term_related_words clustering

**Data-quality flags (informational):**

- `PROSE_ONLY_MEANING` — Meaning for G3876 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
- `VERSE_EVIDENCE_CONCENTRATED` — Only 3 confirmed verse records for G3876. Threshold is 5.


---

## 3. Verses

The complete verse corpus for each OWNER term. This is the object of
classification. Every active verse (`delete_flagged = 0`) must be assessed
against the governing filter. Any existing `verse_context` state is shown
per verse as **Prior classification** — review, and revise only where
clearly warranted (VC Instruction §6.2 Step 2).


### G3876 · *parakoē* — 3 active verse(s)

- **mti_term_id:** 820
- **Language:** Greek
- **Gloss:** disobedience
- **Total verses:** 3 (3 active, 0 delete_flagged)
- **Prior verse_context groups:** 1 active

**Existing verse_context groups for this term:**

| group_code | description | state |
|---|---|---|
| `820-001` | Term names disobedience as the defining inner act with moral and covenantal consequence — the primal refusal that constituted the human condition; the act or disposition of disobedience that draws retribution and demands correction | active |

**Verses:**

**vid=19567** — `Rom 5:19`
*target word in verse:* `disobedience`

> Rom 5:19 For as by the one man’s disobedience the many were made sinners , so by the one man’s obedience the many will be made righteous .

_Prior classification: **relevant** · **anchor** · group=`820-001`_


**vid=19565** — `2Cor 10:6`
*target word in verse:* `disobedience`

> 2Cor 10:6 being ready to punish every disobedience , when your obedience is complete .

_Prior classification: **relevant** · related · group=`820-001`_


**vid=19566** — `Heb 2:2`
*target word in verse:* `disobedience`

> Heb 2:2 For since the message declared by angels proved to be reliable , and every transgression or disobedience received a just retribution ,

_Prior classification: **relevant** · related · group=`820-001`_



---

## 4. Other terms in this registry

A pointer-only list of the other terms in this registry, so that
wrong-face set-asides can reference them accurately (VC Instruction §3.6).
**Do not classify these terms here** — each is handled in its own Session A
per-term document.


### Other OWNER terms

| Strong's | Translit. | Gloss | Language |
|---|---|---|---|
| `G0543` | apeitheia | disobedience | Greek |
| `G0545` | apeithēs | disobedient | Greek |
| `G0545` | apeithēs | disobedient | Greek |
| `G0545` | apeithēs | disobedient | Greek |
| `G3878` | parakouō | to ignore | Greek |

### XREF terms (OWNER elsewhere)

| Strong's | Translit. | Gloss | OWNER registry | OWNER word |
|---|---|---|---:|---|
| `G3982` | peithō | to persuade | — | to persuade |
| `G3982` | peithō | to persuade | — | to persuade |
| `G3982` | peithō | to persuade | 163 | trust |

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
`mti_term_id = 820`. On apply, Claude Code flips
this term's `mti_terms.vc_status` to `complete` and re-derives the
owning registry's `verse_context_status` from the aggregate of all
its OWNER + XREF-via-OWNER term statuses (VC-2 in the applicator;
alignment analysis v4 §8.2).

*End of Session A prose for term G3876
(050 disobedience).*
