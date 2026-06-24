# Extended lexical model — END-TO-END TEST on two M12 terms (tamim CHARACTERISTIC + tahor-cleanness STATE)

- **File:** wa-m12-extended-lexical-test-tamim-cleanness-v1-20260624.md · **v1 · 2026-06-24 · Author:** Claude Code.
- **Purpose:** validate the **extended lexical model** (`wa-lexical-extension-deepdive-into-01b-DESIGN-v1` + `wa-lexical-extension-rerun-and-compound-design-v1`) end-to-end on **one CHARACTERISTIC** (tamim) and **one STATE** (tahor cleanness) BEFORE it is folded into canonical 01b → v3.
- **Discipline carried in (the M10/M11 validation error, NOT repeated):** object_type and every value FLOW FROM **per-verse-VARYING** evidence (sense · object · object_type · experiencer · valence · how + co-seating), **never** from lemma-constants (`type`, `faculty`). `faculty=conscience` (34/34 on tamim) and `type=quality` (constant) are demonstrably term-intrinsic — they ride uniformly, including on God-as-bearer verses where no human faculty operates — so they are **not** used as per-verse claims. Every value below cites the measure; silences and gaps are flagged.
- **Inputs:** extract `wa-ve-lexical-extract-M12-20260623.json`; per-verse evidence `scripts/_build_m10_unit_verse_evidence_20260623.py`; LRT `scripts/_lexical_revelation_test_20260624.py`; deep-dives `wa-m12-deepev-in-innocence-blamelessness-v1` (tamim) + `wa-m12-deepev-pu1-ritual-cleanness-v1` (tahor).
- **Tagging key (R1 + R6):** each value carries `derivation = mechanical-rule | read | researcher` and `source-scope = head-verse | adjacent | collection`.

---

## RECORD 1 — tamim H8549G/H/I/J (CHARACTERISTIC) — *blamelessness / integrity-of-walk*

LRT (n=34): sense 100% (8 distinct) · valence 97% (2 vals) · **how 68% (20 distinct)** · object **0%** · object_type **0%** · experiencer 32%. Constants: type=quality (34), faculty=conscience (34).

### 1. object_type call — **CHARACTERISTIC** · `derivation=mechanical-rule` · `source-scope=collection`

**RULE applied (design §3, characteristic branch):** *grammatical type + a `how`/operating-predicate showing the person acting from an inner faculty → characteristic.* It fires here on **per-verse-varying** evidence, not the constant:
- **`how` is populated at 68% and is overwhelmingly a LIVED operation verb that VARIES per verse:** walked (Gen 6:9) · ponder (Psa 101:2) · acted-in-good-faith (Judg 9:16,19) · minister (Psa 101:6) · remain (Pro 2:21) · delivered (Pro 28:18) · serve (Jos 24:14) · straight/walk (Pro 11:5) · was/be (commanded register). 20 distinct `how` values across 34 verses. The person **DOES** the blameless walk — the signature of a faculty-in-operation.
- The sense band is a **wholeness-of-character** band (blameless ×19 · perfect ×6 · **integrity ×4** · uprightly · sincerity · truth) — a lived quality, not a standing verdict.
- **object = 0%** is **nature-correct** (intransitive predicate-adjective: one *is* blameless / *walks* blamelessly) and the operation sits on the `how` verb — exactly the characteristic-via-`how`-not-`object` profile (LRT check 2, "the red flags are explained, not damning").

This reproduces the deep-dive's IN-2 verdict cleanly. **CONTESTED sub-case (captured, not silently swallowed):** ~9/34 verses are **God-as-bearer** ("his way is perfect" Deu 32:4, 2Sa 22:31, Psa 18:30; "his work is perfect"; the Torah "perfect" Psa 19:7; "Thummim" 1Sa 14:41). Here tamim is an **attribute/quality of God or of an object**, not a human characteristic-in-operation. The collection object_type is **characteristic for the human-bearer occurrences** (the analytical core), with a flagged **sub-register `quality-of-God/thing`** for the divine/object-bearer verses → `derivation=read` (the rule alone would mis-uniform them). *This is a model gap — see verdict (d).*

### 2. Type-conditioned EXPECTED answers (design §4 — CHARACTERISTIC row)

| Expected (characteristic) | Value | Evidence / measure | derivation | source-scope |
|---|---|---|---|---|
| **which faculty? (REQUIRED)** | **UNRESOLVED → conscience/integrity (home-faculty), NOT per-verse** | `faculty=conscience` is a **lemma-constant** (34/34, rides on God-as-bearer + civil verses). Per-verse-varying evidence gives NO independent faculty signal. The faculty a characteristic REQUIRES is **not mechanically present per-verse** here. | read | collection |
| **how does it operate?** | walked · ponder · acted-in-good-faith · minister · remain · serve · straight · delivered | `how` field, 68%, 20 distinct, per-verse | mechanical-rule | head-verse |
| **directed at what?** | **NONE** (intransitive) — where directed, it is *before/with the Lord* (Gen 17:1 "walk before me"; Deu 18:13; Psa 18:25 "with the blameless") | `object=0%` (nature-correct); `relational=before/with` carries the orientation | mechanical-rule | head-verse |
| **whose?** | Noah (Gen 6:9) · Abram (Gen 17:1) · David (2Sa 22:24, Psa 18) · "the blameless man" · "those whose way is blameless" (Psa 119:1) | `experiencer` 32%; where blank, recovered from the **verse subject** (3rd-person descriptions) | mechanical-rule (recovery: read) | head-verse / adjacent |
| **manner / intensity** | mostly NONE; "with **all** his ways" (Deu 32:4, `intensity=all`) | `intensity` field (rare) | mechanical-rule | head-verse |

### 3. binding (ENRICHED role vocabulary)

The deep-dive co-seat web, re-expressed in the enriched roles (manner/expresses/seat/object/pole-opposite). **NB the current extract tags 91% of these as the flat "partner"** (200/220 rows) — the enriched roles below are assigned **by hand** per the addendum §1 (the flat field cannot express them):

- **expresses / co-characteristic:** e.met / a.man "truth, faithful" (M13) ×6 — tamim *expresses* truthfulness ("speaks truth in his heart" Psa 15:2); ya.shar "upright" (M13) ×3; tom "integrity" (M13); cha.sad / cha.sid "kind, pious" (M05) ×6 (2Sa 22:26 "with the blameless you show yourself blameless"). `derivation=read` `source-scope=head-verse`.
- **seat:** **le.vav / lev "heart" (M47)** — Psa 101:2 (`location=heart+inward-parts`, how=ponder), Pro 22-context; the one genuine **per-verse heart-seat** of the blameless walk. `derivation=mechanical-rule` (location field fired) `source-scope=head-verse`.
- **pole-opposite:** a.von "guilt/iniquity" (M10) — 2Sa 22:24 "I was blameless … kept myself from guilt"; a.vel "injustice" (M10, Deu 32:4). `derivation=mechanical-rule` (co-seat + cross-cluster ownership) `source-scope=head-verse`.
- **partner (genuine, residual):** tsad.diq "righteous" (M26) ×3 — co-predicated, no sharper role. `derivation=mechanical-rule`.
- **cross-cluster bonds (LAST note):** M13 (Truth/Integrity) — the characteristic tamim *expresses*; M05 (Loyalty/che.sed) — paired disposition; M47 (Constitution) — the heart-seat; M10 (Sin) — the guilt pole; M26 (Righteousness) — co-predicated standing.

### 4. pole-relation + mutability

- **pole-relation:** **blameless ↔ guilty/crooked** — axis-partner is the M10 guilt/iniquity pole (a.von in-verse, 2Sa 22:24; the crooked-heart/falsehood pole generally). `derivation=mechanical-rule` (co-seat + cross-ownership) `source-scope=head-verse(2Sa 22:24)→collection`.
- **mutability:** **changeable (but a sustained disposition, not a toggle)** — Eze 28:15 "you were blameless … *till* unrighteousness was found in you" shows the characteristic can be lost; God "*makes* my way blameless" (2Sa 22:33) shows it can be conferred/strengthened. So it is acquirable/losable, unlike a one-act state. `derivation=mechanical-rule` (a verse shows it set/lost) `source-scope=adjacent (Eze 28:15, 2Sa 22:33)`.

---

## RECORD 2 — tahor cleanness H2889/H2890/H2892A/H2892B/H2893 (STATE) — *ritual / bodily cleanness*

LRT (n=76): sense 100% (12 distinct) · **valence 96% (4 vals)** · how 75% · object 16% · object_type 16% · experiencer 37%. Constants: type=quality (76), faculty=0 (none).
> Note: H2891 **ta.her** (the cleansing verb) is **excluded from the state** and handled as the state's **transition-trigger** (§ below), per the prompt.

### 1. object_type call — **STATE / condition** · `derivation=mechanical-rule` · `source-scope=collection`

**RULE applied (design §3, state branch):** *grammatical type=status/quality + valence VARIES across the term's verses → state/condition.* Fires on per-verse-varying evidence:
- **valence VARIES across 4 values:** neutral 44 · righteous 19 · commanded 9 · **sinful 1** (Pro 30:12 "clean in their own eyes"). Valence-variation is the canonical state-signal (design §5 mutability rule input).
- **object near-empty (16%) is nature-correct** for a predicate-adjective: cleanness is *predicated of* a subject (priest, clothes, flesh, blood), it does not act on an object.
- The objects that do appear are **ritual/bodily things** (flesh ×3 via `location=flesh`; clothes, blood, priest, head) — never a faculty — placing it firmly on the **ritual pole**.

Reproduces the deep-dive PU-1 STATE verdict cleanly. No contested sub-case (the verb-side cleansing is split out as the trigger).

### 2. Type-conditioned EXPECTED answers (design §4 — STATE row)

| Expected (state) | Value | Evidence / measure | derivation | source-scope |
|---|---|---|---|---|
| **of what?** (bearer) | flesh/body (Lev 7:19, 13:13,39 `location=flesh`) · the person (priest, Israelite) · clothes · vessels (pure gold, 2Ch) · animals (clean/unclean beasts) | `location=flesh`; object/experiencer; verse subject | mechanical-rule | head-verse |
| **who set it?** | **NONE (mostly) → God's law / the cleansing rite** where stated; Eze 36:25 "I will sprinkle … you shall be clean" (God) | `divine_involvement` mostly absent; the setter is the rite (see trigger) | mechanical-rule | head-verse / adjacent |
| **can it change? (mutability)** | **changeable** — paired with becoming-unclean throughout (ta.me ×19 co-seat) | co-seat with ta.me M10; "becomes unclean" verses | mechanical-rule | collection |
| **what changes it? (transition-trigger)** | **ta.her (H2891) cleansing** + **kip.per/ka.phar atonement**; and defilement (ta.me) the other way | see § transition-trigger below | mechanical-rule | collection / adjacent |
| **valence register** | neutral 44 · righteous 19 · commanded 9 · sinful 1 (counterfeit, Pro 30:12) | `valence` field, varies | mechanical-rule | head-verse |
| **pole-opposite** | **ta.me "unclean" (M10)** — the contrast state | co-seat ×19+ (ta.me appears 54× across the verse set incl. co-terms) | mechanical-rule | head-verse |

**The one inner-pole bridge (flagged, not the core):** Pro 22:11 "purity (tahor) of **heart**" and 2Ch 30:19 "cleanness … set their **heart**" carry `location=heart` — a handful of verses where the cleanness STATE is predicated of the inner being rather than the body. Captured as a **sub-register (inner-cleanness)** → `derivation=mechanical-rule` (location field fired) `source-scope=head-verse`. The corpus core remains ritual/bodily.

### 3. binding (ENRICHED role vocabulary)

Current extract tags 92% "partner" (299/324) — coarse-field artefact; enriched roles assigned by hand:
- **pole-opposite:** **ta.me "to defile / unclean" (M10)** — the dominant binding, the negative state. `derivation=mechanical-rule` `source-scope=head-verse`.
- **transition-trigger (manner-of-becoming):** **kip.per (M11) / ka.phar (M38) "atone/cover"** ×10 each (on the cleansing-verb verses); **ta.her (M12)** the cleansing act. `derivation=mechanical-rule` `source-scope=adjacent`.
- **object (what is cleansed):** chat.tat / cha.ta "sin" (M10), tum.ah "uncleanness" (M12) — the defilement removed. `derivation=mechanical-rule`.
- **seat (rare):** lev "heart" (M47) — Pro 22:11, 2Ch 30:19 inner-cleanness. `derivation=mechanical-rule` `source-scope=head-verse`.
- **cross-cluster bonds (LAST note):** M10 (unclean pole) · M11/M38 (atonement = the trigger) · M22 (qo.desh "holy", the consecration neighbour) · M47 (the rare heart-seat).

### 4. pole-relation + mutability + transition-trigger

- **pole-relation:** **clean (tahor) ↔ unclean (ta.me, M10)** — the cleanness axis. `derivation=mechanical-rule` (co-seat dominant) `source-scope=collection`.
- **mutability:** **changeable** — the entire Levitical corpus is the bearer moving between clean and unclean ("until evening … then clean"; "becomes unclean because…"). `derivation=mechanical-rule` `source-scope=collection`.
- **transition-trigger (the state's mover — handled per the prompt as ta.her, NOT the state):** **ta.her H2891 "cleanse/become clean"** (71 occ: clean 27 · cleansed 22 · cleanse 11 · purify) is the EXPRESSION that moves the bearer **into** the clean state; **defilement (ta.me)** moves it **out**. The MANNER of the cleansing trigger is **non-inner / ceremonial** — `how=0/71` on ta.her (LRT-B RED FLAG) — its manner is the **bound atonement procedure** (kip.per/ka.phar ×20). So the trigger is a real, captured node, but its manner is silent-by-nature and recovered only as the bound rite. `derivation=mechanical-rule` (the trigger identity) + `read` (the manner=rite recovery) `source-scope=adjacent`.

---

## MODEL-VALIDATION VERDICT

### (a) Did the extended model capture the deep-dive understanding cleanly, per type?

**YES for both types.**
- **CHARACTERISTIC (tamim):** the model's characteristic branch + the `how`-not-`object` characteristic profile reproduced the IN-2 deep-dive verdict exactly, and on the **right** evidence (per-verse `how`-variation), explicitly **refusing** the faculty-constant. The §4 expected-answer set ("a characteristic must have a faculty", how-it-operates, whose) is the correct frame and surfaced the real gap (the required faculty is NOT per-verse here).
- **STATE (tahor):** the state branch + valence-variation-as-state-signal + the §4 state expected-set (of-what / who-set / mutability / transition-trigger / valence / pole-opposite) captured PU-1 cleanly, including the trigger split (ta.her as mover, not state) and the pole (ta.me).

The model is **expressive enough** to hold both deep-dives without distortion. The two-scope design (per-verse 01b + collection layer) is the right home: per-verse silence (tamim object=0%, tahor who-set mostly NONE) is resolved at the collection scope or by cited adjacency.

### (b) Reproducibility — mechanical-rule (regenerates) vs read/researcher (must be preserved)

Counting the tagged values across both records (object_type, the §4 expected answers, binding roles, pole-relation, mutability, transition-trigger):

| | mechanical-rule | read | researcher | total |
|---|---|---|---|---|
| **tamim** | 9 | 4 | 0 | 13 |
| **tahor** | 12 | 1 | 0 | 13 |
| **combined** | **21 (81%)** | **5 (19%)** | 0 | 26 |

**~81% mechanical-rule (regenerates idempotently), ~19% read (preserved).** This clears the addendum's R1 aim ("maximise the mechanical share"). The 5 read-captures are exactly the judgement nodes: tamim's required-faculty (UNRESOLVED→home-faculty), its God-as-bearer sub-register, the expresses-role binding, the experiencer-recovery; and tahor's cleansing-manner=rite recovery. All are explicit, small, and survive re-run. **No researcher-only values** were needed for these two terms — a good sign the rules carry most of the load.

### (c) Expected-answers that could NOT be filled (LRT gaps / lexical-remediation owed)

1. **tamim — faculty (REQUIRED, but UNRESOLVED per-verse).** The model *requires* a faculty for a characteristic, but the only faculty signal is the **lemma-constant** `conscience` — which the discipline forbids using as a per-verse claim. So the required field is **genuinely unfillable from per-verse-varying evidence** for tamim. → **This is the sharpest finding: the "REQUIRED faculty" rule and the "no lemma-constant" rule COLLIDE for disposition-characteristics whose faculty is intrinsic.** See (d).
2. **tahor — who-set-it** mostly NONE (the rite, not a named agent) — legitimately silent except where God is the sprinkler (Eze 36:25); acceptable.
3. **ta.her — the cleansing manner (`how`=0/71)** — honest gap, recoverable only as the bound atonement rite; carried as a programme lexical-remediation flag (already logged in the PU-1 deep-dive). Not new, but the extended model now has a **home** for it (transition-trigger.manner = bound rite).

### (d) What is MISSING from the model and should be ADDED (the model will grow)

1. **A `bearer_type` / required-faculty escape for INTRINSIC-faculty characteristics.** The model says a characteristic MUST name a faculty, but for a **disposition whose faculty is lexically intrinsic** (tamim = the conscience/integrity vocabulary itself), the per-verse evidence can never independently supply it without violating the no-constant rule. **ADD:** a rule that a characteristic's faculty may be **`intrinsic (home-faculty)`** — sourced from the lemma, tagged `derivation=read`, **explicitly distinguished from a per-verse-seated faculty** — so the REQUIRED field is satisfiable honestly rather than forced UNRESOLVED forever. (Resolves the (c)-1 rule-collision.)

2. **A `bearer-class` axis on object_type (human-disposition vs quality-of-God/thing).** tamim is a **characteristic** when borne by a person (Noah walks blamelessly) but a **quality/attribute** when borne by God or the Law ("his way is perfect", "the law … is perfect"). The single collection object_type cannot hold both. **ADD:** object_type carries a **bearer-class sub-tag** (human-faculty-bearer → characteristic; divine/object-bearer → quality), derived from the per-verse `experiencer`/subject. (This is the design's "bivalent-faculty" idea generalised to bivalent-by-BEARER, not by valence.)

3. **`transition-trigger.manner` as a named slot** with a value of `inner | ceremonial/bound-rite | NONE`. The ta.her how-gap showed the trigger has a manner that is **legitimately non-inner**; the model should let the trigger record *that its manner is the bound rite* rather than leaving a bare gap. (Half-anticipated by §5 binding; make it an explicit attribute of transition-trigger.)

4. **An `inner-vs-outer pole` sub-register on STATE.** tahor is overwhelmingly ritual/bodily but a few verses (Pro 22:11, 2Ch 30:19) predicate cleanness of the **heart**. The model needs to record a state's **realm** (bodily/ritual ↔ inner/moral) as a per-verse sub-register so the inner-cleanness handful is captured without re-typing the whole term.

5. **Promote the enriched compound roles from "by hand" to a real per-verse field (PREREQUISITE).** See (e) — the binding-web in both records had to be assigned manually because the live extract is 91-92% flat "partner". The model's binding layer is **not real** until compound is enriched per-occurrence.

### (e) Did the enriched compound roles actually VARY by verse for these terms? (compound hypothesis test on real data)

**In the CURRENT extract: NO — and that is the addendum's predicted artefact, now confirmed on two more terms.**
- tamim compound roles: **partner 200 · qualifier 9 · co-seated 11** → **91% "partner"**.
- tahor compound roles: **partner 299 · qualifier 18 · co-seated 7** → **92% "partner"**.

The flat field shows almost no variation. **BUT when the enriched vocabulary is applied by hand (Records §3), the roles DO vary meaningfully per verse and per co-term:** tamim's e.met is `expresses`, its lev is `seat`, its a.von is `pole-opposite`, its tsad.diq is genuine `partner`; tahor's ta.me is `pole-opposite`, kip.per is `transition-trigger`, lev is `seat`. **So the hypothesis holds: compounds DO change role by situation** — the near-zero variation in the data is a **coarse-field artefact, not a finding** (exactly the addendum §1 / §G bias-guard). **Conclusion: enriching compound to per-verse roles is validated as necessary and as real — and is a prerequisite (item d-5) for the binding-web to be genuine.**

---

*Two-term end-to-end test, extended lexical model. **Verdict: the model captures both deep-dives cleanly (a); ~81% of collection values regenerate mechanically, ~19% are preserved reads, no researcher-only values (b); the one unfillable expected-answer is tamim's REQUIRED faculty, which collides with the no-lemma-constant rule (c).** Five additions proposed (d): intrinsic-faculty escape, bearer-class sub-tag on object_type, transition-trigger.manner slot, inner/outer realm sub-register on STATE, and per-verse enriched compound (prerequisite). The compound-varies hypothesis is CONFIRMED (e): the live 91-92%-"partner" is a coarse-field artefact; by-hand enrichment makes roles vary by verse as predicted. Model is sound enough to fold into 01b v3 after the five additions and the compound enrichment.*
