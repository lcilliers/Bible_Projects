# M10 cold-read validation — the CHARACTERISTIC vs CONDITION/STATE object-kinds

- **File:** wa-m10-validation-characteristic-condition-v1-20260624.md · **v1 · 2026-06-24 · Author:** Claude Code.
- **Mandate:** cold read against the **lexical** (per `wa-m10-m11-coldread-validation-framework-and-foundation-v1`). Test whether the CHARACTERISTIC kind (#20 Faithlessness, #21 Perversion, #27 Iniquity-scheming) and the CONDITION/STATE kind (#11/#12 sin-noun, #24 Evil-constitutional, #29–32 Defilement) are **grounded in the per-verse evidence** (sense/object/object_type/experiencer/valence) or **relabel lemma-constants** (faculty/type).
- **Method:** induction-first — for each unit the per-verse aggregate was computed mechanically from the corpus (`scripts/_tmp_m10_charcond_validate.py` over `wa-m10-corpus-1904verses-v1_0`), the legit fields read *before* the claim, the claimed kind judged last. faculty/type excluded as per-verse evidence (they are lemma-constants per §2 of the framework).
- **Anti-confirmation note:** the validator is Claude and carries the same harvest-to-fit reflex; null default applied (every kind is IMPOSED until the per-verse evidence earns it). A "low imposition" result would itself be re-scrutinised.

---

## §A. Headline verdict

**Both object-kinds are predominantly TYPE-TAG RELABELS.** The characteristic↔condition distinction is **not carried by any legitimate per-verse field** — it is the `type` tag (action ↔ status), which is a lemma-constant, plus the `faculty` tag, which is 100% constant and mostly empty. Reading the legit per-verse evidence (sense/object/object_type/experiencer/valence) for the six units, the two kinds are **not distinguishable**: both are sin-glosses, both have ~50% empty object/object_type, both sit on a sinful valence, both touch the heart/soul at a low rate. The one place where the per-verse evidence *does* earn a real distinction is **defilement's non-moral valence** (CONDITION) and, weakly, **a.ven's per-verse type-variation + experiencer=self** (CHARACTERISTIC #27) — these are partial, term-specific footholds, not a grid.

- **Imported-meaning rate (kind-level claims):** **5 of 6 units** carry the kind label primarily on a constant tag → `TERM-CONSTANT`/`IMPOSED`. Only **#29–32 Defilement** earns its "state" reading from a genuine per-verse field (valence) → `SUPPORTED (partial)`. #27 is the strongest characteristic foothold but still rests its headline ("most-seated = the data signature") on a frequency, not a per-verse discriminator → `OVERREACH`.

---

## §B. Claim × verdict × per-verse evidence × corrected reading

| # | Unit / claim | Claimed kind rests on | Legit per-verse evidence (sense/obj/obj_type/exp/val + location) | Verdict | Corrected reading |
|---|---|---|---|---|---|
| #27 | **Iniquity-scheming** = the **anchor CHARACTERISTIC** — "faculty in operation"; "most-seated is the data signature" | O1 rests on `faculty` (a.ven `[affect,moral_evaluation]` **constant on all 69**; ro'a None on all 14); O2 rests on interior-seating *count* | a.ven **`type` varies status 46 / action 16** (genuinely per-verse ✓); location heart/soul/inward **13/83 ≈16%**; sense = iniquity/evildoers/trouble; object_type empty on most; experiencer=other dominant, **self present**. The generative metaphor (conceive→birth) is in the *verse text/sense*, not a lexical field. | **OVERREACH** (O1 `TERM-CONSTANT`; O2 a *frequency* not a per-verse property) | a.ven is the **one unit with a real per-verse action/status split** and the densest interior count — so it has the *best* claim to "operative". But "faculty in operation" reads the constant faculty tag; the operative signal is the **type-variation + the verse-level generative predicate**, not the kind label. Keep #27 as the strongest characteristic candidate; ground it on type-variation + co-seating, not "faculty". |
| #21 | **Perversion** = CHARACTERISTIC ("inner inversion", faculty/disposition in operation) | `type` **constant per-term on all 14 lemmas**; `faculty` **None on 63/64** | sense = perverted/corruption/subverts/destroys (lemma-driven); object_type **empty 34/64**, else abstract 14 / person 11; **object = "cause/justice/mind"** in the bribe-and-corrupt-the-mind verses; location heart 7 / mind 1 / flesh 1; co-seated lev 5, nous 1, sarx 2. | **IMPOSED / TERM-CONSTANT** | The unit is a **lexical grab-bag of two registers** (Hebrew bend/twist + Greek corrupt-the-mind) glued by the lemma glosses, not by any per-verse field. Its own §G admits #21 is "partly consequence" and cha.val is mis-glossed. "Characteristic-in-operation" is not in the per-verse evidence; the legit signal is only the **heart/mind co-seating on ~9/64 occ**. Not a clean characteristic. |
| #20 | **Faithlessness** = CHARACTERISTIC ("the will that breaks covenant loyalty") | `faculty` **None on all 101**; type action 74 / status 26 (varies on 2 of 3 lemmas) | sense = treacherous/faithless/breach (lemma-driven); **object = Lord/God 36 occ** (the covenant partner) — a real per-verse object pattern; object_type empty 35, else **God 32**; experiencer=other; location **soul 9** (ne.phesh co-seated 3). | **CONTRADICTED (as a "characteristic")** | The per-verse evidence makes #20 **RELATIONAL/directed-against-God**, not an inner faculty — object is overwhelmingly *the Lord*. Its own §G concedes the faithfulness-pole "lives in M13/M31". The relational object is the genuine per-verse signal and it points away from "inner-being characteristic". `type=action` is the only support and it is a lemma tag. |
| #11/#12 | **Sin-noun** (chat.tat + a.von) = CONDITION/STATE ("the state all stand under" / enslaving power) | `type=status` **431/432** (H2403H, H5771G fully constant; only H2403B varies, 1 occ action) | sense = iniquity/sin/sin-offering (lemma); object_type empty 247/432, else abstract 132 / person 25; **object = Jeroboam/blood/people/sin-offering** (referents, not a "state"); experiencer mixed; valence sinful 334 / **commanded 31 / neutral 59** (the sin-*offering* sense); location soul 18 / heart 15 (≈40/432 ≈9%). | **TERM-CONSTANT / IMPOSED** | "Condition/state" = the lemma's `type=status` tag, full stop — there is **no per-verse field that reads "the state one is under"**. The cited Pauline "under sin / enslaving power" texts (Rom 5–8) are a *verse-text* register, **not** lexical fields (object is "blood/Jeroboam/offering", not "bondage"). The "universal condition" is a theological frame on a status tag → needs the root verse → `LEXICAL-GAP` for the operative predicate. |
| #24 | **Evil-constitutional** = CONDITION ("built into the nature / the heart's default") | `type` quality 56 / status 22 (constant per-term bar G4190); `faculty=moral_evaluation` **constant on 77/78** | sense = evil/wicked/malice/evil-one (lemma); **object_type empty 68/78**, object empty 58/78; location heart 6 / mind 2 / soul 1 (**11/78 ≈14%**); co-seated kardia 6. | **IMPOSED** (its own §G: "~8 heart-seatings of 88… a strong frame on a bounded set") | The "constitutional / heart's-default-output" reading is a **frame on ~8–11 heart occurrences out of 78**; the modal per-verse evidence is the **bare adjective "evil"** with empty object/object_type. ponēros is mostly a *verdict-face* (evil generation/deeds/eye), i.e. a quality tag, not a state-the-inner-being-is-in. The constitutional claim is not pervasively evidenced. |
| #29–32 | **Defilement** = CONDITION/STATE (the cleanest "state is its own kind") | `type` constant per-term; `faculty` **None on all 226** | sense = unclean/defiled/impurity (lemma); object = **"evening" 25** (the duration of the state), spirit/days/clothes; object_type person 65 / thing 24; **valence neutral 84 + forbidden 31 + sinful 96 + righteous 4** — *valence genuinely varies per-verse*; location flesh 18 / soul 18 (**39/226 ≈17%**). | **SUPPORTED (partial)** | This is the **one unit where a legit per-verse field earns the kind**: `valence` **varies (neutral/forbidden/sinful)** within the same lemma (H2931: neutral 31 / sinful 16 / forbidden 10; H5079: neutral 8 / sinful 7), proving a **non-moral state** exists — exactly Obs-04 O5. The "until evening" object also marks a *durative state*. So "state can be non-moral" is grounded. But "condition" as a *kind* still leans on `type`; what the evidence actually carries is **non-moral durative uncleanness**, not the four-subtype "condition" superstructure. |

---

## §C. The decisive cross-kind test — does the per-verse evidence DISTINGUISH characteristic from condition?

Reading the legit fields side by side, the two kinds are **not separated by any per-verse field**:

| Field (legit, per-verse) | CHARACTERISTIC (#20/#21/#27) | CONDITION (#11-12/#24/#29-32) | Distinguishes? |
|---|---|---|---|
| **sense** | sin-glosses (perverse, treacherous, iniquity) | sin-glosses (sin, evil, unclean) | **No** — both lemma-driven |
| **object_type** empty rate | #20 35/101 · #21 34/64 · #27 high | #11-12 247/432 · #24 68/78 · #29-32 113/226 | **No** — ~50% empty both sides |
| **valence** | sinful-dominant | sinful-dominant **except defilement (neutral 84)** | **Only at defilement** |
| **location/co-seat** rate | #20 ~10% · #21 ~14% · #27 ~16% | #24 ~14% · #11-12 ~9% · #29-32 ~17% | **No** — defilement (a "condition") seats *more* than faithlessness (a "characteristic") |
| **type** (EXCLUDED — lemma-constant) | action-leaning | status-leaning | this is the *only* separator, and it is a tag |

The supposed discriminator in Obs-07 — **"seatedness is the data-level signature of a characteristic"** (O2) — **fails this test**: defilement (#29–32, a *condition*) seats at ~17%, *above* #27's ~16% and well above #20's ~10%. Interior density does **not** track the characteristic↔condition line; it tracks individual lemmas. The characteristic/condition split is therefore **the action/status `type` tag relabelled into an ontology**, with one genuine exception (defilement's non-moral valence proves "state" is real for *that* family).

---

## §D. LEXICAL-GAP list (claims that needed the root verse → lexical defect for that occurrence)

| Claim | Field that was empty/insufficient | Note |
|---|---|---|
| #11/#12 "the state all stand under / enslaving power" (Rom 5–8) | `object` = "blood/Jeroboam/offering/people"; **no field carries "bondage/under-sin"** | The Pauline condition register is in the *verse text*, not the lexical. `how` empty 95/432. → the operative predicate is a lexical gap. |
| #27 generative arc "conceive→pregnant→birth" (Psa 7:14; Job 15:35; Isa 59:4) | `how` empty 76/101-class; the gestation predicate is in verse text/sense only | The strongest characteristic evidence is a **verse-text metaphor**, not a lexical field — logged as a gap. |
| #24 "the heart's default output / treasury" (Mat 12:34-35) | `object_type` empty 68/78; `object` empty 58/78 | The constitutional claim has no per-verse object support; needs the root verse. |
| #21 cha.val "my spirit is broken" (Job 17:1) inner-state | sense="broken" but **lemma_meaning mis-glossed ("to bind"→"to destroy")** | Confirmed mis-gloss in the lexical (re-gloss candidate); the inner-state sense is not recoverable from the (defective) lemma fields. |
| #21 2 Cor 11:3 "thoughts led astray" (noēma) | occurrence **absent from the 1,904-verse corpus** | Coverage gap already flagged in the unit's §A3; cannot be validated from the lexical. |

**General gap:** `how` is empty on a majority of occurrences in every unit (#11-12 95/432, #20 76/101, #21 42/64, #24 31/78, #29-32 140/226). All "how sin operates" / "lifecycle / operation" claims (Obs-07 O3) therefore rest mostly on **absent data + verse text**, not the lexical — consistent with the framework's §2 prediction.

---

## §E. Imported-meaning rate

- **Kind-level claims (6 units):** 5/6 carry the object-kind primarily on a lemma-constant (`type`/`faculty`) → **≈83% imported**. Only defilement's "non-moral state" is per-verse-grounded.
- **The characteristic↔condition *distinction* itself:** **IMPOSED** — no legit per-verse field separates the two kinds (§C); the separator is the excluded `type` tag.
- **Sub-claims audited as TERM-CONSTANT:** Obs-07 O1 (faculty-in-operation), O2 (seatedness = signature — also contradicted by §C), the per-term "faculty" rest of #20/#21/#24; Obs-04 O1 (type=status reading).
- This ≈83% is the **expected order of magnitude** given the framework's §2 (faculty 0% per-verse, type 14% per-verse) and matches the pilot's 6/7. A lower rate would have triggered re-scrutiny.

---

## §F. What survives (genuinely per-verse, keep)

1. **Defilement is a non-moral durative state** — `valence` varies within-lemma (H2931 neutral 31/sinful 16; H5079 neutral 8/sinful 7) and the object "until evening" marks duration. This is real and is the **one solid leg** of the CONDITION kind (Obs-04 O5 confirmed).
2. **#27 a.ven has a genuine per-verse type split** (status 46 / action 16) and the densest interior co-seating (lev/levav/nephesh ~13×) — so *if* any unit is "operative", it is this one, but ground it on type-variation + co-seating, **not** "faculty".
3. **#20 is relational, object=the Lord (36×)** — a real per-verse pattern, but it points to M13/M31 (faithfulness), *contradicting* its placement as an inner-being characteristic.
4. **Co-seatedness** (which other terms appear: lev, nephesh, nous, kardia) is legit per-verse and is the honest interior signal — distinct from the (invalid) faculty tag.

## §G — Bias-guard on this validation
- I am Claude and carry the harvest-to-fit reflex. Guards applied: induction-first per unit; null default; faculty/type **mechanically excluded** as per-verse evidence; verdicts checked against the mechanical aggregates (`_tmp_m10_charcond_validate.py`), not narrative; the cross-kind test (§C) was the explicit attempt to *find* a per-verse discriminator and report honestly that none holds across the line.
- **Caveat against over-correction:** the result is **not** "the kinds are meaningless." `type` (action vs status) is a real linguistic property of the lemma; the error is **promoting a lemma tag to a per-verse object-kind ontology** and claiming the verses earn it. Defilement shows a kind *can* be earned per-verse. The corrected stance: object-kinds must be **re-derived from sense/object/object_type/experiencer/valence**, and where they reduce to `type`, labelled as a lemma classification, not a verse reading.
- **Single point of trust:** the lexical itself is the evidence base; the one confirmed lexical defect surfaced here is **cha.val's mis-gloss** (#21), already a re-gloss candidate.

*Validation: the M10 CHARACTERISTIC vs CONDITION distinction is a `type`-tag (action↔status) relabel, not a per-verse object-kind — ~83% imported; no legit per-verse field separates the two kinds (defilement, a "condition", out-seats faithlessness, a "characteristic"). Defilement's non-moral valence is the one per-verse-grounded leg; #27's type-variation is the best characteristic foothold. faculty-in-operation and seatedness-as-signature are TERM-CONSTANT/contradicted.*
