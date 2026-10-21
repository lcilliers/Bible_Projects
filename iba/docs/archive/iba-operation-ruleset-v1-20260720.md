# IBA operation ruleset (v1) — the char in motion, put into words

> **Status: DESIGN FOR CONFIRMATION.** Directed 2026-07-20. Prepared as **content first**
> (representation-agnostic); the config-home is decided separately (§7). Grounds on the authoritative
> ve_nr dimension catalogue (`Workflow/Catalogue/wa-ve-lexical-catalogue-v1-20260702.md`; mirrored in
> `iba/config/process/lexical.json`) and the plan's §14.4 (`operation` table).

---

## 1. The framing (researcher, 2026-07-20)

> **The lexical is the technical layer of the lexicon. The operations output is putting the operation
> in words.** — e.g. *"God's grace abounds in the inner being."*

Two layers over the same read, kept distinct:

| | **Lexical** (`ve_lexical`) | **Operation** (`operation`) |
|---|---|---|
| nature | technical decomposition | the operation **in words** |
| unit | one ve_nr dimension-value on a span | one verbalised statement of the char in motion |
| grain | 101–118, as pair / event / flag / value | a short, self-contained sentence |
| audience | the machine (queryable, drift-checkable) | the reader |
| relation | the **parts** | the **sentence built from the parts** |

The operation is **composed from** the lexical; it never adds meaning the lexical didn't ground
(the `verse-bounded` / no-eisegesis rule carries over). **Collectively, a char's operations describe it
in motion** (§14.4); the **`meaning`** paragraph (§14.4) is the further synthesis *of* those operations.

---

## 2. How an operation is composed from the lexical

An operation is a **predication**: a predicate with its filled arguments and its qualifiers. Each slot is
drawn from a specific ve_nr dimension — nothing invented:

```
[bearer/source]  [PREDICATE]  [target | seat/locus]  ( qualified by: intensity · specifier · manner · direction · device )
    105 / 103       106          107  /  104,116                109        110        108      118        117
```

- **Predicate** = ve_nr **106 operation** (the governing act — *abounds, trusts, fears, turns*).
- **Subject/driver** = ve_nr **103 source** (what drives it) or **105 bearer** (who bears it).
- **Object/locus** = ve_nr **107 target** (+ 116 locus internal/external) or **104 seat**.
- **Result** = ve_nr **111 effect** (the produced state).
- **Qualifiers** (do not spawn their own operation; they modify the sentence): **109 intensity ·
  110 specifier · 108 manner · 118 direction · 117 device**.
- **Body-type tag** (D2): each argument carries its `body_type` — **ib / other-being / physical** — so
  *"God's grace"* is an **other-being** qualifier acting on the **ib** locus, and *"with the hands"* is a
  **physical** qualifier. This is what makes the other-being and physical catalogues extractable (§14.5 / D2).

**Worked example — "God's grace abounds in the inner being":**

| slot | value | ve_nr | body_type |
|---|---|---|---|
| source | God's grace | 103 | other-being |
| predicate | abounds | 106 | — |
| locus | the inner being | 116 (internal) | ib |
| → operation type | **arises-from** (external agent acts on the IB) | | |
| → verbalised | *"God's grace abounds in the inner being."* | | |

---

## 3. The operation-type catalogue (proposal — the ruleset core)

Each type is a **relation skeleton**: the researcher's verbs (*affected-by / affects / has-status /
comes-from / goes-to / interacts / co-exists*, §14.4) made precise, mapped to the ve_nr it reads from,
with a verbalisation template. **This table is the thing to confirm/adjust.**

| # | operation_type | researcher's verb | draws from ve_nr | direction | verbalises as (template) |
|---|---|---|---|---|---|
| 1 | **performs** | (the act) | 106 (+107) | char → | *"the IB's {char} {predicate}s {target}"* |
| 2 | **arises-from** | comes-from / affected-by | 103 source | driver → char | *"{driver} {predicate}s in / drives the IB's {char}"* |
| 3 | **directed-at** | goes-to / affects | 107 target (+116) | char → object | *"the IB's {char} is directed at {object}"* |
| 4 | **produces** | affects | 111 effect | char → state | *"the IB's {char} produces {state}"* |
| 5 | **seated-in** | (has a seat) | 104 seat | seat → char | *"the {char} is seated in the {seat}"* |
| 6 | **borne-by** | (whose) | 105 bearer | person → char | *"{bearer} bears the {char}"* |
| 7 | **has-status** | has-a-status | 102 (type=status) | — | *"the IB is {status}"* |
| 8 | **interacts-with** | interacts | char↔char relation | char ↔ char | *"the {char} {relation}s {other char}"* (gives-way-to / triggers / opposes) |
| 9 | **co-exists-with** | co-exists | 112 coupling | char ↔ co-term | *"the {char} is bound with {co-term}"* |

**Notes on the set:**
- Types **1–7** are argument-structure over one char; **8–9** are char-to-char (they feed the aggregator /
  the neighbour graph). This is where "interlocks with other characteristics" (RESET object) lives.
- The **other-being** and **physical** readings are **not** their own operation types — they enter as
  **body_type-tagged arguments** (usually qualifiers, per D2), which keeps them catalogue-extractable
  without a parallel operation taxonomy.
- ve_nr **106** is *the predicate slot*, not an operation type — resolving the naming collision (the
  dimension named "operation" is one ingredient of an `operation` row, not the row itself).

---

## 4. Verbalisation rules (how the words are formed)

1. **Grounded only.** Every operation is composed from ve_nr values that passed `verse-bounded`; the
   sentence may not assert what no dimension recorded (no eisegesis).
2. **Self-interpretable.** The sentence must read without the verse — it carries its own subject, predicate,
   object (the study's standing `self-interpretable` rule, applied to prose).
3. **Qualifiers fold in, never drop.** intensity / specifier / manner / direction / device modify the
   sentence in place (*"grace abounds **greatly**"*), never becoming standalone (§ the qualifier rule).
4. **Silence is silence.** If a slot is `none`, it is absent from the sentence; if `unknown`, the operation
   is held on the worklist, not fabricated.
5. **One motion per operation.** A verse yielding several motions yields several operation rows; the
   `meaning` paragraph is where they are woven together.

---

## 5. What this gives each downstream object

- **`operation` rows** — the verbalised motions; the primary human-readable analytical unit.
- **`meaning`** — synthesises a char's operations into the meaning paragraph (§14.4).
- **the aggregator** (D4, register/cluster) — groups operations by char / by relation for the concordance.
- **the other-being & physical catalogues** — filter operations by argument `body_type` (D2).

---

## 6. Open boundaries to pin (not blocking the catalogue)

- **operation vs finding** (D3 renamed to both): is a `finding` a *higher-order observation* drawn from
  operations (a movement/tension the operations reveal), or a synonym we should collapse? Proposed:
  **operation = one verbalised motion; finding = an observation across operations** (movement / association
  / seat / expression / tension). Confirm.
- **operation vs meaning**: operation = per-motion sentence; meaning = the char's synthesised paragraph.
  Confirmed by §1 framing; noted for the schema cut.

---

## 7. Config-home (decide separately)

The ruleset content above is representation-agnostic on purpose. Placement options, given the two config
stores (the `config/*.json` seed is **not yet loadable**; `app/db cfg_*` is the flat runtime):
- a new **`cfg_operation_type`** table (the `cfg_candidate_rule` pattern) in the runtime, +
- an **`enum.operation_type`** vocabulary, +
- verbalisation templates as a `spec` on each type.

Recommend we settle the type set (§3) and the operation/finding boundary (§6) **first**, then bind to
whichever config store we carry forward.

---

## 8. Confirm

1. **The framing** (§1) — lexical = technical parts; operation = the parts put into words. Right?
2. **The operation-type set** (§3) — is this the right list of motions (add/cut/rename)? Especially:
   is **has-status** (7) a real type, and are **interacts / co-exists** (8–9) one type or two?
3. **operation vs finding** (§6) — adopt "operation = one motion, finding = observation across motions"?
