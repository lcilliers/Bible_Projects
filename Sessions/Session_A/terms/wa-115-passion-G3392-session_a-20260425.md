# Session A — Term `G3392` *miainō* — to stain

**Registry:** 115 passion  
**mti_term_id:** 5948  
**Language:** Greek  
**md_version:** `v1`  ⚠ the patch's `_patch_meta.input_versions[5948]` must equal `1` at submission time or the applicator will reject it as stale (A-03 version gate).  
**Generated:** 2026-04-25 14:20  
**Current vc_status:** `not_done`  
**Existing verse_context rows:** 4 active (of 4 verses for this term).  ⚠ Per-verse: emit `insert` for verses with no active row; emit `update` for verses with an active row being revised. See v3_5 §2.1–§2.4 and §6.1. The per-verse state is shown in the Verses section below.  
**Source:** `data/bible_research.db` (deterministic render, no analytics)  
**Governing instruction:** wa-versecontext-instruction [current]  
**Produced by:** `scripts/build_session_a_prose.py --term`

---

## About this document

This document is the Session A input for **Verse Context classification** of
a single OWNER term — `G3392` *miainō* (to stain) from registry
115 passion. It contains the STEP-sourced data for this one term only.
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


### G3392 · *miainō* · to stain

- **Language:** Greek
- **mti_term_id:** 5948
- **STEP gloss:** to stain
- **Word-analysis gloss:** to stain
- **Mounce short def:** to pollute, stain, defile; (<i>passive</i>) to be defiled, corrupted, become ceremonially unclean; this refers to both ceremonial and moral uncleanness
- **Occurrence count:** 116

**Parsed senses:**

- `1` to pollute, stain, defile; (passive) to be defiled, corrupted, become ceremonially unclean; this refers to both ceremonial and moral uncleanness 
primarily to tinge, dye, stain; to pollute, defile, ceremonially, Jn. 18:28; to corrupt, deprave, Tit. 1:15 (2x); Heb. 12:15; Jude 8*

**Related words:**

- `G0283` *amiantos* — pure
- `G3393` *miasma* — defilement
- `G3394` *miasmos* — defilement

**Root family:**

- `MIAINŌ` (Greek) — to stain — Backfilled 2026-04-09 from wa_term_related_words clustering

**Data-quality flags (informational):**

- `NO_WORD_ANALYSIS` — meaning field is null for G3392. STEP returned no word analysis block for this term.
- `PROSE_ONLY_MEANING` — Meaning for G3392 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
- `VERSE_EVIDENCE_CONCENTRATED` — Only 4 confirmed verse records for G3392. Threshold is 5.


---

## 3. Verses

The complete verse corpus for each OWNER term. This is the object of
classification. Every active verse (`delete_flagged = 0`) must be assessed
against the governing filter. Any existing `verse_context` state is shown
per verse as **Prior classification** — review, and revise only where
clearly warranted (VC Instruction §6.2 Step 2).


### G3392 · *miainō* — 4 active verse(s)

- **mti_term_id:** 5948
- **Language:** Greek
- **Gloss:** to stain
- **Total verses:** 4 (4 active, 0 delete_flagged)
- **Prior verse_context groups:** 1 active

**Existing verse_context groups for this term:**

| group_code | description | state |
|---|---|---|
| `5948-001` | Term names moral or ritual defilement — the corruption or staining of the inner person (mind, conscience) or the body as expressive of inner moral disorder | active |

**Verses:**

**vid=184125** — `Joh 18:28`
*target word in verse:* `defiled`

> Joh 18:28 Then they led Jesus from the house of Caiaphas to the governor’s headquarters . It was early morning . They themselves did not enter the governor’s headquarters , so that they would not be defiled , but could eat the Passover .

_Prior classification: **relevant** · related · group=`5948-001`_


**vid=184127** — `Tit 1:15`
*target word in verse:* `defiled`

> Tit 1:15 To the pure , all things are pure , but to the defiled and unbelieving , nothing is pure ; but both their minds and their consciences are defiled .

_Prior classification: **relevant** · **anchor** · group=`5948-001`_


**vid=184124** — `Heb 12:15`
*target word in verse:* `defiled`

> Heb 12:15 See to it that no one fails to obtain the grace of God ; that no “ root of bitterness ” springs up and causes trouble , and by it many become defiled ;

_Prior classification: **relevant** · related · group=`5948-001`_


**vid=184126** — `Jude 8`
*target word in verse:* `defile`

> Jude 8 Yet in like manner these people also , relying on their dreams , defile the flesh , reject authority , and blaspheme the glorious ones.

_Prior classification: **relevant** · related · group=`5948-001`_



---

## 4. Other terms in this registry

A pointer-only list of the other terms in this registry, so that
wrong-face set-asides can reference them accurately (VC Instruction §3.6).
**Do not classify these terms here** — each is handled in its own Session A
per-term document.


### Other OWNER terms

| Strong's | Translit. | Gloss | Language |
|---|---|---|---|
| `G3116` | makrothumōs | patiently | Greek |
| `G3116` | makrothumōs | patiently | Greek |
| `G3116` | makrothumōs | patiently | Greek |
| `G3116` | makrothumōs | patiently | Greek |
| `G3394` | miasmos | defilement | Greek |
| `G3958` | paschō | to suffer | Greek |
| `G3958` | paschō | to suffer | Greek |

### XREF terms (OWNER elsewhere)

| Strong's | Translit. | Gloss | OWNER registry | OWNER word |
|---|---|---|---:|---|
| `G2371` | thumomacheō | to quarrel | — | to quarrel |
| `G2371` | thumomacheō | to quarrel | — | to quarrel |
| `G2371` | thumomacheō | to quarrel | 4 | to quarrel |
| `G2372` | thumos | wrath | — | wrath |
| `G2372` | thumos | wrath | — | wrath |
| `G2372` | thumos | wrath | 4 | anger |
| `G2372` | thumos | wrath | — | wrath |
| `G2372` | thumos | wrath | — | wrath |
| `G2373` | thumoō | to anger | — | to anger |
| `G2373` | thumoō | to anger | — | to anger |
| `G2373` | thumoō | to anger | 4 | anger |
| `G2552` | kakopatheia | suffering | — | suffering |
| `G2552` | kakopatheia | suffering | 23 | suffering |
| `G2553` | kakopatheō | to endure | — | to endure |
| `G2553` | kakopatheō | to endure | 23 | to endure |
| `G3356` | metriopatheō | be gentle | — | be gentle |
| `G3356` | metriopatheō | be gentle | 23 | be gentle |
| `G3663` | homoiopathēs | like | — | like |
| `G3663` | homoiopathēs | like | 23 | like |
| `G3713` | oregō | to aspire | — | to aspire |
| `G3713` | oregō | to aspire | — | to aspire |
| `G3713` | oregō | to aspire | 193 | craving |
| `G3715` | orexis | lust | — | lust |
| `G3715` | orexis | lust | 43 | desire |
| `G3804` | pathēma | suffering | — | suffering |
| `G3804` | pathēma | suffering | 23 | suffering |
| `G3805` | pathētos | suffering | — | suffering |
| `G3805` | pathētos | suffering | 23 | suffering |
| `G4777` | sunkakopatheō | to suffer with | — | to suffer with |
| `G4777` | sunkakopatheō | to suffer with | 23 | to suffer with |
| `G4834` | sumpatheō | to sympathize | — | to sympathize |
| `G4834` | sumpatheō | to sympathize | 23 | compassion |
| `G4835` | sumpathēs | sympathetic | — | sympathetic |
| `G4835` | sumpathēs | sympathetic | 23 | sympathetic |

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
`mti_term_id = 5948`. On apply, Claude Code flips
this term's `mti_terms.vc_status` to `complete` and re-derives the
owning registry's `verse_context_status` from the aggregate of all
its OWNER + XREF-via-OWNER term statuses (VC-2 in the applicator;
alignment analysis v4 §8.2).

*End of Session A prose for term G3392
(115 passion).*
