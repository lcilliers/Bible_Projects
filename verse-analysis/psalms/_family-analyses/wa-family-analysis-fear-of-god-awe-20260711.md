# Family analysis (in isolation) — `fear-of-god-awe` (Psalms)

> Source: `verse-analysis/psalms/_base-sources/psalms__fear-of-god-awe.json` (only). Scope: **24 meanings · 79 instances · 61 passages**, all genre `poetic/wisdom`. Every claim cites `reference · span_id · Dnnn(label)` into that file. Nothing imported from outside it.

---

## 0. Data-integrity screen

**D112(coupling)/D116(locus) field-swap — 24 of 79 instances transposed.** Correct order is D116 = a code, D112 = a phrase. In 24 instances D112 holds the `internal:`/`external:` code and D116 holds the prose phrase — read them corrected. The swapped instances (D112 code → true locus; D116 phrase → true coupling):
`Psa 103:11·269074`, `Psa 103:13·269090`, `Psa 103:17·269115`, `Psa 111:5·270603`, `Psa 112:1·270647`, `Psa 115:11·270836`, `Psa 115:13·270854`, `Psa 118:4·271157`, `Psa 128:1·272650`, `Psa 128:4·272666`, `Psa 135:20·273105`, `Psa 102:15·268931`, `Psa 118:6·271172`, `Psa 130:4·272821`, `Psa 91:5·285133`, `Psa 112:7·270696`, `Psa 112:8·270707`, `Psa 111:10·270572`, `Psa 105:38·269490`, `Psa 105:23·307386`, `Psa 120:5·307783`, `Psa 105:12·307358`, `Psa 96:9·285618`, `Psa 99:1·285792` — all `D112(coupling)`/`D116(locus)`. The other 55 are in correct order (phrase in D112, code — or `none` — in D116). **All 79 carry both fields; none is missing.** Corrected locus distribution: **external:god = 36, internal:ib-state = 43**.

**Self-loop "edges" — 216 of 251 edges are non-edges.** The `edges` arrays total 251 rows: `flag`=201, `event`=15, `pair`=35. Every `flag` (all `resolution:inferred`) and every `event` has `from_span:null` and `to_span` = the span's **own id** (string-typed) — e.g. `Psa 103:11·269074` bearer/target/coupling flags all point `to_span:"269074"`. These 216 are self-referential markers (bearer D105, target D107, coupling D112, source D103, operation D106, manner D108 self-attributions), **not** network links. Only the **35 `pair`/`resolution:span`** edges link to a *different* span and constitute the genuine network (§ Network).

**seat(D104)/manner(D108) = "none".** D104 seat = `none` in **all 79** instances — the interior seat is never filled. D108 manner = `none` in **70**; only **9** are filled (all inferred or span-derived): `Psa 60:4·280818` "fleeing to the banner", `Psa 46:2·279047` "though the earth give way", `Psa 49:5·279384` "in times of trouble", `Psa 72:5·282322` "while the sun endures…", `Psa 76:8·282845` "struck silent", `Psa 51:5·279750` "in iniquity, from conception", `Psa 61:4·280877` "forever", `Psa 53:5·279928` "great, such as has never been", `Psa 55:4·280184` "of death" — all `D108(manner)`.

**Absent dimensions (across all 79).** `D109 intensity`, `D110 specifier`, `D111 effect` appear on **no** instance. `D113 prohibition` appears filled on only **3**: `Psa 46:2·279047` "negated", `Psa 49:5·279384` "rhetorically none", `Psa 49:16·279331` "deprecated" — all `D113(prohibition)`; absent on the other 76. `D103 source` filled on only **6** (Psa 60:4, 46:2, 55:19, 67:7, 65:8, 53:5).

**Cluster NULL / crossover.** `cluster.code = null` (all_candidates `T2(Supplementary)`) on the 2 `H0935:enter` instances: `Psa 143:2·273887`, `Psa 5:7·280730` — the term-cluster cannot type them. Two flagged **outliers** (genuine non-adjacent crossover): `Psa 25:14·275980` `H5475:friendship` → M17(Counsel); `Psa 15:4·274642` `H3513:honor` → M22(Praise). Two more sit in **M03(Grief)** un-flagged: `Psa 51:5·279750` `H2342:broughtforth`, `Psa 96:9·285618` `H2342:trembl`. Remaining 73 = M01(Fear).

**Role (D115).** Uniform: **characteristic** on all 79. No qualifier/standalone rows.

**Bearer (D105).** Inferred on all 79 — no bearer is text-explicit at the field level.

---

## 1. Coherence check — the label only partly fits its data

`fear-of-god-awe` is a **keyword grouping that fuses one coherent affect-axis with several lexical/co-text crossovers**. The coherent core (the genuine fear/awe axis, ~69 instances) is itself **tri-polar**, and ~8–10 instances are **not fear at all**, pulled in because their verse *contains* fear-of-God language or because the lemma is a homograph of a dread-root.

**Coherent core — the fear axis (three poles):**
- **(A) Reverent fear / awe of God** — the label's proper referent. `yare`/`yirah`/`pachad`(awe): `Psa 103:11·269074 · D101(sense)="fear (yare)"`, `Psa 111:10·270572 · D101` "fear of the LORD is the beginning of wisdom", `Psa 19:9·275331 · D101` "the fear of the LORD, clean", `Psa 34:9·277284 · D106(operation)` "fear the LORD, you his saints", `Psa 22:23·275679 · D102(type)=volition` summoning God-fearers to praise, `Psa 65:8·281231 · D101` "in awe at your signs", `Psa 119:161·271599 · D101` "stand in awe (pachad)". Types disposition/affect/status; corrected locus **external:god**.
- **(B) Fearlessness / fear refused** — the *negation* of A, dread dissolved by trust/presence: `Psa 23:4·275829 · D101` "I will fear no evil", `Psa 27:1·276198 · D101` "whom shall I fear", `Psa 46:2·279047 · D113(prohibition)="negated"`, `Psa 3:6·278184 · D106`, `Psa 56:4·280285`/`Psa 56:11·280238 · D112(coupling)` "not afraid", `Psa 91:5·285133`, `Psa 112:7·270696`/`Psa 112:8·270707`, `Psa 118:6·271172`, `Psa 78:53·283302`, `Psa 49:16·279331 · D113="deprecated"`. Types affect/state/action; locus **internal:ib-state**. This is the opposite movement to A under the same keyword.
- **(C) Dread / terror / trembling (affliction pole)** — raw panic and its somatic register, *not* reverence: `Psa 55:4·280184 · D101` "terrors (emah) of death", `Psa 31:13·276699 · D106` "terror on every side", `Psa 64:1·281096 · D101` "dread (pachad) of the enemy", `Psa 53:5·279928 · D101` "great terror", `Psa 105:38·269490 · D101` "dread (pachad)" of the Egyptians, `Psa 78:33·283155 · D101` "terror (behalah)", `Psa 119:39·271820 · D101` "dread (yagor)"; trembling: `Psa 48:6·279231 · D101` "trembling (raad)", `Psa 55:5·280190 · D101`, `Psa 96:9·285618 · D101` "tremble (chul)", `Psa 99:1·285792 · D101` "tremble (ragaz)". Locus **internal:ib-state**.

**Fused-in — not the fear/awe movement (crossover ~8):**
- **Sojourning/dwelling (`gur`, homograph of "to dread")** — read as *stranger status*, no fear content: `Psa 105:12·307358 · D101` "sojourners (gur)", `Psa 105:23·307386 · D101` "sojourned", `Psa 120:5·307783 · D101` "sojourn", `Psa 61:4·280877 · D101` "dwell/sojourn (gur) in your tent". Lemma H1481 gloss = "to dread; to sojourn; to quarrel" — the fear-sense drew them in; the read took the sojourn-sense.
- **Birth-in-iniquity (`chul`)** — `Psa 51:5·279750 · D101` "brought forth in iniquity" (M03 Grief); a homograph of the writhe/tremble root, read as *birth/innate sin*, not fear.
- **enter/come (`bo`, cluster null)** — `Psa 143:2·273887 · D101` "confession of unworthiness / Enter not into judgment" — pulled by co-text ("judgment"), no fear content. (Its sibling `Psa 5:7·280730` "enter to bow in the fear of God" *does* belong to pole A — reverent worship.)
- **Co-text outliers** — `Psa 25:14·275980 · D101` "the friendship (sod) of the LORD" and `Psa 15:4·274642 · D101` "honours the God-fearers": the master word is friendship/honour; only the *object* ("those who fear him") touches the family.

**Finding:** the family is not one movement. It is A (reverent fear, external:god) **plus its own negation** B (fearlessness, internal) **plus** C (affective terror/trembling, internal) — three genuine but distinct fear-movements — **plus** a homograph/co-text tail (gur/chul/bo/friendship/honour) that is not fear at all. Any synthesis must keep A, B, C separate and exclude the tail.

---

## 2. The movements evidenced (grounded)

**M2.1 — Reverent fear as a durable disposition and communal identity.** The dominant lemma `H3373` (23 inst) reads the God-fearers as a *class* on whom God's goods rest: `Psa 103:11·269074 · D102(type)=disposition · D106(operation)="fear / revere" · D107(target)="God"[inferred]`, coupled (corrected) to "God's great steadfast love" (`D112`); likewise compassion `Psa 103:13·269090`, everlasting love `Psa 103:17·269115`, provision `Psa 111:5·270603`, blessing `Psa 115:13·270854`. Fear is the *root* of the blessed/flourishing life: `Psa 112:1·270647 · D116(locus, corrected)` "delighting in his commandments"; `Psa 128:1·272650`/`Psa 128:4·272666`. It is the ground of wisdom: `Psa 111:10·270572 · D114(discovery)` "the fear of the LORD is the beginning of wisdom". It is *clean and enduring*, named as a state of the interior itself: `Psa 19:9·275331 · D101(sense)="the fear of the LORD, clean" · D102=affect`.

**M2.2 — Reverent fear draws divine response.** The operation repeatedly ties fear to what God *does back*: instruction `Psa 25:12·275969 · D106`, hoarded goodness `Psa 31:19·276748 · D106`, the watching eye `Psa 33:18·277043 · D106` "the eye of the LORD is on those who fear him", desire fulfilled and cry heard `Psa 145:19·274113 · D106`, God's pleasure `Psa 147:11·274288 · D106` "the LORD takes pleasure in those who fear him", nearness of salvation `Psa 85:9·284242 · D116(corrected)`. Forgiveness *produces* fear (not licence): `Psa 130:4·272821 · D114` "with you there is forgiveness, that you may be feared".

**M2.3 — Fear that God is owed by all creation.** Reverence widens from Israel to the nations/earth: `Psa 102:15·268931 · D105(bearer)="the nations"[inferred]`, `Psa 47:2·279097 · D101` "to be feared, a great king", `Psa 67:7·281437 · D103(source)="because God blesses us"[span] · D106`, `Psa 72:5·282322 · D108(manner)` "while the sun endures", `Psa 65:8·281231` awe at his signs, `Psa 64:9·281155 · D101` "then all mankind fears", `Psa 96:9·285618`/`Psa 99:1·285792` "tremble before him, all the earth".

**M2.4 — Fearlessness: the interior refuses dread on God's ground.** Fear is *negated* and the ground named: `Psa 46:2·279047 · D103="grounded in God our refuge and strength (v1)"[span] · D113="negated"`; `Psa 27:1·276198 · D106` "whom shall I fear" (God as light/salvation/stronghold); `Psa 23:4·275829 · D114` "I will fear no evil, for you are with me"; `Psa 118:6·271172 · D116(corrected)` "the LORD on his side"; `Psa 3:6·278184`; `Psa 91:5·285133` "you will not fear the terror of the night". The God-fearer of M2.1 is precisely the one who does not fear news/foes: `Psa 112:7·270696`/`Psa 112:8·270707 · D116(corrected)` "the firm, trusting heart".

**M2.5 — The honest hinge: fear owned, then pivoted into trust.** `Psa 56:3·280274 · D114` "When I am afraid (yare), I put my trust in you" — fear not denied but turned; answered in the same passage by `Psa 56:4·280285` and `Psa 56:11·280238` "I shall not be afraid" (the coupling edges bind v3↔v4, § Network).

**M2.6 — Terror as affliction (the dread pole).** Panic invades body and soul: `Psa 55:4·280184 · D101="terrors (emah) of death" · D108(manner)="of death"` → `Psa 55:5·280189 · D101` "fear (yirah)" → `Psa 55:5·280190` "trembling (raad)" — a triad (terror→fear→trembling) chained by coupling edges. Encircling dread: `Psa 31:13·276699 · D106` "terror on every side". The godless collapse into groundless terror: `Psa 53:5·279928 · D103="because God scatters the bones of the besieger"[span] · D108="great, such as has never been"[span]`. Somatic seizure: `Psa 48:6·279231 · D106="take hold of them"[inferred]` (the fleeing kings).

**M2.7 — Fear absent in the wicked = their sin.** The negation of A as *indictment*, not comfort: `Psa 55:19·280118 · D101="do not fear God" · D105="the enemies (lacking it)"`; `Psa 64:4·281126 · D101` "shooting… without fear" `· D105="the wicked (lacking it)"`.

**M2.8 — Reverent fear enacted as worship-posture.** `Psa 5:7·280730 · D106` "enter your house… bow toward your temple in the fear of you" `· D107(target)="reverent-worship"[inferred]`; `Psa 22:23·275679 · D102=volition` recruits the whole God-fearing community to praise; `Psa 86:11·284260 · D114` "unite my heart to fear your name"; `Psa 119:120·271346 · D114` "my flesh trembles for fear of you".

**M2.9 — Non-fear tail (documented, excluded from the fear synthesis).** Sojourn/dwell `Psa 105:12·307358`, `Psa 105:23·307386`, `Psa 120:5·307783`, `Psa 61:4·280877` (all `D101` gur, read as stranger/pilgrim status); innate-sin `Psa 51:5·279750 · D101` (chul, birth in iniquity); confession `Psa 143:2·273887 · D101`; friendship `Psa 25:14·275980`; honour `Psa 15:4·274642`. Each cited so none is silently dropped.

---

## The network (genuine `pair`/`span` edges only — 35)

All 251 edge-rows minus 216 self-referential flags/events leave **35 genuine cross-span links**; every one has `direction:null` (undirected). They are dominated by **D112(coupling)** links (co-occurring interior states within a passage), with a few D103(source), D107(target), D108(manner). Notable clusters:

- **Ps 56 fear↔trust lattice:** `Psa 56:11·280238 → 280285`, `Psa 56:3·280274 → 280276`, `Psa 56:4·280285 → 280274` (`D112 coupling`) — the fear-owned / fear-refused refrain binding v3↔v4↔v11.
- **Ps 55 terror-triad:** `Psa 55:4·280184 → 280189` (`D112`) and `→ 280185` (`D108 manner`); `Psa 55:5·280189 → 280190` and `280190 → 280189` (`D112`) — terror↔fear↔trembling reciprocally linked.
- **Ps 61 dwelling/heritage:** `Psa 61:4·280877 → 280879` (`D107 target`, `D108 manner`) and `→ 280880` (`D112`); `Psa 61:5·280890 → 280892` (`D107`) and `→ 280886` (`D112`).
- **Ps 76 earth-feared-and-was-still:** `Psa 76:8·282845 → 282842` (`D107 target`), `→ 282846` (`D108 manner` and `D112 coupling`) — fear welded to "was still".
- **Ps 60 disciplined-remnant:** `Psa 60:4·280818 → 280776` (`D103 source`), `→ 280823` (`D112`).
- Single links: `Psa 46:2·279047 → 279024` (`D103` God-refuge), `Psa 49:5·279384 → 279387` (`D107`), `Psa 52:6·279841 → 279842` (`D112`), `Psa 64:1·281096 → 281092` (`D112`), `Psa 64:4·281126 → 281122`, `Psa 64:9·281155 → 281156`, `Psa 65:8·281231 → 281224` (`D103`) `→ 281232` (`D107`), `Psa 66:16·281286 → 281284` (`D112`), `Psa 67:7·281437 → 281433` (`D103`), `Psa 72:5·282322 → 282331` (`D112`), `Psa 51:5·279750 → 279751` (`D108`) `→ 279752` (`D112`), `Psa 53:5·279928 → 279933` (`D103`) `→ 279930` (`D108`), `Psa 48:6·279231 → 279234` (`D112`).

**Network shape:** sparse, undirected, passage-local. It clusters into small in-passage knots (Ps 55, Ps 56, Ps 61, Ps 64) rather than a corpus-wide web; the axis is overwhelmingly **coupling** (interior state co-occurrence), with **source** and **manner** as the causal/adverbial trim. No edge crosses between the reverent-fear pole (A) and the terror pole (C); the poles are linked only within their own passages.

---

## The interior anatomy the data actually names

- **Seat (D104):** unnamed everywhere (`none` × 79). The field carries no heart/soul/spirit/eye value at all.
- **But the read-text (D101/D106/D114) names interior organs the seat field omits:** heart — `Psa 86:11·284260 · D114` "unite my heart", `Psa 112:7·270696 · D116(corrected)` "trusting heart", `Psa 119:161·271599 · D114` "my heart stands in awe"; flesh — `Psa 119:120·271346 · D114` "my flesh trembles". This is a **field/evidence gap**: the anatomy is in the prose, absent from D104.
- **Locus (D116, corrected):** the only filled interior-map dimension — a clean split, **external:god (36)** for reverent/owed fear (bound *to* God) vs **internal:ib-state (43)** for fearlessness, terror, trembling and the non-fear tail (a state *within*).
- **Coupling (D112, corrected):** what fear is bound to — steadfast love / compassion / provision / blessing (pole A), the trusting/steady heart (pole B), fear-trembling-horror (pole C). This is the richest relational dimension.
- **Source (D103, 6):** God as cause on both sides — refuge/strength `Psa 46:2·279047`, blessing `Psa 67:7·281437`, judgment that scatters `Psa 53:5·279928`, discipline `Psa 60:4·280818`, humbling `Psa 55:19·280118`, creation-power `Psa 65:8·281231`.
- **Operation/target (D106/D107):** operation filled widely as "fear / revere" or the read-verb; target is God / God's name / God's word (pole A) or fearlessness / dread-object (poles B, C) — but always **inferred** (self-loop flags, not links).

---

## What could not be derived (from this source)

1. **Interior seat** — D104 never filled (79/79 `none`); the heart/flesh in the prose is not captured at the seat dimension.
2. **Intensity (D109), specifier (D110), effect (D111)** — absent on all 79; no gradation, no sub-typing, no consequence field is recorded (though M2.1–M2.2 read effects like blessing/instruction into D106/D114 prose, they are not typed as D111).
3. **Prohibition (D113)** — recorded on only 3 of the ~13 negated/fearless instances; the fearlessness pole (B) is under-tagged at D113 (e.g. `Psa 23:4`, `Psa 27:1`, `Psa 118:6` carry no D113 though they are refusals of fear).
4. **Source (D103)** — filled on only 6; for most reverent-fear instances *what moves the fear* is left implicit.
5. **Manner (D108)** — 70/79 `none`.
6. **Bearer (D105)** — inferred on all 79; no bearer is field-explicit, so "whose inner being" always rests on the reader's inference (mostly the psalmist, the God-fearers, the nations, or — in the tail — the wicked/Egyptians/kings, i.e. groups).
7. **Cluster typing** — 2 instances untypeable (`cluster.code=null`, T2); 4 sit in non-Fear clusters (M03 Grief ×2, M17 Counsel, M22 Praise). The term-cluster layer does not resolve the homograph/co-text fusion — the reader's D101/D114 do.
8. **Directionality** — every edge `direction:null`; the network gives adjacency, not flow.

---

## Summary

`fear-of-god-awe` (Psalms) = **24 meanings / 79 instances**, all `poetic/wisdom`, role uniformly *characteristic*, seat uniformly unfilled. **The label fuses three distinct fear-movements — reverent fear of God (external:god, 36), fearlessness/fear-refused (internal, ~13), and affliction-terror/trembling (internal, ~20) — plus a homograph/co-text tail (gur sojourn ×4, chul birth, bo enter/confession, friendship, honour) that is not fear at all.** Integrity load: 24 D112/D116 field-swaps (listed), 216/251 edges are self-referential non-links (only 35 genuine, undirected, passage-local coupling knots), D109/D110/D111 wholly absent, D113 on 3, seat on 0. The genuine interior map the data bears is the **corrected locus split (external-to-God vs internal-state)** and the **coupling** of fear to God's steadfast love (reverence) or to the trusting heart / the terror-triad (its poles) — with the heart/flesh named only in the prose, not the seat field.
