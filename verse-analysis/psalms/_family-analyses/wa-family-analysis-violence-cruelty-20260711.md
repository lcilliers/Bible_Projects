# Family analysis — Psalms `violence-cruelty` (in isolation)

> Source: `verse-analysis/psalms/_base-sources/psalms__violence-cruelty.json` only. Method: `Workflow/methodology/wa-psalms-family-analysis-method-v1-20260711.md`. 14 meanings · 21 instances · 16 passages. Expected family cluster = **M06 (Hate)**. British spelling. Every claim cited `reference · span · Dnnn(label)`.

Instance roster (span · ref · lemma · read-sense · cluster):
- 272139 · Psa 119:87 · H3615 end · "be near ended (kalah)" · null/T2
- 285040 · Psa 90:7 · H3615 end · "be consumed / brought to an end" · null/T2
- 285058 · Psa 90:9 · H3615 end · "bring to an end (kalah)" · null/T2
- 280206 · Psa 55:9 · H2555 violence · "chamas — I see violence in the city" · M27 Evil
- 280481 · Psa 58:2 · H2555 violence · "chamas — deal out violence" · M27 Evil
- 282502 · Psa 73:6 · H2555 violence · "chamas — covers them as a garment" · M27 Evil
- 282320 · Psa 72:4 · H1792 crush · "dakah — crush the oppressor" · M24 Weakness (OUTLIER)
- 285415 · Psa 94:5 · H1792 crush · "daka" · M24 Weakness (OUTLIER)
- 279984 · Psa 54:3 · H6184 ruthless men · "arits — seek my life" · M06 Hate
- 284285 · Psa 86:14 · H6184 ruthless men · "arits" · M06 Hate
- 280298 · Psa 56:6 · H1481 strife · "gur — stir up strife" · M01 Fear (OUTLIER)
- 280605 · Psa 59:3 · H1481 strife · "gur — against me" · M01 Fear (OUTLIER)
- 280271 · Psa 56:2 · H3898 attack · "lacham — many attack me" · null
- 285389 · Psa 94:21 · H1413 band together · "gadad" · null
- 280598 · Psa 59:2 · H1818 bloodthirsty · "dam — men of blood" · null
- 284011 · Psa 83:5 · H3289 conspire · "yaats" · M15 Wisdom (OUTLIER)
- 283774 · Psa 80:6 · H4066 contention · "madon — object of contention" · M02 Anger
- 279919 · Psa 53:4 · H0398 eat up · "akal — eat up my people" · null
- 307123 · Psa 94:6 · H2026 kill · "harag" · null
- 269024 · Psa 102:3 · H3615 pass away · "kalah — days pass away" · null/T2
- 280207 · Psa 55:9 · H7379 strife · "rib — violence and strife" · M02 Anger

---

## 0. Data-integrity screen

**0.1 D112(coupling)/D116(locus) field-swap — 4 instances transposed.** Correct order = D116 a code (`internal:`/`external:`), D112 a phrase. These four hold the code in D112 and a phrase in D116, i.e. **swapped** (read corrected):
- Psa 94:5 · span 285415 · D112(coupling)="internal:ib-state" / D116(locus)="paired with afflicting the heritage" → corrected: locus `internal:ib-state`, coupling *paired with afflicting the heritage*.
- Psa 94:21 · span 285389 · D112="internal:ib-state" / D116="paired with condemning the innocent" → corrected likewise.
- Psa 94:6 · span 307123 · D112="internal:ib-state" / D116="paired with murdering the fatherless" → corrected likewise.
- Psa 102:3 · span 269024 · D112="internal:ib-state" / D116="paired with the burning bones" → corrected likewise.

All 4 are **cluster-null** terms and 3 of the 4 sit in Psalm 94 (94:5/6/21). The remaining 17 instances carry D112/D116 in the correct order.

**0.2 Self-loop "edges" are not links.** The overwhelming majority of `edges[]` entries are `flag`+`inferred` with `from_span:null` and `to_span` = the span's own id (D105 bearer, D107 target, D112 coupling, and one D106 operation on span 280481). These are self-loops, **not** network edges. Genuine `pair`/`resolution:"span"` edges to a *different* span (§The network) number 15 across the file, and only **one** links two masters *inside this family*.

**0.3 seat(D104)/manner(D108)="none".** Seat = "none" on **all 21/21** instances — the interior is never located. Manner = "none" on **17/21**; only 4 fill it: Psa 73:6·282502·D108 ("as a garment enveloping them"), Psa 54:3·279984·D108 ("they do not set God before themselves"), Psa 56:2·280271·D108 ("proudly / from on high"), Psa 53:4·279919·D108 ("as they eat bread").

**0.4 Absent dimensions.** D109 intensity, D110 specifier, D111 effect, D113 prohibition — **absent on all 21**. D103 source appears **once only** (Psa 55:9·280207·D103) — absent on the other 20.

**0.5 Cluster NULL / T2 — 9/21 untyped.** No typing cluster on: H3615 end ×3 (272139, 285040, 285058, all `null`/`T2(Supplementary)`), H3615 pass away (269024, `null`/T2), H3898 attack (280271, null), H1413 band together (285389, null), H1818 bloodthirsty (280598, null), H0398 eat up (279919, null), H2026 kill (307123, null). The term-cluster cannot type these; typing rests on read-sense + D114 alone. The 12 typed instances split M27 Evil (3), M06 Hate (2), M24 Weakness (2, outlier), M01 Fear (2, outlier), M02 Anger (2), M15 Wisdom (1, outlier).

**0.6 Outliers (is_outlier=true) — 3 meanings / 5 instances.** All flagged "expects M06(Hate)": H1792 crush → M24 Weakness (282320, 285415); H1481 strife/gur → M01 Fear (280298, 280605); H3289 conspire → M15 Wisdom (284011). Only H6184 ruthless men actually lands on the family's expected M06 (279984, 284285).

**0.7 Bearer resolution.** All 21 D105 bearer values carry `resolution:"inferred"`; none is text-explicit. All bearers are human (the wicked / enemies / rulers / the king / the psalmist / "we mankind") — the human-IB screen holds — but note (§1) that most bear the *aggressor's* interior, not the psalmist's.

---

## 1. Coherence — does "violence-cruelty" fit its data?

**Partly. The keyword grouping has fused (at least) three distinct movements.** The label fits the core but sweeps in two foreign movements via lemma polysemy and valence.

**Movement A — aggressor violence/cruelty (core, coherent, ~14 instances).** The disposition and acts of the wicked/enemies against the innocent: violence *chamas* seen in the city / dealt out / worn as a garment (280206, 280481, 282502 · D101 sense); ruthless *arits* men who seek the psalmist's life (279984, 284285); *gur* stirring-up / banding (280298, 280605); *lacham* attacking (280271); *gadad* banding against the righteous (285389); *dam* bloodthirsty men (280598); *yaats* conspiring against God (284011); *akal* devouring God's people as bread (279919); *harag* killing widow and sojourner (307123); *daka* crushing God's people (285415); *rib* strife (280207) and *madon* contention (283774) as the civic condition of a violent place. This is one coherent movement and matches the label.

**Movement B — frailty / being consumed / mortality (FUSED-IN, 4 instances).** H3615 *kalah* "end / pass away": Psa 119:87·272139 ("they had almost made an **end** of me" — near-destruction endured · D114), Psa 90:7·285040 ("we are brought to an **end** by your anger" · D114), Psa 90:9·285058 ("we bring our years to an **end** like a sigh" · D114), Psa 102:3·269024 ("my days **pass away** like smoke" · D114). Bearer here = the psalmist / "we (mankind)" (D105), a **passive perishing under God's wrath or affliction**, not perpetrated cruelty. It enters the family only because *kalah*'s gloss spans "to end: destroy / consume" (evidence.lexical_gloss). Type = `state` throughout (272139/285040/285058/269024 · D102). This is a **distinct movement** (mortality / near-annihilation), not violence-cruelty as disposition.

**Movement C — righteous retributive violence (FUSED-IN by valence, 1 instance).** Psa 72:4·282320·D101 "**crush** (dakah) the oppressor" — bearer = **the king** (D105), locus `external:person` (D116), coupled as "the reverse of defending the poor" (D112, edge 282320→282314). This is *justice-violence* against the cruel, valence-opposite to Movement A (which the wicked inflict). The sibling instance 285415 (Psa 94:5, "they crush your people") belongs to Movement A. So the lemma H1792 itself straddles A and C.

Naming these distinct movements is a first-class finding: **the "violence-cruelty" family is a core (A) plus a mortality tail (B, kalah ×4) plus a lone righteous-retribution reading (C, crush 72:4).**

---

## 2. The movements/operations evidenced

**2.1 Violence as garment / condition, not act (chamas).** All three H2555 instances read violence as a **status** (D102), a thing the wicked *are* or are *covered by*, not primarily a verb: Psa 55:9·280206 "I see violence in the city" (D101), Psa 58:2·280481 "deal out violence on earth" (D101; D106 operation "dealt out", inferred), Psa 73:6·282502 "violence covers them as a garment" (D101; D106 operation "cover them" · edge 282502→282503; D108 manner "as a garment enveloping them" · edge 282502→282503; D112 coupling "paired with their pride" · edge 282502→282500). The garment image (282502) is the fullest picture: cruelty as the whole self's clothing, welded to pride.

**2.2 Predatory / lethal acts against the defenceless.** *akal* devouring God's people "as they eat bread" — routine, conscienceless (Psa 53:4·279919·D101, D108 manner edge 279919→279921, D112 coupling "paired with not calling upon God" edge 279919→279924). *harag* killing the widow and sojourner (Psa 94:6·307123·D101/D114). *daka* crushing God's people (Psa 94:5·285415·D101/D114). *dam* bloodthirsty "men of blood" (Psa 59:2·280598·D101), coupled to "the workers of evil" (D112, edge 280598→280594).

**2.3 Organised, banded hostility.** A recurrent sub-motion: the foes *mass* rather than strike singly. *gur* "stir up strife / band together" (Psa 56:6·280298, Psa 59:3·280605 · D101/D114, both coupled to watching the psalmist's steps / the fierce men's act); *gadad* "band together against the life of the righteous" (Psa 94:21·285389·D101/D114); *yaats* "conspire with one accord … against you" (Psa 83:5·284011·D101/D114, target=against God · D107); *lacham* "many attack me proudly" (Psa 56:2·280271·D101, D108 manner "proudly / from on high" edge 280271→280272, D112 coupling "the trampling enemies now as warring assailants" edge 280271→280266). The D114 notes name this explicitly: "organised malice, not random hostility" (280298), "many peoples fused into one hostile will" (284011).

**2.4 Ruthlessness as godless disposition.** *arits* "ruthless men" (Psa 54:3·279984, Psa 86:14·284285 · D101), read as status (D102). The distinguishing note is manner/coupling: they "do not set God before themselves" (Psa 54:3·279984·D108 manner) — cruelty freed by godlessness. 284285 couples them to "the insolent" (D112, inferred).

**2.5 Violence suffered as social shame.** Psa 80:6·283774 "object of contention (madon)" — the people *made a thing fought over* by neighbours (D101, type=state D102, D106 "become a thing fought over"), coupled to "the enemies' laughter" (D112). Read (D114) as "humiliation felt as an inner wound." This is the passive/received face of the family.

**2.6 Righteous crush (the counter-movement).** Psa 72:4·282320 — the king *crushes the oppressor* (D101), the only instance whose bearer is a just agent and whose D112 frames it as "the reverse of defending the poor." See §1 Movement C.

**2.7 The mortality tail (kalah).** See §1 Movement B: 272139, 285040, 285058, 269024 — perishing/being-consumed, all type=state, bearer=psalmist/mankind.

---

## 3. The network (genuine `pair` edges only)

15 genuine span-resolved edges exist; **only one links two masters within this family** — the rest exit to companion spans not carried as family masters (companion word-spans in the same verse).

**The single intra-family edge — Psa 55:9, violence ⇄ strife (reciprocal):**
- 280206 (violence, chamas) —D112 coupling→ 280207 (strife, rib): "paired with strife filling the city."
- 280207 (strife, rib) —D112 coupling→ 280206 (violence): "paired with violence."

So the family's entire internal wiring is one reciprocal violence↔strife couple inside a single verse (Psa 55:9). Additionally 280207 carries the file's **only** D103 source edge: 280207 —D103 source→ 280200 ("the psalmist asks God to destroy and confuse their tongues", exits the family). Everything else in the family is unlinked.

**Family-exit pair edges (to non-master companion spans, cited by from→to):**
- 280481 —D112→ 280478 (violence ← "wrongs devised", Psa 58:2).
- 282502 —D106→ 282503, —D108→ 282503, —D112→ 282500 (violence-garment ← pride, Psa 73:6).
- 282320 —D107→ 282321 (crush → the oppressor), —D112→ 282314 (← defending the poor, Psa 72:4).
- 279984 —D112→ 279985 (ruthless men ← seeking the psalmist's life, Psa 54:3).
- 280298 —D112→ 280300 (strife/gur ← watching his steps, Psa 56:6).
- 280605 —D112→ 280604 (strife/gur ← the fierce men, Psa 59:3).
- 280271 —D108→ 280272 (attack ← proudly), —D112→ 280266 (← trampling enemies, Psa 56:2).
- 280598 —D112→ 280594 (bloodthirsty ← workers of evil, Psa 59:2).
- 279919 —D108→ 279921 (eat-up ← as bread), —D112→ 279924 (← not calling on God, Psa 53:4).

**Network character:** extremely sparse and non-directional (`direction:null` throughout). Nine of the 14 meanings have **no** genuine pair edge at all (their entire edge set is self-loops): H3615 end (all 3), H1792 crush/94:5, H6184 ruthless/86:14, H1413 band-together, H3289 conspire, H4066 contention, H2026 kill, H3615 pass-away. The family does not form a web; it forms one couple (55:9) and a scatter of single ties reaching *out* of the family.

---

## 4. Interior anatomy the data names

- **Seat (D104): none named — 21/21.** The family never locates violence in a faculty (no heart/soul/ruach/eye). Where the verse *text* would license a heart-seat — Psa 58:2·280481 "in your **hearts** you devise wrongs", Psa 73:7 "their **hearts** overflow", Psa 55:21 "war was in his **heart**" — the ledger still records D104="none". The interior is read entirely off outward act. (Flagged as a derivation gap, §5.)
- **Locus (D116, corrected):** `internal:ib-state` on 15, `external:person` on 6 (Psa 54:3·279984, Psa 56:6·280298, Psa 59:3·280605, Psa 56:2·280271, Psa 53:4·279919, Psa 72:4·282320). The `external:person` set = the outward, enacted aggressions (attack, stir-strife, devour, crush-the-oppressor, ruthless-seek-life); `internal:ib-state` = the dispositions/states/conditions. This is the only interior/exterior partition the data supplies.
- **Type (D102):** action 9 (crush ×2, strife/gur ×2, attack, band-together, conspire, eat-up, kill), status 7 (violence ×3, ruthless ×2, bloodthirsty, strife/rib), state 5 (end ×3, contention, pass-away). **No** affect / disposition / faculty / volition / cognition type appears — violence-cruelty is encoded only as ACT or CONDITION, never as a named inner faculty or feeling.
- **Bearer (D105):** the aggressor's interior dominates — "the wicked / enemies / unjust rulers / fierce men / evildoers" (17 of 21). The psalmist/"we mankind" bear only the mortality tail (272139, 285040, 285058, 269024) and the received shame (283774); the king alone bears righteous violence (282320). So the "inner being" this family mostly exhibits is **the cruel person's**, observed from without.
- **Source (D103): named once** — Psa 55:9·280207 (God asked to confuse the wicked's tongues). No other instance names what moves the violence.
- **Coupling (D112, filled):** the repeated welds are violence↔strife/pride (Ps55:9, Ps73:6), banding↔surveillance/lying-in-wait (Ps56:6, Ps59:3, Ps56:2), cruelty↔godlessness (Ps53:4 "not calling on God", Ps54:3 "not setting God before themselves"). Cruelty is consistently bound to (a) other violence, (b) pride, and (c) the refusal of God.

---

## 5. What could not be derived

- **Interior location of violence — never (D104="none" 21/21),** including where verse text offers a heart-seat (Psa 58:2·280481, cf. 73:7, 55:21). The family cannot tell us *where* in the inner being cruelty sits.
- **Intensity (D109), specifier (D110), effect (D111), prohibition (D113): entirely absent** — no gradation, no named consequence, no prohibition captured, on any instance.
- **Source (D103): 20/21 blank** — only Psa 55:9·280207 names a mover.
- **Manner (D108): 17/21 blank.**
- **9/21 instances untyped by cluster** (null/T2, §0.5); typing for these rests on read-sense + D114 only.
- **4 instances have D112/D116 swapped** (§0.1) and must be read corrected (all cluster-null; 3 in Ps 94).
- **Network is not derivable as a web:** only one intra-family edge exists (violence⇄strife, Ps55:9); 9 of 14 meanings have no genuine edge; all directions are null. Cross-family relational structure is real only as single ties out of the family.
- **Family fusion (§1):** the label cannot be taken to describe one movement — the *kalah* mortality tail (4) and the righteous-crush reading (1) are foreign to "violence-cruelty" as an aggressor disposition and must be separated before any family-level claim.

---

## Summary

`violence-cruelty` = 14 meanings / 21 instances, coherent at its **core** (Movement A: the wicked's enacted, organised, godless violence against the innocent — chamas, arits, gadad, akal, harag, daka, dam, yaats, lacham) but **fused** with a mortality tail (H3615 *kalah* "end/pass away" ×4, bearer = the perishing psalmist/mankind) and one **righteous-retribution** outlier (crush the oppressor, Psa 72:4, bearer = the king). The data encode cruelty **only as act or condition (action/status/state), never as a located inner faculty** — seat is unnamed on all 21, and the interior/exterior split (D116) is the sole anatomy given. The network is effectively empty: a single violence⇄strife couple at Psa 55:9, everything else self-loops or exits the family. Cruelty's one consistent binding (D112) is to **pride and the refusal of God**.
