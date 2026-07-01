# ve-lexical dimension catalogue — design proposal (D1–D14 as ve-lexical items)

- **File:** wa-ve-lexical-dimension-catalogue-design-v1-20260701.md · **2026-07-01 · Author:** Claude Code · **status: DRAFT for researcher review.**
- **Purpose:** design how the observation dimensions **D1–D14** become **ve-lexical catalogue items** — so the dimension is *part of the ve-lexical* (not a separate `ib_observation` table). Implements the researcher's direction (extract doc §5, §7.5) and the confirmed baseline (extract doc §8 / §7).
- **Companion:** [wa-observation-dimensions-extract-v1-20260701.md](wa-observation-dimensions-extract-v1-20260701.md) — dimensions (§1), current ve-lexical items (§6), storage schema (§7), baseline (§7 verify).

---

## 1. The model — PAIRS and EVENTS

Per the researcher: a dimension is captured as a **statement of a pair** (two spans, a **direction always read 1→2**) or an **event** (a process / action). Formalised:

- **PAIR item** — an ordered edge `element1 → element2` between two things in the verse. **The primary TERM is the hub**; each dimension attaches its counterpart to the term by a directed edge. Every pair carries a **resolution** (below).
- **EVENT item** — a process/action value (a predicate, or a chain of predicates/states), not a two-node edge. Used where the dimension *is* a movement (operation, process).
- **Resolution of a pair** (generalises the researcher's three D2 outcomes) — the state of `element1`:
  - **`span`** — element1 is an actual span in the verse (`span(source) → span(term)`). *strongest.*
  - **`inferred`** — element1 is not in the verse but is deduced (`inferred(source) → term`).
  - **`unknown`** — element1 cannot be determined (`unknown → term`). *the open worklist.*
  - (plus **`none/silent`** — the verse genuinely has no such element; expectation test P5.)

> **Direction convention — the one decision to confirm.** The researcher's rule is *"direction is always 1→2."* Two readings:
> - **(A) Uniform "counterpart → term"** — slot1 = the dimension's counterpart, slot2 = the term, for *every* dimension (matches the D2 spec literally; the term is always slot2, the hub).
> - **(B) Semantic flow** — slot1→slot2 follows meaning: **into** the term for source/seat/operation/process (cause→term), **out of** the term for target/effect (term→object). D2/D3/D4/D7 point in; D5/D8 point out.
>
> Recommendation: **(B) semantic flow**, because it keeps the arrow meaningful (`cause → term`, `term → object`) and the "always 1→2" rule is preserved *within each dimension's fixed slot definition*. Flagged for your call — it drives the column semantics below.

---

## 2. Span identity (what a "span" is)
A **span** = one or more original-language words in the verse. The measure layer already holds them: `verse_morphology` (one row per word: surface · strongs · morph · position) under the master `verse`. A span reference is therefore a **(verse_id, word-position range)** — or the `verse_morphology.id`(s). The primary term's own span is the anchor; the counterpart span is another word/phrase in the same verse (or, for `inferred`, none).

---

## 3. The catalogue — D1–D14 → ve-lexical items

Legend: **shape** = PAIR / EVENT / FLAG · **reuse** = maps to an existing `ve_label` (extract §6.2) or **NEW**.

| dim | item / `ve_label` | shape | slot1 (from) | slot2 (to) | reuse of existing | notes |
|---|---|---|---|---|---|---|
| **D1** Identity | `sense` + `type` (+ term span) | (base) | — | — | `sense`(1), `type`(2) | already in ve-lexical; the term itself is the hub, no edge |
| **D2** Source | `source` | PAIR | source span | **term** | `cause`(17)+`cause_clause`(22)+`from-source`(23) | the 3 resolutions live here (span/inferred/unknown); **converge 17+22+23** |
| **D3** Seat/bearer | `seat` + `bearer` | PAIR | seat span / bearer span | **term** | `location`(5)=seat, `experiencer`(20)=bearer | two edges: seat (heart/soul…) and bearer (who) |
| **D4** Operation | `operation` | EVENT | — (the predicate) | **term** | `operation`(27)/`how`(18) | the governing verb; **converge 18+27**; event, not pair |
| **D5** Target | `target` | PAIR | **term** | target span | `object`(16)+`object-type`(16) | edge points OUT of the term (semantic-flow reading) |
| **D6** Manner | `manner` | PAIR | qualifier span | **term** | `intensity`(19)+`compound`-qualifier-role(3) | pair the qualifier/adverb span with the term |
| **D7** Process | `process` | EVENT | — (the chain) | **term** | **NEW** (reset "transition/becomes") | the movement/escalation chain; may span adjacent verses (→ D14) |
| **D8** Impact | `effect` | PAIR | **term** | effect span | `immediate-response`(11) + produces-effect | edge OUT of the term to the produced state |
| **D9** Coupling | `coupling` | PAIR | co-term span | **term** | `compound`(3) with role | the in-verse weld (partner/qualifier/object role) |
| **D10** Valence | `valence` | FLAG | — | (term) | `valence`(21) | **researcher: needs more work; may not be lexical-level** — keep as the existing flag, do not force into a pair |
| **D11** Discovery | `discovery` | FLAG | — | (verse) | `discovery`(29) | lookout; already a flag; **not a per-term pair** |
| **D12** Hidden meaning | — | — | — | — | (none) | **researcher: not lexical-level / not verse-level** — PARK; do not add a lexical item |
| **D13** Cohabitation | `cohabitation` | FLAG (verse-level) | — | verse/term | **NEW** (verse-level) | **researcher: a verse-level indicator** — cross-corpus family; computed across the corpus, not a per-verse span-pair |
| **D14** Package-ref | `read_with` (+`isolable`) | FLAG | verse | adjacent verse(s) | `isolable`(28) + `read_with` | **already exists** (extract §6.2 item 28) — signals read-with-adjacent; confirm it satisfies D14 |

### 3a. Consequences of the mapping
- **Three convergences to do first** (extract §6.3): D2 folds `cause`+`cause_clause`+`from-source`; D4 folds `how`+`operation`; D5 keeps `object`+`object-type`. These duplications must be resolved before the pair model is clean.
- **Two genuinely NEW items:** `process` (D7) and `cohabitation` (D13). Everything else **reuses** an existing `ve_label`.
- **D12 is dropped** from the lexical catalogue (researcher: not lexical-level). **D10/D11** stay as flags, not pairs. **D14 already exists** as `isolable`/`read_with`.
- So the "additional catalogue items" are modest: **enrich existing items into the pair shape + add 2 new + retire the D2/D4 duplicates.** Not a rebuild.

---

## 4. Storage design — how a pair is stored

Current `ve_lexical` (extract §7.2): `verse_context_id · ve_nr · ve_label · related_tier · value · notes · source_provenance`. It stores a **single flat value** — it cannot express a directed span-pair. Options:

- **Option A — encode in `value`** (`"span_a → span_b"`, resolution in `notes`). Cheapest; **not queryable**; rejected for a first-class pair model.
- **Option B — add columns to `ve_lexical`** (recommended):
  | new column | holds |
  |---|---|
  | `from_span` | verse_morphology position-range of element1 (NULL if inferred/unknown) |
  | `to_span` | position-range of element2 (the term span) |
  | `direction` | `1to2` (fixed) — reserved for future |
  | `resolution` | `span` \| `inferred` \| `unknown` \| `none` |
  | `pair_kind` | `pair` \| `event` \| `flag` |
  The existing `value` still carries the readable English (P9: "dread → ruthlessness"). Regenerable, single table.
- **Option C — child table `ve_lexical_pair`** (`ve_lexical_id · from_span · to_span · resolution`). Fully normalised; more joins. Prefer B unless a pair can hold >2 nodes.

**Recommended: Option B.** It makes the pair queryable, keeps one table, and the span refs tie every dimension value back to the measure layer (the trace).

---

## 5. What is NOT in this catalogue (researcher directions honoured)
- **D12 Hidden meaning** — not a lexical item (may not be lexical-level). Revisit at synthesis, not verse-lexical.
- **D10 Valence, D11 Discovery** — kept as flags (existing), **not** forced into the pair shape; D10 "needs more work."
- **D13 Cohabitation** — a **verse-level / cross-corpus** indicator, computed from the accumulated corpus, not a per-verse span-pair. Store as a verse/term-level flag, populated by a corpus pass.

---

## 6. Open decisions for the researcher (before build)
1. **Direction convention** — confirm (A) uniform counterpart→term vs (B) semantic flow (§1). *Recommend B.*
2. **Storage** — confirm Option B (columns on `ve_lexical`) vs C (child table) (§4). *Recommend B.*
3. **Convergences** — approve folding `cause`+`cause_clause`+`from-source`→`source` (D2) and `how`+`operation`→`operation` (D4).
4. **D14** — confirm the existing `isolable`/`read_with` satisfies "package reference," or whether a distinct `package_ref` is wanted.
5. **`ve_nr` allocation** — assign numbers to the 2 new items (`process`, `cohabitation`) and the renamed `source`/`target`/`seat`/`bearer`/`manner`/`effect`/`coupling` (or keep old numbers and just add the pair columns).

Once these are settled, the build is: **add the pair columns → converge the duplicate items → add `process`/`cohabitation` → convert the 81 `ib_observation` rows into this shape → retire `ib_observation`** (extract §7.5).

Comments
1 - direction convention - semantic
5 - d12 hidden, not a ve-lexical item
5 - d10 I am not sure what value valence provide, it seems to me to be a AI interpreted element thas often was not based on the evidence
5 - d11 keep for special notes when verse is read and something is detected that may need further research
5 d13 - this is implicit in the multi-term in verse principle, drop

6 1 see above
6 2 columns on ve-lexical
6 3 each pairs convergence rules must be set individually, the same rule does not apply for every pair.
6 4 ve-lexical for a passage is considered on passage level, not on verse level, expecting only on verse in passage to have lexical
6 5. add 2 new numbers, keep old.  make sure that the old number and the new pair delivers the same result. 

Note that some lexical items is related to specific terms, others are verse wide.

check if the current ve-lexical data structure actually handles this - I would not be surprise if the record structure need to pivot.

backtrack to test that the completed set of lexical items will provide all the data needed from the verse to perform a cross verse synthesis for verse with common features.


fundamentally the process work as follows

select verse, is it part of a passage, handle it as a passage, if passage select 1 first of the passage, if selected verse is 1 verse of passage proceed, else skip, cross referencing the selected verse to the passage. Proceed to analyse verse morphology - isolate all terms that will require lexical, perform the full lexical analysis.
---

## 7. Researcher comments RESOLVED + deep-review findings (2026-07-01, tested against data)

### 7.1 Decisions locked in (from the comments)
- **Direction = SEMANTIC** (B). ✔
- **Storage = columns on `ve_lexical`** (Option B). ✔
- **D12 Hidden** — not a ve-lexical item. Dropped. ✔
- **D10 Valence — DROP** (data-confirmed, see 7.2). ✔
- **D11 Discovery — KEEP** as a special-notes channel: when a verse is read and something is detected that may need further research. ✔ (a note, not a pair)
- **D13 Cohabitation — DROP**: it is *implicit in the multi-term-in-verse principle* (a verse already holds its co-occurring terms). No separate item. ✔
- **Convergence rules are PER-PAIR** — each old→new convergence (D2's cause+cause_clause+from-source; D4's how+operation) gets its **own** rule; no blanket rule. And each new pair item must **reproduce the old item's result** (convergence-validation gate).
- **`ve_nr`: keep old numbers, add new.** With D13 dropped, only **`process` (D7)** is genuinely new — *is a 2nd new slot still wanted, or was that for D13?* (open Q).
- **Passage lexical is at PASSAGE level** — only the **first verse** of a passage carries the lexical (matches the passage layer just built).

### 7.2 D10 Valence — tested: DROP is justified
`ve_lexical` valence = **30,776 rows, 99.3% `valence_read_api` (AI-interpreted)**, only 205 mechanical — **and all 30,776 are already soft-deleted.** So valence is interpretation, not evidence, and was already removed. Confirms the researcher's read. *(At most, keep the 205 mechanical prohibition-particle detections as a narrow signal; do not carry AI-valence.)*

### 7.3 ★ STRUCTURE PIVOT — CONFIRMED NEEDED (the researcher's prediction)
> *"check if the current ve-lexical data structure actually handles this — I would not be surprised if the record structure need to pivot."*

**It does not handle it — a pivot is needed.** `ve_lexical` is keyed **only** to `verse_context` (per-term). But verse-level items are stored **redundantly per-term-context**:
- `isolable` — on 2,775 verses; **1,445 carry it on >1 term_context** (same verse-level fact repeated per term; e.g. 1Ch 16:41 = 3 copies).
- `discovery` — on 19,128 verses; **10,862 on >1 term_context.**

So today a verse-level fact is duplicated across a verse's terms. **The pivot:** `ve_lexical` needs a **verse-level tier** — rows keyed to the **verse** (term-independent), alongside the per-term rows. Options: (i) a `scope` column {verse|term} with `verse_id` set and `verse_context_id` NULL for verse-level rows; (ii) a separate `verse_lexical` table for verse-level elements. This is the record-structure pivot to design before the D1–D14 build.

**So the lexical has two tiers:** **per-term** (D1 sense/type, D2 source, D3 seat/bearer, D4 operation, D5 target, D6 manner, D7 process, D8 effect, D9 coupling) and **verse-level** (isolable/passage = D14, discovery = D11). Passage sits above both (passage-level, on the first verse).

### 7.4 The processing algorithm (researcher-stated, for the record)
1. **Select verse.** Is it part of a **passage**? If yes → handle as a passage: take the **first verse** of the passage. If the selected verse **is** the first verse → proceed; **else skip** (cross-reference the selected verse to the passage).
2. **Analyse verse morphology** → isolate all spans that require lexical (the span-completeness pre-pass, `wa-span-completeness-prepass-v1`).
3. **Perform the full lexical analysis** on that term-list.

### 7.5 Further questions / clarifications for the researcher
1. **2nd new `ve_nr`** — with D13 dropped, is only `process` (D7) new, or is a 2nd slot still wanted?
2. **Verse-level tier shape** — `scope` column on `ve_lexical` (i) vs a separate `verse_lexical` table (ii)? (7.3)
3. **D9 vs D13** — with D13 dropped as "implicit in multi-term," does **D9 Coupling** (the in-verse weld) also fold into the multi-term principle, or stay as an explicit pair? (they overlap.)
4. **Convergence-validation** — for each old→new pair, do you want a diff report (old value vs new-pair value) before retiring the old item?
5. **Backtrack test** (your note) — "does the completed lexical-item set provide everything for cross-verse synthesis of verses with common features?" — I propose a concrete check: pick 2–3 verses sharing a feature and confirm the item-set reconstructs the shared meaning. Confirm you want this run as the validation gate.
