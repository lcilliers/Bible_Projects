# 01b — Verse Lexical (VE) Generation — CANONICAL RULES (v3 · 2026-06-24)

> **⚠ FRAMING RESET (2026-06-24):** the *framing* of this document — the object-type grid (Part C) and the intrinsic-faculty field, the "type=characteristic/state" bins, "logical units" as the organising move — is **superseded by `wa-lexical-analysis-rules-reset-v1`** (process/functional reframe: analyse *what the verse does*, let patterns emerge, faculty→"does the verse address a faculty"). The **observable bedrock here (measure layer §2, sense, mode)** and the deterministic mechanics are **retained and referenced** by the reset. Read the reset first; use this for the bedrock detail.

> **v3 (2026-06-24):** added **Part C — the COLLECTION layer** (object_type + the deep-dive understanding captured at term scope, for re-use; resolves Part A §8). Part A (per-verse, v2) is unchanged. See Part C foot for status (tested M12/M13/M14/M16; six object-types stable).

> **Binding companion (2026-06-17):** [01c — T2 treatment & API governance](01c-T2-treatment-and-API-governance.md) fixes (a) the T2 content/grammatical split and its treatment in generation/JSON/reads, and (b) the API governance (batched · ordered · token-minimal · time-monitored with circuit-breaker · self-verified · residue-only — *API never substitutes for a mechanical rule*). Engine alignment + compliance precede any API run.
>
> **This is the canonical instruction for verse-lexical generation.** Every VE item is produced by the deterministic rules below. The original v1 reliability analysis that motivated this is **retained as Part B** at the foot of the file. **Status: design SETTLED 2026-06-16** — all open questions (Q1–Q14) and rule conflicts (C-1…C-6) decided (see inline **[Qn RESOLVED]** / §5 / §7). Remaining work is **list-building + build**, not design.

## 1. Governing principles

- **P1 — Mechanical only.** Every item is fixed by deterministic rules over named measures. **No probabilities, no scoring, no "analytics."** If the rules cannot decide → **UNRESOLVED** (a worklist flag), never a guess. Success = the rules are *definitive*.
- **P2 — Original-language grounded (the error-eliminator).** Signals are read off the **original-language measure layer** (Strong's lemma · morphology · per-occurrence STEP sense · co-occurring tagged terms), **never the English translation string.** Every homograph error (spirit=ghost, will=auxiliary) came from English-string matching; grounding on lemma + morph removes the whole class.
- **P3 — Simple items.** Each item is one simple value (or NONE/UNRESOLVED). Multiples = multiple rows. No compound or narrative values.
- **P4 — Rules may reference other VEs.** Items resolve in a fixed order (§3); a rule may condition on an earlier item's value/presence.
- **P5 — Three states per item — the *expectation test* (governing):** **resolved** = a value, mechanically determined · **NONE / silent** = the verse says nothing about it → **never impute** · **UNRESOLVED** = the verse shows *indicators that a value is expected here* but it cannot be mechanically determined (the read/research worklist). **Silence ≠ UNRESOLVED** — a field goes UNRESOLVED *only* when something in the verse signals the value should exist. So most verses stay legitimately NONE on cause/valence/effect/etc. — no flood of UNRESOLVED.
- **P6 — Whole-verse reset.** The unit of (re)generation is the **verse**. If *any* item must be regenerated (error or omission), **all** items for that verse are reset and re-derived together — single-item patching would break verse coherence.
- **P7 — Citation.** Every resolved value cites the measure/signal that forced it.
- **P8 — Sense is the spine** — resolved first; sense-dependent items read it.
- **P9 — Every coded value carries an English equivalent** [Q2] — no value is stored as a code / transliteration / Strong's alone; each includes a human-readable English form so the researcher can read it (extends the translit-always-with-gloss rule to *all* items).

## 2. The measure layer (acquire FIRST — the prerequisite)

For each verse, ingest the **full-verse original-language morphology** — every word's Strong's + morph code, not just the analysed term (STEP's verse HTML carries this). From it, deterministically read, per term-occurrence:

- lemma · morph → POS · **case/state** · person/number/gender · stem/voice/tense (= mode);
- per-occurrence **target_word** (ESV) + lemma **medium_def** (= the sense inputs);
- **argument structure from morphology** — the term's governing verb; its **subject/possessor** (Greek nominative / verb agreement / Hebrew possessive suffix or construct owner); its **object** (Greek accusative / governed noun / prepositional complement); its **modifiers** (agreeing adjective / quantifier); attached prepositions;
- co-occurring tagged terms (T1/T2) at the reference.

**Why this is the linchpin:** the original language *marks* the predicate-argument structure (Greek case; Hebrew construct/suffix/preposition) that English drops — so object, subject/experiencer, modifier and the governing predicate become **deterministic morphological reads**, satisfying P1. Genuinely ambiguous structure → UNRESOLVED. **[Q1 RESOLVED 2026-06-16]** The full-verse measure layer is **adopted and built**; the lexical items are all mechanically derived and **operate as one coherent collection**. The earlier parking (DI2 and others) is **lifted and superseded** — acquiring this layer is part of the build, not a deferred item.

**PERSISTED 2026-06-16 (M60, schema 3.34.0):** the measure layer now lives **in the DB** — `verse` (canonical, one row per verse) · `verse_morphology` (one row per word: surface · strongs · morph · derived lang/pos/stem/person) · `lexicon` (one row per Strong's: original-language unicode · transliteration · gloss · `medium_def`). The engine **reads these tables, not live STEP** (instant, consistent, auditable). Ingest = `scripts/_apply_ingest_verse_morphology.py` via STEP's direct `getBibleText` endpoint; `wa_verse_records.verse_id` is the FK path. See [[project_measure_layer_persisted]].

## 3. Resolution order (dependency graph)

`mode (column)` → **1 sense** → **2 type** → **experiencer** → **8 attributed-to-God** → **5 location** → **6 origin** → **7 faculty** → **3 compound** → **N1 object** → **13 relational** → **N3 how** → **N4 intensity** → **N2 cause** → **valence** → **11 immediate-response** → **12 produces-effect**. Each may read earlier items.

> ⚠ **Zero-pad fix (2026-06-17, foundational):** the DB measure layer stores Strong's **zero-padded to 4 digits** (`H0430`, `H0408`), but the engine seed lists used the short form (`H430`, `H408`) — so **every <4-digit Hebrew lemma silently failed to match** (Elohim H430, *'al* H408, *'et* H853, faculty H995/H977, …). This broke divine/negation/faculty/object-type detection and masqueraded as "stub" behaviour. Fixed by `_canon()` (pads all seed lists + literals to the DB form). All validations below are **post-fix**. The base rerun will re-derive the corpus on the corrected lists.

## 4. The VE item catalogue

Format — **item · value space · measure · RULE · states · depends-on.** All signal-lists are **original-language lemma/Strong's sets**, not English words.

### 4a. Revised existing items

- **1 sense** · per-occurrence rendering · target_word + lemma medium_def · **RULE:** record **BOTH, explicitly** — the per-occurrence `target_word` AND the lemma `medium_def`, each in readable English (P9). [Q2 RESOLVED] · resolved / UNRESOLVED(no target_word).
- **2 type** · {action, status, quality} · part-of-speech (morph) · **RULE:** verb/participle → action; noun → status; adjective → quality; other → UNRESOLVED. **Part-of-speech ONLY — no sense-override [decided C-1, 2026-06-16].** · resolved / UNRESOLVED.
- **3 compound** · co-occurring tagged terms, **each with its role** · the reference's active term inventory · **RULE:** one row per active co-occurring term (exclude self), value = `translit "gloss" (cluster)` **+ the ROLE/pairing to the head term** (e.g. partner · qualifier-of · object-of · shares-seat). One co-term may carry **more than one role** (C-4/C-6) — state each. Present-only. The "how"/predicate is **not** here → N3. · resolved / (none→no row) · depends: term inventory (DI1). **⚠ may grow into its own VE / need an explicit head↔partner pairing field (researcher flag).**
- **5 location** · {spirit·soul·heart·mind·will·conscience·flesh·body-part:x} (multi) · constitutional-seat **terms** (Strong's seat-map) + their per-occurrence sense · **RULE:** for each co-occurring seat-term whose **sense denotes the seat** (sense-gate via item 1), assign that level. **No English-word scan.** Seat-term present but sense not the seat (e.g. pneuma="apparition/wind") → not a location; sense ambiguous → UNRESOLVED. · multi / NONE / UNRESOLVED · depends: 1 sense, seat-map. **[Q4 RESOLVED — adopt both the seat-map and the sense-gate.]**
- **6 origin** · {within-person · received-from-outside · carried-generationally · not-stated · UNRESOLVED} · original-language source cues · **RULE:** reflexive/internal morph → within-person; a governed "from-source" node → received-from-outside; generational marker → carried; conflict → UNRESOLVED; none → not-stated. **"From God" is NOT a separate origin value** — it is `received-from-outside` + item 8 `God's-role = giver-source` (C-5 de-dup). · **[Q5 RESOLVED — adopt the original-language cue lemma list.]**
- **7 faculty** · the faculties (multi) · **faculty-lemma sets (Strong's)** · **RULE:** R1 the term's lemma IS a faculty → assign; R2 a faculty-lemma term governs/relates-to the term by morph (neighbourhood + grammatical relation) → assign; R4 faculty present but unattributable → UNRESOLVED; R5 none → NONE. English homographs vanish (we key on the Greek/Hebrew volition lemma, not the word "will"). · multi/NONE/UNRESOLVED. **[Q6 RESOLVED — faculty lists are Strong's-lemma sets.]**
- **8 divine involvement (God's role)** · {agent/subject · possessor · giver-source · object/recipient · addressee · none · UNRESOLVED} · a divine lemma (YHWH/Elohim/Theos/Kyrios…) + its morph relation to the term · **RULE (revised + VALIDATED on M01, 2026-06-17):** no divine lemma → **NONE**. Divine lemma present: only the **object** role is mechanical — divine **immediately after the term**, or *'et* (H853) **+ divine after a verb-term** → `object` (the term acts on / is directed at God). All other roles (agent/giver/possessor/addressee) **overlap morphologically** — the distinction is the semantic judgement *is God feared, acting, or giving* — so a divine lemma in any other position → **UNRESOLVED** (→ read). **States the role, never yes/no (C-3).** Single home for all God-related involvement (C-5). · depends: measure layer.
  > **Validation (M01, 1,036 units; post zero-pad fix 2026-06-17):** mechanical `object` = **86/93 = 92%** vs the read (7 leak to `agent`). NONE 601 · object 123 · UNRESOLVED 312. The zero-pad fix (see ⚠) added Elohim detection → object 80→123 at the same precision. Replaces the old meaningless `present`; the read resolves the UNRESOLVED-with-a-role (agent/giver/distant-object/addressee).
- **13 relational** · {direction → object} (multi) · directional prepositions / relational verbs (original-language) + item N1 · **RULE:** a directional/relational node governs the term toward an **object** (N1) → record {direction → object}. **[Q7 RESOLVED]** a directional indicator with **no object at all → NONE**; a directional indicator whose **object is expected but unclear** (needs reading/research) → **UNRESOLVED** (expectation test, P5). · depends: N1.

### 4b. New items (the predicate-argument roles — design as ONE coherent set)

- **N1 object/target** · the node the term acts on/toward · governed object by morph (accusative / direct object / prepositional complement) · **RULE:** record the term's governed object as `translit "gloss"`; sub-attribute **object-type** {person·God·group·thing·abstract·**spiritual-being**} from the object lemma/morph. None → NONE; object position present but unresolved → UNRESOLVED. *(D-A: "may grow its own rules" — object-type is the first such sub-rule.)* **[Q8 RESOLVED — confirmed as new and as defined; object-type sub-rule adopted.]**
- **N2 cause/elicitor** · the node that triggered the term · causal morphology · **RULE:** where the term is an affect/response, the eliciting node = the subject of the **causal clause** (Hebrew *ki* / Greek *hoti/gar* + subject) or the **object of perception** that precedes it. **[Q9 RESOLVED — expectation test, P5]** clear cause → value; verse **silent** on cause → **NONE** (expected for many verses — do not impute); verse shows **indicators a cause exists but it's unclear** → **UNRESOLVED**. Do NOT default whole verses to UNRESOLVED. · depends: 7 faculty.
- **N3 how / governing-predicate** · the verb expressing how the term operates · governing finite verb by morph · **RULE:** record the finite verb governing the term's span as `lemma "gloss"` (e.g. *seized*). None → NONE; unresolved → UNRESOLVED. · depends: measure layer.
- **N4 intensity / quantifier** · "how much" · quantifier/intensifier lemmas agreeing-with/governing the term · **RULE:** record the intensifier (*rab* "many", *me'od* "very", *kol* "all"…) modifying the term. None → NONE. **[Q10 RESOLVED — adopt the intensifier lemma list.]**
- **valence** · {righteous·sinful·commanded·forbidden·neutral·UNRESOLVED} · term-inherent valence + context morph · **RULE (revised + VALIDATED on M01, 2026-06-17 — see note):** mechanical = (a) term-inherent valence (inherently-moral lemmas, e.g. *resha* "wickedness"=sinful) ∪ (b) **forbidden** = a **dedicated prohibition particle** (*'al* H408 vetitive / Greek *mē* G3361) on a **2nd/3rd-person volitive** verb. **`commanded`, `righteous`, `neutral` are NOT mechanised → routed to the read** (interpretive). Expectation test (P5): silent → NONE; the read fills the interpretive valence. (Same NONE-vs-UNRESOLVED logic as cause.)
  > **Validation note (M01 vs the read):** ⚠ **post the zero-pad fix (2026-06-17), `'al` (H0408) now matches** — forbidden fires 27→123 and precision is **99/123 = 80%** (the earlier "93%" was measured on Greek *mē* only, because Hebrew *'al* was silently broken). The 24 misses are *'al-tira* **"fear not" reassurance** (read=neutral) — morphologically identical to a real prohibition. So even `'al`→forbidden is **only ~80% (interpretive ceiling)**; flagged for evaluation at the next cluster (researcher direction). **REJECTED as unreliable:** *lo'+imperfect→forbidden* (ambiguous: "you shall not" prohibition vs "they shall not fear" promise/description — 20 false positives) and *imperative→commanded* (an imperative "fear the LORD" is *both* commanded and the fear righteous — ~50% precise, the choice is interpretive). So valence context is **only partly mechanical**; the read is justified for `commanded`/`righteous`/`neutral`, not an opt-out. Scoping the read by an expectation-test signal is an open design item.
- **experiencer** · {self·other-person·God·group·named} · the term's possessor/subject (morph) · **RULE:** map the term's possessive suffix person / nominative subject → experiencer ("my anguish"→self; "his"→other; divine owner→God). Unresolved → UNRESOLVED. · depends: measure layer. *(Overlaps item 8 — see C-3.)*

### 4c. Read-but-lexical items — INCLUDED [Q13]

These ARE determinable by lexical means (the reaction/result is stated in the verse), so they are mechanical items:
- **11 immediate-response** · the inner being's immediate reaction · the coordinated/following clause (morph: coordinated finite verb after the term's clause) · **RULE:** record the verb-phrase the verse gives as the immediate reaction (e.g. *bowed faces to the ground*). Expectation test (P5): silent → NONE; a reaction is signalled but unclear → UNRESOLVED. · resolved/NONE/UNRESOLVED.
- **12 produces-effect** · the sustained/result effect · result clause (morph: result conjunction / consequence) · **RULE:** record the effect the term produces (e.g. *prostration*). Expectation test as above. · resolved/NONE/UNRESOLVED.

### 4d. Excluded from VE generation (→ synthesis, not lexical) [Q14]

- **VE9 purpose · VE10 typology** — **EXCLUDED.** No clear *lexical* basis (researcher unsure of their objective; if purely conceptual they do not belong in the lexical analysis). Reconsider only if a lexical means of determining them is defined. → synthesis layer.
- **emergent characteristics** (e.g. "perception of the spiritual") — **PARKED for debate (§8)**; the proposal is that they *emerge* from the mechanical items, not as their own item.

### 4e. Meta item — `lexical_note` (a record, not a derived fact)

- **lexical_note** · free-text note attached to the verse · **NOT mechanically derived** — it *records*, it is not a lexical value · **populated by** (i) the read-back audit (§6b) writing its result/flags, and (ii) the researcher · typed by `source`: **`audit`** (auto) or **`researcher`** · **lifecycle:** `audit` notes are **regenerated with the verse** (wiped + rewritten on whole-verse reset, P6); **`researcher` notes are PRESERVED** — never overwritten by regeneration (researcher-authored) · stored as a `ve_lexical` row (`ve_label='lexical_note'`, `value`=note text in plain English per P9, `source_provenance`=`audit`|`researcher`).

## 5. Conflict register (rules that could clash) — researcher decisions, 2026-06-16

- **C-1 type.** *Plain meaning of the old wording:* part-of-speech gives type a first answer (verb→action, noun→status, adjective→quality); v1 then let the word's *sense* override that to split "status" vs "quality"; "supersede deferred" meant we would NOT do that override. **DECISION: type = part-of-speech only** (fully mechanical, no sense-override). *(If sense should later refine status-vs-quality, it becomes its own rule.)*
- **C-2 location. DECISION: always term-sense-gated** — a seat counts only when the seat-term's per-occurrence sense IS the seat; the English-word scan is removed; **if not clear → UNRESOLVED.**
- **C-3 & C-5 — the God items, consolidated. DECISION: state the ROLE, never yes/no** (yes/no is too crude and invites interpretation). All of God's involvement lives in **ONE** item — **"divine involvement (God's role)"** (item 8) — which states *how* God relates to the term: agent/subject · possessor · giver-source · object/recipient · addressee · none · UNRESOLVED. This **removes the duplication** the researcher spotted: origin no longer carries "bestowed-by-God" (that becomes `origin = received-from-outside` **+** `God's-role = giver-source`); "experiencer" states *who bears* the term, item 8 states *God's relation* — two different axes, each role-stated.
- **C-4 & C-6 — compound must state the role. DECISION: every compound row states the ROLE/pairing** of the co-term to the head term (not just the term's name). One co-term may hold more than one role (compound-partner AND object/cause) — each role is stated; never silently collapsed. **Researcher flag (anticipated):** compound may grow into its own VE item, or require an explicit head↔partner *pairing* field — to revisit next iteration.

## 6. Generation procedure (per verse)

1. **Read** the measure layer from the DB (`verse_morphology` + `lexicon`, §2; persisted M60 — no live STEP). 2. Resolve items in order (§3), each by its §4 rule, citing its measure. 3. Write one `ve_lexical` row per resolved value + per UNRESOLVED flag (present-only for NONE). 4. **Compose the narration** (the deterministic view) and **persist it as the single `l2_meaning` finding** per term-in-verse (M-cluster). 5. **Read-back audit (§6b)** — using the narration; record its result in the `lexical_note` item (§4e). 6. **On any change → reset and re-run the whole verse (P6)**, preserving `researcher` notes.

**Supersession is AUTOMATIC and built into the generator** (`scripts/_apply_generate_ve_lexical_v2.py`): on (re)generation each unit's old `ve_lexical` is **hard-replaced** (the items are deterministic + reproducible from the measure layer — the pre-run snapshot is the recovery path, so soft-delete would only bloat the table), and its prior `l2_meaning` finding is **SOFT-deleted** (findings are judgement artefacts — keep the audit trail). The narration finding always reflects the current `ve_lexical`. No stale findings or lexical items are left behind.

## 6b. Read-back audit — the closing loop (per verse)

After generation, read the items **back against the verse** and verify. **The audit reads the narration** (generated at step 4, *before* the audit) against the verse — the narration is the items "read back" in readable form, so it is the primary artefact for the *representative* (a) and *coverage* (c) checks. **The audit FLAGS only — it never silently injects or edits a value** (this keeps generation mechanical and every value traceable). It **writes its result into the `lexical_note` item** (§4e, `source=audit`). Each flag routes to: a rule/list improvement (→ whole-verse regen, P6) · an UNRESOLVED entry · or a researcher decision.

- **(a) Founded & representative.** *Founded* (**mechanical, every verse**): every stored item cites a present measure (P7); any item without a valid citation → flag. *Representative* (**judgement, sampled**): read the **narration** against the verse — does it faithfully carry the verse's inner-being content? PASS or flag. **Scope:** the representative judgement runs on a **sample / flagged verses only** — an interpretive read of all ~40k verses would rebuild the cost+drift the reform removed.
- **(b) Orphans / superseded** (**mechanical, every verse**): every active `ve_lexical` row for the verse must still trace to a live measure (term active, sense present, source not removed); rows that no longer trace → **soft-delete candidates**.
- **(c) Missing-but-relevant** (**mechanical coverage + small judgement, every verse**): enumerate the verse's tagged terms / content words (measure layer); each should be accounted for by ≥1 item (head · co-term · object · cause · modifier · location · …). Unaccounted → **coverage-gap note**. This is the **engine that surfaces new rules/list entries** — the systematised form of the manual verse-by-verse review.

**Convergence:** the coverage gaps and representative-flags feed rule/list refinement; the system is "done" for a cluster when an audit pass surfaces **no new** gaps (loop-until-dry).

## 7. Clarifications — ALL RESOLVED 2026-06-16

Q1–Q14 and the §5 conflicts C-1…C-6 are all decided (see the inline **[Qn RESOLVED]** marks). Two governing additions came out of the answers: the **expectation test** (P5 — silent = NONE, never impute; UNRESOLVED only when the verse signals a value is expected) and **every value carries an English equivalent** (P9).

**Remaining is build, not design** — assemble the rule-lists (seat-map Strong's→level · faculty lemma sets · origin cue lemmas · intensifier lemmas · term-inherent valence list · divine lemmas · directional/relational lemmas · object-type set) and the deterministic morphology readers (governing verb · subject/possessor · object · modifiers) over the measure layer. Then: build → dry-run → per-verse researcher review → live; whole-verse reset on any change (P6).

## 8. Emergent character — the debate (not yet an item)

- **For:** "perceiving the spiritual" (Luk 24:37) is a recurring inner-being capability; capturing it would let synthesis aggregate it.
- **Against (and the mechanical-only principle):** it is interpretive, not derivable from one verse's morphology — making it a VE item violates P1.
- **Proposed resolution (to debate):** it is **not** a VE item; it **emerges** from the mechanical items — `faculty=perception` **+** `N1 object-type=spiritual-being`. Ensure N1 carries `object-type=spiritual-being`, and let the **synthesis layer** detect the pattern → the characteristic. This honours P1 and still captures it. The researcher's view (errors came from not consulting the original language) supports this: strengthen the mechanical items, let characteristics emerge.

---

# Part B — original design analysis (v1, 2026-06-14, retained as rationale)

# L1/L2 fields — reliable measures, what's needed, expected answer

> **Investigation · v1 · 2026-06-14.** Records the discussion that reframed the L1/L2 reliability problem, then works through each of the 14 verse-extraction fields: *what it is · what is needed to arrive at the answer (its reliable measure[s]) · the expected answer.* Read-only design analysis; no DB change.

## 1. The discussion, recorded

**The impasse.** The study is a decompose strategy: whole (inner being) → pieces (words) → verses. The *decomposition* into structured per-verse facts held — where the verse-read ran, the findings are verse-resolved and trace back to a term + verse. What failed was the *re-composition*: pulling the pieces back into the full interdependent web of meaning, exhaustively and as generated prose. That web can't be held, traced both ways, and kept consistent by a single human or AI pass — the meaning paragraphs read well *because* they were narrated, not derived, which is exactly why they couldn't be traced back. The run was also too slow and costly to ever finish (≈5–7 h per cluster; 3 of ~46 done; M02's run never completed), with duplicated layers (1,224 term-in-verse units carrying both `l2_mechanical` and `l2_api`) and ~30k findings redone.

**The reframe (the key move).** "Sense" looked like an irreducible judgment — but deciding *pneuma* = wind vs Holy Spirit is done by **combining the node with other nodes in the verse** (the governing verb, the co-occurring terms, the setting). So **sense is not a property *of* the node — it is a property of the combination of nodes; it lives on the edges, not in the node.** That collapses the "mechanical facts vs interpretive meaning" split: **the meaning emerges from the web of facts.** Sense and the web are the same operation.

**The consequence — reliability = derivability from named measures = traceability.** A finding is reliable exactly to the degree it is **derived from named, present measures** (facts/nodes). When it is, the measures *are* the trace — you can show which facts forced the answer (*pneuma* = Holy-Spirit **because** of these nodes). That is the thing the generative meaning never had. The neighbourhood that decides a field is **local and bounded** (a verse / small passage), and **joint** (a node's sense and its neighbour's sense settle together) — so it is a *constraint problem over a small graph*, not narration of the whole web.

**The strata that fall out.** The 14 fields are not one thing. Each sits in one of four reliability strata by the *kind* of measure it needs:
- **Bedrock fact** — one mechanical signal (morphology, book, lexical structure). Definitive now.
- **Node-combination** — derived from the deciding node(s) present in the verse/passage. Reliable where the node is in reach; traceable to it.
- **Sense-dependent** — derived from the *resolved* sense, so only as reliable as the sense.
- **Out-of-reach residue** — needs the narrative/passage/canon beyond the local node-graph; the genuinely hard ones.

## 1b. Refinements (working session, 2026-06-14)

Four structural points emerged that change the table below:

- **A — a Precede ▸ Supersede key.** A field can have a *first-pass* answer from a cheap measure that a *later, better* measure refines. `morphology` precedes **type** (gives act/status/quality); `sense` then **supersedes** it (refines status-vs-quality). So each field names its inputs (precede) and what may overwrite it (supersede). This applies across the table, not just type.
- **B — predefined signal-lists ("words to look out for").** Several fields are driven by a **predefined dictionary of signal-nodes** — location (seat/body terms), origin (source-cue terms), **faculty** (faculty terms), attributed-to-God (divine-reference terms), relational-implication (directional terms). These are mechanical *lookups*, refined over iterations — not interpretation, not imputation.
- **C — compound is the web-edge generator.** Compound is **not** just "is the term lexically compound." It splits into **(i) term + T2 qualifier** (the "how") and **(ii) term + another T1 term**, and **auto-creates a compound stub for every co-occurring T1 term** in the verse. That is literally how the component-level web strings get built — and it absorbs the "co-occurrence" field floated earlier.
- **D — faculty is stated, not imputed.** A faculty surfaces **only** when the verse references one (directly — the term itself is a faculty-word; or indirectly — a faculty word co-occurs). It is **not** inferred from the term's general sense. `NONE`/silent otherwise.

## 1c. Cross-cutting additions (working session, 2026-06-14)

- **E — an `UNRESOLVED` state on every field.** Beyond a resolved value and a confident `NONE`/`SILENT` (signal legitimately absent), every field carries a third state — **`UNRESOLVED`**: *a signal was expected but the run could not find or decide it.* This is the **backtrack flag** — the set of `UNRESOLVED` findings is the worklist of "the mechanism hit a gap here," kept distinct from "there is genuinely nothing here." (The 38 content terms with no morph are `UNRESOLVED`-mode, not blank — a backfill worklist; a multi-sense term the read can't settle is `UNRESOLVED`-sense, not a guess.)
- **F — signal-LIST vs signal-RULES.** A predefined-signal field needs two things: the **signal-list** (the *vocabulary* — which words to look for) **and** the **signal-rules** (the *decision logic* — how to go from signals-present to an answer, including when to return `UNRESOLVED`). Faculty shows why: the list is the faculty-words, but a rule decides *direct* (the term itself is a faculty) vs *indirect* (a faculty word co-occurs) vs none vs unresolved.

## 1d. Signal-driven fields — list · rules · states

| field | signal-list (vocabulary) | signal-rules (decision logic) | states |
|---|---|---|---|
| **5 location** | seat: heart · soul · mind · spirit · conscience · **flesh** · body: eyes · ears · neck · shoulder · hand · lips · members · back | a listed seat/body word co-occurs → assign that level (multi); none present → `NONE`; a seat/body word present but its attachment to *this* term is unclear → `UNRESOLVED` | level(s) · `NONE` · `UNRESOLVED` |
| **6 origin** | give · pour · fill · grant · show (→ bestowed-by-God) · "from"+source (→ received) · self- · "own" · internal (→ within-person) | a source cue matches → its origin value; conflicting/partial cue → `UNRESOLVED`; no cue → `not-stated` | value · `not-stated` · `UNRESOLVED` |
| **7 faculty** | perception: see · hear · behold · eyes · ears · cognition: know · understand · consider · counsel · wisdom · memory: remember · forget · volition: will · choose · ask · affect: fear · joy · sorrow · longing · zeal · delight · moral-eval: justice · judge · search · conscience: conscience · guilt · integrity | **R1 direct** — the term's own gloss is a faculty → that faculty. **R2 indirect** — a faculty signal-word co-occurs and relates to the term → that faculty. **R3 multi** — assign every faculty with a present signal. **R4 unresolved** — a faculty context present but not attributable to a specific faculty → `UNRESOLVED`. **R5 none** — no signal (direct or indirect) → `NONE` (never imputed) | faculty(ies) · `NONE` · `UNRESOLVED` |
| **8 attributed-to-God** | Lord · LORD · God · Almighty · Holy One · Holy Spirit · YHWH · + a God-subject pronoun | the divine reference is the term's subject/possessor → `yes`; a divine word present but not the subject → `no`; the subject pronoun (he/you) can't be resolved to God or not → `UNRESOLVED` | `yes` · `no` · `UNRESOLVED` |
| **13 relational** | direction: to · toward · from · for · against · before · into · upon · verbs: give · show · serve · seek · deliver · call · choose · forsake · covenant | a directional/relational node attaches to the term → record its direction/relation (multi); present but unattachable → `UNRESOLVED`; none → `NONE` | relation(s) · `NONE` · `UNRESOLVED` |

> Signal-lists are **iteration 1** (seeded from `wa-l1l2-50complex-verses-working-set-20260614.md`) and grow with more verses. The **rules** are the stable decision logic; the **states** make every field auditable — the `UNRESOLVED` rows are the backtrack worklist.

## 1e. Is sense mechanical? — the grounded answer (resolves the confusion)

Sense is **not one reliability** — it is a spectrum, and **most of it is mechanical.** Measured over the 2,501 active clustered terms and their occurrences:

| stratum | share | how sense is got | reliability |
|---|---|---|---|
| **mono-sense term** (1 STEP subgloss) | **79% of occurrences** (6,659 terms) | assign the single subgloss | **fully mechanical** — no read |
| **poly-sense, STEP discriminates per occurrence** | most of the other 21% (370 terms) | **read STEP's PER-OCCURRENCE subgloss** — STEP already split it per verse (*nephesh* → life · person · appetite · myself · animal · …) | **mechanical field-lookup** — not a read |
| **poly-sense, STEP too coarse** | a minority of the 370 (theologically-loaded) | STEP's subgloss lumps distinct senses (*pneuma* "spirit" = Holy-Spirit **+** human spirit **+** wind) → needs a **signal-rule** (*pneuma* + "Holy"/"God" → Holy-Spirit) or the read | node-combination / read → else `UNRESOLVED` |
| **no STEP subgloss source** | 10 terms · 179 occ | nothing mechanical | `UNRESOLVED` until backfilled |

**The correction to the impasse.** The earlier mechanical layer's *"pneuma = wind/breath for all 312 verses (incl. Holy Spirit)"* was reading the term's **uniform gloss** ("spirit/breath") — **not** STEP's per-occurrence subgloss, which already splits `:spirit` (120) from `:breath` (4) per verse. STEP had disambiguated and the run ignored it. So sense is **substantially more mechanical than the impasse implied**: trivially for the mono-sense 79%, and as a field-read of the per-occurrence subgloss for the poly-sense terms STEP discriminates. The genuinely sense-dependent part is the **coarse-ceiling minority** (*pneuma*-type) — bounded, and addressable by **signal-rules** before any narrative read.

**So — yes, sense is the right next step after mode, and most of it is mechanical:** mode (bedrock) → **sense** (mostly mechanical from STEP's per-occurrence subgloss; rule/read only for the coarse residue) → then the sense-dependent fields (**type**, **faculty**) that supersede to it.

## 1f. The target — the 14 fields COMPOSE the meaning (2026-06-14)

This is where the field work is heading, and it **inverts the failed approach**:

- **Failed:** narrate the verse meaning as prose → it read well but couldn't be traced back (it was *narrated*, not *derived*).
- **Target:** derive the 14 fields mechanically (each a traceable finding) → **compose** them into a templated narrative sentence → the meaning is **back-trackable by construction** (every clause maps to a field → finding → verse) and **searchable** (the fields are structured, queryable across clusters and terms).

The meaning sentence is a **deterministic view of the findings, not a new authored artefact** — so it is verifiable (check each clause against its field), reproducible, and can never drift from its evidence.

**Example** (Psa 78:38, *chemah* "rage"):
> *In Psa 78:38, **chemah** (sense: rage) is a **status** (type), in **noun** form (mode), **attributed to God** who restrains it, directed **toward the people** (relational).*

Each clause ← one field ← one finding ← `(mti_term_id, verse_context_id)`.

**Three terminal states carry through per field:**
- **resolved** — a value, cited to its measure;
- **indeterminate** — the verse genuinely does not settle it: a *real finding* ("the text is unclear here"), not a gap;
- **pending** (`UNRESOLVED`) — the mechanism hasn't reached it; a worklist item, optionally resolved by reading the verse.

**Traceability chain** (every field value): source measure on `wa_verse_records` / `wa_verse_term_links` (keyed `mti_term_id` + `reference`) → `verse_context` (same key) → `finding` (`verse_context_id` + `mti_term_id` + catalogue question). The finding **cites** the measure, so it back-traces to the exact node that forced it — the thing the generated prose never had.

## 2. The 14 fields (refined)

> Per **typed term-in-verse**. "What's needed" names the **measure / predefined signal-list**. "Precede ▸ Supersede" is the dependency key. "Expected answer" is the value space.

| # | Field — what it is | What's needed (measure / signal-list) | Precede ▸ Supersede | Expected answer |
|---|---|---|---|---|
| **1** | **sense_applied** — which STEP sense the term carries here | **mechanical floor = STEP's per-occurrence subgloss** (mono → the one subgloss; poly → STEP's per-verse subgloss). Only the **coarse-ceiling residue** (*pneuma*-type) needs disambiguating neighbour-nodes or the read — *joint*. See §1e | ▸ inputs: STEP subgloss ▸ (residue) neighbour-nodes · supersedes: **type, faculty** depend on it | the STEP subgloss · refined sense for the residue · `UNRESOLVED` |
| **2** | **type** — act / status / quality | **morphology** (POS/form) gives the first answer | morphology ▸ **superseded by sense** (status-vs-quality) | `action · status · quality` |
| **3** | **compound** — what the term combines with here *(web-edge generator)* | **verse spans** (which T1/T2 terms co-occur) + **qualifier attachment** (which T2 modifies it). **Auto-creates a stub per co-occurring T1 term** | spans ▸ each T1 co-term spawns an edge-stub (→ reciprocal finding) | `{ lexical-parts · T2-qualifier(s) · T1-co-term(s) → one stub each }` |
| **4** | **mode** — the term's own grammatical realisation *(NOT compound)* | **morphology** (stem/binyan, voice, tense) | bedrock ▸ (none) | short form phrase (stem + voice) |
| **5** | **constitutional_location** — where located here | **predefined seat/body signal-list** (lev/heart · ruach/spirit · nephesh/soul · mind · **flesh** · conscience · organ terms) — surfaces on co-occurrence; silence = NONE; expected-but-unclear = UNRESOLVED | signal-list + spans ▸ (read may confirm) | `spirit · soul · heart · mind · flesh · other-soul:<x> · body-part:<x> · NONE · UNRESOLVED` (multi) — full spec §1d |
| **6** | **origin** — where it comes from | **predefined source-cue signal-list** (giving/sending verbs · divine-source markers · generational markers · internal-generation cues); absent ⇒ not-stated | signal-list ▸ (iterative tuning) | `within-person · received-from-outside · bestowed-by-God · carried-generationally · not-stated` |
| **7** | **faculty** — which faculty the verse *references* *(stated, not imputed)* | **predefined faculty-signal keyword-list** — direct (the term *is* a faculty-word) or indirect (a faculty word co-occurs). **Not** inferred from general sense. `NONE` if unreferenced | signal-list ▸ (none — *not* sense-imputed) | the 10 faculties · `NONE` (multi) |
| **8** | **attributed_to_God** — predicated of God here | **predefined divine-reference list** (God · LORD · YHWH · divine titles/pronouns · "of God"); i.e. the term's subject/possessor is a divine node | signal-list ▸ (none) | `yes · no` (+ how-note) |
| **9** | **purpose_equips** | **DEFERRED** — resolve the others first | — | purpose phrase · `not-stated` |
| **10** | **typology_direction** | **DEFERRED** — resolve the others first | — | `human→divine · divine→human · none` |
| **11** | **immediate_response** | **OPEN — needs more thinking** | — | response phrase · `SILENT` |
| **12** | **produces_effect** | **DEFERRED** — resolve the others first | — | effect phrase |
| **13** | **relational_implication** — directional/relational force | **predefined relational-signal list** (to · toward · from · for · against; give · receive · seek · extend; subject→object direction) | signal-list ▸ (none) | relational/directional phrase |
| **14** | **literary_setting** — *book-level, not per-verse* | the **book's genre** (book metadata — inherited, *not* extracted per verse); contextual setting (judicial/liturgical) may be passage-specific | inherited from book ▸ (none) | form (from book) + optional passage setting |

## 3. Strata (refined)

| Stratum | Fields | Reliability story |
|---|---|---|
| **Bedrock fact** | 2 type *(pre-sense)* · 4 mode · 14 literary-form *(book-inherited)* | definitive from one mechanical signal (morphology / book) |
| **Bedrock web-edge** | 3 compound — co-occurring T1/T2 from spans | the literal web strings; auto-generated |
| **Predefined signal-list** (node-combination by lookup) | 5 location · 6 origin · 7 faculty · 8 attributed-to-God · 13 relational | reliable where a listed signal-node is present; the node *is* the trace; tuned over iterations |
| **Joint neighbour-inference** | 1 sense | reliable where a deciding neighbour is in reach |
| **Deferred / open** | 9 purpose · 10 typology · 11 immediate-response · 12 produces-effect | not yet tackled (residue + needs-thinking) |

## 4. Notes

- **Resolution order** (from the Precede ▸ Supersede key): bedrock (2,4,14) and spans/compound (3) and the predefined-signal fields (5,6,7,8,13) need no read; **sense (1)** is the one joint inference; **sense then supersedes type (2)**; the deferred/open four (9–12) come last.
- **The trace is the deliverable.** Every non-bedrock finding must **cite the node(s) / signal that forced it** — that is the back-trackability the generative meaning lacked.
- **Compound builds the web.** Each co-occurring T1 term spawns a stub (reciprocal edge), so the web is assembled mechanically from the spans as a by-product of extraction — not narrated afterward.
- **Honest residue.** 9–12 are where no local-node measure settles it; flag them rather than let a generative step invent them.

---

# Part C — the COLLECTION layer (deep-dive extension) · v3 · 2026-06-24

> **Status:** added 2026-06-24 from the deep-dive refinement (M12 + the tamim/cleanness test + M13/M14/M16). Part A (per-verse VE) is unchanged and remains the mechanical base. Part C adds the **collection scope** — the lexical of a **term across its verses** — which is where the deep-dive understanding is captured **for re-use**. **This RESOLVES Part A §8** (emergent character): the kinds emerge from the mechanical items as `object_type`. Provenance + evidence: `outputs/markdown/validation/wa-lexical-extension-*` + `wa-lexical-discovery-register-v1`. Items marked **[prov]** are grounded on 1–2 clusters and confirm as more run. Tested on M12/M13/M14/M16 — the six object-types are **stable (no 7th needed)**; ~79–81% of collection values are mechanical (regenerate).

## C.1 Two scopes
- **Per-verse lexical** = Part A items (per term-in-verse), unchanged.
- **Collection lexical** = a term/unit **across its verses** (one record per owned term/sense-family). A value may be sourced from an **adjacent verse / the passage**, not only the head verse — **cite the source verse** (extends P7). Per-verse **silence is expected** (P5); the collection answers what no single verse does. **Group units by SEMANTIC SENSE, never by owning-registry** (registry = provenance, not meaning).

## C.2 `object_type` — the emergent kind (new universal collection item)
- **value space** {**characteristic** · **state/condition** · **expression** · **qualifier** · **identity** · **bivalent-faculty**} · **emergent — derived from per-verse-VARYING evidence + grammatical type**, NEVER from a lemma-constant (type/faculty as a per-verse claim — the M10/M11 validation failure).
- **RULE:** grammatical `type=status` + **valence varies across the term's verses** → state (or **bivalent-faculty** if a faculty is present and valence flips good/evil by verse — the **object devised/aimed-at IS the discriminator**); `how`-predicate of the person acting from a faculty → characteristic; `type=action` + a **binding** (manner-term / co-expressed characteristic) → expression; **always modifies a host** → qualifier; a **person-verdict** (object_type=person) → identity.
- **`asah`-deed override [prov]:** a status-POS noun governed by a do/commit verb (e.g. ne.va.lah "outrage", how=*asah*) → **expression**, not state (POS alone does not fix object_type).
- **A1 bearer-class sub-tag** {human-faculty · divine · object/thing/way}: human-faculty-bearer → characteristic; divine/object/way-bearer → **quality** (same lemma splits by bearer, read per verse — e.g. tamim "be blameless" vs "his way is perfect"; "foolishness of God"). Bivalence is **by bearer and by valence.**
- **A2 intrinsic-faculty escape:** a characteristic's REQUIRED faculty may be the lemma's **intrinsic faculty** declared once at collection scope (`derivation=intrinsic`) — **not** a per-verse seat claim (per-verse seat still needs co-seating evidence).
- **`membership_scope`** {lemma · per-occurrence}: a bivalent term is a **per-occurrence** member (it belongs to the cluster only at its relevant valence — the flip is the cluster boundary). [confirmed M14/M19/M20]
- **The object/aim IS the bivalent discriminator** (confirmed M14 scheming · M19 trust · M20 anxiety/doubt): for a bivalent-faculty the valence is set by *what it is aimed at* (trust in God→righteous vs in wealth/self→sinful). **Transitivity predicts bivalence:** a faculty that takes an object tends to be bivalent (the object-class sets valence); an intransitive disposition tends to be univalent.
- **states:** resolved / UNRESOLVED (never NONE — every analysed term has a kind).

## C.3 Type-conditioned expectedness (the LRT, made canonical)
P5's expectation test, **conditioned by object_type** — this is what makes a blank a *gap* vs a legitimate *silence*. Run the LRT (`scripts/_lexical_revelation_test_*`) per unit before conclusions.

| object_type | EXPECTED answers (empty-where-expected = LRT gap → locate/UNRESOLVED/remediation) |
|---|---|
| **characteristic** | faculty (REQUIRED; A2) · how-it-operates · directed-at-what *(only if `transitivity=transitive` — intransitive dispositions legitimately have object=NONE; transitivity confirmed load-bearing M19/M20)* · whose · intensity |
| **state/condition** | of-what (bearer) · who-set-it · **mutability** (can it change) · **transition-trigger** (what changes it) · valence-register · **realm** · pole-opposite |
| **expression** | the act · the **manner** · **what it expresses** (the bound characteristic) · acted-on-what · who-acts |
| **identity** | classified-as-what · **classifier** [prov] (who gives the verdict) · basis (← cause) · settled-or-reversible |
| **qualifier** | what-it-modifies (host) · the modification (un-X / intensify) · **of-what-property** [prov] · (never standalone) |
| **bivalent-faculty** | the faculty (neutral) · the per-occurrence **valence** (the discriminator) · what-directs-it (object/aim) |

## C.4 New collection items
- **mutability** {fixed · changeable · UNRESOLVED} — does any verse show the state set/removed/reversed (e.g. clean↔unclean, innocent↔guilty).
- **transition-trigger** (+ **`.manner`** sub-slot {inner · ceremonial/bound-rite · **juridical/forensic-covenantal** · **corrective/disciplinary** · **divine-affliction** · NONE}) — the act/agent that moves the bearer between the state and its pole; the manner sub-slot **homes the act-lemma how-gap** (a value, not a gap). [manner vocab extended from M13/M16]
- **binding** (extends Part A item 3 compound) — for an expression, the manner-term + the characteristic it expresses; **A5 — compound/binding is a per-verse role field** {partner · qualifier · object · cause · manner · expresses · seat · pole-opposite · unmarked} (replaces the coarse 94%-"partner" default — *this is a build prerequisite; the live field is still flat*).
- **pole-relation** — the term's inverse/axis-partner (within- or cross-cluster), from co-seating + cross-ownership. **Pole-paired clusters are assembled together** (M13↔M14, M12↔its-defilement-pole, M16↔M15).
- **realm** {ritual/bodily · inner/moral · **forensic/covenantal** · eschatological · **social/communal**} — a per-verse sub-register (generalises beyond states; vocab grows per cluster). [extended from M13/M16]
- **role-in-cluster** {member · pole-anchor · qualifier-import · **alien**} — lets a pole/leakage term (e.g. sha.qar "lie" owned in Truth) be retained as a *cited pole*, or a **provenance-intruder** (e.g. self-control/zeal mis-owned in Trust) be marked `alien` for route-out — without analysing either as a positive member. [confirmed M13/M19; `alien` added M19]
- **cognate-link** — a marker between the object-types of ONE lexical root: act/EXPRESSION ↔ resulting STATE ↔ IDENTITY (e.g. ba.tach "trust"-act ↔ be.tach "security"-state; the-fool ↔ folly). Generalises the person↔condition link. Not a new type — a relation between a root's units. [M16/M19]

## C.5 Re-run / regeneration (R1–R6, governing)
**R1** every collection value is tagged `derivation` {mechanical · read · researcher}: mechanical re-derives (regenerates), read/researcher are **preserved** (never overwritten — cf. §4e). Maximise the mechanical share (≈80% achieved). **R2** three reset scopes: per-verse (P6) → re-derive the term's collection layer; term change → re-derive across its verses; **model change → programme-wide migration**. **R3** stamp each value with `model_version`; a model change is a **re-assess-with-DIFF** (what reclassified), not a silent rewrite. **R4** re-running unchanged inputs at an unchanged model must be **idempotent** — a non-reproducible mechanical value is a **judgement leak** to fix (re-run = drift-detector). **R5** parked/old clusters (M01/M02/M07/M10/M11) re-enter via the **same pipeline** at the live model version. **R6** the LRT "fill-the-blank" recovery is a **rule** where possible (scan passage/bound term); only genuine reads are captured.

## C.6 Storage (in `ve_lexical`, at term scope)
The collection record is a set of `ve_lexical` rows at **term scope** (not verse scope), `ve_label` ∈ {`object_type`, `object_type.bearer`, `mutability`, `transition_trigger`, `transition_trigger.manner`, `realm`, `pole_relation`, `binding`, `classifier`, `role_in_cluster`, `membership_scope`, `transitivity`, `person_condition_link`}, each row carrying `value` (English per P9), `derivation` {mechanical·read·researcher}, `model_version`, and `source_ref` (the verse it was sourced from, incl. adjacency). Regenerable from the per-verse rows + the C.2–C.4 rules; `researcher` rows preserved (§4e lifecycle).

## C.7 Status & open items
- **Tested across SIX clusters:** M12 (full) + tamim/cleanness test + M13 Truth / M14 Deceit / M16 Folly / M19 Trust / M20 Doubt. Six object-types **stable (no 7th needed on any)**; **~79–81% mechanical** every cluster; A1–A5 confirmed; bivalent-faculty (object = the discriminator) + identity validated.
- **Firmed (multi-cluster):** transitivity (load-bearing — predicts bivalence) · membership_scope · role-in-cluster (+`alien`) · bivalent-object-discriminator · cognate-link · A4 realm generalises (vocab: ritual/inner/forensic/eschatological/social-communal) · A3 manner vocab (inner/ceremonial/juridical/corrective/divine-affliction).
- **Still [prov] (not yet exercised):** `classifier` (no identity unit appeared in M19/M20) · `asah`-deed override (not re-triggered since M16). Confirm when an identity/deed cluster runs.
- **Main build prerequisite:** the **enriched per-verse compound field (A5)** — live field still ~90% flat "partner"; needed for the binding-web.
- **Validates on an OLD cluster:** run on M20 (old 4 chars) the model held 3/4 and **split the 4th** (Doubt+Indecision → Doubt[trust-axis bivalent] + Perplexity[cognition, off-axis]) — evidence-derived structure refines the old.
- **Build path:** enrich compound (A5) → build the collection-lexical generator (`object_type` + C.4 items from the per-verse rows + cross-verse rules) → run across clusters → fold convergent [prov] items to firm.
