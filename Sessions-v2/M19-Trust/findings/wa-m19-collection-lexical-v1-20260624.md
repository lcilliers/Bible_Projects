# M19 (Trust) — COLLECTION-LEXICAL (01b Part C, the collection layer) · v1 · 2026-06-24

- **Cluster:** M19 (Trust) · status `Not started` · **AFFECT/VOLITION** cluster (the act/disposition of trusting; pole vs M20 Doubt).
- **Spec:** `Workflow/Instructions/01b-VE-field-reliability-and-rules.md` **Part C** (C.2 object_type incl A1 bearer-class / A2 intrinsic-faculty / asah-override / membership_scope · C.3 type-conditioned EXPECTED · C.4 collection items · C.5 R1–R6) + `outputs/markdown/validation/wa-lexical-extension-model-v2-with-additions-20260624.md` (A1–A5). model_version = **01b-v3 / extension-v2**.
- **Corpus:** `Sessions-v2/M19-Trust/Data/wa-ve-lexical-extract-M19-20260624.json` — 304 verses, **31 owned terms, 329 focus occ**.
- **Method:** REGROUPED by SEMANTIC SENSE (registry = provenance noise). Every value FLOWS FROM per-verse-VARYING evidence (sense/object/object_type/experiencer/valence/how + co-seating), cited to the measure; lemma-constants (type/faculty/lemma_meaning) QUARANTINED. derivation tagged `mechanical | read | researcher` + source-scope.

> **Headline finding.** M19 is **not one kind**. The core is a clean **bivalent disposition** (trust), whose valence is decided **by the OBJECT trusted-in** (God → righteous/commanded; wealth/self/military strength/man → sinful/forbidden) — the textbook *object-discriminated bivalence* of C.2 (the **object aimed-at IS the discriminator**). Around it sit a **state/condition** family (security), a **refuge-object** family (qualifier/quality), a **confidence** family, and **two intruder families** (self-control, zeal) that are alien to Trust and belong elsewhere.

---

## 1. Sense-grouping — the 31 terms into preliminary UNITS (registry collapsed)

The shipped extract groups by owning-registry ("hope"/"trust"/"strength"/"envy"/"zeal"/…). That is provenance, not meaning. Regrouped by semantic sense:

| Unit | Strong's (occ) | core senses | grammatical type | belongs in Trust? |
|---|---|---|---|---|
| **U1 TRUST (act/disposition)** | ba.tach H0982 (117) · sha.an H8172 (12, *lean*) · na.sa H5375O (8, *lift up [the soul]*) · a.man H0540 (3, Aram *trust*) · re.chats H7365 (1, Aram *trust*) · bit.chah H0985 (1) | trust · trusts · rely · lean · lift-up-soul | action (status for the 2 nominal) | **YES — the head** |
| **U2 REFUGE-SEEK (act)** | cha.sah H2620 (36) | take refuge · seek shelter | action | **YES — directional sub-act** |
| **U3 SECURITY (state/condition)** | be.tach H0983 (34, *securely/safety*) · bit.ta.chon H0986 (3) · bat.tu.chot H0987 (1) · miv.tach H4009 (15, *confidence/trust*) | securely · safety · secure · confidence | status | **YES — the resultant state** |
| **U4 REFUGE/SUPPORT (object/thing)** | ma.oz H4581 (20, *stronghold*) · mach.s.seh H4268 (17, *refuge*) · cha.sut H2622 (1) · kis.lah H3690 (2, *confidence/folly*) · mish.an H4937A (2) · mish.en H4937B (2, *support*) | stronghold · refuge · shelter · support | status (noun) | **YES — the object relied-on** |
| **U5 CONFIDENCE / FIRMNESS** | pepoithēsis G4006 (6) · bebaios G0949 (7, *firm/steadfast*) · stereōma G4733 (1, *firmness*) · pistoō G4104 (1, *be convinced*) | confidence · firm · reliable · believed | status/quality | **YES (NT) — the inner-state cognate** |
| **U6 SELF-CONTROL** | enkrateia G1466 (3) · enkrateuomai G1467 (2) · enkratēs G1468 (1) · sōfronismos G4995 (1) · sōfrōn G4998 (4) · nēfaleos G3524 (3, *sober*) | self-control · sober-minded · disciplined | status/quality/action | **NO — intruder → M-self-mastery (route out)** |
| **U7 ZEAL / EAGERNESS** | spoudazō G4704 (11, *be eager*) · zēloō G2206 (11, *be eager/jealous/envy*) · zeō G2204 (2, *fervent*) · frontizō G5431 (1, *be careful*) | do-your-best · eager · diligent · fervent · jealous | action | **NO — intruder → M34 (Diligence) / M28 (Desire-jealousy)** |

The provenance scatter (`envy`/`zeal`/`strength`/`hope`/`trust` registries) confirms why registry grouping is noise: ba.tach lives under "hope", be.tach under "trust", ma.oz under "strength" — yet U1/U3/U4 are one trust complex.

---

## 2. LRT per unit — is the lexical fully revealing? (run before conclusions)

LRT (`scripts/_lexical_revelation_test_20260624.py`) over the regrouped units. `<-- EXPECTED` = field the unit's nature demands; coverage & distinctness below.

| Unit | n | sense | object/obj_type | experiencer | valence (varies?) | how | LRT verdict |
|---|---|---|---|---|---|---|---|
| **U1 TRUST** | 142 | 100% | 77% (obj_type 5d) | 68% (3d) | 94% — **VARIES 5d** | **1%** | object/experiencer well-revealed; **how legitimately near-empty** (a disposition has no manner — not a gap, see §6); faculty constant→A2 |
| **U2 REFUGE-SEEK** | 36 | 100% | 58% (obj_type 2d) | 58% | 97% — varies 3d but **33/36 righteous** | 0% | mono-directional (refuge sought *in God*); near-univalent → role differs from U1 |
| **U3 SECURITY** | 53 | 100% | 25% (obj_type 5d) | 60% | 89% — VARIES 3d | **89%** | a STATE: object mostly NONE (expected — a state is not directed); `how` = *dwell securely* (the co-expressed posture) |
| **U4 REFUGE-OBJECT** | 44 | 100% | low (obj_type 6d) | self-leaning | varies 3d | 52% | object is itself a thing relied-on; mostly modifies a host (qualifier/quality) |
| **U5 CONFIDENCE** | 15 | 100% | low | 60% | righteous/neutral | 40% | inner-state; thin NT sample |
| **U6 SELF-CONTROL** | 14 | 100% | NONE | — | commanded/righteous only | 7% | **odd-one-out** — no object_type, univalent virtue; not a trust kind |
| **U7 ZEAL** | 25 | 100% | mixed | addressed | commanded/sinful/righteous | 0% | **odd-one-out** — eagerness/jealousy; not a trust kind |

**LRT red flags resolved, not papered over:**
- U1 `how` 1/142 — **NOT a gap**: trust is intransitive disposition; its content is *toward-what* (object), which IS revealed (77%). The "act with a manner" expectation (act-nature) does not apply once object_type=**characteristic/disposition** (C.3: intransitive dispositions legitimately have how/object-manner = NONE).
- U1 faculty 8/142 — lemma-constant gap → resolved by **A2 intrinsic-faculty escape** (declare affect+volition once at collection scope; do NOT seat per verse).
- U3 object 25% — **NOT a gap**: a STATE is not directed at an object (C.3 expects bearer/mutability/realm, not object). `how`=*dwell* (89%) is the state's posture, correctly populated.

---

## 3. object_type per unit (C.2 rules, A1 bearer-class)

| Unit | **object_type** | bearer-class (A1) | rule fired | derivation |
|---|---|---|---|---|
| **U1 TRUST** | **bivalent-faculty → characteristic** (the disposition of trusting) | human-faculty | `type=action` + **valence flips good/evil by the OBJECT aimed-at** (C.2 bivalent-faculty: object IS the discriminator) | read (cross-verse) |
| **U2 REFUGE-SEEK** | **characteristic** (a directed sub-act of trust) | human-faculty | `how`-predicate of a person acting from the trust-faculty; near-univalent (refuge→God) | read (cross-verse) |
| **U3 SECURITY** | **state/condition** | human-faculty (the secure person) | `type=status` + valence varies + object NONE + posture (*dwell securely*) | mechanical (type) + read (valence-varies) |
| **U4 REFUGE-OBJECT** | **qualifier** (mostly modifies a host: "the LORD is my *refuge/stronghold*") with a **quality** reading when bearer=divine/thing (A1) | divine / object-way → quality; the relied-on noun | always modifies a host → qualifier; bearer-split → quality | read (cross-verse) |
| **U5 CONFIDENCE** | **state/condition** (inner confidence) | human-faculty | `type=status`; an inner register, object mostly NONE | mechanical (type) + read |
| **U6 SELF-CONTROL** | **characteristic** (a virtue, but **NOT of Trust**) | human-faculty | univalent disposition; alien field | read → **route out** |
| **U7 ZEAL** | **characteristic / bivalent-faculty** (eagerness; jealousy flips) **NOT of Trust** | human-faculty | bivalent (zeal good / jealousy sinful) but alien field | read → **route out** |

**Per-unit object_type CALLS (return summary):** U1 = **bivalent-faculty→characteristic** · U2 = **characteristic** · U3 = **state/condition** · U4 = **qualifier (quality by bearer)** · U5 = **state/condition** · U6 = **characteristic [intruder]** · U7 = **bivalent-faculty [intruder]**.

---

## 4. Collection-lexical records (C.3 EXPECTED filled across verses + C.4 items)

Each value: `value` · `derivation`{mechanical|read|researcher} · `source-scope` (verse cited; adjacency noted). Silent→NONE; expected-but-undetermined→UNRESOLVED.

### U1 — TRUST (ba.tach + sha.an + na.sa + a.man/re.chats) — **bivalent-faculty → characteristic**

| C.3 EXPECTED (characteristic) | value | derivation | source-scope |
|---|---|---|---|
| **faculty** (REQUIRED; A2) | **affect+volition** (the volitional act of resting one's confidence; intrinsic) — declared at collection scope, NOT per-verse seat | researcher (A2 intrinsic) | collection; per-verse faculty silent (8/142) so escape is required |
| **how-it-operates** | resting/leaning the self on an object for security; *na.sa* = "lift the soul to"; *sha.an* = "lean on" | read | sense+lemma across U1; Psa 25:1 (lift soul), Isa 36:6 (lean on staff) |
| **directed-at-what** (transitivity) | **TRANSITIVE** [prov-confirm] — trust takes an object 77% (obj 110/142); object_type {God 44 · thing 24 · person 17 · abstract 17 · situation 8} | mechanical (object morph) | per-verse object field |
| **whose** (experiencer) | self / other / other-addressed (3d, 68%) — exhortation "trust in the LORD" addresses *other* | mechanical | experiencer field |
| **intensity** | NONE (no intensifier governs trust mechanically) | mechanical | silent across U1 |
| **valence (the discriminator)** | **VARIES 5d** by object: God→righteous(20)/commanded(9)/forbidden(2, "do not let him make you trust", Isa 36:15) · wealth/self-mind/strength→sinful(40) · man/prince→forbidden | mechanical (object→valence cross-tab) | cross-tab below |

**Bivalence proof (ba.tach H0982 object_type × valence):** God×righteous 20 · God×commanded 9 · **thing×sinful 13** (Psa 49:6 "trust in wealth") · **abstract×sinful 9** (Pro 28:26 "trusts his own mind is a fool") · **person×sinful/forbidden 6** (Psa 78:22; Psa 146:3) · situation×sinful 3 (Isa 32:9 complacency). → *the object devised/aimed-at IS the discriminator* (C.2). [derivation: mechanical, per-verse object×valence]

| C.4 item | value | derivation | source-scope |
|---|---|---|---|
| **transitivity** [prov] | transitive (object 77%) | mechanical | per-verse object |
| **membership_scope** [prov] | **per-occurrence** — ba.tach/sha.an belong to Trust only at their righteous/commanded valence; the sinful "trust in X" occurrences are the cluster *boundary* (mis-placed confidence) — retained as cited pole, not positive members | read | the valence flip IS the boundary (C.2) |
| **pole-relation** | **inverse axis = M20 Doubt** (da.ag *be anxious* · merimnaō *worry* · dipsuchos *double-minded* · ya.ash *despair* · ekkakeō *lose heart*): trust = the settled confidence, doubt/anxiety = its collapse. **Failure-outcome pole = M07 Shame/bosh** (the wrongly-trusting are "put to shame" — co-seated 9×). **Co-axis = M01 Fear/ya.re** (trust vs fear; ya.re co-seat 11×). NT cognate-overlap = **M31 Faith/pisteuō** (trust-in ≈ believe-in). | read + cross-ownership | co-seat measure: bosh(M07)×9, ya.re(M01)×11; M20 owned-term inspection |
| **realm** | **inner/moral** (the disposition) with a **social/communal** sub-register where the object is a nation/alliance ("trust in Egypt", Isa 36:6) and **forensic/covenantal** where it is trust-in-the-LORD's-covenant-deliverance (Psa 22:4) | read (per-verse object) | per-verse object_type=situation/God |
| **binding** (A5 per-verse role) | partner: che.sed (M05 *steadfast-love*, ×16 — trust rests on God's *chesed*); object-of: ya.re (M01); pole-opposite: bosh (M07). LIVE field still flat — recorded as roles for the build. | read | co-seat measure |
| **classifier** [prov] | n/a (not an identity unit) — NONE | mechanical | — |

### U2 — REFUGE-SEEK (cha.sah H2620) — **characteristic** (directed sub-act)

| C.3 EXPECTED | value | derivation | source-scope |
|---|---|---|---|
| faculty (A2) | affect+volition (intrinsic); per-verse faculty=perception is a **lemma-constant → quarantined** | researcher (A2) | collection |
| directed-at-what | **God 17 · person 4** (obj 21/36); the destination is overwhelmingly God ("in You I take refuge") | mechanical | object field |
| valence | **near-univalent righteous (33/36)** — refuge-seeking is intrinsically the good move; the 1 sinful = false refuge | mechanical | valence field |
| **transitivity** [prov] | transitive-directional (always *takes refuge IN*) | mechanical | object/preposition |
| membership_scope [prov] | **lemma** member (univalent — belongs as a whole, unlike bivalent ba.tach) | read | valence 33/36 righteous |
| pole-relation | refuge ↔ exposure/no-shelter; same M20/M07 axis as U1 | read | shared axis |
| realm | forensic/covenantal + inner/moral (shelter under God's wings, Psa 91) | read | per-verse |

### U3 — SECURITY (be.tach H0983 + bit.ta.chon + miv.tach) — **state/condition**

| C.3 EXPECTED (state) | value | derivation | source-scope |
|---|---|---|---|
| of-what (bearer) | the person/people who dwell (experiencer 60%, *other* dominant — "they dwell securely") | mechanical | experiencer |
| who-set-it | the LORD (where stated) / the object trusted (where false security) | read | adjacency (e.g. Lev 25:18-19 obedience→security) |
| **mutability** | **CHANGEABLE** — security is given and revoked across verses (Deu 28 blessing↔curse; "you felt secure"→judgment) | read | cross-verse contrast |
| **transition-trigger** (+.manner) | trigger = obedience/trust (→security) vs apostasy (→loss); **.manner = inner** (trust/obedience) / **juridical-covenantal** (covenant blessing-curse) | read | Lev 25; Deu 28 |
| valence-register | VARIES 3d: neutral 26 (mere "dwelling safely") · righteous 15 (secure-in-God) · **sinful 6** (false complacent security, Isa 32:9-11; Jdg 18:7) | mechanical | valence field |
| **realm** | mostly **social/communal · bodily** ("dwell securely" = peaceable settled life); flips **inner/moral** when grounded in God | read (per-verse `how`=*dwell* H3427/H7931) | how field |
| pole-opposite | dread/insecurity (M01 Fear); complacency = the sinful failure-mode | read | shared axis |

### U4 — REFUGE/SUPPORT-OBJECT (ma.oz + mach.s.seh + mish.an) — **qualifier (quality by bearer, A1)**

| C.3 EXPECTED (qualifier) | value | derivation | source-scope |
|---|---|---|---|
| what-it-modifies (host) | a predicate "the LORD is my **stronghold/refuge/support**" — modifies the relationship to God | read | per-verse object NONE (it IS the relied-on thing) |
| of-what-property [prov] | reliability/protection — the property of being a secure place | read | sense (*stronghold/shelter*) |
| **bearer-class (A1)** | **divine** ("the LORD is my refuge") → **QUALITY** predicated of God; **object/thing** (a literal fortress, Pharaoh's "strength" Isa 30:2-3) → quality of a thing, often **sinful** (false refuge) | read (per-verse bearer) | ma.oz Isa 30: Egypt as refuge=sinful; Psa 27:1 LORD=refuge=righteous |
| valence | varies: neutral/righteous when God; sinful(7) when a false refuge | mechanical | valence field |
| role-in-cluster [prov] | **qualifier-import** — these nouns name the *object* of trust; analysed as the relied-on quality, not as a faculty | read | grammatical noun, modifies host |

### U5 — CONFIDENCE/FIRMNESS (pepoithēsis + bebaios + stereōma + pistoō) — **state/condition** (NT inner-state)

| C.3 EXPECTED (state) | value | derivation | source |
|---|---|---|---|
| of-what (bearer) | the believer's inner confidence; bebaios also a **quality** of a thing ("firm hope/anchor", Heb 6:19) → A1 quality-by-bearer | read | bearer per verse |
| valence | righteous 7 / neutral 6 (no sinful — NT confidence is in God/the gospel) | mechanical | valence |
| mutability | changeable ("hold firm to the end", Heb 3:14 — confidence can be lost) | read | Heb 3:6,14 |
| realm | inner/moral + eschatological (firmness "to the end") | read | per-verse |
| pole-opposite | wavering/double-mindedness (M20 dipsuchos) | read | cross-ownership |

### U6 — SELF-CONTROL [INTRUDER] & U7 — ZEAL [INTRUDER]

- **U6 (enkrateia/sōfrōn/nēfaleos)** = **characteristic**, faculty=cognition/volition, **univalent righteous/commanded** (a virtue), object_type NONE — but the *domain is self-mastery over appetite*, NOT trust/confidence. **role-in-cluster = NONE (alien)**. → **route to a self-mastery cluster** (no M-code for temperance located; researcher to assign).
- **U7 (spoudazō/zēloō/zeō/frontizō)** = eagerness/diligence (commanded 15) flipping to jealousy/envy (sinful 5) — **bivalent**, but the axis is *zeal vs envy*, NOT trust. → **route: spoudazō/frontizō → M34 (Diligence); zēloō/zeō → M28 (Desire) / jealousy**.
- These two families (49 occ, ~15% of the cluster) are **provenance artefacts** of the "envy"/"zeal"/"being" registries pulled in. **Recommend removal from M19** at term-curation.

---

## 5. Mechanical-vs-captured split (R1 / R5 tagging)

Per-verse VE values feeding the collection (n=329 focus occ), share that is mechanically re-derivable vs read/researcher-captured:

| layer | mechanical | read | researcher | note |
|---|---|---|---|---|
| sense | 329/329 (100%) | — | — | per-occurrence subgloss |
| type (POS) | 329/329 | — | — | lemma-constant |
| object / object_type | ~250/329 (76%) | — | — | morph object |
| experiencer | ~210/329 (64%) | — | — | possessor/subject |
| valence | ~300/329 (91%) | — | — | term-inherent + object cross-tab |
| object_type **call** (C.2) | — | 7 units (read) | A2 faculty (researcher) | the kind is read across verses |
| C.4 items (mutability/trigger/realm/pole/binding/membership) | — | read | — | cross-verse, cited |

**Collection-record mechanical share ≈ 78%** (per-verse fields regenerate; the 7 object_type calls + C.4 cross-verse items + the A2 intrinsic-faculty declaration are read/researcher and **preserved** under R1). In line with the 79–81% Part C benchmark.

---

## 6. Q&A — Round 2 (the [prov] Part-C items: confirmed or not by M19?)

**Q1 — `classifier` [prov] (who gives the verdict, for IDENTITY).** **NOT EXERCISED.** M19 has no IDENTITY unit (no person-verdict). classifier = NONE throughout. → neither confirmed nor refuted by M19; remains grounded on prior clusters only.

**Q2 — `transitivity` [prov].** **CONFIRMED, and load-bearing.** Trust (U1) is **transitive** (object 77%, governs *in/on X*) and the transitivity is what *enables* the bivalence — because trust takes an object, the **object's class sets the valence**. By contrast self-control (U6) is **intransitive** (object_type NONE) and stays univalent. So transitivity is not just a populated field; it **predicts** whether a faculty can be bivalent. **Strengthens the [prov] item → recommend firming.**

**Q3 — `role-in-cluster` [prov] {member · pole-anchor · qualifier-import}.** **CONFIRMED + extended.** Used three ways in M19: (a) **qualifier-import** for U4 refuge-OBJECT nouns (named as the relied-on quality, not analysed as faculties); (b) the **sinful "trust in wealth/self"** occurrences retained as **cited boundary/pole** rather than positive members; (c) a NEW use — **alien-import** for U6/U7 (terms whose *domain* is outside the cluster, not merely the wrong pole). The existing 3 values don't cleanly cover (c): a *self-control* term is not a pole-anchor of trust, it is simply mis-clustered. → **candidate 4th value `role-in-cluster = alien` (route-out marker)**, distinct from pole-anchor.

**Q4 — `membership_scope` [prov] {lemma · per-occurrence}.** **CONFIRMED — clean replay.** ba.tach/sha.an are **per-occurrence** members (Trust only at the righteous/commanded valence; the flip to "trust in X" IS the cluster boundary) — exactly the bivalent-term pattern. cha.sah (U2) is by contrast a **lemma** member (univalent, 33/36 righteous). M19 reproduces both states; the bivalent/univalent split maps directly onto per-occurrence/lemma. **Firm.**

**Q5 — `asah`-deed override [prov].** **NOT TRIGGERED.** No status-POS noun in M19 is governed by a do/commit verb (trust nouns combine with *dwell/lean/seek*, not *asah/do*). The security state's `how`=*dwell* is a posture, not a deed-override. → not exercised by M19; remains grounded on the deed-clusters (M10/M13).

**Q6 — person↔condition link [prov].** **WEAK PARTIAL.** No tight cognate identity↔state pair like "the fool is his folly". The nearest is the U1↔U3 morphological cognate (**ba.tach** *to trust* [act] ↔ **be.tach/bit.ta.chon** *security* [state], same b-t-ch root) — i.e. the **act produces the state** of the same root. That is a real act→state cognate link but not the *person↔condition* (identity↔state) shape the [prov] item describes. → suggests a **sibling item: `act↔state cognate link`** (root-shared act and its resultant state), distinct from person↔condition.

**Q7 — Is trust characteristic / state / expression? (the cluster's own question).** **EVIDENCE-DECIDED: BOTH characteristic AND state, as two cognate units, not one.** The *act/disposition* (ba.tach, cha.sah) is a **bivalent-faculty characteristic**; its *result* (be.tach security) is a **state/condition**; the *object* (ma.oz refuge) is a **qualifier/quality**. "The act of trusting" is captured as the characteristic (transitive, object-discriminated), not as a separate "expression" type — there is no manner-bound deed (`how`=NONE legitimately), so **expression does not apply**. Trust is a **disposition that produces a state**, the U1→U3 root-cognate being the lexical proof.

**Q8 — New gap / candidate 7th object_type?** **NO 7th type needed.** All M19 units fit the six (characteristic / state / qualifier / bivalent-faculty / quality-by-bearer; identity unused). The six remain **stable**. Two model nudges surfaced instead: (i) a **`role-in-cluster=alien`** value (Q3) and (ii) an **`act↔state cognate link`** sibling to person↔condition (Q6). Both are item-level refinements, not a new kind.

**Q9 — pole-relation vs M20 Doubt (the cluster's mandated test).** **CONFIRMED as a true inverse axis.** M20 (anxiety/worry/double-mindedness/despair/lose-heart) is the affect-collapse of trust; co-seating evidence puts **M01 Fear/ya.re** as the co-axis (trust vs fear, ×11) and **M07 Shame/bosh** as the failure-OUTCOME pole (the wrongly-trusting are put to shame, ×9). **M31 Faith/pisteuō** is the NT cognate-overlap. Recommend **M19 ↔ M20 assembled together** (pole-paired-clusters rule, C.4).

---

## 7. Researcher decisions requested

1. **Curation:** remove **U6 self-control** (6 terms) and **U7 zeal/eagerness** (4 terms) from M19 — alien domains (self-mastery; diligence/jealousy). 10 of 31 terms, 49 of 329 occ. Confirm route-out targets (self-mastery cluster TBD; spoudazō→M34; zēloō→M28).
2. **Firm the [prov] items** transitivity (Q2) and membership_scope (Q4) — clean replays here.
3. **Adopt** candidate `role-in-cluster=alien` (Q3) and `act↔state cognate link` (Q6) for the model.
4. **Pole-pair** M19 with M20 (Doubt) for joint assembly.

---

*v1 · 2026-06-24 · Claude Code · model_version 01b-v3 / extension-v2. All per-verse values mechanical (regenerate); object_type calls + C.4 cross-verse items + A2 faculty are read/researcher (preserved, R1). Evidence: corpus 329 occ; ba.tach object×valence cross-tab; co-seat measure; M20/M31 owned-term inspection.*
