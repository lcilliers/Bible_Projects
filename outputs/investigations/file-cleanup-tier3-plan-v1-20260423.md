# File Cleanup Tier 3 — Plan C/D/E (2026-04-23)

**Status:** AWAITING APPROVAL.
**Precursors (done):** Tier 1 (`a2a516c`), Tier 2 dry-run + Tier 3 Stage A/B (`6781567`).

This plan covers the remaining Tier 3 work:
- **Stage C** — non-compliant individual files in `Session_B/`.
- **Stage D** — restructure `data/imports/WA/Prose/`.
- **Stage E** — update `docs/file-organisation-rules.md` to cover `reference/` and `Prose/` with their new roles.

Word_Data is explicitly left alone (researcher wants it adopted into Prose before archiving).

---

## Stage C — Session_B non-compliant files

Current contents of `data/imports/WA/Workflow/Framework_B/Session_B/` (active folder only, not archive). Issues flagged below.

### C.1 Simple renames (no semantic change — propose I execute on approval)

| Current | Proposed | Issue |
|---|---|---|
| `wa-word-study-template-v2-2026-04-13.md` | `wa-word-study-template-v2-20260413.md` | Hyphenated date → compact format per §2.1. |
| `wa-global-sessionc-prose-rule-v1.1-20260414.md` | `wa-global-sessionc-prose-rule-v1_1-20260414.md` | Dot version → underscore per §2.1. |

### C.2 Files needing your judgment

**`Session-A-Instruction-v8-final.docx`** — uppercase, no date, "v8-final" suffix, `.docx` format. Looks like the historical Session A instruction that predates the current naming convention. Three options:

- **Option A** — archive to `Session_B/archive/` as historical (this instruction has been superseded by the rules/reference database extracts, if I'm reading your intent correctly).
- **Option B** — rename in place: `wa-sessiona-instruction-v8-20260318.md` (needs date; would need to check the file's actual date from its content or git history).
- **Option C** — leave it.

My read: **Option A** if Session A is now operationalised through the engine (no standalone instruction doc needed), otherwise Option B.

### C.3 DB-derived extracts in Session_B/ — versioning question

Four files in Session_B/ are DB-derived extracts, currently named `{stem}-{YYYYMMDD}.{ext}` without an explicit `-v{n}-`:

| File |
|---|
| `wa-global-rules-extract-20260421.json` |
| `wa-reference-snapshot-20260421.json` |
| `wa-programme-prose-extract-20260423.json` |
| `database-schema-v3.14.0-20260421.json` |

Your instruction: _"the files in the workflow instructions must be versioned."_ Three readings:

- **Reading A (strict)** — add `-v1-` before the date to every extract file: `wa-global-rules-extract-v1-20260421.json`. Requires updating the extractor scripts' output naming.
- **Reading B (date-as-version)** — date-only is sufficient for daily-regenerable extracts; no action. The extractor already embeds the date.
- **Reading C (semver-in-name)** — the schema file (`database-schema-v3.14.0-20260421.json`) already has a semver in its stem. Apply the same pattern to the others where they represent a versioned snapshot of DB state rather than a per-day output.

My recommendation: **Reading B** — the date is the version for daily-regenerable extracts, and Reading A would require script changes without a clear analytical benefit. Happy to revisit if you'd prefer Reading A.

---

## Stage D — Prose folder restructure

Currently flat: 48 files in `data/imports/WA/Prose/`. These fall into five clear classes. Proposed structure:

```
data/imports/WA/Prose/
├── drafts/                    # authoring scratchpads (v1/v2/v3 of each section)
├── patches/                   # catalogue + PROSE JSON patches ready to apply
├── logs/                      # obslogs + session logs for the prose work
├── reference/                 # review, style/approach, records-list
├── directives/                # wa-global-dir-002-* directives
└── archive/                   # superseded drafts (moved on pass close)
```

### D.1 Proposed moves

| Bucket | Files (current names) | Target |
|---|---|---|
| **drafts/** | All `wa-prose-draft-*.md` (21 files), `wa-prose-corpus-assembly-*.md` (3 files) | `Prose/drafts/` |
| **patches/** | `wa-catalogue-prose-programme-ch2-v1-20260422.json`, `wa-catalogue-prose-programme-ch3-v1-20260422.json`, `wa-prose-catalogue-chapter0-1-v1-20260421.json`, `wa-prose-programme-ch2-v1-20260422.json`, `wa-prose-programme-ch3-v1-20260422.json`, `wa-prose-programme-chapter0-1-v1-20260421.json` (6 files) | `Prose/patches/` |
| **logs/** | `wa-prose-obslog-v1-20260421.md`, `wa-prose-obslog-v2-20260421.md`, `wa-prose-session-log-v1-20260421.md`, `wa-prose-session-log-v2-20260422.md`, `wa-prose-records-list-v1-20260421.md`, `wa-prose-ch3-obslog-v1_0-20260422.md`, `wa-prose-ch3-session-log-v1_0-20260423.md` (7 files) | `Prose/logs/` |
| **reference/** | `wa-prose-framework-review-v1-20260421.md`, `wa-prose-style-and-approach-v1-20260422.md` (2 files) | `Prose/reference/` |
| **directives/** | `wa-global-dir-002-prose-reg-nullable-v1-20260421.md`, `wa-global-dir-002-submission-v1-20260421.md` (2 files) | `Prose/directives/` |

Total: 48 files → 5 subfolders. No files are archived in this stage — the drafts that have a v3 don't automatically archive v1/v2 because you may still be iterating; `archive/` gets populated later at pass close.

### D.2 Same-day version consolidation — optional

If you want to archive superseded-within-day versions now:

| Current | Keep | Archive |
|---|---|---|
| `wa-prose-corpus-assembly-v{1,2,3}-*.md` | v3 (20260422) | v1, v2 (20260421) |
| `wa-prose-draft-key-constraints-v{1,2,3}-*.md` | v3 | v1, v2 |
| `wa-prose-draft-key-principles-v{1,2,3}-*.md` | v3 | v1, v2 |
| `wa-prose-draft-method-overview-v{1,2}-*.md` | v2 | v1 |
| `wa-prose-draft-preamble-v{1,2,3}-*.md` | v3 | v1, v2 |
| `wa-prose-draft-programme-flow-v{1,2}-*.md` | v2 | v1 |
| `wa-prose-draft-publishing-v{1,2}-*.md` | v2 | v1 |
| `wa-prose-draft-purp-mission-v{1,2}-*.md` | v2 | v1 |
| `wa-prose-draft-registry-construction-v{1,2}-*.md` | v2 | v1 |
| `wa-prose-draft-science-in-action-v{1,2,3}-*.md` | v3 | v1, v2 |

Would move ~18 superseded drafts to `Prose/drafts/archive/`. Do this now or wait for a pass-close ceremony?

### D.3 `wa-prose-ch3-session-log-v1_0-20260423.md` — naming variant

Uses `v1_0` (two decimals) rather than `v1` (integer) — consistent with the session logs in `Sessionlogs/`. Leave as-is unless we decide to standardise the version format across the programme.

---

## Stage E — Update `docs/file-organisation-rules.md`

### E.1 Add §3.16 — `data/imports/WA/Prose/`

```markdown
### 3.16 `data/imports/WA/Prose/`

Authoring workspace for programme-wide prose. All programme-stage PROSE
patches are drafted here before application; obslogs and session logs for
prose passes are recorded here; the authoring style/approach documents and
framework review live here.

| Subfolder | What goes here | Naming pattern |
|-----------|---------------|----------------|
| `Prose/drafts/` | Draft prose (v1/v2/v3 iterations per section) | `wa-prose-draft-{topic}-v{n}-{YYYYMMDD}.md` |
| `Prose/patches/` | CATALOGUE_POPULATION + PROSE JSON patches before application | `wa-catalogue-prose-{scope}-v{n}-{YYYYMMDD}.json`, `wa-prose-programme-{scope}-v{n}-{YYYYMMDD}.json` |
| `Prose/logs/` | Obslogs and session logs for prose passes | `wa-prose-{scope}-obslog-v{n}-{YYYYMMDD}.md`, `wa-prose-{scope}-session-log-v{n}-{YYYYMMDD}.md` |
| `Prose/reference/` | Style guides, approach docs, framework reviews | `wa-prose-{topic}-v{n}-{YYYYMMDD}.md` |
| `Prose/directives/` | Prose-related directives (e.g. schema enablement) | `wa-global-dir-{id}-{topic}-v{n}-{YYYYMMDD}.md` |
| `Prose/archive/` | Superseded draft versions at pass close | |

**Lifecycle:** Drafts iterate in `drafts/` until the PROSE patch is prepared
in `patches/`, applied via `scripts/apply_session_patch.py`, and archived to
`archive/patches/`. Prior draft versions (v1, v2) move to `Prose/archive/`
at pass close. Logs stay in `Prose/logs/` as topical historical records.
```

### E.2 Add §3.17 — `data/exports/reference/`

```markdown
### 3.17 `data/exports/reference/`

DB-canonical extracts of reference data — rules, controlled vocabulary,
patch types, file patterns, label patterns, reference snapshot, programme
prose extract. Produced by the respective extract scripts (e.g.
`scripts/build_programme_prose_extract.py`). The latest extract is the
authoritative source and is also copied into `data/imports/WA/Workflow/
Framework_B/Session_B/` where it serves as the current instruction for
authoring sessions.

**Archiving:** When a new extract supersedes a prior dated extract of the
same stem, the prior extract moves to `data/exports/reference/archive/`.
Corresponding `.json` + `.md` move together.

**Not here:** STEP Extracts (→ `data/exports/STEP Extracts/`), Session B
extracts (→ `data/exports/session_b_extracts/`).
```

### E.3 Update §3.7 — `Session_B/` DB-extract policy

Add a paragraph:

```markdown
**DB-derived extracts:** Latest extracts from `data/exports/reference/`
that serve as authoritative instruction input (rules, reference snapshot,
programme prose, database schema) are copied into Session_B/ when a new
version is produced. Prior copies in Session_B/ move to
`Session_B/archive/`. Extracts are dated; explicit `-v{n}-` is not
required in the filename where date-only versioning is the convention
(see `data/exports/reference/` §3.17).
```

---

## Proposed execution order

1. **C.1** — two renames (hyphenated date, dot version). Mechanical. _Execute on approval._
2. **D.1** — 48 files into 5 Prose subfolders. Mechanical once approved. _Execute on approval._
3. **E** — rules update. Commit together with D.1 so the new Prose structure is documented at the same time it lands.
4. **C.2 (`Session-A-Instruction-v8-final.docx`)** — decide Option A/B/C first, then act.
5. **C.3 (DB-extract versioning)** — decide reading A/B/C first, then (if action needed) update extractor scripts and rename existing files.
6. **D.2 (same-day draft archiving)** — decide whether to archive now or at pass close.

---

*Plan produced 2026-04-23 to complete Tier 3 of the file cleanup under `docs/file-organisation-rules.md`.*
