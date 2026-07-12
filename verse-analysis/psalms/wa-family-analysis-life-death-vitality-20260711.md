# Family analysis — Psalms · life-death-vitality (in isolation)

> Source: `verse-analysis/psalms/_base-sources/psalms__life-death-vitality.json` ONLY. Method: `Workflow/methodology/wa-psalms-family-analysis-method-v1-20260711.md`. Every finding cites `reference · span_id · Dnnn(label)` into that file. Nothing imported from outside the file.
>
> Scope: `meta.scope.family = "life-death-vitality"`; 2 meanings, 10 instances, 9 passages.

Instance roster (span · ref · head · type):
- H5315 "life" (nephesh), 8: 271265·Psa 119:109·faculty · 272374·Psa 121:7·faculty · 279406·Psa 49:8·status · 279986·Psa 54:3·status · 279998·Psa 54:4·status · 280305·Psa 56:6·status · 280603·Psa 59:3·status · 284326·Psa 86:2·faculty.
- H2421 "live" (chayah), 2: 271076·Psa 118:17·state · 284810·Psa 89:48·state.

---

## 0. Data-integrity screen (done first)

### 0.1 D112(coupling) / D116(locus) field-swap
Correct order = D116 a code, D112 a phrase. Checked all 10:

**Swapped (D112 holds the `internal:` code, D116 holds the prose) — 3 instances:**
- Psa 121:7 · span 272374 · D112="internal:ib-state" / D116="paired with God keeping from all evil". Corrected: D116(locus)=`internal:ib-state`; D112(coupling)=paired with God keeping from all evil.
- Psa 118:17 · span 271076 · D112="internal:ib-state" / D116="paired with recounting his deeds". Corrected: D116(locus)=`internal:ib-state`; D112(coupling)=paired with recounting his deeds.
- Psa 89:48 · span 284810 · D112="internal:ib-state" / D116="paired with the soul unable to escape Sheol". Corrected: D116(locus)=`internal:ib-state`; D112(coupling)=paired with the soul unable to escape Sheol.

**Correctly ordered — 7 instances:** 271265 (D116 `internal:ib-state`, D112 phrase); 279406 (D116 `internal:seat`, D112 "none"); 279986, 279998, 280305, 280603 (D116 `internal:ib-state`, D112 a coupling phrase/pair); 284326 (D116 `internal:ib-state`, D112 "paired with being godly").

All subsequent locus/coupling readings below use the **corrected** assignment.

### 0.2 Self-loop / non-edge "edges"
The `edges[]` arrays are dominated by non-links. Two non-genuine kinds present:
- **flag/event self-loops** (`item_type` flag or event, `from_span:null` or =self, `to_span`=own id): every instance's D105 bearer edge is one; also D107 target (271265, 272374, 284326, 271076, 284810), D108 manner (279406), D106 operation (279986, 279998, 280305, 280603), and the flag couplings (271265, 272374, 284326, 271076, 284810). These are **not network edges** — they merely re-assert the instance's own inferred flag.
- **self-referential pair**: Psa 49:8 · span 279406 · D104(seat) `pair`/`span` with `from_span`=`to_span`=279406. Same span both ends → **not a genuine link** (method: a pair must reach a *different* span).

**Genuine `pair` (resolution `span`, to a different span) — 4 edges, only 1 pair lies wholly inside the file:**
- Psa 54:3 · span 279986 · D112(coupling) → 279998 (Psa 54:4). **In-file.**
- Psa 54:4 · span 279998 · D112(coupling) → 279986 (Psa 54:3). **In-file** (reciprocal of the above → one dyad).
- Psa 54:4 · span 279998 · D103(source) → 279996. Different span, but 279996 is **not in this file** (external target).
- Psa 56:6 · span 280305 · D112(coupling) → 280251. External (not in file).
- Psa 59:3 · span 280603 · D112(coupling) → 280615. External (not in file).

So the only within-scope network link is the **Psa 54:3 ⇄ 54:4 dyad**. Three further genuine pairs point to spans outside the file and cannot be traversed here.

### 0.3 seat(D104) / manner(D108) = "none"
- **seat=none in 9/10** instances. Only Psa 49:8 · span 279406 · D104="soul (self)" is filled (and that as a self-pair, §0.2).
- **manner=none in 9/10**. Only Psa 49:8 · span 279406 · D108="costly, can never suffice" (flag, inferred) is filled.

### 0.4 Absent dimensions
Across all 10 instances the lexical ledgers carry only nr 101,102,(103),104,105,106,107,108,112,114,115,116. **Never present:** D109(intensity), D110(specifier), D111(effect), D113(prohibition). D103(source) appears **once only** — Psa 54:4 · span 279998 · D103.

### 0.5 Cluster NULL / T2
- **H5315 "life" — cluster.code = null, name = null** (`all_candidates: M47(Constitution) | M25(Life)`). All **8** nephesh instances are **untyped** by the term-cluster; the two candidates are not adjacent (a constitutional-seat reading vs a Life reading), so the cluster cannot decide between "the self/seat" and "life/vitality".
- H2421 "live" — cluster M25(Life); 2 instances typed.
- No T2. `is_outlier=false` on both meanings.

---

## 1. Coherence — does "life-death-vitality" fit its data?

**Partially. The label over-promises "death" and fuses two distinct movements of nephesh.**

1. **No death-head exists.** Death, Sheol, the pit, "perish" appear only in the surrounding **verse/passage text** (e.g. Psa 49:8-15 pit/Sheol; Psa 89:48 "never see death"; Psa 56:13 "delivered from death"), never as a coded characteristic span in this file. "Death" is backdrop/qualifier, not an analysed inner-being head. The family's death pole is therefore **not derivable as data** here.

2. **nephesh splits into two readings** (D102 type):
   - **faculty — the self actively held/committed/kept (3):** Psa 119:109·271265·D102(faculty) "I hold my life in my hand" (D106 "long/cling/keep with the soul"); Psa 121:7·272374·D102(faculty) "he will keep your life" (D106 "be kept"); Psa 86:2·284326·D102(faculty) "preserve my life" (D106 "be preserved").
   - **status — the life as the contested *object* (5):** the unransomable life Psa 49:8·279406·D102(status); and the enemy-sought / God-upheld life Psa 54:3·279986, Psa 54:4·279998, Psa 56:6·280305, Psa 59:3·280603 (all D102 status, D106 "sought/upheld/targeted"). These are one tight sub-movement: *the self as the prize hunted by enemies and held by God.*

3. **chayah "live" (2)** is a third, cleaner reading — **state** (D102): Psa 118:17·271076 "I shall not die but I shall live" (resolve to live for testimony); Psa 89:48·284810 "what man can live and never see death" (mortality reflection). This is the genuine **vitality/mortality** axis, and it is the only place life-vs-death is a stated opposition — but as *state*, not as a death-head.

**Verdict:** the grouping is coherent as **"the nephesh/self endangered-and-preserved, plus the chayah life-vs-death state"**, but it fuses (a) the self-as-faculty, (b) the self-as-contested-object, and (c) life-as-state; and it labels a "death" pole that has no coded head. The strongest single movement in the data is **the endangered-then-upheld nephesh** (5 status instances + the 3 preservation faculty instances converge on it).

---

## 2. The movements evidenced (cited)

### 2.1 The self held in peril, unforgotten (faculty)
Psa 119:109 · span 271265 · D101(sense)="soul (nephesh)" · D102(type)=faculty · D106(operation)="long/cling/keep with the soul" (event) · D107(target)="toward God's word" (inferred) · D116(locus)=`internal:ib-state`. D114(discovery): "the self held in constant peril, yet the law unforgotten." The self is the thing gripped in the hand — vulnerable — while the will stays fixed on the law.

### 2.2 The self kept by God (faculty, preservation)
- Psa 121:7 · span 272374 · D101="life/soul (nephesh)" · D102=faculty · D106="be kept" (event) · D107="by the LORD" (inferred) · D116(locus, corrected)=`internal:ib-state` · D112(coupling, corrected)="paired with God keeping from all evil". D114: "the very self kept by God, the soul preserved from all evil."
- Psa 86:2 · span 284326 · D102=faculty · D106="be preserved" (event) · D107="by God" (inferred) · D112(coupling)="paired with being godly" · D116(locus)=`internal:ib-state`. D114: "the self committed to God for keeping." (Passage anchor.)

Movement: the self is **the object of divine preservation**, offered up ("preserve my life, for I am godly").

### 2.3 The life as the contested prize — enemies seek it, God upholds it (status)
The densest sub-movement (5 instances, all D102 status):
- Psa 54:3 · span 279986 · D101="life/soul (nefesh - seek my life)" · D106="sought (by the enemies)" (event, inferred) · D112(coupling)→ the same nefesh God upholds (v4) [genuine pair, §0.2]. D114: "the contested centre… the self endangered and then sustained."
- Psa 54:4 · span 279998 · D106="upheld (by God)" (event, inferred) · **D103(source)="God the helper and upholder of this life (v4)"** (the sole filled source) · D112(coupling)→ the nefesh the enemies sought (v3). D114: "the turn from threat to confident security."
- Psa 56:6 · span 280305 · D106="targeted (by the enemies)" · D112(coupling)→ "the same nefesh God delivers from death (v13)" [pair to external span 280251]. D114: "endangered then rescued."
- Psa 59:3 · span 280603 · D106="targeted (by the ambush)" · D112(coupling)→ "the life for which God is called to awake and see (v4)" [pair to external span 280615]. D114: "the prize of the ambush."

Every one of these turns on the same shape: **the nephesh is hunted, then the psalm couples it to God's upholding / deliverance.** The threat→rescue turn is carried on D112 coupling, not on any operation of the self.

### 2.4 The unransomable self (status)
Psa 49:8 · span 279406 · D101="soul/life (nefesh - ransom of their life)" · D102=status · D104(seat)="soul (self)" (the only filled seat, but self-pair §0.2) · D106=none · D108(manner)="costly, can never suffice" (the only filled manner) · D116(locus)=`internal:seat`. D114: "the priceless, unbuyable soul… the life no wealth can redeem from the pit, beyond all human price." Here nephesh is the self as an **absolute value**, past all purchase — the seat/self reading (hence the `internal:seat` locus, distinct from the `internal:ib-state` of every other instance).

### 2.5 Life vs death as state (chayah)
- Psa 118:17 · span 271076 · D101="live (chayah)" · D102=state · D106="live and not die" (event) · D107="to recount God's deeds" (inferred) · D112(coupling, corrected)="paired with recounting his deeds" · D116(locus, corrected)=`internal:ib-state`. D114: "the resolve to live for testimony, life spared for praise."
- Psa 89:48 · span 284810 · D102=state · D106="live" (event) · D107="yet not escape death" (inferred) · D112(coupling, corrected)="paired with the soul unable to escape Sheol" · D116(locus, corrected)=`internal:ib-state` · D105(bearer)="any man". D114: "the reflection on mortality, no one delivers his own soul from the grave."

The only place life and death stand as an explicit pair — and it is a **state/mortality reflection**, universal ("any man"), not the psalmist's own inner operation.

---

## 3. The network (genuine pairs only)

**Within-file: one dyad.** Psa 54:3 ⇄ Psa 54:4 on D112(coupling): span 279986 → 279998 and 279998 → 279986. The endangered nefesh (enemies "seek my life", v3) and the sustained nefesh ("the LORD is the upholder of my life", v4) are bound to each other — the file's one traversable inner-being link, and it encodes the **threat→rescue** turn directly.

**Pairs reaching outside the file (genuine but untraversable here):**
- Psa 54:4 · 279998 · D103(source) → 279996 (God the upholder; span not in file).
- Psa 56:6 · 280305 · D112 → 280251 (the nefesh God delivers from death, Psa 56:13; not in file).
- Psa 59:3 · 280603 · D112 → 280615 (the life God is called to see, Psa 59:4; not in file).

**Everything else in `edges[]` is a self-loop/non-edge** (§0.2), including the one self-pair at Psa 49:8 · 279406 · D104. The network is therefore **sparse and near-absent within scope** — a single reciprocal dyad; the rest of the relational reach is to spans this file does not carry.

---

## 4. The interior anatomy the data actually names

Assembling only filled seats/sources/couplings:
- **Seat (D104):** named exactly once — Psa 49:8 · 279406 · "soul (self)". No heart, spirit/ruach, eye, etc. anywhere. The interior is essentially **seatless** in this family: nephesh *is* the self, not something located in a seat.
- **Source (D103):** named exactly once — Psa 54:4 · 279998 · "God the helper and upholder of this life". The only stated mover of the life is **God**.
- **Coupling (D112, corrected):** the life is bound to — the nefesh God upholds/enemies sought (Psa 54:3/4 · 279986/279998), God's deliverance from death (Psa 56:6 · 280305), God's awaking to see (Psa 59:3 · 280603), the whole soul-arc of the psalm (Psa 119:109 · 271265), being godly (Psa 86:2 · 284326), God keeping from all evil (Psa 121:7 · 272374), recounting God's deeds (Psa 118:17 · 271076), the soul unable to escape Sheol (Psa 89:48 · 284810). **Pattern: the life/self is almost always coupled to God's keeping/deliverance** — the one exception being 89:48's coupling to inescapable Sheol.
- **Locus (D116, corrected):** `internal:ib-state` in 9/10; `internal:seat` only at Psa 49:8 · 279406. The family sits as an **inner state**, not a distinct faculty seat.
- **Role (D115):** `characteristic` in all 10 — no qualifiers, no standalones.
- **Bearer (D105):** human IB throughout — "the psalmist" (7×, inferred), "the pilgrim" (Psa 121:7 · 272374), "any man" (Psa 49:8 · 279406; Psa 89:48 · 284810). Screen-0 passes: the inner being is the human's. God recurs as **upholder/keeper/deliverer (the arena/agent), never the bearer** — consistent with the IB-first rule.

---

## 5. What could not be derived (flagged)

- **The "death" pole has no coded head.** Death/Sheol/pit are only verse-text backdrop; not derivable as a characteristic from this file (§1.1).
- **8/10 instances are cluster-untyped** (H5315 code=null; candidates M47 Constitution vs M25 Life unresolved) — the source cannot decide self/seat vs life/vitality for nephesh (§0.5).
- **Seatless (9/10) and manner-less (9/10)**; **no D109 intensity, D110 specifier, D111 effect, D113 prohibition anywhere**; **D103 source filled once** (§0.3–0.4). The anatomy is thin: sense/type/operation/coupling/locus carry almost all the signal.
- **Network near-empty within scope**: 1 in-file dyad (Psa 54:3⇄54:4); 3 genuine pairs reach spans not in the file (§3).
- **3 instances had swapped D112/D116** and were read corrected (Psa 121:7·272374, Psa 118:17·271076, Psa 89:48·284810); the Psa 49:8·279406 D104 seat is a self-pair, not a real link (§0.1–0.2).
- **Operations are mostly passive/inferred** ("be kept", "be preserved", "sought", "upheld", "targeted") — the self rarely *acts*; it is chiefly acted-upon. The two active exceptions are Psa 119:109·271265 (D106 "hold/cling") and Psa 118:17·271076 (D106 "live and not die… recount"). Whether this passivity is the family's true shape or an artefact of thin coding cannot be settled from this file alone.

---

## 6. Summary

10 instances of two heads — **nephesh "life/soul" (8)** and **chayah "live" (2)** — cohere loosely as **"the endangered-and-preserved self, plus a life-vs-death state,"** but the family label over-reaches: there is **no coded death-head** (death is context only), and nephesh fuses three readings (faculty self-held / status self-as-contested-object / — with chayah — life-as-state). The dominant, best-evidenced movement is the **status sub-group: the nephesh hunted by enemies and upheld by God** (5 instances, the sole in-file network dyad at Psa 54:3⇄54:4). The interior is **seatless (9/10), God-sourced (the one D103), and coupled overwhelmingly to God's keeping/deliverance**; role is `characteristic` throughout and the bearer is always the human IB with God as arena. Data is thin (no D109/110/111/113, one seat, one source, one manner) and the network barely exists within scope.
