# VE / lexical analysis — proper data model (redesign)

> Researcher (2026-06-15): the current state is *"very messy and not clearly thought through"* — the "14 VE" is a **phantom** (no real structure), the tier-question links **don't actually answer** their questions, and the bulk is a variable mess (e.g. faculty = 11 separate yes/NONE findings; location = 5). This is the proper structure to convert it to. Design for sign-off; no build yet.

## Core principle
Replace the scattered, half-linked tier findings with a **typed structure** keyed to the real unit, where **cardinality decides storage**:
- a VE that is **1:1** with the term-in-verse → a **column on `verse_context`**;
- a VE that is **1:many** → a row-per-value in a child table **`ve_lexical`**;
- the **meaning** is then **one** composed finding per term-in-verse — a templated narrative of those fields, not 22 loose findings.

## The unit
The term-in-verse = a **`verse_context`** row (`verse_record_id` + `mti_term_id`; ~1:1 with `wa_verse_records`; already carries the cluster refs `group_id` / `cluster_subgroup_id`). All VE data attaches here.

## 1:1 VE → columns on `verse_context`
The singular verdicts (one value per term-in-verse). Several map to fields that already exist or are derivable:

| VE | field | source | note |
|---|---|---|---|
| 1 | sense | `step_subgloss_label` → canonical | `sense_id` column already exists (empty) |
| 2 | type | morphology + sense | action/status/quality |
| 4 | **mode** | `wa_verse_records.morph_code`/`stem` | **already a column** — read via `verse_record_id`, or denormalise a `mode` label |
| 6 | origin | signal-list | within/received/bestowed |
| 8 | attributed_to_God | divine-subject signal | yes/no |
| 9 | purpose_equips | read | 1:1 |
| 10 | typology_direction | read | human↔divine |
| 11 | immediate_response | read | 1:1 |
| 14 | literary_setting | verse-level | narrative/poetry (strictly a verse attribute, not term) |

→ add these as typed columns on `verse_context` (most are short enums/phrases).

## 1:many VE → `ve_lexical` (new child table)
The fields that genuinely take **multiple values** per term-in-verse — today smeared across many boolean findings:

| VE | field | why 1:many | today (the mess) |
|---|---|---|---|
| 3 | compound | the web-edges: term + each co-occurring T1/T2 | 'Co-occurrence' (1 lumped finding) |
| 5 | constitutional_location | a term can sit in Heart **and** Mind… | **5 separate fields** (Heart/Mind/Soul/Spirit/Body) |
| 7 | faculty | Perception **and** Affect… | **11 separate yes/NONE fields** |
| 12 | produces_effect | multiple effects | 'Sustained Effect' |
| 13 | relational_implication | multiple directions | 'Relational Capacity' |

**`ve_lexical` schema (proposed):**
```
ve_lexical(
  id              INTEGER PK,
  verse_context_id INTEGER FK -> verse_context.id,   -- the unit
  ve_number       INTEGER,        -- 3,5,7,12,13 (the VE)
  ve_label        TEXT,           -- 'faculty','constitutional_location',... (readability)
  tier_question_ref TEXT,         -- e.g. 'T3.4.1' (provenance into the catalogue)
  value           TEXT,           -- the actual value (e.g. 'affect', 'heart', co-term strongs)
  delete_flagged  INTEGER DEFAULT 0
)
```
One row per value → faculty with {perception, affect} = 2 rows; location {heart, mind} = 2 rows; the 11/5 boolean fields collapse to only the rows that fire.

## The cluster relationship
The term-in-verse's **primary cluster** is derivable from the term (`mti_terms.cluster_code`) and already referenced on `verse_context` (`cluster_subgroup_id` → cluster) — so it lives on `verse_context`, and `ve_lexical` inherits it via the FK (no duplication). The **secondary clusters** a term-in-verse touches are exactly the **compound (VE3) web-edges** — each compound row points at a co-term whose cluster is the linked cluster. So "which clusters does this sense live in" = primary (verse_context) + the VE3 rows. No separate verse_cluster table needed unless we want a materialised index.

## The single meaning finding (the payoff)
**One** lexical/meaning record per term-in-verse = the **templated narrative** composed from `verse_context` (the 1:1 columns) + its `ve_lexical` rows (the 1:many), in a preset pattern. It is a deterministic *view* of the structured fields — traceable to each, regenerable, searchable. This **replaces** the current ~5–22 scattered findings per unit with: structured evidence (columns + ve_lexical) **+** one composed meaning.

## Migration (current mess → this)
1. Add the 1:1 columns to `verse_context` + create `ve_lexical` (a schema migration, M59).
2. Map existing findings: 1:1 tier findings → `verse_context` columns; the faculty/location/compound/effect/relational findings → `ve_lexical` rows (collapsing the boolean spread; drop the `NONE` rows).
3. Fix sense en route (per-occurrence subgloss, per `wa-sense-operation-setup`).
4. Compose the single meaning finding from the template; retire the scattered tier findings (soft-delete, keep for audit).

## Refinement (researcher, 2026-06-15) — normalise the analytic layer into TWO tables + clean out `finding`
The analytic layer (`verse_context`) should be **normalised into two tables**, and the VE "findings" **retrofitted into them so only real findings remain in `finding`**:

- **verse-level table** (1:1) = `verse_context` itself, extended with the **1:1 VE columns** (sense, type, origin, attributed-God, typology, response, purpose, literary; mode read-through). One row per term-in-verse.
- **items-in-verse-level table** (1:many) = **`ve_lexical`** — the multi-valued VE (compound, location, faculty, produces, relational), one row per value.

**The `finding` table today is overloaded (grounded counts, active):**

| content | rows | disposition |
|---|---|---|
| VE field-values (`VERSE` `l2_api` 182,176 + `l2_mechanical` 115,920) | **298,096** | **retrofit** → verse-level columns (1:1) + `ve_lexical` rows (1:many), then remove from `finding` |
| composed meaning (`VERSE` `l2_meaning`) | **8,174** | the **one templated narrative** per term-in-verse (verse-level column or a single kept finding) |
| **real findings** (`CLUSTER` 1,901 + `GLOBAL` 991) | **2,892** | **STAY** in `finding` |

→ After the retrofit, `finding` holds **only real findings** (~2,892 synthesis/observation rows) instead of ~309k. The VE analytics live as **typed structure** (columns + `ve_lexical`), and the meaning is the composed narrative — exactly the "evidence is structured, the finding is the conclusion" separation.

**Migration shape (M59+):** add the 1:1 columns to `verse_context` + create `ve_lexical` → map the 298,096 VE field-values into them (1:1 tier → column; faculty/location/compound/effect/relational tier → `ve_lexical` rows; drop the `NONE`/boolean spread) → fix sense en route → compose the meaning → soft-delete the migrated VERSE findings, leaving `finding` = real findings only. Keyed on `verse_context_id` (now unique).

## Open design points for sign-off
- **mode** on `verse_context`: read-through from `wa_verse_records` vs denormalised column (recommend read-through — single source of truth).
- **literary_setting (#14)** is verse-level, not term-level — store once per verse, not per term-in-verse?
- whether `ve_lexical` should also hold the **1:1** fields (uniform model, simpler code) vs columns (queryable, typed) — recommend columns for 1:1, table for 1:many, as above.
- the meaning finding: a `verse_context.meaning` column vs a `finding` row.
