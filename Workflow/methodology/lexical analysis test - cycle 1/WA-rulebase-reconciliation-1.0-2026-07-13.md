# WA — Reconciliation of Session Findings against the Authoritative Rule Base

**File:** WA-rulebase-reconciliation-1.0-2026-07-13.md
**Date:** 2026-07-13
**Version:** 1.0
**Author:** le Roux Cilliers

**Instruction documents read in full:**
- `wa-characteristic-role-lexical-cycle-authoritative-v1-20260708.md` (262 lines, incl. §3 the 16 dimensions, §3A P0–P8, §5 the read, §7D v3 meaning-keyed index, §11 the non-negotiables)
- `wa-verse-analysis-method-v1-20260702.md` (165 lines, incl. §6 storage, §12 the two gates, §13 sanity check + role, **§14 the poetic chapter-driven method**)
- `wa-book-lexical-readiness-assessment-AUTHORITATIVE-v1-20260712.md` (read in context)

**Reconciles:** `WA-assess-raw-source-json-1.1`, `WA-projection-spec-1.2`, `WA-explore-E4-direction-target-prelim-1.0`, `WA-explore-inner-seat-heart-soul-spirit-1.0`, `WA-session-log-corpus-and-E1-1.1`.

---

## 0. The researcher's point, and what it costs me

> *"the from / to span is the direction, and the position in the pair is significant. Perhaps the biggest shortcoming was to provide you with the absolute rule base for the 16 lexical dimensions."*

Correct on both counts. Working from the emitted artefact without the rule base, I made **four claims that the rule base now falsifies or materially changes**, and it **sharpens two that survive**. Every one of them is set out below. I would rather this be a long list than a short one.

---

## 1. WITHDRAWN — "`direction` is never populated"

**What I said:** *"`direction` exists as a field and is null in all 176 rows… E4 just found direction may be the constitutive edge. Nothing is in it."*

**What the rule base says.** §3 of the cycle: *a dimension value is a **VALUE**, a **PAIR** (`from_span → to_span`, with `resolution`), an **EVENT**, or a **FLAG**.* §6 of the method: `ve_lexical` carries pair columns `from_span/to_span/direction/resolution/pair_kind`. §5 step 2: *wherever a dimension's value is another span in the verse, store it as a pair (`from_span → to_span`); that span is now a member of this characteristic's lexical.*

**The pair *is* the directed edge. The direction is carried by the ordering of the pair, and the position in the pair is significant.** A separate `direction` scalar is not where direction lives, and its being null is not the defect I called it.

**This is the single most important thing I got wrong,** because it means the model **already has** the edge that E4's preliminary identified as possibly constitutive. It is not missing. It is structural, and it has been from the start.

**What survives, in a much narrower form.** In the emitted JSON the pairs are **half-present**: `to_span` populated on **49 of 176** rows, `from_span` on **4**. I cannot tell from the file alone whether `from_span` is implicitly the characteristic's own span (in which case the pair is complete and only its near endpoint is elided), or whether the near endpoint is genuinely absent. **That is a question about the emission, not a defect in the model, and I am putting it as a question:** *is `from_span` implicit (= the char span) in the emission, or is it missing?* Either way, an artefact that shows one endpoint of a directed pair cannot be read as a directed pair by anyone who does not already know the rule.

---

## 2. WITHDRAWN — "`source`, `intensity`, `effect` were never recorded — the declared silence is unsupported"

This was my sharpest claim of the session, and the rule base **splits it in three**.

### 2.1 `source` (103) and `effect` (111) — **deliberately OFF for poetic genre.** My claim withdrawn.

Method §14, on the poetic chapter-driven method: *"Each verse of the chapter is built on its **own spans only** — no adjacent-verse load, **cross-verse items OFF** (source-across-verses / effect / process would be noise between poetic lines)."*

And §3 of the method: cross-verse items (source D2, effect D8, process D7) are **ON for prose, OFF for poetic/wisdom**, because *"consecutive verses are independent, so cross-verse items would be noise."*

**So `source: ABSENT` and `effect: ABSENT` across all 16 Psalms readings is not a gap. It is the method working as designed.** I called it "absence of reading." It is a deliberate, reasoned, documented methodological decision, and I had no business calling it a defect.

### 2.2 `intensity` (109), `prohibition` (113), `specifier` (110) — **the gap is real.** Claim stands.

Method §14 lists exactly what stays ON for poetic: *"Within-verse items stay on (sense, type, operation, seat, bearer, target, manner, coupling, **intensity**, **prohibition**)."* And `specifier` (ve_nr 110, construct-chain) was added in method v1.1.

**All three are `present: false` in all 16 readings.** They are supposed to be on. They are not there.

Cross-checked against the cycle's own rules: §3A **P4** requires *three states per dimension* — **resolved · none/silent · unresolved** — and states *"Silence ≠ unresolved."* §7C(c) requires the read to write *"16-dimension rows (`ve_nr` 101–116) for each characteristic."* The convention is visible in the data: `seat` writes a **row** with `value: "none"` when silent. So a dimension with **no row at all** is in none of the three permitted states. It is a fourth state that the model does not admit.

### 2.3 The consequence for E1 — and it is worse than I first said

E1's headline: every one of the 167 `inner-seat` narratives closes with *"the psalm does not tell us how strong it was, or how it finally turned out."*

- **"how strong"** = `intensity`. Should have been read (§14). **Was not.** The narrative asserts a silence that was never tested. **My finding stands.**
- **"how it finally turned out"** = `effect`. **Deliberately not read, by design, for poetic genre.** The narrative therefore reports a **methodological decision as though it were a property of the text.**

That second one is the more serious of the two. It is not that the reader looked and found nothing; it is that the method — for good reasons — declined to look, and the narrative layer then told the reader that *Scripture is silent*. **A design decision has been laundered into a finding.**

**Recommendation:** the narrative template must stop asserting silence on `effect` for poetic books. Either it says nothing about outcome, or it says *"outcome is not within the scope of the poetic read"* — which is true, and useful, and honest.

---

## 3. WITHDRAWN — "`type` (102) may be a faculty bin under another name"

Cycle §3: *`101 sense · 102 type` | value | ✅ **derivable** (sub-gloss; POS)*. `type` is a morphology-derived value, not an imposed ontology. The observed vocabulary (`volition`, `disposition`, `action`, `status`) is consistent with that. **The retired-faculty-field concern was unfounded.**

---

## 4. WITHDRAWN — the `H2603` split, restated properly

I withdrew the "gloss fragmentation" charge already. The rule base now explains it fully, and it is a **considered decision, investigated and documented**, not an accident.

Cycle **§7D v3 (2026-07-11) — MEANING-KEYED, not lemma-keyed:**
- Lemma-keying **merges distinct meanings** (halal → praise + boast + deride; gur → sojourn + strife).
- **Stem alone is insufficient** — one form can carry two senses.
- The read-sense (`ve_nr 101`) is a *contextual phrase*, so it **over-splits**.
- Therefore: *"the true meaning-in-context is carried by the **ESV rendering**, cross-checked by stem/morph/attested-gloss."* `char_key = "{lemma}:{normalised_esv}"`.
- And explicitly — *"**Never in the key:** … the bare lemma (it merges meanings)."*

So the ESV rendering is a **validated proxy for meaning-in-context**, adopted *after* lemma-keying and stem-keying were tried and found wanting. The evidence for the split — `stems`, `morph_codes`, `esv_words`, `lexical_gloss`, `read_sense_variants` — is **mandatory in `ib_characteristic`** (§7D: *"Evidence columns (mandatory, so any grouping is auditable and no bad merge is hidden)"*).

**The fix is therefore narrower and more precise than I framed it.** The evidence columns **already exist by mandate**. They are simply **not emitted in the family JSON**. Carry them. Nothing new needs deriving.

---

## 5. SHARPENED — `discovery` (114) is not doing its job, and the rule base makes that unambiguous

I flagged this as "possibly repurposed." The rule base makes it a clear finding.

Cycle §3A **P8 — Discovery-lookout is mandatory:** *"Every read runs: 'what does this verse state or imply about the inner being that the current dimensions do NOT capture?' A verse with nothing to flag records **discovery: none** (so we know it was looked for, not skipped)."*

**In the file: `discovery` is populated 16 of 16, and `discovery: none` appears zero times.** The content is the verse quotation plus a gloss — e.g. *"v14: 'and have PITY (chanan) on her dust' — the tender regard of the servants for ruined Zion…"*. That is a **sense/seed**, not a lookout.

Either the lookout genuinely found an uncaptured inner-being phenomenon on **every single reading** (implausible), or **the field is being used for something else and the emergence engine is not running.** P8 calls it *"the emergence engine."* If it is not running, the mechanism by which new dimensions are discovered and back-propagated (§7 feedback) is dark.

**This is now my highest-priority referral candidate**, above everything else in this document.

---

## 6. CONFIRMED and strengthened — `seat: "none"` is a genuine reader determination

Cycle §3: `104 seat` is *"✅ derivable (construct…)"* — mechanically derivable from morphology. §3A **P4**: `none/silent` = *"the verse says nothing about it → **never impute**"*, and is a **distinct state from `unresolved`**.

`seat` = `"none"`, `resolution: "none"` on **16 of 16**. That is the model's explicit "looked for, found nothing" state, correctly recorded.

**E1's headline finding — that the corpus systematically declines to localise the inner movement in a part of the person — is confirmed at source and confirmed against the rule base.** It is a recorded determination in the model's own vocabulary, not a template artefact. It remains the strongest finding of the session and it now has a rule-based warrant.

---

## 7. Corrected understanding — things I had misread as observations that are actually tautologies

- **`role: characteristic` on all 16.** Cycle §11 rule 6: *"**Only characteristics get their own lexical.**"* Of course every `ve_lexical` row is on a characteristic. This was never an observation.
- **"Relational words are missing / no object-kind field."** Cycle §11 rule 3: *"Relational words (object/source/seat/manner) are **qualifiers** — and are **captured, never dropped**."* §6: the qualifier *"exists only inside the characteristic it serves, as the span on the far side of a dimension pair."* **The object of a movement is the far endpoint of the pair.** My proposed `object_kind` column is not adding a missing concept — at most it is asking for the *kind* of that endpoint to be typed, which §5 step 2 already calls for (*"target with object-type"*). **Check whether object-type is being recorded before asking for a new column.**

---

## 8. What E4 becomes in light of this

E4's preliminary read the narratives and concluded that **direction may be the edge that constitutes the movement** — that seeking-God and seeking-a-life-to-kill are not one movement with two settings, but two movements sharing a verb.

**The rule base says the model already agrees.** Direction is not an afterthought in this design; it is the pair, and *"the position in the pair is significant."* Every relational dimension is a directed edge from the characteristic's span to a qualifier span.

**So E4 stops being a proposal and becomes a validation.** The question is no longer *"should direction be recorded?"* — it is recorded, structurally. The question is:

> **Does the recorded pair structure, read across the corpus, bear out what the narratives assert about direction?**

That is answerable from the `ve_lexical` pairs, mechanically, with no prose reading at all — **provided both pair endpoints are emitted.** Which returns to §1: `from_span` on 4 of 176 rows.

**Nothing else in E4 needs to change.** The adversarial test I proposed (`faint-despair-languishing`, `shame-confusion`, `rest-stillness-peace` — movements that look like states, not acts) is still exactly the right test, and it is now testable against the pairs rather than argued from prose.

---

## 9. Revised asks — replacing everything in `WA-projection-spec-1.2` §4

Not new fields. **Emit what the model already holds.**

| # | Ask | Warrant |
|---|---|---|
| 1 | **Emit both pair endpoints** — `from_span` **and** `to_span`, plus `pair_kind` and `resolution`. If `from_span` is implicit (= the char span), say so; do not leave it to be inferred. | §3, §5 step 2, §6 of method — the pair is the directed edge, and position is significant. |
| 2 | **Emit `verse_ref`, not `passage_ref`.** | Already in the data. Free. |
| 3 | **Emit the evidence columns already mandatory in `ib_characteristic`**: `stems`, `morph_codes`, `esv_words`, `lexical_gloss`, `read_sense_variants`, `key_span_id`. | §7D — *"mandatory, so any grouping is auditable and no bad merge is hidden."* Mandated; simply not emitted. |
| 4 | **Fix the `coupling` ↔ `locus` swap** (10 of 16 rows). | Data-quality fault; unaffected by the rule base. |
| 5 | **Write rows for `intensity`, `prohibition`, `specifier`** — with `none` where silent, per P4. | §14 has them ON for poetic; P4 requires an explicit state. |
| 6 | **Stop the narrative asserting silence on `effect`** for poetic books. | §14 — cross-verse items are deliberately OFF. This is a design decision, not a textual silence. |
| 7 | **Resolve `discovery` (114).** | P8 — the emergence engine. Zero `discovery: none` in 16 readings is the anomaly. |

---

## 10. The process lesson, and it is mine

Three times today I drew a structural conclusion from the emitted artefact without the rule that governs it — three generations (wrong), gloss fragmentation (wrong), direction-never-recorded (wrong). Each time the artefact *supported* my reading; each time the rule base did not.

The tendency is not carelessness about the data. It is **treating the emitted artefact as self-describing** — assuming that what is visible in the file is the whole of what the model holds. It is not, and in this programme it is systematically not: the verse is known but emitted as a range; the morphology is read but not carried; the pair is directed but only half-shown; the effect is deliberately unread but narrated as silence.

**Counter-discipline, stated so it can be enforced:** *before drawing any structural conclusion from an artefact, ask what governs its production, and read that first.* The researcher named this himself — *"perhaps the biggest shortcoming was to provide you with the absolute rule base"* — and it is generous of him to frame it as a supply problem. It is also mine: **I should have asked.**

---

## Change control

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-07-13 | First issue. Reconciles all session findings against the three authoritative instruction documents. **Withdraws four claims** (direction-never-recorded; source/effect never read; `type` as faculty bin; the framing of the H2603 split). **Confirms two** (`seat: none` as a genuine determination; `intensity`/`prohibition`/`specifier` genuinely missing). **Sharpens one** (`discovery` not running as the emergence engine). Recasts E4 from proposal to validation against the pair structure. |
