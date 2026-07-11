# Family analysis — `sin-guilt-iniquity` (Psalms), in isolation

> Source: `outputs/data/psalms-family-base-sources/psalms__sin-guilt-iniquity.json` only. 21 meanings · 55 instances · 32 passages. Every claim cites `reference · span_id · Dnnn(label)` into that file. British spelling. Nothing imported from outside the file.

---

## 0. Data-integrity screen (done first)

### 0.1 D112(coupling)/D116(locus) field-swap — 19 of 55 transposed
Correct order (per method) = D116 a code, D112 a phrase. **36 instances are in correct order** (D116 holds `internal:`/`external:`, D112 holds the prose phrase). **19 are swapped** (D112 holds the code, D116 holds the phrase) and must be read corrected (coupling = the phrase; locus = the code):

`Psa 103:3·269172`, `Psa 106:43·269776`, `Psa 109:14·270177`, `Psa 103:10·269067`, `Psa 107:17·269899`, `Psa 130:3·272813`, `Psa 130:8·272852`, `Psa 109:14·270182`, `Psa 103:12·269082`, `Psa 106:6·269835`, `Psa 94:23·285403`, `Psa 103:10·269062`, `Psa 104:35·269336`, `Psa 106:39·269739`, `Psa 106:6·269837`, `Psa 109:7·270344`, `Psa 106:38·269737`, `Psa 109:7·270347`, `Psa 99:8·307173`.

Example: `Psa 103:3 · span 269172 · D112(coupling)="internal:ib-state"` + `D116(locus)="paired with God's forgiving"` — swapped; read as coupling="paired with God's forgiving", locus=`internal:ib-state`. In every swapped case the code is `internal:ib-state` except `Psa 99:8·307173` (also `internal:ib-state`). No swapped instance carries an `external:` code, so the swap does not corrupt any internal/external classification here — all corrected loci resolve to `internal:ib-state`.

### 0.2 Self-loop "edges" are not real links — 142 of 177
177 total edge records. **142 are self-loop flags** (`item_type:"flag"`, `resolution:"inferred"`, `to_span` = the span's own id) — mechanical restatements of D105/D107/D112 flags, **not** network links. A further **13 are `event`/`inferred` self-loops** (operation restated on-span). **1 is `event`/`resolution:"span"` cross-span** (`Psa 65:3·281201·D106` → span 281200) — a genuine cross-span link but on an event, so excluded from the network per method. **Only 21 are genuine `pair`/`resolution:"span"` edges to a different span** (§ The network).

### 0.3 seat(D104) / manner(D108) = "none"
- **D104 seat="none" in 54 of 55.** The single filled seat: `Psa 59:12 · span 280548 · D104(seat)="the mouth / lips"` (item_type flag, inferred) — the enemies' sin located in speech.
- **D108 manner="none" in 46 of 55.** 9 carry a manner, e.g. `Psa 51:2 · span 279724 · D108(manner)="thoroughly / abundantly"`; `Psa 59:12 · span 280548 · D108(manner)="in the words of their lips"`.

### 0.4 Absent dimensions (across all 55)
**D109 intensity, D110 specifier, D111 effect, D113 prohibition are wholly absent** — no instance carries any of them. D103 source is near-absent (present on only 3). Dimensions present on all 55: D101, D102, D104, D105, D106, D107, D108, D112, D114, D115, D116.

### 0.5 Cluster NULL / T2
- **No T2 instances.**
- **4 instances have `cluster.code = null`** (the term-cluster cannot type them): `Psa 6:7·281972` (H5869 eye), `Psa 106:38·269737` (H2610 pollute), `Psa 31:10·276668` (H3615 spent), `Psa 99:8·307173` (H5949 wrongdoings). Of these, two are genuine sin/defilement (pollute, wrongdoings) and **two are not sin at all** (eye, spent — grief/depletion; see §1).
- 50 instances cluster to **M10 (Sin)**; **1 to M14 (Deceit)** — `Psa 90:8·285046` (H5956 alum, "secret sins"), `is_outlier=False`.

### 0.6 Role carries no signal
**D115(role)="characteristic" in all 55.** The role dimension does not differentiate anything in this family.

---

## 1. Coherence — does the label fit the data?

**Mostly yes, with a small fused edge.** 50/55 instances are M10 (Sin) and one more (M14 secret sins) is sin-adjacent (concealed sin). The Hebrew lexis is the expected penitential vocabulary: `avon` (H5771, 17×), `chatta't`/`chattath`/`chet` (H2403/H2399, 9×), `chata` verb (H2398, 6×), `pesha`/`pasha` (H6588/H6586, 7×), plus `aven` (H0205), `avel` (H5766), `chataah` (H2401), `ashmah` (H0819 "wrongs done"), `avah` (H5753), `tame` (H2930 unclean), `rasha` (H7563 guilty), `alilah` (H5949), `chaneph` (H2610). These form **one coherent movement: human guilt/transgression before God**.

**Two instances do NOT belong** — the keyword grouping has pulled in a distinct *grief/bodily-depletion* movement (null cluster, no sin lexeme):
- `Psa 6:7 · span 281972 · D101(sense)="eye wasting from grief"` — `D106(operation)`: "the eye itself grows weak and wastes away because of grief and the foes"; `D114`: "the interior sorrow is written on the failing eye". This is affliction, not sin.
- `Psa 31:10 · span 276668 · D101(sense)="my life is spent with sorrow"` — `D106`: "the self's life is spent with sorrow… strength failing through iniquity, bones wasting". Depletion-through-grief; sin appears only as a *cause* mentioned in the surrounding verse, not as the term itself.

These are the same body-of-a-penitent affliction motif that co-occurs in penitential psalms (Pss 6, 31, 38) but are a **separate inner-being movement** (grief eroding the body) fused in by verse/keyword adjacency. Flag as a coherence finding: 2 grief-depletion instances mis-filed under sin-guilt-iniquity.

Everything else, including the 4 null-cluster set, is genuinely within the sin field (pollute = defilement, wrongdoings = misdeeds avenged, secret sins = concealed guilt).

---

## 2. What the terms *are* (D101 sense / D102 type)

**41 distinct read-senses across 55 instances** — the family is lexically rich, not repetitive. Type distribution (D102): **state 28 · status 17 · action 8 · cognition 1 · disposition 1**.

- **State/status (45/55)** — sin as an abiding interior *condition*, not merely an act: `Psa 51:5 · span 279751 · D102(type)="status"` ("brought forth in iniquity"), `D114`: "avon shown as native, not acquired". `Psa 51:2 · span 279724 · D102="status"`, `D114`: "the ingrained perversity, deeper than a single act — needing washing, not mere pardon". This state/status dominance is the family's core anatomy claim: guilt as a *standing* of the inner being.
- **Action (8/55)** — sin as a committed deed: `Psa 51:4 · span 279738 · D102="action"` ("sinned"), `Psa 106:6 · span 269835 · D106(operation)="sin"`, `Psa 78:17 · span 283044`, `Psa 78:32 · span 283146`, `Psa 106:6 · span 269837` (avah, "commit iniquity"), `Psa 106:38 · span 269737` (pollute), and the two teaching/turning verbs at `Psa 51:13 · spans 279669/279671`.
- **Cognition (1)** — `Psa 41:4 · span 278456 · D102="cognition"`, `D106`: "healing sought with confession" (the self *acknowledging* it has sinned).
- **Disposition (1)** — `Psa 119:11 · span 271278 · D102="disposition"`, `D106(operation)="not sin"` (the settled resolve *not* to sin, word stored in the heart).

---

## 3. Whose inner being bears it (D105 bearer)

All bearers are human (God is never bearer — sin is a human property, consistent with the IB screen). But the bearer is frequently **not the psalmist's own self**:
- **The penitent / psalmist (self):** e.g. `Psa 51:2 · span 279724 · D105="the penitent"`; `Psa 38:4 · span 277969`; 8× "the penitent", 8× "the psalmist".
- **Third parties (enemies, fathers, the wicked, fools, the city):** `Psa 109:14 · span 270177 · D105="the enemy's fathers"`; `Psa 59:12 · span 280548 · D105="the enemies"`; `Psa 53:1 · span 279888 · D105="the fools"`; `Psa 55:10 · span 280038 · D105="the city's wicked"`; `Psa 106:43 · span 269776 · D105="the fathers"`.
- **Corporate "us/we":** `Psa 90:8 · span 285046 · D105="we (mankind)"`; `Psa 79:8 · span 283540 · D105="us"`; `Psa 106:6 · D105="we and our fathers"`; `Psa 65:3 · span 281201 · D105="the worshippers"`.

All bearers are `resolution:"inferred"` flags (no D105 is asserted on the surface word). So the *ownership* of sin is uniformly a reader inference, never lexically explicit.

---

## 4. What moves it — operation (D106), target (D107), source (D103), manner (D108)

### D106 operation — sin as a thing done *to* by God, or done *by* the self
The dominant operation is **God acting on the guilt** (forgive / blot out / atone / not-repay / bring back):
- `Psa 103:3 · span 269172 · D106(operation)="have iniquity forgiven"`
- `Psa 51:1 · span 279643 · D106` blotting of transgressions (pesha); `Psa 51:9 · span 279780` "blot out all my iniquities"
- `Psa 65:3 · span 281201 · D103(source)="which God atones (v3)"` (pair→281200); `Psa 79:9 · span 283554` atone
- `Psa 78:38 · span 283178` "atoned for their iniquity"; `Psa 85:2 · span 284184` "covered all their sin"
Secondary: **guilt bearing its own judgment / weight**: `Psa 106:43 · span 269776 · D114`: "the guilt that sank them, sin bearing its own judgment"; `Psa 38:4 · span 277969 · D116(locus)="iniquities-burden"` (the burden too heavy). And **confession**: `Psa 38:18`, `Psa 51:3 · span 279733 · D114`: "the chatta't he begged cleansed".

### D107 target — sin is oriented *Godward*
Of 55: **15 none**, but the filled targets are overwhelmingly toward God: **"before God" 6, "against God" 5, "by God" 2, "chastened by God" 2, "not repaid by God" 2**, plus singletons "exposed before God", "remembered by God", "redeemed by God", "avenged by God", "against God ('you only')". E.g. `Psa 51:4 · span 279738 · D107="against God ('you only')"`. This is the family's second core claim: **guilt is a relational vector aimed at / exposed before God**, not a private stain.

### D103 source — present on only 3, all Psalm 51 / 65 pair-links
- `Psa 51:1 · span 279643 · D103(source)="appealed against God's steadfast love and abundant mercy (v1)"` (pair→279637)
- `Psa 51:4 · span 279738 · D103(source)="confessed so that God is shown justified when he judges (v4)"` (pair→279744)
- `Psa 65:3 · span 281201 · D103(source)="which God atones (v3)"` (pair→281200)
Source is otherwise unrecorded — the *origin* of sin is largely not derivable from this file (except the birth-origin note at `Psa 51:5 · span 279751 · D114`: "avon… native, not acquired").

### D108 manner — sparse (9/55)
E.g. `Psa 51:2 · span 279724 · D108="thoroughly / abundantly"`; `Psa 59:12 · span 280548 · D108="in the words of their lips"`.

---

## 5. The network (genuine `pair`/`span` edges only — 21)

Almost the entire network is on **D112(coupling)** (18 edges) plus **D103(source)** (3 edges). Directions are all `null`; edges are effectively **undirected couplings**, many **reciprocal**. The network is **near-entirely intra-psalm** — it links co-occurring sin-terms *within one psalm*, not across the corpus.

**Psalm 51 is the dense hub** (the great penitential psalm; the avon/chatta't/pesha triad cross-linked):
- avon chain: `279724 ↔ 279751` (v2 ↔ v5, D112), `279783 → 279724` (v9 → v2), `279780 → 279783` (v9), `279752 → 279750` (v5 chet).
- chatta't chain: `279728 ↔ 279733` (v2 ↔ v3, D112).
- pesha chain: `279643 ↔ 279732` (v1 ↔ v3, D112) + `279643 → 279637` (D103 source).
- v4 sinned: `279738 → 279740` (D112) + `279738 → 279744` (D103 source).
- v13 teaching: `279669 ↔ 279671` (transgressors ↔ sinners, D112).

**Other psalms — isolated single pairs** (sparse, one coupling each): `Psa 49:5 · 279387 → 279384`; `Psa 55:10 · 280038 → 280039`; `Psa 59:3 · 280608 → 280609`; `Psa 59:12 · 280548 → 280553`; `Psa 65:3 · 281201 → 281200` (D103); `Psa 69:5 · 281879 → 281878`; `Psa 53:1 · 279888 → 279887`.

**Network shape:** one rich hub (Ps 51) and a scatter of dyads. No cross-psalm edges, no edges on any dimension other than coupling and source. The "network" is therefore a set of **within-passage sin-term co-references**, not a corpus-wide inner-being web.

---

## 6. The interior anatomy the data actually names

Assembling only the *filled* seats/sources/couplings:
- **Seat:** essentially unlocated. Only one seat is named in 55 — `Psa 59:12 · span 280548 · D104="the mouth / lips"` (the enemies' sin of speech). No heart / soul / spirit / ruach / eye is named *as the seat of sin* anywhere. (The "eye" of `Psa 6:7·281972` is the organ of *grief*, not a sin-seat, and is null-cluster.)
- **Locus (corrected D116):** uniformly `internal:ib-state` — every instance that resolves to a code resolves to *internal*; three action-context items read `external:god`/`external:person` in the correct-order set (`Psa 51:4·279738`, `Psa 78:17·283044`, `Psa 78:32·283146`, `Psa 51:13·279671`, `Psa 119:11·271278`) marking sin *against/toward* an external party. So sin sits **inside the inner being** as a state, but *points outward* to God/others.
- **Coupling:** sin-terms bind chiefly **to one another within a psalm** (§5) and to **God's answering act** (forgiving/atoning/covering) — `Psa 103:3·269172·D116="paired with God's forgiving"` (corrected coupling); `Psa 85:2·284184` "paired with the sin covered"; `Psa 90:8·285046·D112="paired with the secret sins"`.

**Net anatomy:** the family names sin as an **internal, abiding condition (state/status) of the human inner being, borne by self or others, oriented and exposed Godward, coupled to God's forgiving/atoning act and to sibling sin-terms in the same psalm** — but it does *not* localise sin to any interior organ (heart/soul/spirit), and does not record its intensity, effect, or origin.

---

## 7. What could not be derived from this source

1. **Interior seat of sin** — unlocated in 54/55 (D104="none"); the one filled seat is speech, not a faculty.
2. **Intensity (D109), specifier (D110), effect (D111), prohibition (D113)** — wholly absent; the *degree*, *sub-type*, *downstream effect*, and any *prohibition framing* of sin cannot be read here.
3. **Source/origin (D103)** — present on only 3 instances (all Ps 51/65 pair-links); the origin of sin is otherwise not derivable (bar the single birth-origin discovery note at `Psa 51:5·279751·D114`).
4. **Manner** — none for 46/55.
5. **Directionality of the network** — all 21 genuine edges have `direction=null`; the couplings are undirected, so no ordering (cause→effect) among coupled sin-terms is derivable.
6. **Role differentiation** — D115 is "characteristic" for all 55; carries no analytic signal.
7. **Bearer certainty** — every D105 is `inferred`; whose sin it is, is always a reader inference, never surface-explicit.
8. **Two mis-filed grief instances** (`Psa 6:7·281972`, `Psa 31:10·276668`) are not sin at all and should not be read as evidence for this family.

---

## 8. Summary

`sin-guilt-iniquity` (Psalms): 21 meanings / 55 instances, a **coherent M10(Sin) penitential-vocabulary family** (50 M10 + 1 M14 secret-sins + 4 null, 2 of which are mis-filed grief). The data models **sin as an internal, abiding state/status of the inner being (D102 state 28 / status 17), borne by self and others (all D105 inferred), oriented and exposed Godward (D107 dominantly "before/against God"), and coupled to God's forgiving/atoning act plus sibling sin-terms within a single psalm** (network = 21 undirected pair edges, hub = Psalm 51). Integrity caveats: **19/55 D112↔D116 swapped** (all corrected loci = `internal:ib-state`); **142/177 edges are self-loops**, not links; **seat unlocated in 54/55**; **D109/D110/D111/D113 entirely absent**; **role uniform**; **2 grief instances fused in by keyword adjacency**.
