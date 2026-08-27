# Family analysis — Psalms `joy-gladness` (in isolation)

> Source: `verse-analysis/psalms/_base-sources/psalms__joy-gladness.json` only. Scope = that one file. 27 meanings · 95 instances · 62 passages · 16 distinct lemmas. Every claim cited `reference · span_id · Dnnn(label)`. Method: `Workflow/methodology/wa-psalms-family-analysis-method-v1-20260711.md`.

---

## 0. Data-integrity screen (done first)

### 0.1 D112 (coupling) / D116 (locus) field-swap — **33 of 95 instances transposed**
The method's correct order is D116 = an `internal:`/`external:` code, D112 = a prose phrase. In **33** instances that order is inverted: D112 carries the code and D116 carries the prose — read them corrected. The remaining **62** are already correct (D116 = code, D112 = phrase). Zero instances are ambiguous (both/neither a code).

The 33 swapped instances (D112 wrongly holds the code):
`Psa 105:38·269487`, `Psa 107:30·269969`, `Psa 107:42·270033`, `Psa 109:28·270286`, `Psa 118:24·271120`, `Psa 122:1·272385`, `Psa 92:4·285212`, `Psa 97:8·285697`, `Psa 104:34·269334`, `Psa 105:3·269477`, `Psa 106:5·269826`, `Psa 89:42·284768`, `Psa 97:12·285647`, `Psa 118:24·271119`, `Psa 97:8·285700`, `Psa 107:22·269937`, `Psa 126:2·272566`, `Psa 126:5·272584`, `Psa 126:6·272593`, `Psa 137:6·273297`, `Psa 97:11·285644`, `Psa 100:1·268779`, `Psa 95:1·285445`, `Psa 98:4·285749`, `Psa 98:6·285767`, `Psa 94:3·302415`, `Psa 100:2·268785`, `Psa 105:43·269522`, `Psa 132:9·272991`, `Psa 89:16·284568`, `Psa 126:3·272580`, `Psa 104:15·269240`, `Psa 113:9·270781`.

Example: `Psa 105:38 · span 269487 · D112(coupling)="internal:ib-state"` (a code — belongs in D116) while `D116(locus)="paired with the dread that fell on them"` (a phrase — belongs in D112). Corrected: locus = `internal:ib-state`, coupling = *paired with the dread*.

**After correction, D116 locus resolves cleanly across all 95:** `internal:ib-state` = 61, `external:god` = 34. No instance is left without a locus code once the swap is undone.

### 0.2 Self-loop "edges" are not links — the network is tiny
290 raw edge records; **244 are non-network** (`item_type:"flag"`, `resolution:"inferred"`, `from_span:null` or `to_span`=own span — these merely re-flag the instance's own bearer/target/coupling). Only **46** are genuine `pair` edges (`resolution:"span"`, to a different span). Of those 46, **27 point OUT of this family** (to a co-passage span that is not a joy-gladness instance) and only **19 point to another in-family joy span**. Those 19 reduce to **9 distinct span-pairs**, almost all bidirectional D112(coupling) welds between two joy-verbs standing in the same verse:
- `Psa 48:11 · 279180↔279183 · D112(coupling)`
- `Psa 53:6 · 279952↔279954 · D112(coupling)`
- `Psa 68:3 · 281584↔281585` and `281588↔281589 · D112/D107/D108`
- `Psa 70:4 · 282020↔282021 · D112(coupling)`
- `Psa 63:11 · 281031↔281035 · D112(coupling)`
- `Psa 64:10 · 281099↔281105 · D112(coupling)`
- `Psa 43:4 · 278664↔278665 · D112(coupling)`
- `Psa 51:8 · 279772↔279773 · D112(coupling)`

**Finding:** the intra-family network is sparse and local — it records verb-doubling *within a single verse* (glad-and-rejoice, shout-and-exult), not any cross-passage structure. There is no directed, corpus-spanning graph here.

### 0.3 seat (D104) / manner (D108) = "none"
- **seat=none in 92 of 95.** Only 3 name an interior seat: `Psa 51:8 · 279773 · D104(seat)="the bones (God broke)"`, `Psa 71:23 · 282154 · D104="the lips"`, `Psa 63:5 · 281067 · D104="the lips"`. Joy is overwhelmingly recorded **without an anatomical seat**.
- **manner=none in 87 of 95.** The 8 filled: `Psa 45:8·D108="by stringed instruments"`, `Psa 46:4·D108="by the river's streams"`, `Psa 67:4·D108="singing for joy"`, `Psa 47:1·279094·D108="shouting, with clapping hands"`, `Psa 45:15·D108="led to the king's palace"`, `Psa 71:23·282154·D108="his redeemed soul rejoicing"`, `Psa 43:4·D108="exceeding / of my gladness"`, `Psa 68:3·281588·D108="with joy"`.

### 0.4 Absent dimensions (0 of 95)
**D109 intensity, D110 specifier, D111 effect, D113 prohibition are absent from every instance.** D103 source is present in only **11 of 95** (see §5). D101 sense, D102 type, D104 seat, D105 bearer, D106 operation, D107 target, D108 manner, D112 coupling, D114 discovery, D115 role, D116 locus are on all 95.

### 0.5 Cluster NULL / T2
- **Cluster NULL:** 1 meaning — `H1319:gladnew` (`Psa 40:9 · D101="I told the glad news, I did not restrain my lips"`); its term-cluster cannot type it (see §1.3).
- **Cluster T2:** none.

---

## 1. Coherence — does "joy-gladness" fit its data?

**Partly.** The keyword grouping fuses one dominant inner-being movement with three adjacent-but-distinct ones. By term-cluster:

| cluster | meanings | instances | reading |
|---|---|---|---|
| **M04 (Joy)** | 19 | 74 | the core movement — the family's centre of gravity |
| **M42 (Speech)** | 4 | 11 | *voiced* joy — `rinnah`/`ranan`, joy that becomes shout/song |
| **M22 (Praise)** | 2 | 7 | `rua`/`terua`, the joyful **noise/shout** (`H7321`) |
| **M08 (Pride)** | 1 | 2 | `halal` = exult/**glory/boast** (`H1984`) |
| **NULL** | 1 | 1 | `H1319 basar` = **announce glad news** (see §1.3) |

### 1.1 The coherent core (M04, 74/95)
19 M04 meanings across lemmas `samach`(H8055), `gil`(H1523), `simchah`(H8057), `alats`(H5937), `sason`(H8342), `alaz`(H5970/H5937), `siys`(H7797), `giyl`(H1524) form **one** movement: an interior affective **state** (`D102=state`, 27×) or **affect** (17×) breaking into **action** (38×) — gladness that is felt and then enacted. E.g. `Psa 16:9 · D101(sense)="glad"·D102="state"` beside `Psa 9:2·279? · D112 corrected "glad-and-exult"`.

### 1.2 The fused adjacents — three distinct movements, named
The label "joy-gladness" pulls in the *expression* of joy, which the data types as different movements:
- **Voiced joy → M42 Speech (11):** the reader's own D114 notes flag the shift to utterance — `Psa 126:2 · 272566 · D114(discovery)="the joy that bursts into song, the tongue loosed"`; `Psa 132:9 · 272991 · D114="joy bursting into shout"`. `rinnah`/`ranan` name **joy-as-sound**, not the interior state.
- **Joyful noise → M22 Praise (7):** `H7321 rua` (`Psa 47:1 · 279094 · D101="shout for joy"`, `Psa 100:1 · 268779`) — the acoustic act of acclamation.
- **Exultant boast → M08 Pride (2):** `Psa 63:11 · 281031 · D101="exult/glory (halal)"`, `Psa 64:10 · 281099` — `halal` = *glad boasting of the vindicated in God* (D114). This edges into self-display, a different interior register from `samach`.

### 1.3 One member does not belong
`Psa 40:9 · span (H1319:gladnew) · D101="I told the glad news, I did not restrain my lips"` (cluster NULL, `basar`). D114 reads it as **the operation of proclaiming deliverance** — a Speech/announcement act, keyword-captured only through the English "glad." It is the family's clearest mis-grouping.

### 1.4 Two inversions of the affect (bearer is not the godly IB)
The family label assumes *good* joy, but three instances carry the affect on hostile/ironic bearers — a first-class datum:
- `Psa 105:38 · 269487 · D105(bearer)="the Egyptians"` — *gladness born of terror* (D114), relief not delight.
- `Psa 89:42 · 284768 · D105="the king's enemies"` — *the malicious joy of the foes at the king's ruin* (D114).
- `Psa 94:3 · 302415 · D105="the wicked"` — *the wicked's arrogant triumph, gloating* (D114).
These are genuine inner-being data (human affect) but are **counter-movements** to the family's assumed direction; the grouping does not distinguish them.

**Verdict:** the M04 core (74) is a single coherent movement; M42/M22/M08/NULL (21) are the *expression and boast* of joy plus one announcement verb — related but distinct. The keyword grouping has fused an interior state with its vocal/proud outflow, and swept in three inverted-affect bearers. Report the core and the fusion together.

---

## 2. The core movement — what the affect is (D101/D102)

Joy in this file is typed as, in order of frequency (D102): **action 38, state 27, affect 17, status 11, disposition 1, volition 1**. So the data reads joy less as a static feeling than as **something the IB does** (38 action) rising out of **something it is** (27 state + 17 affect). The single **disposition** and single **volition** are the outliers: joy as settled bent vs joy as willed choice — e.g. the summoned "be glad" imperatives.

The read_characteristic senses cluster into: *glad / be glad* (`samach`), *rejoice / exult* (`gil`, `alats`, `alaz`), *joy / gladness* (nominal `simchah`, `sason`), *shout/ring for joy* (`rinnah`, `ranan`, `rua`), *glory/exult* (`halal`). Cited at `Psa 16:9`, `Psa 9:2`, `Psa 51:8·279776`, `Psa 32:11`, `Psa 47:1·279094`, `Psa 63:11·281031` respectively.

## 3. Whose inner being (D105 bearer)

Bearer is always a human/human-collective IB (never God's own affect); `resolution:"inferred"` where the text does not name them. Dominant bearers: **the psalmist 19**, **the worshippers 8**, **the righteous 8**, **the king 4**, then a long tail of covenant-people collectives (the upright, the humble, the penitent, all who seek God, Zion's people, Israel, the reapers/sower of `Psa 126:5-6`). Three inverted bearers (Egyptians / enemies / wicked, §1.4). **Joy in Psalms is corporate before it is private** — the single largest non-psalmist share is worshipping/righteous collectives.

## 4. What it does and toward what (D106 operation / D107 target)

- **Operation (D106, all 95):** the verbs of joy — *be glad, rejoice, exult, shout for joy, make glad*. Where joy doubles inside a verse, both verbs are welded by the D112 in-family edges of §0.2 (e.g. `Psa 68:3 · 281588→281589 · D106/D107/D108`).
- **Target (D107, all 95):** the object joy reaches for. Frequently God or God's acts, inferred: `Psa 105:38 · 269487 · D107="when Israel departed"`; targets of salvation, God's judgments, God's name recur (see §5 sources, which name the same events as cause).

## 5. What moves it — source (D103, only 11/95)

Where a cause is recorded, **it is always God or God's act** — joy in this family is not self-generated:
- `Psa 46:4 · D103="God's help and presence in her midst"`
- `Psa 67:4 · 281409 · D103="because God judges the peoples with equity"`
- `Psa 58:10 · 280456 · D103="because there is a God who judges on earth"`
- `Psa 66:6 · 281364 · D103="who turned the sea to dry land and rules by his might"`
- `Psa 48:11 · 279183 · D103="God's judgments, the occasion of joy"`
- `Psa 51:8 · 279776 · D103="the bones God himself had broken (chastening) may now exult"`
- `Psa 53:6 · 279952 · D103="when God restores his people's fortunes"`
- `Psa 51:12 · 279662 · D103="the joy OF God's salvation"`
- `Psa 71:23 · 282154 · D103="his soul which God has redeemed"`
- `Psa 45:7 · 278994 · D103="conferred by God's anointing"`
- `Psa 43:4 · 278665 · D103="led to by God's light and truth"`

**84 of 95 record no source** — the affect is registered without stating its cause. This is the single largest derivability gap in the file (§8).

## 6. Locus and coupling — where joy sits, what it is bound to (D112/D116, corrected)

- **Locus (D116, corrected code):** `internal:ib-state` 61, `external:god` 34. Two-thirds sit as an interior state of the bearer; a third are located toward/in God (joy *in the LORD*), consistent with §5's God-as-source.
- **Coupling (D112, corrected phrase):** joy is bound most often to **another joy-word in the same verse** (*paired with rejoicing / exulting / singing for joy* — the verb-doubling of §0.2), and secondarily to its **occasion**: `Psa 105:38 · 269487 · D112="paired with the dread that fell on them"`, `Psa 122:1 · 272385 · D112="paired with the pilgrimage to Jerusalem"`, `Psa 90:15 · D112="paired with the days of affliction"`, `Psa 97:8 · 285697 · D112="paired with hearing"`, `Psa 105:3 · 269477 · D112="paired with the seeking heart"`. A handful name a compound state directly: `Psa 32:11 · D112="glad-and-shout"`, `Psa 9:2 · D112="glad-and-exult"`, `Psa 19:8 · D112="heart-rejoices"`.

## 7. Role (D115) and the network

- **Role: `characteristic` in all 95** — no qualifier, no standalone. Every joy-instance is read as a characteristic of the IB.
- **Network:** as established in §0.2, only 9 real in-family span-pairs, all local within-verse couplings; 27 genuine edges reach out to co-passage non-joy spans (unread from this file — those spans are outside scope). There is **no directed cross-passage joy graph** in this data.

## 8. The interior anatomy the data actually names

Assembling only the filled seats/sources/couplings, the file names a **thin** anatomy:
- **Seats (3):** the **bones** (`Psa 51:8·279773`), the **lips** (`Psa 71:23·282154`, `Psa 63:5·281067`) — joy reaches the frame and the mouth; no heart/soul/spirit seat is ever filled for this family (despite `Psa 16:9`/`Psa 19:8` speaking of the heart in surface text, D104 there = none).
- **Cause (11):** exclusively God's acts (§5).
- **Binding (D112):** joy to joy (verb-doubling) and joy to its occasion.
- **Locus:** interior state (61) or God-directed (34).

## 9. What could NOT be derived from this source

1. **Intensity (D109), specifier (D110), effect (D111), prohibition (D113) — 0/95.** No gradation, no sub-typing, no downstream effect, no proscription is recorded anywhere. Joy's *degree* and *consequence* are unread.
2. **Source (D103) missing in 84/95** — for most instances the file does not say what moves the affect.
3. **Seat (D104) missing in 92/95; manner (D108) in 87/95** — joy is almost always located nowhere anatomically and enacted in no stated manner.
4. **The genuine cross-family edges (27)** point to spans this file does not contain — their far ends are not derivable here.
5. **The D112/D116 swap (33/95)** had to be corrected by rule; the file as stored mislabels which field is code vs phrase.
6. **Cluster typing fails for 1 meaning** (`H1319 basar`, NULL) and mis-fits at least 8 (M42/M22/M08 = expression/boast, not the interior state).
7. **Three inverted-affect bearers** (Egyptian/enemy/wicked joy) are grouped under a positive family label with no field distinguishing direction.

---

## Summary

`joy-gladness` = **27 meanings / 95 instances / 62 passages / 16 lemmas**, cited throughout. A coherent **M04 core (74)** reads joy as a God-caused interior affect (`internal:ib-state` 61) that the human/corporate IB (psalmist, worshippers, righteous) both **is** (state/affect 44) and **does** (action 38), bound within-verse to parallel joy-verbs; but the keyword grouping **fuses** it with *voiced joy* (M42, 11), *joyful noise* (M22, 7), *exultant boast* (M08, 2) and one *announce-glad-news* verb (NULL, 1), and sweeps in **three inverted bearers** (Egyptians/enemies/wicked). Data is thin on anatomy: **seat none 92/95, manner none 87/95, source recorded only 11/95, and D109/D110/D111/D113 entirely absent**; the network is 9 local within-verse pairs only; **33/95 carry the D112/D116 swap** (corrected here); all 95 roles = `characteristic`.
