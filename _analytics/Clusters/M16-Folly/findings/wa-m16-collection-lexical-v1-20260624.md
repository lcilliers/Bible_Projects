# M16 (Folly) — COLLECTION-LEXICAL (Extended Lexical Model v2)

- **File:** wa-m16-collection-lexical-v1-20260624.md · **v1 · 2026-06-24 · Author:** Claude Code.
- **Cluster:** M16 "Folly, Madness and Foolishness" — 30 owned terms · 165 focus-occurrences · 156 verses (OT 119 / NT 46 by occ approx).
- **Corpus:** `Sessions-v2/M16-Folly/Data/wa-ve-lexical-extract-M16-20260624.json` (01b v2 mechanical + verse-read API resolution + measure layer 3.34.0).
- **Model:** Extended Lexical Model **v2** (A1 bearer-class · A2 intrinsic-faculty escape · A3 transition-trigger.manner · A4 realm sub-register · A5 enriched binding) over design v1 (two scopes, type-conditioned EXPECTED answers §4, R1 mechanical/captured tagging).
- **Status of run:** FRESH cluster (no prior M16 reads), new-type stress test — the **pole-pair of M15 (Wisdom)**, which is `Analysis Completed`. This is the deliberate antithesis-stress: does the model handle a cluster that spans CHARACTERISTIC / STATE / IDENTITY / EXPRESSION / BIVALENT-QUALITY all at once.
- **Grounding discipline:** every value FLOWS FROM per-verse-varying evidence, never a lemma-constant. Each derivation is tagged `mechanical | read | researcher` (R1) with source-scope (head-verse | adjacent | collection). The cite is the named measure (morph / sense / co-seat / divine lemma / asah-predicate / pole co-occurrence).

---

## 0. Method and the regrouping (registry → semantic sense)

The provided reader (`_read_full_lexical_composition`) groups by **owning-registry**, which for M16 is provenance noise — it produced labels like "[contempt]", "[will]", "[hope]", "[sloth]" that are registry homes, not folly's semantic structure. **Regrouped by semantic sense** (the instruction), the 30 terms fall into **six preliminary units**, and the discriminator is largely **mechanical: the morphological `type` (POS) plus the per-verse sense**:

| Unit | Sense core | Terms (Strong's) | occ | dominant `type` (POS) |
|---|---|---|---|---|
| **U1 — the FOOL (person-type)** | "a fool / foolish (one)" — a person classed | e.vil H0191 (26) · sa.khal H5530 (6) · mōros G3474 (12) · afrōn G0878 (10) · ba.ar H1198 (5, "brutish/stupid person") · e.vi.li H0196 (1) · ka.sal H3688 (1) | 61 | **quality** (adjective) + a few action |
| **U2 — FOLLY (the abstract condition)** | "folly / foolishness" as a thing one has / is in | iv.ve.let H0200 (24) · sikh.lut H5531B (6)+H5531A (1) · se.khel H5529 (1) · mōria G3472 (5) · afrosunē G0877 (4) | 41 | **status** (noun) |
| **U3 — MADNESS (the disordered mind)** | "madness / out-of-mind / insanity / rave" | ha.lal H1984I "rave" (5) · ho.le.lah H1947 (4) · ho.le.lut H1948 (1) · shig.ga.on H7697 (3) · sha.ga H7696 (6) · mainomai G3105 (5) · mania G3130 (1) · parafroneō G3912 (1) · parafronia G3913 (1) | 27 | **action + status** mixed |
| **U4 — to ACT/BECOME a fool (folly enacted)** | "act foolishly / become a fool / make foolish" | ha.lal H1984C "be foolish" (9) · ya.al H2973 (4) · mōrainō G3471 (4) | 17 | **action** (verb) |
| **U5 — DISGRACE / OUTRAGE (the senseless deed)** | "outrageous thing / outrage / vile thing done in Israel" | ne.va.lah H5039 (13) | 13 | **status** (noun-of-deed) |
| **U6 — singleton fringe (recklessness/sloth/fantasy)** | recklessness · sloth · mental-fancy · transgression | pa.chaz H6349 (1) · oknēros G3636 (3) · har.hor H2031 (1, Aramaic) · pash H6580 (1) | 6 | mixed |

> **Why these units (mechanical):** `type` is POS-only (01b C-1) and it cleaves the corpus almost perfectly — adjectives (the fool **is** foolish, attributive) → U1; deed-nouns (folly **as a thing**) → U2/U5; verbs (folly **enacted**) → U3-action/U4; status-nouns of the disordered mind → U3-status. Sense then separates U2 (resident condition) from U5 (the outrageous *deed*, sense always "outrage/outrageous thing", `how`=*asah* "to do/commit" 11/13) and U3 (mind-disorder) from U2 (general folly). All splits cite per-verse `type`+`sense`, not the lemma label.

**Mechanical-vs-captured at field-value level (focus occ):** 1,230 non-null field-values — **996 mechanical (81%)** vs **234 read-resolved (19%)**. The read fields are exactly the five the corpus marks read (`cause · location · divine_involvement · object_type · valence`); everything structural (sense · type · mode · faculty · origin · how · object · experiencer · intensity · compound) is mechanical. The collection-level object_type/binding/pole/mutability calls below are then **re-derived mechanically from those per-verse rows** (R1) wherever a rule decides them; the residue is captured `read`.

---

## 1. LRT per unit (type-conditioned expected-answer coverage)

LRT run per representative term (`_lexical_revelation_test_20260624.py`). Expected-answer coverage (✓ filled / red-flag where expected-but-sparse), with the recovery verdict.

| Unit (term) | nature run | sense | object | experiencer | valence | how | LRT verdict |
|---|---|---|---|---|---|---|---|
| U1 e.vil H0191 | characteristic | 100% | **0%** (RED) | **4%** (RED) | 96% | 77% | object/experiencer sparse → **legitimately NONE** (see §3-A2): the fool-as-person has no governed object; the *person* IS the experiencer. faculty=cognition 26/26 (constant, intrinsic). |
| U1 mōros G3474 | characteristic | 100% | 25% | 50% | 83% | 50% | object present where the fool acts (builds house, takes lamps); faculty=moral_evaluation 12/12 intrinsic. Healthy. |
| U2 iv.ve.let H0200 | state | 100% | 25% | 75% | 100% | 62% | STATE expected-set well covered: valence 100%, experiencer 75% (who bears it), how varies 15 distinct verbs. object NONE is correct (a condition has no target). |
| U2 mōria G3472 | state | — | low | 80% | partial | — | small; valence sparse because of "foolishness OF God" (1Cor) = read-neutral/None (the A1 flip). |
| U3 sha.ga H7696 | act | 100% | 33% (RED) | **0%** (RED) | 67% | 17% (RED) | madness-as-behaviour: experiencer 0% = **mechanical gap** (subject is a 3rd-person verb without possessive suffix — recoverable from the clause subject, R6). how sparse: the verb IS the madness (no manner). |
| U3 ho.le.lah H1947 | state | 100% | 0% | 0% | 100% | 50% | the *condition* of madness; valence 100% (sinful 3/neutral 1). object NONE correct. |
| U4 ha.lal H1984C | act | 100% | 56% | 67% | 100% | **0%** (RED) | EXPRESSION: how 0% is the act-lemma how-gap → **A3 manner = NONE/intrinsic** (the verb is the foolish act; manner lives in the bound co-term, see binding). 4/9 have neither object nor how = bare "act foolishly". |
| U5 ne.va.lah H5039 | state | 100% | 38% | 54% | 100% (sinful 13/13) | 92% | the disgraceful DEED: how 92% = *asah* "do/commit" (the deed is *done*); object=Israel (the community wronged). Best-covered unit. |

**LRT summary:** the red flags are **all legitimately explained by object-type** (A2 intrinsic-faculty escape and the expected-set per type), not data gaps — **except** U3 `sha.ga` experiencer (a genuine mechanical recovery target: read the clause subject, R6) and the act-units' `how` (resolved by A3 = manner is intrinsic/bound, not a gap).

---

## 2. Object-type call per unit (model-v2 A1/A2 rules)

Each call FLOWS FROM per-verse-varying evidence (type-variation, valence-variation, faculty presence, bearer-class), never the lemma.

### U1 — the FOOL → **IDENTITY** (person-classification), with a CHARACTERISTIC reading on the faculty terms
- **Call: IDENTITY.** `derivation=mechanical` (rule §3 design: object_type=person + a verdict/label → identity). Evidence per verse: the term is an **attributive adjective/substantive predicated of a person** ("a foolish man", "you fools", "five were foolish") — type=quality 55/61, object NONE 0% (a person-class has no governed object), experiencer = the person themselves. The classification varies by **who** is classed and **who classifies** (man / brother / virgins / the wise-claiming).
- **Bearer-class (A1):** `human` for almost all (the fool is a person) → IDENTITY. **One bearer-flip:** mōros in **1Cor 1:25, 1:27** — "the **foolishness of God**", "God chose what is **foolish**" — bearer = **divine/God's-strategy** → here folly is a **QUALITY predicated of God's wisdom-by-paradox**, valence read NOT sinful (None), divine_involvement=object. `derivation=read` (the A1 split needed the bearer read). This is the exact tamim-pattern the model predicted — **same lemma, split by bearer**.
- **CHARACTERISTIC sub-reading (A2 intrinsic-faculty escape):** e.vil carries **faculty=cognition 26/26**; mōros/afrosunē carry **faculty=moral_evaluation**. By A2 these are **collection-level intrinsic-faculty properties of the IDENTITY** ("the fool is cognition-/judgement-defective"), declared once `derivation=intrinsic`, NOT a per-verse seat-claim. So U1 is an **IDENTITY whose defining defect is an intrinsic faculty** — identity and characteristic are not rivals here; A2 lets both hold.

### U2 — FOLLY (the condition) → **STATE/condition**
- **Call: STATE.** `derivation=mechanical` (type=status 41/41 + valence varies sinful/neutral + bearer is a person who *has* it). Evidence: "folly is bound up in the heart" (Pro 22:15), "folly **inherit**" (Pro 14:18), folly that "**festers**" (Psa 38:5) — a condition one is in, seated (heart 7×). object mostly NONE (a condition has no target) — correct for STATE.
- **realm (A4):** `inner/moral` — folly is seated in the **heart** (location=heart 7× across U2) and is morally weighted (valence sinful 30+). Not ritual/forensic.

### U3 — MADNESS → **STATE/condition** (status terms) + **EXPRESSION** (the verbs), a split-by-type unit
- **Call: STATE for the status terms** (ho.le.lah, shig.ga.on, mania, parafronia: type=status) — the disordered *condition* of mind; **EXPRESSION for the verbs** (sha.ga, mainomai, parafroneō, ha.lal-rave: type=action) — madness *behaved*. `derivation=mechanical` (the POS split is the rule).
- **BIVALENT by bearer + valence (A1):** madness is **neutral** when it is **clinical/behavioural** (David feigns madness 1Sa 21:14-15; "is he mad?" 2Ki 9:11; Paul "talking like a madman" 2Cor 11:23 = rhetorical) and **sinful** when **moral** (Ecc "evil madness", Hos 9:7 "the prophet is mad"). The same family flips good/neutral↔evil **by verse** → genuine bivalence, read per occurrence.
- **DIVINE-AGENT sub-reading:** shig.ga.on in **Deu 28:28, Zec 12:4** — "the LORD will **strike** you with madness", divine_involvement=**agent**, valence neutral. Madness as **inflicted judgment** — a STATE whose **transition-trigger is divine affliction** (A3 manner = `divine-affliction`, not inner). `derivation=read` (divine agent role).

### U4 — to ACT/BECOME a fool → **EXPRESSION**
- **Call: EXPRESSION.** `derivation=mechanical` (type=action + a binding co-term / manner). Evidence: "act foolishly", "**became** fools" (Rom 1:22 — a transition verb), "God **made foolish** the wisdom of the world" (1Cor 1:20, divine=agent). The act expresses an inner folly; faculty=moral_evaluation intrinsic (ya.al, mōrainō).
- **A3 manner:** `NONE/intrinsic` — the how-field is 0% because the **verb itself IS the foolish act**; manner, where present, lives in the **bound co-term** (binding, §4).

### U5 — DISGRACE / OUTRAGE (ne.va.lah) → **EXPRESSION** (a senseless DEED), NOT the same kind as U2
- **Call: EXPRESSION (deed of disgrace).** `derivation=mechanical`. Though POS=status (a noun), the **sense is invariantly "outrageous thing / outrage"** and the **how is invariantly *asah* "to do/commit" (12/13)** with **object=Israel (the community)** — i.e. this noun names a **deed done to/in the community**, not a resident condition. This is the strongest **stress-finding**: a status-POS term that is lexically an EXPRESSION. The rule that catches it: *status-POS + invariant deed-sense + an *asah*-binding + a community object → EXPRESSION* (`derivation=read` on the EXPRESSION override of the POS default; the underlying facts are mechanical).
- **realm:** `social/communal` (a public outrage in Israel) — a realm value the A4 list (ritual/inner/forensic/eschatological) **does not yet carry** (see Q&A Q2).

### U6 — singletons → mixed, mostly **STATE/QUALIFIER**
- pa.chaz "recklessness/unstable" (Gen 49:4, of Reuben) → **STATE/QUALITY of a person** (unstable as water); oknēros "slothful" (Mat 25:26, Rom 12:11) → **QUALITY/CHARACTERISTIC** (a faculty-of-will defect, valence varies sinful/forbidden/neutral); har.hor "fancies/fantasies of the head" (Dan 4:5, Aramaic) → **EXPRESSION/thought-content** (mental imagery, NOT folly proper — a borderline-membership flag); pash "transgression" (Job 35:15) → mis-homed, reads as M10-sin not folly. `derivation=read` (small N, each is a single verse).

**Object-type roll-up:** M16 is **NOT one kind** — it is, by mechanical evidence:
- **IDENTITY** (U1, the fool-as-person) — the largest unit;
- **STATE/condition** (U2 folly resident · U3-status madness · U6-pa.chaz);
- **EXPRESSION** (U4 acting-foolishly · U5 the outrage-deed · U3-verbs madness behaved);
- **BIVALENT** by bearer/valence (U3 madness; U1 the "foolishness of God" flip);
- **QUALITY** on divine bearer (1Cor) and on the sloth/recklessness fringe.

This is exactly the multi-kind span the prompt anticipated — and the model v2 handles all of it **except** the communal-deed realm (U5) and a possible "the fool IS his folly" identity↔state collapse (see §6/Q&A).

---

## 3. Collection-lexical record (type-conditioned EXPECTED answers, filled across verses)

Per unit: the design §4 expected-answer set for its object_type, filled from the corpus (head-verse | adjacent | collection); silent→NONE; expected-undetermined→UNRESOLVED. Plus A5 binding, pole-relation (esp. vs M15), mutability, realm. Tags: `[M]`=mechanical, `[R]`=read, `[Rs]`=researcher; scope in parens.

### U1 — the FOOL (IDENTITY; intrinsic CHARACTERISTIC)
- **classified as what?** a fool / foolish one (person-class). `[M]`(head) — sense 100%, type=quality.
- **who classifies?** the sage / Christ / the narrator (Pro: the wise observer; Mat 5:22, 23:17, 25:2 Jesus; Rom 1:22 Paul). `[R]`(collection) — verdict-giver read from speaker.
- **on what basis?** moral-cognitive defect: despises wisdom/instruction (Pro 1:7), does not do Christ's words (Mat 7:26), unprepared (Mat 25:2-8), self-wise (Pro 26:5), claims wisdom (Rom 1:22). `[R]`(adjacent) — basis from the surrounding clause.
- **settled or reversible? (mutability)** → **CHANGEABLE-but-resistant.** `[M]`(collection): Pro 22:15 folly bound in the child's heart but **the rod of discipline drives it out** (removable); BUT Pro 27:22 "crush a fool… yet his folly will **not depart**" (resistant); Rom 1:22 "**became** fools" (a transition INTO it). So the identity is acquirable and in-principle reversible by discipline, but characteristically clings. `derivation=mechanical` (transition verbs present across verses).
- **intrinsic faculty (A2):** cognition (e.vil) / moral_evaluation (mōros). `[Rs/intrinsic]`(collection) — declared once, not per-verse seated.
- **location/seat:** **heart** (e.vil heart 2×, ba.ar le.vav 1×). `[R]`(head) — the fool's folly is heart-seated.
- **binding (A5):** **pole-opposite** to the wise — co-occurs with cha.kham 9×, da.at 2×, bin 2×, a.rum 1× (e.vil); mōros co-occurs sofos/fronimos 6×. Role = `pole-opposite` `[M]`(collection).
- **pole-relation:** **M15 (Wisdom) — direct antithesis.** `[M]`: the fool is defined *against* cha.kham "wise"/sofos, da.at "knowledge", bin "understanding". The strongest cross-cluster pairing in the corpus.
- **divine_involvement:** mostly NONE; **object** in 1Cor 1:25/27 (the bearer-flip). `[R]`.
- **realm:** `inner/moral`.

### U2 — FOLLY (STATE/condition)
- **of what / whose?** a person's condition — experiencer "other" 16 / self 2 (iv.ve.let). `[M]`(head).
- **who set it?** within-person mostly (origin not-stated/within); received-from-outside 1× (sikh.lut). `[M]`.
- **can it change? (mutability)** → **CHANGEABLE (by discipline) / else FIXED.** Same Pro 22:15 ↔ 27:22 evidence as U1. `[M]`(collection).
- **what changes it? (transition-trigger + A3 manner)** the **rod of discipline** (Pro 22:15) — manner = `corrective/disciplinary` (NOT inner repentance, NOT ceremonial). `[M]`(adjacent). A genuinely new A3 manner value (see Q&A Q3).
- **valence register:** sinful 30 / neutral 11 — predominantly **sinful**, neutral where folly is *examined* (Ecc "to know madness and folly"). `[M]`(head).
- **pole-opposite:** **M15** — iv.ve.let co-occurs da.at 5×, a.rum 4×, cha.kham 4×, te.vu.nah 2×; the Ecc triad "wisdom and madness and folly" sets them as explicit opposed objects of study. `[M]`(collection).
- **how (operating):** varies 15 distinct verbs — proclaims (Pro 12:23), flaunts (13:16), pours out (15:2), builds-house (14:1). The condition **expresses outward** — folly is loud. `[M]`(head). *(Note: this "how" on a STATE is the condition's characteristic output — borderline EXPRESSION, see §6.)*
- **location:** **heart** 7× — folly seated in the heart. `[R]`.
- **realm:** `inner/moral`.

### U3 — MADNESS (STATE + EXPRESSION; BIVALENT)
- **of what?** the mind / the man (experiencer other 12). `[M]`.
- **who set it?** within-person (clinical/moral) OR **God (judicial)** — Deu 28:28, Zec 12:4 divine=agent. `[R]`(head).
- **can it change?** UNRESOLVED at collection — no verse in M16 shows madness lifted (the model expects a transition for a STATE; none attested here). `[R/UNRESOLVED]`(collection) — honest gap.
- **what changes it (transition-trigger + A3 manner):** divine affliction ("the LORD will strike", Deu 28:28) — manner = `divine-affliction`. `[R]`(head). New A3 manner value.
- **valence (BIVALENT):** neutral 11 (feigned/clinical/rhetorical) / sinful 13 (moral madness). Flips per verse — the discriminator. `[M]`(head).
- **pole-opposite:** M15 (Ecc triad pairs madness with wisdom); also adjacent to **M01 (Fear/panic)** — co-seat tim.ma.hon "terror" 2× (Deu 28:28 madness+confusion). `[M]`(collection).
- **binding (A5):** in Deu 28:28 madness is **partner** to blindness + confusion-of-mind (a judicial triad); role `partner`/`co-seated`. `[M]`.
- **realm:** mixed — `inner/moral` (Ecc) · `bodily/clinical` (1Sa, 2Ki) · `forensic/judicial` (Deu, Zec divine-inflicted). **Three realms on one family** — A4 realm tag earns its keep here.

### U4 — to ACT/BECOME a fool (EXPRESSION)
- **the act:** act foolishly / become a fool / make foolish. `[M]`(head) sense+type.
- **the manner (A3):** NONE/intrinsic — the verb is the act. `[M]`.
- **what it expresses (binding):** the inner folly (U1/U2); in Rom 1:22 it expresses **idolatrous self-wisdom** (adjacent: "claiming to be wise"). `[R]`(adjacent).
- **acted on what?** ya.al → princes/people (object=person 2×); mōrainō → salt/wisdom (object). `[M]`/`[R]`.
- **who acts?** the people (Rom 1:22), **God** (1Cor 1:20 — God makes the world's wisdom foolish, divine=agent). `[R]`(head).
- **pole-opposite:** M15 — mōrainō co-occurs sofos 2×, sofia 1× ("became fools" vs "claiming wise"). `[M]`.
- **mutability:** the bearer transitions (Rom 1:22 "became") — supports U1/U2 CHANGEABLE. `[M]`.

### U5 — DISGRACE / OUTRAGE — ne.va.lah (EXPRESSION: deed of disgrace)
- **the act:** an outrage / outrageous thing **done** (sense invariant). `[M]`(head).
- **the manner (A3):** *asah* "to do/commit" 12/13 — the deed is **committed**; manner = the doing itself. `[M]`(head).
- **what it expresses:** senselessness that violates covenant order — bound to a sexual/covenant crime (Gen 34:7 Dinah; Deu 22:21; 2Sa 13:12 Tamar; Judg 19-20). `[R]`(adjacent) — the crime named in the passage.
- **acted on what? (object)** **Israel / the community** (object=Israel 4×, "in Israel"). `[M]`(head) — distinctive: the wronged party is the covenant community, not an individual.
- **who acts?** the offender (Shechem, the Gibeah men, Amnon, Achan). `[R]`(adjacent).
- **valence:** sinful 13/13 — the **only invariantly-sinful unit**. `[M]`.
- **binding:** partner to a.nah "humble/violate" 2×, a.tsav/cha.rah "anger" (the victim's family's grief). Role `cause` (the outrage causes grief). `[M]`.
- **realm:** **`social/communal`** — a public disgrace in Israel. `[R]`. *(A4 realm vocabulary gap — Q&A Q2.)*
- **mutability:** N/A — a deed, once done, is not "reversed" (NONE, not UNRESOLVED). `[M]`.

### U6 — singleton fringe
- pa.chaz "unstable/reckless" — STATE/QUALITY, valence sinful, "unstable as water" (Gen 49:4). `[R]`.
- oknēros "slothful" — QUALITY/will-defect; valence varies sinful (Mat 25:26)/forbidden (Rom 12:11 "do not be slothful")/neutral (Phil 3:1 "no trouble"); pole-opposite to **M34 (diligence/spoudē)** + M19 (zeal/zeō) — co-seat present. `[R]`. **Membership flag: oknēros is a will/diligence-defect, weakly a folly term.**
- har.hor "fancies of the head" (Dan 4:5, Aramaic) — EXPRESSION/thought-content (mental imagery), experiencer=self; **borderline M16 membership** (it is dream-fancy, not folly). `[R]`.
- pash "transgression" (Job 35:15) — reads as M10-sin; **mis-homed in M16**. `[R]`.

---

## 4. Pole-relation synthesis vs M15 (Wisdom) — the headline finding

M16 is the **mechanically-confirmed antithesis of M15.** Across units, M16 terms co-occur with M15 terms **44 times** in-verse (cha.kham "wise" 22×, da.at "knowledge" 12×, bin/bi.nah "understanding" 7×, a.rum "prudent" 5×, sofos/sofia 12×, fronimos 4×). The pairing is **structural, not incidental**:
- **Ecc 1:17, 2:12, 7:25** set "wisdom **and** madness **and** folly" as the explicit triad of objects Qoheleth studies — wisdom on one pole, madness+folly on the other.
- **Pro 26:5** "answer a fool… lest he be **wise** in his own eyes" — fool defined against wise.
- **1Cor 1:18-27** runs the **paradox-inversion**: the world's wisdom is folly to God; God's "folly" (the cross) is wiser than men — the pole **inverts by bearer** (A1).

**pole-relation = M15 (Wisdom), direct inverse**, `derivation=mechanical` (co-occurrence + cross-cluster ownership). The **bearer-flip** (1Cor) is the one read-captured nuance.

Secondary poles: **M34 (diligence)** for oknēros (sloth); **M01 (terror/panic)** adjacency for judicial madness (Deu 28:28 madness+confusion).

---

## 5. Mutability + realm roll-up

- **Mutability:** U1/U2/U4 = **CHANGEABLE-but-resistant** (rod of discipline drives folly out, Pro 22:15; but it will not depart from the hardened fool, Pro 27:22; bearers "become" fools, Rom 1:22). U3 madness = **UNRESOLVED** (no lifting attested in M16). U5 deed = N/A. Transition-trigger manner values surfaced: `corrective/disciplinary` (U2), `divine-affliction` (U3), `transition-into` (Rom 1:22). The first two are **new A3 manner values** (model has inner / ceremonial / NONE only).
- **Realm (A4):** `inner/moral` (U1, U2, much of U3) · `bodily/clinical` (U3 feigned/clinical madness) · `forensic/judicial` (U3 divine-inflicted) · **`social/communal`** (U5 — NOT in the A4 vocabulary). A4 generalises beyond purity (the open question in model v2) — **confirmed**, with one missing value.

---

## 6. The "what kind of thing is folly?" verdict (the stress-test answer)

Folly is **irreducibly multi-kind**, and the evidence (not a prior) decides which per unit:
- as the **fool** (U1) it is an **IDENTITY** (a person-class verdict) with an **intrinsic cognitive/moral faculty-defect** (A2);
- as **folly** (U2) it is a **STATE/condition** seated in the heart, morally weighted, disciplinarily reversible;
- as **madness** (U3) it is a **BIVALENT STATE/EXPRESSION** (clinical-neutral ↔ moral-sinful ↔ judicial-inflicted);
- as **acting/becoming foolish** (U4) and as **the outrage** (U5) it is an **EXPRESSION** (a deed) — U5 specifically a **communal deed of disgrace**, a status-POS term that is lexically an act.

The model v2 **handled the span** — A1 (bearer flip on 1Cor), A2 (identity↔characteristic on the fool), A3 (act how-gap), A4 (three+ realms on madness), A5 (pole-opposite binding to M15) all fired on real per-verse evidence. **Two genuine gaps** emerged: a missing **realm value (`social/communal`)** and missing **transition-manner values (`corrective/disciplinary`, `divine-affliction`)**; and **one structural tension** — the fool's IDENTITY (U1) and folly's STATE (U2) are the *same property* viewed as person vs condition ("the fool is his folly"), which the six-type scheme splits but the synthesis layer will want linked.

---

## 7. Q&A — discovery register

**Q1. Does folly need a 7th object-type the model v2 lacks?**
**A (grounded): No new top-level type — but it exposes that IDENTITY and STATE can be the SAME property in two guises.** The fool (IDENTITY, U1) and folly (STATE, U2) are lexically one defect: e.vil (adjective, the fool) ↔ iv.ve.let (noun, the folly) share root and heart-seat; Pro 22:15 says *folly* is in the *child's* heart — the state lives in the person who *is* the fool. The six types are sufficient, but a **`derived-from`/`person↔condition` link** between an IDENTITY and its cognate STATE is needed so synthesis doesn't treat them as unrelated. Candidate model addition: a **noun↔adjective cognate-pairing** marker (mechanical: shared root + opposed POS), NOT a 7th type. `derivation=read`.

**Q2. Is the A4 realm vocabulary complete?**
**A: No — add `social/communal`.** ne.va.lah (U5) is invariantly "an outrage **in Israel**" against the covenant community — a realm that is neither ritual, inner, forensic, nor eschatological. The A4 open question ("does realm generalise beyond purity?") is answered **yes**, and the list needs a fifth value. `derivation=mechanical` (object=Israel/community 4× + the "in Israel" formula).

**Q3. Does the A3 transition-trigger.manner vocabulary cover folly?**
**A: No — add `corrective/disciplinary` and `divine-affliction`.** Model v2 has manner = {inner · ceremonial/bound-rite · NONE}. M16 needs: **`corrective/disciplinary`** (the rod drives folly out, Pro 22:15 — neither inner nor ceremonial) and **`divine-affliction`** (the LORD strikes with madness, Deu 28:28). Both are read off named measures (the disciplining instrument; the divine-agent verb). `derivation=mechanical`.

**Q4. Can a status-POS term be an EXPRESSION (does POS over-determine object_type)?**
**A: Yes — ne.va.lah proves POS is a default, not a verdict.** It is a noun (type=status) but invariantly a **deed done** (*asah* 12/13, object=community). The object_type rule must let **invariant deed-sense + an act-binding (asah) override the status-POS default to EXPRESSION**. This refines the §3 rule (currently "type=status+valence-varies→state"): add *"unless sense is invariantly a deed and a doing-verb binds it → expression."* `derivation=read` (the override), facts mechanical. A reusable rule, not folly-specific.

**Q5. How does the bivalent/bearer machinery hold on a "negative" cluster (vs M15's positive tamim test)?**
**A: It holds and is symmetric.** M15 found tamim flipping characteristic↔quality by bearer (human vs divine/way). M16 finds folly flipping the **valence** of the SAME pole: the world's wisdom is *folly to God* and God's *folly* is wisest (1Cor 1:18-27) — the A1 bearer-flip works on a negative term exactly as on a positive one, with the **pole itself inverting** by bearer. The pole-pair stress test **passes**: running M16 against M15's machinery reproduced the antithesis mechanically (44 in-verse co-occurrences) and the one paradox-flip read cleanly. Confidence that model v2 generalises beyond positive virtues is now high. `derivation=read` (the synthesis judgement).

---

### Return-summary (for the caller)
- **Path:** `Sessions-v2/M16-Folly/findings/wa-m16-collection-lexical-v1-20260624.md`
- **Per-unit object_type:** U1 fool = **IDENTITY** (+ intrinsic CHARACTERISTIC faculty, A2; 1Cor bearer-flip to QUALITY-on-God); U2 folly = **STATE** (heart-seated, inner/moral); U3 madness = **BIVALENT STATE/EXPRESSION** (clinical-neutral ↔ moral-sinful ↔ divine-inflicted); U4 act-foolishly = **EXPRESSION**; U5 ne.va.lah = **EXPRESSION (communal deed of disgrace)**; U6 = STATE/QUALITY fringe (oknēros + har.hor + pash are weak/mis-homed members).
- **Mechanical-vs-captured:** 81% of field-values mechanical, 19% read (the five read fields); collection calls re-derived mechanically where rules decide, residue tagged read/researcher.
- **Top Q&A / model gaps:** (1) no 7th type needed, but IDENTITY↔STATE are one property in two POS-guises → add a cognate person↔condition link; (2) A4 realm needs **`social/communal`** (ne.va.lah); (3) A3 manner needs **`corrective/disciplinary`** + **`divine-affliction`**; (4) status-POS can be EXPRESSION (asah-deed override — a reusable rule); (5) pole-pair stress test PASSES — M16 reproduced the M15 antithesis mechanically (44 co-occurrences) and the 1Cor bearer-flip read cleanly.
