# Family analysis — `rest-stillness-peace` (Psalms), in isolation

> Source: `outputs/data/psalms-family-base-sources/psalms__rest-stillness-peace.json` only. Method: `verse-analysis/psalms/_family-analysis-method-20260711.md`. Scope strictly this one file. Citations = `reference · span · Dnnn(label)`.
> Counts (meta): **9 meanings · 10 instances · 8 passages.** All genre `poetic/wisdom`; all `role`(D115)=`characteristic`.

Instance roster (span · ref · lemma:meaning · D102 type · cluster):

| span | ref | meaning | D102 | cluster |
|---|---|---|---|---|
| 278067 | Psa 39:2 | H0481:mute | state | null |
| 278132 | Psa 39:9 | H0481:mute | volition | null |
| 272870 | Psa 131:2 | H7737:calm | action | null (cand. T2) |
| 272323 | Psa 120:7 | H7965:peac | disposition | M33 Peace |
| 272871 | Psa 131:2 | H1826:quiet | action | M33 Peace |
| 285328 | Psa 94:13 | H8252:rest | state | M33 Peace |
| 306385 | Psa 55:6 | H7931:rest | status | null |
| 280101 | Psa 55:18 | H7965:safety | status | M33 Peace |
| 276902 | Psa 32:3 | H2790:silent | state | M33 Peace |
| 282846 | Psa 76:8 | H8252:still | response | M33 Peace |

---

## 0. Data-integrity screen (done first)

**0.1 D112(coupling)/D116(locus) field-swap.** Correct order = D116 a code (`internal:`/`external:`), D112 a phrase. **Four instances are transposed** — D112 holds the code `internal:ib-state` and D116 holds a prose phrase:
- `Psa 131:2 · span 272870 · D116(locus)="paired with quieting the soul"` / `D112(coupling)="internal:ib-state"` — SWAPPED.
- `Psa 120:7 · span 272323 · D116="paired with their bent for war"` / `D112="internal:ib-state"` — SWAPPED.
- `Psa 131:2 · span 272871 · D116="paired with calming the soul"` / `D112="internal:ib-state"` — SWAPPED.
- `Psa 94:13 · span 285328 · D116="paired with the pit dug for the wicked"` / `D112="internal:ib-state"` — SWAPPED.

Read corrected: these four have **locus = `internal:ib-state`** and **coupling = the prose phrase**. The other six are in correct order (D116 a code, D112 a phrase/flag): spans 278067, 278132, 306385, 280101, 276902 (locus `internal:ib-state`), and 282846 (locus `external:god`).

**0.2 Self-loop "edges" (not network links).** Every `flag`+`inferred` (and the one such `event`) edge whose `to_span` = the span's own id is a self-loop, discarded from the network:
- D105(bearer) self-loop on **all 10** instances (`from_span:null → to_span = own id`).
- D107(target) inferred self-loop on 278067, 278132, 272870, 272323, 272871, 285328, 276902.
- D112(coupling) inferred self-loop (flag) on 278067, 278132, 272870, 272323, 272871, 285328, 276902.
- D106(operation) inferred self-loop on `Psa 55:6 · span 306385`.
- D108(manner) inferred self-loop on `Psa 76:8 · span 282846`.

Genuine `pair`/`span` edges only (§1 network below): three spans, four edges — 306385, 280101, 282846.

**0.3 Seat(D104)/manner(D108)="none".**
- **D104 seat = "none" on all 10/10** — the interior seat is never named in this family.
- **D108 manner = "none" on 9/10**; the sole filled manner is `Psa 76:8 · span 282846 · D108(manner)="hushed by dread"` (inferred).

**0.4 Absent dimensions (across all 10 instances).** Never present in any ledger: **D103 source · D109 intensity · D110 specifier · D111 effect · D113 prohibition.** Note D103 source is wholly absent — "what moves it" is never derivable here.

**0.5 Cluster null / T2.** Not typed by an M-cluster:
- `H0481:mute` — cluster `null` (both `Psa 39:2 · 278067`, `Psa 39:9 · 278132`).
- `H7737:calm` — code `null`, `all_candidates="T2(Supplementary)"` (`Psa 131:2 · 272870`). Per the T2-reference rule this is a qualifier-grade candidate, not a standalone cluster.
- `H7931:rest` — cluster `null` (`Psa 55:6 · 306385`).
The remaining six carry **M33 (Peace)**: 272323, 272871, 285328, 280101, 276902, 282846.

---

## 1. Coherence — does the label fit its data?

**Partial fit; the keyword grouping has fused ≥4 distinct inner-being movements.** A genuine rest/peace/self-quieting core exists, but "silence/stillness" surface-words have pulled in movements of opposite or non-IB character. The distinct movements:

**(A) Deliberate self-stilling of the soul** — the active settling of the restless interior. `Psa 131:2 · span 272870 · D101="calm (shavah)" · D102 action · D106="calm the soul"`; `Psa 131:2 · span 272871 · D101="quiet (damam)" · D102 action · D106="quiet the soul"`; D114 (272870): "the active work of settling the restless self." This is the label's true centre.

**(B) Peace / safety as a disposition or granted state** — `Psa 120:7 · span 272323 · D101="peace (shalom)" · D102 disposition · D106="be for peace"`; `Psa 55:18 · span 280101 · D101="safety / peace (shalom)" · D102 status` (peace as fruit of redemption, D114); `Psa 94:13 · span 285328 · D101="rest (shaqat)" · D102 state · D106="be given rest"` (rest God grants the disciplined, D114). Fits the label.

**(C) Longing for rest / escape** — not possession but ache: `Psa 55:6 · span 306385 · D101="be at rest / settle (shakan)" · D102 status · D106="long to rest / dwell in peace"`; D114: "the ache for peace… not mere escape but rest." Fits the label as *desire*, not state.

**(D) Failed / destructive silence — the ANTI-rest movement.** Same "silence" surface, opposite valence: silence that corrodes rather than settles. `Psa 32:3 · span 276902 · D101="kept silent, my bones wasted" · D106="concealment corroding the body"`, D114: "the interior, refusing to speak, rots itself"; `Psa 39:2 · span 278067 · D101="I was mute, and my distress grew worse" · D106="the failure of forced silence"`, D114: "bottling the words… inflamed it." These are grouped by keyword but are the **negation** of rest — a first-class coherence flaw.

**(E) Submissive silence before God** — distinct again: `Psa 39:9 · span 278132 · D102 volition · D106="silent submission to God's dealing"`, D114 explicitly contrasts it with the tongue-guard.

**(F) The earth's dread-hush (non-human-IB).** `Psa 76:8 · span 282846 · D105(bearer)="the earth / its inhabitants" · D102 response · D108="hushed by dread" · D116(locus)="external:god"`; D114: "the silence of awe… dread expressed not as clamour but as quiet." Bearer is not the human IB and locus is external:god — this instance sits outside the study's inner-being lens (Screen 0), included only by the "still" keyword.

Verdict: the label names **movement (A)+(B)+(C)** correctly (six instances) but silence-keyword capture has fused in **(D) anti-rest silence** (276902, 278067), **(E) submissive silence** (278132), and **(F) a non-IB awe-hush** (282846). The family is a keyword band, not one coherent movement.

---

## 2. The movements/operations evidenced (all instances, cited)

**Self-quieting (2).** `Psa 131:2 · 272870 · D106="calm the soul"` and `· 272871 · D106="quiet the soul"`, both D102 action, D107(target inferred) "from craving" / "into stillness". The one place the family shows the IB *acting on itself* toward rest. Coupled to each other in prose (corrected D112 phrases "paired with quieting/calming the soul") but **not** as a genuine span-edge (see §3).

**Peace held / granted (3).** Disposition `Psa 120:7 · 272323 · D106="be for peace" · D107="toward the hostile"`, set against foes' "bent for war" (corrected D112). Granted rest `Psa 94:13 · 285328 · D106="be given rest" · D105="the disciplined man" · D107="from days of trouble"`. Redemption-peace `Psa 55:18 · 280101 · D101 safety/shalom · D106="none"` (operation not derivable — status only), coupled (D112 pair) to "the peace in which the soul is redeemed."

**Longing for rest (1).** `Psa 55:6 · 306385 · D106(inferred)="long to rest / dwell in peace" · D107="none"`; passage-anchor (`is_passage_anchor:true`). Rest as unattained object of desire.

**Silence that harms (2).** `Psa 32:3 · 276902 · D106="concealment corroding the body" · D107="concealment's-cost"`; `Psa 39:2 · 278067 · D106="the failure of forced silence" · D107="silence's-failure"`. Operations of restraint backfiring.

**Silence as submission (1).** `Psa 39:9 · 278132 · D106="silent submission to God's dealing" · D107="submissive-silence" · D102 volition`.

**Awe-hush (1, non-IB).** `Psa 76:8 · 282846 · D106="fall silent / be quieted" · D107(pair)="before God's judgment" · D108="hushed by dread"`.

Type spread (D102): state ×3 (278067, 285328, 276902), status ×2 (306385, 280101), action ×2 (272870, 272871), disposition ×1 (272323), volition ×1 (278132), response ×1 (282846). No single ontological type dominates — consistent with a fused family.

---

## 3. The network (genuine `pair`/`span` edges only)

Only three spans carry real edges, four edges total, and **every target lies outside this file's 10 master spans** — so there are **no intra-family links**; the network points entirely outward and is sparse/one-directional:

- `Psa 55:6 · span 306385 · D112(coupling) → span 306384` ("the goal of the longed-for flight") — links the rest-longing to the (external) flight span.
- `Psa 55:18 · span 280101 · D112(coupling) → span 280100` ("the peace in which the soul is redeemed") — links safety to its (external) redemption span.
- `Psa 76:8 · span 282846 · D107(target) → span 282842` ("before God's judgment") and `· D112(coupling) → span 282845` ("paired with the earth's fear") — links the hush to God's judgment and to the earth's fear.

No edge connects any two of the ten family instances to one another; the self-stilling pair (272870/272871), though prose-coupled, has **no span-edge** between them. Network within the family = empty.

---

## 4. The interior anatomy the data actually names

- **Seat (D104): never named** — "none" on all 10. Though "soul" surfaces in the read text (`Psa 131:2`, `Psa 55:18`), it is not coded into a seat; the interior locus is asserted only generically.
- **Locus (D116, corrected): `internal:ib-state` on 9/10** (272870, 272323, 272871, 285328 after swap-correction; plus 278067, 278132, 306385, 280101, 276902); **`external:god` on 1** (`Psa 76:8 · 282846`).
- **Bearer (D105): the psalmist on 8** (incl. "the psalmist (longing)" 306385, "the psalmist (his soul)" 280101); **"the disciplined man"** `Psa 94:13 · 285328`; **"the earth / its inhabitants"** `Psa 76:8 · 282846` (non-human IB). All bearer values are `inferred`.
- **Manner (D108): only one filled** — "hushed by dread" (`Psa 76:8 · 282846`), inferred.
- The named interior motion is almost entirely **operation (D106) + target (D107)**; there is no named **source (D103)**, **intensity (D109)**, **specifier (D110)**, **effect (D111)** or **prohibition (D113)** anywhere.

---

## 5. What could not be derived (flagged)

- **What moves rest/peace (D103 source): unknown** — D103 absent on all 10. The cause/impetus of stilling is never coded.
- **Intensity (D109), specifier (D110), effect (D111), prohibition (D113): none** across all instances — degree, sub-typing, downstream effect and any prohibitive framing are not derivable from this source.
- **Seat (D104): unstated on all 10** — no heart/soul/ruach seat is coded, only inferred generic "internal."
- **Operation for `Psa 55:18 · 280101`: "none"** — safety is coded status-only; its verb is not derivable. Target "none" also on 280101 and on `Psa 55:6 · 306385`.
- **Four swapped D112/D116 records** (272870, 272323, 272871, 285328) — read corrected above; the raw file cannot be trusted field-labelled at those spans.
- **`Psa 76:8 · 282846` bearer is non-human ("the earth")** and locus external:god — its inclusion is keyword-driven; it does not evidence the human inner being and should not be read as a rest/peace IB-movement.
- **No intra-family network** — every genuine edge exits the ten-span set; relations among these instances are not derivable from the edges (only from prose D114/D112 phrases).
- **Three meanings untyped by cluster** (mute ×2, calm-T2, rest-H7931); the term-cluster cannot place them under M33.

---

## Summary

Nine meanings / ten instances, all `poetic/wisdom`, all role=characteristic. The `rest-stillness-peace` label genuinely names a **self-stilling + peace-held/granted + rest-longing** core (272870, 272871, 272323, 285328, 280101, 306385) but the silence keyword has **fused in three foreign movements**: destructive/failed silence that is the *anti-rest* (276902, 278067), submissive silence (278132), and a **non-IB** earth-hush of dread (282846). Interior anatomy is thin — seat never named, source/intensity/specifier/effect/prohibition wholly absent, manner filled once. Four instances have transposed D112/D116 (read corrected); the network is empty within the family (all real edges exit the set).
