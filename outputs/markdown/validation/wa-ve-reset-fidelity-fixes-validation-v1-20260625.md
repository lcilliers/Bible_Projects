# VE reset — fidelity fixes baked into the engine: validation + 5 new verses for review

- **File:** wa-ve-reset-fidelity-fixes-validation-v1-20260625.md · **v1.1 · 2026-06-25 · Author:** Claude Code.
- **v1.1 update:** adds **§5 — increment 3** (the next mechanical-delta batch baked: possessive-object · intransitive-stative suppression · instrument/binding · purpose/telos · adjacency/isolable; transition deliberately **not** baked). Crash-tested over all 1,686 M12 units (0 errors). Decision: **build all mechanical deltas, then ONE sweep** (read-only validation per delta makes mid-sweeps wasteful).
- **What this is:** the researcher approved baking the pilot-review findings into the build. This records (1) **my assessment**, (2) the **before/after full lexical** for the six reviewed verses — validating the errors are corrected, (3) **5 new verses** for the next review pass. **Read-only** throughout (engine code changed; no DB write — the corpus sweep is a later, gated step).
- **Engine changed:** `scripts/_ve_engine_v2.py` `derive()` — a new **RESET FIXES** block + helpers (`tense_of`, `QUANT_SURF`, `SPEECH`, `H9006` added to `FROM_PREP`). Harness: `scripts/_read_ve_pilot_compare_20260625.py` (read-only before/after).

---

## 1. Assessment (short)

**The fixes work, and the review-before-sweep discipline paid off twice.** The first pass corrected the headline errors but introduced two *new* mis-fires (quality-bearer firing on a preposition "before"; operation grabbing the narrative speech-verb "said" instead of "walk"). A second tightening fixed both. **Had we swept blind, we'd have written the bare-quantifier bug corpus-wide *and* these two new ones.** That is the whole case for (b).

What is now **baked in** (all six reviewed errors corrected — §2):

| Delta | Fix | Validated on |
|---|---|---|
| **object-fidelity** | a bare **quantifier** object ("all") → advance to the **head noun** | Eze 36:25 *all→uncleannesses* |
| **from-source** | the noun governed by a **"from"** prep — incl. the Hebrew `min`-prefix `H9006` (was missed) | Eze 36:25 *idols+uncleannesses*; Heb 9:14 *works* |
| **tense fidelity** | annotate captured effect/response/cause verbs with **morph tense** (never flatten) | Mat 5:8 *they see God **[future]*** |
| **quality-bearer** | for an adjective, the **immediately-adjacent** noun it describes (skip prep-nouns) | Psa 24:4 *hands*; Mat 5:8 *heart* |
| **operation** | the **lived-conduct verb** when a quality is asserted with a copula — **imperative preferred**, speech/negated verbs skipped | Gen 17:1 *be blameless → **walk*** |

**Residuals (known, bounded — not yet fixed):**
- **Intransitive-stative object:** Eze 36:25 *ta.her* ("be clean **from** X") still emits `object=uncleannesses` — for a stative there is no object; it is from-source. The bare-quantifier bug is gone, but object shouldn't fire on an intransitive stative. *(Deeper refinement; flagged.)*
- **Possessive-pronoun object (NEW, from the 5-new set):** Pro 20:9 *"made my heart pure"* → `object=my` (the possessive), not **heart**. This is the **same class** as the quantifier bug — object-fidelity should also skip a bare possessive/pronoun and take the head noun. **Recommend baking the same way** (low-risk, mechanical) — surfaced here for your sign-off rather than auto-applied.

**Shape verdict unchanged:** the substrate is right; these are edge-fidelity fixes, not a redesign. And the inner-being payoff is visible — the from-source now disambiguates realm (cleansed *from idols/iniquity/sin* = moral, not physical), and a real **cross-verse movement** has emerged from the new set (see §3: *self cannot* → *God creates/cleanses*).

---

## 2. Before / after — the six reviewed verses (validation)

> `BEFORE` = the rows currently in `ve_lexical`; `AFTER` = the patched `derive()`. Only the changed/added fields shown.

### Psa 24:4 — "clean hands and a pure heart …" (na.qi)
- **BEFORE:** no quality-bearer; `immediate-response = lift up soul`; "clean hands" only as a weak qualifier-compound.
- **AFTER:** `quality-bearer = hands` ◀ ; `immediate-response = lift up soul [perfect]` ◀tense. *(operation correctly does **not** fire — the only verbs are the negated pole "(not) lift up / (not) swear".)*

### Mat 5:8 — "the pure in heart … they shall see God" (katharos)
- **BEFORE:** `cause_clause = they see God` (tense flattened); no quality-bearer.
- **AFTER:** `cause_clause = they see God [future]` ◀tense ; `quality-bearer = heart` ◀ ; object=God retained.

### Eze 36:25 — "clean water … from all your idols I will cleanse you" (tum.ah / ta.hor / ta.her)
- **BEFORE:** `object = all` (ta.her); **no from-source** anywhere; `immediate-response = cleanse`.
- **AFTER:** `object = uncleannesses` (was "all") ◀ ; `from-source = uncleannesses | idols` on all three terms ◀ ; `quality-bearer = water` (ta.hor) ◀ ; `immediate-response = cleanse [perfect]` ◀tense. *(residual: ta.her is intransitive "be clean from" — object shouldn't fire; from-source is the right home.)*

### Gen 17:1 — "walk before me, and be blameless" (ta.mim)
- **BEFORE:** `how = be` (copula only) — the lived verb "walk" lost to a coverage-gap.
- **AFTER:** `operation = walk (H1980)` ◀ — the imperative, correctly preferred over the narrative "said". *(first pass wrongly grabbed "said"; tightened.)*

### Heb 9:14 — "the blood of Christ … purify our conscience from dead works" (katharizō)
- **BEFORE:** `object = conscience` (good); no from-source.
- **AFTER:** `object = conscience` retained ◀ ; `from-source = works` ◀ ; location=spirit+conscience. *(the agent "blood" remains a coverage-gap — the binding/agent delta is still on the list, not yet baked.)*

### Deu 15:10 — "give … freely … your heart shall not be grudging" (na.tan)
- **BEFORE / AFTER:** `sense = give, freely, give` (manner kept); `cause_clause = … bless all work [infinitive]` ◀tense added. *(object=heart is a pre-existing mis-parse — heart is the subject of a different clause; unchanged by these fixes, noted.)*

---

## 3. Five new verses — for your review

> Chosen for diversity: a creation-prayer, a washing-from-sin, a rhetorical impossibility, an NT purpose-clause, a refining metaphor. Full before/after in the harness output; here is what each **captured well** and what it **surfaces for your eye**.

1. **Psa 51:10 — "Create in me a clean heart, O God"** (ta.hor)
   - ✓ `quality-bearer = heart`; `how = Create (bara)`; location heart/spirit/inward-parts.
   - **Surfaces:** purity here is **created by God**, not achieved — divine-monergism. With Pro 20:9 below this forms a **movement: self cannot make clean → God creates/cleanses** (Eze 36:25 too). The substrate now carries the edges to assemble it.

2. **Psa 51:2 — "wash me … from my iniquity, and cleanse me from my sin"** (ta.her)
   - ✓ `object = me`; `from-source = iniquity | sin` ◀ (both clauses); origin=received-from-outside.
   - **Surfaces:** clean from-source = the **content of defilement is moral** (iniquity/sin), confirming the realm-disambiguation payoff. "Wash" (the parallel verb) is a coverage-gap → a binding/parallel-verb candidate.

3. **Pro 20:9 — "Who can say, 'I have made my heart pure; I am clean from my sin'?"** (ta.her)
   - ✓ `from-source = sin`; location=heart.
   - **Surfaces (two):** (a) **possessive-pronoun object** residual — `object = my` should be **heart** (§1 residual, recommend baking); (b) **rhetorical impossibility** — the verse asserts *no one* can self-purify; the mechanical pass reads it flat (misses the rhetorical negation/modality). → **exegesis-gate** lens (rhetorical question / asserted-impossibility).

4. **Tit 2:14 — "to purify for himself a people … zealous for good works"** (katharizō)
   - ✓ `object = people`; `from-source = lawlessness` ◀.
   - **Surfaces:** purification has a **purpose/telos** ("for himself … zealous for good works") — a purpose-clause edge not yet a field (overlaps the cause/effect-joinable delta). Christ as **agent** (gave himself) is a coverage-gap (binding/agent delta).

5. **Mal 3:3 — "he will purify the sons of Levi and refine them like gold"** (ta.her)
   - ✓ `object = silver`; co-term tse.da.qah "righteousness".
   - **Surfaces:** the **metallurgical refining metaphor** — the *tenor* is purifying **people** (sons of Levi); the *vehicle* is **metalwork** (refiner/silver/gold). The engine grabbed the vehicle-object "silver" over the tenor "sons of Levi". → **exegesis-gate** lens (metaphor vehicle-vs-tenor), and an object-fidelity edge case (two objects, one figurative).

**Net from the 5-new:** two more **gate-bound interpretive lenses** (rhetorical-impossibility, metaphor vehicle/tenor), one more **mechanical residual** (possessive-pronoun object), and — importantly — a **genuine cross-verse movement** assembled from the corrected edges (self-cannot → God-creates-purity). The discovery-lookout flagged the uncaptured content words in every case.

---

## 4. Recommendation

- **Reviewed-six: corrected and validated** — bake confirmed. ✓
- **From the 5-new:** bake the **possessive-pronoun object** fix (same class as the quantifier one, low-risk); route **rhetorical-impossibility** and **metaphor vehicle/tenor** to the **L1.5 exegesis gate** (they are interpretive); keep **intransitive-stative object** and **binding/agent** + **purpose/telos** + **parallel-verb** on the mechanical-delta list for the next engine increment.
- **Then:** one more tightening pass (possessive-object + the residuals you approve) → re-pilot → **gated corpus sweep** for the clean ve-lexical baseline (DB integrity check after, per the tracker).
- **Your steer:** sign off the 5-new (and the possessive-object bake), and tell me whether to (i) do the next mechanical-delta increment now (binding/agent · purpose · parallel-verb · stative-object · possessive-object) before the sweep, or (ii) sweep on the current confirmed set and carry the rest as gate/next-increment.

*Fidelity fixes validated on six reviewed verses (all errors corrected, two new mis-fires caught and fixed in a second pass — the case for reviewing before sweeping); five new verses surface two more gate lenses, one mechanical residual, and a real cross-verse movement. No DB write; engine code only.*

---

## 5. Increment 3 — the next mechanical-delta batch (baked + validated)

Per your steer ("proceed to 1 — build all known mechanical areas before the sweep"), the remaining cleanly-mechanical deltas are now in `derive()`. **Crash-tested over all 1,686 M12 units → 0 errors.** Each validated read-only (no DB write).

| Delta | What it does | Validated |
|---|---|---|
| **possessive-object** | object that is a bare possessive ("my") → advance to the head noun *if a noun follows* (object pronoun "cleanse me" kept) | Pro 20:9 *my → (then suppressed, see below)*; 1Ch 28:5 *all → sons* |
| **intransitive-stative suppression** | "be clean **from** X" has no object — drop the object row when its value is a from-source noun (+ orphaned object-type) | Eze 36:25 *ta.her*; Pro 20:9 (object dropped — it's "clean from sin") |
| **instrument / binding** | noun governed by an **unambiguous** instrumental (Greek *dia* "through") | Heb 9:14 *Spirit* (en/Hebrew be- dropped — too polysemous → gate) |
| **purpose / telos** | infinitive-of-purpose after the term (Greek inf. mood `N`; Hebrew inf.), or eis/hina/pros + noun | Heb 9:14 *serve God*; 261 across M12 |
| **adjacency / isolable** | a verse OPENING with a causal/coordinating conjunction depends on the prior verse → `isolable=no` (must not be read alone) | 1Ch 28:5; 189 across M12 |
| **transition** | **deliberately NOT baked** — the "from X → state Y" movement is an *inference*; per the reset it is assembled at **synthesis-B** from the per-verse facts (from-source · sense · tense), not mechanised. (It mis-fired on non-cleansing terms — "all → given" — confirming it is not a per-verse fact.) | removed |

**Mis-fires caught and fixed during this increment** (again, the value of validating before sweeping):
- `instrument = Lord` (Mal 3:3) — Hebrew prefix-prep is **inline on the noun**, not a separate token; `_gov()` now handles both tokenizations, and `be-`/`en` were dropped as too ambiguous. Now correctly silent there.
- duplicate `from-source`, orphaned `object-type` after suppression — fixed.
- degenerate `transition` ("uncleanness → uncleanness", "all → given") — led to the decision to **not** bake transition at all.
- `from-source = all` (1Ch 28:5) — `_gov()` now skips a quantifier/possessive even in the inline-prefix case → *sons*.

**Field coverage across all 1,686 M12 units:** object 1170 · from-source 514 · purpose 261 · isolable 189 · quality-bearer 156 · operation 23 · instrument 3 · discovery 1686 (every verse). Conservative where it should be (operation/instrument fire rarely and only on clean signals).

### Still open (by design)
- **Mechanical, deferred:** Hebrew/`en` instrument + **agent-as-subject** ("the blood … purify") — needs subject detection, risk of noise; left for a later pass or the read.
- **→ L1.5 exegesis gate (interpretive):** figurative/somatic-metaphor (clean hands), **metaphor vehicle-vs-tenor** (Mal 3:3 silver vs sons of Levi), **rhetorical-impossibility** (Pro 20:9), parallelism-as-composite, the "ultimate-reward" reading.
- **→ synthesis-B:** transition/becomes, faculty-as-observable (the seats are already captured via `location`; the lemma-intrinsic `faculty` field is a model decision, not a fidelity fix).

### Recommendation
The mechanical fidelity layer is now **comprehensive and stable** (0 errors over the full M12 corpus). I recommend: **one more thing to confirm with you, then the single gated sweep** — namely whether the deferred **agent-as-subject** is worth a noisy mechanical attempt now or left to the read. If you're content to leave it to the read, we are **ready to sweep**: wire the runner to also persist the new fields + the runner-side adjacent verse-lexical ref for `isolable`, `--dry-run` → inspect → `--live`, integrity check after (per the tracker). The interpretive lenses go to the gate either way.
