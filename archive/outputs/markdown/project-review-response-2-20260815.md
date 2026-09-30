# Response to Review Notes (2) — 2026-08-15

Follows [project-review-response-20260815.md](project-review-response-20260815.md). Covers: the
Claude Code vs Claude API question, actions taken (manifest refresh, SQLite script filing), the
governance-alignment register + first proposed item, and where the rest of your instructions
stand.

## 1. Claude Code chat vs the Claude API — how they actually differ here

Your model is right in shape; here's the precise mapping and one gap to know about.

**What "Claude Code chat" (this conversation) is.** A harness around the same underlying model
(Sonnet 5 right now) with tools bolted on — file read/write, bash, DB queries, git. There's no
separate "AI agent" it silently hands off to for a normal reply: when you ask something here, I
do the work myself, in this conversation, with full read/write access to the repo and both
databases. The one place a real hand-off happens is if I explicitly spawn a background subagent
(the `Agent` tool) for a genuinely independent, parallel chunk of work — that *is* a separate
Claude Code process, but it's still Claude Code, not a different product, and I only do it when
it's actually warranted, not as routine behaviour.

**What "the API" is.** A raw HTTP endpoint (`POST /v1/messages`) with no tools, no filesystem, no
memory of its own — just "send a prompt, get a completion." Your own code (in this case, IBA app
Python/PowerShell) calls it directly. This is what "configure it in IBA, then run it with an
instruction" should compile down to for anything that must behave identically every time:

- The **rules, input shape, and output shape live in `cfg_*` config** (as you already do for
  everything else in IBA) — e.g. a `cfg_method_rule` row holding the prompt template, a schema
  for the expected response.
- The **call itself is `output_config: {format: {...}}`** (structured outputs) so the response is
  *guaranteed* to match a JSON schema you define — no free-text parsing, no drift between runs.
  This is the direct fix for "consistency and quality could not be achieved" from the old method:
  the old approach asked a free-form question and hoped the shape held; structured outputs make
  the shape a contract the API enforces.
- It's registered as a normal `cfg_step`/`cfg_utility`, same as any other IBA script — the fact
  that one step happens to call an LLM isn't architecturally different from a step that runs a
  SQL query.

**So the working rule is:**

| Work package characteristic | Route |
|---|---|
| Same rules, same input shape, same output shape, every run — no human judgment needed per-run | **Claude API call from IBA app code**, config-driven, structured-outputs schema |
| Genuine enquiry, investigation, judgment call, anything needing back-and-forth or my read of the actual DB/files | **Claude Code chat** (here) — already has full tool access, no reason to leave |
| Repeatable *and* needs multi-step autonomous tool use (not just one classification call) but should run unattended/on a schedule | **Managed Agents** (a third surface, hosted sessions Anthropic runs) — not needed yet for anything you've described, but worth knowing it exists once "restart findings/analysis" needs an unattended multi-step pipeline rather than single-call classification |

**"There should be no reason to use the Claude desktop" — agreed, with the actual reason stated.**
Claude AI desktop's whole value is a chat UI with no filesystem/DB access — it's for people
without a coding environment. Claude Code already does everything Claude AI desktop does
(read, write, reason, converse) *plus* direct DB/file access, in the same window you're already
using. There's no capability Claude desktop has that this doesn't. The one asterisk: a direct API
call from IBA app code needs its own credential (`ANTHROPIC_API_KEY` or `ant auth login`),
separate from your Claude Code subscription — a new, small infrastructure dependency once IBA
starts calling the API itself, worth knowing about now rather than discovering it mid-build.

## 2. Actions taken

- **File manifest rebuilt** (`python scripts/build_file_manifest.py`) — was stale since 2026-07-23
  (three weeks). Now current: 18,640 files tracked, 10,086 active / 8,554 archived.
- **SQLite-extension scratch queries relocated and named**, per your instruction. The three files
  that had landed in `database/scripts/` (one literally `Untitled-3.sqlite3-query`) are now in
  `scripts/`, prefixed `SQLite_`, with the DB-relative path in each file's header comment
  corrected for their new location:
  - `scripts/SQLite_prose_section_type_list.sqlite3-query`
  - `scripts/SQLite_prose_section_type_with_body.sqlite3-query`
  - `scripts/SQLite_programme_prose_body_export.sqlite3-query`

  One thing worth your eye, not something I resolved myself: `SQLite_prose_section_type_list` and
  the first query in `SQLite_prose_section_type_with_body` are near-duplicates (same
  `SELECT * FROM prose_section_type ORDER BY source_stage, sort_order[, chapter_no]`). I kept
  both rather than silently merging them — happy to delete the narrower one if you agree it's
  redundant.
  - `database/scripts/` (the old location) is now empty — the OS won't let me remove the folder
    itself (still held open, likely by the SQLite extension), but that's cosmetic; git never
    tracked empty directories so it won't appear in any diff.
  - `.gitignore`'s `database/scripts/*.sqlite3-query` rule is removed — no longer needed now that
    the convention is "these live in `scripts/`, tracked and committed like any other script,"
    per your instruction to save exploration/extraction scripts there going forward.

## 3. Manifest search — what exists vs. what you're asking for

Read `scripts/build_file_manifest.py` before promising anything: the manifest indexes **filename
metadata** — registry number, date, cluster code, word, version, VCB batch — extracted by pattern
matching on the path/filename, plus a `category`/`type` classification. `--search` matches against
that metadata, not file *contents*. So `--search "grace"` works today only because "grace" happens
to appear in filenames; it does not scan inside files.

What you're describing next — "find all files that reference a specific keyword (likely a
characteristic) or Strong's reference" — is **content search**, a different mechanism entirely.
That's not a quick addition to today's manifest; it needs its own design (a content index, kept
current as files change — the DB's own `prose_section_fts` FTS5 table is the closest existing
precedent in this project). I'm not building that now — it belongs in the file-store-consolidation
step you asked to move earlier (§4 below), where it can be scoped properly rather than bolted on.
For the immediate need — you reviewing/consolidating the analytic-phase files right now — a
plain `grep`/`rg` over `Sessions/`, `Sessions-v2/`, `Workflow/` will outperform anything the
manifest can do today; I can run targeted searches for you in this chat as you go, rather than
waiting on a proper index.

## 4. Governance-alignment register — Step 1, first item for your approval

You said proceed on step 1, but as a controlled process: keep a register, surface conflicts, ask
before each change. Register started:
[`docs/governance-alignment-register.md`](../../docs/governance-alignment-register.md).

**First item logged and proposed** (not yet applied): `CLAUDE.md` §4/§5/§7/§8 still present the
old engine/STEP pipeline (`python -m engine.engine`, `word_study_extract.py`,
`build_complete_extract.py`) as the live, authoritative way to do base-layer work — word
initiation through verse-lexical analysis. Per your correction, that entire layer is now owned by
`iba.db`/`iba/app/`, and those sections are stale, not current. Left as-is, anyone (me included)
reading CLAUDE.md cold gets routed to the wrong system for that work.

**Proposed fix** (matches the existing pattern already used at the top of the file for prior
resets — a superseded-by banner, not a rewrite): add a banner over §4/§5/§7/§8 stating the base
layer moved to IBA as of this session, pointing to `iba/app/USER-GUIDE.md`, and marking those
sections **provenance-only** (accurate history of the old pipeline, not instructions to follow).
I have not made this edit — it's the first entry in the register precisely so you can approve,
amend, or reject it before anything changes in the steering document.

## 5. Filing and archiving rules

Logged as its own register item, not started — you flagged this should be config-defined (an
IBA `cfg_*` concern), which fits your alignment-plan ordering: it's really part of "bring
governance together" (step 1) applied to filing specifically, and it overlaps with the file-store
consolidation (now step 2). I'd fold the filing/archiving-rules review into step 2's plan rather
than run it as a separate fifth thread — flagged in the register for you to confirm or redirect.

## 6. Where things stand on the rest

- **DB split (two-database plan): agreed in principle.** `iba.db` as process-control + base
  layer, `bible_research.db` as prose + analytic findings, is consistent with everything the
  sanity check found — IBA's governance is being followed in practice; the main repo's isn't yet
  aligned to say so. The "remove the base layer from `bible_research.db` once the split is
  proven" step stays a checkpoint after §1/§2 below, per your own sequencing, not something to
  act on now.
- **Revised alignment order, as you set it:**
  1. Align governance/docs (in progress — register above; first item awaiting your approval)
  2. Consolidate the file store (moved up; folds in the manifest content-search work from §3 and
     the filing/archiving-rules review from §5)
  3. Merge windows-debate work with prose → one consolidated analytics methodology, scoped as you
     described: the base-layer (STEP→lexical) portion is **documentation only** — record that IBA
     now owns and controls it, don't re-derive the how-to; the analytics/synthesis portion (old
     Session B/C/D) is where the real critical-review-and-redesign work happens
  4. DB-split formalisation checkpoint
  5. Merge findings into prose — explicitly not started; you asked for a fully detailed plan
     before any prose changes in the Findings book, given how much thought this needs
- **Every step still needs its own detailed plan submitted for your review and approval before
  any update lands** — nothing above is authorisation to execute; it's the register recording
  where each thread stands.

Two written guides you also asked for are filed separately (design-heavy content, not review
material):

- [`Workflow/Obsidian/obsidian-usage-guide-v1-20260815.md`](../../Workflow/Obsidian/obsidian-usage-guide-v1-20260815.md)
- [`Workflow/SQLite/sqlite-extension-best-practice-v1-20260815.md`](../../Workflow/SQLite/sqlite-extension-best-practice-v1-20260815.md)
