# Observation dimensions (D1–D13) — extract

- **File:** wa-observation-dimensions-extract-v1-20260701.md · **2026-07-01 · Author:** Claude Code.
- **Purpose:** a single working sheet of the inner-being observation dimensions — the schema each IB operation is described against.
- **Provenance / source of truth:**
  - **Definitions** (name · question · evidencing) are from `Workflow/methodology/wa-IB-verse-dimensions-definition-v2-20260629.md` (the authoritative doc). *The DB does not hold the dimension definition text — there is no `ib_dimension` table.*
  - **Live usage counts** are extracted from the DB table `ib_observation.dimension` (81 rows) as of 2026-07-01. This is where the dimensions are *in the DB* — as coded values against captured observations.
  - Catalogue companion: `Workflow/Catalogue/wa-IB-verse-dimensions-catalogue-v2-20260629.md`.

---

## 1. The dimensions

Each IB **operation** (one per fan-out track; a verse may hold several) is swept across all 13 dimensions. Each dimension value carries: **value** (or NONE / *silent*) · **status** · **provenance** · **basis**.

| # | dimension | the question — what it captures | how it is evidenced | DB obs |
|---|---|---|---|--:|
| **D1** | **Identity** | *what is the operation?* — the named inner-being movement | the span + lemma/sense + morphology | 10 |
| **D2** | **Source / antecedent** | *where does it come from?* — driver / cause / motive (incl. from context) | causal clause; the operation in a prior/context verse; the actor's prior state | 9 |
| **D3** | **Seat / bearer** | *where is it seated / who bears it?* — named seat (heart/soul/spirit) or the bearer | a seat lemma in-verse; else the grammatical subject (bearer) | 4 |
| **D4** | **Operation / action** | *what does it do?* — the act itself + its grammatical realisation | the predicate + **stem** (Qal=simple · Hiphil=causative · Piel=factitive) | 5 |
| **D5** | **Object / target** | *on whom / what?* — the patient / recipient | accusative / object marker / prepositional complement | 6 |
| **D6** | **Manner** | *how is it done?* — the qualifier on the operation | manner phrase / adverb / intensifier | 5 |
| **D7** | **Process / movement** | *how does it unfold / morph?* — the dynamic chain (incl. **emergence**: an operation that *grows* / escalates) | the sequence of operations/states; causative stems; result/sequence clauses; escalation across context verses | 7 |
| **D8** | **Impact / produced state** | *what does it produce?* — the effect/outcome state in the object | result clause; the produced-state verb (e.g. *marar* Piel = made bitter) | 7 |
| **D9** | **Coupling / relation** | *what binds with it HERE?* — the functional/grammatical binding within this operation's realisation (manner / partner / object-relation) | grammatical binding; tight in-verse co-occurrence | 5 |
| **D10** | **Colour / valence** | *moral register — WHERE EVIDENCED IN THE VERSE* (never imported) | term-inherent moral lemma; prohibition; the verse's framing | 6 |
| **D11** | **Discovery** | *anything the dimensions do not capture* (emergence) | the lookout — feeds new dimensions back | 6 |
| **D12** | **Hidden meaning** | *what latent / non-obvious IB implication does the verse carry?* | a deeper meaning to investigate further | 9 |
| **D13** | **Cohabitation** | *what other operations does this one keep company with — and what shared root does that company reveal?* | the recurring **cross-corpus co-occurrence** with other operations (the family it travels in); the **common root** the family points to, read off the accumulating verses | 2 |

**Completeness of an operation** = every dimension swept (a value, or marked *silent*) + D11 checked. **Complete ≠ resolved** — most values may be `needs-corroboration`.

---

## 2. Two boundaries that are easy to blur

### D9 Coupling vs D13 Cohabitation
- **D9 Coupling** = the **in-verse weld**: how this operation is structurally bound *here* (e.g. `be-perek` binds the Hiphil `abad` as its manner; a partner term).
- **D13 Cohabitation** = the **cross-corpus company**: which *other* operations this one habitually travels with (e.g. ruthlessness ↔ killing, exploitation of the weak), and what that company reveals about its **source**.
- They connect — the company (D13) often shares a deep root that is a kind of ultimate Source (D2) — but D2 is the *per-verse* antecedent, D9 is the *in-verse* weld, and D13 is the *corpus-wide family + its emergent root*.

### D13 — the root emerges, it is not imposed
Vices do not stand alone; they cohabit. Mapping the company a vice keeps is how the **shared root** surfaces — read off the verses as they accumulate, never asserted a priori. Assess D13 for **every** operation (virtues keep their own company toward their own root).

---

## 3. Value fields (per dimension value, as stored in `ib_observation`)

| field | column | allowed values (in live use) |
|---|---|---|
| **status** | `status` | `resolved` (56) · `needs-corroboration` (15) · `open` (8) · `silent` (2) |
| **provenance** | `provenance` | mechanical · researcher · fan-out · convergence · digested · claude-chat · logos · scholarship (and combinations, e.g. `researcher+fan-out`, `mechanical+digested`) |
| **basis** | `basis` | the citation / morphology / contributor the value rests on |
| anchor | `origin_verse` / `origin_verse_id` | the verse the operation is read from |
| unit | `operation` | the named IB operation (one per fan-out track) |

---

## 4. Live DB grounding (`ib_observation`, 81 rows, 2026-07-01)

- **Dimensions in use:** all D1–D13.
- **Origin verses captured:** Exo 1:13, Exo 1:14, Lev 25:43, Gen 6:5, Gen 6:6, Gen 49:7, Jer 17:9, Ecc 8:9, Mark 7:21-23.
- **Operations captured:** ruthlessness, enslavement, cruelty, dominion, evil, wickedness, fear-of-god, heart.
- **Status spread:** 56 resolved · 15 needs-corroboration · 8 open · 2 silent.

> Note the shape of the data: D1/D2/D12 are the most populated (identity, source, hidden meaning are swept early and richly); **D13 Cohabitation has only 2 observations** — it is the newest dimension (added v2, 2026-06-29) and the least developed. D3 (seat/bearer) is also thin (4).

---

## 5. Status of the dimension set

- The dimension set is **D1–D13** — a *starting, revisable* set. **D11 Discovery** keeps it open; **D13 Cohabitation** is the first dimension D11 produced.
- Definitions authoritative in the methodology doc (v2, 2026-06-29); live per-observation values in `ib_observation`.

Researcher comments
my aim is to add the dimensions to each verse lexicon.  The key difference between the prior work (arriving at observations) and what I intend, is that the dimension is part of the ve-lexical, and consist of the statement of pairs (using the span on both sides and the direction is always from 1 to 2); and events (processes, actions)
observations on these dimensions are as follows:

D1 - this is already captured in ve-lexical
D2 - the question should be: specify the source for each term: source -> term: this has three outcomes: span (source) -> span (primary term) or inferred (source) -> primary term or unknown -> primary term
D3 (seat/bearer), D4 (operation, ) , D5 (target) follows the same pattern, as well as D7,D8,
D6 - looks at the other span and pair the qaulifyer with the term
D10,D11,D12 - need more work, this may not be lexical level stuff and should not be assessed at verse level
D13 - is a verse level indicator
D14 (new) - package reference. This is to signal that the verse and lexical should be read with the adjacent verses.

observations about the ve-lexical:
the lexical must contain a set of data for each primary term in the verse, not only the owner-term. The concept of a term being dominant in a verse (owner term) and other primary terms being lesser significant is not sustainable.

Add the ve-lexical items (not the values) and their definition to this. I want to see what information is collected for each verse

---

## 6. The ve-lexical items — what is collected for each verse

> Added 2026-07-01 (CC) in response to the researcher comments above. This is **what the `ve_lexical` table actually collects per verse** — the *items* and their *definitions*, not their values.

### 6.1 How ve_lexical is structured
`ve_lexical` is the **items-in-verse-level** table. It is **normalised one row per value**: `verse_context_id · ve_nr · ve_label · related_tier · value · notes · source_provenance`. So a single verse-term carries **many rows** (one per item that resolved), and an item that recurs (e.g. two co-occurring terms under `compound`) is multiple rows. Total live rows: **507,651**.

- **Keyed to `verse_context_id`** — i.e. to a **term-in-verse** (`verse_context` is per term-occurrence). *This already spans every classified term-occurrence, not a single owner-term — see §6.4 re: your "each primary term" point.*
- **`source_provenance`** records the generator: the deterministic base is `v2_engine_iter1`; read-resolved values carry `*_read_api`; researcher notes carry `researcher`.
- **`related_tier`** carries the T-tier the value sits under (T0–T7); NONE/silent items are not stored (present-only).

### 6.2 The item catalogue (26 items live)
Definitions are from the canonical spec **01b-VE-field-reliability-and-rules.md** (items 0–21) and the reset lexical spec **wa-lexical-analysis-rules-reset-v1** §3 (the v2-engine functional items, 22–29). Counts are live from the DB, 2026-07-01.

| ve_nr | item (`ve_label`) | what it captures (definition) | spec | rows | verses |
|--:|---|---|---|--:|--:|
| 0 | **lexical_note** | a free-text note on the verse — **not a derived value**; written by the read-back audit (`source=audit`, regenerated) or by the researcher (`source=researcher`, preserved) | 01b §4e | 40,473 | 40,473 |
| 1 | **sense** | the per-occurrence sense the term carries here — the STEP subgloss (floor) + lemma medium_def, both in English | 01b §4a·1 | 40,473 | 40,473 |
| 2 | **type** | act / status / quality — from part-of-speech only (verb→action, noun→status, adjective→quality) | 01b §4a·2 | 40,473 | 40,473 |
| 3 | **compound** | each co-occurring tagged term **with its role** to the head (partner · qualifier-of · object-of · shares-seat …) — the web-edge generator | 01b §4a·3 | 82,151 | 32,500 |
| 5 | **location** | the constitutional seat the term is located in (heart · soul · spirit · mind · will · conscience · flesh · body-part) — sense-gated, never English-scan | 01b §4a·5 | 7,977 | 7,317 |
| 6 | **origin** | where it comes from — within-person · received-from-outside · carried-generationally · not-stated | 01b §4a·6 | 3,631 | 3,631 |
| 7 | **faculty** | which inner-being faculty/seat the verse **addresses** (presence observation, not a claim the term *is* a faculty) | 01b §4a·7 / reset §4 | 51,341 | 19,865 |
| 8 | **divine-involvement** | God's **role** relative to the term — agent · possessor · giver-source · object/recipient · addressee · none (states the role, never yes/no) | 01b §4a·8 | 21,266 | 21,264 |
| 11 | **immediate-response** | the inner being's immediate reaction — the coordinated/following finite verb after the term's clause | 01b §4c·11 | 6,637 | 6,637 |
| 13 | **relational** | directional/relational force → its object (`{direction → object}`) | 01b §4a·13 | 8,615 | 7,989 |
| 16 | **object** | the node the term acts on / toward — the governed object by morph (`translit "gloss"`) | 01b §4b·N1 | 20,617 | 20,617 |
| 16 | **object-type** | the *kind* of that object, observed — person · God · group · thing · abstract · spiritual-being | 01b §4b·N1 sub-rule | 20,068 | 20,068 |
| 17 | **cause** | the node that triggered the term — the eliciting subject / object-of-perception | 01b §4b·N2 / reset §3 | 10,022 | 10,022 |
| 18 | **how** | the governing predicate — the finite verb expressing how the term operates | 01b §4b·N3 | 16,437 | 16,437 |
| 19 | **intensity** | the manner / how-much — the intensifier or quantifier modifying the term (*me'od* "very", *kol* "all") | 01b §4b·N4 | 4,934 | 4,437 |
| 20 | **experiencer** | who bears the term — self · other-person · God · group · named (from the possessor/subject morph) | 01b §4b | 27,497 | 27,497 |
| 21 | **valence** | moral register where evidenced in the verse — righteous · sinful · commanded · forbidden · neutral | 01b §4b | 30,776 | 30,776 |
| 22 | **cause_clause** | the actual **causal-clause text** that supports the cause (the *ki* / *hoti/gar* clause recorded) — the evidence node behind item 17 | reset §3 (antecedent/cause measure) | 9,841 | 9,841 |
| 23 | **from-source** | the **source node** a received-from-outside operation comes *from* ("from God", "from the well") | reset §3 (direction/origin) | 8,852 | 7,394 |
| 24 | **instrument** | the **means/instrument** by which the operation is carried out (e.g. "sea", a tool) | reset §3 (argument role) | 715 | 650 |
| 25 | **purpose** | the **purpose/aim** the operation serves (the "in order to" phrase) — *(was excluded as lexical in 01b §4d; the v2 engine now captures a purpose phrase — confirm scope with the reset)* | reset §3 / 01b §4d (VE9) | 6,349 | 6,349 |
| 26 | **quality-bearer** | for a quality-type term, **whose/what** quality it is — the bearer ("gold", "food") | reset §3 (bearer role) | 2,092 | 2,092 |
| 27 | **operation** | the governing predicate as an **operation** verb (`lemma (Strong's)`, e.g. "took (H5493)") — the reset's naming of the "how it operates" edge | reset §3 (operation/how) | 634 | 634 |
| 28 | **isolable** | yes/**no** — is the verse's inner-being movement **self-contained**, or must it be read with adjacent verses (the adjacency-checker) | reset §3a (2026-06-25) | 5,406 | 5,406 |
| 29 | **discovery** | the mandatory **discovery-lookout** flag — what the current items do **not** capture (coverage-gap / emergence); "discovery: none" if nothing to flag | reset §5 | 40,374 | 40,374 |

### 6.3 Notes on the catalogue
- **Two provenance layers coexist.** Items **0–21** are the 01b core (Part A/B/C); items **22–29** are the reset **v2-engine functional edges** (all `source_provenance=v2_engine_iter1`). They were built in different iterations, so a few **overlap**: `cause` (17) ↔ `cause_clause` (22, its evidence text); `how` (18) ↔ `operation` (27, the reset's re-naming of the same governing-predicate edge). Worth deciding whether to converge these before building on them.
- **Coverage skew.** `sense`/`type`/`lexical_note`/`discovery` fire on ~40.4k verse-terms (near-universal); the functional edges are sparser and legitimately so (`instrument` 715, `operation` 634 — most verses have no instrument/operation). Sparse ≠ broken (expectation test P5).
- **Sub-attributes.** `object` (16) and `object-type` (16) share `ve_nr=16` — object-type is a sub-rule of object, stored as its own row.

### 6.4 On your comments (flagged, not yet acted)
- **"data for each primary term, not only the owner-term."** `ve_lexical` is keyed to `verse_context_id` = **each term-occurrence**, so structurally it is *not* owner-only — but whether every *primary* term in a verse currently has a full item-set (vs XREF/secondary terms being thin) is a **coverage question I have not yet verified**. Flagged as the first check when you take this up.
- **The reframe (dimensions as span→span pairs + events; D2–D8 as source→term, D6 qualifier-pairing, D13 verse-level, D14 package-reference).** Noted as **direction**, not yet built. Several of your intended pairs already have a home here: your D2 source→term ≈ `cause`+`cause_clause`+`from-source`; D4 operation ≈ `operation`/`how`; D5 target ≈ `object`; D6 qualifier ≈ `compound` role + `intensity`; D14 package-reference ≈ `isolable`/`read_with` (§6.2 item 28). This mapping is the natural next working step.

---

## 7. Storage — the database schema + example rows

> Added 2026-07-01 (CC). The captured data lives in **two** tables — `ve_lexical` (the item values) and `ib_observation` (the dimension observations) — both anchored on the term-in-verse row in `verse_context`. Schemas + 10 example rows each below. Row counts as of 2026-07-01.

### 7.1 Storage map
| what is captured | table | grain | anchor / key |
|---|---|---|---|
| the **ve-lexical items** (§6) — one value per row | `ve_lexical` (507,651 rows) | one row per resolved value | `verse_context_id` → `verse_context.id` |
| the **dimension observations** (§1) — D1–D13 | `ib_observation` (81 rows) | one row per operation × dimension | `origin_verse_id` + `term_anchor` (Strong's) |
| the **term-in-verse anchor** both hang off | `verse_context` (45,224 rows) | one row per classified term-occurrence | FKs → `wa_verse_records`, `mti_terms`, `verse_context_group` |

**The join runs through the master verse index (`verse`).** Both stores resolve to the canonical `verse` table (23,593 rows, one per verse):
- `ib_observation.origin_verse_id` → `verse.id` (populated 81/81).
- `ve_lexical.verse_context_id` → `verse_context.verse_record_id` → `wa_verse_records.verse_id` → `verse.id`.

So the dimension observations and the lexical items **are** joinable at the verse grain via the master index — e.g. `verse.id = 6542` (Exo 1:13) reaches both.

> ⚠ **Two caveats at the current verse-grain join (context only — see the planned direction below):**
> 1. **Grain differs.** `ve_lexical` is **per-term** (via `verse_context` → `mti_term`); `ib_observation` is **per-operation**, anchored by `term_anchor` = Strong's (text), not `mti_term_id`. A term-level join would need Strong's ↔ `mti_terms.strongs_number` reconciliation.
> 2. **A verse_id backfill gap — FIXED 2026-07-01.** `wa_verse_records.verse_id` had NULLs, but only **70 active** rows were affected (the rest soft-deleted legacy). Backfilled **66** active rows to the master `verse` index via `(book_id,chapter,verse_num)` — `scripts/_apply_backfill_verse_id_active_20260701.py` (DB backed up first; 0 FK orphans). Result: all **9** `ib_observation` verses now resolve into `ve_lexical` (was 8; Exo 1:13's 5 lexical rows now join). **4 rows remain blocked** — `2Sa 12:15`, `Deu 28:17`, `Deu 28:18`, `Gen 9:25` — because those verses are **not yet in the `verse` master index** (it holds 23,593 verses, not the full Bible); they need verse-morphology ingestion first. Root cause: fanout onboarding (2026-06-28) creates verse_records without `verse_id`.

### 7.5 Planned direction — `ib_observation` is transitional (researcher, 2026-07-01)
**`ib_observation` will not persist.** Once the new ve-lexical (the item model that carries the dimensions) is confirmed, the **current `ib_observation` entries will be converted into the new ve-lexical**, and the `ib_observation` table will then **cease to exist**. Sequence:

1. **Confirm** the new ve-lexical (dimensions as `ve_lexical` items — the span→span pairs + events per the researcher comments in §5).
2. **Convert** the 81 `ib_observation` rows into the new ve-lexical form (keyed on `verse_context_id`, at the correct grain).
3. **Retire** `ib_observation`.

**Consequence:** the two-store join caveats above are **moot** — no backfill/dedup of the `ib_observation`↔`ve_lexical` link is warranted, because `ib_observation` is being folded into `ve_lexical` and dropped, not maintained as a second store. The only linkage that matters going forward is `ve_lexical` → `verse_context` → master `verse` index, which is sound.

### 7.6 Integrity check — do XREF verses carry ve-lexical? (2026-07-01)
**Question (researcher):** only OWNER-term verses should carry ve-lexical; XREF verses should not — suspicion that some XREF verses have incomplete ve-lexicals.

**Finding — the rule holds for complete lexicals, but there is a confined contamination:**
- **Complete lexicals are OWNER-only.** 40,235 verse_contexts on OWNER + active verses carry the full sweep (avg **8.6** distinct items). No XREF verse carries a complete lexical.
- **BUT 106 inactive verse-records** (`wa_verse_records.delete_flagged=1` — the XREF/duplicate copies) **carry 187 stray ve_lexical rows.** Every one is the **`faculty` item (ve_nr 7) only** — 1 item each, no sense/type/sweep — and **all from a single run: `faculty-verse-explicit-v1-20260626`** (2026-06-26). That targeted faculty run wrote onto delete_flagged records the main v2-engine sweep skips. **Not systemic** — one field, one run.
- **Adjacent (not XREF):** 236 *active* verse_contexts have `NULL` `term_owner_type` but look complete (~9.7 items) — unlabeled terms (likely recent onboards), not contamination.

**Signals used:** OWNER/XREF via `wa_term_inventory.term_owner_type` (through `wa_verse_records.term_inv_id`) and the `wa_verse_records.delete_flagged` flag (XREF verses are delete_flagged). Diagnostic scripts under session scratchpad.

**Cleanup — APPLIED 2026-07-01.** Soft-deleted the 187 stray `faculty` rows (`scripts/_apply_cleanup_stray_ve_lexical_on_deleted_records_20260701.py`, DB backed up first). Verified: 0 active ve_lexical rows now sit on delete_flagged verse-records.

### 7.2 `ve_lexical` — the item store
**Schema**
| col | type | null? | default | notes |
|---|---|---|---|---|
| `id` | INTEGER | — | — | PK |
| `verse_context_id` | INTEGER | NOT NULL | — | **FK → `verse_context.id`** (the term-in-verse) |
| `ve_nr` | INTEGER | — | — | item number (0–29; see §6.2) |
| `ve_label` | TEXT | — | — | item name (`sense`, `faculty`, …) |
| `related_tier` | TEXT | — | — | T-tier the value sits under (T0–T7) |
| `value` | TEXT | — | — | the value, English per P9 |
| `notes` | TEXT | — | — | generation/read note |
| `source_provenance` | TEXT | — | — | `v2_engine_iter1` · `*_read_api` · `researcher` |
| `delete_flagged` | INTEGER | NOT NULL | 0 | soft-delete |
| `created_at` | TEXT | — | — | ISO-8601 |

**10 example rows** (one per varied item)
| id | vc_id | ve_nr | ve_label | tier | value | notes | prov |
|--:|--:|--:|---|---|---|---|---|
| 5008469 | 64479 | 1 | sense | T7.1.3 | crawl | set aside: crawl homonym | v2_engine_iter1 |
| 5008471 | 64479 | 3 | compound | T6.1.1 | che.mah "rage" → partner | set aside: crawl homonym | v2_engine_iter1 |
| 5008473 | 64479 | 7 | faculty | T3 | affect | set aside: crawl homonym | v2_engine_iter1 |
| 5008472 | 64479 | 16 | object | T1.1.4 | dust | set aside: crawl homonym | v2_engine_iter1 |
| 2726257 | 15208 | 16 | object-type | T1.1.4 | situation | resolved by read pass | object_type_read_api |
| 2351222 | 15145 | 17 | cause | T2.9.2 | the Lord's greatness above all gods | resolved by cause read | cause_read_api |
| 6332053 | 65029 | 18 | how | T1.4.1 | give (H5414) | governing verb; term=object | v2_engine_iter1 |
| 3101535 | 15071 | 21 | valence | T0.3.1 | sinful | resolved by read pass | valence_read_api |
| 6708922 | 35825 | 28 | isolable | — | no | opens with 'seek' (causal) | v2_engine_iter1 |
| 6708870 | 16561 | 29 | discovery | — | coverage-gap: Saul; command | mechanical lookout | v2_engine_iter1 |

### 7.3 `ib_observation` — the dimension store
**Schema**
| col | type | null? | default | notes |
|---|---|---|---|---|
| `id` | INTEGER | — | — | PK |
| `operation` | TEXT | — | — | the named IB operation (ruthlessness, cruelty…) |
| `dimension` | TEXT | — | — | D1–D13 |
| `narrative` | TEXT | — | — | the observation text |
| `term_anchor` | TEXT | NOT NULL | — | the Strong's the operation reads from |
| `origin_verse` | TEXT | — | — | verse reference (text) |
| `origin_verse_id` | INTEGER | — | — | verse id |
| `reconsider_at` | TEXT | — | — | revisit marker |
| `status` | TEXT | — | — | resolved · needs-corroboration · open · silent |
| `provenance` | TEXT | — | — | mechanical · researcher · fan-out · convergence · claude-chat … |
| `basis` | TEXT | — | — | the citation/morphology/contributor |
| `raw_file` | TEXT | — | — | source working file |
| `created` | TEXT | — | `datetime('now')` | timestamp |

**10 example rows**
| id | operation | dim | narrative (clipped) | term_anchor | origin_verse | status | prov | basis (clipped) |
|--:|---|---|---|---|---|---|---|---|
| 39 | ruthlessness | D1 | Ruthlessness (perek) is harsh, MERCILESS crushing of a weak… | H6531 | Exo 1:13 | resolved | mechanical | perek lemma; manner-noun |
| 40 | ruthlessness | D2 | It springs from the Egyptians' DREAD of a perceived threat… | H6531 | Exo 1:13 | resolved | researcher+fan-out | Exo 1:12 context; researcher |
| 41 | ruthlessness | D2 | Its restraint is the fear of God — not a narrow brake… | H6531 | Exo 1:13 | resolved | researcher+fan-out | 3-witness; most explicit cause |
| 42 | ruthlessness | D2 | The deeper wellspring of cruelty is the heart's evil… | H4284 | Exo 1:13 | resolved | researcher+fan-out | logos+claude — heart as source |
| 43 | cruelty | D2 | [Re-homed off Exo 1:13 2026-06-29: a CRUELTY-genus source…] | H7185 | Gen 49:7 | needs-corroboration | claude-chat | aph (H0639) anger-cruelty text |
| 44 | cruelty | D2 | [Re-homed off Exo 1:13 2026-06-29: a CRUELTY-genus source…] | H7980 | Ecc 8:9 | needs-corroboration | convergence | logos+claude — power-without… |
| 46 | ruthlessness | D3 | It is borne by the actor (the Egyptians); no inner seat… | H6531 | Exo 1:13 | silent | mechanical | no seat lemma in-verse |
| 47 | ruthlessness | D5 | Its object is always a weaker party (here Israel)… | H6531 | Exo 1:13 | resolved | researcher | the 6 perek verses concern rule |
| 48 | ruthlessness | D9 | It couples to enslavement as its MANNER (be-perek modifies…) | H6531 | Exo 1:13 | resolved | mechanical | morph: be-perek on HVhw3mp |
| 49 | ruthlessness | D10 | It is condemned — the Levitical law forbids ruling perek… | H6531 | Exo 1:13 | resolved | convergence | the 3 Leviticus prohibitions |

### 7.4 `verse_context` — the term-in-verse anchor
The row both stores hang off; also carries the L1/L2 classification fields. Key columns (full table has 24):

**Schema (selected)**
| col | type | null? | default | notes |
|---|---|---|---|---|
| `id` | INTEGER | — | — | PK — the `verse_context_id` in `ve_lexical` |
| `verse_record_id` | INTEGER | NOT NULL | — | FK → `wa_verse_records.id` (the verse+term) |
| `mti_term_id` | INTEGER | NOT NULL | — | FK → `mti_terms.id` (the Strong's term) |
| `group_id` | INTEGER | — | — | FK → `verse_context_group.id` |
| `cluster_subgroup_id` | INTEGER | — | — | FK → `cluster_subgroup.id` |
| `is_anchor` / `is_relevant` / `is_related` | INTEGER | NOT NULL | 0 | role flags |
| `analysis_note` | TEXT | — | — | the L1/L2 verse-read note |
| `keywords` | TEXT | — | — | JSON keyword array |
| `step_meaning_applied` | TEXT | — | — | the applied STEP sense |
| `pole` / `pole_is_metaphor` | TEXT/INT | — | — | pole classification |
| `thing_type` / `triage_status` | TEXT | — | — | triage |
| `meaning_provenance` | TEXT | — | — | `l2_refit` … |
| `sense_id` / `sense_multiplicity` / `step_envelope_note` / `residue_flag` / `set_aside_reason` / `flagged_for_review` / `delete_flagged` | mixed | — | — | supporting fields |

**10 example rows** (key columns)
| id | vrec | mti | anch | relv | analysis_note (clipped) | keywords (clipped) | step_meaning | triage | prov |
|--:|--:|--:|--:|--:|---|---|---|---|---|
| 21 | 203 | 12 | 0 | 1 | What humans exalt as admirable is an ab… | ["self justifying","pr… | abomination, someth… | ACCEPT | l2_refit |
| 22 | 206 | 12 | 0 | 1 | Entry into the holy city is barred to t… | ["purity required","ab… | abomination, someth… | ACCEPT | l2_refit |
| 23 | 204 | 12 | 0 | 1 | The golden cup full of abominations and… | ["corruption concealed"… | abomination, someth… | ACCEPT | l2_refit |
| 27 | 200 | 13 | 1 | 1 | Those called abominable profess knowled… | ["hypocrisy defining"… | detestable, abomina… | ACCEPT | l2_refit |
| 33 | 288 | 19 | 1 | 1 | Selfish rivalry is located in the heart… | — | selfish ambition, f… | ACCEPT | l2_refit |
| 34 | 283 | 19 | 0 | 1 | Self-seeking rivalry, rooted in the wil… | — | selfish ambition, f… | ACCEPT | l2_refit |
| 35 | 284 | 19 | 0 | 1 | Rivalry appears in a cluster of relatio… | — | selfish ambition, f… | ACCEPT | l2_refit |
| 36 | 285 | 19 | 0 | 1 | Rivalries are named as a work of the fl… | — | selfish ambition, f… | ACCEPT | l2_refit |
| 37 | 137865 | 19 | 0 | 1 | Selfish ambition here is the inner moti… | — | selfish ambition, f… | ACCEPT | l2_refit |
| 38 | 137866 | 19 | 0 | 1 | Selfish ambition is to be the ground of… | — | selfish ambition, f… | ACCEPT | l2_refit |

Researcher comments 1

there is lots of room for confusion on verse data. and we first need to step by step work through it - so do not run away.

first confirm the base line.  The lowest unit of measure (row) is a ve-id in the term_index within the verse_record_id. A vcerse_record_id can have, and is highly likely to have multiple term_index and each term_index could have any number of the ve-catalogue ids of 1-29

Confirming your statement clause by clause
"The lowest unit (row) is a ve-id in the term within the verse..." — ✅ Yes. The lowest row is a ve_lexical row (one ve-catalogue value), sitting on a term.

"A verse_record_id can have multiple term_index" — ⚠️ Naming correction. A verse_record_id (a wa_verse_records row) IS one term — it cannot hold multiple terms. The thing that holds multiple terms is the verse (reference / verse_id). So the sentence is true if you read it as "a verse has multiple terms" — confirmed, 1–16 per verse. verse_record_id = the term level, not the verse level.

"each term could have any number of the ve-catalogue ids 1-29" — ✅ Yes, with two notes: the range is 0–29 (item 0 = lexical_note exists), and a single ve_nr can repeat on one term (e.g. two compound rows). Worked example — 1Ch 16:25 has 2 terms: feared (H3372) → 14 ve_lexical rows across 12 items; praised (H1984) → 13 rows across 10 items.

The corrected baseline (one line)
verse (reference/verse_id) → term-in-verse (wa_verse_records, one row per term) → classification anchor (verse_context, ~1:1) → ve-item value (ve_lexical, many per term, ve_nr 0–29).

The one nuance to hold onto: ve_lexical doesn't hang off wa_verse_records directly — it hangs off verse_context, which is the ~1:1 per-term twin of wa_verse_records. So there are effectively two term-level rows (the measure row wa_verse_records and the anchor row verse_context).

Want me to record this confirmed baseline into the doc (a short §8) so it's the written reference before we take the next step?

Researcher comments 2

ve-id->verse_record_id"A verse_record_id can have multiple term_index" — ⚠️ Naming correction. A verse_record_id (a wa_verse_records row) IS one term — it cannot hold multiple terms. The thing that holds multiple terms is the verse (reference / verse_id). So the sentence is true if you read it as "a verse has multiple terms" — confirmed, 1–16 per verse. verse_record_id = the term level, not the verse level.

ve-id -> term_id -
---

## 7.7 Baseline verification (a–d, 2026-07-01)

Researcher-requested checks against the DB.

**(a) Chain + cardinality — CONFIRMED (with naming).** Live example: `ve_id 2351222 → verse_context 15145 → verse_record 60883 → verse_id 84 (1Ch 16:25)`, term `mti=298` consistent on both. Corrected chain: **`ve_lexical (ve-id) → verse_context (the term-in-verse "index") → wa_verse_records (verse_record_id, per-term) → verse_id (the verse)`**. A `verse_id` carries multiple terms (1–16); *only OWNER-term contexts carry ve-lexical* — confirmed (§7.6, and (c) below).

**(b) The 4 blocked verses — all `arar` (H0779) fanout onboards.** `2Sa 12:15`, `Deu 28:17`, `Deu 28:18`, `Gen 9:25` each carry the recently-onboarded term **H0779 (arar, "curse")**, `verse_id` NULL, and **0 ve_lexical rows** (not yet analysed). None are in the `verse` master index (not by reference nor by book/ch/vs) — the verses were never ingested into the measure layer. **Fix = ingest these 4 verses** (`scripts/_apply_ingest_verse_morphology.py`) → then verse_id fills and lexical can generate. Low urgency (no lexical hangs on them yet).

**(c) OWNER/XREF + term identity.**
- Post-cleanup: ve-lexical-bearing verse_contexts = **40,235 OWNER + 236 (null owner_type), 0 XREF, 0 on delete_flagged.** Clean.
- **Term identity** (`verse_context.mti_term_id` vs `wa_verse_records.mti_term_id`): **40,463 of 40,471 agree; 8 mismatch** — all homonym sub-entries (`H2803I/J`, `H3772H`) at `2Ch 21:7`, `Isa 29:17`, `Psa 40:17`, `41:7`, `52:2`. A tiny grounding inconsistency (likely OT-DBR-009 mti dedup); flagged, not fixed.

**(d) Anchor — NOT universal.** Of ve-lexical-bearing OWNER-active contexts: `is_anchor=1` = **3,934**, `is_anchor=0` = **36,301**. Of **2,185** OWNER terms carrying ve-lexical, **273 have no `is_anchor=1` verse_context at all.** So "each owner term has an anchor verse" does **not** hold today. ⚠ Open question: is `is_anchor` still load-bearing under the fanout model, or a legacy of the verse_context_group era? Needs a researcher decision before treating the 273 as a defect.

> **The D1–D14 → ve-lexical catalogue design** (item e) is in [wa-ve-lexical-dimension-catalogue-design-v1-20260701.md](wa-ve-lexical-dimension-catalogue-design-v1-20260701.md).
