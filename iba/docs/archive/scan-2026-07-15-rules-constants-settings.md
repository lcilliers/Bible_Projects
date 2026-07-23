# Re-scan B — Global rules, patterns, constants, settings (2026-07-15)

> Raw findings from the re-scan requested by the researcher 2026-07-15, run against `Workflow/Global_rules/`, `Workflow/reference/`, `Workflow/registry/`, `engine/constants.py`, `docs/file-organisation-rules.md`, `docs/interaction-preferences.md`, and the backup/mirror scripts.
>
> **Source material, not config.** Companion to [scan-2026-07-15-instructions-catalogue.md](scan-2026-07-15-instructions-catalogue.md).

## ★★ The finding that mattered — `.env` is a loaded gun

The first STEP audit (earlier today) read `.env`'s **key names** by grep and never read its **values**. The re-scan read the values.

| key | `.env` actually holds | the client hard-codes |
|---|---|---|
| `STEP_API_BASE_URL` | `https://www.stepbible.org/api` — **the REMOTE public API** | `http://localhost:8989` — **LOCAL** |
| `STEP_DEFAULT_VERSION` | `ESV` — **UNTAGGED** | `ESV_th` — **TAGGED** |
| `STEP_REQUEST_TIMEOUT` | `10` | `30` |

**The only reason this study has tagged data is that the client ignores its own configuration.**

`.env` is configured for exactly what `docs/step_setup.md` instructs — the remote public API with plain ESV. The client ignores `.env` entirely. Make the client read its configuration, change nothing else, and the study silently loses every Strong's number and every morph code it depends on. No error at any layer; a well-formed 200 with correct-looking English text.

**`step.connection` v1 ruled precisely that change** — *"the client is rewritten to read them; .env is NOT bent to match the client."* The rule was authored from a grep of key names. It took reading the values to see it was a loaded gun. **Corrected at `config_version` 0.1.4**: names from `.env`, **values from the client**, `.env`'s values are wrong and must be corrected **first**, before any client rewrite. `gate.step.env-parity` v2 now checks values, not just names.

*A config audit that reads names and not values is not an audit.*

## Global rules — 34 active, 12 categories

`Workflow/Global_rules/wa-global-rules-extract-20260427.json` (schema 3.17.0, generated from DB `wa_rule_registry`; **DB is source of truth post-M33 — the JSON is a build artefact, not the master**).

**Session/discipline:** GR-LOAD-001 (3-step startup, non-waivable) · GR-OBS-001 (obslog authoritative; researcher feedback captured **verbatim before responding**) · GR-CAD-001 (self-check every substantive response, non-waivable) · GR-TEMPO-001 (obslog write precedes chat response; meta-work is substantive) · GR-RD-007 (obslog carries detail, chat is alert-only, raise-when-arising) · GR-PASS-001 · GR-HF-001 (help-forward restrained by default).

**Data:** GR-DATA-001 (`status IN ('extracted','extracted_thin')` on every active-term query — non-waivable) · GR-DATA-002 · GR-DATA-003 (`mti_term_flags` authoritative for somatic, not `wa_term_inventory.somatic_link`) · GR-DATA-004 · GR-DATA-005 (`god_as_subject` + `somatic_link` **high error rate — verify against verse evidence**) · GR-DB-001 (no DB state assumptions; **memory of a DB fact is an assumption**).

**Document:** GR-REF-001 (single-authority referencing, 5 disciplines, + the **content-authority map**) · GR-REF-002 (`[current]` resolves to highest version; provenance refs pin).

**File naming:** GR-FILE-001 (`[prefix]-[reference]-[description]-[version]-[date]`) · GR-FILE-002 (description **max 30 chars**) · GR-FILE-003 (version `v{major}_{minor}`, **both always**) · GR-FILE-005 (**JSON structured / md descriptive / docx-PDF on request only**) · GR-FILE-006 (prefixes: `wa-global`, `wa-023`, `wa-c17`, `wa-sd`, `wa-vcb-001`) · GR-FILE-007 (**fully lowercase**) · GR-FILE-008 (dual-write to `/home/claude` + `/mnt/user-data/outputs/`) · GR-FILE-009 (compact `YYYYMMDD` in filenames).

**Process:** GR-PROC-001 (step incomplete until output exists AND is validated) · GR-PROC-002 (findings trace to a source **or are labelled hypothesis**) · GR-PROC-004 (**no patch or directive without researcher review — without exception**).

**Programme:** GR-PROG-001 (**verse always leads**) · GR-PROG-002 (the governing question) · GR-PROG-003 (dimensions data-derived, grounded in ≥1 verse) · GR-PROG-004 · GR-PROG-005 (**two-AI split; patches + directives are the SOLE DB-change mechanisms**) · GR-PROG-006 (characteristic-centric grouping) · GR-PROG-007 (relevance filter at **term level**, not verse theme) · GR-PROG-009 (**inferential ≠ confirmed; must be labelled**).

⚠ **GR-FILE-008 is environment-legacy** — `/home/claude` and `/mnt/user-data/outputs/` are Claude-AI-sandbox paths, not this machine. Encoding it verbatim would encode a dead rule.

## Programme flags — 15; and CLAUDE.md is stale on the one that matters

`archive/Sessions/wa-global-flags-v1_6-20260420.md`. Open 6 · Resolved 6 · Obsolete 3 · Standing 0.

⚠ **FLAG-010 is OBSOLETE, and its blocking gate on new word analysis was explicitly LIFTED on 2026-04-20. No open flag currently gates programme operations.** CLAUDE.md §10 still lists "FLAG-010 = blocking gate" as live. *(Not fixing old docs, per the researcher's ruling — recorded so the configurator does not inherit it.)*

Open: FLAG-001 (Session C instruction deferred) · FLAG-006 (Session D output format) · FLAG-007 (SB_* codes) · FLAG-011 (retire cc-instructions-v3_6) · FLAG-013 · FLAG-014.

## Patterns — all generated from the DB

| register | count | source table |
|---|---:|---|
| label patterns | 11 | `wa_label_pattern` (M35) |
| file patterns | 23 | `wa_file_name_pattern` (M35) |
| patch types | 15 | `wa_patch_type_registry` (M35) |
| global rules | 34 | `wa_rule_registry` (M33) |

**All four extracts say the DB is source of truth.** A config-driven app must treat these JSON files as **build artefacts, not masters** — and that is a direct conflict with the configurator's own claim to be the single home for rules. → **new reconciliation needed.**

**Labels:** `PATCH-{YYYYMMDD}-{NNN}-{TYPE}-V{n}` · `DIR-{YYYYMMDD}-{NNN}` · `DIM-{registry}-{NNN}` · `DIM-{registry}-SD{NNN}` · `PH2-{registry}-{NNN}` · `{mti_term_id}-{NNN}` · `Q-COV-01..12` · `VCB-{NNN}` · 2 legacy patterns pending reconciliation.

**Patch types:** `session_b_status` **required** for PREANALYSIS + SESSIONB; **exempt** for the other 13.

## Constants — `engine/constants.py`

| constant | value |
|---|---|
| `EXPECTED_SCHEMA_VERSION` | **3.40.0** *(CLAUDE.md §4 says 3.33.0 — stale)* |
| `LOCK_SENTINEL` | `"In Progress"` (title case + space; `IN_PROGRESS` never matched — RD-DBR-001) |
| `STALE_LOCK_SECONDS` | 7200 |
| `BACKUP_RETENTION` | 10 |
| `HIGH_FREQ_THRESHOLD` | 500 |
| `THIN_DATA_THRESHOLD` | 20 |
| `SMALL_VERSE_SAMPLE_THRESHOLD` | 5 |
| `VERSE_OCCURRENCE_RATIO_THRESHOLD` | 0.15 (WR-08) |
| `VERSE_OCCURRENCE_MIN_COUNT` | 20 (WR-08) |
| `AUDITED_SENTINEL` · `ENGINE_VERSION` · `PARSER_VERSION` · `SPECIFICATION` · `LANG_PREFIX` | sentinels/versions |

⚠ **Governance debt noted in the file itself:** M64–M66 were applied by scripts and **never registered in `engine/migrate.py`**; the constant is kept in sync **by hand** so the A2 gate passes. A schema gate maintained manually is a gate that passes because someone remembered.

## Backup / retention — `scripts/backup_db_to_nas.py`

Grandfather-father-son, kept if it satisfies **any** tier: `KEEP_RECENT` **24** · `KEEP_DAILY` **30** · `KEEP_WEEKLY` **26**. `MIN_PLAUSIBLE_BYTES` **50 MB**.

**Safety invariants worth encoding as-is** — this script is the most defensively-written thing in the repo: source opened read-only + `PRAGMA integrity_check` → SQLite online-backup API → temp → integrity-check → copy → **sha256 byte-for-byte verify** → prune. **An abort prunes NOTHING** — a broken DB can never prune away good backups. Exit codes 0/2/3/4/5/6/7 distinguish every failure mode.

Mirror: robocopy `/MIR`, two trees (repo + `.claude` memory), **rc 0–7 = success, ≥8 = failure**, log written outside the repo so it does not churn the mirror.

## Model / cost

`MODEL = "claude-sonnet-4-6"` — **hardcoded** in `scripts/_apply_verse_read_meaning.py`; a CLI default in one other script. **No cost, price, budget or model-tier configuration exists anywhere in the repo.**

Plan §2.5 rules: *"the interpretive reads use the cheapest model that produces valid results, with the model tier re-selectable via the configurator."* Nothing of that exists yet — the tier is a constant in a script.

## Filing — two version conventions that conflict

⚠ **GR-FILE-003** mandates `v{major}_{minor}`, both components, for all files. **`docs/file-organisation-rules.md` §2.1/§2.3** uses single-integer `-v{n}` for session artefacts and reserves `v{major}_{minor}` for `WA-` governing docs. **These are two pattern classes, and the config must model both** — not silently pick one. *(This session's own docs used `-v{n}`.)*

Other filing rules: **living documents** (§2.3a) carry no `-vN` and no date — one stable filename, integer `Doc version:` in the header, git is the history. Zero-pad: **registry → 3 digits**, **chapter+verse → 3 digits**, **version integers explicitly no leading zero**. Same-day revision increments; **new day resets to v1**. 8 archiving triggers. Manifest `currency` enum: current · cross-reference · historical · backup · archived · other.

## ⚠ New reconciliations this scan forces

1. **`.env` values vs client values** — *resolved at 0.1.4*, but `.env` itself still holds the wrong values. **The repair is outstanding, and its order matters: fix `.env` first, then the client.**
2. **DB-vs-config authority for the four pattern registers.** All four extracts declare the DB (`wa_rule_registry`, `wa_file_name_pattern`, `wa_label_pattern`, `wa_patch_type_registry`) the source of truth. The configurator claims to be the single home for rules. **Both cannot be true.** Recommendation: the new configurator supersedes them — those tables belong to the *old* DB and the plan does not migrate config (§3.4.1: *"Config/control — New (author fresh)"*). But it must be said, or the old tables silently remain authoritative for anyone who reads their canonical note.
3. **Two version conventions** (GR-FILE-003 vs file-organisation-rules) — two pattern classes, needs a ruling.
4. **GR-FILE-008 dual-write** is environment-legacy (Claude-AI sandbox paths). Mark LEGACY, do not encode.
5. **FLAG-010's blocking gate was lifted 2026-04-20** but CLAUDE.md still presents it as live. The configurator must take the flag register's state, not the compact reference's.

## Disposition

- `wide/governance.json` *(pending)* — 34 GR-* rules, 15 FLAG-*, interaction protocols, the content-authority map
- `wide/patterns.json` *(pending)* — 23 file patterns, 11 label patterns, 15 patch types, both version conventions, zero-pad rules
- `wide/settings.json` *(pending)* — every `engine/constants.py` value, backup retention (24/30/26/50MB), model tier, budget caps
- `utility/filing.json` *(pending)* — archiving triggers, living-doc rule, manifest currency enum
- `utility/git.json` *(pending)* — commit cadence
- `utility/db.json` *(pending)* — the backup/restore safety invariants (they are the best-engineered controls in the repo)
- `wide/reconciliations.json` — items 1–5 above
