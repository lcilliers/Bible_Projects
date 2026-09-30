# L2 finding system — schema design (migration M56 proposal)

> **Design · v1 · 2026-06-09 · CC.** Governing rule: **all study work in the DB** ([[feedback_all_study_work_in_db]]).
> The L2 finding lifecycle (formulate → write → correct) must be DB-resident. This designs the schema as an
> **extension of existing infrastructure, not a parallel system**. **Proposal for researcher review — not yet
> applied** (DB schema change → backup + dry-run + the migration discipline first).

---

## 0. Principle
Findings, the clarification library, tier-question links, correction history — **all in the DB.** The JSON
prototype store is retired; `.md`/`.json` are outputs only.

## 1. Reuse what exists (no duplication)
- **`verse_context`** (43,722 rows) = the per-**(verse, term)** anchor. Already has `step_meaning_applied`
  (lexical meaning), `sense_id`, `sense_multiplicity`, `keywords`, `pole`, `pole_is_metaphor`,
  `residue_flag`, `set_aside_reason`, `analysis_note` (M55). → the home of the **per-term-in-verse finding**.
- **`wa_verse_records`** carries `morph_code` / `stem` (the mode). 
- **`cluster_finding`** (19,996) + **`wa_finding_catalogue_links`** = cluster-level finding↔question. → the
  **roll-up** above the verse-level findings (unchanged).
- **`wa_obs_question_catalogue`** = the 242 tier questions. → tier findings link to it.

## 2. Extend `verse_context` (the anchor) — ADD columns
| column | type | meaning |
|---|---|---|
| `thing_type` | TEXT | ACTION / STATUS / QUALITY (from morph; the term-in-verse type) |
| `triage_status` | TEXT | ACCEPT · ESCALATE · RESEARCHER · STATE_SILENT (the L2 triage outcome) |
| `meaning_provenance` | TEXT | mechanical · clarification:`<id>` · api · researcher |
| `flagged_for_review` | INTEGER | 1 = induced / low-confidence (the state-not-induce hook) |

(Lexical meaning = existing `step_meaning_applied`; mode = `wa_verse_records.stem`.)

## 3. NEW — `vc_tier_finding` (the verse-level tier findings)
One row per (verse-term-finding, tier question) — the ~5–6 L2-answerable tiers per verse, **including
stated-silent** (silence is a recorded finding, never induced).
```
id INTEGER PK
verse_context_id INTEGER  → verse_context.id
question_id INTEGER       → wa_obs_question_catalogue.obs_id   (the tier, e.g. T7.1/T1.2/T2/T3)
finding_value TEXT        -- the answer text
finding_status TEXT       -- ANSWERED · STATED_SILENT · STATED_UNRESOLVED
provenance TEXT           -- mechanical · clarification · api · researcher
clarification_id INTEGER  → clarification.id  (nullable; which rule justified it)
created_at TEXT, last_updated_date TEXT, delete_flagged INTEGER
```

## 4. NEW — `clarification` (the clarification library) + back-links
The disambiguation rules; findings reference the one that justified them, so a library change drives
targeted re-evaluation.
```
id INTEGER PK
code TEXT                 -- e.g. CLAR-FEAR-THREAT-DREAD
rule_text TEXT            -- "fear + threat-object → dread"
signal_read TEXT          -- the verse-signal it reads (the validity basis)
reads_present_signal INT  -- 1 = reads a present signal (VALID) · 0 = induces (FORCED → invalid)
scope TEXT                -- term · cluster · global
status TEXT               -- proposed · validated · revoked
supersedes_id INTEGER     → clarification.id (nullable)
created_at TEXT, validated_at TEXT, notes TEXT
```
Back-link: `vc_tier_finding.clarification_id` (and `verse_context.meaning_provenance` may name it). Revoking
or editing a clarification → re-evaluate its linked findings.

## 5. NEW — `vc_tier_finding_revision` (append-only correction history)
```
id INTEGER PK
vc_tier_finding_id INTEGER → vc_tier_finding.id
field TEXT, value_from TEXT, value_to TEXT
reason TEXT, clarification_id INTEGER → clarification.id
revised_at TEXT, revised_by TEXT
```
Append-only — the audit trail of the augment+correct cycle. (Same pattern can serve `verse_context`
meaning-field revisions.)

## 6. Roll-up (unchanged)
`cluster_finding` / `wa_finding_catalogue_links` remain the **cluster-level** roll-up; the verse-level
`vc_tier_finding` rows aggregate up into them (a later derived step), so both grains coexist in the DB.

## 7. Migration M56 (3.29.0 → 3.30.0)
- `engine/migrate.py`: `_m56(conn)` — `ALTER TABLE verse_context ADD COLUMN …` (×4) + `CREATE TABLE`
  `clarification`, `vc_tier_finding`, `vc_tier_finding_revision` + indexes (`vc_tier_finding.verse_context_id`,
  `.question_id`, `.clarification_id`). Idempotent, own transaction, history-aware (the M55 pattern).
- `engine/constants.py`: `EXPECTED_SCHEMA_VERSION = "3.30.0"`.
- Apply discipline: backup → `--migrate --dry-run` → review → `--migrate` → verify.

## 8. Volume sanity
~43k verse_contexts × ~6 L2 tiers ≈ **~260k `vc_tier_finding` rows** at full coverage — fine for SQLite.
(Not 80 tiers/verse — L2 only writes the lexically-answerable identify-tiers; the rest are cluster roll-ups.)

## 9. Broader all-in-DB follow-ons (separate, after M56)
- **Keyword allocation** → write to `verse_context.keywords` / a keyword table (retire the CSV prototype).
- **thing-type / relationship-type / adequacy-signal vocabularies** → small DB lookup tables.
- The **assembly** is a derived view (read-only query), not stored — acceptable (it's computed, not a result).

## Decision points (review)
- **D1** Anchor the verse-finding on `verse_context` (+4 columns) — agree? `____`
- **D2** `vc_tier_finding` keyed to `wa_obs_question_catalogue.obs_id` (tier questions) — agree, or use a
  short `tier_code` instead of the full question link? `____`
- **D3** `clarification` library + `clarification_id` back-link on findings (for propagating corrections) —
  agree? `____`
- **D4** `vc_tier_finding_revision` append-only history — agree (vs a generic audit table)? `____`
- **D5** Record `STATE_SILENT` tier rows explicitly (≈260k) vs store only answered + treat absence as silence?
  (Recommend explicit — silence is a finding.) `____`
