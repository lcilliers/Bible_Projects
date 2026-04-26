# Session A — Term `G1258` *dialektos* — language

**Registry:** 127 reasoning  
**mti_term_id:** 6065  
**Language:** Greek  
**md_version:** `v1`  ⚠ the patch's `_patch_meta.input_versions[6065]` must equal `1` at submission time or the applicator will reject it as stale (A-03 version gate).  
**Generated:** 2026-04-25 16:06  
**Current vc_status:** `not_done`  
**Existing verse_context rows:** 5 active (of 6 verses for this term).  ⚠ Per-verse: emit `insert` for verses with no active row; emit `update` for verses with an active row being revised. See v3_5 §2.1–§2.4 and §6.1. The per-verse state is shown in the Verses section below.  
**Source:** `data/bible_research.db` (deterministic render, no analytics)  
**Governing instruction:** wa-versecontext-instruction [current]  
**Produced by:** `scripts/build_session_a_prose.py --term`

---

## About this document

This document is the Session A input for **Verse Context classification** of
a single OWNER term — `G1258` *dialektos* (language) from registry
127 reasoning. It contains the STEP-sourced data for this one term only.
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


### G1258 · *dialektos* · language

- **Language:** Greek
- **mti_term_id:** 6065
- **STEP gloss:** language
- **Word-analysis gloss:** language
- **Mounce short def:** language, dialect, a communication code whether written or oral; in the NT this always refers to known languages commonly spoken in the ancient world
- **Occurrence count:** 7

**Parsed senses:**

- `1` language, dialect, a communication code whether written or oral; in the NT this always refers to known languages commonly spoken in the ancient world 
speech; manner of speaking; peculiar language, of a nation, dialect, vernacular idiom, Acts 1:19; 2:6, 8; 21:40; 22:2; 26:14

**Related words:**

- `G1256` *dialegō* — to dispute

**Root family:**

- `LEGŌ` (Greek) — rebuke — Backfilled 2026-04-09 from wa_term_related_words clustering

**Data-quality flags (informational):**

- `NO_WORD_ANALYSIS` — meaning field is null for G1258. STEP returned no word analysis block for this term.
- `PROSE_ONLY_MEANING` — Meaning for G1258 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
- `VERSE_EVIDENCE_CONCENTRATED` — Low occurrence count: 7. Statistical patterns unreliable with fewer than 20 occurrences.


---

## 3. Verses

The complete verse corpus for each OWNER term. This is the object of
classification. Every active verse (`delete_flagged = 0`) must be assessed
against the governing filter. Any existing `verse_context` state is shown
per verse as **Prior classification** — review, and revise only where
clearly warranted (VC Instruction §6.2 Step 2).


### G1258 · *dialektos* — 6 active verse(s)

- **mti_term_id:** 6065
- **Language:** Greek
- **Gloss:** language
- **Total verses:** 6 (6 active, 0 delete_flagged)
- **Prior verse_context groups:** 1 active

**Existing verse_context groups for this term:**

| group_code | description | state |
|---|---|---|
| `6065-001` | Term names the native language as the vehicle through which inner understanding, recognition, and response are engaged — hearing in one's own language facilitates inner comprehension and attention | active |

**Verses:**

**vid=187509** — `Act 1:19`
*target word in verse:* `language`

> Act 1:19 And it became known to all the inhabitants of Jerusalem , so that the field was called in their own language Akeldama , that is , Field of Blood .)


**vid=187510** — `Act 2:6`
*target word in verse:* `language`

> Act 2:6 And at this sound the multitude came together , and they were bewildered , because each one was hearing them speak in his own language .

_Prior classification: **relevant** · **anchor** · group=`6065-001`_


**vid=187511** — `Act 2:8`
*target word in verse:* `language`

> Act 2:8 And how is it that we hear , each of us in his own native language ?

_Prior classification: **relevant** · related · group=`6065-001`_


**vid=187512** — `Act 21:40`
*target word in verse:* `language`

> Act 21:40 And when he had given him permission , Paul , standing on the steps , motioned with his hand to the people . And when there was a great hush , he addressed them in the Hebrew language , saying :

_Prior classification: **relevant** · related · group=`6065-001`_


**vid=187513** — `Act 22:2`
*target word in verse:* `language`

> Act 22:2 And when they heard that he was addressing them in the Hebrew language , they became even more quiet . And he said :

_Prior classification: **relevant** · related · group=`6065-001`_


**vid=187514** — `Act 26:14`
*target word in verse:* `language`

> Act 26:14 And when we had all fallen to the ground , I heard a voice saying to me in the Hebrew language , ‘ Saul , Saul , why are you persecuting me ? It is hard for you to kick against the goads .’

_Prior classification: **relevant** · related · group=`6065-001`_



---

## 4. Other terms in this registry

A pointer-only list of the other terms in this registry, so that
wrong-face set-asides can reference them accurately (VC Instruction §3.6).
**Do not classify these terms here** — each is handled in its own Session A
per-term document.


### Other OWNER terms

| Strong's | Translit. | Gloss | Language |
|---|---|---|---|
| `G0483` | antilegō | to dispute | Greek |
| `G0483` | antilegō | to dispute | Greek |
| `G0557` | apelegmos | discredit | Greek |
| `G0557` | apelegmos | discredit | Greek |
| `G1246` | diakatelenchomai | to refute | Greek |
| `G1246` | diakatelenchomai | to refute | Greek |
| `G1256` | dialegō | to dispute | Greek |
| `G1256` | dialegō | to dispute | Greek |
| `G1261` | dialogismos | reasoning | Greek |
| `G1261` | dialogismos | reasoning | Greek |
| `G1261` | dialogismos | reasoning | Greek |
| `G1649` | elegxis | rebuke | Greek |
| `G1649` | elegxis | rebuke | Greek |
| `G1650` | elenchos | rebuke | Greek |
| `G1650` | elenchos | rebuke | Greek |
| `G1651` | elenchō | to rebuke | Greek |
| `G1651` | elenchō | to rebuke | Greek |
| `G1827` | exelenchō | to convict | Greek |
| `G1827` | exelenchō | to convict | Greek |
| `G1951` | epilegō | to call/choose | Greek |
| `G1951` | epilegō | to call/choose | Greek |
| `G2639` | katalegō | to enrol | Greek |
| `G2639` | katalegō | to enrol | Greek |
| `G3004H` | legō | to say: name | Greek |
| `G3004H` | legō | to say: name | Greek |
| `G4302` | prolegō | to foretell | Greek |
| `G4302` | prolegō | to foretell | Greek |

### XREF terms (OWNER elsewhere)

| Strong's | Translit. | Gloss | OWNER registry | OWNER word |
|---|---|---|---:|---|
| `G1260` | dialogizomai | to discuss | — | to discuss |
| `G1260` | dialogizomai | to discuss | 112 | to discuss |
| `G1260` | dialogizomai | to discuss | 160 | thought |

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
`mti_term_id = 6065`. On apply, Claude Code flips
this term's `mti_terms.vc_status` to `complete` and re-derives the
owning registry's `verse_context_status` from the aggregate of all
its OWNER + XREF-via-OWNER term statuses (VC-2 in the applicator;
alignment analysis v4 §8.2).

*End of Session A prose for term G1258
(127 reasoning).*
