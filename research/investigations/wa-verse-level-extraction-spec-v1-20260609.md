# Verse-level extraction spec — what to tease out of each verse that feeds the tiers

> **Design · v1 · 2026-06-09 · CC.** Researcher review of the catalogue against verse-level analysis
> (`Workflow/Tiers/wa-tier-questions-extract-v1-20260604.md`). **Core finding: the catalogue (T0–T7) is
> written for *characteristic-level synthesis* — every question says "this characteristic" — and does not
> suit verse-level analysis; but the verse level *feeds* the tiers.** So we define a **verse-level extraction
> record**: structured fields per typed-term-in-verse, with **explicit option-lists**, that roll up into the
> tiers. The current L2 extracts only 4–5 of these. **Proposal for researcher review.**

---

## 1. Principle
- **Catalogue tiers = the synthesis target** (characteristic-level, interpretive, the roll-up).
- **Verse-extraction record = the evidence** (per typed-term-in-verse, structured, with option-lists).
- The L2 **read produces the extraction record**; the mechanical pass pre-fills what it can; the **tiers are
  computed by rolling the records up**. We do **not** ask the characteristic-level question at the verse — we
  extract the verse fields that *feed* it.

## 2. The verse-level extraction record (per typed-term-in-verse)
Researcher-flagged verse-feedable questions → fields. **M** = mechanical (L1/morph/lexical) · **R** = read.

| # | field | option-list / format | feeds tier(s) | M/R | L2 now |
|---|---|---|---|---|---|
| 1 | **sense_applied** | the verse-specific sense (clean) | T1.1.2 · T7.1.3 | M | ✓ (raw, needs clean) |
| 2 | **type** | `action · status · quality` | T1.2.1 | M | ✓ |
| 3 | **compound** | `simple` · `compound:<parts>` | T1.2.2 | R | ✗ |
| 4 | **mode** | the stem / contextual mode | T1.4.2 | M | ✓ |
| 5 | **constitutional_location** *(multi)* | `spirit · soul · heart · mind · will · conscience · other-soul:<x> · body-part:<x> · NONE` | T2.1–T2.8 (.1 located? / .3 silent) | M-keyword + R | partial (body only) |
| 6 | **origin** *(the fix)* | `within-person · received-from-outside · bestowed-by-God · carried-generationally · **from-other-spirits** · not-stated` | T2.9 | R | ✗ |
| 7 | **faculty** *(the T3 restructure, multi)* | `perception · cognition · memory · affect · creativity · volition · agency · moral-evaluation · conscience · relational · NONE` | T3.x.1 | R (per-term from meaning) | partial (M01 only, induced) |
| 8 | **attributed_to_God** | `yes · no` (+ note) | T0.1.2 / T0.1.3 | R | ✗ |
| 9 | **purpose_equips** | text — what it equips the person to be/do/become | T0.2.1 | R | ✗ |
| 10 | **typology_direction** | `human→divine · divine→human · none` | T0.4.2 | R | ✗ |
| 11 | **immediate_response** | text · `SILENT` | T1.5.1 / T1.5.3 | R | ✗ |
| 12 | **produces_effect** | text — what it produces | T1.6.1 (→ also seeds T5/T6) | R | ✗ |
| 13 | **directional_relational_implication** | text | T1.1.3 | R | ✗ |

## 3. The three structural fixes (from the review)
1. **Origin (field 6) = an explicit checklist, and ADD `from-other-spirits`.** The current T2.9.1 lists only
   *within / from-outside / from-God / generational* — **spiritual-being origin is excluded and must be
   included** (angelic/adversarial influence is a real constitutional source; cf. T4.6 exists at characteristic
   level but origin-from-spirits was missing). Naming origins as an explicit list also makes the field
   answerable + auditable, not open prose.
2. **Faculty (field 7) = restructure T3.** The catalogue's 11 faculties × 3 questions (33) collapse to **one
   verse field: which faculty(ies) this term engages**, a multi-select from the 11, **derived per-term from
   the lexical meaning** (not per-cluster — fixes the induction, [[feedback_faculty_must_be_per_term_not_per_cluster]]).
   The "enable/deepen/bypass/impair" (T3.x.2) and "what it reveals" (T3.x.3) are **roll-up/read**, not verse fields.
3. **Location (field 5) = explicit list across ALL constitutional levels**, not just body — the T2.X.1
   "located at X?" series becomes one multi-select location field; T2.X.3 silence = `NONE`.

## 4. What this means for L2
- **The L2 read's job is to produce the extraction record (fields 1–13)** — not just resolve the lexical
  shade. The mechanical pass pre-fills 1,2,4 (and 5 by keyword); the **read fills 3,6,8–13 and confirms 5,7**.
- **Option-list fields** (type, location, origin, faculty, typology) are **closed vocabularies** → auditable,
  state-not-induce friendly (`not-stated`/`NONE`/`SILENT` are first-class, never guessed).
- **The mechanical-vs-API triage refines:** simple verses where the read adds nothing beyond the mechanical
  pre-fill = ACCEPT; verses needing the read fields (purpose, response, produces, origin, God-attribution) =
  the read. So the *extraction record defines what the read must deliver*.
- **Tiers are computed, not asked:** the catalogue answers (T0–T3) are roll-ups over the extraction fields;
  T4/T5/T6 (relational/dynamic/cross-term) draw on fields 11–12 + the verse term-array (T6.1 co-occurrence
  is already the verse's multi-term set).

## 5. Scope note
- Verse-extraction feeds **T0–T3** (identity / divine / constitution / faculty) directly. **T4/T5/T6** are the
  relationship/dynamic layer above — fed by fields 11–12 and the co-occurrence array, resolved in the synthesis.
- **T7** is method: T7.1 lexical = field 1 rolled up; T7.2/T7.3 are read/external.

## 6. Open decisions (review)
- **D1** Adopt the 13-field extraction record as the L2 output (replacing the ad-hoc 4-tier write)? `____`
- **D2** Origin checklist incl. `from-other-spirits` — confirmed? Any other origin to add? `____`
- **D3** Faculty as a per-term multi-select from the 11 (the T3 restructure) — confirmed? `____`
- **D4** Location as a multi-select across spirit/soul/heart/mind/will/conscience/body — confirmed list? `____`
- **D5** Which fields are mandatory-mechanical vs read-only — confirm the M/R column? `____`
