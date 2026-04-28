# Batch 2 — Medium Rules — Rewrites for Review

**Filename:** wa-global-rewrites-batch2-medium-v1-20260421.md
**Date:** 2026-04-21
**Reference to prior output:** wa-global-rules-review-obslog-v1_0-20260421.md §54–§60; prior batch: wa-global-rewrites-batch1-long-v1-20260421.md.
**Batch scope:** 10 medium rules (rule_text 300–450 chars).
**Governing discipline:** content-evaluation (appropriateness + correctness); consistency is key (§54).

---

## How to read this document

Each rule shows: current state summary, evaluation judgements (what stays / moves / drops and why), and proposed new field values. Fields that stay NULL are shown explicitly as *(NULL — none appropriate)* to make the structure visible. Two rules inherit content from the singular `example` column — migration is shown explicitly.

---

## 1. GR-FILE-003 — Version numbering

### Current state
Version: `3_0`. Length: 431 chars. `applies_to`: all processing instructions. `example`: NULL.

### Evaluation
Already close to rules-form. The "grouped in logical batches" qualifier on minor bumps is application guidance, not binding. No rationale is articulated; a single-sentence rationale would help (searchability + avoiding SemVer dot-meaning collisions in JSON). Add a simple correct/wrong pair as examples because this is a frequently-applied rule.

### Proposed new field values

**`rule_text`:**
> Version numbers use the format `v[major]_[minor]` with both components always present. The first version of any document is `v1_0`. Minor increments cover updates and modifications; major increments apply when a document is rewritten from scratch. This format is used consistently in filenames, JSON version fields, and prose references. It applies to all files, documents, instructions, observations logs, and patches.

**`rationale`:**
> Underscored dual-component versions give a uniform, grep-searchable form that sorts predictably in filename listings, and they avoid the SemVer dot convention which carries different meaning in package-ecosystem contexts.

**`application_notes`:**
> **Minor increments in logical batches.** Minor version bumps typically group a logical batch of updates rather than changing on every save. A single edit followed by another edit five minutes later normally shares a minor version. The judgement is what is sensible for the audit trail, not a fixed cadence.

**`examples`:**
> Correct: `v1_0`, `v2_7`, `v3_1`.
> Wrong (SemVer-style dot): `v2.7`.
> Wrong (missing minor): `v2`.

**`version`:** `3_0` → `3_1` (minor).

---

## 2. GR-PROG-009 — Inferential is not confirmed

### Current state
Version: `2.0` (dot notation). Length: 422 chars. `applies_to`: Session B, Session C, Session D instructions. `example`: NULL.

### Evaluation
The third sentence ("An inferential label in a published document is accurate description of the evidence state, not a failure") is rationale — it explains why the author should not hide the label. Moves to `rationale`. Rule_text stays with the two-sentence binding.

### Proposed new field values

**`rule_text`:**
> Where a connection, claim, or classification is theologically plausible or analytically reasonable but is not directly supported by data in the current extract, it is labelled inferential. Inferential connections may not be presented or upgraded as confirmed without supporting correlation signal or verse evidence.

**`rationale`:**
> An inferential label in a published document is accurate description of the evidence state, not a failure. Suppressing the label to make a finding look more solid than it is would misrepresent the evidence and defeat the purpose of separating findings from hypotheses.

**`application_notes`:** *(NULL — none appropriate)*

**`examples`:** *(NULL — none appropriate)*

**`version`:** `2.0` → `2_1` (minor + notation normalisation).

---

## 3. GR-PROC-002 — Findings rooted in data

### Current state
Version: `2_0`. Length: 407 chars. `applies_to`: all sessions, all phases. `example`: NULL.

### Evaluation
Binding is the first two sentences. The third ("A finding initially formed on a hypothesis is acceptable only when subsequent evidence supports it on its own terms") is application — it tells the author how to handle a finding that started as a hypothesis. Moves to `application_notes`.

### Proposed new field values

**`rule_text`:**
> Every analytical finding must be rooted in and traceable back to data in the database. A finding that cannot be traced to a specific verse record, term entry, lexical source, correlation signal, or extract field is a hypothesis, not a finding, and must be labelled as such or discarded.

**`rationale`:** *(NULL — the programme's empirical discipline makes this self-evident)*

**`application_notes`:**
> **Hypothesis-to-finding conversion.** A finding initially formed on a hypothesis is acceptable only when subsequent evidence supports it on its own terms. The original hypothesis-based statement is replaced with the evidence-grounded one; the earlier wording is not left in place with the evidence tacked on.

**`examples`:** *(NULL — none appropriate)*

**`version`:** `2_0` → `2_1` (minor).

---

## 4. GR-OBS-003 — Obslog vs session log

### Current state
Version: `2_0`. Length: 406 chars. `applies_to`: all sessions, all phases. `example`: NULL.

### Evaluation
Rule is clean. Vocabulary normalisation: "observations log" on first mention stays in full form; subsequent uses harmonise to "obslog" per GR-OBS-001 canonical form. No content moves; style tighten only.

### Proposed new field values

**`rule_text`:**
> The observations log (obslog) and the session log are separate files with separate purposes. The obslog is the working paper, written continuously per GR-OBS-001. The session log is the handoff record, produced at session close and at any named batch boundary within a session. A session that closes without a session log has not closed cleanly — the session log is always produced before the session ends.

**`rationale`:** *(NULL — the separation is self-evident given GR-OBS-001)*

**`application_notes`:** *(NULL — rule_text covers scope)*

**`examples`:** *(NULL — none appropriate)*

**`version`:** `2_0` → `2_1` (minor + vocabulary harmonisation).

---

## 5. GR-FILE-009 — Compact date format

### Current state
Version: `2.0` (dot notation). Length: 376 chars. `applies_to`: all processing instructions.
`example` (singular): `"WRONG: wa-023-compassion-sessionb-brief-v1-2026-04-14.md — CORRECT: wa-023-compassion-sessionb-brief-v1-20260414.md"`

### Evaluation
Rule is clean. Migration: move singular `example` content into new plural `examples` column; set singular to NULL per §48 decision.

### Proposed new field values

**`rule_text`:**
> Dates appearing in filenames use compact format `YYYYMMDD` with no separators. Dates within prose, table cells, change notes, or analytical observations may use ISO 8601 (`YYYY-MM-DD`) for readability. The compact format is required in filenames, patch IDs, document header date fields, and anywhere a date forms part of a structured identifier.

**`rationale`:** *(NULL — parseability and sort order are self-evident)*

**`application_notes`:** *(NULL — rule_text covers scope)*

**`examples`** (migrated from singular `example`):
> Wrong: `wa-023-compassion-sessionb-brief-v1-2026-04-14.md`
> Correct: `wa-023-compassion-sessionb-brief-v1-20260414.md`

**`example`** (singular): **set to NULL** — content migrated to plural `examples`.

**`version`:** `2.0` → `2_1` (minor + notation normalisation).

---

## 6. GR-DATA-002 — Extract is authoritative for Session B

### Current state
Version: `2.0` (dot notation). Length: 364 chars. `applies_to`: Session B instruction. `example`: NULL.

### Evaluation
Binding is clean. Style tighten only.

### Proposed new field values

**`rule_text`:**
> The current versioned extract produced by Claude Code is the authoritative data source for Session B analysis. Prior session outputs — observations logs, word studies, analytical briefs — are reference material only and do not override extract data. Where a prior output conflicts with the extract, the extract is correct and the prior output requires correction.

**`rationale`:** *(NULL — programme's canonical-DB discipline makes this self-evident)*

**`application_notes`:** *(NULL — none appropriate)*

**`examples`:** *(NULL — none appropriate)*

**`version`:** `2.0` → `2_1` (minor + notation normalisation).

---

## 7. GR-DATA-004 — Export version confirmation

### Current state
Version: `2.0` (dot notation). Length: 356 chars. `applies_to`: Session B instruction. `example`: NULL.

### Evaluation
Rule is clean. Minor style tighten ("before any analytical work begins" → "before analytical work begins").

### Proposed new field values

**`rule_text`:**
> The complete word data export is a versioned file managed by Claude Code. Claude AI confirms the version number of the export at session start, before analytical work begins. If the version is not confirmed, Claude AI requests it from Claude Code. Claude AI does not proceed on an extract whose version has not been confirmed in the current session.

**`rationale`:** *(NULL — overlaps with GR-DB-001 rationale on stale DB state)*

**`application_notes`:** *(NULL — none appropriate)*

**`examples`:** *(NULL — none appropriate)*

**`version`:** `2.0` → `2_1` (minor + notation normalisation).

---

## 8. GR-FILE-001 — Filename structure

### Current state
Version: `2.0` (dot notation). Length: 357 chars. `applies_to`: all processing instructions.
`example` (singular): `"wa-023-compassion-sessionb-brief-v1-20260411.md"`

### Evaluation
Rule is clean. Migration: move singular `example` content into plural `examples` column; set singular to NULL.

### Proposed new field values

**`rule_text`:**
> All files follow the pattern `[prefix]-[reference]-[short description]-[version]-[date]`. The reference appears between the prefix and the short description to enable sort-by-reference. Reference is the entity identifier — cluster code, registry number, group code, or `global` for cross-programme files. Dates in filenames use compact format per GR-FILE-009.

**`rationale`:** *(NULL — self-evident)*

**`application_notes`:** *(NULL — reference-identifier list sits naturally in rule_text)*

**`examples`** (migrated from singular `example`):
> `wa-023-compassion-sessionb-brief-v1-20260411.md`

**`example`** (singular): **set to NULL** — content migrated.

**`version`:** `2.0` → `2_1` (minor + notation normalisation).

---

## 9. GR-FILE-008 — Dual-write discipline

### Current state
Version: `2.0` (dot notation). Length: 355 chars. `applies_to`: all processing instructions. `example`: NULL.

### Evaluation
Binding is the first two sentences. The output-type list ("observations logs, session logs, patches, instruction documents, analytical briefs") is scope illustration — moves to `application_notes`.

### Proposed new field values

**`rule_text`:**
> All output files are written to both the working directory (`/home/claude` or equivalent) and `/mnt/user-data/outputs/` simultaneously. An output that exists only in memory, or only in one location, has not been written. This applies without exception to all output types.

**`rationale`:** *(NULL — self-evident given GR-OBS-001 + GR-CAD-001)*

**`application_notes`:**
> **Scope.** The rule applies to observations logs, session logs, patches, directives, instruction documents, analytical briefs, and any other output file produced in a session. No output type is exempt.

**`examples`:** *(NULL — none appropriate)*

**`version`:** `2.0` → `2_1` (minor + notation normalisation).

---

## 10. GR-PASS-001 — Pass-close download

### Current state
Version: `1.0` (dot notation). Length: 335 chars. `applies_to`: Session B, Session C, Session D instructions. `example`: NULL.

### Evaluation
Binding is clean. One terminology tightening: "patch specifications" → "patches" (the patch specification document was absorbed into the patch instruction in v2_0; the generic term going forward is "patches").

### Proposed new field values

**`rule_text`:**
> All internal outputs produced during a pass are made available for download at the end of that pass, before the next pass begins. This applies to observations logs, patches, directives, session logs, and any other pass-level output. A pass that closes without presenting outputs for download has not closed cleanly.

**`rationale`:** *(NULL — self-evident given GR-CAD-001 present_files discipline)*

**`application_notes`:** *(NULL — none appropriate)*

**`examples`:** *(NULL — none appropriate)*

**`version`:** `1.0` → `1_1` (minor + notation normalisation).

---

## Summary — batch 2 aggregate

| Rule | Old chars | New rule_text chars | Δ% | rationale | appl_notes | examples | Notation fix |
|---|---:|---:|---:|:---:|:---:|:---:|:---:|
| GR-FILE-003 | 431 | 426 | −1% | ✓ | ✓ | ✓ | — |
| GR-PROG-009 | 422 | 323 | −23% | ✓ | — | — | ✓ |
| GR-PROC-002 | 407 | 301 | −26% | — | ✓ | — | — |
| GR-OBS-003 | 406 | 399 | −2% | — | — | — | — |
| GR-FILE-009 | 376 | 311 | −17% | — | — | ✓ (migrated) | ✓ |
| GR-DATA-002 | 364 | 356 | −2% | — | — | — | ✓ |
| GR-DATA-004 | 356 | 336 | −6% | — | — | — | ✓ |
| GR-FILE-001 | 357 | 334 | −6% | — | — | ✓ (migrated) | ✓ |
| GR-FILE-008 | 355 | 272 | −23% | — | ✓ | — | ✓ |
| GR-PASS-001 | 335 | 296 | −12% | — | — | — | ✓ |

Reductions are modest as predicted — these rules were already close to rules-form. The value added in this batch is less about shortening and more about consistency: notation normalised, commentary separated where it existed, vocabulary harmonised, scope lists relocated to application_notes where they were sitting in rule_text for convenience.

**Content preservation:** no binding content dropped. One terminology update: "patch specifications" → "patches" in GR-PASS-001 (the source document was absorbed into wa-patch-instruction [current] in v2_0).

---

## Cross-cutting observations

1. **8 of 10 rules received version-notation correction** (dot → underscore) per GR-FILE-003. Folded into each rule's minor bump.
2. **2 rules received `example` → `examples` migration** (GR-FILE-001, GR-FILE-009) per §48 decision — content moves to plural column, singular set to NULL.
3. **Terminology consolidation:** "patch specifications" (in GR-PASS-001) replaced with "patches" — aligns with post-v2_0 document structure where wa-patch-specification was absorbed into wa-patch-instruction.
4. **NULL is the correct answer** for most commentary fields on these rules. Forcing content into them would dilute the structure.

---

## Open check before patch applies

1. Directional acceptance of the ten rewrites. If any specific rule's rewrite needs revision, say which — I will redo that rule only.
2. The "patch specifications" → "patches" terminology update in GR-PASS-001 is an authorship judgement; confirm acceptable.
3. The `example` → `examples` migrations in GR-FILE-001 and GR-FILE-009 clear the singular column as agreed in §48; confirm this is still the right approach.

---

*End of Batch 2 review document. Patch follows at wa-rules-batch2-medium-update-v1-20260421.json.*
