# Family analysis — `memory-remembrance` (Psalms), in isolation

> Source: `outputs/data/psalms-family-base-sources/psalms__memory-remembrance.json` only. 7 meanings, 46 instances, 35 passages. Every claim cited `reference · span N · Dnnn(label)` into that file. Nothing imported from outside it.

## Roster (meaning → lemma → cluster → count)
| # | char_key | lemma | cluster | instances |
|---|---|---|---|---|
| 1 | H2142:remember | H2142 (zakar) | **M41 Remembrance** | 20 |
| 2 | H7911:forget | H7911 (shakach) | **null** | 16 |
| 3 | H7911:forgotten | H7911 | **null** | 4 |
| 4 | H7911:forgot | H7911 | **null** | 3 |
| 5 | H2142:mindful | H2142 | M41 Remembrance | 1 |
| 6 | H5769:never | **H5769 (olam)** | **null / `T2(Supplementary)`** | 1 |
| 7 | H2142:remind | H2142 | M41 Remembrance | 1 |

Two lemmas carry the family: **zakar** (remember/mindful/remind, 22 instances, all M41) and **shakach** (forget/forgotten/forgot, 23 instances, all cluster-null). A single alien lemma, **olam** (never, 1), is swept in.

---

## 0. Data-integrity screen

### 0.1 D112(coupling) / D116(locus) field-swap — **12 of 46 transposed**
Correct order = D116 a code (`internal:`/`external:`), D112 a phrase. Transposed where **D112 coupling holds the code** and **D116 locus holds the prose phrase**. Read them corrected:

- Psa 103:18 · span 269122 — D112=`external:god`, D116="paired with keeping the covenant" → swap
- Psa 105:5 · span 269539 — D112=`external:god`, D116="paired with the wondrous works and covenant" → swap
- Psa 106:7 · span 269845 — D112=`internal:ib-state`, D116="paired with not considering, and with rebelling" → swap
- Psa 109:16 · span 270195 — D112=`internal:ib-state`, D116="paired with pursuing the poor" → swap
- Psa 137:1 · span 273272 — D112=`internal:ib-state`, D116="paired with the weeping" → swap
- Psa 137:6 · span 273290 — D112=`internal:ib-state`, D116="paired with setting Jerusalem above his highest joy" → swap
- Psa 103:2 · span 269135 — D112=`internal:ib-state`, D116="paired with blessing the LORD" → swap
- Psa 102:4 · span 302594 — D112=`internal:ib-state`, D116="paired with the withered heart" → swap
- Psa 137:5 · span 308031 — D112=`internal:ib-state`, D116="paired with the hand failing if he forgets" → swap
- Psa 137:5 · span 308035 — D112=`internal:ib-state`, D116="paired with the vow not to forget" → swap
- Psa 106:13 · span 269602 — D112=`internal:ib-state`, D116="paired with not waiting for his counsel" → swap
- Psa 106:21 · span 307456 — D112=`internal:ib-state`, D116(locus) a phrase → swap

The other 34 instances are in the correct order (D112 a phrase or `none`; D116 a code), e.g. Psa 119:55 · span 271924 · D112="paired within its char-arc" / D116=`external:god`. **Diagnostic rule for this file:** any instance whose D112 value is a bare `internal:`/`external:` code is transposed.

### 0.2 Self-loop "edges" are not links
Every instance emits self-loop pseudo-edges — `item_type:"flag"`, `resolution:"inferred"`, `from_span:null`, `to_span` = its own id — on D105 bearer, D107 target, D112 coupling (e.g. Psa 103:18 · span 269122 · edges → 269122). These are **not** network edges and are excluded from §The network.

### 0.3 seat(D104) / manner(D108) = "none"
- **D104 seat = "none" in all 46 instances** (100%). The data names **no interior seat** for memory anywhere — not heart, soul, nor ruach — even where the verse text says "heart" (Psa 119:11) or "soul" (Psa 42:4).
- **D108 manner = "none" in ~39 of 46.** Manner is filled in only ~7: Psa 42:4 · span 278553 ("pouring out his soul"); Psa 42:6 · span 278582 ("from the land of Jordan and Hermon"); Psa 63:6 · span 281070 ("upon his bed, in the night"); Psa 77:11 · span 282875 ("resolved, deliberate ('I will')"); Psa 77:11 · span 282879 ("emphatic repetition ('yes, I will remember')"); Psa 77:3 · span 282959 ("with moaning"); Psa 77:6 · span 282971 ("meditating in the heart").

### 0.4 Absent dimensions (across all 46)
- **D109 intensity — absent (0/46).**
- **D110 specifier — absent (0/46).**
- **D111 effect — absent (0/46).**
- **D113 prohibition — present once only:** Psa 44:17 · span 278740 · D113("negated ('we have NOT forgotten you')").
- **D103 source — effectively absent:** appears only twice, both as pair edges (Psa 50:22 · span 279570 · D103 → 279562). No standard ledger carries a source value.

### 0.5 Cluster null / T2
- **All 24 shakach + olam spans have `cluster.code = null`** (meanings 2, 3, 4, 6). The term-based cluster types **only the positive pole (zakar → M41)**; forgetting and "never" are untyped.
- **Psa 30:6 · span 276627** ("never", olam) additionally carries `all_candidates: "T2(Supplementary)"` — flagged supplementary, i.e. the term-cluster itself judges it a non-core reference.

---

## 1. Coherence — does the label fit its data?

**Mostly yes, as one bipolar faculty; with one genuine intruder.** The family is not a fusion of unrelated movements but the **two poles of a single inner-being axis — memory**:

- **Remembering (zakar, 22):** deliberate recall, mostly Godward (Psa 105:5 · span 269539 · D114: "the deliberate recalling of God's deeds").
- **Forgetting (shakach, 23):** memory's failure or its guarded refusal (Psa 103:2 · span 269135 · D114: "worship that refuses amnesia"; Psa 106:7 · span 269845 · D114: "the forgetting of God's love that bred rebellion").

Both are one movement seen from opposite ends, so the keyword grouping is defensible. **One instance does not belong:** **Psa 30:6 · span 276627 · D101("in prosperity, 'I shall never be moved'")** — lemma **H5769 olam**, gloss "forever: enduring…", ESV "never". This is an adverb of **permanence/complacency**, not a memory verb; D114 reads it as "past over-confidence… a false sense of permanence." It is swept in by the English string "never/forget-adjacent", not by any memory sense. **Flag as mis-grouped (1 instance).**

A second, subtler flag: **Psa 8:4 · span 284919** ("mindful", zakar). The verb's grammatical agent is **God** ("you are mindful of him"); the coded human IB is only the *responding* affect — D102(cognition), D107("humbled-wonder"), D114: "the interior… astonished at being noticed at all." So the memory-act here is God's; the family keyword lands on the human's wonder, not on a human remembering. Legitimate as IB-response (Screen-0), but note the derivation.

---

## 2. The movement evidenced

### 2.1 Type (D102) — memory as act, hardening to disposition
Predominantly **action** (the bare remember/forget verbs, e.g. Psa 105:5 · span 269539 · D102(action)). A distinct **disposition** band clusters on the negated Psalm-119 "I do **not** forget your law" vows — a settled trait, not an event: Psa 119:16 · span 271585; Psa 119:61 · span 271973; Psa 119:93 · span 272188; Psa 119:109 · span 271270; Psa 119:139 · span 271452; Psa 119:141 · span 271471; Psa 119:153 · span 271541; Psa 119:176 · span 271699 — all D102(disposition). The enemy's failure to remember mercy is also disposition: Psa 109:16 · span 270195 · D102(disposition). Scattered edges: **cognition** (Psa 25:7 · span 276080; Psa 143:5 · span 273909; Psa 8:4 · span 284919; Psa 30:6 · span 276627), **affect** (Psa 22:27 · span 275724 — the nations remember-and-worship), **state** (Psa 31:12 · span 276692 "forgotten like one who is dead"; Psa 102:4 · span 302594), **status** (Psa 59:11 · span 280542).

### 2.2 Operation (D106) — remember / fail-to-remember / forget
Three event-shapes: `remember` (Psa 103:18 · span 269122 · D106(remember)), `fail to remember` (Psa 106:7 · span 269845; Psa 109:16 · span 270195 · D106("fail to remember")), and forgetting (meanings 2–4). The pivot instances spell memory as **chosen remedy**: Psa 77:11 · span 282875 · D114("the decisive act of will that turns the psalm; memory chosen as remedy… remembrance now healing where in v3 it wounded"); its foil, Psa 77:3 · span 282959 · D114("memory of God brings not solace but anguish… remembrance that deepens the groan").

### 2.3 Bearer (D105) — human IB throughout, individual and collective
All D105 are inferred flags. Bearers: **the psalmist** (Psa 119:55 · span 271924; Psa 137:6 · span 273290; Psa 143:5 · span 273909), **the faithful/worshippers** (Psa 103:18 · span 269122; Psa 105:5 · span 269539), **the fathers** (Psa 106:7 · span 269845), **the exiles** (Psa 137:1 · span 273272), **the nations** (Psa 22:27 · span 275724), **the enemy** (Psa 109:16 · span 270195). Human interior in every case; several collective.

### 2.4 Target (D107) — memory is object-directed, and its object is chiefly God
Targets (mostly inferred flags): God's commandments (Psa 103:18 · span 269122), wondrous works (Psa 105:5 · span 269539), steadfast love (Psa 106:7 · span 269845), word (Psa 119:55 · span 271924), name; Zion (Psa 137:1 · span 273272), Jerusalem-above-all-joy (Psa 137:6 · span 273290). Forgetting targets the same: God, his law, his benefits. Memory here is never contentless — it is always *of* something, overwhelmingly God and his acts.

### 2.5 Locus (D116, corrected) — the interior turned outward to God
After correcting the swaps, D116 splits between `internal:ib-state` (memory as inner condition, e.g. Psa 143:5 · span 273909; Psa 22:27 · span 275724; Psa 25:7 · span 276080) and `external:god` (memory bound to God as its pole, e.g. Psa 119:55 · span 271924; Psa 77:11 · span 282875; Psa 44:17 · span 278740; Psa 71:16 · span 282081), with one `external:person` (Psa 45:17 · span 278930, the king's name made-remembered).

---

## 3. The network (genuine `pair` edges only)

20 genuine `pair` edges (`resolution:"span"`, to a different span) span 11 instances. **Only ONE links two spans inside this family:** the reciprocal Psa 77:11 doublet —
- Psa 77:11 · span 282875 → **282879** · D112(coupling) ; and 282879 → **282875** · D112(coupling): the two "I will remember" resolves bound to each other (D114: "the doubled resolve, memory pressed home").

**All other pair edges radiate to spans outside the 46-instance set** (other terms in the same passage), so as a within-family network the graph is a single edge plus isolates:
- Psa 42:4 · span 278553 → 278555 · D108(manner)
- Psa 42:6 · span 278582 → 278578 · D112(coupling)
- Psa 45:17 · span 278930 → 278935 · D112(coupling)
- Psa 63:6 · span 281070 → 281073 · D112(coupling)
- Psa 77:11 · span 282875 → 282876 · D107(target)
- Psa 77:11 · span 282879 → 282881 · D107(target)
- Psa 77:3 · span 282959 → 282961 · D108(manner); → 282963 · D112(coupling)
- Psa 77:6 · span 282971 → 282974 · D108(manner); → 282977 · D112(coupling)
- Psa 45:10 · span 278887 → 278893 · D112(coupling)
- Psa 50:22 · span 279570 → 279562 · D103(source); → 279567 · D112(coupling)
- Psa 59:11 · span 280542 → 280553 · D112(coupling)
- Psa 44:17 · span 278740 → 278742 · D112(coupling)
- Psa 71:16 · span 282081 → 282082 · D107(target); → 282077 · D108(manner); → 282067 · D112(coupling)

The remaining ~35 instances carry **only self-loops** (§0.2) — no genuine edges at all. The network is therefore **very sparse and outward-facing**: memory is coded as coupling *to its object* (mostly non-family spans in the same verse), not as an inner web among memory-terms. The only inner-being link the family names to itself is the Psa 77:11 remember↔remember pair.

---

## 4. The interior anatomy the data actually names

Assembling only filled dimensions:
- **Seat:** none named (0/46). The data grants memory **no organ** — a striking silence for a faculty.
- **Agent (bearer):** the whole human interior — psalmist, faithful, fathers, exiles, nations, enemy — always inferred.
- **Object (target/locus):** overwhelmingly **God and his acts** (commandments, works, steadfast love, name), plus city/home (Zion, Jerusalem). Memory is intrinsically Godward-directed.
- **Manner (where named):** posture and setting — pouring out the soul (Psa 42:4 · span 278553), on the bed in the night (Psa 63:6 · span 281070), with moaning (Psa 77:3 · span 282959), meditating in the heart (Psa 77:6 · span 282971), resolved/emphatic will (Psa 77:11 · spans 282875, 282879).
- **Coupling (corrected phrases):** memory welded to obedience (Psa 103:18 · span 269122 "keeping the covenant"), to grief (Psa 137:1 · span 273272 "the weeping"), to ordered love (Psa 137:6 · span 273290 "Jerusalem above his highest joy"), to rebellion via its failure (Psa 106:7 · span 269845 "rebelling").
- **Source:** essentially unnamed (§0.4).

Net picture: **memory is a seatless, object-directed act of will, Godward by default, that hardens into a settled disposition (the "I do not forget" vows) and whose failure (forgetting) is the engine of rebellion.**

---

## 5. What could not be derived

- **No seat anywhere** (D104 0/46): the interior organ of memory is unrecoverable from this source.
- **No intensity, specifier, or effect** (D109/D110/D111 0/46): the strength of a remembering, its qualifier, and its downstream effect are all unread.
- **Source (D103) all but absent** (2/46, edges only): what *triggers* memory is undetermined.
- **Manner unread in ~39/46.**
- **Cluster untyped for the negative pole:** all 24 shakach/olam spans are `cluster.code = null`; the term-model cannot type forgetting — a structural gap, not a reading.
- **Alien instance:** Psa 30:6 · span 276627 (olam "never") is not a memory movement and should be removed from the family (§1).
- **Agent ambiguity at Psa 8:4 · span 284919:** the memory-act is God's; only the human wonder is the coded IB (§1).
- **Network is nearly self-referential:** with self-loops excluded, only one genuine intra-family edge exists (Psa 77:11 doublet); all other pairs point outside the family, so intra-memory relations are largely underivable here.

---

## Summary
The `memory-remembrance` family is a **coherent bipolar faculty — zakar (remember, M41) against shakach (forget, cluster-null)** — read across 46 spans as a **seatless, will-driven, Godward act** that stiffens into disposition (the Psalm-119 "I do not forget" vows) and whose failure drives rebellion. Data-integrity load: **12/46 D112↔D116 swaps** (all where D112 holds a bare code), **seat "none" in every instance**, **D109/D110/D111 wholly absent**, the **negative pole entirely untyped by cluster**, one **alien instance** (olam "never", Psa 30:6), and a **near-empty within-family network** (one real edge, the Psa 77:11 doublet; all else self-loops or outward pairs).
