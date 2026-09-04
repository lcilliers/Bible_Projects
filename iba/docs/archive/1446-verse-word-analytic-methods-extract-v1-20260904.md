# Verse/word analytic methods — extract (v1)

**Filename:** 1446-verse-word-analytic-methods-extract-v1-20260904.md
**Escalation:** #1446 (spawned from #1443)
**Instruction this answers, verbatim (researcher, on #1443 v3, 2026-09-04):** "noted. Spawn a new
escalation from this to extract all verse word analytic methods."

**Scope, as read from that instruction:** every analytic method the project has used, or is
proposing to use, to derive findings **from an individual word/code within a single verse** —
not characteristic-level catalogue questions, cluster/M-code assignment, or Session-D/synthesis
work, which are a different grain and already have their own extracts elsewhere (e.g.
`iba/docs/1376-characteristic-tables-cross-db-inventory-v2-20260901.md`,
`iba/docs/1444-catalogue-outstanding-work-harvest-v1-20260904.md`). This is a straight compilation
of what already exists in the live system and design docs — no new investigation, no new
judgement calls, nothing resolved here that wasn't already resolved in its own source document.

Four layers, in chronological/supersession order. Each is named by its actual status, not
flattened into one undifferentiated list.

---

## 1. LIVE today (`iba.db`, unchanged, in production) — `verse_lexical` T1–T3

**Source:** `cfg_step` row `lexical.build` (`iba/app/handlers/lexical.py`); confirmed live via
`1383-verse-lexical-window1-full-build-specification-v1-20260904.md` §B.4.

One row per (span, code). For every code in a span's (possibly compound) `strong_variant`:

| Field | Method |
|---|---|
| `role` | classifies the code `content` vs `function` (grammar-only) |
| `resolved_sense` | stem/voice-selects the operative STEP sense for a `content` code |
| `status` | `resolved` or `unregistered` |
| `ambiguity_note` | flags same-base sibling ambiguity, never resolves it silently |

This is the only layer that is actually built and running today. Everything below is either
proposed-not-yet-built or historical/superseded.

---

## 2. PROPOSED, not yet built (`iba.db`, escalation #1383, in propose stage — v22, not approved)

**Source:** `1379-verse-lexical-enrichment-checklist-v1-20260902.md` (the original prototype list,
test-driven against Ps 25:2 / Hos 2:4 / Dan 1:8) and
`1383-verse-lexical-window1-full-build-specification-v1-20260904.md` (the full build spec built
from it — governance, configs, logic, validation, error handling, PS behaviour, reporting).
Nothing in this section is live; it is what #1383 is currently asking the researcher to approve.

### 2a. Layer 1 — mechanical, no judgement (new columns on `verse_lexical`)

| Field | Method |
|---|---|
| `position` / `surface` | straight copy from `span.position` / `span.surface` |
| `language` | straight copy from `strong.language` |
| `testament` | derived from `cfg_book_order.ordinal` (≤38 → OT, else NT) |
| `is_negator` | looked up in `cfg_lexical_code_class` (class=`negator`) |
| `narrative_morph` | Hebrew-only; regex-matches `morph_code` for wayyiqtol / az+imperfect narrative-sequencing markers |
| `gloss_consistent_in_verse` | data-quality check — does the same (strong, morph_code) pair carry >1 distinct `resolved_sense` in this verse |
| `party_kind` | looked up in `cfg_lexical_code_class` (party_divine/human/angelic → divine/human/non_human) |

### 2b. Layer 2 — judgement, one `verse_lexical_note` row per (code, test)

11 `note_type` values, each a distinct analytic test:

| note_type | What it tests |
|---|---|
| `idiom` | is this span part of a multi-code compound whose combined gloss diverges from a literal code-by-code reading |
| `pronoun_resolution` | same-verse antecedent resolution for a pronoun (person/number/gender agreement) — `unresolved` if not resolvable from this verse alone |
| `noun_relational` | does a noun name another party engaged in the verse's action (target/source/addressee) |
| `noun_severity` | does a noun sharpen the weight of an object/action without naming a party |
| `chain` | narrative-sequencing marker (Hebrew wayyiqtol) linking this operation to another as "and then" — no Greek equivalent built yet |
| `connective` | logical/causal connective linking two clauses by reason, not narrated order |
| `related_word` | mechanical pull of `strong_related` links for content-role codes — recorded raw, sorting left as a judgement field |
| `polarity` | is this row a negation/modifier attached to a declared operation |
| `entity_link` | ties an operative verb/noun back to its named subject (possessive suffix, proper name, person/number match) |
| `inert` | positive confirmation that a function-word row contributes nothing beyond grammar |
| `structural_pattern` | detects a verse-level rhetorical relationship (merism/chiasm/antithetic-parallelism/paired-image) spanning multiple codes — **detection only**; interpreting what it means is Stage 2's job (this is exactly what #1443 resolved) |

Plus a same-code data-quality check promoted out of the note layer: "same code, different gloss"
within one verse (now `gloss_consistent_in_verse` in Layer 1 above).

---

## 3. HISTORICAL — VE-lexical per-term dimensions (`bible_research.db`, catalogue v1, 2026-07-02)

**Source:** `Workflow/Catalogue/wa-ve-lexical-catalogue-v1-20260702.md`. This catalogue explicitly
states it **supersedes the tier catalogue** (§3 below) for word/verse-level dimension work. It is
itself now superseded in turn — CLAUDE.md's 2026-08-17 banner moved the base lexical layer to
`iba.db`/IBA entirely, and #1383 (section 2 above) is the line of work that replaces it going
forward. Retained here for provenance/genealogy, not as a live method.

Per-term dimensions, each value a PAIR (`element1 → element2`, direction + resolution state),
an EVENT, or a FLAG:

| dim | item | shape | what it captures |
|---|---|---|---|
| D1 | sense | value | per-occurrence STEP subgloss |
| D1 | type | value | action / status / quality (from POS) |
| D2 | source | PAIR | driver/antecedent → term |
| D3 | seat | PAIR | constitutional seat (heart/soul/spirit…) → term, via construct chain |
| D3 | bearer | PAIR | who bears it (experiencer/subject) → term — flagged not-yet-derived even at the time |
| D4 | operation | EVENT | the governing predicate |
| D5 | target | PAIR | term → object (+ object-type) |
| D6 | manner | PAIR | qualifier span → term, + intensity |
| D8 | effect | PAIR | term → produced-state (prose only) |
| D9 | coupling | PAIR | morphological weld (construct/preposition binding) only |
| D10 | prohibition | FLAG | mechanical negation/prohibition particle |

Verse-level (not per-term): D14 passage membership, genre, D7 process (escalation chain, prose
narrative only), D11 discovery (uncertainty notes channel). D10-valence, D12-hidden-meaning,
D13-cohabitation were dropped by researcher decision at the time (see the catalogue's own §4);
`related_tier` (the T-scheme below) was marked deprecated by this same document.

---

## 4. HISTORICAL — tier catalogue T1–T3 (`bible_research.db`, pre-2026-07-02, DEPRECATED)

**Source:** `Workflow/Tiers/wa-tier-catalogue-restructured-v2-20260611.md`. Explicitly superseded
by section 3 above (its own §4/deprecation note). Different grain from everything above: these are
**characteristic-level catalogue questions answered from verse evidence**, not per-code mechanical
tests — included here only because the VE-lexical catalogue names it directly as what it replaced,
so the genealogy would be incomplete without it.

- **T1 — Definition:** name/naming, kind, boundary, modes of operation, immediate response,
  sustained effect, conditions of reception.
- **T2 — Constitutional Location and Boundaries:** spirit-level location, body-direction,
  origin/source, constitutional movement.
- **T3 — The Inner Faculties:** perception, cognition, memory, affect, creativity, volition,
  agency, moral evaluation, conscience, conscientiousness, relational capacity.

(T0 and T4–T9 exist in the same catalogue but operate at the characteristic/theological-synthesis
grain, not the word/verse grain this extract is scoped to — omitted here as out of scope, not
overlooked.)

---

## Summary — one method, three predecessors

| Layer | Grain | Status | Location |
|---|---|---|---|
| `verse_lexical` T1–T3 | per-code | **LIVE** | iba.db |
| Window 1 Stage 1 (Layer 1 + Layer 2, 11 note_types) | per-code, per-span | **PROPOSED** (#1383, awaiting approval) | iba.db |
| VE-lexical D1–D11/D14 | per-term | historical, superseded | bible_research.db |
| Tier catalogue T1–T3 | per-characteristic (different grain) | historical, deprecated | bible_research.db |

No new decision is made in this document. If the researcher's intent was narrower or broader than
this scope reading, that's the one thing worth flagging back rather than guessing further.
