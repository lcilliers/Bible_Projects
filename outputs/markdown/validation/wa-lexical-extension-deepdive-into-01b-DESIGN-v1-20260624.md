# Capturing the deep-dive understanding INTO the lexical — integration design for 01b (v3)

- **File:** wa-lexical-extension-deepdive-into-01b-DESIGN-v1-20260624.md · **v1 · 2026-06-24 · Author:** Claude Code.
- **Researcher framing (2026-06-24):** the deep-dive findings are **part of the lexical of each verse** (or collection of verses). They (i) **fill blanks** in existing lexical elements, (ii) add **new elements applicable across all types**, and (iii) add **elements specific to a type** (a STATE expects: *of what? who set it? can it change? what changes it?*; a CHARACTERISTIC must have a *faculty*; etc.). The **core lexical definition exists** — `Workflow/Instructions/01b-VE-field-reliability-and-rules.md` — and **the current work must find its way into it.** Aim: **capture the deep-dive understanding for re-use.**
- **What this doc is:** the integration design — how the M12/M13/M14 work extends 01b. **Proposal for confirmation before editing the canonical 01b (→ v3).** It also **closes 01b §8** (the emergent-character debate).

## §1. The framing, in 01b's own terms

01b already holds the architecture this needs:
- the **expectation test P5** (resolved · NONE/silent · UNRESOLVED) — a field goes UNRESOLVED *only when the verse signals a value is expected.* The deep-dive's **type-specific expectations** are simply *what signals a value is expected* — i.e. **P5, conditioned by object-type.**
- **§8 emergent character** — the parked proposal that characteristics **emerge from the mechanical items**. The deep-dive resolves it: the **object-type emerges** from the per-verse evidence, and it in turn **conditions which items are expected.**
- **two scopes.** 01b is per-verse; the researcher notes a value may live in **adjacent verses** or be **silent here**. So the lexical operates at **two scopes**: the **per-verse lexical** (01b as-is) and a **per-term/unit collection lexical** (the term across its verses) — the home of the deep-dive understanding. Per-verse silence ≠ unit silence (the value may surface in another verse of the same term).

## §2. The three growths, mapped to 01b

| Growth (researcher) | In 01b terms |
|---|---|
| **(i) fill blanks in existing elements** | the **LRT recovery** — a nature-EXPECTED field that is empty is located (verse / adjacent verse / bound term) and filled, or flagged UNRESOLVED / lexical-remediation. (e.g. the `how`/manner on giving.) Uses existing items (N3 how, N1 object, 6 origin…). |
| **(ii) new elements applicable across ALL types** | new **universal VE items** — chiefly **object-type** (§3) and **pole-relation** (the axis-partner) and the **binding-web** as first-class (extends item 3 compound). |
| **(iii) elements specific to a type** | **type-conditioned expected element-sets** (§4) — P5 expectation made type-specific; plus a few **new type-specific items** (§5). |

## §3. The new universal item — `object_type` (the emergent kind) — closes §8

- **object_type** · {characteristic · state/condition · expression · qualifier · identity · bivalent-faculty} · **emergent — derived from the per-verse evidence + grammatical `type`**, at the **collection (term) scope** · **RULE (flows from evidence, never from a lemma-constant):**
  - grammatical `type=status` + **valence varies across the term's verses** → **state/condition** (or **bivalent-faculty** if a faculty is present and valence flips good/evil by verse);
  - grammatical `type` + a **`how`/operating-predicate** showing the person acting from an inner faculty (faculty present) → **characteristic**;
  - grammatical `type=action` + a **binding** (a manner-term or a co-expressed characteristic) → **expression**;
  - always **modifies another term** (own object empty; rides a host virtue) → **qualifier**;
  - a **person-classification** (object_type=person, a verdict/label) → **identity**.
- **states:** resolved · UNRESOLVED (evidence insufficient) — NOT NONE (every analysed term has a kind).
- **Distinct from item 2 `type`** (POS, mechanical bedrock). object_type is the **analytical kind** the grammatical type + evidence yields. **This is 01b §8's "characteristic emerges from the mechanical items" — generalised to six kinds.**
- It is **the switch that selects the expected element-set** (§4).

## §4. Type-conditioned EXPECTED element-sets (P5 made type-specific — the LRT formalised)

For each object_type, the verse/collection is **expected to answer** a set of questions; an expected-but-empty answer is the LRT red flag (→ locate / UNRESOLVED / remediation), a silent-and-not-expected answer is legitimately NONE.

| object_type | Expected answers (the "what it must say") | Mostly via 01b items |
|---|---|---|
| **STATE / condition** | **of what?** (the bearer/subject) · **who set it?** · **can it change?** (mutability) · **what changes it?** · its **valence register** · its **pole-opposite** | N1 object/sense · 6 origin + 8 divine · **NEW mutability** · N2 cause / **NEW transition-trigger** · valence · **NEW pole-relation** |
| **CHARACTERISTIC** | **which faculty?** (REQUIRED — a characteristic must have one) · **how does it operate?** · **directed at what?** · **whose?** · manner/intensity | **7 faculty (required)** · N3 how · N1 object · experiencer · N4 intensity |
| **EXPRESSION** | **the act** · **the manner** (how) · **what it expresses** (the bound characteristic) · **acted on what?** · **who acts?** | N3 how / item 2 action · **NEW binding** (extends 3 compound) · N1 object · experiencer |
| **IDENTITY** | **classified as what?** · **who classifies?** (the verdict-giver) · **on what basis?** · **settled or reversible?** | sense · 8 divine / experiencer · N2 cause/basis · **NEW mutability** |
| **QUALIFIER** | **what does it modify?** (the host) · **what modification?** (un-X / intensify) · (never standalone) | 3 compound (role=modifies) · sense |
| **BIVALENT-FACULTY** | **the faculty** (neutral) · **the per-occurrence valence** (good/evil) · **what directs it?** (aim/object) | 7 faculty · **valence (the discriminator)** · N1 object |

*(The researcher's STATE example is row 1 in full; CHARACTERISTIC's "must have a faculty" is the REQUIRED tag on item 7.)*

## §5. New items needed (small, additive)

- **mutability** · {fixed · changeable · UNRESOLVED} · collection-scope · **RULE:** across the term's verses, does any verse show the state set/removed/reversed? (e.g. cleanness ↔ defilement, innocence ↔ guilt). Expected for STATE/IDENTITY. · NONE if not a state.
- **transition-trigger** · the node/act that changes the state · collection-scope · **RULE:** the act/agent that moves the bearer between the state and its pole (e.g. cleansing → clean; sinning → guilty). Often an EXPRESSION elsewhere. Maps onto / extends N2 cause.
- **binding** (extends **item 3 compound**) · for an EXPRESSION, the **manner-term + the characteristic it expresses** (with cluster) · **RULE:** the manner-word in the verse (or adjacent) and/or the co-seated characteristic = what the act expresses (e.g. give + "freely"/willing-heartedness M09 / che.sed M05). The compound **role** vocabulary gains `expresses` / `manner-of`.
- **pole-relation** · the term's inverse/axis-partner (within- or cross-cluster) · collection-scope · **RULE:** the antithesis the evidence pairs it with (clean↔unclean, truth↔deceit, innocence↔guilt, incorruption↔corruption). Co-seating + cross-cluster ownership give it.

All four obey P5 (NONE when not expected; UNRESOLVED when expected-but-undetermined) and P1 (derived from named measures: valence-variation, co-seating, cross-cluster ownership, the binding term).

## §6. The collection scope + silence/adjacency (researcher's point, formalised)

- The deep-dive lexical has **two scopes:** **per-verse** (01b items, as built) and **per-term/unit collection** (object_type, mutability, pole-relation, the consolidated expected-answers — *assembled across the term's verses*).
- **A value may be sourced from an adjacent verse or the passage**, not only the head verse — recorded with **citation of the source verse** (extends P7). Per-verse **silence is expected and fine** (P5); the **collection** answers what no single verse does.
- This is the reuse payload: once a term's collection-lexical is filled (object_type + its expected answers + binding-web + pole-relation), it is **captured once and reused** — synthesis reads it, other clusters cite it, and re-derivation reproduces it (P6 whole-verse reset still holds per-verse; the collection layer is rebuilt from the per-verse rows + the cross-verse rules).

## §7. How it lands in 01b (→ v3) — and what it closes

1. Add **object_type** (§3) as a new universal item (resolution order: after the per-verse items, at collection scope).
2. Add **§4 type-conditioned expectedness** as the formal statement of P5-by-type (this is the LRT spec, promoted into the canonical rules).
3. Add the four **new items** (§5).
4. Add the **collection scope** + adjacency-citation (§6) to §2/§6.
5. **Close §8** — emergent character is resolved: characteristics (and the other five kinds) **emerge as `object_type`** from the mechanical items; not authored, derived. (Also revisit §4d: some "type-specific expected answers" — who-set, what-changes — overlap purpose/effect, but now have a *lexical* basis via origin/cause/transition-trigger, so the §4d exclusion may narrow.)
6. **Storage:** the collection-lexical rows live in `ve_lexical` at term scope (a `ve_label` set: `object_type`, `mutability`, `pole_relation`, `binding`…), regenerable from the per-verse rows + the cross-verse rules; researcher notes preserved (§4e lifecycle).

## §G — bias-guard

- This **extends, does not replace** 01b — every new item still obeys P1 (mechanical/derived from named measures), P5 (expectation test), P7 (citation). The object_type RULE is explicitly tied to **per-verse-varying** evidence (valence-variation, how-predicate, binding) — **never** the lemma-constants (type/faculty as per-verse claims) that the M10/M11 validation caught.
- The type-conditioned expectedness is the **LRT made canonical** — it is what tells us a blank is a *gap* vs a legitimate *silence*, by object-type. That is the researcher's "a status must say… / a characteristic must have a faculty."
- It is a **DESIGN proposal** — 01b is canonical and SETTLED; this should be confirmed (and ideally test-applied to one M12 term end-to-end) before editing 01b to v3.

*Integration design — the deep-dive understanding is the lexical growing at a new collection scope: one new universal item (object_type, which closes §8's emergent-character debate), type-conditioned expectedness (the LRT made canonical — "what a state/characteristic/expression must say"), four small new items (mutability, transition-trigger, binding, pole-relation), and the verse-or-collection scope with adjacency-citation. Lands in 01b as v3, captured once in ve_lexical for reuse.*
