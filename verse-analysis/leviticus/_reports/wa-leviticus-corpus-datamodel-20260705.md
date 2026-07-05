# Leviticus study — corpus data model (how it lives in the DB)

> **Requirements (researcher, 2026-07-05):** the Leviticus study must be (1) **discoverable as part of the corpus**, (2) **in the DB**, (3) **searchable**, (4) **all observations evidenced**, (5) **extendable when new questions arise**, (6) **cover ALL verse-record verses** — not only the ones the current questions touch.
>
> **Resolution: zero new tables.** Every requirement is met by reusing the live corpus structures. The design below maps each requirement to its mechanism, grounded in the live schema (v3.37.0).

---

## Part 1 — Requirement → corpus mechanism

| # | Requirement | Mechanism (existing table) |
|---|---|---|
| 1 | discoverable as part of the corpus | observations are **`finding`** rows carrying `cluster_code` (M12 clean, M10 sin, M11 atone, M22 holy, M47 self) → they surface under the existing cluster/characteristic model, alongside all other findings |
| 2 | in the DB | coding in **`ve_lexical`**, observations in **`finding`**, questions in **`wa_obs_question_catalogue`** — no `.md` is the record; files are working views only |
| 3 | searchable | `ve_lexical` is SQL-queryable per dimension; `finding` is queryable + FTS-adjacent (prose_section_fts); questions catalogued |
| 4 | all observations evidenced | every `finding` links to its verse-records via **`finding_verse_link`** (role=SUPPORT) and to Strong's/cross-refs via **`finding_citation`** — no un-evidenced claim |
| 5 | extendable for new questions | a new dimension = a new `ve_label` value (no migration); a new question = a new **`wa_obs_question_catalogue`** row; findings attach to it via **`finding_question_link`** |
| 6 | cover ALL verse-record verses | Phase A codes **every** Leviticus verse-record occurrence into `ve_lexical`; verses with no inner-being span get a coverage marker row (`ve_label='coverage'`, `value='ritual-no-ib-span'`) so completeness is total and auditable |

---

## Part 2 — The three layers

### Layer 1 — the coding → `ve_lexical` (one row per occurrence-dimension-value)

`ve_lexical` is the corpus's *items-in-verse* table and is **already an extensible EAV model** (`ve_label` = dimension name, `value` = coded value, keyed on `verse_context_id` / `verse_span_id`, isolated by `source_provenance`). Its live label-set already includes `bearer`, `source`, `operation`, `discovery`, `manner`, `target`, `locus`, `effect` — the same shape as our coding.

**We add a Leviticus scheme under `source_provenance='leviticus-lexical-v1'`.** Each axis-term occurrence generates one row per coded dimension:

| ve_lexical field | use |
|---|---|
| `verse_context_id` / `verse_span_id` | the occurrence (verse-record / word-span) — the key |
| `ve_label` | the **dimension** — controlled vocab below |
| `value` | the coded value (controlled vocab per dimension) |
| `notes` | one-line verse-context |
| `source_provenance` | `leviticus-lexical-v1` |
| `gate`, `pair_kind`, `from_span`… | left NULL (VE-model fields, N/A here) |

**Dimension vocabulary (`ve_label` values) for the Leviticus scheme:**
`axis` · `polarity` · `bearer` · `source` · `source_domain` · `reset` · `purpose` · `driver` · `person_role` · `awareness` · `temporal` · `transmissibility` · `co_term` · `coverage`
*(value vocabularies as defined in [`wa-leviticus-lexical-coding-schema-20260705.md`](wa-leviticus-lexical-coding-schema-20260705.md); a new dimension later = just a new `ve_label` value — no schema change, satisfying requirement 5.)*

**Completeness (requirement 6):** Phase A iterates **every** verse-record verse in Leviticus (688 verses). Inner-being occurrences get their full dimension row-set; a verse with only T2/ritual content gets one `coverage='ritual-no-ib-span'` row. Result: **every verse accounted for**, and a single query proves it (`verses coded = verses in record`).

### Layer 2 — the observations → `finding` (evidenced)

Interpretive output = `finding` rows, `provenance='leviticus-lexical-v1'`:

- **Per-verse / per-occurrence observation** → `level='VERSE'`, `verse_context_id` set, `cluster_code` = the axis's M-code, `finding_value` = the observation.
- **Term / axis discovery** (e.g., *"kaphar 'cover' is reserved for moral fault; bodily uncleanness is reset by washing"*) → `level='GLOBAL'`, `finding_value` = the discovery.
- **Evidence (requirement 4):** every finding gets `finding_verse_link` rows (one per supporting occurrence, `role='SUPPORT'`) + `finding_citation` rows (Strong's, cross-refs). *No finding without evidence links.*
- **Revision:** `supersedes_id` / `finding_revision` when a discovery is refined by later evidence (extensible over time).

### Layer 3 — the questions → `wa_obs_question_catalogue` (extensible)

The researcher's questions become catalogue rows (`scope='leviticus'`, a `component_code` per axis), e.g.:

| question_code | question_text (abridged) |
|---|---|
| LEV-CLN-01 | Why is it necessary to be clean? (what does cleanness enable / uncleanness cost) |
| LEV-CLN-02 | Where does the concept of "unclean" come from? (source + root) |
| LEV-CLN-03 | Why *cover* the unclean rather than scrub it clean? |
| LEV-CLN-04 | Is the need to be clean IB-desire, external expectation, or prerequisite? |
| LEV-CLN-05 | Does awareness of unclean come into play? |
| LEV-CLN-06 | Is clean status past-only, or also forward-standing? |
| … | *(new questions added as rows anytime — requirement 5)* |

Findings link to the questions they resolve via `finding_question_link` (`coverage='answers'|'partial'`). **A question's answer = the set of findings linked to it, each evidenced** — fully traceable.

---

## Part 3 — Worked example (Lev 16:30) through all three layers

*"On this day shall **atonement** (kipper/kaphar) be made to **cleanse** (taher) you; you shall be **clean** before the LORD from all your **sins** (chattat)."*

**Layer 1 — `ve_lexical` rows** (provenance `leviticus-lexical-v1`, keyed to the 16:30 occurrences):
```
16:30 kaphar : axis=ATONE_COVER · polarity=n.a. · reset=atone-cover · source_domain=moral · driver=divine-initiative · temporal=recurring · co_term=taher,chattat
16:30 taher  : axis=CLEAN_UNCLEAN · polarity=clean · reset=purge-clean · source_domain=moral · purpose=belonging(before-the-LORD) · temporal=recurring · co_term=kaphar,chattat
16:30 chattat: axis=SIN_GUILT · polarity=guilty→cleared · source_domain=moral · co_term=kaphar,taher
```
**Layer 2 — `finding`** (level=GLOBAL, cluster_code=M11, provenance leviticus-lexical-v1):
`finding_value` = *"Atonement (cover) is the mechanism; the state-change it effects is clean-from-sin (taher). The covering serves a cleansing of the person's moral state, renewed annually."*
→ `finding_verse_link`: 16:30 (+ 4:20, 4:26… the other kipper→forgiven occurrences) as SUPPORT.
→ `finding_citation`: H3722 (kaphar), H2891 (taher), H2403 (chattat).
**Layer 3 — `finding_question_link`:** → LEV-CLN-03 (`answers`), LEV-CLN-06 (`partial`).

Now the question *"why cover not scrub?"* is answered by: `SELECT` findings linked to LEV-CLN-03 → each traceable to its `ve_lexical` cross-tab (`reset` × `source_domain`) and its verse evidence. **Transparent, searchable, evidenced.**

---

## Part 4 — Query patterns (how the questions resolve, in SQL)

- **Cover vs scrub:** `ve_lexical` pivot — `reset` × `source_domain` where provenance=leviticus-lexical-v1 → shows covering↔moral, washing↔bodily.
- **Where unclean comes from:** `GROUP BY value` on `ve_label='source'` / `'source_domain'`.
- **Awareness:** occurrences where `ve_label='awareness'` ≠ `not-in-view`, grouped by `source_domain`.
- **Desire/external/prereq:** distribution of `ve_label='driver'` and `'person_role'`.
- **Past/future:** distribution of `ve_label='temporal'` by `axis`.
- Each pivot returns occurrence keys → join to `wa_verse_records` for the text → the evidenced `finding` cites them.

---

## Part 5 — Build plan & decisions

**Build sequence:**
1. **Seed questions** — insert the LEV-* catalogue rows (the six above + a holder for new ones).
2. **Phase A (coding, all 27 chapters)** — code every verse-record occurrence into `ve_lexical` (provenance `leviticus-lexical-v1`), with coverage markers; reusable loader script (`_apply_load_lev_coding` from a per-chapter JSON I produce by reading each chapter's verses). Verify `coded verses = record verses`.
3. **Phase B (discoveries)** — per axis (clean/unclean first), run the pivots, read the returned occurrences, write evidenced `finding` rows + `finding_verse_link` + `finding_question_link`. Filed working-view `.md` in `_discoveries/` mirrors each DB finding (view only; DB is the record).

**Decisions to confirm:**
1. **Coding home** — **(A, recommended)** reuse `ve_lexical` under `leviticus-lexical-v1` (corpus-native, extensible, zero new tables — but co-locates with the in-flux VE/RESET data, isolated only by provenance); **(B)** a dedicated `lev_lexeme` table (cleaner isolation, but a new structure + migration). Recommend **A** — it is the designated items-in-verse table and best satisfies "discoverable as part of the corpus."
2. **Add `transmissibility`** as a coded dimension (does the uncleanness spread to people/objects)? Recommend **yes**.
3. **Coding granularity of the key** — key each occurrence to `verse_span_id` (word-precise, via `verse_span_index`) where the axis-term maps cleanly, else `verse_context_id` (verse-precise). Recommend the hybrid.

---

*Filed 2026-07-05. Supersedes the "persistence" decision in the schema doc (now resolved: DB via `ve_lexical` + `finding` + catalogue). Companions: [`wa-leviticus-lexical-coding-schema-20260705.md`](wa-leviticus-lexical-coding-schema-20260705.md), [`wa-leviticus-terminology-orientation-and-plan-20260705.md`](wa-leviticus-terminology-orientation-and-plan-20260705.md), [`wa-leviticus-verse-records-listing-20260705.md`](wa-leviticus-verse-records-listing-20260705.md). No DB writes yet — pending sign-off on the three decisions.*
