# Prose store — IBA incorporation build plan (v3)

**Escalation #784.** Replaces v2 (same file, superseded — item 1 below is now resolved and several
things happened live since v2 that need recording). v1 and v2 are left on disk for history.

**How to read this document:** every place I decided to do something, or decided *not* to do
something, is followed by a line starting **Rule:** quoting the actual governance text I'm
following. Where no such rule exists, I say so.

---

## Status update since v2 — read this first

- **Item 1 (`prose.extractor_version`) is CLOSED — dropped from code, not added to config.**
  Working through it surfaced that the value was superficial tooling metadata (the export
  script's own version label, nothing to do with prose content or `prose_section.version`'s real
  per-section versioning) — it controlled nothing, gated nothing. Researcher, 2026-08-22: *"the
  config is not necessary, the code need to change to drop it from the code."* Done —
  `EXTRACTOR_VERSION`/`extractor_version()` removed entirely from `iba/app/lib/prosestore.py`, and
  from the JSON/MD/DOCX extract output. Tested live: all three formats still generate correctly.
  Items 2–4 (`chapter_names`, `book_stage_map`, `search_default_limit`) are **unaffected** — still
  queued exactly as in v2, still genuinely config-driven values, not superficial labels.
- **Escalation #790 (the `raise_()` bug) is fixed and verified live**, twice — once against a
  throwaway test row, once for real (the correction to #787, see below). `comment`/`originator`/
  `from_id`/`next_action` are now all populated correctly on every newly-raised dispatcher
  escalation.
- **Escalation #787 was approved and applied — but I made a mistake applying it.** When I re-ran
  the approved proposal, I dropped the `key` field from the payload, so it wrote a `cfg_setting`
  row with `key=NULL` instead of `key='prose.extractor_version'`. Caught, and — now that item 1 is
  dropped entirely — the fix isn't "add the missing key," it's "delete the orphan row." That's
  **escalation #796**, awaiting your decision, not yet applied.
- **A second bug surfaced answering the correction (escalation #793/#794):** dispatcher-tied
  escalations collapse `approve`/`reject`/`revise` to the identical `completed` status — your
  `revise` decision on #794 landed as `completed`, same as an approve would have. Raised as its own
  item, **escalation #795**, with your stated design intent recorded, no fix proposed by me. Not
  blocking anything below.

---

## Part A — what's already built (code), and what's queued to configure it

This is the narrow fix: the 4 named scripts were switched off (`cfg_utility.inactive=1`) and 2 of
them had hardcoded values that should have been config. This part turns them back on and fixes
that. It does **not** touch the deeper problem in Part B.

### A1. Code already written and tested — no config was needed to build or test this

Four files carry the actual logic now. I tested every one directly against your live
`bible_research.db` — nothing below is hypothetical.

**`iba/app/lib/prosestore.py`** — the real implementation of all four operations (extract, search,
export a chapter, import an edited chapter). Connects to `bible_research.db` through
`cfg.database_path('bible_research')` instead of a typed-out path (a setting that already existed
but had no real user until now). Reads `chapter_names`/`book_stage_map`/`search_default_limit`
from `cfg_setting` instead of having them typed into the file.

**`iba/app/handlers/prose.py`** — four short functions that let the above be run through IBA's own
dispatcher, the same mechanism every other registered operation in the app uses.

**`iba/app/ps/Prose.ps1`** — the PowerShell command a person types to run one of the four
operations, e.g. `.\Prose.ps1 -Step Search -Query grace`.

**The four original `scripts/*.py` files** — kept, but rewritten to call into `prosestore.py`
instead of having their own copy of the logic. Command-line usage is unchanged.

**Test results** (against the live DB, read-only unless noted):

| I ran | What happened |
|---|---|
| `python scripts/build_programme_prose_extract.py --book Programme --also-markdown --also-docx --include-body` | Wrote JSON + Markdown + Word, 51 section types, 51 populated sections — correct, and re-verified today after removing extractor_version |
| `python scripts/search_prose.py grace --limit 3` | Found 146 matches, wrote a report showing 3 — correct |
| `python scripts/export_prose_chapter_edit.py --book Programme --chapter 1` | Exported 6 sections to an editable Markdown file — correct |
| `python scripts/import_prose_chapter_edit.py <the file just exported, unedited>` | Validated all 6 sections and generated a patch file. **Checked `database/bible_research.db`'s last-modified time before and after — unchanged.** This script only writes a patch file, never the database itself, and it didn't. |

Also ran the same four operations directly through `iba.app.handlers.prose` (the code path the
PowerShell command will use once registered) — same correct results.

### A2. Config changes queued — 3 remain, down from 4

Each block: **the exact config**, **what it means**, **which code reads it**, **which governance
rule it satisfies**.

`configmaint.propose` only allows one pending change at a time. Two are currently pending your
decision (#795 and #796, both explained above); once those clear, these three are next.

> **Rule (why config changes go through this gate at all):** *"IBA config changes: never
> silent/automatic writes — propose→validate→escalate→apply"*
> (`feedback_iba_config_changes_require_researcher_approval_never_silent`).

#### 1. `prose.chapter_names`

- **Adds:** a new row in `cfg_setting`, key `prose.chapter_names`, value:
  ```json
  {"0":"Preamble","1":"Programme purpose","2":"Research methodology","3":"Research approach","4":"Data architecture","5":"Data integrity & governance","6":"Instruction corpus"}
  ```
- **In plain English:** the extract needs to turn a chapter number like `4` into a readable name
  like "Data architecture" when it writes the Markdown/Word version. This is that lookup table.
- **Code that reads it:** `prosestore.py`, function `chapter_names(cfg)`.
- **Rule this fixes:** the script was flagged `NON-COMPLIANT (escalation #648)` in `cfg_utility`
  for hardcoding this.

#### 2. `prose.book_stage_map`

- **Adds:** a new row in `cfg_setting`, key `prose.book_stage_map`, value:
  ```json
  {"Programme":["programme"],"Detail design":["session_a","session_b","session_b_phase9","session_c","session_d"],"Findings":["synthesis","verse-analysis"],"Essays":["essay"]}
  ```
- **In plain English:** when you run the extract with `--book Programme`, the tool needs to know
  "Programme" is a real, allowed choice. This is the list of allowed book names and which internal
  stage each covers.
- **Code that reads it:** `prosestore.py`, function `book_stage_map(cfg)`.
- **Rule this fixes:** same escalation #648 flag.

#### 3. `prose.search_default_limit`

- **Adds:** a new row in `cfg_setting`, key `prose.search_default_limit`, value `100`.
- **In plain English:** if you search prose and don't say how many results you want, this is the
  cap.
- **Code that reads it:** `prosestore.py`, function `search_default_limit(cfg)`.
- **Rule this fixes:** `search_prose.py`'s own escalation #648 flag.

### A3. Turn the four scripts back on (4 more changes)

Each: set `cfg_utility.inactive` from `1` to `0`, and replace the `purpose` text with a short note
that it's fixed and where its logic now lives.

| Script | New `purpose` text |
|---|---|
| `scripts/build_programme_prose_extract.py` | "Programme-stage prose extract (JSON/MD/DOCX). Reactivated 2026-08-21 (escalation #784): hardcoded values moved to cfg_setting, resolving escalation #648 (except EXTRACTOR_VERSION, dropped from the code entirely — superficial, controlled nothing). Logic now in iba/app/lib/prosestore.py, also runnable via Prose.ps1 -Step Extract." |
| `scripts/search_prose.py` | "Search prose_section by keyword. Reactivated 2026-08-21 (escalation #784): hardcoded value moved to cfg_setting, resolving escalation #648. Logic now in iba/app/lib/prosestore.py, also runnable via Prose.ps1 -Step Search." |
| `scripts/export_prose_chapter_edit.py` | "Export a prose chapter for editing. Reactivated 2026-08-21 (escalation #784) — no hardcoded values were flagged here. Logic now in iba/app/lib/prosestore.py, also runnable via Prose.ps1 -Step ExportChapter." |
| `scripts/import_prose_chapter_edit.py` | "Turn an edited chapter into a patch. Reactivated 2026-08-21 (escalation #784) — no hardcoded values were flagged here. Logic now in iba/app/lib/prosestore.py, also runnable via Prose.ps1 -Step ImportChapter." |

- **Rule this satisfies:** the literal instruction — *"activate the 4 scripts."*

### A4. Registering the 4 operations with IBA's own dispatcher — held, see Part B

Still holding back the `cfg_work_package`/`cfg_step` rows for the same reason as v2: you told me
prose is a full module, not a utility, and Part B (unchanged from v2, below) is what that means
once checked against the real config. Proposing those rows now, before Part B is decided, would
lock in a shape that might be wrong.

---

## Part B — "prose is not a utility, it's a full module" (unchanged from v2)

> **Rule I'm applying in this whole section:** *"no operational or process rule may exist only in
> GOVERNANCE.md, BUILD.md, USER-GUIDE.md, or memory without a referenced cfg_* row recording it...
> Any deviation discovered requires escalation."* (`governance.rules_must_be_config_driven`) and
> *"each operating module must have a config table (or tables) in the cfg_* series to control all
> aspects of the module's operation"* (`governance.module.config`).

**What a real module looks like here** (checked against `candidate`/`cluster`/`lexicon`/`passage`):
`kind='operations'` steps (not `'utility'`), a `cfg_write_grant` row per writing step, and its own
status tracked in `cfg_status_flow`.

**What I built for prose is only the reporting layer.** The 4 operations registered
(`extract`/`search`/`export_chapter`/`import_chapter`) are correctly `kind='utility'` — none writes
to `prose_section`. The real write happens through `scripts/apply_session_patch.py`, which has
**zero IBA registration of any kind** — not in `cfg_step`, `cfg_work_package`, or
`cfg_write_grant`. That's the part of prose that's genuinely a module, and it's entirely outside
IBA today.

**Five rules from `docs/prose-store-architecture.md`, checked one by one against the config —
none found:**

| The architecture document says | Found in config? |
|---|---|
| `status` CHECK-constrained to draft/in_review/approved/archived | **No** — `cfg_status_flow` has no `entity='prose_section'` row at all |
| `author` CHECK-constrained to claude_ai/claude_code/researcher | **No** — no author-related `cfg_enum` exists |
| `session_a_replace` in-place-update exception, gated on `author='claude_code'` | **No** — not in `cfg_method_rule` (scoped to the debate pipeline only) or `cfg_behaviour_rule` |
| The two-patch pattern (`CATALOGUE_POPULATION` then `PROSE`) | **No** — no `patch_type` enum exists anywhere in `cfg_*`; the real list lives only in `wa_patch_type_registry`, in `bible_research.db` |
| Supersede-only discipline (a revision creates a new row, nothing is edited/lost) | **No** — stated once in prose, enforced only by the applicator's own code |

**Not fixing this now.** Building a real status flow, author enum, rule table, and patch-type enum
for prose's write side is a second, separate, larger piece of work.

> **Rule:** *"build in SIMPLE STEPS; machinery-heavy plans get rejected as overengineering"*
> (`feedback_simple_steps_not_engineered_designs`).

---

## What I need from you

1. **#795** and **#796** — both pending, both block every proposal below until answered.
2. **A2 items 1–3** and **A3 items** (7 changes total) — say whether to proceed as written.
3. **A4** (registering the 4 operations with the dispatcher) — say whether to raise as its own
   escalation now, or decide together with Part B.
4. Part B itself — is bringing prose's write side under IBA something to scope/schedule now, or
   later?
