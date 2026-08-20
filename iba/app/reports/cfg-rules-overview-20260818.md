# The IBA config, told as a story — 2026-08-18 (rebuilt, same day, later — cycle 4)

**What this is.** A narrative walk through everything currently live in `iba.db`'s `cfg_*` tables
— not a table-by-table dump (that's `CONFIG-REPORT.md`'s job), a *story*: how the project comes
alive, how its different surfaces behave, how the whole thing is governed, what it's actually
built on, and how its working parts move. Every claim below is a live query against the DB run
today, not a summary of documentation — where a rule is still thin or a gap is open, that's said
plainly rather than smoothed over.

> **Rebuild note (escalation `#715` cycle 3):** this version was checked both directions against
> the live tables, not written from memory of the first draft — from the story out (every number
> and named table below re-queried) and from the tables in (all 31 `cfg_*` tables enumerated and
> checked against what the story actually says). What that audit found: the original draft's
> snapshot numbers had already drifted (tables 29→31, settings 153→156 even before this cycle's own
> additions) — both corrected below. Two real subsystems the story never named are now covered:
> `cfg_connection`/`cfg_api` (§1, the STEP integration the pre-flight check actually reads) and
> `cfg_content_index_exclude`/`cfg_content_index_size_override` (§5). One real gap is flagged, not
> yet folded into the narrative voice: `cfg_candidate_rule` (289 rows — accept/reject overrides for
> candidate Strong's numbers during onboarding) is a sibling of `cfg_method_rule`'s "37 rules across
> five steps" in kind (analytical-content-shaping config) but a different shape (override table, not
> prose rule) and deserves its own telling, not a retrofit into §5's existing paragraph — left as a
> named follow-on rather than force-fit here. The remaining unmentioned tables
> (`cfg_change_detail`, `cfg_change_log`, `cfg_report`, `cfg_report_csv_table`,
> `cfg_report_section`, `cfg_index`, `cfg_unique`, `cfg_book_order`) were checked individually and
> are correctly omitted by the story's own stated scope — implementation plumbing, not governance
> shape; that is exactly what `CONFIG-REPORT.md` is for.

**Snapshot at time of writing:** 31 `cfg_*` tables, 161 settings, 27 work packages, 55 dispatcher
steps, 37 analytical method rules, 17 quality checks, **42** operational-behaviour rules across
**6** classes (was 15 rules / 5 classes as of the first draft this morning — cycle 3 populated
`chat` from empty and added real content to `terminal`/`sqlite`/`documentation`/`llm_output`;
cycle 4 added a 6th class, `development`, after a structural read-through of cycles 1–3 found no
literal duplication but did find two rules that would have duplicated existing `governance.*`
settings — not added, once found), 2 databases, 7 programme-prose chapters. All of it reachable
from one entry point: `governance.rules_must_be_config_driven` — *"no operational or process rule
may exist only in a document or memory without a referenced `cfg_*` row recording it as the
evidence that the configuration control is in operation."* Everything that follows is that
principle, applied.

---

## 1. How the project starts up

Before anything else happens — before a word is onboarded, a passage is debated, a report is
run — the app boots through one idempotent sequence, `iba/app/init.py`, invoked as
`iba\app\ps\Start-Iba.ps1`:

1. **Validate the config seed** (`cfgcheck`) — refuse to start at all if the seed itself is
   incoherent. Nothing downstream is trusted until this passes.
2. **Load the config into the DB**, if it isn't already there (`--reload` to reseed deliberately).
3. **Build the data tables from the config**, if they're missing (`--reset` to rebuild, which
   drops data — a deliberately loud, opt-in flag).
4. **Pre-flight STEP** — not just "is port 8989 listening," but *up and answering with the tagged
   module* (a known-answer probe: `H0430 → H0430G gloss 'God'`). A live port with the wrong module
   loaded would pass a weaker check and silently corrupt every lexical read downstream. The
   connection itself is config, not a literal in a client class: `cfg_connection` holds the base
   URL, module version, and timeout; `cfg_api` catalogues the three actual REST calls the app
   issues (route template, input, response shape) — the IBA-side equivalent of
   `scripts/analytics/step_client.py`'s method list on the main-project side.
5. **Orient on `BUILD.md` + `GOVERNANCE.md`** — what's built, and how config governs it. The
   startup sequence itself points at the record of its own history before doing anything new.
6. **Print every `governance.*` setting explicitly.** This is the one deliberate exception to
   "config is read, not printed" — a `governance.*` row has no runtime value to *apply*, so being
   printed at every session start **is** its usage (the mechanism `find_orphan_configs` checks
   against, so a governance rule can never silently rot unread).
7. **Report status.**

The database itself carries only two facts as its own identity: `cfg_meta.database = 'iba'` and
`cfg_meta.config_version`. Everything else — every table, every setting, every rule — is built up
from that one seed, in that one order, every time. There is no other path into a working session.

---

## 2. How the different interfaces behave

Six behaviour classes, one shared mechanism (`cfg_behaviour_class` + `cfg_behaviour_rule`,
`governance.operational_behaviour_control` as the anchor). Four cycles in now (escalation `#715`):
cycle 1 seeded "the obvious ones" from the retired `wa_rule_registry`, cycle 2 swept three
never-`CLAUDE.md`-referenced `Workflow/*` guides, cycle 3 did the sweeps the researcher named
directly — `docs/interaction-preferences.md`, `CLAUDE.md` §9, confirmed `feedback_*` memory, and
`Workflow/Instructions/` for prior attempts — and populated `chat` from empty, cycle 4 (escalation
`#732`, after a structural read-through under `#733`) added a 6th class, `development`.
`authoritative_doc` is set on 5 of 6 classes (all but `development`, which has no single source —
its content is memory + this sweep's own findings), though for `chat`/`terminal` it still names
the main-project document the content came *from* (`docs/interaction-preferences.md`), not a
cfg-native replacement — real duplication, quantified not yet resolved (see §3).

**`chat`** — 9 rules, no longer empty. The AskUserQuestion tool is never used (config-blocked after
three prior memory-only bans failed); non-trivial work is summarised and confirmed before it
starts, but an already-approved plan runs to completion without re-confirming every step; all
substantive output goes to a file, chat carries only a pointer; work proceeds from verified facts,
never a guess; the cheaper technical path is flagged before acting; a genuine open item raised in
chat becomes an escalation the same turn (a pointer to `cfg_escalation.chat_routing`'s own fuller
rule, not a restatement of it); a review closes with a verified fix, not just a finding; and
reporting shows the actual evidence rather than a smoothed-over summary.

**`sqlite`** — 6 rules. Never act on assumed or remembered database state; verify live. Open
connections read-only by default. Never write to either database through an ad-hoc tool (a patch
for `bible_research.db`, `Config-Maintenance.ps1 -Step Propose` or a registered utility for
`iba.db` — inspection and the fix are different paths, deliberately). Don't assume which database a
table lives in — the two share names (`cluster`, `passage`, `verse`, `word_registry`) for
genuinely different tables. Keep scratch query files named, findable, and committed if they're
worth re-running. And — folded in this cycle under a `governance.behaviour_boundary.*` decision
rather than a new class — study work is captured only through a replayable mechanism (a patch, a
registered utility, an engine run); the 2026-06-03 DB-loss incident traces directly to an
interactive mutation that wasn't.

**`llm_output`** — 9 rules, the one with the clearest present-tense stakes (this is where real
money gets spent). A claim generated by an LLM/API call is inferential until it's grounded in
verifiable data — never silently upgraded to confirmed, and a superlative ("most", "clearest") is
the same failure made concrete: never written unless every candidate was actually checked. New
analytical work derives from the authoritative instruction, never from a prior run's unreviewed
output used as an implicit template. No hardcoded model IDs, rates, paths, or caps in a handler —
every one is a setting. No live call before a pre-call cost estimate *and* a hard cap check
(refuse over the cap, escalate under it). Every real call's usage gets logged. Sonnet 5 is the
default; Opus needs a reason. The API key is never written anywhere, by anyone, for any reason. No
second dependency (the `anthropic` SDK) without raising that as its own decision.

**`terminal`** — 6 rules, up from 1. A step isn't done until its output is confirmed to exist and
match what it was supposed to produce — extended this cycle: a fix isn't done until tested against
both a synthetic bad case and real data, and re-verified per site when applied more than once. A
read-only command needs no upfront permission; one that writes stays inside an approved task. A
reported console error is the thing to diagnose, never quietly routed around. A multi-line
here-string is PowerShell syntax, never Bash heredoc syntax, in this environment. And — the other
`governance.behaviour_boundary.*` decision — git commit and push are one unit, never left split,
committed incrementally through the session rather than gathered at the end.

**`documentation`** — 7 rules, up from 2. Pointer, not copy — one authoritative source per content
type, a rule never lives in both a document and a `cfg_*` row at once. An Obsidian-edited copy of a
DB-generated file is never itself authoritative. New this cycle: guidance given mid-session gets
baked into the authoritative record the same session, not left in memory alone; a "complete" record
never hedges with a "see raw data" pointer in place of a resolved answer; an ongoing
investigation is one living document updated in place, not a new competing file each pass; a claim
about project history is grounded in the written record and cited, not recollected; and — the
rule this cycle's own retirement work is itself an instance of — a consolidation document is only
as good as its live enforcement, and one with no live reader is retired (banner + pointer,
provenance kept), however recently written. Applied live, same session: two orphaned 2026-06-14
consolidation docs (`wa-operational-governance-v1_0`, `docs/project-orientation-core-memory-map.md`)
retired under exactly this rule.

**`development`** — 5 rules, the newest class (added cycle 4, escalation `#732`, after a structural
read-through of the other five found the base coherent). Governs how work on this project *itself*
gets done, not a specific interaction channel: fix the cause, not the instance — a defect that's an
instance of a class gets fixed at the shared mechanism, never remediated case-by-case; work is
built in simple, direct steps, not machinery-heavy speculative designs; every open item discovered
anywhere — a review finding, a validation run, a sweep — routes through the escalation table, the
general case of `chat.chat-items-become-escalations`'s conversation-timing instance; a module a
person operates by hand gets a dedicated PS entry point, not just raw Python/SQL (found violated by
this very system: 3 build cycles before `Behaviour.ps1` existed); and a tool/module/behaviour
change isn't complete until `USER-GUIDE.md` reflects it, in the same unit of work (found violated
the same way — zero guide coverage across those same 3 cycles, closed in the cycle that named the
rule). Two candidate rules from the same request were checked and **not** added, because they
already existed: temp-file discipline is `governance.scripts_and_routines`; script-folder
destination is `governance.scripts_ps_dir`/`governance.scripts_python_dir` — exactly the
duplication risk the researcher flagged before this class was built, avoided by checking first.

---

## 3. How the environment is governed

Strip away the specific rules and one loop repeats everywhere: **propose → validate → escalate →
apply.** `configmaint.propose` is the one sanctioned path for changing a `cfg_*` row by hand —
DB-direct, single-row, approval-gated; the first call always pauses and escalates, the researcher's
answer (`Approve`/`Reject`/`Revise`/`Hold`/`Noted`) resumes it. `configmaint.validate` is the
read-only coherence check, safe to run any time, that everything in this document was pulled
through today. `configmaint.report` regenerates `CONFIG-REPORT.md` from the live tables. Three
independent operations sharing one registration — not a fixed pipeline, three doors into the same
room.

**The escalation system has its own seven governing rules** (`cfg_escalation`), because
"how a question gets asked" turned out to need as much discipline as the answers themselves:
`source_classification` (who raised it — Claude or researcher, by convention, lowercase);
`duplicate_suppression`; `module_blocking` (an unresolved escalation blocks its own step from
re-dispatching — the mechanism that made this exact session's `#720`/`#719` chain visible rather
than silently retried); `resolution_precedence`; `chat_routing` (a genuine open item raised in
conversation gets an escalation the same turn, not after being asked — extended, after being
caught live once, to cover judgement calls reported only in chat prose too); `document_reference_
grouping` (a multi-part package shares one `related_activity` and one `reference_doc`, mechanically
enforced — not just a convention someone might forget); `full_path_file_references` (a file named
in an escalation is a full repo-relative path, never a bare filename that might resolve five
different ways in a large repo).

**Underneath both loops, a small set of registration disciplines makes the whole thing checkable
at all**, not just documented: every table in either database goes in `cfg_table`
(`governance.tables`), every column in `cfg_column` (`governance.table_columns`) with a real `use`
text, every script or routine in `cfg_utility` in the same unit of work it's created
(`governance.new_utility_registration_timing`), every writer of every table gets an explicit
`cfg_write_grant` row or nothing can legitimately maintain it. `governance.build_md_on_code_change`
and `governance.governance_md_on_rule_change` close the loop the other direction — a code change
updates `BUILD.md`, a rule change updates `GOVERNANCE.md`, in the same unit of work, so the
documents never drift ahead of or behind what's actually true. `governance.session_log_triggers_
commit` is the one standing exception to "never commit unless asked."

None of this is presented as finished. `governance.past_precedent_investigation_signals_missing_
config` names its own failure mode directly: needing to read history to reconstruct a missing
step is itself the signal that a piece of config is missing, not a puzzle to solve from precedent.
And the loop *has* failed before — `wa_rule_registry`, the direct predecessor of everything in
this document, ran 59 rules for four months with no `enforced_by` mechanism, drifted across every
method pivot, and was retired 2026-08-17. The lesson carried forward isn't "rules work now" — it's
that a rule without a live check tends to rot regardless of how it's stored. The same lesson
recurred one level up during this document's own cycle-3 rebuild: two documents written 2026-06-14
specifically to *consolidate* scattered operational rules (`wa-operational-governance-v1_0`,
`docs/project-orientation-core-memory-map.md`) had themselves silently drifted out of every live
read path — neither the current `start-project` skill nor this app's own governance ever pointed at
them — and sat unretired for two months until this sweep found and closed them. A rules table and
a consolidation document fail the same way: written with good intent, never wired to anything that
actually reads it, and nothing notices until someone goes looking.

---

## 4. What the project is actually built on

**Two databases, one split, now structurally named, not just described.** `bible_research.db`
(`database/bible_research.db`) holds prose and analytic findings; `iba.db`
(`iba/app/db/iba.db`) holds process control and the entire base data layer, word initiation through
verse-lexical. That split used to live only as a sentence (`governance.project_databases`); as of
today it's also a queryable `cfg_enum project_database` (two members) plus two structured path
settings — the difference between a human reading a paragraph and code that can actually iterate
"every known project database" without parsing prose. `governance.scope_iba_app`/`scope_iba_db`/
`scope_research_db`/`scope_project` say the same split again from the governance side: IBA is the
project's process-control mechanism for *everything*, not a sub-section of it — the stated
end-state (not yet reality) is one governed system, not two.

**Three programme stages** (`governance.programme_stages`): Base_data (STEP through lexical),
Analysis (deriving understanding of the inner being), Publishing (essays and output) — the modern
names for what used to be Session A/B/C/D, methodology changed materially across all three but the
three-stage shape held.

**And, as of today, a canonical answer to "what is this project actually about"** that isn't
scattered prose anymore either. `governance.prose_canonical_authority` names the programme prose
(`Workflow/Programme/programme_prose/`) as the authority, and two new tables make it addressable
rather than just asserted: `cfg_prose_chapter` — seven chapters, zero through six, Preamble through
Instruction corpus — four of them (0–3) reviewed and final, three (4–6) explicitly flagged
`not_yet_aligned` and already escalated for a real pass, not silently carried forward as if they
were current. `cfg_prose_concept` is the more interesting piece: not a copy of the prose, a
*pointer* into it — `verse_primacy` and `inner_being_definition` both resolve to chapter 1 today,
direct successors of two of the old `wa_rule_registry` rules (`GR-PROG-001`, `GR-PROG-002`) that
used to restate a definition as rule text. Now the rule *is* the pointer; the prose is the only
place the actual definition lives. That's the `documentation` class's own
`single-authority-pointer-not-copy` rule, applied to the project's own founding statements, not
just to code.

**One governing constraint sits above all of it:** `governance.project_change_rule` — any change
of operations, methodology, or approach channels through the IBA app; anything defined in the past
that isn't in the app yet is scheduled to migrate in. `governance.primary_responsibility` names who
that migration work belongs to: Claude, for both the coding and the ongoing integrity of it.

---

## 5. How the different elements actually behave

Two different kinds of "step" live side by side in this system, and the split matters:
**operations** (34 live steps — the study's substantive analytic content: `hib.set`,
`operation.set`, `phenomenon.set`, `closing.set`, `passage.build`, and the report/registry/word
work around them) and **utility** (21 live steps — the app running itself: `configmaint.*`,
`content_index.*`, `manifest.*`, backups, escalation plumbing). `content_index.*`'s own scope is
config, not a hardcoded skip-list: `cfg_content_index_exclude` names path patterns the rebuild
skips outright (today: `Workflow/Programme/programme_prose/`, excluded 2026-08-17 because generated
analysis prose saturated with biblical vocabulary was drowning every search — one file alone
produced ~597,000 hits), `cfg_content_index_size_override` is the manual-release valve for a
specific oversized file that should be indexed anyway (empty by default — nothing released until
named). 27 registered work packages carry
those 55 steps between them — most (`configuration-maintenance`, `reports`, `table-export`, the
content-index and file-manifest trio) run standalone, `runs_over='none'`; the ones that operate
over real study content (`new-word`, `word-audit`, `verse-lexical`, `book-narrative`,
`build-passages`) are chained — their steps run in sequence automatically once triggered, rather
than needing to be invoked one at a time.

**The analytical steps carry their own rule layer, separate from — and older than — the
operational-behaviour work in §2.** `cfg_method_rule`: 37 rules across five steps (`hib.set` ×7,
`phenomenon.set` ×9, `operation.set` ×9, `closing.set` ×6, `passage.build` ×6) — the actual
substance of *how to read a passage and register what's found in it*: which candidates count as a
Human Inner Being, how a non-human being can never itself be one, how a collective stays one row
not many, and on through every step of the read. `cfg_quality_check` sits directly alongside it —
17 checks across the same five steps, each one a question ("Is `hib.kind` one of the six live enum
values, not free text? Does this candidate actually refer to a human being, not a place or object
personified only grammatically?") with a declared `test_kind` (existence / reasonableness /
non-existence) — some mechanically checkable, some genuinely requiring judgement, and the
`test_kind` says plainly which is which rather than pretending everything is machine-verifiable.

**Failure has a declared shape, not an ad-hoc one.** `cfg_on_fail` routes 67 (step, condition)
pairs to one of four outcomes (`pause-continue`, `report-stop`, `report-continue`, `self-heal`) —
whether an error means "stop everything," "keep going and log it," "ask and wait," or "the system
already knows how to recover" is a declared fact per condition, not something decided in the
moment. `cfg_status_flow` gives the one entity that currently has a tracked lifecycle — `word` —
an ordered sequence of statuses, each with a named step that sets it, so "what does 'approved'
mean and what can set it" is answered by a table, not by convention.

**The shape repeats at every level of this project, which is really the point of writing this
document at all**: a start-up sequence that refuses to proceed on bad input, an escalation system
whose own rules are as governed as the questions it asks, a change-control loop that requires
proof before it trusts itself, a founding definition of the project that now lives in one place
addressable by pointer, and an analytical engine whose every step carries both a rule for what to
do and a check for whether it was done right. None of it is finished — every rule in §2 states
`enforced_by: not yet mechanically checked`, a deviation-monitoring mechanism still named as
missing everywhere it's cited; `docs/interaction-preferences.md`/`CLAUDE.md` §9 still duplicate
what §2's `chat`/`terminal` classes now state natively, quantified not resolved; §4's chapters 4–6
are flagged not-aligned; §3's own predecessor system failed once already, and so — one level up —
did two of the very documents meant to stop rules scattering in the first place (§3's closing
paragraph). But the shape is the same shape everywhere, which is the thing `wa_rule_registry`
never had.
