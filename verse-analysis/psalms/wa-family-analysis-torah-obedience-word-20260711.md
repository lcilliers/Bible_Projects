# Family analysis — `torah-obedience-word` (Psalms), in isolation

> Source: `verse-analysis/psalms/_base-sources/psalms__torah-obedience-word.json` only. Scope strictly that one file. 4 meanings / 4 instances / 4 passages, one master span each. Every claim cited `reference · span_id · Dnnn(label)`.

The four instances:

| span_id | reference | lemma | meaning | ESV | cluster |
|---|---|---|---|---|---|
| 281341 | Psa 66:3 | H3584 | come cringing | come cringing | NULL |
| 271962 | Psa 119:60 | H2363 | hasten | hasten | NULL |
| 277754 | Psa 37:31 | H8451 | law | law | NULL |
| 269676 | Psa 106:25 | H8085 | obey (negated) | obey | M41 (Remembrance) — outlier |

---

## 0. Data-integrity screen

**D112/D116 field-swap — ONE instance affected: span 269676 (Psa 106:25).** Here `D116 locus = "paired with murmuring"` (a prose phrase) and `D112 coupling = "external:god"` (a code) — transposed. Read corrected: `Psa 106:25 · span 269676 · D116(locus) = external:god` and `· D112(coupling) = paired with murmuring`. The other three are in correct order (D116 holds a code, D112 holds a phrase/none): `Psa 66:3 · span 281341 · D116(locus)=external:person / D112(coupling)=none`; `Psa 119:60 · span 271962 · D116(locus)=external:god / D112(coupling)="paired within its char-arc across the psalm"`; `Psa 37:31 · span 277754 · D116(locus)=internal:ib-state / D112(coupling)="law-in-heart"`.

**Self-loop "edges" (not network links).** Every edge on this file except one is a self-loop (`item_type:flag`, `resolution:inferred`, `to_span` = the span's own id): `Psa 66:3 · span 281341 · D105(bearer)` + `D107(target)`; `Psa 119:60 · span 271962 · D105(bearer)` + `D107(target)` + `D112(coupling)`; `Psa 37:31 · span 277754 · D105` + `D107` + `D112`; `Psa 106:25 · span 269676 · D105` + `D107` + `D112`. None are real links.

The **only genuine pair edge** is `Psa 66:3 · span 281341 · D108(manner)` → `to_span 281338`, `item_type:pair`, `resolution:span`. It points to span **281338, which is not present in this file** — so even the one real edge is un-followable within scope. Net: the in-scope inner-being network is empty.

**Seat (D104) = "none" — all 4 instances** (281341, 271962, 277754, 269676). No interior seat named anywhere.

**Manner (D108) = "none" — 3 of 4** (271962, 277754, 269676). Only 281341 fills it (the pair edge above).

**Coupling (D112) = "none" — 1** (281341). The other three carry a value (271962 phrase; 277754 "law-in-heart"; 269676 the swapped "external:god" code).

**Absent dimensions (across all 4 instances):** D103 (source), D109 (intensity), D110 (specifier), D111 (effect), D113 (prohibition). None appears in any ledger.

**Cluster NULL / outlier:** three instances have `cluster.code = null` (281341, 271962, 277754) — the term-cluster cannot type them. The fourth, `Psa 106:25 · span 269676`, is `M41 (Remembrance)` and is explicitly flagged `is_outlier=true` with `outlier_note`: family expects M30 (Obedience) but the term-cluster is M41 (Remembrance). So the one typed instance is typed *wrongly* for the family.

---

## 1. Coherence — does the label fit the data?

**No — the keyword grouping has fused two unrelated movements**, and the one "torah/word" cluster signal present is mis-typed.

- **Movement A — human devotion to God's word/law (3 instances).**
  - `Psa 119:60 · span 271962 · D101(sense)="hasten (chush)"` / `D106(operation)="hasten to obey"`, bearer the psalmist — promptness of obedience (`D114`: "the promptness of obedience").
  - `Psa 37:31 · span 277754 · D101(sense)="the law in his heart, steps not slipping"` / `D102(type)=cognition` — internalised law producing a steady walk (`D114`: "the law made inward … the interior's walk stays sure-footed").
  - `Psa 106:25 · span 269676 · D101(sense)="obey (shama, negated)"` / `D106(operation)="fail to obey"` — the *negative* of the movement (the fathers' disobedience). Belongs to the theme by contrast.

- **Movement B — feigned/forced submission of God's enemies (1 instance, a keyword accident).**
  - `Psa 66:3 · span 281341 · D101(sense)="cringe / feign submission (kachash)"`, `lexical_gloss="to deceive"`, bearer `"the enemies (of God)"`. `D114`: "the feigned, forced submission of the foes … a submission of dread, not love." This is *deception/cowering pretence*, not torah-keeping. It landed in the family only because the read-phrase paraphrases kachash as "feign **obedience**" (`D106(operation)="cringe / feign obedience"`). It is not the human IB devoted to the word; it is the opposite pole — hollow, dread-driven pseudo-submission.

So the family label `torah-obedience-word` genuinely covers **271962, 277754, 269676** (obedience-to-the-word, one of them negated), and **wrongly absorbs 281341** (kachash = deceive/cringe). One clean movement + one intruder.

---

## 2. The movements/operations evidenced (cited)

### 2a. Obedience made prompt — `Psa 119:60 · span 271962`
`D102(type)=action`; `D106(operation)="hasten to obey"`; bearer `D105="the psalmist"` (inferred); target `D107="God's word"` (inferred); `D116(locus)=external:god`; `D112(coupling)="paired within its char-arc across the psalm"` (inferred). Seat and manner "none". The interior act is a disposition of readiness — the will moving *without delay* toward the commandments (`D114`: "'I HASTEN and do not delay to keep your commandments'"). No seat, source, intensity or effect named — the file records the *act*, not the faculty behind it.

### 2b. Law internalised → steady walk — `Psa 37:31 · span 277754`
Uniquely typed `D102=cognition` (the only non-action of the four). `D106(operation)="the law of his God is in his heart, so his steps do not slip - internalised law producing a steady walk"`; bearer `D105="the righteous"` (inferred); target `D107="internalised-law"` (inferred); `D112(coupling)="law-in-heart"`; `D116(locus)=internal:ib-state` — the **only instance located inside the IB**. `D114`: "the law made inward; because it lives in the heart, the interior's walk stays sure-footed." This is the richest instance: it names an interior *state* (law-in-heart) and its downstream effect on conduct (steps not slipping) — though note **D111 effect is not filled**; the effect lives only in the D106 prose and the verse text ("his steps do not slip"), not as a typed dimension.

### 2c. Obedience refused — `Psa 106:25 · span 269676`
`D102=action`; `D106(operation)="fail to obey"`; sense `D101="obey (shama, negated)"`; bearer `D105="the fathers"` (inferred); target `D107="the voice of the LORD"` (inferred). Corrected: `D116(locus)=external:god`, `D112(coupling)="paired with murmuring"`. `D114`: "the disobedience behind the murmuring." The interior movement is a *withholding* of obedience, welded (per the corrected coupling) to murmuring — the file frames disobedience not as absence but as the twin of complaint. This is the one instance the term-cluster typed, and it typed it `M41 (Remembrance)`, not obedience — a signal the term (shama) sits nearer memory/hearing than volitional obedience in the cluster model.

### 2d. Feigned submission of the foe — `Psa 66:3 · span 281341` (family intruder)
`D102=action`; `D106(operation)="cringe / feign obedience"`; sense `D101="cringe / feign submission (kachash)"`; bearer `D105="the enemies (of God)"` (inferred); target `D107="to God"` (inferred); `D116(locus)=external:person`; `D112(coupling)=none`; `D108(manner)="before the greatness of God's power"` (the one filled manner, carried as the pair edge). `D114`: "the cowering pretence of obedience wrung from enemies by God's great power … a submission of dread, not love." A distinct movement (see §1B) and the only instance whose *bearer is not the devout human IB* but God's adversaries.

---

## 3. The network

Effectively none in scope. Fourteen of fifteen edges are self-loops (§0) and carry no relational information. The single genuine `pair` edge — `Psa 66:3 · span 281341 · D108(manner)` → `to_span 281338` (`resolution:span`) — binds the enemies' cringing to the *greatness of God's power* as its trigger, but 281338 is outside this file, so the link cannot be resolved here. **The four instances are mutually unconnected within this source.** No verse links to another verse in the family.

---

## 4. The interior anatomy the data actually names

Sparse. Assembling only filled interior fields:

- **Seat:** never named (D104="none" ×4). The file offers no heart/soul/spirit seat *as a typed dimension* — even Psa 37:31, whose verse text and D106/D114 speak of the "heart," leaves `D104=none`; "heart" survives only in prose, not as a coded seat.
- **Locus:** three external (`external:person` 281341; `external:god` 271962; `external:god` 269676-corrected) and **one internal** — `internal:ib-state` at `Psa 37:31 · span 277754`. So the family is almost entirely externally-oriented (movement *toward* God/word), with law-in-heart the sole interiorised state.
- **Coupling (filled):** `law-in-heart` (277754) and `paired with murmuring` (269676-corrected) — the only two substantive couplings. They pair obedience with its interior lodging (heart) and disobedience with its interior symptom (murmuring).
- **Type:** three `action`, one `cognition` (277754). The family is read overwhelmingly as *doing*, not faculty/affect/volition.
- **Role:** `characteristic` on all four (D115). No qualifiers or standalones.
- **Bearer:** all inferred, all human groups/persons — the psalmist (271962), the righteous (277754), the fathers (269676), the enemies of God (281341). No seat is attached to any bearer.

---

## 5. What could not be derived

- **No source (D103), intensity (D109), specifier (D110), effect (D111), or prohibition (D113)** anywhere — so what *drives* each movement, how strong it is, and its typed consequence are all unread. Notably Psa 37:31's effect (steps not slipping) and Psa 119:60's negation ("do not delay") live only in prose/verse, not as coded dimensions.
- **No interior seat** for any instance (D104="none" ×4) — the anatomy is unlocalised.
- **The one real relational edge is un-followable** (target span 281338 absent from the file); the in-scope network is empty.
- **The one cluster-typed instance is mis-typed for the family** (M41 Remembrance, not M30 Obedience) and self-flagged outlier; the other three are cluster-NULL — so the term-cluster layer offers no coherent typing of this family.
- **The family label is not self-consistent**: it fuses word-obedience (271962, 277754, 269676) with the deceit/dread-submission of God's enemies (281341, kachash="to deceive"). Whether 281341 belongs at all is not resolvable from this file — flagged as a keyword-collision, not confirmed.

---

## 6. Summary

`torah-obedience-word` (Psalms) = 4 meanings / 4 instances, each a lone span, mutually unlinked. The coherent core is **obedience to God's word** read as *action*: hastening to keep the commandments (Psa 119:60·271962), the law internalised in the heart steadying the walk (Psa 37:31·277754, the only `internal:ib-state`), and its negation — the fathers refusing to obey, welded to murmuring (Psa 106:25·269676). One **intruder** — the feigned, dread-driven cringing of God's enemies (Psa 66:3·281341, kachash="to deceive") — fuses a second, opposite movement into the family. The interior anatomy is thin: no seat anywhere, no source/intensity/effect/prohibition, only two substantive couplings (law-in-heart; obedience↔murmuring). Data-integrity: one D112/D116 swap (269676), fourteen self-loop non-edges, the sole genuine edge pointing out of scope, and the only cluster-typed instance mis-typed (M41 Remembrance) and flagged outlier.
