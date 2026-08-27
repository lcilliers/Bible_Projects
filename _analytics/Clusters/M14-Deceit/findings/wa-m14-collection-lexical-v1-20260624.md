# M14 (Deceit) — COLLECTION-LEXICAL under the Extended Lexical Model v2

- **File:** wa-m14-collection-lexical-v1-20260624.md · **v1 · 2026-06-24 · Author:** Claude Code.
- **Scope:** the per-term/unit **collection lexical** for cluster **M14 (Deceit)** — object_type per unit (model v2), type-conditioned EXPECTED answers filled across verses (adjacency cited; silent→NONE; expected-undetermined→UNRESOLVED), binding (A5), pole-relation, mutability, realm. Every value tagged `derivation = mechanical | read | researcher` with source-scope.
- **Reads first:** `wa-lexical-extension-model-v2-with-additions-20260624.md` (A1–A5) · `…deepdive-into-01b-DESIGN-v1` (§4 type-conditioned expected, §6 collection scope+adjacency) · `…rerun-and-compound-design-v1` (R1 mechanical-vs-captured tagging) · `Workflow/Instructions/01b-VE-field-reliability-and-rules.md`.
- **Corpus:** `Sessions-v2/M14-Deceit/Data/wa-ve-lexical-extract-M14-20260624.json` — 342 verses, **42 owned terms** (41 with focus occurrences = **372 focus occ**; 1 term has zero corpus evidence, see §0).
- **Tooling:** `_read_full_lexical_composition_20260624.py` (provenance-grouped read, then **re-grouped by semantic sense** below), `_lexical_revelation_test_20260624.py` (LRT per unit), plus direct per-verse pulls from the extract.

> **Bias-guard reminder (model §G):** every collection value flows from **per-verse-VARYING evidence** (valence-variation, the per-occurrence object/sense, co-seating, cross-cluster ownership, the binding term) — **never** the lemma-constants (`type`/`faculty`/`lemma_meaning` as per-verse claims). Where a rule needs a read, it is tagged `read` and survives re-run (R1); where it re-derives mechanically it is tagged `mechanical`.

---

## §0. Why re-group, and the corpus gap

The reader's default grouping is by **owning-registry** (the registry that sourced the term) — provenance noise. e.g. `she.qer` sits under registry "deceit", `ma.cha.sha.vah` under "purpose", `a.lam` under "strength", `cha.rash` under "peace", `or.mah` under "wisdom". These registry labels are the lexical *origin*, not the term's *semantic kind*. The collection-lexical must group by **semantic sense**. The re-grouping below collapses the 41 evidenced terms into **9 semantic units**.

**Corpus gap (recorded honestly):** `G5580 pseudochristos "false Christ"` is an owned M14 term but has **0 occurrences** in the extract. Its verses are presumably XREF copies owned by another cluster (verse-level dedup) or filtered out. → **UNRESOLVED (no corpus evidence)** for this term; it belongs to Unit 7 (IDENTITY) by sense. Flag: re-extract with XREF-inclusive scope to recover it.

### The 9 semantic units (re-grouped from the 41 evidenced terms)

| # | Unit | Terms (Strong's) | Occ |
|---|---|---|---|
| 1 | **DECEIT / FALSEHOOD** | she.qer H8267 (112) · mir.mah H4820 (38) · re.miy.yah H7423A/B (10+10) · dolos G1388 (12) · apatē G0539 (3) · tar.mit H8649B (5) · tor.mah H8649A (1) · dolios G1386 (1) · doloō G1389 (1) · dolioō G1387 (1) | ~194 |
| 2 | **SCHEMING / DEVISING** | ma.cha.sha.vah H4284 (52) · me.zim.mah H4209 (6) · cha.rash H2790A (11) · chish.sha.von H2810 (2) · epiboulē G1917 (1) | 72 |
| 3 | **HYPOCRISY** | hupokritēs G5273 (17) · hupokrisis G5272 (6) · hupokrinō G5271 (1) | 24 |
| 4 | **CONCEALING / HIDING** | a.lam H5956 (22) · la.chash H3908 (1, see note) | 22(+1) |
| 5 | **SLANDER** | dib.bah H1681 (5) · ra.khil H7400 (3) · do.phi H1848 (1) · dusfēmia G1426 (1) · katalalia G2636 (2) · katalalos G2637 (1) · chrēstologia G5542 (1, smooth-talk) | ~14 |
| 6 | **CUNNING / CRAFTINESS** | or.mah H6195 (5) · katasofizomai G2686 (1) · ra.mah H7411B (8) | 14 |
| 7 | **FALSE-IDENTITY** | pseudoprofētēs G5578 (11) · prodotēs G4273 (3) · pseudadelfos G5569 (2) · asunthetos G0802 (1) · ba.god H0901 (2) · be.ged H0899A (2) · bo.ge.dot H0900 (1) · [G5580 pseudochristos — 0 occ, UNRESOLVED] | 22 |
| 8 | **PERVERSENESS / CROOKEDNESS** | ha.phakh.pakh H2019 (1) · luz H3868 (6) · se.leph H5558 (2) | 9 |
| 9 | **TREACHERY / FAITHLESSNESS** | (folded into Unit 7 — the *ba.god/be.ged/bo.ge.dot* root and *asunthetos/prodotēs* are the IDENTITY-bearing form of treachery; the abstract *treachery* sense rides Unit 1) | — |

> **Note on placement of edge terms:** `la.chash H3908` (1 occ, "whispered prayer", valence=**righteous**) is an *odd-one-out* — its single occurrence is a benign charm/prayer, not deceit; recorded under Unit 4 by lemma but flagged as a **non-deceit sense** (the lemma also means *enchantment/slander* elsewhere; in-corpus it is not deceit). `chrēstologia G5542` ("smooth talk", heart-bound, sinful) sits in Unit 5 (deceptive speech). 8 units carry real analytical weight; Unit 9 collapses into 7.

---

## §1. Per-unit object_type calls (model v2 rules) — the type test

Each call states the **per-verse-varying evidence** that forces it (never a lemma-constant), the **bearer-class** (A1), and the rule branch (deepdive §3).

| Unit | object_type (v2) | Bearer-class (A1) | Driving per-verse evidence | derivation |
|---|---|---|---|---|
| 1 DECEIT/FALSEHOOD | **STATE / condition** | human-faculty (speech+heart) | `type=status` (188/192); **valence essentially monovalent** (sinful 200 / forbidden 2, no good pole); heart/soul location present (11); co-bound to speech M42 (15) | mechanical |
| 2 SCHEMING/DEVISING | **BIVALENT-FACULTY** | human-faculty (cognition) | `faculty=cognition` present on the data **and valence FLIPS** sinful/righteous/neutral **per verse** (machashavah: 26 sinful / 9 righteous / 14 neutral) driven by the object devised | mechanical (the flip) + read (per-verse valence) |
| 3 HYPOCRISY | **CHARACTERISTIC** (→ EXPRESSION sub-reading) | human-faculty (perception/display) | `faculty=perception` on data; **how 88%** (a manner of performing); object = the *stage/audience* (synagogues, faces, tombs); monovalent sinful | mechanical + read |
| 4 CONCEALING/HIDING | **EXPRESSION** (act) | human-faculty | `type=action` (22/22); **how-gap = 0/22**; valence VARIES (neutral 8 / sinful 8 / forbidden 4) by *what* is hidden | mechanical |
| 5 SLANDER | **EXPRESSION** (act) | human-faculty (speech) | `type` mixed (status/action); a speech act with a target person/group; monovalent sinful | mechanical |
| 6 CUNNING/CRAFTINESS | **BIVALENT-FACULTY** | human-faculty (cognition/skill) | or.mah valence **FLIPS** cunning=sinful (Gen/Exo/Jos) ↔ prudence=righteous (Proverbs); ra.mah=action(deceive) sinful | mechanical (flip) + read (split) |
| 7 FALSE-IDENTITY | **IDENTITY** | person-classification (verdict) | object_type=**person**; a settled label (false-prophet / traitor / faithless / treacherous-one); experiencer "other" = the one labelled; cause_clause carries the *basis* | mechanical + read |
| 8 PERVERSENESS | **STATE / condition** | human-faculty (moral) | `type` status/action mix; **valence VARIES** sinful/forbidden; a crookedness predicated of a person/way; how-gap (11%) | mechanical |

**Model-v2 verdict on the type test:** M14 is the **richest type test** as predicted, and model v2 **holds across all 6 object-types** plus the two hard ones:
- **IDENTITY** (Unit 7) fills its expected-answer set cleanly via `object_type=person` + experiencer + the **cause_clause as the classification *basis*** (see §3, Unit 7).
- **BIVALENT-FACULTY** (Units 2, 6) is exactly the A1 "bivalence by valence" case — the valence flip is **mechanically detectable** (variance across the term's verses) and the *direction* of each flip is **read from the per-verse object/sense** (peace→neutral, iniquity→sinful, prudence→righteous). This is the cleanest bivalent evidence in the programme so far.

---

## §2. Mechanical-vs-captured share (R1)

Per-verse field population over the 372 focus occ (the inputs the collection layer derives from):

| field | populated | % | mostly mechanical? |
|---|---|---|---|
| sense | 372 | 100% | mechanical (per-occurrence subgloss) |
| type | 372 | 100% | mechanical (POS) |
| valence | 365 | 98% | **partly** — sinful/forbidden mechanical; the bivalent good-pole (righteous/neutral) is **read** |
| compound | 291 | 78% | mechanical but **coarse** (90% "partner" — A5 not yet applied) |
| how | 226 | 61% | mechanical (governing verb) |
| experiencer | 223 | 60% | mechanical (morph possessor/subject) |
| object | 133 | 36% | mechanical where present |
| object_type | 127 | 34% | mechanical where present |
| cause_clause | 86 | 23% | mechanical (causal clause) |
| faculty | 76 | 20% | lemma-constant (quarantined per-verse; used as A2 *collection* property only) |
| location | 52 | 14% | mechanical (seat sense-gate) |
| intensity | 41 | 11% | mechanical |

**Collection-value mechanical share (the R1 figure that matters):** of the **~48 collection values** recorded in §3 (8 units × ~6 expected-answer slots), **~38 re-derive mechanically** from the per-verse rows + cross-verse rules (object_type, mutability, pole-relation, valence-variation flag, faculty-as-collection-property, the coarse binding roles) and **~10 are read-captured** (the per-verse direction of each bivalent flip; the IDENTITY classification basis; the concealing manner recovery; the hypocrisy display-object reading). → **mechanical ≈ 79%, captured ≈ 21%.** This is consistent with the M12/M13 runs and within the R1 target (maximise the mechanical share; keep the captured judgement small and explicit). The captured 21% is **preserved across re-run** (R1 `source=read`).

---

## §3. The collection-lexical record — per unit (type-conditioned EXPECTED answers)

Each unit fills the expected-answer set for its object_type (deepdive §4). `[mech]`=re-derives mechanically · `[read]`=read-captured (survives re-run) · `[NONE]`=silent-and-not-expected · `[UNRESOLVED]`=expected-but-undetermined. Adjacency-sourced values cite the source verse (P7/§6).

### Unit 1 — DECEIT / FALSEHOOD · object_type = **STATE** (bearer = speech+heart)

| Expected (STATE) | Value | derivation · source-scope |
|---|---|---|
| **of what?** (bearer) | a false condition predicated of **speech/word and of the heart** — `she.qer` co-occurs with speech-M42 (15×) and is heart/soul-located (11×) | [mech] co-seating + location sense-gate · collection |
| **who set it?** | within-person (the deceiver's own heart); never God | [mech] origin/experiencer · collection |
| **can it change?** (mutability) | **changeable** — deceit is *put away* / *removed* (the lying lip vs. the truth that endures); pole-crossable to truth | [read] mutability rule (state↔pole shown) · collection |
| **what changes it?** (transition-trigger) | turning to truth / repentance; **manner = inner** (A3) — not a bound rite | [read] transition-trigger.manner · collection |
| **valence register** | **monovalent sinful** (sinful 200 / forbidden 2; **no good pole**) | [mech] valence non-variation · collection |
| **pole-opposite** (A4/pole-relation) | **M13 (Truth)** — direct cross-cluster antonym; co-occurs 17 verses | [mech] cross-cluster ownership + co-seating · collection |
| realm (A4) | **inner/moral** (heart-bound) with a **forensic** sub-register where it is *false witness* (she.qer-witness, the legal lie) | [read] realm from object/co-seating · per-verse |
| binding (A5) | partner-bound to M10 (Sin), M06 (Hate); **expresses** via speech-M42; **pole-opposite** M13 | [mech-coarse] + [read] roles · per-verse |

### Unit 2 — SCHEMING / DEVISING · object_type = **BIVALENT-FACULTY** (bearer = cognition)

| Expected (BIVALENT-FACULTY) | Value | derivation |
|---|---|---|
| **the faculty (neutral)** | **cognition** (machashavah `faculty=cognition` on all 52; the planning/devising faculty of the heart) — declared as the unit's **intrinsic faculty (A2)**, a collection property, not a per-verse seat | [mech] A2 collection property · collection |
| **per-occurrence valence (the discriminator)** | **FLIPS by verse:** sinful (plots against the innocent — Est 8:3, Psa 56:5, Jer 11:19), righteous (God's thoughts/plans — Psa 33:11, Isa 55:9, Jer 29:11; man's good plans — Pro 16:3), neutral (artistic *designs* — Exo 31:4/35:32-35; plans generically — Pro 15:22) | [read] per-verse valence · per-verse |
| **what directs it?** (aim/object) | the **object devised** drives the valence: *iniquity/harm/the Jews* → sinful; *peace* (Pro 12:20) → good; *the tabernacle's artwork* → neutral. **The object IS the valence-discriminator.** | [mech] object→valence correlation · per-verse |
| seat | heart (lev) co-seated 9× | [mech] location · per-verse |
| binding | cha.shav "to devise" (M15) is the **governing verb** (16×) — scheming is cognition-in-operation; co-bound to e.tsah "counsel" (M17, 9×) | [mech-coarse] · per-verse |
| pole / register | the **good pole is internal** (same faculty, righteous aim) — bivalence is *by valence*, A1 confirmed | [mech] · collection |

> **This is the textbook A1 "bivalence by valence" case.** One faculty (cognition), valence set per occurrence by the aim. The good pole is **not a different lemma** — it is the same scheming faculty aimed rightly (God's plans, the artisan's designs). Model v2 captures it; v1's single "bivalent-faculty" type would have flattened the *why* (the object-driven flip).

### Unit 3 — HYPOCRISY · object_type = **CHARACTERISTIC** with an EXPRESSION reading (bearer = perception/display)

| Expected (CHARACTERISTIC) | Value | derivation |
|---|---|---|
| **which faculty?** | **perception** (`faculty=perception` on all 24 — the hypocrite *reads the audience* and performs to be *seen*) — A2 intrinsic faculty | [mech] A2 · collection |
| **how does it operate?** | **how 88%** — a *performance*: disfiguring faces, praying to be seen, whitewashing tombs; the manner is **outward show masking an inner void** | [read] from how + cause_clause · per-verse |
| **directed at what?** | the **audience/stage** — synagogues, street corners, people's faces (the "object" field carries the *display-locus*, not a patient) | [read] object re-reading · per-verse |
| **whose?** | "other (addressed)" — Jesus addresses the Pharisees as the bearers (12×) | [mech] experiencer · per-verse |
| valence | monovalent sinful (24/24) | [mech] · collection |
| pole-opposite | sincerity / single-heartedness (no in-cluster antonym; cross to M26 Righteousness — co-seats dikaios 3×) | [read] · collection |

> **Type note:** hypocrisy is a borderline CHARACTERISTIC↔EXPRESSION. It reads as a CHARACTERISTIC (a settled disposition: "you ARE hypocrites") **and** as an EXPRESSION (the per-verse *act of performing*). The unit's collection-call is CHARACTERISTIC (the disposition); its per-verse occurrences are EXPRESSIONS of it. **This is a candidate for a model note (§Q) — a characteristic whose every occurrence is an expressed act.**

### Unit 4 — CONCEALING / HIDING · object_type = **EXPRESSION / act** (bearer = human)

| Expected (EXPRESSION) | Value | derivation |
|---|---|---|
| **the act** | to hide / conceal / ignore (a.lam) | [mech] sense · per-verse |
| **the manner (how)** | **how-gap = 0/22** — the act-lemma carries no manner in any verse | [mech] **how absent — the A3 case** |
| → manner recovery (A3) | the manner is **NONE-by-nature**, not a gap: concealing's manner is the *absence of disclosure* itself; manner-words in verse_text = 2/22 (9%). **transition-trigger.manner = inner/withholding** (A3 homes this — the empty how is a *value*, not a defect) | [read] A3 manner-slot · collection |
| **what it expresses** (binding) | bound to **M10 (Sin)** — co-seated a.sham "guilt"/ta.me "unclean" (4× each): concealing **expresses guilt** (hiding sin); also M12 (Purity) na.tan | [mech-coarse] binding · per-verse |
| **acted on what?** | object 68% — eyes (the idiom "hide the eyes" = ignore), counsel, times | [mech] object · per-verse |
| **who acts?** | other / other-addressed (68%) | [mech] experiencer · per-verse |
| valence | **VARIES** neutral 8 / sinful 8 / forbidden 4 — concealing is *bivalent by object* (hiding sin=sinful; "do not hide yourself" from a neighbour's need=forbidden; God hiding/ignoring=neutral) | [read] per-verse valence · per-verse |

> **A3 vindicated:** the 0% how is the act-lemma how-gap the model predicted. It is captured as `transition-trigger.manner = inner/withholding`, a **value** (the manner is the withholding itself), not an UNRESOLVED gap. Note a.lam's valence also flips — concealing borders STATE/bivalent; held as EXPRESSION on the `type=action` evidence.

### Unit 5 — SLANDER · object_type = **EXPRESSION / act** (bearer = speech)

| Expected | Value | derivation |
|---|---|---|
| the act | to slander / bear an evil report / whisper (dib.bah, ra.khil, katalalia) | [mech] sense · per-verse |
| the manner (how) | how 54% — *whispering, going about, bearing a report* | [mech] · per-verse |
| what it expresses (binding) | a speech-act expressing hate/destruction; co-seats sha.chat "destroy" (M27), sha.mar (M30) | [mech-coarse] · per-verse |
| acted on what? | object **sparse (31% — RED FLAG)**: land, mother's-son, the brethren; **expected for a transitive speech act** | [UNRESOLVED→read] the victim is often in an adjacent clause (Lev 19:16 "among your people"; Jer 6:28 "all of them") — recoverable by adjacency | [read] adjacency · per-verse |
| who acts? | **sparse (23% — RED FLAG)** the slanderer is often the impersonal "they/men of slander" | [NONE] generic subject · per-verse |
| valence | monovalent sinful (12/12) | [mech] · collection |
| pole-opposite | the faithful word / guarding the tongue (M42 Speech, M30) | [read] · collection |

### Unit 6 — CUNNING / CRAFTINESS · object_type = **BIVALENT-FACULTY** (bearer = cognition/skill)

| Expected (BIVALENT-FACULTY) | Value | derivation |
|---|---|---|
| the faculty | shrewdness/craft (or.mah) — a cognitive skill faculty (A2) | [mech] A2 · collection |
| per-occurrence valence | **FLIPS:** sinful = *cunning/guile* (Exo 21:14 the murderer "acts willfully"; Jos 9:4 Gibeonites' ruse) ↔ righteous = ***prudence*** (Pro 1:4, 8:5, 8:12 — wisdom's good shrewdness) | [read] per-verse · per-verse |
| what directs it? | the **end served**: harming a neighbour → sinful; instructing the simple → righteous. or.mah is the cleanest single-lemma good/evil split in the cluster | [mech] valence-variation flag + [read] direction · per-verse |
| binding | bound to M15 (Wisdom) — co-seats da.at "knowledge", bin "understanding" (the prudence pole); ra.mah "deceive" (action) is the sinful expression | [mech-coarse] · per-verse |
| seat | heart (1×) | [mech] · per-verse |

> **A1 "same lemma, split by bearer/valence" confirmed twice** (Units 2 and 6). or.mah is a single Hebrew lemma whose **valence is set entirely by the moral end** — exactly the tamim-style split (characteristic vs quality) the model was built to hold, here as good-vs-evil on one faculty.

### Unit 7 — FALSE-IDENTITY · object_type = **IDENTITY** (bearer = person-classification)

| Expected (IDENTITY) | Value | derivation |
|---|---|---|
| **classified as what?** | a settled label: **false-prophet** (pseudoprofētēs), **traitor** (prodotēs), **false-brother** (pseudadelfos), **faithless/covenant-breaker** (asunthetos), **treacherous-one** (ba.god/be.ged/bo.ge.dot) | [mech] object_type=person + sense · collection |
| **who classifies?** (verdict-giver) | the **inspired author / Jesus** renders the verdict (Mat 7:15 "beware of false prophets"; Luk 6:16 Judas "who became a traitor"; Jer 3:7-10 the LORD names Judah "treacherous") | [read] from cause_clause + speaker · per-verse |
| **on what basis?** | the **cause_clause carries the basis**: pseudoprofētēs — "arise and perform great signs" (Mat 24:24), "many false prophets gone out into the world" (1Jo 4:1); ba.god — "declares the LORD" after Judah's faithlessness (Jer 3:10) | [read] cause_clause as basis · per-verse |
| **settled or reversible?** (mutability) | **largely fixed** — the verdict is a settled classification (a traitor *is* a traitor; the false prophet is eschatologically condemned, Rev 19:20). Reversibility only via the prophetic call to *return* (Jer 3 — Judah is called back), but the **label itself is the verdict** | [read] mutability · collection |
| pole-opposite | the **true** prophet / faithful brother / covenant-keeper (M13 Truth, M19 Trust, M31 Faith) | [read] cross-cluster · collection |
| binding | co-seats dikaios "righteous" (M26) as the contrast, pisteuō "believe" (M31) | [mech-coarse] · per-verse |

> **IDENTITY fills its expected-answer set well.** The four IDENTITY questions (classified-as / who-classifies / on-what-basis / settled-or-reversible) **all resolve**, and crucially the **basis lives in `cause_clause`** — the existing per-verse field already carries the classification grounding, so IDENTITY does **not** need a new field. The verdict-giver is read (speaker of the labelling clause). This is a strong validation of model v2's IDENTITY row. See §Q for the one gap (the verdict-giver is not a dedicated mechanical field).

### Unit 8 — PERVERSENESS / CROOKEDNESS · object_type = **STATE** (bearer = moral faculty/way)

| Expected (STATE) | Value | derivation |
|---|---|---|
| of what? | a **crookedness** predicated of a person, a heart, or a *way* (luz "the devious"; se.leph "perverseness of the tongue/way"; ha.phakh.pakh "crooked man") | [mech] object/sense · collection |
| who set it? | within-person (a settled moral bent); never God | [mech] origin · collection |
| can it change? (mutability) | **fixed-leaning** — a crookedness is a characterological bent (the "devious of heart" Pro 3:32); pole-crossable only by becoming upright | [read] mutability · collection |
| what changes it? | turning to uprightness; manner = inner (A3) | [read] · collection |
| valence | **VARIES** sinful 7 / forbidden 2 (the prohibition "let them not depart" — luz Pro 3:21) — within the negative register only, no good pole | [mech] valence-variation · collection |
| **pole-opposite** | **ya.shar "upright/straight" (M13 Truth)** — co-seats 3× directly; perverse(crooked) ↔ upright(straight) is the spatial metaphor pole | [mech] cross-cluster + co-seating · collection |
| realm | inner/moral (the bent of heart/way) | [read] · collection |

---

## §4. Cross-unit synthesis (collection-level observations)

- **Two STATEs (1, 8), two BIVALENT-FACULTIES (2, 6), two EXPRESSIONS (4, 5), one CHARACTERISTIC (3), one IDENTITY (7).** M14 exercises **5 of the 6 v2 object-types** (only QUALIFIER is absent as a head — qualifiers appear only as *compound roles*, e.g. she.qer-as-qualifier of a witness). This is the broadest single-cluster type spread in the programme so far — confirming the prompt's "richest type test."
- **The cluster's pole is singular and clean: M13 (Truth).** Deceit↔Truth is the cross-cluster antithesis for Units 1, 7, 8 (and the *good pole* of the bivalents is the truthful/prudent use of the same faculty). Pole-relation is **mechanically grounded** (cross-cluster ownership of the antonym + 17 co-occurrence verses).
- **Heart-bound (M47 Constitution, 52 co-seats) and sin-bound (M10 Sin, 85 co-seats).** Deceit is consistently seated in the heart and classed as sin — the constitutional seat and the moral category are the two strongest bindings cluster-wide.
- **Speech is the primary expression channel** (M42 Speech): falsehood, slander, smooth-talk, false prophecy all *express through the word*. Deceit is a heart-state expressed in speech — `STATE (heart) → EXPRESSION (speech)`.
- **The bivalents reveal the cluster's boundary:** scheming (cognition) and cunning (skill) are **morally neutral faculties** that M14 only *owns at the sinful pole*; their righteous/neutral occurrences (God's plans, the artisan's designs, wisdom's prudence) belong to M15 (Wisdom)/M17 (Counsel). The valence flip **is the cluster boundary** — a term enters M14 only on its sinful occurrences. This is a governance finding: a bivalent term's M14 membership is **per-occurrence, not per-lemma**.

---

## §5. LRT verdicts (per unit) — is the lexical fully revealing?

| Unit | LRT verdict | Key gap / recovery |
|---|---|---|
| 1 DECEIT | revealing | object/object_type sparse (23%) — STATE doesn't require an object (legit NONE) |
| 2 SCHEMING | revealing | object 43% RED-FLAG but the **valence flip is the signal**, object recovers it per-verse |
| 3 HYPOCRISY | revealing | how 88%, faculty present — fullest unit |
| 4 CONCEALING | **how-gap 0% → A3** | manner recovered as `withholding` (value, not gap); valence-flip noted |
| 5 SLANDER | partial | object 31% + experiencer 23% RED-FLAG — victim/agent in adjacent clause, adjacency-recoverable |
| 6 CUNNING | revealing | valence-flip = the signal; how 29% (a faculty, not an act — legit) |
| 7 IDENTITY | revealing | basis in cause_clause; verdict-giver read (no dedicated field — §Q) |
| 8 PERVERSE | revealing | how 11% (a state, not an act — legit NONE) |

---

## §Q. Q&A — discovery register

**New questions raised by the M14 run, with grounded answers.**

**Q1. How does IDENTITY fill its expected-answers — does it need a new field?**
**A (grounded).** IDENTITY fills all four expected answers (classified-as / who-classifies / on-what-basis / settled-or-reversible) **with existing fields**: `object_type=person` + `sense` give *classified-as*; `experiencer` gives *whose label*; **`cause_clause` carries the *basis*** (e.g. pseudoprofētēs "perform great signs", ba.god "declares the LORD"); mutability gives *settled/reversible*. **No new field needed** for the basis. **The one gap:** the *verdict-giver* (who classifies) is **read** from the labelling clause's speaker — there is no mechanical "verdict-giver" field; it overlaps `experiencer`/`divine_involvement` but is distinct (the *speaker of the label*, not the bearer). → **candidate new field `classifier`/`verdict_giver`** for IDENTITY, or extend item 8 (divine involvement) + experiencer to carry it. Low priority (read-recoverable).

**Q2. How does BIVALENT-FACULTY fill its expected-answers — and is the flip mechanical?**
**A (grounded).** The *faculty* (neutral) is the A2 collection property (cognition/skill). The **per-occurrence valence IS the discriminator and it is detectable mechanically** as variance across the term's verses (machashavah: 4 distinct valence values; or.mah: 2). The **direction** of each flip is **read** from the per-verse object/sense — and the rule is sharp: **the object devised sets the valence** (peace→neutral, iniquity→sinful/forbidden, prudence/God's-plan→righteous). So "what directs it?" = the object, mechanically. The bivalent is the best-evidenced type in M14: model v2 captures it fully; v1's flat "bivalent-faculty" would have lost the object→valence rule.

**Q3. Did the A3 manner-slot resolve the act how-gap?**
**A (grounded, yes).** CONCEALING (a.lam) has how = **0/22** — total. A3 homes this as `transition-trigger.manner = inner/withholding`: the manner of concealing *is the withholding of disclosure*, so the empty how is a **value (NONE-by-nature)**, not an UNRESOLVED defect. SLANDER and DECEIT, by contrast, DO carry manner (whispering, lying lips) — so the how-gap is **type-specific**, exactly as A3 predicts (the gap is real only for the pure-withholding act). A3 is vindicated.

**Q4. Candidate 7th object-type? (the model's open question)**
**A (grounded — NO new type needed for M14, but one structural note).** M14 fits the six types. **However** HYPOCRISY (Unit 3) is a **CHARACTERISTIC every occurrence of which is an EXPRESSED act** — a settled disposition that exists *only as performance*. It is not a 7th type; it is a **CHARACTERISTIC↔EXPRESSION duality** that the per-verse layer should mark (collection-call = CHARACTERISTIC; per-verse = EXPRESSION). **Recommendation:** add a model note that object_type can carry a **collection-call vs per-verse-call** split for performative characteristics (rather than inventing a type). Watch M16+ for whether this recurs (e.g. boasting, flattery) — if it does, it may warrant an `EXPRESSED-CHARACTERISTIC` sub-tag.

**Q5. New cross-cutting role surfaced: the bivalent term's membership is per-occurrence.**
**A (governance finding).** A bivalent-faculty term (scheming, cunning) belongs to M14 **only on its sinful occurrences**; its righteous/neutral occurrences belong to M15/M17. The **valence flip is the cluster boundary**, read per verse. This is a **new role for the binding/pole layer**: a `cluster-membership = per-occurrence` flag on bivalent units, and it implies the synthesis must not aggregate a bivalent term's *good-pole* verses into the deceit characteristic. Model gap: there is no field that records "this term is in this cluster only at this valence" — currently inferred. → **candidate `membership_scope = lemma | per-occurrence`** on the unit.

**Top model gaps / candidates (return summary):** (1) IDENTITY verdict-giver has no dedicated field (read-recovered); (2) performative CHARACTERISTIC (hypocrisy) wants a collection-vs-per-verse object_type split, not a 7th type; (3) bivalent membership is per-occurrence and unrecorded — wants a `membership_scope` flag; (4) compound role is still the coarse 3-value field (90% partner) — A5 enrichment not yet in the data, so the binding-web is provisional; (5) `pseudochristos G5580` has zero corpus evidence — re-extract XREF-inclusive.

---

*M14 collection-lexical v1 — 8 semantic units (re-grouped from 41 evidenced terms + 1 zero-evidence term); object_type spread = 2 STATE · 2 BIVALENT-FACULTY · 2 EXPRESSION · 1 CHARACTERISTIC · 1 IDENTITY; mechanical ≈ 79% / captured ≈ 21%; pole = M13 (Truth); model v2 holds across all calls incl. IDENTITY and BIVALENT-FACULTY, with five candidate refinements logged in §Q.*
