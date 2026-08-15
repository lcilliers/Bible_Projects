# Session Log - 2026-08-15 - Project sanity check and alignment kickoff

## Session scope

Requested sanity check on the whole project (main study + IBA sub-app) for state of maintenance
and coherency. The researcher's review of that check corrected the working picture of the project
in several material ways, then authorised the first step of a resulting consolidation/alignment
plan as a controlled, ongoing process. This log covers both halves.

## Sanity check findings (`outputs/markdown/project-sanity-check-20260815.md`)

- **Git backlog:** the 2026-08-14 prose-hierarchy/revision-workflow session was fully completed
  but never committed — 56 files sitting uncommitted since commit `aab47254` (2026-08-13). Closed
  this session with a catch-up commit (`00bc047c`), including a `.gitignore` tightening (blanket
  `.obsidian/` ignore).
- **IBA app:** found internally coherent — clean git state, `governance.build_md_on_code_change`
  and `governance_md_on_rule_change` both live and actually followed, `EXPECTED_SCHEMA_VERSION` in
  code matching the DB's latest migration. No action needed there.
- **Repo hygiene:** flagged (not yet all resolved) `.obsidian/` untracked state, VS Code SQLite
  scratch files sitting in `database/scripts/`, a stray `query_db.py` at repo root.
- **One open question surfaced rather than resolved:** whether 2026-08-14's main-DB prose work was
  in-scope relative to the "study closed 2026-08-03 / IBA reopened 2026-08-05" memory. This
  triggered the researcher's correction below.

## Researcher correction — project status and architecture

The researcher's review (filed at
`Workflow/Chat_responses/#  biblestudyproject - review notes.txt`) corrected the working memory
of project status, which had become fragmented:

- The project has been **live and actively engaged with since February 2026** — not closed. The
  2026-08-03 closure was of the old AI-driven analysis method specifically, not the whole project.
- **~1 month before this session, the IBA app was built** as an integrated operational platform.
  It now **owns the entire process-control machine and the base data layer** — the full cycle from
  word initiation (STEP) through verse-lexical analysis is completely migrated to `iba.db`. Old-DB
  instructions/scripts pointing to that layer are now redundant.
- **`database/bible_research.db` retains two things that are NOT redundant**: the entire prose
  section, and all findings/analysis tables and files. The 2026-08-14 prose work was legitimate,
  integral, ongoing project work — the sanity check's open question is resolved: no scope
  violation occurred.
- The project is currently **preparing to restart the findings/analysis stage** and evaluating
  methods for it.
- **Two-database split confirmed in principle**: `bible_research.db` = analytic output + prose
  (the canonical story); `iba.db` = process control + base data layer. If the split holds up,
  the base layer will eventually be removed from `bible_research.db` and remaining process-control
  machinery consolidated into IBA.

Memory updated to reflect this as the current-status record, superseding the fragmented framing
(closure/reopening memories kept as accurate history, not current state):
`project_current_architecture_and_status_20260815`, plus supporting memories on the DB-visibility
trust gap (`feedback_verify_db_claims_via_visible_tooling`), the researcher's existing
`Workflow/Chat_responses/` notes pattern (`reference_chat_responses_notes_location`), and the
alignment-process discipline (`feedback_alignment_work_is_register_driven_plan_gated`).

## Claude Code vs Claude API

Answered directly (`outputs/markdown/project-review-response-2-20260815.md` §1): repeatable,
rule-bound work packages should be config-driven direct Claude API calls from IBA app code
(structured outputs via `output_config.format`, rules/schema in `cfg_*`), routed through the same
`cfg_step`/`cfg_utility` registration as any other IBA script. General enquiries, investigation,
and judgment calls stay in Claude Code chat, which already has full DB/file access — confirmed
there is no remaining reason to use Claude AI desktop for this project's work, with one caveat: a
direct API integration needs its own `ANTHROPIC_API_KEY`/`ant auth login` credential, separate
from the Claude Code subscription.

## Housekeeping actions taken

- `file_manifest.json` rebuilt (`python scripts/build_file_manifest.py`) — was stale since
  2026-07-23. Now 18,640 files tracked (10,086 active / 8,554 archived). Noted for the record:
  the manifest indexes filenames/metadata only, not file contents — the researcher's ask to find
  files by keyword/Strong's reference is a different mechanism, out of scope for today, folded
  into the file-store-consolidation step below.
- VS Code SQLite-extension scratch queries relocated from `database/scripts/` to `scripts/`,
  renamed with an `SQLite_` prefix and corrected DB-relative paths per the researcher's naming
  instruction: `SQLite_prose_section_type_list.sqlite3-query`,
  `SQLite_prose_section_type_with_body.sqlite3-query`,
  `SQLite_programme_prose_body_export.sqlite3-query`. `.gitignore`'s now-moot ignore rule for the
  old location removed — these are tracked going forward, per instruction to save
  exploration/extraction scripts to `scripts/` as a standing practice.
- Two guides written per direct request:
  - `Workflow/Obsidian/obsidian-usage-guide-v1-20260815.md` — single-vault-at-root recommendation,
    frontmatter/tagging convention, backlinks/graph as the actual navigation fix, and an explicit
    caution that Obsidian is a reading layer, never a second source of truth over the DB.
  - `Workflow/SQLite/sqlite-extension-best-practice-v1-20260815.md` — names the researcher's
    stated trust gap directly (Claude's DB reporting has misled him before) and sets the
    verify-don't-just-trust practice, plus read-only-by-default against `iba.db` (active WAL
    writes) and a hard rule against using the extension to bypass the governed write paths
    (`apply_session_patch.py` / `Config-Maintenance.ps1 -Step Propose`).

## Governance-alignment register opened

`docs/governance-alignment-register.md` created as the living, ongoing tracking mechanism the
researcher required before any alignment work proceeds: "keep a register of alignments in
progress... Ask and challenge... done with consideration." Status model: `Proposed → Approved →
Applied → Verified`, nothing advances without an explicit researcher decision recorded in the
register.

**First item logged, status `Proposed`, not applied:** `CLAUDE.md` §4/§5/§7/§8 still present the
old `engine/`/STEP pipeline as the live, authoritative route for base-layer work. Proposed fix is
a superseded-by banner (matching the file's own existing convention for prior method-reset
pivots) marking those sections provenance-only and pointing to `iba/app/USER-GUIDE.md` — awaiting
approval before any edit.

**Second item logged:** filing/archiving rules should be config-defined per the researcher's own
framing — recommended folding into the file-store-consolidation step rather than running as a
separate thread; researcher agreed.

## Revised alignment plan (researcher's own sequencing, 2026-08-15)

The originally-proposed 5-step order was reordered on the researcher's instruction:

1. **Align governance/docs** — in progress via the register above.
2. **Consolidate the file store** (moved up from last) — folds in the manifest content-search gap
   and the filing/archiving-rules review.
3. **Merge the IBA windows-debate work with prose** → one consolidated analytics methodology,
   replacing current prose sections and updating related `Workflow/` instructions + IBA configs.
   Explicit scope note: the base-layer (STEP→lexical) portion needs documentation only — record
   the change IBA brought about, don't re-derive the how-to; the real critical-review/redesign
   work is on the analytics/synthesis side (old Session B/C/D).
4. **DB-split formalisation checkpoint** — removing the base layer from `bible_research.db` once
   the split is proven in practice.
5. **Merge findings into prose** (moved to last, explicitly not started) — needs its own fully
   detailed plan before any prose change in the Findings book; "a lot of thought must go into it."

**Standing rule for all five steps, restated because it governs everything that follows:** each
step needs its own fully detailed plan submitted for researcher review and approval before any
update takes place. This session's work stops at that gate — no step-1 edit has been applied, no
step-2 through step-5 work has started.

## Commits this session

- `00bc047c` — catch-up commit for the 2026-08-14 prose-hierarchy/revision-workflow session
  (closes the git-backlog finding above).
- `2bf9fd06` — sanity check, architecture correction, alignment register, Obsidian/SQLite guides,
  manifest rebuild, SQLite-script relocation.

Both pushed; working tree clean as of session close.

## Next session

Start at `docs/governance-alignment-register.md`. The researcher's stated next step is to review
the plans and the register and begin the actual alignment work — expect that to mean working
through register item #1 (the `CLAUDE.md` banner) toward approval first, then scoping a detailed
plan for step 2 (file-store consolidation) before any of it executes.
