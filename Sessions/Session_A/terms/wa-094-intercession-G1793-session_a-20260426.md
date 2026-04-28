# Session A — Term `G1793` *entunchanō* — to call on

**Registry:** 094 intercession  
**mti_term_id:** 938  
**Language:** Greek  
**md_version:** `v1`  ⚠ the patch's `_patch_meta.input_versions[938]` must equal `1` at submission time or the applicator will reject it as stale (A-03 version gate).  
**Generated:** 2026-04-26 09:03  
**Current vc_status:** `not_done`  
**Existing verse_context rows:** 5 active (of 5 verses for this term).  ⚠ Per-verse: emit `insert` for verses with no active row; emit `update` for verses with an active row being revised. See v3_5 §2.1–§2.4 and §6.1. The per-verse state is shown in the Verses section below.  
**Source:** `data/bible_research.db` (deterministic render, no analytics)  
**Governing instruction:** wa-versecontext-instruction [current]  
**Produced by:** `scripts/build_session_a_prose.py --term`

---

## About this document

This document is the Session A input for **Verse Context classification** of
a single OWNER term — `G1793` *entunchanō* (to call on) from registry
094 intercession. It contains the STEP-sourced data for this one term only.
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


### G1793 · *entunchanō* · to call on

- **Language:** Greek
- **mti_term_id:** 938
- **STEP gloss:** to call on
- **Word-analysis gloss:** to call on
- **Mounce short def:** to intercede, appeal, petition
- **Occurrence count:** 5

**Parsed senses:**

- `1` to intercede, appeal, petition 
to fill in with, meet; to have conversation with, address; to address, or apply to any one, Acts 25:24; ὑπέρ τινος, to intercede for any one, plead the cause of, Rom. 8:27, 34; Heb. 7:25; κατά τινος, to address a representation or suit against any one, to accuse, complain of, Rom. 11:2*

**Related words:**

- `G1722` *en* — in/on/among
- `G1783` *enteuxis* — intercession
- `G5177` *tunchanō* — to obtain/happen
- `G5241` *huperentunchanō* — to intercede

**Root family:**

- `TUNCHANŌ` (Greek) — to call on — Backfilled 2026-04-09 from wa_term_related_words clustering

**Data-quality flags (informational):**

- `NO_WORD_ANALYSIS` — meaning field is null for G1793. STEP returned no word analysis block for this term.
- `PROSE_ONLY_MEANING` — Meaning for G1793 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
- `VERSE_EVIDENCE_CONCENTRATED` — Low occurrence count: 5. Statistical patterns unreliable with fewer than 20 occurrences.


---

## 3. Verses

The complete verse corpus for each OWNER term. This is the object of
classification. Every active verse (`delete_flagged = 0`) must be assessed
against the governing filter. Any existing `verse_context` state is shown
per verse as **Prior classification** — review, and revise only where
clearly warranted (VC Instruction §6.2 Step 2).


### G1793 · *entunchanō* — 5 active verse(s)

- **mti_term_id:** 938
- **Language:** Greek
- **Gloss:** to call on
- **Total verses:** 5 (5 active, 0 delete_flagged)
- **Prior verse_context groups:** 1 active

**Existing verse_context groups for this term:**

| group_code | description | state |
|---|---|---|
| `938-001` | Term names the act of intercession — the inner act of pleading before God on behalf of another, or the divine advocacy undertaken on behalf of the person | active |

**Verses:**

**vid=175160** — `Act 25:24`
*target word in verse:* `petitioned`

> Act 25:24 And Festus said , “ King Agrippa and all who are present with us , you see this man about whom the whole Jewish people petitioned me , both in Jerusalem and here , shouting that he ought not to live any longer .

_Prior classification: **relevant** · related · group=`938-001`_


**vid=28175** — `Rom 8:27`
*target word in verse:* `intercedes`

> Rom 8:27 And he who searches hearts knows what is the mind of the Spirit , because the Spirit intercedes for the saints according to the will of God .

_Prior classification: **relevant** · **anchor** · group=`938-001`_


**vid=28176** — `Rom 8:34`
*target word in verse:* `interceding`

> Rom 8:34 Who is to condemn ? Christ Jesus is the one who died — more than that , who was raised — who is at the right hand of God , who indeed is interceding for us .

_Prior classification: **relevant** · related · group=`938-001`_


**vid=28174** — `Rom 11:2`
*target word in verse:* `appeals`

> Rom 11:2 God has not rejected his people whom he foreknew . Do you not know what the Scripture says of Elijah , how he appeals to God against Israel ?

_Prior classification: **relevant** · related · group=`938-001`_


**vid=28173** — `Heb 7:25`
*target word in verse:* `intercession`

> Heb 7:25 Consequently , he is able to save to the uttermost those who draw near to God through him , since he always lives to make intercession for them .

_Prior classification: **relevant** · **anchor** · group=`938-001`_



---

## 4. Other terms in this registry

A pointer-only list of the other terms in this registry, so that
wrong-face set-asides can reference them accurately (VC Instruction §3.6).
**Do not classify these terms here** — each is handled in its own Session A
per-term document.


### Other OWNER terms

| Strong's | Translit. | Gloss | Language |
|---|---|---|---|
| `G1793` | entunchanō | to call on | Greek |
| `G5177` | tunchanō | to obtain/happen | Greek |
| `G5241` | huperentunchanō | to intercede | Greek |
| `H4645` | miph.ga | target | Hebrew |
| `H4645` | miph.ga | target | Hebrew |
| `H6293` | pa.ga | to fall on | Hebrew |
| `H6293` | pa.ga | to fall on | Hebrew |
| `H6294` | pe.ga | chance | Hebrew |
| `H6294` | pe.ga | chance | Hebrew |

### XREF terms (OWNER elsewhere)

| Strong's | Translit. | Gloss | OWNER registry | OWNER word |
|---|---|---|---:|---|
| `G1783` | enteuxis | intercession | — | intercession |
| `G1783` | enteuxis | intercession | 212 | — |
| `G1783` | enteuxis | intercession | 122 | prayer |

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
`mti_term_id = 938`. On apply, Claude Code flips
this term's `mti_terms.vc_status` to `complete` and re-derives the
owning registry's `verse_context_status` from the aggregate of all
its OWNER + XREF-via-OWNER term statuses (VC-2 in the applicator;
alignment analysis v4 §8.2).

*End of Session A prose for term G1793
(094 intercession).*
