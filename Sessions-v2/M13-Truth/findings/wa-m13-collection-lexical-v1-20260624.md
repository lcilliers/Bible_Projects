# M13 (Truth, Faithfulness and Integrity) — COLLECTION-LEXICAL (Extended Lexical Model v2)

- **File:** wa-m13-collection-lexical-v1-20260624.md · **v1 · 2026-06-24 · Author:** Claude Code · model_version = **v2** (five additions A1–A5).
- **Scope:** the per-term/unit **collection** layer for cluster M13 — `object_type` (bearer-class aware, A1), the type-conditioned EXPECTED answers (design §4) filled across each term's verses, plus `binding` (A5 enriched roles), `pole_relation`, `mutability`, `realm` (A4 where STATE), `transition-trigger.manner` (A3 where relevant). Built from the per-verse VE rows in `Data/wa-ve-lexical-extract-M13-20260624.json` (568 verses, 1,576 occ, 592 focus occ across **25 distinct owned Strong's**).
- **Grounding discipline (bias-guard):** every value FLOWS FROM per-verse-VARYING evidence (sense/object/object_type/experiencer/valence/how + co-seating), cited to the measure. `type`/`faculty` are treated as **lemma-constants** (mechanical bedrock) — **never asserted as per-verse claims**; where a CHARACTERISTIC needs a faculty it is supplied by the **A2 intrinsic-faculty escape** (`derivation=intrinsic`), a collection-level property, **not** a per-verse seat. Every value tagged `derivation=mechanical|read|researcher|intrinsic` + `source-scope=head|adjacent|collection` (R1/R3).
- **Re-grouping note (required by the brief):** the composition reader groups by **owning-registry**, which is PROVENANCE NOISE (registry labels "faith / despair / uprightness" do not match the semantic sense — e.g. `a.man` "believe" sits under *despair*; `ya.shar` "right" under *uprightness*; `e.met` is split across *faith* and *despair*). The units below are **re-grouped by SEMANTIC SENSE**, not registry.

---

## 0. Sense re-grouping — the 25 owned terms → 10 preliminary units

| Unit | object_type (call) | Terms (Strong's) | occ | Re-grouped FROM registry-noise |
|---|---|---|---|---|
| **U1 TRUTH (quality)** | QUALITY / CHARACTERISTIC (bivalent by bearer, A1) | `alētheia` G0225, `alēthēs` G0227, `alēthinos` G0228, `alētheuō` G0226, `e.met` H0571H "truth: true" | 139 | split out of *faith*/*despair*/*truthfulness* |
| **U2 FAITHFULNESS** | QUALITY / CHARACTERISTIC (bivalent by bearer, A1) | `e.met` H0571G "truth: faithful", `e.mu.nah` H0530, `e.mun` H0529, `pistos` G4103, `o.men` H0544 | 183 | *faith* + *despair* + *covenant* merged |
| **U3 BELIEVING / TRUSTING (act / expression)** | EXPRESSION (act of an inner faculty) | `a.man` H0539 | 86 | mis-filed under *despair* |
| **U4 UPRIGHTNESS** | CHARACTERISTIC / QUALITY (bivalent by bearer) | `ya.shar` H3477G, `ya.shar` H3477I, `na.kho.ach` H5228 | 114 | *uprightness* + *justice* |
| **U5 INTEGRITY-OF-HEART** | CHARACTERISTIC | `tom` H8537, `tum.mah` H8538 | 26 | *innocence* + *integrity* merged (one sense) |
| **U6 SINCERITY** | CHARACTERISTIC | `eilikrineia` G1505, `haplous` G0573 | 5 | *sincerity* + *devotion* merged |
| **U7 CERTAINTY / CONFIRMATION (state + act)** | STATE/condition (+ EXPRESSION sub-sense) | `e.met` H0571I "truth: certain", `bebaioō` G0950, `bebaiōsis` G0951, `a.ma.nah` H0548 | 22 | *faith*/*despair*/*strength*/*covenant* |
| **U8 TESTIMONY / WARNING (act)** | EXPRESSION | `ud` H5749B | 9 | *testimony* |
| **U9 DECEIT (pole intruder)** | EXPRESSION (sinful pole) | `sha.qar` H8266 | 6 | *deceit* — the **deceit-pole intruder**, NOT an inner-being characteristic |
| **U10 IRREVOCABILITY** | QUALITY (of a divine act/gift) | `ametameletos` G0278 | 2 | *repentance* |

> The brief anticipated 26 owned terms; the corpus carries **25 distinct owned Strong's** (the `e.met` family resolves to three sub-entries G/H/I, all retained and distributed by sense). `haplous` G0573 ("sound/healthy" — sincerity/single-ness) and `o.men` H0544 are minor; folded into their nearest sense.

**LRT verdict summary (per unit, run at model_version v2):**

| Unit | nature | sense cov | object cov | exper cov | how cov | LRT red flags |
|---|---|---|---|---|---|---|
| U1 TRUTH | characteristic | 100% | 29% ⚠ | 63% | 67% | object sparse — but **legit-silent** for a quality (truth is not transitive); NONE not UNRESOLVED |
| U2 FAITHFULNESS | characteristic | 100% | 26% ⚠ | 57% | 61% | object sparse — legit-silent (a quality borne, not directed) |
| U3 BELIEVING | act | 100% | 79% | 64% | **1% ⚠⚠** | **how-gap = the act-lemma manner gap** (A2/A3); object well-populated (believing is transitive) |
| U4 UPRIGHTNESS | characteristic | 100% | **0%** | 30% ⚠ | 69% | object NONE (a quality of conduct, intransitive) — legit-silent |
| U5 INTEGRITY-HEART | characteristic | 100% | 50% | 77% | 77% | clean |
| U6 SINCERITY | characteristic | 100% | 0% | 20% ⚠ | 0% | thin (5 occ); object/how legit-silent for a manner-quality |
| U7 CERTAINTY | state | 100% | 27% | 45% | 36% | state — expects of-what/mutability (see record) |
| U8 TESTIMONY | act | 100% | 89% | 89% | **0% ⚠** | how-gap (A3 — manner bound, see record) |
| U9 DECEIT | act | 100% | 67% | 100% | **0% ⚠** | how-gap; sinful pole |
| U10 IRREVOCABLE | characteristic | 100% | 50% | 50% | 50% | thin (2 occ) |

**Mechanical-vs-captured (R1), measured across all 592 focus occurrences × per-verse fields:**
- **mechanical = 78.8%** (sense, lemma_meaning, type, object, experiencer, compound, faculty, how, immediate_response, relational, intensity = 3,727 values)
- **captured/read = 21.2%** (object_type, divine_involvement, valence, cause/cause_clause = 1,003 values)
- This matches the corpus meta (object_type, cause, divine_involvement, valence are the API-resolved interpretive fields). The collection-layer values below inherit this split: the **object_type CALL, mutability, pole_relation, binding roles re-derive mechanically** from these per-verse rows; only a handful of bearer-class / pole calls are `read`-captured (flagged per record).

---

## UNIT RECORDS (collection-lexical)

### U1 — TRUTH (quality) · `alētheia` G0225 · `alēthēs` G0227 · `alēthinos` G0228 · `alētheuō` G0226 · `e.met` H0571H

- **object_type = QUALITY ↔ CHARACTERISTIC (BIVALENT BY BEARER — A1)** · `derivation=read` (the bearer split needs a per-verse read) · `source-scope=collection`.
  - **bearer=divine / way / word → QUALITY:** `divine_involvement=possessor` in 8 occ (Psa 25:5 "thy truth", God's truth; Joh "grace and truth"). A property of God/his word, not a human inner characteristic.
  - **bearer=human conduct → CHARACTERISTIC:** "speak truth to one another" (Zec 8:16, `valence=commanded`), truth as the disposition of the upright speaker. A faculty-borne quality of a person.
  - *Evidence for bivalence:* `object_type` over the unit = {abstract 27, situation 3, person 3, God 2, spiritual-being 1}; `divine_involvement` = {possessor 8, object 4, agent 1}. The kind splits by **who bears it**, read per verse — exactly the A1 generalisation. `derivation=mechanical` would NOT recover this; it is `read`.
- **EXPECTED ANSWERS (CHARACTERISTIC / QUALITY, design §4):**
  - **faculty (REQUIRED):** `cognition+moral_evaluation` (123/139 carry it as the lemma's intrinsic faculty) → **A2 intrinsic-faculty escape**: truth is a *cognition/moral-evaluation-faculted* quality, declared once as a collection property · `derivation=intrinsic` · `source-scope=collection`. **NOT** a per-verse seat claim. (Where the verse independently co-seats a faculty term, that is the per-verse seat; the unit-level faculty is intrinsic.)
  - **how does it operate / manner:** populated 67% by the per-verse governing verb (speak / lead / endure / delight-in) · `derivation=mechanical` · `source-scope=head`. The remaining silence is legit-NONE (a quality borne, not always "operated").
  - **directed at what (object):** mostly **NONE / legit-silent** — truth is largely **intransitive** (a property, not acting on a target); object cov 29% and where present it is the *content domain* (word, judgement) not a patient. **States NONE, not UNRESOLVED** (per LRT: not expected for a non-transitive quality).
  - **whose (experiencer):** other 48 · self 22 · other-addressed 17 · `derivation=mechanical`.
  - **valence register:** righteous 69 · commanded 1 · neutral 1 → predominantly **righteous**, `commanded` when enjoined as conduct · `derivation=mechanical (inherent) + read (commanded)`.
- **binding (A5 enriched roles)** · `derivation=mechanical` · `source-scope=head`: the per-verse roles are 165 `partner` / 11 `co-seated` / 9 `qualifier` (the coarse-field 94%-partner artefact, R1 §1 — **NOT a finding**, a field limitation). Synthesis-relevant bindings recovered by re-reading the partners: truth **binds with** `che.sed`/`agapaō` (M05, role=**partner→co-virtue**: "grace and truth", "love rejoices with the truth"), `dikaiosunē` (M26, role=co-virtue), `pisteuō`/`pistis` (M31, role=**expresses** — truth is what belief rests on), `logos` (M15, role=**object/domain** — "the word is truth"). Top co-seat: mish.pat(M26) 8, chay(M25) 4, sha.lom(M33) 4, pisteuō(M31) 4, logos(M15) 4, dikaiosunē(M26) 4.
- **pole_relation = truth ↔ falsehood/lie** · `derivation=mechanical` (co-seating + cross-cluster) · the antithesis surfaces co-seated in the same verses (`pseudos`/`she.qer` "lying", and within U1's own verses Pro 12:19 pairs "Truthful" status with "lying" status). Cross-cluster: the deceit pole (U9 `sha.qar`, M10/deceit territory).
- **mutability = NONE** (not a state — a quality/characteristic) · `derivation=mechanical`.
- **realm (A4):** N/A (not a STATE). (Truth-of-heart cases, where they occur, would be `realm=inner/moral`; not a dominant register here.)

---

### U2 — FAITHFULNESS · `e.met` H0571G · `e.mu.nah` H0530 · `e.mun` H0529 · `pistos` G4103 · `o.men` H0544

- **object_type = QUALITY ↔ CHARACTERISTIC (BIVALENT BY BEARER — A1)** · `derivation=read` · `source-scope=collection`.
  - **bearer=divine → QUALITY:** the dominant register. `divine_involvement=possessor` in **27 occ** (Lam 3:23 "great is thy faithfulness"; Psa "thy faithfulness to all generations"); `object_type=God` 14. God's faithfulness = a property predicated of God. `derivation=read` (bearer call).
  - **bearer=human-faculty → CHARACTERISTIC:** "a faithful man" (`pistos`), "men of truth/faithfulness" (Exo 18:21), faithfulness shown by a servant (Gen 24:49). A person's faculty-in-operation. `object_type=person` 8.
- **EXPECTED ANSWERS (CHARACTERISTIC / QUALITY):**
  - **faculty (REQUIRED):** `cognition+moral_evaluation` (128/183) → **A2 intrinsic** (`derivation=intrinsic`, collection-scope). `pistos` carries `perception` intrinsically (61 occ) — the trusting/reliable-perceiving slant; folded as a second intrinsic faculty for the Greek sub-sense.
  - **how / manner:** 61% — governed verbs (show / keep / deal / lead) · `derivation=mechanical`.
  - **object:** 26% — **legit-silent / NONE** (a borne quality, not transitive). Where present it is the *covenant-relation domain* (faithfulness **to** a person), recovered via the `relational=toward` field + che.sed pairing.
  - **whose:** other 55 · other-addressed 37 · self 13.
  - **valence:** righteous 59 · commanded 5 → **righteous** dominant.
- **binding (A5)** · `derivation=mechanical`: the **signature M13 binding** — faithfulness binds with **`che.sed` (M05) in 108 co-occurrences** (role=**partner→hendiadys**: "steadfast love and faithfulness", che.sed+e.met as a fixed pair). Also `tse.deq`/`tse.da.qah`/`mish.pat` (M26, role=co-virtue righteousness), `na.tan` (M12 give, role=manner-of-bestowal when divine). The 296-partner count is the coarse-field artefact; the **synthesis-relevant binding is the che.sed hendiadys** (read off the recurring partner).
- **pole_relation = faithfulness ↔ faithlessness / treachery** · `derivation=mechanical` · cross-cluster: `sha.qar` (U9, "deal falsely") and `be.ged`/`ma.al` (treachery, M10/M30 territory). The deceit pole co-seats with faithfulness directly (U9 `sha.qar` shows `che.sed` co-seat 6× — the same hendiadys partner, inverted).
- **mutability = NONE** (quality, not a state). · `derivation=mechanical`.

---

### U3 — BELIEVING / TRUSTING (act) · `a.man` H0539

- **object_type = EXPRESSION (the act of an inner faculty)** · `derivation=mechanical` (rule: `type=action` + a binding/co-expressed characteristic → expression) · `source-scope=collection`. `type=action` 85/86; transitive (object cov **79%**). Believing is the **outward act that expresses** the inner faculties of trust/cognition.
- **EXPECTED ANSWERS (EXPRESSION, design §4):**
  - **the act:** believe / trust / be established / find sure (sense varies 22d) · `derivation=mechanical`.
  - **the manner (how) — THE GAP:** how cov = **1%** (1/86). This is the **act-lemma how-gap** the LRT flags. **A3 transition-trigger.manner / A2 reading:** the manner of believing is **NOT an outer ceremonial procedure** (so not `ceremonial/bound-rite`) — it is **`manner=inner` (an inner disposition of trust)**. The how-field is empty because the manner is *intrinsic to the faculty*, not lexicalised as a separate verb. Recorded as `transition-trigger.manner = inner` · `derivation=read` · `source-scope=collection` (the LRT recovery rule: no manner-word in text, manner lives in the faculty). 17/86 occ have neither object nor how (the bare "he believed") — these are legit-NONE on manner (the act IS the disposition).
  - **what it expresses (the bound characteristic):** trust / faith resting on God's faithfulness (U2). The binding co-terms locate it: `che.sed`(M05) 8, `be.rit`(M44) 6 (believing **within** covenant), `ya.da`(M15) 5 (believing as a mode of knowing), `chay`(M25) 4 (Hab 2:4 "the righteous shall live by his faith"). · role=**expresses** · `derivation=mechanical`.
  - **acted on what (object):** person 23 · abstract 21 · God 14 · spiritual-being 3 · `derivation=read` (object_type). Believing is directed at **God** (Gen 15:6 "believed the LORD"), at a **word/report** (abstract), or at a **person**. The `spiritual-being`/`situation` objects are the **odd-one-out** (believing a lying spirit, believing a false situation) → the **sinful-valence occurrences** (sinful 7, forbidden 4).
  - **who acts (experiencer):** other 37 · other-addressed 12 · self 6.
- **valence = BIVALENT BY OBJECT/DIRECTION** · `derivation=read` · righteous 43 · neutral 19 · commanded 9 · **sinful 7 · forbidden 4**. Believing flips valence by **what is believed**: believing God = righteous/commanded; believing a lie / not-believing God = sinful/forbidden. The per-occurrence valence (not the lemma) is the discriminator.
- **pole_relation = believing ↔ unbelief / disbelief** · `derivation=mechanical` · the negated `a.man` ("did not believe", Num 14:11, 2Ki 17:14) is the within-lemma pole.
- **mutability:** N/A as a state; but the act **moves a state** (it is itself a transition-trigger for the believer's standing — "counted to him as righteousness", Gen 15:6) · noted as `binding→transition-trigger` for U7/righteousness-state.

---

### U4 — UPRIGHTNESS · `ya.shar` H3477G · `ya.shar` H3477I · `na.kho.ach` H5228

- **object_type = CHARACTERISTIC ↔ QUALITY (bivalent by bearer — A1)** · `derivation=read` · `source-scope=collection`.
  - **bearer=human conduct → CHARACTERISTIC:** "the upright" (the person), "do what is right in the eyes of the LORD" (Deu 6:18) — a person's moral-evaluation faculty in operation.
  - **bearer=God's way/word → QUALITY:** "the word of the LORD is upright" (Psa 33:4, `divine_involvement=possessor`), "his way is straight" — a property of the divine word/way (parallels A1 tamim).
- **EXPECTED ANSWERS (CHARACTERISTIC / QUALITY):**
  - **faculty (REQUIRED):** `moral_evaluation` (110/114) → **A2 intrinsic** (`derivation=intrinsic`, collection-scope). Uprightness is the *moral-evaluation-faculted* quality. **NOT** a per-verse seat.
  - **how / manner:** 69% — governed verbs (do / walk / lead / make-straight) · `derivation=mechanical`.
  - **object = NONE (0% — legit-silent, INTRANSITIVE)** · `derivation=mechanical`. Uprightness is a quality of conduct/the person, not directed at a target. **States NONE, not UNRESOLVED** (LRT: object NOT expected for an intransitive moral quality — the 0% is correct silence, not a gap).
  - **whose (experiencer):** only 30% (`other` 20, `other-addressed` 9, `self` 5). The low coverage is because uprightness is often **predicated absolutely** ("what is right") without a named bearer — **legit-silent**, the bearer is the implicit subject/God's standard. Where a bearer is named it is captured.
  - **valence:** righteous 91 (dominant) · the rare sinful/forbidden (4/1) are **pole-contrast verses** ("they have NOT done right", Job 33:27 — uprightness named to mark its absence).
- **binding (A5)** · `derivation=mechanical`: binds with `tov`(M04 good) 12, `tsad.diq`/`tse.deq`(M26 righteous) 11, `lev`(M47 heart) 10 (role=**seat** — "uprightness of heart", the one true co-seat in this unit), and contrasts `ra.sha`(M10 wicked) 9 (role=**pole-opposite**). `sha.mar`/`sur`(M30 keep/turn-from) — role=manner (keep upright / turn from evil).
- **pole_relation = upright ↔ crooked / wicked (`ra.sha`, `a.qash`)** · `derivation=mechanical` · the strongest co-seated pole in the cluster (ra.sha M10, 9 co-occurrences; the "straight vs twisted/perverted" image, Job 33:27 `perverted` H5753).
- **mutability = NONE** (characteristic). · realm N/A.

---

### U5 — INTEGRITY-OF-HEART · `tom` H8537 · `tum.mah` H8538

- **object_type = CHARACTERISTIC** · `derivation=mechanical` (rule: faculty present + how-predicate + person bearer → characteristic) · `source-scope=collection`. `type=status` 26/26 but consistently a **human inner characteristic** (the bearer is always a person, `object_type` person 5 / abstract 7 = the integrity-content). Not bivalent — integrity is intrinsically human-borne (God is not said to "have integrity"; God is its **witness/object**, divine_involvement=object 2).
- **EXPECTED ANSWERS (CHARACTERISTIC):**
  - **faculty (REQUIRED):** `conscience` (26/26) → the cleanest faculty call in the cluster; **A2 intrinsic** but here it is also **per-verse co-seated** with `lev`/`le.vav` (M47 heart, 5 co-occurrences: "integrity of heart") — so this unit has BOTH the intrinsic faculty AND a real per-verse seat (`derivation=mechanical/read` for the seat, `intrinsic` for the faculty). The strongest integrity↔heart binding in the corpus.
  - **how / manner:** 77% — "walk in integrity", "in the integrity of my heart and innocency of my hands" (Gen 20:5) · `derivation=mechanical`.
  - **object:** 50% — integrity OF something (heart, way) — the content-domain, recovered via the construct (`tom-le.vav`) · `source-scope=head`.
  - **whose:** self 8 · other 8 · other-addressed 4 — notably balanced (integrity is claimed of self AND ascribed to others, e.g. God to Abimelech "I know you did this in the integrity of your heart").
  - **valence:** righteous 18 (dominant).
- **binding (A5)** · `derivation=mechanical`: `le.vav`/`lev` (M47, role=**seat** — the defining "integrity of heart"); `yo.sher`(M26 uprightness, role=co-virtue — links U5 to U4); `cha.zaq`(M23 strength, role=manner — "hold fast my integrity", Job 27:6); `sur`(M30, role=manner — turn from evil).
- **pole_relation = integrity ↔ crookedness / perversity (`iqqesh`)** · `derivation=mechanical` · 1Ki 9:4 "integrity of heart" vs the bent path.
- **mutability = NONE** (characteristic — though "hold fast / not let go" (Job) implies it can be *abandoned under pressure*; recorded as a binding=manner note, not a state-mutability).

---

### U6 — SINCERITY · `eilikrineia` G1505 · `haplous` G0573

- **object_type = CHARACTERISTIC** · `derivation=mechanical` · `source-scope=collection`. Thin (5 occ). `faculty=conscience` 3/5; the inner disposition of single-minded, unmixed motive ("godly sincerity", 2Cor 1:12; "single eye", Mat 6:22 `haplous`).
- **EXPECTED ANSWERS (CHARACTERISTIC):**
  - **faculty (REQUIRED):** `conscience` → **A2 intrinsic** (`derivation=intrinsic`). `haplous` "single/sound" carries an intrinsic **volition/affect** slant (single-hearted devotion).
  - **how / manner = 0% — legit-silent** (sincerity is itself the *manner* of acting, not a thing acted with a manner; the LRT 0% is correct silence for a manner-quality, NOT a gap).
  - **object = NONE (0%, intransitive)** · legit-silent.
  - **whose:** 20% (1/5) — **legit-silent**; sincerity is predicated of conduct in the abstract ("in sincerity and truth", 1Cor 5:8) without always a named bearer.
  - **valence:** righteous 5/5.
- **binding (A5)** · `derivation=mechanical`: **co-seated with U1 TRUTH** ("sincerity and truth", 1Cor 5:8 — role=co-virtue, the in-cluster link); contrasts `kakia`/`ponēria` (M10 malice/wickedness, role=**pole-opposite** — "not with the leaven of malice ... but sincerity"). `suneidesis`(M47 conscience, role=seat).
- **pole_relation = sincerity ↔ malice / hypocrisy / duplicity** · `derivation=mechanical` (co-seated kakia/ponēria, M10).
- **mutability = NONE**.

---

### U7 — CERTAINTY / CONFIRMATION · `e.met` H0571I · `bebaioō` G0950 · `bebaiōsis` G0951 · `a.ma.nah` H0548

- **object_type = STATE/condition (of a thing/word/covenant being established)** + an EXPRESSION sub-sense (the act of confirming, `bebaioō`) · `derivation=mechanical` (rule: `type=status` + valence-varies + a "settled/sure" sense → state; the `bebaioō` verbs = the transition-act) · `source-scope=collection`. `type` = status 13 + action 8 (the act of confirming) + quality.
- **EXPECTED ANSWERS (STATE, design §4 — the full row):**
  - **of what? (bearer/subject):** a **word / promise / covenant / message** is made sure (`a.ma.nah` "firm covenant"; `bebaioō` "the promise is confirmed", "the testimony of Christ confirmed"; `e.met` H0571I "security/assured") · object_type abstract 4, person 2 · `derivation=read`.
  - **who set it? (origin):** **God / the divine word** (`divine_involvement` possessor 3, giver 1, agent 1) — God establishes/confirms. The NT `bebaioō` cases: God confirms (1Cor 1:8) or the gospel is confirmed by witnesses · `source-scope=head/adjacent` · `derivation=read`.
  - **can it change? (mutability) = FIXED** · `derivation=mechanical` (the sense is "sure / firm / established / irrevocable" — the state is constitutively non-reversible; no verse shows it un-set). This is the defining property of the unit.
  - **what changes it? (transition-trigger):** the **act of confirming / establishing** — `bebaioō`/`a.man`(hiphil "make firm") IS the trigger that moves word→established. **A3 transition-trigger.manner = `inner`** for belief-grounded confirmation, but **`bound-rite`-adjacent** where it is an oath/covenant ratification (`a.ma.nah` "firm covenant" = a covenant instrument) · `derivation=read` · `source-scope=collection`.
  - **valence register:** righteous 7 · neutral 3 — mostly righteous, neutral when descriptively "sure/secure".
  - **pole-opposite:** ↔ shakeable / wavering / void (a promise that fails) · `derivation=mechanical`.
- **realm (A4) = forensic / covenantal** (not ritual/bodily, not eschatological) · `derivation=read` · the confirmation is **forensic-legal** (testimony confirmed, covenant made firm) — the M13 instance of the realm sub-register.
- **binding (A5)** · `derivation=mechanical`: `che.sed`(M05) 2, `na.tan`(M12 give) 2, `ka.rat`(M44 cut-covenant) 1 (role=**manner** — covenant "cut" = how a firm covenant is set), `tse.da.qah`(M26), `sha.lom`(M33).
- **mutability = FIXED** (see above). · **transition-trigger = act of confirming/establishing**, `manner = inner | bound-rite` (oath/covenant).

---

### U8 — TESTIMONY / WARNING (act) · `ud` H5749B

- **object_type = EXPRESSION** · `derivation=mechanical` (`type=action` 9/9, transitive, object cov 89%) · `source-scope=collection`. The act of solemnly warning / testifying / admonishing.
- **EXPECTED ANSWERS (EXPRESSION):**
  - **the act:** warn / testify / admonish / give-warning / charge-solemnly · `derivation=mechanical`.
  - **the manner (how) = 0% — A3 GAP, manner is BOUND:** no manner-verb in text. The manner of testifying is **`bound-rite` / formal-juridical** (a solemn legal charge, often "calling heaven and earth to witness", Deu 30:19; 31:28) — the how is empty because the manner is the *fixed juridical act*, not an inner disposition. `transition-trigger.manner = ceremonial/bound-rite (juridical witness-formula)` · `derivation=read` · `source-scope=adjacent` (the witness-formula is in the surrounding clause).
  - **what it expresses:** the testifier's **fidelity to covenant / the truth charged** (binds `shuv` M45 turn-back, `sha.ma` M41 hear/heed — role=**immediate-response** the act seeks) · `derivation=mechanical`.
  - **acted on what (object):** person 6 (the people warned), God 1, spiritual-being 1 · `derivation=read`. Strongly **person-directed** (testifying TO Israel).
  - **who acts:** other 3 · self 3 · other-addressed 2 · `divine_involvement=agent` 6 (God is the one who testifies/warns).
  - **valence:** neutral 4 · righteous 3 — the act itself is neutral-to-righteous (the warning is good; the content may be judgement).
- **binding (A5)** · `derivation=mechanical`: `sha.ma`(M41 hear) 2 (role=immediate-response sought), `shuv`(M45 return) 2 (role=intended-effect), `sha.mar`(M30 keep) 1; contrasts `ma.rad`/`cha.ta`(M30/M10 rebel/sin, role=pole — the warned-against behaviour).
- **pole_relation = warning-heeded ↔ warning-ignored (rebellion)** · `derivation=mechanical` (co-seated ma.rad/cha.ta).
- **mutability:** N/A (act). · realm = forensic/covenantal (juridical witness).

---

### U9 — DECEIT (the pole intruder) · `sha.qar` H8266

- **object_type = EXPRESSION (SINFUL POLE) — NOT an inner-being characteristic** · `derivation=mechanical` · `source-scope=collection`. `type=action` 6/6, "deal falsely / lie / be false". **This is the deceit-pole intruder the brief flagged** — it sits in M13's verses only because it is the **antithesis** of faithfulness/truth, co-seated with `che.sed`(M05) in **all 6** occurrences (the same hendiadys partner as U2, inverted: "deal falsely / not deal falsely with the kindness").
- **EXPECTED ANSWERS (EXPRESSION, sinful):**
  - **the act:** deal falsely / lie / break faith · `derivation=mechanical`.
  - **manner (how) = 0% — A3:** manner is `inner` (deceitful intent) — no manner-verb; the falseness is the disposition. `transition-trigger.manner = inner` · `derivation=read`.
  - **acted on what (object):** person 4 (deal falsely **with** a person — Gen 21:23 "you will not deal falsely with me", Lev 19:11) · `derivation=read`.
  - **who acts (experiencer):** other-addressed 2 · other 2 · self 2.
  - **valence = SINFUL / FORBIDDEN** (sinful 4 · forbidden 2) — the **only consistently negative-valence unit**; the forbidden cases are the prohibition "you shall not deal falsely" (Lev 19:11, `'al`/`lo` + verb). · `derivation=mechanical (inherent) + read`.
- **binding (A5)** · `derivation=mechanical`: `che.sed`(M05) 6 (role=**pole-opposite within a fixed pair** — faithfulness is what deceit violates); `be.rit`(M44 covenant, role=object — deceit breaks covenant), `ne.tsach`(M34), `na.cham`(M11).
- **pole_relation = deceit ↔ faithfulness/truth (U2/U1)** · `derivation=mechanical` · **this term IS the pole** — it is recorded as the cluster's internal pole-anchor, not as a positive M13 characteristic. **Recommendation: route to the deceit/wickedness cluster (M10) as the analytical home; retain in M13 only as the cited pole-relation for U1/U2.**
- **mutability:** N/A (act).

---

### U10 — IRREVOCABILITY · `ametameletos` G0278

- **object_type = QUALITY (of a divine gift/call)** · `derivation=mechanical` · `source-scope=collection`. Thin (2 occ). "The gifts and calling of God are irrevocable / without repentance" (Rom 11:29); "godly grief produces a repentance not to be regretted" (2Cor 7:10). A **property predicated of a divine act/gift** (bearer=divine → QUALITY, A1).
- **EXPECTED ANSWERS (QUALITY):**
  - **faculty:** none intrinsic (it qualifies an act, not a faculty) → **A2 does not apply**; this is the case where a "characteristic-shaped" lemma is actually a **qualifier/quality of another term** (the gift/call), not a standalone inner characteristic. Flagged below in Q&A.
  - **bearer / of-what:** the divine **gift / calling / repentance** (object_type abstract 1) · `derivation=read`.
  - **valence:** righteous 2/2.
  - **mutability of the thing it qualifies = FIXED** (the whole point: irrevocable). The lemma is essentially a **mutability=fixed predicate** applied to a host term · `derivation=mechanical`.
- **binding (A5)** · `derivation=mechanical`: `klēsis`(M31 calling, role=**host/object** — what is irrevocable), `charisma`(M39 gift, role=host), `metanoia`(M45 repentance, role=host), `soteria`(M38 salvation, role=host). It always **rides a host term** — i.e. it behaves like a **QUALIFIER** more than a free quality.
- **pole_relation = irrevocable ↔ revocable / regretted** · `derivation=mechanical`.

---

## Cross-unit observations (collection-scope)

1. **The che.sed (M05) hendiadys is the spine of M13's positive pole.** Faithfulness (U2) binds che.sed 108×; deceit (U9) inverts the *same* pair (che.sed 6×). The binding-web's strongest M13 edge is **truth/faithfulness + steadfast-love**, and its pole is **deceit + broken-love**.
2. **Bivalence-by-bearer (A1) is pervasive here:** U1 (truth), U2 (faithfulness), U4 (uprightness) all split QUALITY (divine bearer) ↔ CHARACTERISTIC (human bearer) on the same lemma — confirming A1 is the right generalisation, and that `derivation=read` is needed only for the bearer call (the rest re-derives mechanically).
3. **Two faculty homes:** the **cognition+moral-evaluation** family (truth/faithfulness/uprightness — the *epistemic-moral* virtues) and the **conscience** family (integrity/sincerity — the *interior-motive* virtues). Both supplied via A2 intrinsic-faculty escape, not per-verse seats; integrity (U5) is the one with a real recurring per-verse seat (`lev` M47).
4. **The act-lemma how-gap (A2/A3) recurs** on U3 (believing, 1%), U8 (testimony, 0%), U9 (deceit, 0%) — and in **every case the manner is bound, not missing**: `inner` (believing, deceit = intrinsic disposition) or `bound-rite/juridical` (testimony = witness-formula). A3's manner slot homes all three as VALUES, not gaps.

---

## Q&A — Discovery Register (new questions M13 raised)

**Q1. The "intransitive quality" object-silence: is a 0–29% object-coverage a gap or legitimate NONE for a CHARACTERISTIC?**
Model v2 §4 lists "directed at what? (object)" as an EXPECTED answer for CHARACTERISTIC — so the LRT flags U1 (29%), U2 (26%), U4 (0%), U6 (0%) as red. **Grounded answer: it is legitimate NONE, not a gap.** Truth, faithfulness, uprightness, sincerity are **borne** qualities, not transitive acts — they have no patient. The object EXPECTATION should be **conditioned on transitivity**: a CHARACTERISTIC that is a *disposition* (intransitive) legitimately has object=NONE; only a CHARACTERISTIC that *operates on a target* (e.g. love → object) expects one. **Proposed new rule (for 01b v3 / model v2.1): add a `transitivity` sub-tag to CHARACTERISTIC {transitive · intransitive-disposition}, read from the lemma's argument structure; object is EXPECTED only when transitive.** This converts four false red-flags into correct silences.

**Q2. Where does the deceit-pole intruder `sha.qar` (U9) belong — is it an M13 unit at all?**
Model v2 has no slot for a **pole-anchor that is not itself an inner-being characteristic of the cluster.** `sha.qar` is a sinful EXPRESSION sitting in M13 only as the antithesis. **Grounded answer:** it is a **pole-relation citation, not a cluster member** — its analytical home is the deceit/wickedness cluster (M10). **Proposed: a unit-level tag `role-in-cluster = member · pole-anchor · qualifier-import`**, so a term can be *retained-as-cited-pole* without being analysed as a positive characteristic. This generalises the T2-reference principle to the collection layer.

**Q3. `ametameletos` (U10) and `o.men`/`a.ma.nah` behave like QUALIFIERS that ride a host term, not free qualities — does model v2 capture "a characteristic-shaped lemma that is actually a qualifier"?**
**Candidate new item / refinement.** Model v2's `object_type=qualifier` exists, but the §4 expected-answer set for QUALIFIER ("what does it modify? what modification?") was designed for grammatical modifiers, not for **abstract qualities that always predicate a host** (irrevocable→gift/call). **Grounded answer:** treat U10 as `object_type=qualifier (quality-predicate)` with `binding.role=host` carrying the host term — model v2 *can* express it via A5 binding role=host + qualifier, but the **§4 QUALIFIER expected-set should add "of-what-property" (here: mutability=fixed)**. Minor refinement, not a 7th type.

**Q4. Is a 7th object-type needed for CERTAINTY/CONFIRMATION (U7) — a state that is a FORENSIC/COVENANTAL settledness, plus its own confirming-act?**
The model's open question (model v2 §27) asked whether a pure RELATION/bond or PROCESS type is needed. **Grounded answer: NO new type for M13** — U7 fits **STATE** cleanly (of-what / who-set / fixed-mutability / transition-trigger all answerable), and the realm sub-register **A4 already extends to it as `realm=forensic/covenantal`** (answering the model's open "does realm generalise beyond purity?" — **YES, M13 supplies a forensic/covenantal realm value**, the second realm family after purity's ritual/inner/moral). The confirming-act (`bebaioō`) is the **transition-trigger**, not a separate type. So M13 **confirms A4 generalises** and needs **no 7th type**.

**Q5. The A3 `transition-trigger.manner` slot — M13 needs a third manner value beyond {inner · ceremonial/bound-rite · NONE}: a `juridical/forensic` manner (the witness-formula).**
**Grounded answer / proposed new value.** U8 (testimony) and U7 (covenant confirmation) have a manner that is neither a private inner disposition nor a purity/atonement ceremony — it is a **formal legal/covenantal act** (calling heaven and earth to witness; cutting a covenant; confirming testimony). I filed it under `bound-rite` but it is distinct. **Proposed: extend A3 manner to {inner · ceremonial/bound-rite · juridical/forensic-covenantal · NONE}.** This is the cleanest model-gap M13 exposed.

---

### Honest residue (what is missing / unfillable)
- **U6 SINCERITY (5 occ)** and **U10 IRREVOCABLE (2 occ)** are thin — their collection calls are sound but low-evidence; flagged for re-derivation if more verses enter.
- **The 94%-"partner" compound** is a coarse-field artefact (R1 §1) across every unit — the binding roles I recorded (partner→co-virtue, seat, pole-opposite, host, manner) were **read off the partners by hand**; a programmatic enriched-compound rerun (model v2 A5) is the prerequisite for a real binding-web and would re-derive these mechanically.
- **Bearer-class (A1)** for U1/U2/U4 is `derivation=read` (~the 21% captured share) — reproducible only as a preserved judgement until a `bearer` mechanical sub-rule (divine-possessor vs human-subject by morph) is built; the `divine_involvement=possessor` signal already gets ~most of it mechanically and is the candidate rule.
