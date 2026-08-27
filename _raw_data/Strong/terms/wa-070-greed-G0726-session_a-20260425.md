# Session A — Term `G0726` *harpazō* — to seize

**Registry:** 070 greed  
**mti_term_id:** 5493  
**Language:** Greek  
**md_version:** `v1`  ⚠ the patch's `_patch_meta.input_versions[5493]` must equal `1` at submission time or the applicator will reject it as stale (A-03 version gate).  
**Generated:** 2026-04-25 05:13  
**Current vc_status:** `not_done`  
**Existing verse_context rows:** 10 active (of 13 verses for this term).  ⚠ Per-verse: emit `insert` for verses with no active row; emit `update` for verses with an active row being revised. See v3_5 §2.1–§2.4 and §6.1. The per-verse state is shown in the Verses section below.  
**Source:** `data/bible_research.db` (deterministic render, no analytics)  
**Governing instruction:** wa-versecontext-instruction [current]  
**Produced by:** `scripts/build_session_a_prose.py --term`

---

## About this document

This document is the Session A input for **Verse Context classification** of
a single OWNER term — `G0726` *harpazō* (to seize) from registry
070 greed. It contains the STEP-sourced data for this one term only.
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


### G0726 · *harpazō* · to seize

- **Language:** Greek
- **mti_term_id:** 5493
- **STEP gloss:** to seize
- **Word-analysis gloss:** to seize
- **Mounce short def:** to catch, steal, carry off
- **Occurrence count:** 45

**Parsed senses:**

- `1` to catch, steal, carry off 
to seize, catch as a wild beast, Jn. 10:12; take away by force, snatch away, carry off Mt. 13:19; Jn. 10:28, 29; Acts 23:10; Jude 23; metaphorically to seize on with avidity, eagerly, appropriate, Mt. 11:12; to convey away suddenly, transport hastily, Jn. 6:15

**Related words:**

- `G0138` *haireō* — to choose
- `G0727` *harpax* — rapacious
- `G1283` *diarpazō* — to rob

**Root family:**

- `HARPAG` (Greek) — plunder — Backfilled 2026-04-09 from wa_term_related_words clustering

**Data-quality flags (informational):**

- `NO_WORD_ANALYSIS` — meaning field is null for G0726. STEP returned no word analysis block for this term.
- `PROSE_ONLY_MEANING` — Meaning for G0726 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.


---

## 3. Verses

The complete verse corpus for each OWNER term. This is the object of
classification. Every active verse (`delete_flagged = 0`) must be assessed
against the governing filter. Any existing `verse_context` state is shown
per verse as **Prior classification** — review, and revise only where
clearly warranted (VC Instruction §6.2 Step 2).


### G0726 · *harpazō* — 13 active verse(s)

- **mti_term_id:** 5493
- **Language:** Greek
- **Gloss:** to seize
- **Total verses:** 13 (13 active, 0 delete_flagged)
- **Prior verse_context groups:** 2 active

**Existing verse_context groups for this term:**

| group_code | description | state |
|---|---|---|
| `5493-001` | Term names the snatching that threatens or violates the inner being — the evil one taking the word from the heart, the wolf scattering the sheep, and the divine security that makes such snatching impossible | active |
| `5493-002` | Term names the divine catching away of the person — eschatological rapture, Spirit transportation, and protective snatching to God — acts in which the inner person is taken into the divine presence or safety | active |

**Verses:**

**vid=168001** — `Mat 11:12`
*target word in verse:* `force`

> Mat 11:12 From the days of John the Baptist until now the kingdom of heaven has suffered violence , and the violent take it by force .

_Prior classification: **relevant** · related · group=`5493-001`_


**vid=168002** — `Mat 13:19`
*target word in verse:* `snatches away`

> Mat 13:19 When anyone hears the word of the kingdom and does not understand it, the evil one comes and snatches away what has been sown in his heart . This is what was sown along the path .

_Prior classification: **relevant** · **anchor** · group=`5493-001`_


**vid=167999** — `Joh 6:15`
*target word in verse:* `force`

> Joh 6:15 Perceiving then that they were about to come and take him by force to make him king , Jesus withdrew again to the mountain by himself .


**vid=167996** — `Joh 10:12`
*target word in verse:* `snatches`

> Joh 10:12 He who is a hired hand and not a shepherd , who does not own the sheep , sees the wolf coming and leaves the sheep and flees , and the wolf snatches them and scatters them.

_Prior classification: **relevant** · related · group=`5493-001`_


**vid=167997** — `Joh 10:28`
*target word in verse:* `snatch`

> Joh 10:28 I give them eternal life , and they will never perish , and no one will snatch them out of my hand .

_Prior classification: **relevant** · related · group=`5493-001`_


**vid=167998** — `Joh 10:29`
*target word in verse:* `snatch`

> Joh 10:29 My Father , who has given them to me , is greater than all , and no one is able to snatch them out of the Father’s hand .

_Prior classification: **relevant** · **anchor** · group=`5493-001`_


**vid=167995** — `Act 8:39`
*target word in verse:* `away`

> Act 8:39 And when they came up out of the water , the Spirit of the Lord carried Philip away , and the eunuch saw him no more , and went on his way rejoicing .


**vid=167994** — `Act 23:10`
*target word in verse:* `force`

> Act 23:10 And when the dissension became violent , the tribune , afraid that Paul would be torn to pieces by them , commanded the soldiers to go down and take him away from among them by force and bring him into the barracks .


**vid=167992** — `2Cor 12:2`
*target word in verse:* `caught up`

> 2Cor 12:2 I know a man in Christ who fourteen years ago was caught up to the third heaven — whether in the body or out of the body I do not know , God knows .

_Prior classification: **relevant** · related · group=`5493-002`_


**vid=167993** — `2Cor 12:3`
*target word in verse:* `caught up`

> 2Cor 12:3 And I know that this man was caught up into paradise — whether in the body or out of the body I do not know , God knows —

_Prior classification: **relevant** · related · group=`5493-002`_


**vid=167991** — `1Th 4:17`
*target word in verse:* `caught up`

> 1Th 4:17 Then we who are alive , who are left , will be caught up together with them in the clouds to meet the Lord in the air , and so we will always be with the Lord .

_Prior classification: **relevant** · **anchor** · group=`5493-002`_


**vid=168000** — `Jude 23`
*target word in verse:* `snatching`

> Jude 23 save others by snatching them out of the fire ; to others show mercy with fear , hating even the garment stained by the flesh .

_Prior classification: **relevant** · related · group=`5493-001`_


**vid=168003** — `Rev 12:5`
*target word in verse:* `caught up`

> Rev 12:5 She gave birth to a male child , one who is to rule all the nations with a rod of iron , but her child was caught up to God and to his throne ,

_Prior classification: **relevant** · related · group=`5493-002`_



---

## 4. Other terms in this registry

A pointer-only list of the other terms in this registry, so that
wrong-face set-asides can reference them accurately (VC Instruction §3.6).
**Do not classify these terms here** — each is handled in its own Session A
per-term document.


### Other OWNER terms

| Strong's | Translit. | Gloss | Language |
|---|---|---|---|
| `G0724` | harpagē | plunder | Greek |
| `G4123` | pleonektēs | greedy | Greek |
| `G4123` | pleonektēs | greedy | Greek |

### XREF terms (OWNER elsewhere)

| Strong's | Translit. | Gloss | OWNER registry | OWNER word |
|---|---|---|---:|---|
| `G4124` | pleonexia | greediness | — | greediness |
| `G4124` | pleonexia | greediness | 35 | covetousness |
| `H5314` | na.phash | be refreshed | — | be refreshed |
| `H5314` | na.phash | be refreshed | — | be refreshed |
| `H5314` | na.phash | be refreshed | — | be refreshed |
| `H5314` | na.phash | be refreshed | — | be refreshed |
| `H5314` | na.phash | be refreshed | — | be refreshed |
| `H5314` | na.phash | be refreshed | — | be refreshed |
| `H5314` | na.phash | be refreshed | — | be refreshed |
| `H5314` | na.phash | be refreshed | — | be refreshed |
| `H5314` | na.phash | be refreshed | 182 | be refreshed |
| `H5315G` | ne.phesh | soul | — | soul |
| `H5315G` | ne.phesh | soul | — | soul |
| `H5315G` | ne.phesh | soul | — | soul |
| `H5315G` | ne.phesh | soul | — | soul |
| `H5315G` | ne.phesh | soul | — | soul |
| `H5315G` | ne.phesh | soul | — | soul |
| `H5315G` | ne.phesh | soul | — | soul |
| `H5315G` | ne.phesh | soul | — | soul |
| `H5315G` | ne.phesh | soul | 182 | soul |
| `H5315H` | ne.phesh | soul: life | — | soul: life |
| `H5315H` | ne.phesh | soul: life | — | soul: life |
| `H5315H` | ne.phesh | soul: life | — | soul: life |
| `H5315H` | ne.phesh | soul: life | — | soul: life |
| `H5315H` | ne.phesh | soul: life | — | soul: life |
| `H5315H` | ne.phesh | soul: life | — | soul: life |
| `H5315H` | ne.phesh | soul: life | — | soul: life |
| `H5315H` | ne.phesh | soul: life | — | soul: life |
| `H5315H` | ne.phesh | soul: life | 182 | soul |
| `H5315I` | ne.phesh | soul: myself | — | soul: myself |
| `H5315I` | ne.phesh | soul: myself | — | soul: myself |
| `H5315I` | ne.phesh | soul: myself | — | soul: myself |
| `H5315I` | ne.phesh | soul: myself | — | soul: myself |
| `H5315I` | ne.phesh | soul: myself | — | soul: myself |
| `H5315I` | ne.phesh | soul: myself | — | soul: myself |
| `H5315I` | ne.phesh | soul: myself | — | soul: myself |
| `H5315I` | ne.phesh | soul: myself | — | soul: myself |
| `H5315I` | ne.phesh | soul: myself | 182 | soul |
| `H5315J` | ne.phesh | soul: person | — | soul: person |
| `H5315J` | ne.phesh | soul: person | — | soul: person |
| `H5315J` | ne.phesh | soul: person | — | soul: person |
| `H5315J` | ne.phesh | soul: person | — | soul: person |
| `H5315J` | ne.phesh | soul: person | — | soul: person |
| `H5315J` | ne.phesh | soul: person | — | soul: person |
| `H5315J` | ne.phesh | soul: person | — | soul: person |
| `H5315J` | ne.phesh | soul: person | — | soul: person |
| `H5315J` | ne.phesh | soul: person | 182 | soul |
| `H5315K` | ne.phesh | soul: animal | — | soul: animal |
| `H5315K` | ne.phesh | soul: animal | — | soul: animal |
| `H5315K` | ne.phesh | soul: animal | — | soul: animal |
| `H5315K` | ne.phesh | soul: animal | — | soul: animal |
| `H5315K` | ne.phesh | soul: animal | — | soul: animal |
| `H5315K` | ne.phesh | soul: animal | — | soul: animal |
| `H5315K` | ne.phesh | soul: animal | — | soul: animal |
| `H5315K` | ne.phesh | soul: animal | — | soul: animal |
| `H5315K` | ne.phesh | soul: animal | 182 | soul |
| `H5315L` | ne.phesh | soul: appetite | — | soul: appetite |
| `H5315L` | ne.phesh | soul: appetite | — | soul: appetite |
| `H5315L` | ne.phesh | soul: appetite | — | soul: appetite |
| `H5315L` | ne.phesh | soul: appetite | — | soul: appetite |
| `H5315L` | ne.phesh | soul: appetite | — | soul: appetite |
| `H5315L` | ne.phesh | soul: appetite | — | soul: appetite |
| `H5315L` | ne.phesh | soul: appetite | — | soul: appetite |
| `H5315L` | ne.phesh | soul: appetite | — | soul: appetite |
| `H5315L` | ne.phesh | soul: appetite | 182 | soul |
| `H5315M` | ne.phesh | soul: dead | — | soul: dead |
| `H5315M` | ne.phesh | soul: dead | — | soul: dead |
| `H5315M` | ne.phesh | soul: dead | — | soul: dead |
| `H5315M` | ne.phesh | soul: dead | — | soul: dead |
| `H5315M` | ne.phesh | soul: dead | — | soul: dead |
| `H5315M` | ne.phesh | soul: dead | — | soul: dead |
| `H5315M` | ne.phesh | soul: dead | — | soul: dead |
| `H5315M` | ne.phesh | soul: dead | — | soul: dead |
| `H5315M` | ne.phesh | soul: dead | 182 | soul |
| `H5315N` | ne.phesh | soul: neck | — | soul: neck |
| `H5315N` | ne.phesh | soul: neck | — | soul: neck |
| `H5315N` | ne.phesh | soul: neck | — | soul: neck |
| `H5315N` | ne.phesh | soul: neck | — | soul: neck |
| `H5315N` | ne.phesh | soul: neck | — | soul: neck |
| `H5315N` | ne.phesh | soul: neck | — | soul: neck |
| `H5315N` | ne.phesh | soul: neck | — | soul: neck |
| `H5315N` | ne.phesh | soul: neck | — | soul: neck |
| `H5315N` | ne.phesh | soul: neck | 182 | soul |
| `H5317` | no.phet | honey | — | honey |
| `H5317` | no.phet | honey | — | honey |
| `H5317` | no.phet | honey | — | honey |
| `H5317` | no.phet | honey | — | honey |
| `H5317` | no.phet | honey | 182 | honey |
| `H5317` | no.phet | honey | — | honey |
| `H5317` | no.phet | honey | — | honey |
| `H5317` | no.phet | honey | — | honey |
| `H5317` | no.phet | honey | — | honey |

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


_No open catalogue questions linked to this registry's flags._

---

## Footer — what happens next

A Claude AI Verse Context session produces a `VERSECONTEXT` patch
covering this term (and any others classified in the same session).
The patch must declare `_patch_meta.terms_covered` including
`mti_term_id = 5493`. On apply, Claude Code flips
this term's `mti_terms.vc_status` to `complete` and re-derives the
owning registry's `verse_context_status` from the aggregate of all
its OWNER + XREF-via-OWNER term statuses (VC-2 in the applicator;
alignment analysis v4 §8.2).

*End of Session A prose for term G0726
(070 greed).*
