# The Lexical-Revelation Test (LRT) — is the lexical fully revealing? (governing, step-3 gate)

- **File:** wa-lexical-revelation-test-LRT-spec-v1-20260624.md · **v1 · 2026-06-24 · Author:** Claude Code.
- **Origin:** researcher requirement (2026-06-24): deep evidence-gathering must include tests for whether the lexical is **fully revealing** — *what is missing, what is expected but not present, what contradicts, were all the lexical fields properly considered, is there an odd one out, how do the parts play together* — with the worked principle that **giving's `how` cannot be null** (an act has a manner; a null there means the lexical missed something real → locate it, assess it).
- **Status:** GOVERNING — run the LRT on **every unit during step 3 (deep evidence)**, *before* any object-type/characteristic conclusion. Mechanical helper: `scripts/_lexical_revelation_test_20260624.py`. Builds on the validation finding that the lexical base is accurate but **incomplete on operational predication** (`how`/`object` empty when the predicate sits on a partner word).

## §1. The seven checks (per unit)

1. **All fields considered?** — coverage % of every per-verse field (sense, object, object_type, experiencer, valence, how) + the constants (type/faculty/lemma_meaning, used descriptively only).
2. **Expectedness / what's missing** — given the unit's **nature**, which fields *should* be populated? A nature-expected field that is empty/sparse = **RED FLAG** (the lexical is not fully revealing there).
3. **Locate the missing** — for each red flag, *where is the content*: (a) in the verse_text (predicate on a partner word), (b) in a **bound/co-seated term** (often another cluster), (c) genuinely absent, (d) in the wrong field. Quantify + propose how to assess/recover.
4. **Contradiction** — fields that conflict (e.g. action-type with no object **and** no how; valence neutral but co-seated with sin-terms; sense moral but valence neutral).
5. **Odd one out** — outlier occurrences whose field-profile diverges from the unit (candidate mis-owned / mis-glossed / genuine sub-sense).
6. **Parts play together** — do the fields compose into one coherent reading, or fragment into registers (distinctness counts)?
7. **Verdict** — is the lexical FULLY REVEALING for this unit? If not: state precisely what's missing and the recovery/assessment route (→ a lexical-remediation item).

## §2. Expectedness rules (nature → fields the lexical must carry)

| Nature | Fields the term's nature DEMANDS | Empty-where-expected = |
|---|---|---|
| **act / expression** | sense · object · **how (manner)** · experiencer | a manner-gap (giving/consecrating: *how* must not be null) |
| **state / condition** | sense · **valence** (and valence-variation = state-signal) | a register-gap |
| **characteristic** (faculty-in-operation) | sense · object · experiencer (often how) | a direction/operation-gap |
| **relational** | sense · object · experiencer | a relation-gap |

The nature is taken from the lemma's grammar (type) **as a descriptive property only** — used to set *expectations*, never to assign the object-type (which still flows from the per-verse evidence, step 4).

## §3. Worked demonstration (M12)

| Unit (nature) | nature-expected field | coverage | LRT verdict |
|---|---|---|---|
| **Cleanness tahor (state)** | valence | **96%** | **fully revealing for its nature** — the state-register is captured |
| **Holiness/consecr (act)** | how (manner) | **4%** → RED FLAG | **not fully revealing** — *what* (object 80%, 78 distinct) + *valence* (97%, incl. counterfeit sinful/forbidden) are rich; the **manner of consecrating is missing** (needed for expression-vs-devotion call) |
| **Giving na.tan (act)** | how (manner) | **0%** → RED FLAG | **not fully revealing — and the gap reveals a SPLIT** (below) |

**The giving case (the principle in action).** `how` = 0/1065 is impossible for an act *if* the act is an inner-being expression — so the LRT forces the question. Recovery:
- Manner-words appear in the verse_text in only **~3–5%** of occurrences (freely / willingly / freewill / liberally / not-grudgingly).
- **83/1065** are action with **no object AND no how** — pure bare transfer.
- The heart/manner binding co-terms (lev M47 ×29, che.sed M05 ×21, ba.rakh M39 ×28) cluster on a small subset.

→ **The how-gap is two things at once:** (a) a **true split the lexical failed to mark** — a small *willing/heart-bound* giving that **is** an inner-being EXPRESSION (manner recoverable from verse_text + M09 willing-heartedness / M05 che.sed bindings), inside (b) a large mass of *transactional transfer* (give land / into hand) that has **no manner because it is not an inner-being act**. The lexical lumped both as "give." Assessment route: **mark the inner-being giving subset** (manner-word in verse OR heart/che.sed/freewill binding) and study only that as an expression; the rest is out-of-scope transfer. This both serves the analysis and logs a **lexical-remediation item** (capture manner / mark the inner-being-vs-transfer split on na.tan).

## §4. How the LRT plugs into the sequence
- **Step 3 (deep evidence):** run the LRT first per unit → know what the lexical does and doesn't carry, and recover/locate the missing before reading.
- **Step 4 (object-type test):** decide characteristic / state / expression **only** from the fields the LRT confirmed are populated + the located bindings; never from a field the LRT flagged as missing (don't infer a characteristic from a bare act whose manner is absent).
- **Output:** each unit's deep-evidence file carries an **LRT section** (the 7 checks + verdict) and feeds a programme **lexical-remediation backlog** (where the lexical needs enrichment — esp. `how`/manner on act-lemmas).

## §G — bias-guard
- The LRT is mostly **mechanical** (coverage, distinctness, odd-one-out, contradiction heuristics) so it resists the reflex; the interpretive part (expectedness, recovery) is constrained by the nature-rules.
- It is symmetrical: it **clears** units where the nature-expected field is populated (cleanness) and **flags** where it isn't (giving/consecration) — not a blanket "lexical is deficient."
- "Missing where expected" is the key signal the researcher named — it caught the giving split that the bare fields hid.

*The LRT — seven checks run before conclusions; a nature-expected field that is empty means the lexical is not fully revealing, so locate and assess the missing content. Demonstrated on M12: cleanness (state) is fully revealing; giving and consecration (acts) have a manner-gap, and giving's gap exposes the transactional-vs-expression split. Governing for step 3 of every cluster.*
