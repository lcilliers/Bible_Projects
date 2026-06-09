# L2 finding system — schema design v2 (migration M56) — incorporating researcher markup

> **Design · v2 · 2026-06-09 · CC.** Supersedes v1 (`wa-l2-finding-schema-design-v1`) after researcher markup
> of D1–D5. Key change: **D3 collapses the clarification library into the finding model** — a clarification is
> just an OPEN/RESOLVED finding at the correct level. One level-aware finding table; "clarification" is a role.
> All study work in the DB ([[feedback_all_study_work_in_db]]). **Proposal — not yet applied.**

---

## Researcher decisions (2026-06-09)
- **D1 ✅** anchor the verse-finding on `verse_context` (+4 columns).
- **D2 ✅ + M:N** finding↔tier-question is **many-to-many** → an **index/junction table** (not a single FK).
- **D3 ✅ reframed** a **clarification = an open/not-resolved finding at the correct level** → **no separate
  clarification table**; one level-aware finding model; verse findings link up to the resolving finding.
- **D4 ✅** append-only revision history (useful for trends / validate / backtrack).
- **D5 ✅** record **STATE_SILENT explicitly** — rationale: *if 99 of 100 verses are silent and 1 is a
  positive finding for a tier, that rarity IS the significance.* Silence must be counted to see it.

## 1. `verse_context` — the per-(verse, term) anchor (D1) — ADD 4 columns
| column | type | meaning |
|---|---|---|
| `thing_type` | TEXT | ACTION / STATUS / QUALITY (the term-in-verse type, from morph) |
| `triage_status` | TEXT | ACCEPT · ESCALATE · RESEARCHER · STATE_SILENT |
| `meaning_provenance` | TEXT | mechanical · clarification:`<finding_id>` · api · researcher |
| `flagged_for_review` | INTEGER | 1 = induced / low-confidence (state-not-induce hook) |
Lexical meaning = existing `step_meaning_applied`; mode = `wa_verse_records.stem`.

## 2. `finding` — ONE level-aware finding table (D3) — NEW
The universal finding record. A **clarification is a finding** at TERM/CLUSTER/GLOBAL level (OPEN = unresolved
question, RESOLVED = applicable rule). Verse-level tier findings are findings at VERSE level.
```
id INTEGER PK
level TEXT                  -- VERSE · TERM · CLUSTER · GLOBAL
verse_context_id INTEGER    → verse_context.id      (level=VERSE)
mti_term_id INTEGER         → mti_terms.id           (level=TERM)
cluster_code TEXT           → cluster.cluster_code   (level=CLUSTER)
finding_value TEXT
finding_status TEXT         -- ANSWERED · STATED_SILENT · STATED_UNRESOLVED · OPEN · RESOLVED
provenance TEXT             -- mechanical · clarification · api · researcher
justified_by_finding_id INTEGER → finding.id   -- the clarification (higher-level finding) that justified this
supersedes_id INTEGER       → finding.id        -- correction lineage
flagged_for_review INTEGER
created_at TEXT, last_updated_date TEXT, delete_flagged INTEGER
```
- **STATE_SILENT** verse findings are stored explicitly (D5).
- **Clarification lifecycle = finding lifecycle:** a verse that can't resolve a tier → `STATED_UNRESOLVED` +
  links up to an `OPEN` term/cluster finding (the open question). When that resolves (`RESOLVED`), it becomes
  the clarification the verse findings cite via `justified_by_finding_id`. Editing/revoking it →
  re-evaluate the findings that cite it.

## 3. `finding_question_link` — M:N finding ↔ tier question (D2) — NEW
```
id INTEGER PK
finding_id INTEGER   → finding.id
question_id INTEGER  → wa_obs_question_catalogue.obs_id
coverage TEXT        -- full · partial · evidence
created_at TEXT, delete_flagged INTEGER
```
One finding may answer several tier questions; one question is answered by many findings. (Verse-level analogue
of the existing cluster-level `wa_finding_catalogue_links`.)

## 3b. `finding_verse_link` — M:N finding ↔ verse — NEW
A finding (esp. TERM/CLUSTER level, incl. migrated Session B findings) anchors to **many** verses.
```
id INTEGER PK
finding_id INTEGER       → finding.id
verse_record_id INTEGER  → wa_verse_records.id   (or reference TEXT where no row)
role TEXT                -- anchor · evidence
created_at TEXT, delete_flagged INTEGER
```
Lets verse-coverage **surface the OPEN findings anchored to the current verse** and resolve them.

## 3c. Session B reconciliation — resolve through L2 ([[feedback_session_b_findings_resolved_through_l2]])
**All Session B findings must be resolved by a finding.** Migrate `wa_session_b_findings` (2,883 active) into
`finding` as **TERM/CLUSTER-level** findings:
- **8** with `related_finding_id` → status **CLOSED** (defer to the related finding).
- **1,432** verse-anchored, unresolved → status **OPEN**; their `anchor_verses` → `finding_verse_link`. These
  are **L2 work items**: as each anchor verse is covered, the verse-read **resolves/updates** the SB finding
  (links via `justified_by_finding_id` / `supersedes_id`; status → RESOLVED).
- the rest (~1,443, mostly `resolved_qa`, non-verse-anchored) → migrate as TERM/CLUSTER findings but **not**
  part of the verse process.

This is a **data step after M56** (load SB findings into `finding` + `finding_verse_link`), reversible.

## 4. `finding_revision` — append-only history (D4) — NEW
```
id INTEGER PK
finding_id INTEGER  → finding.id
field TEXT, value_from TEXT, value_to TEXT
reason TEXT, justified_by_finding_id INTEGER → finding.id
revised_at TEXT, revised_by TEXT
```
Append-only — supports trend analysis, validation, and backtracking (D4 rationale).

## 5. Legacy reconciliation (the one open question)
`cluster_finding` (19,996) and `wa_session_b_findings` (2,883) are existing finding stores at cluster/registry
level. To honour **no-duplication**, the go-forward intent is that **`finding` becomes the single store** and
the legacy rows **migrate into it** as CLUSTER/REGISTRY-level findings — but as a **planned follow-on**, *not*
in M56 (a big-bang migration of 23k rows is risky and unrelated to standing up L2). M56 creates `finding`
for the evolved verse/term work; legacy migration is a later, separate, reversible step.
→ **Confirm:** new `finding` table now + legacy migrates in later? (recommended) — or extend a legacy table?

## 6. Migration M56 (3.29.0 → 3.30.0)
`engine/migrate.py _m56`: ALTER `verse_context` +4 cols · CREATE `finding`, `finding_question_link`,
`finding_revision` + indexes (`finding.verse_context_id`, `.level`, `.justified_by_finding_id`;
`finding_question_link.finding_id`, `.question_id`). Idempotent · own transaction · history-aware (M55
pattern). `constants.EXPECTED_SCHEMA_VERSION = "3.30.0"`. Apply: backup → `--migrate --dry-run` → review →
`--migrate` → verify.

## 7. Volume
~43k verse_contexts × ~6 L2 tiers ≈ **~260k VERSE-level findings** (incl. STATE_SILENT) + the smaller
term/cluster/global finding set. Fine for SQLite.

## Remaining confirm
- §5 legacy reconciliation: new `finding` table now, legacy migrates later — agree?
- Otherwise D1–D5 are settled and I can write M56.
