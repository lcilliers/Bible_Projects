# Session A — Term `G3552` *noseō* — be sick

**Registry:** 193 craving  
**mti_term_id:** 1295  
**Language:** Greek  
**md_version:** `v1`  ⚠ the patch's `_patch_meta.input_versions[1295]` must equal `1` at submission time or the applicator will reject it as stale (A-03 version gate).  
**Generated:** 2026-04-25 14:20  
**Current vc_status:** `not_done`  
**Existing verse_context rows:** 1 active (of 1 verses for this term).  ⚠ Per-verse: emit `insert` for verses with no active row; emit `update` for verses with an active row being revised. See v3_5 §2.1–§2.4 and §6.1. The per-verse state is shown in the Verses section below.  
**Source:** `data/bible_research.db` (deterministic render, no analytics)  
**Governing instruction:** wa-versecontext-instruction [current]  
**Produced by:** `scripts/build_session_a_prose.py --term`

---

## About this document

This document is the Session A input for **Verse Context classification** of
a single OWNER term — `G3552` *noseō* (be sick) from registry
193 craving. It contains the STEP-sourced data for this one term only.
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


### G3552 · *noseō* · be sick

- **Language:** Greek
- **mti_term_id:** 1295
- **STEP gloss:** be sick
- **Word-analysis gloss:** be sick
- **Mounce short def:** to be unhealthy, ill sick
- **Occurrence count:** 1

**Parsed senses:**

- `1` to be unhealthy, ill sick 
to be sick;, metaphorically to have a diseased appetite or craving for a thing, have an excessive and vicious fondness for a thing, 1Tim. 6:4*

**Related words:**

- `G3553` *nosēma* — disease
- `G3554` *nosos* — illness

**Root family:**

- `NOS` (Greek) — be sick — Backfilled 2026-04-09 from wa_term_related_words clustering

**Data-quality flags (informational):**

- `NO_WORD_ANALYSIS` — meaning field is null for G3552. STEP returned no word analysis block for this term.
- `PROSE_ONLY_MEANING` — Meaning for G3552 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
- `VERSE_EVIDENCE_CONCENTRATED` — Only 1 confirmed verse records for G3552. Threshold is 5.


---

## 3. Verses

The complete verse corpus for each OWNER term. This is the object of
classification. Every active verse (`delete_flagged = 0`) must be assessed
against the governing filter. Any existing `verse_context` state is shown
per verse as **Prior classification** — review, and revise only where
clearly warranted (VC Instruction §6.2 Step 2).


### G3552 · *noseō* — 1 active verse(s)

- **mti_term_id:** 1295
- **Language:** Greek
- **Gloss:** be sick
- **Total verses:** 1 (1 active, 0 delete_flagged)
- **Prior verse_context groups:** 1 active

**Existing verse_context groups for this term:**

| group_code | description | state |
|---|---|---|
| `1295-001` | Term names the sick/morbid craving of the inner person — the unhealthy inner obsession with controversy that produces envy, dissension, and evil suspicions | active |

**Verses:**

**vid=54662** — `1Ti 6:4`
*target word in verse:* `unhealthy craving`

> 1Ti 6:4 he is puffed up with conceit and understands nothing . He has an unhealthy craving for controversy and for quarrels about words , which produce envy , dissension , slander , evil suspicions ,

_Prior classification: **relevant** · **anchor** · group=`1295-001`_



---

## 4. Other terms in this registry

A pointer-only list of the other terms in this registry, so that
wrong-face set-asides can reference them accurately (VC Instruction §3.6).
**Do not classify these terms here** — each is handled in its own Session A
per-term document.


### Other OWNER terms

| Strong's | Translit. | Gloss | Language |
|---|---|---|---|
| `G3553` | nosēma | disease | Greek |
| `G3554` | nosos | illness | Greek |
| `G3713` | oregō | to aspire | Greek |
| `G3713` | oregō | to aspire | Greek |
| `G3713` | oregō | to aspire | Greek |

### XREF terms (OWNER elsewhere)

| Strong's | Translit. | Gloss | OWNER registry | OWNER word |
|---|---|---|---:|---|
| `H0176A` | o | or | — | or |
| `H0176A` | o | or | — | or |
| `H0176A` | o | or | 175 | wonder |
| `H0176A` | o | or | — | or |
| `H0176A` | o | or | — | or |
| `H0183` | a.vah | to desire | — | to desire |
| `H0183` | a.vah | to desire | — | to desire |
| `H0183` | a.vah | to desire | — | to desire |
| `H0183` | a.vah | to desire | 43 | desire |
| `H0185` | av.vah | desire | — | desire |
| `H0185` | av.vah | desire | — | desire |
| `H0185` | av.vah | desire | 43 | desire |
| `H0185` | av.vah | desire | — | desire |
| `H1933A` | ha.va | to fall | — | to fall |
| `H1933A` | ha.va | to fall | — | to fall |
| `H1933A` | ha.va | to fall | — | to fall |
| `H1933A` | ha.va | to fall | 43 | to fall |
| `H1933A` | ha.va | to fall | — | to fall |
| `H1933B` | ha.vah | to be | — | to be |
| `H1933B` | ha.vah | to be | — | to be |
| `H1933B` | ha.vah | to be | — | to be |
| `H1933B` | ha.vah | to be | 43 | to be |
| `H1933B` | ha.vah | to be | — | to be |
| `H1934` | ha.va | to be | — | to be |
| `H1934` | ha.va | to be | — | to be |
| `H1934` | ha.va | to be | — | to be |
| `H1934` | ha.va | to be | 198 | might |
| `H1942` | hav.vah | desire | — | desire |
| `H1942` | hav.vah | desire | — | desire |
| `H1942` | hav.vah | desire | 43 | desire |
| `H1943` | ho.vah | misfortune | — | misfortune |
| `H1943` | ho.vah | misfortune | — | misfortune |
| `H1943` | ho.vah | misfortune | 43 | misfortune |
| `H1962` | hay.yah | calamity | — | calamity |
| `H1962` | hay.yah | calamity | — | calamity |
| `H1962` | hay.yah | calamity | 43 | calamity |
| `H3068H` | ye.ho.vah | The Lord | — | The Lord |
| `H3068H` | ye.ho.vah | The Lord | — | The Lord |
| `H3068H` | ye.ho.vah | The Lord | 42 | The Lord |
| `H3068H` | ye.ho.vah | The Lord | — | The Lord |
| `H3068H` | ye.ho.vah | The Lord | — | The Lord |
| `H3068I` | ye.ho.vah | [Jerusalem of] the Lord | — | [Jerusalem of] the Lord |
| `H3068I` | ye.ho.vah | [Jerusalem of] the Lord | — | [Jerusalem of] the Lord |
| `H3068I` | ye.ho.vah | [Jerusalem of] the Lord | 42 | [Jerusalem of] the Lord |
| `H3068I` | ye.ho.vah | [Jerusalem of] the Lord | — | [Jerusalem of] the Lord |
| `H3068I` | ye.ho.vah | [Jerusalem of] the Lord | — | [Jerusalem of] the Lord |
| `H3092K` | ye.ho.sha.phat | [Valley of] Jehoshaphat | — | [Valley of] Jehoshaphat |
| `H3092K` | ye.ho.sha.phat | [Valley of] Jehoshaphat | — | [Valley of] Jehoshaphat |
| `H3092K` | ye.ho.sha.phat | [Valley of] Jehoshaphat | 43 | [Valley of] Jehoshaphat |
| `H3970` | ma.a.vay | desire | — | desire |
| `H3970` | ma.a.vay | desire | — | desire |
| `H3970` | ma.a.vay | desire | 43 | desire |
| `H3970` | ma.a.vay | desire | — | desire |
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
| `H8378` | ta.a.vah | desire | — | desire |
| `H8378` | ta.a.vah | desire | — | desire |
| `H8378` | ta.a.vah | desire | — | desire |
| `H8378` | ta.a.vah | desire | 43 | desire |

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
`mti_term_id = 1295`. On apply, Claude Code flips
this term's `mti_terms.vc_status` to `complete` and re-derives the
owning registry's `verse_context_status` from the aggregate of all
its OWNER + XREF-via-OWNER term statuses (VC-2 in the applicator;
alignment analysis v4 §8.2).

*End of Session A prose for term G3552
(193 craving).*
