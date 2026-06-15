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
