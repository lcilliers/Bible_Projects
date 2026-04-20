# Reference as Database — Design Investigation — 2026-04-20

| Field | Value |
|---|---|
| Filename | reference-as-database-design-20260420.md |
| Trigger | Researcher proposal 2026-04-20 following Claude AI review of reference-instruction gaps |
| Input document | `data/imports/WA/Workflow/methodology_logs/wa-dimreview-reference-gap-session-log-v1-20260420.md` |
| Researcher proposal | "Should we not use the database to control the references and just provide a json extract in every session to AI to ensure it always use the right references?" |
| Status | DESIGN — awaiting researcher direction on scope + sequencing |
| Produced | 2026-04-20 |

---

## 1. Digest of Claude AI's gap-analysis review

Claude AI read `wa-dimensionreview-instruction-v3_3` against `wa-reference-v5_7` and identified **12 in-scope gaps** inside the Reference's own declared scope (controlled vocabulary, schema, file-naming, patch index):

| # | Category | Gap |
|---|---|---|
| 1 | Controlled vocabulary | `dominant_subject` values (GOD / HUMAN / OTHER_HUMAN / UNSEEN / NONE) |
| 2 | Controlled vocabulary | `dimension_confidence` values (KEYWORD_WEAK / KEYWORD_STRONG / CLAUDE_AI) |
| 3 | Controlled vocabulary | `manual_override` field and values |
| 4 | Controlled vocabulary | QA flag set (QA-CLEAR, QA-TERMCENTRIC, QA-VAGUE, QA-BROAD, QA-EXTERNALISED, QA-REVIEW) |
| 5 | Schema | `word_registry.dim_review_status` column missing from §13.1 |
| 6 | Schema | `word_registry.dim_review_version` column missing from §13.1 |
| 7 | Schema | `wa_dimension_index` table missing entirely from §13 |
| 8 | Schema | `wa_dim_review_cluster_log` table missing from §13 |
| 9 | Patch index | `DIMREVIEW` patch type missing from §12 (self-declared "single navigation point") |
| 10 | Patch index | `DIMREVIEW-GRPDESC` missing from §12 |
| 11 | File naming | `wa-dim-{cluster}-...` family (11 sub-patterns) missing from §1 |
| 12 | Label convention | `DIM-{nnn}-{seq}` / `DIM-{nnn}-SD{seq}` missing from §5.4 |

Plus a structural asymmetry noted: Reference §4.3 points OUT to DimReview §7.7 as the canonical source for dimensions. The Reference is calling DimReview authoritative on vocabulary — which is the opposite direction from what "Reference is the single authority" would imply.

**Pattern diagnosis (Claude AI's reflection §6.1):**

> *"The Dimension Review instruction appears to have evolved in parallel with the Reference rather than being integrated into it."*

This is not a one-off. Every specialised instruction that adds vocabulary/tables/patch types has the same risk — and some portion of the same gap will recur with every new instruction.

---

## 2. Researcher's proposal — assessment

**Proposal:** move reference management from markdown document to database; generate a JSON extract at session start for AI to consume.

**CC endorses — strongly.** The proposal is the right architectural response to exactly the failure mode the gap analysis surfaced. Reasoning below.

### 2.1 What the DB-as-reference approach fixes

| Failure mode (current doc-based) | DB-based fix |
|---|---|
| Doc drift — doc says X, DB has Y (today's dimension-label issue) | DB IS the source; no possible drift |
| Orphan additions — new instruction adds vocabulary but doesn't update reference (Claude AI's gap list) | Every addition is a patch/migration; reference is automatically updated |
| Cross-document inconsistency (§4.3 vs §7.7 direction-of-authority) | Single canonical row per item; direction-of-authority is meaningless because there's one source |
| Validation relies on manual edits (CANONICAL_DIMENSIONS hardcoded in `apply_session_patch.py`) | Validator queries DB directly — always in sync with reference |
| Each AI session starts "do you have the latest reference?" uncertainty | JSON snapshot at session start; always current; single file to load |
| Narrative version management (v5_6 → v5_7 → v5_8...) | Reference data is versioned via existing `schema_version` + migration patterns |
| Typos / spacing variants in labels | Enforced uniqueness on DB rows; validators reject non-canonical |

### 2.2 What the approach does NOT fix

| Not fixed | Why / what to do |
|---|---|
| Narrative content (anchor verse definition, XREF architecture, process explanations) | These belong in INSTRUCTION documents (where process and explanation live), not in reference. Move narrative out of `wa-reference` into the relevant instruction docs. |
| Cross-doc pointers ("see wa-patch-instruction §6.2") | Remain as document-level pointers. The DB doesn't need to know about them. |
| Instruction-to-vocabulary mapping ("Dimension Review uses QA flags") | A thin layer of DB metadata: each vocabulary set can carry an `originating_instruction` field for traceability. Not essential. |

### 2.3 Risks and friction to consider

| Risk | Mitigation |
|---|---|
| Migration cost — current Reference has ~684 lines; some of it is taxonomic, some narrative | Split taxonomic/narrative at design time; only taxonomic goes to DB |
| "Can AI load a JSON extract at session start?" | Already the pattern for cluster extracts, pool analysis datasets, Session A extracts. Proven workflow. |
| Change-control friction — vocab changes require patches rather than doc edits | This is a FEATURE not a bug. Current doc-based change control is the source of the drift. Patches bring discipline. |
| What if the DB extract is stale? | Extractor runs at session start; never more than 5 minutes stale. Compare: current doc can be weeks out of date. |
| Governance — who can edit the reference rows? | Same discipline as any other patch — researcher approval via `apply_session_patch.py` + backup. Actually stronger than current "free-form doc edit" |

---

## 3. Proposed architecture

### 3.1 What moves to DB

| Reference content | DB representation |
|---|---|
| Controlled vocabularies (dominant_subject, dimension_confidence, session_b_status, term_owner_type, etc.) | New table `wa_vocab_set` + `wa_vocab_member` |
| QA flag sets (QA-CLEAR, QA-TERMCENTRIC, …) | Same — rows in vocab tables |
| Research-action routes (R_STEP_EXHAUST_CHECK, …) | Already DB — `wa_quality_flag_types.research_actions` |
| Q-COV catalogue questions | Already DB — `wa_obs_question_catalogue` |
| Canonical dimension vocabulary (11 labels) | New vocab set; source of truth for `CANONICAL_DIMENSIONS` validator |
| Schema column registries (dim_review_status, word_synopsis, etc.) | Query `PRAGMA table_info` at extract time — zero maintenance overhead |
| Schema table list | Same — query `sqlite_master` |
| Patch type registry (PREANALYSIS, DIMREVIEW, VERSECONTEXT, ...) | New table `wa_patch_type_registry` (code, description, session_b_status_exempt, governing_instruction, schema_affected) |
| File-naming patterns (`wa-dim-{cluster}-...`, `wa-{nnn}-...`, etc.) | New table `wa_file_name_pattern` (code, pattern, scope, description, governing_instruction) |
| Label conventions (DIM-{nnn}-SD{seq}, PH2-{nnn}-{seq}, etc.) | New table `wa_label_pattern` (entity, pattern, description, governing_instruction) |
| Cross-registry link types | Already DB — `wa_crosslink_type` |
| Flag type definitions | Already DB — `wa_quality_flag_types` |

### 3.2 What stays narrative (in instruction documents)

| Content | Home |
|---|---|
| Anchor verse definition (what is an anchor, dual purpose, minimum requirement) | `wa-dimensionreview-instruction` and `wa-versecontext-instruction` (each references per its own needs) |
| XREF architecture explanation | `wa-registry-management-guide` |
| Session B workflow narrative | `wa-sessionb-analysis-readiness` + `wa-sessionb-analysis-output` |
| Field-authority rules (e.g. "mti_term_flags is authoritative for somatic, not wa_term_inventory.somatic_link") | Move to `wa-global-general-rules` where policy lives |
| Delete_flagged discipline | `wa-global-general-rules` |
| Document validation standard | `wa-global-general-rules` |

`wa-reference` document either (a) becomes a **view** of the DB (auto-generated at reference-extract time) or (b) is deprecated entirely once the DB-extract-at-session-start pattern is proven.

### 3.3 Extract mechanism

New script: `scripts/build_reference_snapshot.py`

- Reads live DB — all reference tables + schema + patch-type registry + file-name patterns + label patterns
- Also runs `PRAGMA table_info` for every table + `sqlite_master` for table list
- Emits one JSON file: `data/exports/reference/wa-reference-snapshot-{YYYYMMDD}.json`
- Also emits a markdown view: `data/exports/reference/wa-reference-snapshot-{YYYYMMDD}.md` (for human reading / AI context if preferred)
- Session-start discipline: AI loads the snapshot in `GR-LOAD-001`-equivalent step

### 3.4 Validator mechanism

Upgrade `scripts/apply_session_patch.py`:

- Replace `CANONICAL_DIMENSIONS` hardcoded frozenset with a DB query at validator-init time
- Same pattern for every controlled vocabulary the validator checks (dominant_subject, dimension_confidence, etc.)
- Result: validator can never be out of sync with reference

### 3.5 Change control

Adding a new vocabulary member / patch type / file pattern becomes a patch operation:

- `insert into wa_vocab_member (set_id=N, value='new_code', ...)` via `apply_session_patch.py`
- Or a migration for structural changes

Per-change backup; discipline already proven by M29/M30/M31.

---

## 4. Proposed execution phases

### Phase 1 — DESIGN (this note + researcher review)

Capture the scope, identify exactly what moves to DB vs what stays narrative. Researcher reviews + approves scope.

### Phase 2 — SCHEMA DESIGN

Propose specific table shapes for `wa_vocab_set`, `wa_vocab_member`, `wa_patch_type_registry`, `wa_file_name_pattern`, `wa_label_pattern`. Researcher reviews.

### Phase 3 — MIGRATION (M32+)

Migration introduces the new tables + seeds them from the current reference content. Per-migration backup. Dry-run first.

### Phase 4 — EXTRACTOR + VALIDATOR REWIRE

Build `build_reference_snapshot.py`. Update `apply_session_patch.py` validator paths to query DB instead of hardcoded frozensets.

### Phase 5 — DOC DEPRECATION

Mark `wa-reference` document as superseded by the DB-driven snapshot. Narrative content relocated to instruction documents (per §3.2 above). Auto-generated markdown view can continue to serve human readers.

---

## 5. Pre-flight: what the DB already has vs what's new

Current DB (v3.11.0) already holds as reference data:

- ✅ `wa_quality_flag_types` (flag codes + descriptions + deprecated + research_actions)
- ✅ `wa_crosslink_type` (cross-registry link types)
- ✅ `wa_obs_question_catalogue` (194 + 12 Q-COV questions)
- ✅ `wa_flag_type_question_link` (M31 — junction)
- ✅ `prose_section_type` (section type catalogue — 26 types)
- ✅ `phase2_flag_types`
- ✅ `schema_version` (version history)

New tables needed (Phase 3 migration scope):

- `wa_vocab_set` (controlled vocabulary set registry)
- `wa_vocab_member` (individual values)
- `wa_patch_type_registry` (patch type catalogue)
- `wa_file_name_pattern` (file-naming patterns)
- `wa_label_pattern` (label conventions: DIM-, PH2-, etc.)

Existing DB queries already usable for reference extract:

- `PRAGMA table_info(<table>)` — column list per table
- `SELECT name FROM sqlite_master WHERE type='table'` — table list
- `SELECT * FROM wa_quality_flag_types` — flag code reference
- `SELECT * FROM wa_obs_question_catalogue` — catalogue questions
- etc.

Much of the reference is ALREADY queryable. The gaps Claude AI found are mostly (a) content that isn't yet registered anywhere, and (b) content that's in DB but not mirrored to the document.

---

## 6. Benefits beyond the immediate problem

1. **AI session start becomes reliable.** Every session begins with a fresh snapshot. No "wait, is the AI working from a stale reference?"
2. **Validators always current.** CC's patch validator queries the live vocabulary, not a hardcoded list. Never out of sync.
3. **Change control with discipline.** Every vocabulary addition is traceable (patch ID, timestamp, backup). Currently: someone edits a markdown doc.
4. **Programme-wide searchability.** "Where is QA-VAGUE used?" — SQL query across all reference tables + instruction docs. Currently: grep.
5. **Instruction docs focus on process.** Instructions stop duplicating reference data; they cite the authoritative source.
6. **Automated consistency tests.** CI check: any patch referencing a value not in vocab → reject. Automated. Impossible to break.
7. **Enables multi-client access.** CC + Claude AI + any future tool all query the same DB. No synchronisation needed.

---

## 7. Risks and things to decide before executing

### 7.1 Decisions awaiting researcher

| # | Decision |
|---|---|
| D-1 | **Approve the overall approach** — DB-as-reference is right for this programme |
| D-2 | **Scope of Phase 1 → Phase 3 migration** — do we move ALL 12 gap items at once, or stage (vocabularies first, patch types next, file patterns last)? |
| D-3 | **Narrative relocation** — does narrative content (anchor verse definition, XREF architecture) move to its governing instruction, stay in wa-reference, or move to a new narrative doc? |
| D-4 | **wa-reference document** — deprecate entirely after migration, or keep as auto-generated view? |
| D-5 | **Migration number** — M32 (evidence-flag redesign was M29–M31; next natural is M32) OR M33+ (reserving M32 for OT-DBR-009 mti_terms dedup that was tentatively-M32)? |

### 7.2 Risks

- **Scope creep.** This is a significant architectural change. Do it carefully.
- **Breaking existing consumers.** The Reference doc is referenced from many instruction documents. If we deprecate it, every pointer breaks until updated.
- **Narrative content loss.** Some narrative content (e.g. the anchor verse definition) should move to its authoritative instruction rather than be lost. Plan the relocation before deprecating the source.

---

## 8. Immediate possible first step (low-risk)

**Rather than a full migration today**, propose a minimal proof-of-concept:

1. Add just `wa_vocab_set` + `wa_vocab_member` (M32)
2. Seed with the 11 canonical dimension labels (the vocabulary that triggered the whole discussion)
3. Update `apply_session_patch.py::CANONICAL_DIMENSIONS` to load from DB at init
4. Generate a reference-snapshot JSON for a test C01 session

If this works cleanly, expand to patch types, file patterns, labels in successive migrations.

This deferred-scope approach tests the pattern without committing to full migration. Researcher can evaluate after Phase 1 runs.

---

## 9. Recommended next move

1. **Researcher reviews this design note.**
2. **Researcher decides §7.1 D-1..D-5.**
3. On approval:
   - Phase 2: draft schema for the new tables
   - Phase 3: M32 migration (minimum: vocab_set/vocab_member + 11 dimension labels)
   - Phase 4: rewire validator
   - Phase 5: plan narrative relocation

4. For the **immediate documentation integrity problem** — Claude AI's 12 gaps — the proposed DB approach supersedes manual patching of wa-reference with each new instruction's gaps. But in the interim: we could patch the 12 gaps into wa-reference v5_8 this session (not recommended — it recreates the exact drift problem) OR leave them in place until M32 migration lands (recommended — one-off migration vs ongoing gap-patching).

---

*Design v1 — 2026-04-20. Awaiting researcher direction on §7.1.*

---

## 10. Extensions to the design (researcher direction 2026-04-20 evening)

Two extensions proposed by the researcher that widen and consolidate the architecture:

### 10.1 Global rules also move to DB

**Proposal:** `wa-global-general-rules-v2_11-20260418.json` (currently file-based) is a reference artefact in the same sense as `wa-reference`. It should move to the DB alongside vocabularies, with AI-session exposure via JSON snapshot.

**CC endorses.** Reasoning:

- Rules file already has a **structured shape** (JSON — easier transition than markdown):
  - Each rule has `id` (e.g. `GR-LOAD-001`), `category` (e.g. `LOAD`, `REF`, `FILE`, `OBS`, `PROG`, `PROC`, `DATA`, `DIR`, `EVIDENCE`, `BACKUP`), `statement`, `rationale`, `scope`, `version`
  - Some carry `deprecated` / `superseded_by` / addendum pointers
- Same drift risks: rules are cited from many instruction docs; when a rule is added or revised, all callers may not be updated in sync
- Same validation benefit: CC can check "does this patch comply with GR-FILE-003?" via SQL rather than string-match on a JSON file

**Schema proposal** (new table):

```sql
CREATE TABLE wa_rule_registry (
    id              INTEGER PRIMARY KEY,
    rule_id         TEXT NOT NULL UNIQUE,  -- e.g. "GR-LOAD-001"
    category        TEXT NOT NULL,          -- e.g. "LOAD", "REF", "FILE"
    statement       TEXT NOT NULL,
    rationale       TEXT,
    scope           TEXT,                   -- when the rule applies
    version         TEXT NOT NULL,          -- e.g. "2.11"
    introduced_at   TEXT,                   -- ISO-8601 date rule first appeared
    deprecated      INTEGER NOT NULL DEFAULT 0,
    deprecation_note TEXT,
    superseded_by   TEXT,                   -- rule_id of replacement
    addendum_ref    TEXT,                   -- e.g. "ADD-REF-001" if absorbed from addendum
    created_at      TEXT NOT NULL,
    last_modified   TEXT
);

CREATE INDEX idx_rule_category ON wa_rule_registry(category) WHERE deprecated = 0;
```

**Rule additions/updates** become patches via `apply_session_patch.py`:

- `insert` operation for new rules
- `update` operation for revisions (increments version; records supersedes chain)
- `deprecate` operation for retirement (sets `deprecated=1`, optionally `superseded_by`)

**Session-start exposure:** `build_reference_snapshot.py` includes a `rules` section in the JSON output. AI loads it at GR-LOAD-001-equivalent step.

### 10.2 Programme-wide narrative content consolidated in prose infrastructure

**Proposal:** narrative content currently living in `wa-reference` (and parts of global rules addenda) — anchor verse definition, XREF architecture, document validation standard, field-authority policies — move into the prose store (M20 infrastructure), rather than back to instruction documents as §3.2 of this note originally proposed.

**CC endorses — stronger than the original §3.2 proposal.** Reasoning:

- The prose store already exists, is schema-canonical, is FTS5-searchable, supports version/supersede chain, and has round-trip markdown editing via PROSE_SECTION markers
- Putting programme-wide narrative there gives it the same integrity discipline as Session A/B/C/D analytical prose
- Cross-topic discovery works: "search prose for anchor verse" returns the programme-wide definition AND every Session A/B section that mentions it
- New section types seed the space cleanly

**Schema additions to prose store** (M20 already defines `source_stage`; add new value + new section types):

New `source_stage = 'programme'`. Seed 6–10 programme-wide narrative section types, for example:

| Code | Label | Content |
|---|---|---|
| `prog_anchor_verse` | Programme — Anchor Verse Definition | Canonical definition, dual purpose, minimum requirement |
| `prog_xref_architecture` | Programme — XREF Architecture | OWNER/XREF semantics; verse_context inheritance; canonical-row rule |
| `prog_validation_standard` | Programme — Document Validation Standard | Inflection point completeness; gap status discipline; cross-doc consistency |
| `prog_delete_discipline` | Programme — Delete-Flagged Discipline | Soft-delete rules; cascade rules |
| `prog_field_authority` | Programme — Field Authority Rules | mti_term_flags canonical sites; deprecation notes |
| `prog_backup_discipline` | Programme — Backup Discipline | Per-migration; per-patch; 6-month retention |
| `prog_patch_failure_protocol` | Programme — Patch Failure / REPAIR Protocol | What to do when a patch is rejected |
| `prog_instruction_override_protocol` | Programme — Instruction Override Protocol | How overrides are declared and logged (per today's handoff convention) |

**Benefits of this home:**

- Narrative becomes versioned like analytical prose
- FTS5 search across programme narrative (no more `grep` across instruction docs)
- Round-trip editing via `.md` files with PROSE_SECTION markers — the same workflow researchers already use for session outputs
- AI can be given a topic-filtered prose snapshot ("give me everything programme-wide about anchor verses") rather than loading the entire reference
- Instruction documents become shorter, focused on process — they POINT AT the programme-wide narrative rather than duplicating it

### 10.3 Three-layer reference architecture (consolidated)

| Layer | Content type | Storage | Integrity mechanism | AI session-start access |
|---|---|---|---|---|
| **L1 Taxonomic** | Vocabularies, schema registry, patch types, file/label patterns, global rules | DB tables | Patch/migration discipline + CC validators | JSON snapshot |
| **L2 Narrative** | Programme-wide policies, architecture definitions, cross-stage discipline statements | Prose store (`source_stage = 'programme'`) | Supersede chain + FTS5 + PROSE_SECTION markers | Prose snapshot (topic-filtered optional) |
| **L3 Process** | Workflow instructions (DimReview, VC, Session B/C/D, Patch, Directive, CC) | Markdown instruction documents | Version stamping + `[current]` pointer convention | Load on demand per workflow |

The three layers map to three different questions an AI or human reader is asking:

- **L1:** "What values/codes/patterns exist? Is this one valid?" — fast lookup, machine-validatable
- **L2:** "What is the programme's policy / definition / architecture on topic X?" — readable narrative, topic-searchable
- **L3:** "How do I execute workflow Y?" — procedural, step-by-step, version-pinned

**Current `wa-reference` document conflates L1 and L2** (§1 file naming is taxonomy; §16 anchor verse definition is narrative; §18 validation standard is narrative). Separating them is the core architectural move.

### 10.4 Migration scope implications

Phased migration under the 3-layer model:

| Phase | Scope | Migration |
|---|---|---|
| **M32 (L1 vocabulary seed)** | `wa_vocab_set` + `wa_vocab_member`; seed 11 dimensions + 10-ish other vocabularies | Low-risk POC |
| **M33 (L1 rule registry)** | `wa_rule_registry`; seed from current `wa-global-general-rules-v2_11-20260418.json` | Medium-risk — rule file has ~40+ rules |
| **M34 (L2 programme prose)** | Extend prose store with `source_stage='programme'` + seed 6-10 section types | Schema touch + seeding |
| **M35 (L1 remaining taxonomy)** | `wa_patch_type_registry`, `wa_file_name_pattern`, `wa_label_pattern` | Depends on scope decision D-2 |
| **Post-M35** | Populate L2 programme prose by migrating narrative from wa-reference | Series of PROSE patches |
| **Post-migration** | Deprecate `wa-reference` document (or auto-generate from L1+L2) | Documentation cleanup |

Each migration has its own dry-run + backup discipline per M19-M31 precedent.

### 10.5 Updated decision matrix (supersedes §7.1)

| # | Decision |
|---|---|
| D-1 | Approve the 3-layer architecture (L1 DB / L2 prose / L3 instructions) |
| D-2 | Scope + sequencing — stage through M32–M35 as above, or bundle differently? |
| D-3 | L1 scope — include global rules (M33), patch types, file patterns, label patterns in addition to vocabularies? |
| D-4 | L2 scope — which programme-wide narratives move to prose store; what section types to seed |
| D-5 | Instruction document contract — do we require every instruction doc that previously duplicated L1/L2 content to update its pointers post-migration? When? |
| D-6 | `wa-reference` document — deprecate + remove after M32–M35, or auto-regenerate from L1 + L2 for backward compat with external consumers? |
| D-7 | First-migration POC — confirm minimum M32 (vocab_set/member + 11 dimensions) as the starting step? |

### 10.6 Immediate feasibility note

Both extensions are tractable. No architectural blockers. The rules file being JSON already makes L1 rule-registry seeding straightforward. The prose store being live (v3.11.0) makes L2 extension a low-risk ALTER + INSERT operation.

The ~40+ global rules are small compared to the reference document's 684 lines — most of the effort is schema design and seeding.

---

*v1.1 — 2026-04-20 evening. Two extensions absorbed (L1 adds global rules; L2 goes to prose store). Three-layer architecture consolidated.*
