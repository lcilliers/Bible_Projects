# Session A — Term `G1381` *dokimazō* — to test

**Registry:** 020 character  
**mti_term_id:** 4841  
**Language:** Greek  
**md_version:** `v1`  ⚠ the patch's `_patch_meta.input_versions[4841]` must equal `1` at submission time or the applicator will reject it as stale (A-03 version gate).  
**Generated:** 2026-04-26 09:03  
**Current vc_status:** `not_done`  
**Existing verse_context rows:** 17 active (of 21 verses for this term).  ⚠ Per-verse: emit `insert` for verses with no active row; emit `update` for verses with an active row being revised. See v3_5 §2.1–§2.4 and §6.1. The per-verse state is shown in the Verses section below.  
**Source:** `data/bible_research.db` (deterministic render, no analytics)  
**Governing instruction:** wa-versecontext-instruction [current]  
**Produced by:** `scripts/build_session_a_prose.py --term`

---

## About this document

This document is the Session A input for **Verse Context classification** of
a single OWNER term — `G1381` *dokimazō* (to test) from registry
020 character. It contains the STEP-sourced data for this one term only.
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


### G1381 · *dokimazō* · to test

- **Language:** Greek
- **mti_term_id:** 4841
- **STEP gloss:** to test
- **Word-analysis gloss:** to test
- **Mounce short def:** testing, trying, examination
- **Occurrence count:** 45

**Parsed senses:**

- `1` testing, trying, examination 
proof, probation, testing,trying, examination, Heb. 3:9*

**Related words:**

- `G0593` *apodokimazō* — to reject
- `G1382` *dokimē* — test
- `G1383` *dokimion* — testing
- `G1384` *dokimos* — tested

**Root family:**

- `DOKIM` (Greek) — test — Backfilled 2026-04-09 from wa_term_related_words clustering

**Data-quality flags (informational):**

- `NO_WORD_ANALYSIS` — meaning field is null for G1381. STEP returned no word analysis block for this term.
- `PROSE_ONLY_MEANING` — Meaning for G1381 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.


---

## 3. Verses

The complete verse corpus for each OWNER term. This is the object of
classification. Every active verse (`delete_flagged = 0`) must be assessed
against the governing filter. Any existing `verse_context` state is shown
per verse as **Prior classification** — review, and revise only where
clearly warranted (VC Instruction §6.2 Step 2).


### G1381 · *dokimazō* — 21 active verse(s)

- **mti_term_id:** 4841
- **Language:** Greek
- **Gloss:** to test
- **Total verses:** 21 (21 active, 0 delete_flagged)
- **Prior verse_context groups:** 2 active

**Existing verse_context groups for this term:**

| group_code | description | state |
|---|---|---|
| `4841-001` | Term names the inner act of moral and spiritual discernment — the mind's tested capacity to distinguish what is genuinely good, true, or pleasing to God | active |
| `4841-002` | Term names the process by which character is tested and proven — trial that discloses the genuine quality of the inner person | active |

**Verses:**

**vid=145503** — `Luk 12:56`
*target word in verse:* `interpret`

> Luk 12:56 You hypocrites ! You know how to interpret the appearance of earth and sky , but why do you not know how to interpret the present time ?


**vid=145504** — `Luk 14:19`
*target word in verse:* `examine`

> Luk 14:19 And another said , ‘I have bought five yoke of oxen , and I go to examine them . Please have me excused .’


**vid=145506** — `Rom 1:28`
*target word in verse:* `see fit`

> Rom 1:28 And since they did not see fit to acknowledge God , God gave them up to a debased mind to do what ought not to be done.


**vid=145509** — `Rom 2:18`
*target word in verse:* `approve`

> Rom 2:18 and know his will and approve what is excellent , because you are instructed from the law ;

_Prior classification: **relevant** · related · group=`4841-001`_


**vid=145507** — `Rom 12:2`
*target word in verse:* `testing`

> Rom 12:2 Do not be conformed to this world , but be transformed by the renewal of your mind , that by testing you may discern what is the will of God , what is good and acceptable and perfect .

_Prior classification: **relevant** · **anchor** · group=`4841-001`_


**vid=145508** — `Rom 14:22`
*target word in verse:* `approves`

> Rom 14:22 The faith that you have , keep between yourself and God . Blessed is the one who has no reason to pass judgment on himself for what he approves .

_Prior classification: **relevant** · related · group=`4841-001`_


**vid=145491** — `1Cor 3:13`
*target word in verse:* `test`

> 1Cor 3:13 each one’s work will become manifest , for the Day will disclose it, because it will be revealed by fire , and the fire will test what sort of work each one has done.

_Prior classification: **relevant** · related · group=`4841-002`_


**vid=145489** — `1Cor 11:28`
*target word in verse:* `examine`

> 1Cor 11:28 Let a person examine himself , then , and so eat of the bread and drink of the cup .

_Prior classification: **relevant** · related · group=`4841-002`_


**vid=145490** — `1Cor 16:3`
*target word in verse:* `accredit`

> 1Cor 16:3 And when I arrive , I will send those whom you accredit by letter to carry your gift to Jerusalem .


**vid=145499** — `2Cor 8:8`
*target word in verse:* `prove`

> 2Cor 8:8 I say this not as a command , but to prove by the earnestness of others that your love also is genuine .

_Prior classification: **relevant** · related · group=`4841-001`_


**vid=145498** — `2Cor 8:22`
*target word in verse:* `tested`

> 2Cor 8:22 And with them we are sending our brother whom we have often tested and found earnest in many matters , but who is now more earnest than ever because of his great confidence in you .

_Prior classification: **relevant** · related · group=`4841-002`_


**vid=145497** — `2Cor 13:5`
*target word in verse:* `Test`

> 2Cor 13:5 Examine yourselves , to see whether you are in the faith . Test yourselves . Or do you not realize this about yourselves , that Jesus Christ is in you ?— unless indeed you fail to meet the test !

_Prior classification: **relevant** · **anchor** · group=`4841-002`_


**vid=145501** — `Gal 6:4`
*target word in verse:* `test`

> Gal 6:4 But let each one test his own work , and then his reason to boast will be in himself alone and not in his neighbor .

_Prior classification: **relevant** · related · group=`4841-001`_


**vid=145500** — `Eph 5:10`
*target word in verse:* `discern`

> Eph 5:10 and try to discern what is pleasing to the Lord .

_Prior classification: **relevant** · **anchor** · group=`4841-001`_


**vid=145505** — `Phili 1:10`
*target word in verse:* `approve`

> Phili 1:10 so that you may approve what is excellent , and so be pure and blameless for the day of Christ ,

_Prior classification: **relevant** · related · group=`4841-001`_


**vid=145494** — `1Th 2:4`
*target word in verse:* `approved`

> 1Th 2:4 but just as we have been approved by God to be entrusted with the gospel , so we speak , not to please man , but to please God who tests our hearts .

_Prior classification: **relevant** · **anchor** · group=`4841-002`_


**vid=145495** — `1Th 5:21`
*target word in verse:* `test`

> 1Th 5:21 but test everything ; hold fast what is good .

_Prior classification: **relevant** · related · group=`4841-001`_


**vid=145496** — `1Ti 3:10`
*target word in verse:* `tested`

> 1Ti 3:10 And let them also be tested first ; then let them serve as deacons if they prove themselves blameless .

_Prior classification: **relevant** · related · group=`4841-002`_


**vid=145502** — `Heb 3:9`
*target word in verse:* `test`

> Heb 3:9 where your fathers put me to the test and saw my works for forty years .

_Prior classification: **relevant** · related · group=`4841-002`_


**vid=145493** — `1Pe 1:7`
*target word in verse:* `tested by`

> 1Pe 1:7 so that the tested genuineness of your faith —more precious than gold that perishes though it is tested by fire —may be found to result in praise and glory and honor at the revelation of Jesus Christ .

_Prior classification: **relevant** · related · group=`4841-002`_


**vid=145492** — `1Jo 4:1`
*target word in verse:* `test`

> 1Jo 4:1 Beloved , do not believe every spirit , but test the spirits to see whether they are from God , for many false prophets have gone out into the world .

_Prior classification: **relevant** · related · group=`4841-001`_



---

## 4. Other terms in this registry

A pointer-only list of the other terms in this registry, so that
wrong-face set-asides can reference them accurately (VC Instruction §3.6).
**Do not classify these terms here** — each is handled in its own Session A
per-term document.


### Other OWNER terms

| Strong's | Translit. | Gloss | Language |
|---|---|---|---|
| `G1382` | dokimē | test | Greek |
| `G1383` | dokimion | testing | Greek |
| `G1384` | dokimos | tested | Greek |

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
`mti_term_id = 4841`. On apply, Claude Code flips
this term's `mti_terms.vc_status` to `complete` and re-derives the
owning registry's `verse_context_status` from the aggregate of all
its OWNER + XREF-via-OWNER term statuses (VC-2 in the applicator;
alignment analysis v4 §8.2).

*End of Session A prose for term G1381
(020 character).*
