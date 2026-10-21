# Finishing the catalogue configuration + config-not-code audit

**Filename:** 1383-catalogue-finishing-and-config-not-code-audit-v1-20260903.md
**Escalation:** #1383
**Instruction, verbatim:** `wa_obs_question_catalogue` (`bible_research.db`) is the authoritative
catalogue table. Wording changes, splitting questions, and adding a column narrating how each
question is answered (if none exists) are all part of finishing this build's configuration. Update
the glossary. Rules belong in config, not code.

**Confirmed against the live tooling before planning anything** (not assumed): `obs_catalogue.update`
(`iba/app/lib/cataloguewrite.py`, registered, escalation #1007) is a plain UPDATE-by-`obs_id` tool —
**no config-approval gate** (this table is ordinary content, not `cfg_*`), but **no INSERT support
either**. Wording fixes on existing rows can be applied with it directly, in this session, no
Developer Mode needed. **Adding a new column and creating the split rows both need new code** (a
one-off migration, same shape as the existing `add_obs_catalogue_source_last_modified...` precedent)
— **checked live: this session is not in Developer Mode** (`.claude/.developer-mode-active`
absent). That part is planned and specified below, not built — flagged plainly, not attempted.

---

## 1. The new column

**Proposed:** `answered_by` — TEXT, nullable. One line per question: which stage answers it, and
by what mechanism, in the same style as the field-mapping document (§3–5 there), condensed to a
single traceable sentence per question. Registered the same way `source`/`last_modified` were
(one-off migration + `cfg_column` row), not decided here — a build item, named precisely so it
isn't vague when picked up.

## 2. Questions to split — exact proposed wording, not just "split it"

| Old code | Old text (as-is) | New codes + wording |
|---|---|---|
| `T0.1.2` | "Across the characteristic's verses, is it ever borne by God himself or only by the creature, and what does that pattern of presence or absence indicate for its place in the human person and in the divine image?" | **`T0.1.2a`** (mechanical half): "Across the characteristic's verses, is the characteristic ever predicated of God himself (not just present in a verse where God is also mentioned)?" — Stage 1 aggregation. **`T0.1.2b`** (interpretive half): "What does the pattern of presence/absence found in T0.1.2a indicate for the characteristic's place in the human person and in the divine image?" — Stage 2 Pass 2b, T0.2.1-class. |
| `T6.1.1` | "Which adjacent characteristics appear alongside this one in the verse evidence, and how frequently? Record none if no significant co-occurrence appears." | Already single-purpose (a count) — **not split, kept as-is**, `answered_by` narrates it directly. Listed here only because it was wrongly paired with T6.1.2 in this session's own earlier read — correcting that pairing, not the question itself. |
| `T6.1.2` | "What does the co-occurrence pattern show about this characteristic's place in the inner-being landscape?" | Kept as-is — already correctly its own question; the earlier error was treating it as inseparable from T6.1.1, not the wording. |
| `T4.6.2` | "Is the characteristic a site of adversarial activity — something that can be attacked, distorted, or weaponised by adversarial powers — as the evidence shows?" | **`T4.6.2a`** (mechanical half, once the angelic/adversarial-name lexicon is built, §4 below): "Does an adversarial-being code ever appear as an acting party in a verse carrying this characteristic?" — Stage 1 aggregation. **`T4.6.2b`**: "What does that pattern show about the characteristic being a site of adversarial activity?" — Stage 2, T0.2.1-class. |
| `T4.6.3` | "Is the characteristic communicated, strengthened, or mediated through angelic ministry in the evidence?" | Same split shape as `T4.6.2` — **`T4.6.3a`**/**`T4.6.3b`**. |

Four splits, not more — every other "hybrid" this session found (`T0.1.1` itself, `T4.1.1`,
`T4.2.1`) turned out to be *fully* mechanical once corrected (§2/§5 of the coverage document), not
actually hybrid — only these four still have a genuine mechanical/interpretive seam.

## 3. Wording fixes for clarity — the ones this session's own work grounds an actual fix for

Not a general sweep (that's a larger, separate task the researcher already flagged as needed) —
only the questions this session's own investigation directly earned a concrete rewrite for:

| Code | Problem found | Proposed fix |
|---|---|---|
| `T7.2.1` | "role in the sentence and argument" bundles two different, differently-answered things (§2 of the coverage doc — sentence-role is Stage 1, argument-role is an unowned gap) | Split the *wording*, not the question code: "What is the function of the primary term within its primary verse — (a) what role does it play in the sentence, and (b) what role does it play in the verse's own argument, if a connective/chain edge shows one?" — makes the two-part answer the question already needs explicit, without a new code. |
| `T7.1.4`–`T7.1.7` | Each currently reads as a single yes/no ("Record it, or none") when this session's work shows each has a mechanical inventory half (does the vocabulary include a term of type X) and a judgement half (what does that inclusion mean) bundled the same way `T0.1.2` was | Flagged, not fixed here — same split shape as §2's four, but four more instances; proposing this as a **follow-on batch**, not done in this pass, to keep this pass's scope to what's already fully grounded. |

## 4. Config-not-code — every lexicon this session prototyped, now specified as data, not constants

**Direct instruction applied**: this session's own drift-mitigation demo script hardcoded
`CONNECTIVE_LEXICON`/`NEGATOR_LEXICON` as Python dicts — fine for a same-session proof of concept,
**wrong for the actual build**, exactly the class of thing `governance.rules_must_be_config_driven`
exists to catch. Fixed in the design doc (revised again here):

**New table, one home for every code-classification lexicon this build needs** (not five separate
ad-hoc tables): `cfg_lexical_code_class` — `strong_code` (TEXT), `class` (TEXT, `cfg_enum`:
`negator` / `connective_causal` / `connective_coordinating` / `connective_purpose` / `party_divine`
/ `party_human` / `party_angelic`), `evidence_note` (TEXT — why this code is classed this way, per
`traceable-by-construction`), `active` (INTEGER). Every mechanical column in the design doc that
reads a lexicon (`is_negator`, the connective-type note, `party_kind`) queries this table — none of
them hardcode the code list in the handler's own source.

**Status of each lexicon, honestly, not overstated:**

| Lexicon | Status |
|---|---|
| Negator | Seeded and verified live this session (7 codes) — ready to load into `cfg_lexical_code_class` as-is. |
| Connective (causal/coordinating/purpose) | Seeded and verified live this session (6 codes) — ready to load. |
| Divine-name (`party_divine`) | Seeded and verified live this session (7 codes) — ready to load. |
| Human-name (`party_human`) | **Not built.** Named as needed (§3 of the field-mapping doc) — no seed list exists yet. Real pre-build work, not yet started. |
| Angelic/adversarial-name (`party_angelic`) | **Not built.** Same status — needed for `T4.6.1`/`T4.6.2a`/`T4.6.3a`, none of which are answerable until this exists. |

## 5. Glossary — terms this session used that aren't defined yet

Checked against the live glossary (§2 of the earlier design-doc revision already confirmed
`surface`/`grain`/`gloss`/`sub gloss`/`lemma`/`term`/`word` exist and are correct) — these do not:

`Layer 1` / `Layer 2` (this session's own mechanical/judgement split within Stage 1 — distinct from
Stage 1/Stage 2, easy to conflate, worth its own disambiguating entry), `Stage 1` / `Stage 2` (the
blueprint's own terms, `Window 1`/`Window 2` as their prior names), `party_kind`, `grain` vs.
`resolved_sense` (a cross-reference entry making the distinction explicit, since this session's own
false-alarm on `resolved_sense` shows it's genuinely easy to conflate the two), `structural_pattern`
(the note_type, and the Stage-1-detect/Stage-2-interpret split it carries), `passage boundary
suggester`, `cfg_lexical_code_class`. Not written yet — flagged as a real follow-on item, same
governed path as #1377's own glossary work (`prosestore.py`'s chapter-edit cycle), not attempted in
this document.

## 6. What's actually executable now vs. what needs Developer Mode

- **Executable now, standard mode, no gate**: none of §2/§3's wording changes yet — they're
  proposals for your confirmation first (the same "recommendation, not a silent decision" discipline
  as everything else this session), not applied blind. Once confirmed: real `obs_catalogue.update`
  calls, one per row, each one real and verifiable, not a bulk unreviewed sweep.
- **Needs a build item (new migration script, then Developer Mode or your explicit go-ahead)**: the
  `answered_by` column itself (§1); the 4 split rows as new `question_code`s (§2, since
  `cataloguewrite.py` has no INSERT path); `cfg_lexical_code_class` itself (a new `iba.db` table);
  the glossary entries (§5, via `prosestore.py`'s own governed chapter-edit cycle).
