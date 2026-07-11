# Family analysis — `confession-forgiveness` (Psalms), in isolation

> Source: `outputs/data/psalms-family-base-sources/psalms__confession-forgiveness.json` only. Method: `_family-analysis-method-20260711.md`. Every claim cites `reference · span_id · Dnnn(label)`. British spelling. Nothing imported from outside the file.

**Scope counts (meta.counts):** 3 meanings · 3 instances · 3 passages. Each meaning has exactly one instance, so the family is three single spans:

| span_id | ref | lemma | meaning | cluster | outlier? | type (D102) |
|---|---|---|---|---|---|---|
| 276927 | Psa 32:5 | H3034 | confess | M22 Praise | **yes** | volition |
| 277935 | Psa 38:18 | H5046 | confess | M42 Speech | **yes** | cognition |
| 275962 | Psa 25:11 | H5545 | pardon | M11 Repentance | no | cognition |

---

## 0. Data-integrity screen (done first)

**D112(coupling) / D116(locus) swap — NONE swapped.** In all three spans D116 holds the code and D112 holds the phrase, i.e. the *correct* order per method:
- `Psa 32:5 · span 276927 · D116 locus = "internal:ib-state"` (code) / `D112 coupling = "acknowledge-confess"` (phrase).
- `Psa 38:18 · span 277935 · D116 locus = "internal:ib-state"` / `D112 coupling = "confess-and-sorry"`.
- `Psa 25:11 · span 275962 · D116 locus = "internal:ib-state"` / `D112 coupling = "pardon-great-guilt"`.
No instance requires correction.

**Self-loop "edges" — ALL edges are self-loops; the network is empty.** Every one of the nine `edges` entries (three per span, on D105 bearer, D107 target, D112 coupling) is `item_type:"flag"`, `resolution:"inferred"`, `from_span:null`, `direction:null`, and `to_span` equal to the span's own id (e.g. `Psa 32:5 · span 276927 · D105 bearer → to_span "276927"`). By the method these are self-loops, **not** network edges. There is **not one** `pair` edge (`resolution:"span"`) to a different span anywhere in the file. → **Zero genuine inner-being links.**

**seat(D104) / manner(D108) = "none":** unfilled in **3/3** instances each — `span 276927·D104`, `span 277935·D104`, `span 275962·D104` all `"none"` (flag); likewise `·D108` all `"none"` (flag). No interior seat and no manner is named anywhere.

**Absent dimensions (across all 3 instances):** D109 intensity, D110 specifier, D111 effect, D113 prohibition are absent — as the method anticipates. **Additionally D103 source is absent** from every lexical ledger (not in the method's expected-absent list, so flagged here). Present dimensions everywhere: 101,102,104,105,106,107,108,112,114,115,116.

**Cluster NULL / T2:** none. No null and no T2 cluster. But two of three are flagged `is_outlier:true` (see §1).

**Further integrity note — H5046 evidence/instance mismatch:** the meaning record `H5046:confes` carries `evidence.stems:null` and `evidence.morph_codes:null`, yet its single instance `Psa 38:18 · span 277935` carries `morphology.morph_code:"HVhi1cs", stem:"Hiphil"` (identical to H3034's). The aggregate evidence and the instance disagree; the morphology is derivable only from the instance.

---

## 1. Coherence — does the label fit its data?

**The confession pole is coherent; the forgiveness pole is NOT coded as an IB characteristic.** All three read-senses are one movement — the penitent turn of the interior naming its own guilt:
- `Psa 32:5 · span 276927 · D101 sense` = "I confessed and did not cover it";
- `Psa 38:18 · span 277935 · D101 sense` = "I confess my iniquity, I am sorry for my sin";
- `Psa 25:11 · span 275962 · D101 sense` = "pardon my guilt, for it is great".

But **no span bears "forgiveness" as its characteristic**. The pardon span (H5545, `span 275962`) is the human's *plea* for pardon (`D115 role = characteristic`, `D106 operation` = "the self asks pardon for its guilt… confession without minimising") — it is still the confessing side, not forgiveness enacted. Forgiveness itself appears only inside operation/discovery prose as **God's** act, contextual, never coded: `Psa 32:5 · span 276927 · D106 operation` = "…and God forgave — the decisive turn"; `D114 discovery` = "…and you FORGAVE the iniquity of my sin". → The family name pairs two poles but the data supplies only the human confession pole; "forgiveness" is the arena/response, not a coded inner-being characteristic (consistent with the IB-screen: God's action is the arena, not the IB point).

**Term-cluster fusion — the keyword grouping over-rides term typing.** The meaning-family "confession-forgiveness" expects M11(Repentance), yet the term-clusters scatter:
- `span 276927` (H3034) → **M22(Praise)**, `outlier_note`: expects M11 but term-cluster is M22 — H3034's `lexical_gloss` = "to give thanks", so the lemma types toward praise/thanksgiving, not repentance.
- `span 277935` (H5046) → **M42(Speech)**, `outlier_note`: expects M11 but M42 — H5046's `lexical_gloss` = "to tell", typing toward speech/telling.
- `span 275962` (H5545) → **M11(Repentance)**, non-outlier, `lexical_gloss` = "to forgive".

So the family is a **read-sense grouping (all read "confess/pardon") that fuses three lexically distinct lemmas** whose own clusters are Praise, Speech and Repentance. Only 1/3 sits in the expected cluster. The coherence is at the level of the *reader's sense* (D101/D114), not at the term-cluster level.

---

## 2. The movements evidenced (cited, per instance)

Three parallel single-span movements, all `D116 locus = internal:ib-state`, all `D115 role = characteristic`, all `D105 bearer = "the psalmist"` (flag, `resolution:inferred`), all `genre = poetic/wisdom`, none a passage anchor (`is_passage_anchor:false`).

**(a) The confessing turn — `Psa 32:5 · span 276927` (H3034, M22 Praise).**
`D102 type = volition`; `D106 operation`(event) = "the self acknowledged its sin, did not cover its iniquity, resolved to confess — and God forgave — the decisive turn"; `D107 target`(flag,inferred) = "confessing-turn"; `D112 coupling` = "acknowledge-confess". `D114 discovery` reads it as "the hinge of the psalm: the interior stops hiding and speaks, and forgiveness follows at once." → an act of **will** (volition): the interior chooses to stop covering and speak.

**(b) The penitent turn — `Psa 38:18 · span 277935` (H5046, M42 Speech).**
`D102 type = cognition`; `D106 operation`(event) = "the self confesses its iniquity and is sorry for its sin — penitence spoken and felt"; `D107 target`(flag,inferred) = "penitence"; `D112 coupling` = "confess-and-sorry". `D114 discovery`: "the interior names its guilt and grieves it, not merely its consequences." → naming + sorrow: penitence both spoken and felt.

**(c) Unflinching confession — `Psa 25:11 · span 275962` (H5545, M11 Repentance).**
`D102 type = cognition`; `D106 operation`(event) = "the self asks pardon for its guilt, honestly owning that it is great — confession without minimising"; `D107 target`(flag,inferred) = "honest-confession"; `D112 coupling` = "pardon-great-guilt". `D114 discovery`: "the interior does not shrink the sin but names it great and appeals to God's name." → confession that refuses to minimise; the plea rests on God's name, not the self's merit.

**Cross-cutting shape (from the filled fields only):** the interior's movement is *stop-hiding → name the guilt → grieve/own it → appeal to God*. Type splits volition (1) vs cognition (2); no instance is coded affect/faculty/disposition, though sorrow is described in the D106/D114 prose of (b).

---

## 3. The network

**Empty.** No genuine `pair` edge exists (§0). All nine edges are inferred self-loop flags (D105/D107/D112 pointing to the span's own id with `from_span:null`). The three spans are **not** linked to each other or to any other span in this file. The family is three isolated points, not a connected sub-web — expected, since each meaning holds a single span and the spans sit in three different passages (1623, 1635, 1614).

---

## 4. The interior anatomy the data actually names

Assembling only the *filled* seats/sources/couplings:
- **Seat (D104):** none named — the interior organ (heart/soul/spirit) is unstated in all 3 (though passage text mentions "heart", "bones", "soul", none is coded onto these spans).
- **Source (D103):** absent entirely — what moves the confession is uncoded.
- **Locus (D116):** uniformly `internal:ib-state` — all three are placed inside the inner being as a state.
- **Bearer (D105):** uniformly "the psalmist" (inferred) — the human IB, first person.
- **Operation (D106):** the only richly filled dimension — the confessing/penitent turn (three prose events, §2).
- **Target (D107):** the confessing act itself ("confessing-turn" / "penitence" / "honest-confession") — the movement is reflexive: it targets its own turning, not an external object.
- **Coupling (D112):** each binds confession to a partner element — acknowledge↔confess, confess↔sorrow, pardon↔great-guilt.

Named interior anatomy is therefore **thin**: locus + bearer + operation + reflexive target + coupling. Seat, source, manner, intensity, specifier, effect and prohibition are all unnamed.

---

## 5. What could not be derived from this source

- **Any inner-being network** — no `pair` edges; connectivity between the three confession spans is not derivable.
- **The forgiveness pole as an IB characteristic** — present only as God's contextual act in D106/D114 prose; no span codes it (`role`/`operation` are always the human confessing side).
- **Seat (D104)** for all 3 — where in the interior the confession sits is unstated.
- **Source (D103), manner (D108), intensity (D109), specifier (D110), effect (D111), prohibition (D113)** — absent across all 3; the force, mode, degree and consequence of confession are not coded.
- **Term-cluster coherence** — cannot be asserted; 2/3 spans are outliers (M22 Praise, M42 Speech) against the expected M11 Repentance (§1).
- **H5046 stem/morph from the aggregate record** — `evidence.stems`/`morph_codes` are null; recoverable only from the instance (HVhi1cs, Hiphil), an internal inconsistency.

---

## Summary

`confession-forgiveness` = 3 meanings / 3 instances (Psa 25:11 · 32:5 · 38:18), all first-person penitent confession coded `internal:ib-state`, `role=characteristic`, bearer "the psalmist" (inferred). The **confession pole is coherent** but the **forgiveness pole is never coded** (God's act, prose-only), and the grouping **fuses three lexically distinct lemmas** — 2/3 are cluster outliers (M22 Praise, M42 Speech vs expected M11 Repentance). No D112/D116 swap; **no genuine network edges** (all self-loops); seat, source, manner and D109–D113 all unfilled. The only richly filled dimension is D106 operation — the interior's decisive turn to stop hiding and name its guilt.
