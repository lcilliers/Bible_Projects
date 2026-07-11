# Family analysis — `strength-courage-steadfastness` (Psalms), in isolation

> Scope: `outputs/data/psalms-family-base-sources/psalms__strength-courage-steadfastness.json` only. 7 meanings · 8 instances · 7 passages. Every claim cited `reference · span_id · Dnnn(label)`. Nothing imported from outside this file.

Instance roster (span → ref → sense):
- 270102 · Psa 108:13 · valiantly (chayil) — H2428, M23
- 280798 · Psa 60:12 · valiantly / with strength (chayil) — H2428, M23
- 269954 · Psa 107:26 · courage (nephesh) — H5315, **M47 outlier**
- 281127 · Psa 64:5 · hold fast (chazaq) — H2388, M23
- 284107 · Psa 84:5 · strength (oz) — H5797, M23
- 284122 · Psa 84:7 · strength (chayil) — H2428, M23
- 284485 · Psa 88:4 · strength (eyal) — H0353, M23
- 276809 · Psa 31:24 · be strong / take courage (chazaq) — H2388, M23

---

## 0. Data-integrity screen (done first)

**D112(coupling)/D116(locus) field-swap — 2 instances transposed.** Correct order = D116 a code, D112 a phrase. Swapped where D116 holds a phrase and D112 holds a code:
- **270102 · Psa 108:13** — D116(locus)="paired with the vanity of human help" (phrase) · D112(coupling)="external:god" (code, `flag`/inferred). **Transposed.** Read corrected: locus = `external:god`; coupling = "paired with the vanity of human help".
- **269954 · Psa 107:26** — D116(locus)="paired with the melting" (phrase) · D112(coupling)="internal:ib-state" (code, `flag`/inferred). **Transposed.** Read corrected: locus = `internal:ib-state`; coupling = "paired with the melting".

The other six are correctly ordered (D116 a code, D112 a phrase/pair): 280798, 281127, 284107, 284122, 284485, 276809. Note the two swapped instances are exactly the two whose D112 is a `flag`/`inferred` item — the swap co-occurs with inferred coupling.

**Self-loop "edges" are not real links.** Genuine network edges = `pair`/`resolution:"span"` to a *different* span. Screening all 8 edge-sets:
- **270102** — 3 edges (D105 bearer, D107 target, D112 coupling), all `flag`/inferred with `to_span`=270102 (own id) = self-loops. **No genuine edge.**
- **280798** — D103 source `pair` 280798→**280800**, D108 manner `pair` 280798→**280800**, D112 coupling `pair` 280798→**280793** are genuine; D105 bearer is a self-loop. **3 genuine.**
- **269954** — 3 edges, all self-loops (to_span=269954). **No genuine edge.**
- **281127** — D103 source `pair` 281127→**306458**, D107 target `pair` 281127→**281128**, D112 coupling `pair` 281127→**281128** genuine; D105 bearer self-loop. **3 genuine.**
- **284107, 284122, 284485, 276809** — 3 edges each, all self-loops. **No genuine edge.**

**Every genuine edge points OUTSIDE this file.** Target spans (280800, 280793, 306458, 281128) are none of the eight family spans. The family therefore has **zero intra-family edges** — the network is entirely outward and unresolvable within scope. Only 2 of 8 instances (280798, 281127) carry any genuine relation at all.

**seat(D104)/manner(D108)="none".**
- D104 seat = "none" in **all 8** instances (270102, 280798, 269954, 281127, 284107, 284122, 284485, 276809). No interior seat is ever filled.
- D108 manner = "none" in **7 of 8**; filled only at 280798 · Psa 60:12 · D108(manner) `pair` "with God, who treads down the foes".

**Absent dimensions (across all 8 instances).** D109 intensity, D110 specifier, D111 effect, D113 prohibition are **wholly absent** — no instance carries them. D103 source present in only 2 of 8 (280798, 281127). Present dimensions everywhere: D101, D102, D104, D105, D106, D107, D108, D112, D114, D115, D116.

**Cluster NULL / T2.** None NULL, none T2. Six meanings sit in **M23(Strength)**; one — 269954 · Psa 107:26 · courage(nephesh), H5315 — is flagged `is_outlier:true` in **M47(Constitution)** (`outlier_note`: family expects M23, term-cluster is M47). This is the one place the term-cluster diverges from the family.

**Bearer(D105) — all inferred.** All 8 bearers are `flag`/`resolution:"inferred"`; no bearer is explicitly named on the span. Bearers span "we (with God)" (270102), "the people" (280798), "the sailors" (269954), "the wicked" (281127), "the pilgrim(s)" (284107, 284122), "the psalmist" (284485), "those who wait" (276809).

---

## 1. Coherence — does the label fit its data?

**Finding: the keyword grouping fuses at least three distinct, near-antonymic inner-being movements. The label "strength-courage-steadfastness" fits only loosely (all touch a strength lexeme) but conflates polarity, moral valence, and bearer.**

Distinct movements evidenced:

**(a) God-grounded strength / valour (positive) — 5 instances.**
- 270102 · Psa 108:13 · D114(discovery) "the courage that is God's gift, valour grounded not in man but in him"; D116(locus, corrected)=external:god.
- 280798 · Psa 60:12 · D114(discovery) "God-founded courage… confidence in God, not self-confidence"; D103(source) "because it is God who treads down our foes".
- 284107 · Psa 84:5 · D101(sense) strength(oz); D114(discovery) "reliance on God as one's power"; D116(locus)=external:god.
- 284122 · Psa 84:7 · D101(sense) strength(chayil); D114(discovery) "mounting vigour of the pilgrim, renewed… as Zion nears".
- 276809 · Psa 31:24 · D102(type) volition; D114(discovery) "commanding the waiting interior to summon strength; hope braced with courage".

**(b) Failure / absence of strength (negative) — 2 instances.**
- 269954 · Psa 107:26 · D106(operation) "have courage melt"; D114(discovery) "the inmost self unnerved, heart failing".
- 284485 · Psa 88:4 · D106(operation) "have no strength"; D114(discovery) "utter powerlessness of the sufferer, vitality gone".

**(c) The wicked's resolute clinging to evil (moral inverse) — 1 instance.**
- 281127 · Psa 64:5 · D105(bearer) "the wicked"; D106(operation) "hold fast / strengthen themselves in"; D107(target, `pair`) "their evil purpose"; D114(discovery) "resolute, mutually-encouraged clinging to wickedness… God's counter-arrow will shatter".

The three groups are pulling in opposite directions: (a) is strength *given by and leaning on God*; (b) is strength *collapsing/absent*; (c) is a *self-strength weaponised for evil* in the enemy. The label's "steadfastness" strand is thinly represented and split across polarities — steadfast hope in waiting (276809, positive) vs. steadfast entrenchment in evil (281127, negative). No single "steadfastness" movement holds. Type (D102) is likewise scattered — disposition (270102, 284107), action (280798, 281127), faculty (269954), state (284122, 284485), volition (276809) — with no affect/cognition/status present; the grouping is lexical (a strength-word keyword), not a unified IB motion.

---

## 2. The movements/operations evidenced (cited)

### 2.1 Valour that is God's, not man's — the "do valiantly" pair (chayil, H2428)
Two near-identical war-close verses:
- 280798 · Psa 60:12 · D101(sense) "valiantly / with strength (chayil)"; D102(type) action; D106(operation) "do valiantly / act with valor"; D108(manner, `pair`) "with God, who treads down the foes"; D103(source, `pair`) "because it is God who treads down our foes"; D112(coupling, `pair`) "the positive counterpart to man's vain salvation (v11)".
- 270102 · Psa 108:13 · D101(sense) "valiantly (chayil)"; D102(type) **disposition** (differs from 280798's *action*); D106(operation) "act valiantly"; D107(target, inferred) "through God"; D116(locus, corrected)=external:god; D112(coupling, corrected)="paired with the vanity of human help".
The movement: human valour is *enacted* but *sourced and manner-ed in God* — courage is a disposition/act whose power sits `external:god`. The two share verse text ("With God we shall do valiantly…") but the ledger types them differently (action vs disposition) — a captured inconsistency, not a difference in the text.

### 2.2 Strength as leaning-on-God and mounting vigour (Psa 84)
- 284107 · Psa 84:5 · D101(sense) strength(oz); D102(type) disposition; D106(operation) "find strength"; D107(target, inferred) "in God"; D116(locus)=external:god; D114(discovery) "the inner leaning that sustains the journey".
- 284122 · Psa 84:7 · D101(sense) strength(chayil); D102(type) state; D106(operation) "go from strength to strength"; D107(target, inferred) "toward God"; D116(locus)=internal:ib-state; D114(discovery) "renewed not drained".
Within one passage (1737): strength first as an *outward-anchored disposition* (locus external:god) then as an *internal state* that increases toward God — a movement from reliance to accumulating vigour.

### 2.3 Strength as exhorted volition in waiting (Psa 31:24)
- 276809 · Psa 31:24 · D102(type) **volition**; D106(operation) "the self exhorts all who wait for the LORD to be strong and let their heart take courage — self-and-communal command to steadfast hope"; D112(coupling, corrected)="strong-in-waiting"; D114(discovery) "hope braced with courage". The only *volitional/imperative* instance — strength commanded, not possessed.

### 2.4 The collapse and absence of strength
- 269954 · Psa 107:26 · D102(type) faculty; D106(operation) "have courage melt"; D107(target, inferred) "in their plight"; D116(locus, corrected)=internal:ib-state; D114(discovery) "the inmost self unnerved". Courage as a *faculty that liquefies* under terror.
- 284485 · Psa 88:4 · D102(type) state; D106(operation) "have no strength"; D107(target, inferred) "against death"; D112(coupling) "paired with being counted dead"; D114(discovery) "utter powerlessness… vitality gone". Strength as a *state entirely absent* at death's edge.
These are the negative pole — the same lexical field naming the *evacuation* of strength.

### 2.5 The enemy's self-hardening (Psa 64:5)
- 281127 · Psa 64:5 · bearer "the wicked"; D106(operation) "hold fast / strengthen themselves"; D107(target, `pair`) "their evil purpose"; D103(source, `pair`) "until God shoots his arrow at them (v7)"; D114(discovery) "mutually-encouraged clinging to wickedness". A steadfastness turned malignant — the only bearer that is not the faithful/suffering self, and the only instance whose *source* is a coming judgement rather than God's aid.

---

## 3. The network (genuine `pair` edges only)

Two nodes carry genuine relations; both point **outside the file** (targets unresolvable within scope):

- **280798 · Psa 60:12** — D103(source) →280800; D108(manner) →280800; D112(coupling) →280793. The "do valiantly" act is bound (source + manner) to the *same external span* 280800 (God treading the foes) and coupled to 280793 (the vain human-salvation counterpart, v11).
- **281127 · Psa 64:5** — D103(source) →306458 (the coming divine arrow, v7); D107(target) →281128; D112(coupling) →281128. The wicked's holding-fast targets and is coupled to *the same external span* 281128 (their evil purpose).

Observations: the network is **sparse (2/8 nodes), outward-only, and undirected** (`direction:null` on every edge). No two family spans link to each other. The two related nodes sit at opposite poles — God-grounded valour (280798) and entrenched evil (281127) — and neither connects to the five God-grounded-strength nodes (270102, 284107, 284122, 284485, 276809), which are relationally inert (self-loops only). The interior "web" this family would contribute is therefore not evidenced here; it lives in spans not in scope.

---

## 4. The interior anatomy the data actually names

Assembling only filled structural dimensions:

- **Seats (D104):** none — the interior *location* is unnamed in all 8, even where the verse text supplies one. Psa 31:24 ("let your **heart** take courage", 276809) and Psa 84:5 ("in whose **heart**", 284107) name the heart in the verse and D114, yet D104 seat="none". The anatomy is textually present but **not captured** — a derivable-but-underfilled gap.
- **Loci (D116, corrected):** `external:god` (270102, 284107) vs `internal:ib-state` (269954, 280798, 281127, 284122, 284485, 276809). The one real structural axis the data names: strength either seated *outside in God* or held *as an internal state* — split 2 external / 6 internal.
- **Sources (D103, only 2):** 280798 "God who treads down our foes"; 281127 "God's arrow (v7)". In both, the mover is a *divine act* — aid for the faithful, judgement for the wicked.
- **Manner (D108, only 1):** 280798 "with God, who treads down the foes".
- **Bearers (D105):** all human (faithful, pilgrims, psalmist, sailors, the wicked, the waiting community) — the family stays within the human IB throughout; God appears as arena/source/locus, never as bearer. All inferred.
- **Role (D115):** "characteristic" in all 8 — no qualifiers, no standalones.

Named interior, therefore, reduces to: a strength/courage that is **either God-anchored (external locus) or an internal state**, moved (where moved at all) by **God's action**, borne by the **human self or the enemy**, and typed inconsistently across disposition/action/state/faculty/volition — with the seat itself never specified.

---

## 5. What could not be derived (flagged)

1. **All seats unknown** — D104="none" ×8; heart is named in the text at Psa 31:24 (276809) and Psa 84:5 (284107) but left uncaptured. Interior location is not derivable from the ledger.
2. **No intensity, specifier, effect, or prohibition** — D109/D110/D111/D113 absent across all 8; degree, qualification, outcome, and any negative-command reading are not derivable.
3. **Source/manner mostly empty** — D103 in 2/8, D108 in 1/8; for six instances what moves the strength and how is not stated.
4. **Network unresolvable in scope** — the only genuine edges (from 280798, 281127) point to spans 280800/280793/306458/281128, none of which are in this file; their content cannot be read here. Five of eight instances carry no genuine relation at all.
5. **Two D112/D116 swaps** (270102, 269954) must be read corrected; taken at face value they misattribute coupling and locus.
6. **Bearers all inferred** — no bearer is explicitly on the span; each is a contextual inference, not a direct datum.
7. **Type conflict on identical text** — 270102 (disposition) vs 280798 (action) code the same verse-formula differently; the "true" type is not derivable from the file.
8. **Outlier cross-cluster** — 269954 (courage/nephesh) sits in M47(Constitution) not M23; whether it belongs to this family is flagged uncertain by the source itself (`is_outlier:true`).

---

## Summary

7 meanings / 8 instances of a strength-lexeme keyword group that the source itself does not unify: it fuses **God-grounded strength/valour** (5 instances), the **collapse/absence of strength** (2), and the **wicked's steadfast clinging to evil** (1) — near-antonymic movements sharing only a lexeme. Structurally thin: seats never named (D104="none" ×8, heart uncaptured despite the text), no D109/D110/D111/D113, source in 2/8, manner in 1/8; the only real axis is locus (2 external:god / 6 internal:ib-state). The network is sparse and points wholly outside the file (2/8 nodes, zero intra-family edges). Two D112/D116 swaps (270102, 269954) and one cross-cluster outlier (269954, M47) noted.
