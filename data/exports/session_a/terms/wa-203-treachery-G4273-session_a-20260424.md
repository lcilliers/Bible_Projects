# Session A — Term `G4273` *prodotēs* — traitor

**Registry:** 203 treachery  
**mti_term_id:** 1365  
**Language:** Greek  
**md_version:** `v1`  ⚠ the patch's `_patch_meta.input_versions[1365]` must equal `1` at submission time or the applicator will reject it as stale (A-03 version gate).  
**Generated:** 2026-04-24 19:18  
**Current vc_status:** `not_done`  
**Existing verse_context rows:** 3 active (of 3 verses for this term).  ⚠ Per-verse: emit `insert` for verses with no active row; emit `update` for verses with an active row being revised. See v3_5 §2.1–§2.4 and §6.1. The per-verse state is shown in the Verses section below.  
**Source:** `data/bible_research.db` (deterministic render, no analytics)  
**Governing instruction:** wa-versecontext-instruction [current]  
**Produced by:** `scripts/build_session_a_prose.py --term`

---

## About this document

This document is the Session A input for **Verse Context classification** of
a single OWNER term — `G4273` *prodotēs* (traitor) from registry
203 treachery. It contains the STEP-sourced data for this one term only.
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


### G4273 · *prodotēs* · traitor

- **Language:** Greek
- **mti_term_id:** 1365
- **STEP gloss:** traitor
- **Word-analysis gloss:** traitor
- **Mounce short def:** traitor, betrayer, treacherous one
- **Occurrence count:** 3

**Parsed senses:**

- `1` traitor, betrayer, treacherous one 
a betrayer, traitor, treacherous one Lk. 6:16
- `2` Acts 7:52
- `3` 2Tim. 3:4*

**LSJ (Greek lexicon):**

- Gloss: προ-δότης, ου, 
Doric dialect -ας, ὁ, betrayer, traitor, [Refs 5th c.BC+]; π

**Related words:**

- `G4272` *prodidōmi* — to give in advance

**Root family:**

- `PRODO` (Greek) — traitor — Backfilled 2026-04-09 from wa_term_related_words clustering

**Data-quality flags (informational):**

- `NO_WORD_ANALYSIS` — meaning field is null for G4273. STEP returned no word analysis block for this term.
- `VERSE_EVIDENCE_CONCENTRATED` — Only 3 confirmed verse records for G4273. Threshold is 5.


---

## 3. Verses

The complete verse corpus for each OWNER term. This is the object of
classification. Every active verse (`delete_flagged = 0`) must be assessed
against the governing filter. Any existing `verse_context` state is shown
per verse as **Prior classification** — review, and revise only where
clearly warranted (VC Instruction §6.2 Step 2).


### G4273 · *prodotēs* — 3 active verse(s)

- **mti_term_id:** 1365
- **Language:** Greek
- **Gloss:** traitor
- **Total verses:** 3 (3 active, 0 delete_flagged)
- **Prior verse_context groups:** 1 active

**Existing verse_context groups for this term:**

| group_code | description | state |
|---|---|---|
| `1365-001` | Term characterises a person by the inner disposition and act of betrayal — treachery as a defining moral quality of the inner person | active |

**Verses:**

**vid=54770** — `Luk 6:16`
*target word in verse:* `traitor`

> Luk 6:16 and Judas the son of James , and Judas Iscariot , who became a traitor .

_Prior classification: **relevant** · related · group=`1365-001`_


**vid=54769** — `Act 7:52`
*target word in verse:* `betrayed`

> Act 7:52 Which of the prophets did your fathers not persecute ? And they killed those who announced beforehand the coming of the Righteous One , whom you have now betrayed and murdered ,

_Prior classification: **relevant** · related · group=`1365-001`_


**vid=54768** — `2Ti 3:4`
*target word in verse:* `treacherous`

> 2Ti 3:4 treacherous , reckless , swollen with conceit , lovers of pleasure rather than lovers of God ,

_Prior classification: **relevant** · **anchor** · group=`1365-001`_



---

## 4. Other terms in this registry

A pointer-only list of the other terms in this registry, so that
wrong-face set-asides can reference them accurately (VC Instruction §3.6).
**Do not classify these terms here** — each is handled in its own Session A
per-term document.


### XREF terms (OWNER elsewhere)

| Strong's | Translit. | Gloss | OWNER registry | OWNER word |
|---|---|---|---:|---|
| `G4272` | prodidōmi | to give in advance | — | to give in advance |
| `G4272` | prodidōmi | to give in advance | 180 | to give in advance |
| `H0898` | ba.gad | to act treacherously | — | to act treacherously |
| `H0898` | ba.gad | to act treacherously | 59 | faith |
| `H0899A` | be.ged | treachery | — | treachery |
| `H0899A` | be.ged | treachery | 59 | treachery |
| `H0899B` | be.ged | garment | — | garment |
| `H0899B` | be.ged | garment | 59 | garment |
| `H0900` | bo.ge.dot | treachery | — | treachery |
| `H0900` | bo.ge.dot | treachery | 59 | treachery |
| `H0901` | ba.god | treacherous | — | treacherous |
| `H0901` | ba.god | treacherous | 59 | treacherous |
| `H0906` | bad | linen | — | linen |
| `H0906` | bad | linen | 59 | linen |
| `H0908` | ba.da | to devise | — | to devise |
| `H0908` | ba.da | to devise | 59 | to devise |
| `H4820` | mir.mah | deceit | — | deceit |
| `H4820` | mir.mah | deceit | 40 | deceit |
| `H7411A` | ra.mah | to shoot | — | to shoot |
| `H7411A` | ra.mah | to shoot | 40 | to shoot |
| `H7411B` | ra.mah | to deceive | — | to deceive |
| `H7411B` | ra.mah | to deceive | 40 | to deceive |
| `H7423A` | re.miy.yah | deceit | — | deceit |
| `H7423A` | re.miy.yah | deceit | 40 | deceit |
| `H7423B` | re.miy.yah | slackness | — | slackness |
| `H7423B` | re.miy.yah | slackness | 40 | slackness |
| `H8649A` | tor.mah | treachery | — | treachery |
| `H8649A` | tor.mah | treachery | 40 | deceit |
| `H8649B` | tar.mit | deceitfulness | — | deceitfulness |
| `H8649B` | tar.mit | deceitfulness | 40 | deceitfulness |

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
`mti_term_id = 1365`. On apply, Claude Code flips
this term's `mti_terms.vc_status` to `complete` and re-derives the
owning registry's `verse_context_status` from the aggregate of all
its OWNER + XREF-via-OWNER term statuses (VC-2 in the applicator;
alignment analysis v4 §8.2).

*End of Session A prose for term G4273
(203 treachery).*
