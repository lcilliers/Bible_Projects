# Session A — Term `H4906` *mas.kit* — figure

**Registry:** 085 imagination  
**mti_term_id:** 916  
**Language:** Hebrew  
**md_version:** `v1`  ⚠ the patch's `_patch_meta.input_versions[916]` must equal `1` at submission time or the applicator will reject it as stale (A-03 version gate).  
**Generated:** 2026-04-25 14:20  
**Current vc_status:** `not_done`  
**Existing verse_context rows:** 3 active (of 6 verses for this term).  ⚠ Per-verse: emit `insert` for verses with no active row; emit `update` for verses with an active row being revised. See v3_5 §2.1–§2.4 and §6.1. The per-verse state is shown in the Verses section below.  
**Source:** `data/bible_research.db` (deterministic render, no analytics)  
**Governing instruction:** wa-versecontext-instruction [current]  
**Produced by:** `scripts/build_session_a_prose.py --term`

---

## About this document

This document is the Session A input for **Verse Context classification** of
a single OWNER term — `H4906` *mas.kit* (figure) from registry
085 imagination. It contains the STEP-sourced data for this one term only.
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


### H4906 · *mas.kit* · figure

- **Language:** Hebrew
- **mti_term_id:** 916
- **STEP gloss:** figure
- **Word-analysis gloss:** figure
- **Occurrence count:** 6

**Parsed senses:**

- `1` show-piece, figure, imagination, image, idol, picture
- `1a` show-piece, carved figure (of idols)
- `1b` imagination, conceit

**Related words:**

- `H7634` *sa.khe.yah* — Sachia
- `H7906` *se.khu* — Secu
- `H7907` *sekh.vi* — heart
- `H7914` *se.khiy.yah* — craft
- `H7915` *sak.kin* — knife

**Root family:**

- `SKIT` (Hebrew) — craft — Backfilled 2026-04-09 from wa_term_related_words clustering

**Data-quality flags (informational):**

- `NO_WORD_ANALYSIS` — meaning field is null for H4906. STEP returned no word analysis block for this term.
- `VERSE_EVIDENCE_CONCENTRATED` — Low occurrence count: 6. Statistical patterns unreliable with fewer than 20 occurrences.


---

## 3. Verses

The complete verse corpus for each OWNER term. This is the object of
classification. Every active verse (`delete_flagged = 0`) must be assessed
against the governing filter. Any existing `verse_context` state is shown
per verse as **Prior classification** — review, and revise only where
clearly warranted (VC Instruction §6.2 Step 2).


### H4906 · *mas.kit* — 6 active verse(s)

- **mti_term_id:** 916
- **Language:** Hebrew
- **Gloss:** figure
- **Total verses:** 6 (6 active, 0 delete_flagged)
- **Prior verse_context groups:** 1 active

**Existing verse_context groups for this term:**

| group_code | description | state |
|---|---|---|
| `916-001` | Term names the figure or imagination as an inner mental content — the inner picture the person holds of reality, whether the heart's overflow of fancies or the mind's false image of security | active |

**Verses:**

**vid=25235** — `Lev 26:1`
*target word in verse:* `figured`

> Lev 26:1 “You shall not make idols for yourselves or erect an image or pillar , and you shall not set up a figured stone in your land to bow down to it, for I am the Lord your God .


**vid=25236** — `Num 33:52`
*target word in verse:* `figured stones`

> Num 33:52 then you shall drive out all the inhabitants of the land from before you and destroy all their figured stones and destroy all their metal images and demolish all their high places .


**vid=169899** — `Psa 73:7`
*target word in verse:* `follies`

> Psa 73:7 Their eyes swell out through fatness ; their hearts overflow with follies .

_Prior classification: **relevant** · related · group=`916-001`_


**vid=169897** — `Pro 18:11`
*target word in verse:* `imagination`

> Pro 18:11 A rich man’s wealth is his strong city , and like a high wall in his imagination .

_Prior classification: **relevant** · **anchor** · group=`916-001`_


**vid=169898** — `Pro 25:11`
*target word in verse:* `setting`

> Pro 25:11 A word fitly spoken is like apples of gold in a setting of silver .


**vid=169896** — `Eze 8:12`
*target word in verse:* `pictures`

> Eze 8:12 Then he said to me, “ Son of man , have you seen what the elders of the house of Israel are doing in the dark , each in his room of pictures ? For they say , ‘The Lord does not see us, the Lord has forsaken the land .’”

_Prior classification: **relevant** · related · group=`916-001`_



---

## 4. Other terms in this registry

A pointer-only list of the other terms in this registry, so that
wrong-face set-asides can reference them accurately (VC Instruction §3.6).
**Do not classify these terms here** — each is handled in its own Session A
per-term document.


### Other OWNER terms

| Strong's | Translit. | Gloss | Language |
|---|---|---|---|
| `G1760` | enthumeomai | to reflect on | Greek |
| `G1760` | enthumeomai | to reflect on | Greek |
| `G1761` | enthumēsis | reflection | Greek |
| `G1761` | enthumēsis | reflection | Greek |
| `H4906` | mas.kit | figure | Hebrew |
| `H4906` | mas.kit | figure | Hebrew |
| `H7914` | se.khiy.yah | craft | Hebrew |
| `H7914` | se.khiy.yah | craft | Hebrew |
| `H7914` | se.khiy.yah | craft | Hebrew |
| `H7915` | sak.kin | knife | Hebrew |
| `H7915` | sak.kin | knife | Hebrew |
| `H7915` | sak.kin | knife | Hebrew |

### XREF terms (OWNER elsewhere)

| Strong's | Translit. | Gloss | OWNER registry | OWNER word |
|---|---|---|---:|---|
| `H7907` | sekh.vi | heart | — | heart |
| `H7907` | sekh.vi | heart | — | heart |
| `H7907` | sekh.vi | heart | 183 | heart |

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
`mti_term_id = 916`. On apply, Claude Code flips
this term's `mti_terms.vc_status` to `complete` and re-derives the
owning registry's `verse_context_status` from the aggregate of all
its OWNER + XREF-via-OWNER term statuses (VC-2 in the applicator;
alignment analysis v4 §8.2).

*End of Session A prose for term H4906
(085 imagination).*
