# VE lexical — corrective-actions analysis (categorised) — 2026-06-15

> Overnight digest of the five review examples (vc=1630, 2670, 2671, 14782, 14779). Researcher's verdict: **not one verse-lexical was complete.** This works through every example and sorts every corrective action into types — **error corrections · rule changes · extensions of existing VEs · new VEs**, plus **data-integrity** and **study/characteristic-level** (which don't fit the four but are real). To be worked through with the researcher in the morning.
>
> Running log of the raw items: [wa-ve-iteration2-action-register-20260615.md](wa-ve-iteration2-action-register-20260615.md) (A1–A9, D-A…D-D). Per-verse evidence: [wa-ve-narration-feedback-vc1630-20260615.md](wa-ve-narration-feedback-vc1630-20260615.md). Authoritative design: [01b](01b-VE-field-reliability-and-rules.md).

---

## 1. The meta-pattern — *why* no verse was complete

A verse makes a **proposition** about an inner-being term. That proposition has predicate-argument structure:

| role | the question it answers | example (2Sa 1:9 *agony*) | captured today? |
|---|---|---|---|
| **subject** = the term | identity / what it is | *agony* (sense, type, mode, faculty) | ✅ yes (mostly) |
| **location** | where it is seated | the *nephesh* (soul) | ⚠ mis-derived (homograph/English-word) |
| **predicate / "how"** | how it operates | *seized* (it grips) | ❌ no |
| **object / target** | on whom / toward what | *me* ("directed for…") | ❌ bare preposition only |
| **cause / elicitor** | what triggered it | (vc=14779: the perceived spirit) | ❌ no |
| **effect / response** | what it produces | (vc=14782: *bowing faces*) | ❌ no (read VE deferred) |
| **intensity** | how much | (vc=2670: *cares are many*) | ❌ no |
| **emergent characteristic** | what capability it reveals | (vc=14779: *perceiving the spiritual*) | ❌ no (synthesis layer) |

**The systemic gap:** the mechanical pass captures the **subject's attributes** but almost none of the **predicate-argument web** — and that web *is* where the verse's meaning lives. So the "new VEs" are not random additions: they are precisely the **argument roles around the term** (object, cause, predicate/how, intensity, effect). The "rule changes" fix the **subject attributes** that were mis-derived (sense, location). That is the whole shape of the work.

---

## 2. The five verses at a glance

| vc / ref | term | what it exposed | categories touched |
|---|---|---|---|
| 1630 / 2Sa 1:9 | *sha.vats* "agony" | translit-no-gloss; location missed (nephesh); relational has no object; "seized" (how) absent; "od" qualifier soft-deleted | A,B,C,D,E |
| 2670 / Psa 94:19 | *sar.ap.pim* "anxiety" | 3 co-terms no gloss; "cares **are many**" (intensity) absent | C, D |
| 2671 / Psa 139:23 | *sar.ap.pim* "anxiety" | **sense is the uniform gloss, not per-occurrence** (the biggest error); (mislink suspicion → cleared) | A, B |
| 14782 / Luk 24:5 | *emfobos* "afraid" | **effect** "bowed faces" missing (read VEs 9–12 not built) | C |
| 14779 / Luk 24:37 | *emfobos* "afraid" | location=spirit **false** (ghost); spirit is the **cause** of fear; **"perceiving a spirit" = a missed characteristic** | A,B,D,F |

---

## 3. Corrective actions by category

### A — ERROR CORRECTIONS (values currently *wrong* in the DB — highest priority; the 30,571 narration findings carry them)
- **E1 · VE1 sense = uniform short gloss** [A7] — `step_subgloss_label` is STEP's `gloss` (e.g. "anxiety"), stamped on every occurrence; the true per-occurrence sense is `target_word` ("thoughts" / "cares"). **Systematic — all 40,739 units.** Fixed by **R1**.
- **E2 · VE5 location homographs** [A2] — "spirit"=ghost (14779); the English-word scan also assigns literal "hand/back/members" and out-of-context seats. Fixed by **R2**.
- **E3 · VE7 faculty homograph** [dry-run] — "will" (auxiliary) → false `volition` (Deu 31:20). Fixed by **R3**.
- **E4 · VE13 relational noise** [dry-run] — bare "to/for/from" assigned with no object. Fixed by **R4 + N1**.

### B — RULE CHANGES (derivation logic of existing VEs)
- **R1 · VE1 sense source** [D-C] — derive from `target_word` (per-occurrence) anchored to `medium_def` (lemma meaning), replacing the uniform gloss. *Resolves E1. FOUNDATIONAL — underpins R2.*
- **R2 · VE5 location = sense-gated** [A2] — assign a seat only when the term's/co-term's **per-occurrence sense IS the constitutional seat**; drop the blind English-word scan; use seat **terms**. *Depends on R1.*
- **R3 · VE7 faculty list refinement** — disambiguate/remove homographs ("will"); keep R1-direct(gloss) / R2-neighbourhood-gated.
- **R4 · VE13 relational requires an object** — drop object-less bare prepositions; restrict to relational verbs + directional-with-resolved-object. *Pairs with N1.*
- **R5 · rendering rule** [A1] — a transliteration is **never** shown without its gloss (VE3 values + narration + all outputs). *(Already a governing memory.)*

### C — EXTENSIONS OF EXISTING VEs
- **X1 · VE3 compound** [A1, A4] — (i) render co-terms **with gloss**; (ii) implement the **"term + T2 qualifier (the how)"** arm that 01b §1b-C specified but is not built (today only co-occurring registered terms exist). *The qualifier predicate itself needs data — see DI2; overlaps N3.*
- **X2 · VE5 location** [A2] — extend signals to constitutional-seat **terms**, sense-gated (= R2).
- **X3 · VE13 relational** [A3] — extend bare direction → direction + object (= R4 / N1).
- **X4 · VE1 sense** [A7] — extend to per-occurrence + lemma anchor (= R1).
- **X5 · build the read VEs 9–12** [A8] — purpose, typology, **immediate-response, produces-effect**; the effect ("bowing faces") lives here. *(Decision D-D: recover from soft-deleted l2_api / re-read / mechanical proxy.)*

### D — NEW VEs (the predicate-argument roles — recommend designing as ONE coherent extension, not piecemeal)
- **N1 · OBJECT / target** [D-A] — the node the term is directed at / acts on (the fear's object = the spirit; "directed **for** *him*").
- **N2 · ELICITING CAUSE** [14779] — what triggered the term (the perceived spirit **caused** the fear). Distinct from object (cause ≠ target).
- **N3 · the "how" / governing-predicate qualifier** [D-B, A4] — the verb expressing how the term operates (*seized*).
- **N4 · INTENSITY / quantifier** [A4] — "how much" (*cares are many*).
- *These match the cause-side-gap design (eliciting_cause · object · valence · experiencer_type · typed_relationship). Consider also **valence** (righteous/sinful) and **experiencer** while designing N1–N4.*

### E — DATA-INTEGRITY FIXES (the underlying data, not VE logic)
- **DI1 · soft-deleted qualifier/seat occurrences** [A5] — *od* ("still lingers") at 2Sa 1:9 and *pneuma* at Luk 24:37 are legit qualifier/seat terms but `delete_flagged=1`, thinning the compound/location web. Investigate the verse-uniqueness/XREF cleanup over-reach.
- **DI2 · governing predicates not stored** [enables N3] — *seized* / *many* aren't tagged at all (only analysed terms get spans). Capturing the "how"/intensity needs **re-parsing STEP's full verse HTML** for the span's governing verb/modifier — a data-acquisition step.
- **DI3 · verse↔term correlation** [A6] — sampled clean (0 mislinks); OWNER/XREF coverage asymmetry noted, not a bug. **CLOSED** unless a full sweep is wanted.

### F — STUDY / CHARACTERISTIC-LEVEL (above the VE layer)
- **S1 · emergent characteristics** [A9] — the model flattens capabilities into generic faculties; *"perception of (apparent) spiritual phenomena"* (Luk 24:37) is a real inner-being capability completely missed. The synthesis layer must surface these from the verse evidence (object + faculty + nature). Note *dokeō* "**thought** they saw" → a **believed/mistaken** perception — the *veridicality* of perception is itself a dimension.
- **S2 · the verdict** — the mechanical pass nails the **subject**, not the **proposition**; completeness needs C + D + X5 (the predicate-argument + effect web) plus the read layer.

---

## 4. Consolidated matrix

| ID | category | item | example(s) | register | depends on |
|---|---|---|---|---|---|
| E1 | error | VE1 sense = uniform gloss | 2671 | A7 | R1 |
| E2 | error | VE5 location homographs | 14779,1630 | A2 | R2 |
| E3 | error | VE7 "will" homograph | (dry-run) | — | R3 |
| E4 | error | VE13 bare-preposition noise | (dry-run) | — | R4,N1 |
| R1 | rule | VE1 sense ← target_word+medium_def | 2671 | D-C | — (foundational) |
| R2 | rule | VE5 location sense-gated | 14779 | A2 | R1 |
| R3 | rule | VE7 list refinement | — | — | — |
| R4 | rule | VE13 requires object | 1630 | A3 | N1 |
| R5 | rule | translit always + gloss | all | A1 | — |
| X1 | extension | VE3 + gloss + qualifier arm | 1630,2670 | A1,A4 | DI2 |
| X5 | extension | build read VEs 9–12 | 14782 | A8 | D-D |
| N1 | new VE | object/target | 1630,14779 | D-A | — |
| N2 | new VE | eliciting cause | 14779 | — | DI2? |
| N3 | new VE | "how"/predicate | 1630 | D-B | DI2 |
| N4 | new VE | intensity/quantifier | 2670 | A4 | DI2 |
| DI1 | data | soft-deleted qualifiers/seats | 1630,14779 | A5 | — |
| DI2 | data | predicates not stored (STEP reparse) | 1630,2670 | — | — |
| S1 | study | emergent characteristics | 14779 | A9 | N1,N2 |

---

## 5. Suggested sequence (dependency-ordered)

1. **R1 (sense source)** — foundational, corrects the single widest error (E1) and unblocks R2. *Decision D-C.*
2. **R5, R2, R3, R4** — refine the existing mechanical fields (cheap), then **regenerate ve_lexical + the narration findings** once. Corrects E1–E4 + renders gloss.
3. **DI2 (STEP full-verse reparse)** — acquire governing predicates/modifiers; unblocks N3, N4 and the X1 qualifier arm.
4. **N1–N4 (predicate-argument VEs)** — design together as one coherent extension; then extend the narration composer to render them.
5. **X5 (read VEs 9–12)** — *Decision D-D* (recover vs re-read vs proxy); extend composer.
6. **DI1 (soft-deleted qualifiers/seats)** — investigate the cleanup over-reach; affects the web.
7. **S1 (emergent characteristics)** — synthesis-layer, later.

---

## 6. Open design decisions for the morning

- **D-C — VE1 sense source:** target_word (per-occurrence) · medium_def (lemma) · or both. *(Recommend both: per-occurrence anchored to lemma.)* — **do first.**
- **D-A — object/target (N1):** new VE, or fold into VE13? And is **cause (N2)** a separate field from object?
- **D-B — the "how"/predicate (N3) + intensity (N4):** acquire via STEP reparse (DI2), read, or UNRESOLVED?
- **D-D — read VEs 9–12 (X5):** recover from soft-deleted l2_api (8,174 verses), re-read all, or mechanical proxy?
- **New — valence & experiencer:** design alongside N1–N4 (per the cause-side-gap field set)?
- **New — emergent-characteristic capture (S1):** is this a VE flag, or purely a synthesis-layer concern?

---

*Nothing in the data has been changed. This is analysis only — the corrections, extensions, new VEs and rule changes are queued for the morning's work-through.*
