# Session A — Term `G0019` *agathōsunē* — goodness

**Registry:** 067 goodness  
**mti_term_id:** 885  
**Language:** Greek  
**md_version:** `v1`  ⚠ the patch's `_patch_meta.input_versions[885]` must equal `1` at submission time or the applicator will reject it as stale (A-03 version gate).  
**Generated:** 2026-04-25 16:06  
**Current vc_status:** `not_done`  
**Existing verse_context rows:** 4 active (of 4 verses for this term).  ⚠ Per-verse: emit `insert` for verses with no active row; emit `update` for verses with an active row being revised. See v3_5 §2.1–§2.4 and §6.1. The per-verse state is shown in the Verses section below.  
**Source:** `data/bible_research.db` (deterministic render, no analytics)  
**Governing instruction:** wa-versecontext-instruction [current]  
**Produced by:** `scripts/build_session_a_prose.py --term`

---

## About this document

This document is the Session A input for **Verse Context classification** of
a single OWNER term — `G0019` *agathōsunē* (goodness) from registry
067 goodness. It contains the STEP-sourced data for this one term only.
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


### G0019 · *agathōsunē* · goodness

- **Language:** Greek
- **mti_term_id:** 885
- **STEP gloss:** goodness
- **Word-analysis gloss:** goodness
- **Mounce short def:** goodness
- **Occurrence count:** 17

**Parsed senses:**

- `1` goodness, virtue, beneficence, Rom. 15:14; Eph. 5:9; 2Thess. 1:11; generosity, Gal. 5:22*

**Related words:**

- `G0014` *agathoergeō* — to do good
- `G0015` *agathopoieō* — to do good
- `G0016` *agathopoiia* — doing good
- `G0017` *agathopoios* — doing good
- `G0018` *agathos* — good
- `G0865` *afilagathos* — hating good
- `G5358` *filagathos* — lover of good

**Root family:**

- `AGATHŌSUN` (Greek) — goodness — Backfilled 2026-04-09 from wa_term_related_words clustering

**Data-quality flags (informational):**

- `NO_WORD_ANALYSIS` — meaning field is null for G0019. STEP returned no word analysis block for this term.
- `PROSE_ONLY_MEANING` — Meaning for G0019 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
- `VERSE_EVIDENCE_CONCENTRATED` — Only 4 confirmed verse records for G0019. Threshold is 5.


---

## 3. Verses

The complete verse corpus for each OWNER term. This is the object of
classification. Every active verse (`delete_flagged = 0`) must be assessed
against the governing filter. Any existing `verse_context` state is shown
per verse as **Prior classification** — review, and revise only where
clearly warranted (VC Instruction §6.2 Step 2).


### G0019 · *agathōsunē* — 4 active verse(s)

- **mti_term_id:** 885
- **Language:** Greek
- **Gloss:** goodness
- **Total verses:** 4 (4 active, 0 delete_flagged)
- **Prior verse_context groups:** 1 active

**Existing verse_context groups for this term:**

| group_code | description | state |
|---|---|---|
| `885-001` | Term names goodness as an inner-being disposition and Spirit-produced fruit — a quality that fills the person and is completed by God, expressed in righteous conduct and resolve | active |

**Verses:**

**vid=24450** — `Rom 15:14`
*target word in verse:* `goodness`

> Rom 15:14 I myself am satisfied about you , my brothers , that you yourselves are full of goodness , filled with all knowledge and able to instruct one another .

_Prior classification: **relevant** · related · group=`885-001`_


**vid=24449** — `Gal 5:22`
*target word in verse:* `goodness`

> Gal 5:22 But the fruit of the Spirit is love , joy , peace , patience , kindness , goodness , faithfulness ,

_Prior classification: **relevant** · **anchor** · group=`885-001`_


**vid=24448** — `Eph 5:9`
*target word in verse:* `good`

> Eph 5:9 ( for the fruit of light is found in all that is good and right and true ),

_Prior classification: **relevant** · related · group=`885-001`_


**vid=164874** — `2Th 1:11`
*target word in verse:* `good`

> 2Th 1:11 To this end we always pray for you , that our God may make you worthy of his calling and may fulfill every resolve for good and every work of faith by his power ,

_Prior classification: **relevant** · related · group=`885-001`_



---

## 4. Other terms in this registry

A pointer-only list of the other terms in this registry, so that
wrong-face set-asides can reference them accurately (VC Instruction §3.6).
**Do not classify these terms here** — each is handled in its own Session A
per-term document.


### Other OWNER terms

| Strong's | Translit. | Gloss | Language |
|---|---|---|---|
| `G0019` | agathōsunē | goodness | Greek |
| `G0019` | agathōsunē | goodness | Greek |
| `G5544` | chrēstotēs | kindness | Greek |
| `G5544` | chrēstotēs | kindness | Greek |
| `H2896A` | tov | pleasant | Hebrew |
| `H2896A` | tov | pleasant | Hebrew |
| `H2896A` | tov | pleasant | Hebrew |

### XREF terms (OWNER elsewhere)

| Strong's | Translit. | Gloss | OWNER registry | OWNER word |
|---|---|---|---:|---|
| `G0014` | agathoergeō | to do good | — | to do good |
| `G0014` | agathoergeō | to do good | — | to do good |
| `G0014` | agathoergeō | to do good | 65 | to do good |
| `G0015` | agathopoieō | to do good | — | to do good |
| `G0015` | agathopoieō | to do good | — | to do good |
| `G0015` | agathopoieō | to do good | 65 | to do good |
| `G0016` | agathopoiia | doing good | — | doing good |
| `G0016` | agathopoiia | doing good | — | doing good |
| `G0016` | agathopoiia | doing good | 65 | doing good |
| `G0017` | agathopoios | doing good | — | doing good |
| `G0017` | agathopoios | doing good | — | doing good |
| `G0017` | agathopoios | doing good | 65 | doing good |
| `G0018` | agathos | good | — | good |
| `G0018` | agathos | good | — | good |
| `G0018` | agathos | good | 65 | generosity |
| `G0865` | afilagathos | hating good | — | hating good |
| `G0865` | afilagathos | hating good | — | hating good |
| `G0865` | afilagathos | hating good | 65 | hating good |
| `G5358` | filagathos | lover of good | — | lover of good |
| `G5358` | filagathos | lover of good | — | lover of good |
| `G5358` | filagathos | lover of good | 103 | love |
| `H2869` | tav | fine | — | fine |
| `H2869` | tav | fine | 42 | fine |
| `H2895` | tov | be pleasing | — | be pleasing |
| `H2895` | tov | be pleasing | — | be pleasing |
| `H2895` | tov | be pleasing | 103 | love |
| `H2896B` | tov | good | — | good |
| `H2896B` | tov | good | 42 | good |
| `H2896B` | tov | good | — | good |
| `H2896C` | to.vah | welfare | — | welfare |
| `H2896C` | to.vah | welfare | 186 | gladness |
| `H2896C` | to.vah | welfare | — | welfare |
| `H2896C` | to.vah | welfare | — | welfare |
| `H2898` | tuv | goodness | 103 | love |
| `H2898` | tuv | goodness | 103 | goodness |
| `H2898` | tuv | goodness | 103 | goodness |
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
| `H3652` | ken | thus | — | thus |
| `H3652` | ken | thus | — | thus |
| `H3652` | ken | thus | — | thus |
| `H3652` | ken | thus | — | thus |
| `H3652` | ken | thus | 48 | thus |
| `H4605` | ma.al | above | — | above |
| `H4605` | ma.al | above | — | above |
| `H4605` | ma.al | above | — | above |
| `H4605` | ma.al | above | 52 | above |
| `H4605` | ma.al | above | — | above |
| `H4607` | mo.al | lifting | — | lifting |
| `H4607` | mo.al | lifting | — | lifting |
| `H4607` | mo.al | lifting | — | lifting |
| `H4607` | mo.al | lifting | 52 | lifting |
| `H4607` | mo.al | lifting | — | lifting |
| `H4608` | ma.a.leh | ascent | — | ascent |
| `H4608` | ma.a.leh | ascent | — | ascent |
| `H4608` | ma.a.leh | ascent | — | ascent |
| `H4608` | ma.a.leh | ascent | 52 | ascent |
| `H4608` | ma.a.leh | ascent | — | ascent |
| `H4609A` | ma.a.lah | thought | — | thought |
| `H4609A` | ma.a.lah | thought | — | thought |
| `H4609A` | ma.a.lah | thought | — | thought |
| `H4609A` | ma.a.lah | thought | 52 | thought |
| `H4609A` | ma.a.lah | thought | — | thought |
| `H4609B` | ma.a.lah | step | — | step |
| `H4609B` | ma.a.lah | step | — | step |
| `H4609B` | ma.a.lah | step | — | step |
| `H4609B` | ma.a.lah | step | 52 | step |
| `H4609B` | ma.a.lah | step | — | step |
| `H5920H` | al | height | — | height |
| `H5920H` | al | height | — | height |
| `H5920H` | al | height | — | height |
| `H5920H` | al | height | 52 | height |
| `H5920H` | al | height | — | height |
| `H5920H` | al | height | — | height |
| `H5922` | al | since | — | since |
| `H5922` | al | since | — | since |
| `H5922` | al | since | — | since |
| `H5922` | al | since | 52 | since |
| `H5924` | el.la | above | — | above |
| `H5924` | el.la | above | — | above |
| `H5924` | el.la | above | — | above |
| `H5924` | el.la | above | 52 | above |
| `H5927G` | a.lah | to ascend: rise | — | to ascend: rise |
| `H5927G` | a.lah | to ascend: rise | — | to ascend: rise |
| `H5927G` | a.lah | to ascend: rise | — | to ascend: rise |
| `H5927G` | a.lah | to ascend: rise | 188 | weeping |
| `H5927G` | a.lah | to ascend: rise | — | to ascend: rise |
| `H5927G` | a.lah | to ascend: rise | — | to ascend: rise |
| `H5927H` | a.lah | to ascend: establish | — | to ascend: establish |
| `H5927H` | a.lah | to ascend: establish | — | to ascend: establish |
| `H5927H` | a.lah | to ascend: establish | — | to ascend: establish |
| `H5927H` | a.lah | to ascend: establish | 52 | to ascend: establish |
| `H5927H` | a.lah | to ascend: establish | — | to ascend: establish |
| `H5927I` | a.lah | to ascend: offer up | — | to ascend: offer up |
| `H5927I` | a.lah | to ascend: offer up | — | to ascend: offer up |
| `H5927I` | a.lah | to ascend: offer up | — | to ascend: offer up |
| `H5927I` | a.lah | to ascend: offer up | 52 | to ascend: offer up |
| `H5927I` | a.lah | to ascend: offer up | — | to ascend: offer up |
| `H5927J` | a.lah | to ascend: attack | — | to ascend: attack |
| `H5927J` | a.lah | to ascend: attack | — | to ascend: attack |
| `H5927J` | a.lah | to ascend: attack | — | to ascend: attack |
| `H5927J` | a.lah | to ascend: attack | 52 | to ascend: attack |
| `H5927J` | a.lah | to ascend: attack | — | to ascend: attack |
| `H5927K` | a.lah | to ascend: copulate | — | to ascend: copulate |
| `H5927K` | a.lah | to ascend: copulate | — | to ascend: copulate |
| `H5927K` | a.lah | to ascend: copulate | — | to ascend: copulate |
| `H5927K` | a.lah | to ascend: copulate | 52 | to ascend: copulate |
| `H5927K` | a.lah | to ascend: copulate | — | to ascend: copulate |
| `H5927L` | a.lah | to ascend: dawn | — | to ascend: dawn |
| `H5927L` | a.lah | to ascend: dawn | — | to ascend: dawn |
| `H5927L` | a.lah | to ascend: dawn | — | to ascend: dawn |
| `H5927L` | a.lah | to ascend: dawn | 52 | to ascend: dawn |
| `H5927L` | a.lah | to ascend: dawn | — | to ascend: dawn |
| `H5927M` | a.lah | to ascend: regurgitate | — | to ascend: regurgitate |
| `H5927M` | a.lah | to ascend: regurgitate | — | to ascend: regurgitate |
| `H5927M` | a.lah | to ascend: regurgitate | — | to ascend: regurgitate |
| `H5927M` | a.lah | to ascend: regurgitate | 52 | to ascend: regurgitate |
| `H5927M` | a.lah | to ascend: regurgitate | — | to ascend: regurgitate |
| `H5929` | a.leh | leaf | — | leaf |
| `H5929` | a.leh | leaf | — | leaf |
| `H5929` | a.leh | leaf | — | leaf |
| `H5929` | a.leh | leaf | 52 | leaf |
| `H5929` | a.leh | leaf | — | leaf |
| `H5930A` | o.lah | burnt offering | — | burnt offering |
| `H5930A` | o.lah | burnt offering | — | burnt offering |
| `H5930A` | o.lah | burnt offering | — | burnt offering |
| `H5930A` | o.lah | burnt offering | 52 | burnt offering |
| `H5930A` | o.lah | burnt offering | — | burnt offering |
| `H5930B` | o.lah | ascent | — | ascent |
| `H5930B` | o.lah | ascent | — | ascent |
| `H5930B` | o.lah | ascent | — | ascent |
| `H5930B` | o.lah | ascent | 52 | ascent |
| `H5930B` | o.lah | ascent | — | ascent |
| `H5940` | e.li | pestle | — | pestle |
| `H5940` | e.li | pestle | — | pestle |
| `H5940` | e.li | pestle | — | pestle |
| `H5940` | e.li | pestle | 52 | pestle |
| `H5940` | e.li | pestle | — | pestle |
| `H5942` | il.li | upper | — | upper |
| `H5942` | il.li | upper | — | upper |
| `H5942` | il.li | upper | — | upper |
| `H5942` | il.li | upper | 52 | upper |
| `H5942` | il.li | upper | — | upper |
| `H5944` | a.liy.yah | upper room | — | upper room |
| `H5944` | a.liy.yah | upper room | — | upper room |
| `H5944` | a.liy.yah | upper room | — | upper room |
| `H5944` | a.liy.yah | upper room | 52 | upper room |
| `H5944` | a.liy.yah | upper room | — | upper room |
| `H5945A` | el.yon | high | — | high |
| `H5945A` | el.yon | high | — | high |
| `H5945A` | el.yon | high | — | high |
| `H5945A` | el.yon | high | 52 | high |
| `H5945A` | el.yon | high | — | high |
| `H5945A` | el.yon | high | — | high |
| `H5945B` | el.yon | Most High [God] | — | Most High [God] |
| `H5945B` | el.yon | Most High [God] | — | Most High [God] |
| `H5945B` | el.yon | Most High [God] | — | Most High [God] |
| `H5945B` | el.yon | Most High [God] | 52 | Most High [God] |
| `H5945B` | el.yon | Most High [God] | — | Most High [God] |
| `H5945B` | el.yon | Most High [God] | — | Most High [God] |
| `H5945G` | el.yon | Upper [Beth Horon] | — | Upper [Beth Horon] |
| `H5945G` | el.yon | Upper [Beth Horon] | — | Upper [Beth Horon] |
| `H5945G` | el.yon | Upper [Beth Horon] | — | Upper [Beth Horon] |
| `H5945G` | el.yon | Upper [Beth Horon] | 52 | Upper [Beth Horon] |
| `H5945G` | el.yon | Upper [Beth Horon] | — | Upper [Beth Horon] |
| `H5945G` | el.yon | Upper [Beth Horon] | — | Upper [Beth Horon] |
| `H5945H` | el.yon | [LORD] Most High | — | [LORD] Most High |
| `H5945H` | el.yon | [LORD] Most High | — | [LORD] Most High |
| `H5945H` | el.yon | [LORD] Most High | — | [LORD] Most High |
| `H5945H` | el.yon | [LORD] Most High | 52 | [LORD] Most High |
| `H5945H` | el.yon | [LORD] Most High | — | [LORD] Most High |
| `H5945H` | el.yon | [LORD] Most High | — | [LORD] Most High |
| `H8585A` | te.a.lah | conduit | — | conduit |
| `H8585A` | te.a.lah | conduit | — | conduit |
| `H8585A` | te.a.lah | conduit | — | conduit |
| `H8585A` | te.a.lah | conduit | 52 | conduit |
| `H8585A` | te.a.lah | conduit | — | conduit |
| `H8585B` | te.a.lah | healing | — | healing |
| `H8585B` | te.a.lah | healing | — | healing |
| `H8585B` | te.a.lah | healing | — | healing |
| `H8585B` | te.a.lah | healing | 52 | healing |
| `H8585B` | te.a.lah | healing | — | healing |

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
`mti_term_id = 885`. On apply, Claude Code flips
this term's `mti_terms.vc_status` to `complete` and re-derives the
owning registry's `verse_context_status` from the aggregate of all
its OWNER + XREF-via-OWNER term statuses (VC-2 in the applicator;
alignment analysis v4 §8.2).

*End of Session A prose for term G0019
(067 goodness).*
