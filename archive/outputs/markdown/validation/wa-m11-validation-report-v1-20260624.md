# M11 cold-read validation — claims × verdicts against the lexical

- **File:** wa-m11-validation-report-v1-20260624.md · **v1 · 2026-06-24 · Author:** Claude Code.
- **Mandate:** revalidate all M11 (Repentance/Forgiveness/Restoration) analysis against the **lexical** evidence base, hunting the AI reflex to *get a concept then make the evidence fit it*. Method + trusted-base rules: `wa-m10-m11-coldread-validation-framework-and-foundation-v1-20260624.md` (§1 method, §2 per-verse-vs-constant split, §3 verdict codes).
- **Evidence base:** `Sessions-v2/M11-Repentance/Data/wa-ve-lexical-extract-M11-20260623.json` (275 verses, 792 occurrences, 15 focus lemmas). Validation is **against the lexical fields only**; where a claim can only be settled by reading verse_text, that is logged as a **LEXICAL-GAP** (the field that should carry it is empty).
- **Claims sourced from** (read for the claims, not their justifications): `wa-m11-cluster-synthesis-v1-20260623.md` (§2–§4, §6), the 5 unit files `wa-m11-unit-01…05`, and `wa-m11-unit-04-repentance-tieranalysis-v1_0`.

## §A. Mechanical baseline (computed first, before judging any claim)

Per-unit field distributions over **focus occurrences** (the unit's own defined lemmas):

| Unit (focus lemmas) | n | type | faculty | the legit per-verse fields (object_type) |
|---|---|---|---|---|
| **#1 Atonement** kip.per H3722A | 81 | **action 81/81** | **none 81/81** | person 53 · abstract 10 · none 11 · thing/situation/God 7 |
| **#2 Forgiveness** sa.lach/sal.lach/se.li.chah | 49 | action 45 · status 3 · quality 1 | **none 49/49** | none 22 · abstract 15 · person 11 · God 1 |
| **#3 Release** afesis/afiēmi×3/exaleifō/apobolē | 108 | action 91 · status 17 | **none 108/108** | none 60 · abstract 20 · person 17 · thing 9 · spiritual-being 2 |
| **#4 Repentance** na.cham/shuv/ud | 42 | **action 42/42** | affect 34 · (memory,volition) 7 · none 1 | situation 25 · abstract 8 · none 6 · person 2 · God 1 |
| **#5 Reconciliation** katallassō/apokatallassō | 8 | **action 8/8** | **none 8/8** | none 3 · person 3 · God 2 |

**Mechanical consequences (confirming framework §2, now on M11 focus lemmas):**
- **`type` is unit-constant** for the lemmas that carry the unit's identity claims: #1 action 100%, #4 action 100%, #5 action 100%. Any object-kind keyed to `type` is a **relabel of a fixed tag**, not a verse reading.
- **`faculty` = none** for #1, #2, #3, #5 (the four "non-characteristic" units) and **affect/memory/volition is lemma-fixed** for #4 (na.cham = affect on all 34; shuv = memory+volition on all 7). Every "faculty-seated" claim that varies *per verse* is invalid; the faculty tag is a lemma constant.
- **`how` coverage is near-zero on the units making operational claims:** #1 = 0/81, #4 = 0/42, #5 = 0/8, #2 = 2/49, #3 = 6/108. Operational/"how it works" claims rest on absent data.
- **Legit per-verse evidence = `sense · object · object_type · experiencer` (+valence).** All object-kind verdicts below are re-derived from these.

## §B. Claims × verdicts × evidence

| # | Claim (source) | Per-verse lexical evidence (induced) | Verdict | Corrected inductive reading |
|---|---|---|---|---|
| 1 | **na.cham = BILATERAL characteristic, "God repents too"** (synthesis §2★, unit-04 T0.1.2) | na.cham obj = **disaster 10 · calamity 2 · war/fierce 1 · good 1 · blessing 1**; object_type = **situation 23/34**; sense = relent/relented 23×, regret 4×; divine_involvement=agent 24. **Object=sin only at Jer 8:6 — and that is the human "no man relents of his *evil*" (absence case).** | **CONTRADICTED (the "repents of sin" framing)** / SUPPORTED (the bare "God relents" fact) | God's na.cham relents **of/from disaster (planned punishment)** — obj=situation, never sin. "God repents *too*" smuggles in a symmetry with human repentance-from-sin that the object field denies. The divine act is *relenting from judgment*; calling it the divine half of "repentance" (turning from sin) is the imposition. |
| 2 | **#4 is a CHARACTERISTIC, faculty-seated in the heart** (unit-04 §A, T2.1, "heart 9×") | faculty is a **lemma-constant** (na.cham=affect all 34; shuv=memory+volition all 7) — §2. "heart 9×" = **co-seated co-terms** (lev/levav present in the verse), which IS legit per-verse — but the *faculty tag* on na.cham/shuv does not vary and is not verse-evidence of seating. | **TERM-CONSTANT** (the faculty claim) / partially SUPPORTED (co-seatedness) | The action-typing + co-occurring heart-terms are real per-verse signals that #4 behaves like a characteristic. But "faculty=affect/volition, heart-seated" reads a fixed lemma tag as a per-verse finding. Keep the co-seatedness (lev co-occurs); drop the faculty-tag-as-evidence. |
| 3 | **#4 human-turn vs divine-relent split is grounded per-verse** (unit-04 ★, T1.4.2) | experiencer self 13 / other 20 / addressed 4 — **does vary per verse** (legit). divine_involvement agent 24 / none 9 — varies. So the *two-experiencer* split is real in the data. | **SUPPORTED** | The experiencer/divine-role split is genuine per-verse evidence; the human-vs-divine distinction stands. (It is the **label "bilateral *repentance*"** that overreaches — see #1: the divine side is relenting-from-disaster, not repenting.) |
| 4 | **§10 object-kind #1 atonement = REMEDY/mechanism** (synthesis §10; unit-01) | type=action 81/81 (**constant**); object_type=person 53 (the one atoned-*for*), abstract 10 (the sin); sense = "make atonement" 45. | **TERM-CONSTANT / OVERREACH** | "Atonement *does* something to a sin-object" is the lemma meaning (action verb, "to cover/purge"), not a verse finding. The per-verse evidence (object=person/sin) supports "an act performed for a person regarding sin" — fine — but the REMEDY *kind* is read off `type=action`, which never varies. Relabel, lightly grounded. |
| 5 | **#2 forgiveness = act (REMEDY) + state (being-pardoned)** (synthesis §10 "#2"; unit-02) | type=action 45 · **status 3 · quality 1**. The status/quality occurrences (se.li.chah Psa 130:4; sal.lach Psa 86:5) **do vary from the action norm per occurrence**. object=sin 6/iniquity 4 (what is pardoned) vs person 11 (who). | **SUPPORTED (narrowly)** | Unlike #5, here `type` genuinely varies (3 status + 1 quality among 49) — so the "act + state" duality is carried by real per-verse type variation on distinct lemmas (verb vs abstract noun vs adjective). This is the one bilateral claim earned by the data. |
| 6 | **#3 release = "blot the record" (exaleifō) + "free the condition" (afesis)** (synthesis §10 #3, §4 row-1; unit-03) | exaleifō: obj=**record only at Col 2:14** ("canceling" a debt-certificate); Act 3:19/Rev 7:17/Rev 21:4 carry **no "record" object**. afesis: **type=status 16/16** → the CONDITION/state face is lexically real (status noun). | **#3-afesis SUPPORTED · #3-"blot the record" OVERREACH** | afesis-as-condition is well grounded (status 16/16). But "blot **the record**" generalises a single Col 2:14 ("canceling the record of debt") across the exaleifō set; the other 3 are "wipe away [tears]" / unspecified. Record-narrowing on 1 of 4. |
| 7 | **#5 reconciliation = positive STATE / "9th object-kind"** (synthesis §2,§6; unit-05 ★ candidate-new-kind) | focus lemmas katallassō/apokatallassō = **type=action 8/8** (constant), sense=reconcile/reconciled. The **STATE** is carried only by the **co-term katallagē G2643 (type=status, tagged M05)** — *not* in the unit's focus set. | **OVERREACH / TERM-CONSTANT** | The unit's own terms are an **act** (action 8/8). The "state/9th kind" is read off a co-term (katallagē) that is filed under M05, not M11. The verb is relabelled a "state" to fill a wanted positive-outcome category. The all-positive valence (5 righteous/2 commanded) is real and notable — but "positive *state*" is not what the focus lemmas say. |
| 8 | **§4 pole-pair: M10 #13 "record (written/engraved, Jer 17:1)" ↔ M11 #3 "blot out (exaleifō; Isa 43:25)"** (synthesis §4) | **Isa 43:25 is not in the M11 extract at all** (it is Hebrew machah, outside this Greek-release corpus). exaleifō-with-record = Col 2:14 only. The two poles share **no lexical link**; the pairing is a cross-verse construction. | **IMPOSED + LEXICAL-GAP** | A constructed cross-verse synthesis. The cited inverse-verse (Isa 43:25) is absent from the evidence base, so the pole-pair cannot be settled against the lexical — and where checkable (exaleifō) the "record" object appears once. Same verdict as pilot rows 2–3. |
| 9 | **§3 resolution SEQUENCE: human turn (shuv) → divine relent (na.cham) → atonement/forgiveness → reconciliation** (synthesis §3; unit-04 T6.2) | The M11 **focus shuv (H7725N)** is the **memory/recall** lemma — sense = lay/call/turn-to-**mind**/**heart**/recall (Deu 4:39, Lam 3:21, Isa 46:8…), faculty=memory+volition. The moral "turn-from-sin" verb (H7725O) is **owned by M45, not in M11 focus**. Jer 18:8 / Jon 3:10 (the cited "if turn… I relent" hinges) contain **only na.cham (obj=disaster); no shuv term in the verse**. | **IMPOSED (the sequence as lexically chained)** | The causal chain is asserted across verses, but the "human turn" step rests on the **wrong shuv** (M11's is recall-to-mind) and the hinge verses lexically contain only the *relenting*, not the *turn*. The sequence is a theological narrative, not a per-verse-grounded chain. (na.cham→sparing is locally visible; the four-step order is constructed.) |
| 10 | **2Cor 5:19 "reconciliation = the non-reckoning of the sin-record"** (unit-05 ↔BOND; synthesis §4) | katallassō (M11) co-occurs with **logizomai "counting" (M26) + paraptōma "trespasses" (M10)** in the same verse — genuine co-occurrence. "record" is **not a field**; it is the synthesizer's gloss on logizomai. | **SUPPORTED (co-occurrence) / mild OVERREACH ("record")** | The verse really does pair reconciling with not-counting-trespasses (legit co-term evidence). Calling the trespass-count "the sin-**record**" imports the M10 #13 "record" frame; "not counting trespasses" is what the lexical carries. |
| 11 | **#1 atonement's constitutional locus is the ne.phesh (soul), "operates on the soul" (×5)** (unit-01 §A, #1609) | ne.phesh co-occurs in 5 kip.per verses (legit co-seatedness). But these are mostly the **"atonement money for your *lives*"** ransom verses (Exo 30:15-16) — ne.phesh="lives", not an inner-being seat being operated on. | **OVERREACH** | Co-occurrence of ne.phesh is real (5×); "atonement's constitutional operation **is on the nephesh**" over-reads a co-term (often meaning "life/person" in a ransom-count) into a seated mechanism. Keep "ne.phesh co-occurs in the ransom verses"; drop "operates on the soul." |
| 12 | **#3 is genuinely multi-kind / per-occurrence (afiēmi splits forgive/leave/permit, carries sinful+forbidden valence)** (unit-03) | valence on #3 = righteous 53 · neutral 18 · commanded 14 · **sinful 8 · forbidden 3** · none 12 — and these track the leave/permit senses (e.g. Mar 7:8 "leave the commandment" sinful; Mat 23:13 "not allow" sinful). valence/sense **vary per occurrence**. | **SUPPORTED** | The multi-sense, broad-valence character is carried by real per-verse variation (the only unit with sinful/forbidden). The per-occurrence discipline is correctly applied here. |

## §C. LEXICAL-GAP list (claim needed verse_text / a field was empty)

| Verse / claim | Field that should carry it but is empty/insufficient |
|---|---|
| **Isa 43:25** (synthesis §4 pole-pair, claim #8) | **Verse absent from the M11 extract entirely** — the inverse pole cannot be checked against the lexical. |
| na.cham "God repents of sin" reading (claim #1) | Where it might mean more than "relent from disaster" the only recourse is verse_text; the `object` field uniformly says disaster/situation → no lexical support, root-text not relied upon. |
| #1 atonement "how it covers/purges/bears" (operational mechanism, unit-01) | `how` = **0/81** — every operational claim about *how* atonement works rests on an empty field. |
| #4 repentance "how the turn operates" (unit-04 mechanism claims, T5.3) | `how` = **0/42**. |
| #5 reconciliation operational/"act produces state" mechanism (unit-05) | `how` = **0/8**; the STATE lives only in co-term katallagē (M05), not the focus lemmas. |
| "blot **the record**" generalisation (exaleifō, claim #6) | `object`=record present only at Col 2:14; absent on the other 3 exaleifō occurrences → narrowing not carried by the field. |

## §D. Imported-meaning rate

Counting verdicts that import or contradict (IMPOSED + CONTRADICTED + the imposition-side of OVERREACH/TERM-CONSTANT that exceed the evidence):

- **CONTRADICTED:** #1 (na.cham "repents of sin").
- **IMPOSED:** #8 (pole-pair, +LEXICAL-GAP), #9 (resolution sequence as lexical chain).
- **OVERREACH / TERM-CONSTANT (label exceeds the fixed tag / co-term):** #4 (atonement REMEDY off type), #6-blot-record, #7 (#5 "state" off a co-term), #11 (atonement "operates on soul"), #10-"record" (mild).
- **SUPPORTED (earned by per-verse variation):** #3 (experiencer split), #5 (#2 act+state via real type variation), #6-afesis-condition, #10 co-occurrence, #12 (#3 multi-kind).
- **TERM-CONSTANT (faculty claim):** #2.

**Imposed-or-contradicted (clear): 8 of 12 high-leverage claims** (#1, #2, #4, #6-record, #7, #8, #9, #11) read meaning the lexical does not carry — **≈ 0.67 (8/12)**, the same order as the pilot's 6/7. The imposition concentrates **entirely in the superstructure** (the §10 object-kind labels, the pole-pairs, the resolution sequence, the "9th kind", faculty/locus-seatedness) — **not** in the base sense-readings, which are sound.

> The four that survive (#3, #5-act+state, #6-afesis, #12) all share one trait: the claim rests on a field that **genuinely varies per occurrence** (experiencer, type-across-distinct-lemmas, valence). That is the mechanical signature of an earned claim — and the dividing line for the whole pass.

## §E. The pattern, stated plainly (what M11 got wrong)

1. **Object-kinds are read off `type`** — which is unit-constant (#1/#4/#5 = action 100%). "REMEDY = action", "atonement does-something" = the lemma definition relabelled, not a verse finding.
2. **The "9th kind / positive STATE" (#5)** is the clearest harvest-to-fit: the focus lemmas are an action 8/8; the wanted *state* was taken from a **co-term (katallagē) that the programme files under M05**. The category was wanted (a positive outcome the sin-cluster lacked), so a co-term was promoted to fill it.
3. **na.cham "God repents too"** forces a human↔divine symmetry the `object` field refuses: divine na.cham relents **from disaster**, never from sin.
4. **The pole-pairs and resolution sequence** are cross-verse theological constructions; one cited anchor (Isa 43:25) is not even in the corpus, and the "human turn" step uses the wrong shuv (M11's is recall-to-mind; the moral turn is M45's).
5. **Faculty-seatedness** (#4 heart-seated, #1 soul-operated) conflates legitimate **co-seatedness** (co-terms present in the verse — keep) with the **faculty tag** (a lemma constant — drop), exactly the framework §2 distinction.

What is **sound**: the per-verse base readings (sense/object/object_type/experiencer), the #2 act+state duality (real type variation), the #3 multi-sense afiēmi (real valence variation), afesis-as-condition, and the experiencer-based human/divine *distinction* (just not its "repentance" label).

## §F. Headline verdicts (for the return)

1. **na.cham "God repents too" → CONTRADICTED.** obj=disaster/situation 23/34, never sin; the divine act is *relenting from punishment*, not repenting.
2. **#5 reconciliation "positive STATE / 9th kind" → OVERREACH/TERM-CONSTANT.** Focus lemmas = action 8/8; the "state" is a co-term (katallagē) filed under M05, promoted to fill a wanted category.
3. **§4 M11↔M10 pole-pairs → IMPOSED + LEXICAL-GAP.** Constructed cross-verse synthesis; the cited inverse-verse (Isa 43:25) is absent from the evidence base.
4. **§3 resolution sequence (shuv→na.cham→atonement→reconciliation) → IMPOSED.** The "turn" step uses M11's *recall-to-mind* shuv (moral-turn shuv is M45's); the hinge verses contain only na.cham.
5. **#1 atonement = REMEDY/mechanism → TERM-CONSTANT/OVERREACH.** Read off type=action (constant) + the lemma gloss; "operates on the nephesh" over-reads a ransom co-term.
6. **#4 faculty-seatedness → TERM-CONSTANT;** but the **human/divine experiencer split → SUPPORTED** (experiencer genuinely varies per verse).
7. **#2 forgiveness act + state → SUPPORTED** (the one earned bilateral claim — real type variation: action 45 / status 3 / quality 1).
8. **#3 release multi-kind + afesis-as-condition → SUPPORTED** (real per-verse valence variation; afesis type=status 16/16).

**Imported-meaning rate ≈ 0.67 (8/12).** Imposition is entirely in the object-kind/pole-pair/sequence/seatedness superstructure; the base sense-readings hold.

## §G — Bias-guard on this validation
- The validator is Claude and carries the same get-a-concept-then-fit reflex. Guards applied: (a) the mechanical per-unit distributions in §A were computed **before** judging any claim; (b) null-default — each claim was IMPOSED until a *per-verse-varying* field earned SUPPORTED; (c) faculty/type/lemma_meaning excluded as evidence by rule (§2); (d) the goal was to **find** imposition — a low rate would itself be suspect. The four SUPPORTED verdicts were each checked to rest on a field that varies per occurrence (experiencer/type-across-lemmas/valence), not on a constant.
- A "passing" pass would be the failure mode here. The 8/12 rate matches the pilot's order of magnitude and is consistent with framework §2's mechanical prediction (object-kinds keyed to constant tags will read as imposition).
- **Remediation deferred** per the framework — this pass surfaces the extent; it does not rewrite the units.

*M11 validation — base sense-readings sound; the §10 object-kind superstructure (REMEDY/STATE/9th-kind), the M10 pole-pairs, the resolution sequence, na.cham bilaterality, and faculty/locus-seatedness largely import meaning the lexical does not carry. Imported-meaning rate ≈ 0.67.*
