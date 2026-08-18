# Operational-behaviour rules — cfg encapsulation plan (parked)

**Raised:** 2026-08-18, in chat, by the researcher.
**Status:** Parked, to be worked as its own unit alongside/after the other unhomed global-rule
items (see [`docs/governance-alignment-register.md`](../../../docs/governance-alignment-register.md)
row 5, and escalation #714 for the sibling `GR-PROG-001` prose-authority item).

## The instruction, as given

> Quite a few of these [global rules] handle 'chat behaviour' (and there are others also that came
> up in the past). IBA `cfg.settings` should have a governance setting to regulate the project
> operational behaviours: chat, terminal, SQLite (and others). Then there should be a `cfg` where
> the custom rules for the different setup behaviours are encapsulated. This should include the use
> of the different guides and methods descriptions which currently is all over the place (e.g. user
> guide, governance, build, readme, etc.).

Three parts:

1. A `governance.*` setting naming the operational-behaviour-class taxonomy (chat, terminal,
   SQLite, documentation/guides, and others not yet identified) and anchoring where each class's
   rules live — the entry point, same pattern as the `GR-PROG-001` item's part (a).
2. A `cfg_*` table encapsulating the actual rule content per behaviour class — the "custom rules
   for the different setup behaviours."
3. That table's scope explicitly includes **which document is authoritative for which behaviour
   class** — the guide-sprawl problem (`USER-GUIDE.md`, `GOVERNANCE.md`, `BUILD.md`, `README.md`,
   `CLAUDE.md`, `docs/interaction-preferences.md`, memory) named directly as part of the same gap.

## What already exists (found while filing this, not yet acted on)

- `governance.rules_must_be_config_driven` already states the principle this whole item extends:
  *"no operational or process rule may exist only in GOVERNANCE.md, BUILD.md, USER-GUIDE.md, or
  memory without a referenced cfg_* row recording it as the evidence that the configuration control
  is in operation."* This item is that principle's own gap, applied to itself — the behaviour rules
  it demands live in cfg_* mostly don't yet.
- `governance.User_Guide_scope` is the one existing per-document scope statement (`"the user guide
  must reflect the latest state of all the tools..."`) — a partial precedent, but `GOVERNANCE.md`,
  `BUILD.md`, `README.md`, `CLAUDE.md` and `docs/interaction-preferences.md` have no equivalent
  scope row, and nothing maps "this behaviour class → this document" across the set.
- Two existing tables are the closest structural analogues for part 2, though neither is
  cross-cutting: `cfg_method_rule` (rule_key/rule_text/source_doc/enforced_by, keyed by analytical
  `step` — e.g. `hib.set`) and `cfg_escalation` (rule_key/rule_text/enforced_by, keyed to the
  escalation module only — its `chat_routing` row is, in fact, already a chat-behaviour rule, just
  scoped narrowly to escalation-routing rather than chat behaviour generally). Whether the new work
  extends one of these, adds a `behaviour_class` column to a shared shape, or is a genuinely new
  table is not decided here — left for scoping when this is picked up.

## Global rules paired into this class

Of the six `wa_rule_registry` principle-rules found unhomed 2026-08-18, three are operational-
behaviour rules (not research-content principles) and pair with this item:

| Rule | Behaviour class | Why it fits here |
|---|---|---|
| `GR-DB-001` — never assume DB state, always verify | SQLite | Directly a database-interaction discipline: check current state before acting, don't trust stale/assumed state. |
| `GR-PROC-001` — a step isn't complete until its output exists and is validated | Terminal / execution | A command/script-execution discipline — what "done" means when running an operation, independent of which operation. |
| `GR-REF-001` — single-authority content referencing across documents | Documentation / guides | This is literally the guide-sprawl problem named in the instruction — pointer-not-copy, one owning document per content type, staleness checks at version bumps. |

`GR-PROG-001` (verse always leads) is **not** included — already parked separately as escalation
#714 (prose-as-canonical-authority), a research-content item, not operational behaviour.

## Addendum 2026-08-18 — a fourth class: LLM/API-output discipline (`GR-PROG-009`)

Researcher, same session: `GR-PROG-009` (inferential-vs-confirmed labelling) is reframed as the
rule governing **what applies whenever the API or LLM is used** — content generated via an LLM/API
call (Claude's own output, subagent reports, WebSearch synthesis, STEP-derived interpretation, any
future automated classification) must not be presented as confirmed unless directly grounded in
verifiable source data; the drift this causes when not enforced has recurred repeatedly (matches
memory `feedback_never_model_output_on_prior_unreviewed_pass`,
`feedback_verify_db_claims_via_visible_tooling`, `feedback_source_of_truth_is_written_record`).
Researcher's own framing: *"I don't think there are any rules in cfg.* currently to guide Claude on
using API or LLM, and it may just be a subset of the chat behaviour cfg that is already planned."*

**Recommendation (Claude, for researcher decision when this is worked, not applied here):** make
it a **fourth peer class — `llm_output` — within this same mechanism**, not nested under `chat` and
not a separate parallel table/setting. Reasoning:

- `chat` (as scoped above) governs the *interaction channel/protocol* with the researcher — turn-
  taking, confirmation-before-acting, output-to-file, cost awareness. `llm_output` governs
  *epistemic trust in generated content* — a different failure mode (presenting inference as fact)
  that isn't specific to the chat channel: it applies equally to a prose draft, a DB write, a
  subagent's report, or an automated candidate-classification pass that never touches chat at all.
- Folding it under `chat` would make the `chat` class do two unrelated jobs (protocol discipline +
  epistemic discipline), and would miss the non-chat cases (subagents, automated pipelines) where
  the same discipline is needed just as much.
- It still belongs in the **same table/mechanism** as `chat`/`terminal`/`sqlite` (not a standalone
  table), because it's the same shape of thing — a named behaviour class with its own rule rows and
  its own authoritative-document pointer — and a fifth ad hoc table for one more class would
  re-fragment exactly what this item exists to stop fragmenting.

This recommendation is not applied/decided here — flagged for confirmation when the item is picked
up, per `governance.config_changes_require_researcher_approval`-style discipline (propose →
validate → escalate → apply, never silent).

**Reference-sweep note (parallel to `GR-PROG-002`'s, not GR-PROG-009's own — `GR-PROG-009` is
reframed/repointed, not retired):** `grep -rl "GR-PROG-009"` finds ~33 hits, again overwhelmingly
April–June 2026 archive/pre-reset material. Live/recent hits worth checking when this is worked:
`iba/app/verse-analysis/word_registry/Fear/wa-obslog-fear-synergise-v1-20260809.md`,
`iba/docs/windows debate/WA-inner-being-windows-register-v2.2-2026-08-11.md`,
`iba/docs/windows debate/WA-inner-being-windows-register-v2_3-2026-08-12.md`,
`iba/docs/windows debate/wa-obslog-ref-body-act-verbs-v1-20260810.md`,
`Logs/session-log-v1-20260715.md`. Not opened or characterised further here.

## Other known scattered material (candidates, not yet triaged)

Surfaced from memory/doc search while filing this — listed as pointers for whoever scopes this,
not pre-decided or folded in yet:

- `cfg_escalation.chat_routing` row (already DB-resident, escalation-scoped only).
- `docs/interaction-preferences.md` and `CLAUDE.md` §9 (Instruction Confirmation, Output-to-file,
  Factual Discipline, Cost Awareness) — main-project chat-behaviour rules with no IBA-side
  equivalent at all.
- `feedback_*` memory entries that are pure operational-behaviour rules rather than project facts,
  e.g. `feedback_verify_db_claims_via_visible_tooling`, `feedback_review_via_files_not_chat`,
  `feedback_heredoc_only_in_powershell`, `feedback_pre_op_db_snapshots_prune_or_skip`,
  `feedback_dont_sidestep_reported_ps_errors`, `feedback_no_hedge_pointers_in_complete_records`,
  `feedback_close_the_loop_not_just_investigate_and_report` — each currently lives only in Claude's
  memory files, exactly the "not config-driven" gap `governance.rules_must_be_config_driven` warns
  against.

## Cycle 1 — done (2026-08-18, researcher-approved via escalation #715 + comments file)

Researcher comments (`Workflow/Chat_responses/comments-operational-behaviour-plan`, 2026-08-18):
proceed; scope is project-wide, not `iba/app/**` only; start with the obvious ones and clear them,
then work everything else in later cycles; keep class boundaries in `governance.*` where unclear;
rule text must be definitive, not interpretive; no rule may live in both a document and cfg at
once; deviation from these rules must eventually be monitored, not just documented.

Built via `iba/app/migration/bootstrap_behaviour_rules_v1_20260818.py`: `cfg_behaviour_class` +
`cfg_behaviour_rule` tables (registered in `cfg_table`/`cfg_column`, write-granted to
`configmaint.propose`); `governance.operational_behaviour_control` anchor setting; five classes
(`chat` seeded empty — deliberately, see below); four rules seeded (`GR-DB-001` → `sqlite`,
`GR-PROC-001` → `terminal`, `GR-REF-001` → `documentation`, `GR-PROG-009` → `llm_output`), each
reworded as a definitive statement. Two pre-existing gaps `configmaint.validate` surfaced while
checking this (missing write-grants on `cfg_method_rule`/`cfg_quality_check`; this migration's own
zero-Cfg-usage flag) fixed via `fix_missing_write_grants_v1_20260818.py`. Full detail:
`BUILD.md` §145.

## Cycle 2 — done (2026-08-18): `Workflow/*` survey + guide sweep

Per the researcher's own sequencing, surveyed `Workflow/*` before writing more content. Found
`Workflow/Claude_API/`, `Workflow/SQLite/`, `Workflow/Obsidian/` (all 2026-08-15, never in
`CLAUDE.md`) holding real unclaimed rule content. `migration/bootstrap_behaviour_rules_cycle2_v1_
20260818.py` seeded 11 rules from them: 6 `llm_output`, 4 `sqlite`, 1 `documentation`. `chat` still
empty — none of the three docs cover the human-Claude protocol. The actual "failed prior attempt"
was identified as `wa_rule_registry` itself (confirmed via session-log search), not these three
guides — full detail `BUILD.md` §147.

**Cycles 3+ (not started, per "start with the obvious ones... then eat into everything else in
different focusses"):**

- Survey `Workflow/*` for prior (including failed) attempts to regulate the system — learn from
  what didn't stick before building further.
- Survey session logs for indicators of missing or misused rules.
- Audit `CLAUDE.md` + Claude's memory files for chat-behaviour content to migrate in (candidates
  already listed above: `docs/interaction-preferences.md`, CLAUDE.md §9, the `feedback_*` set).
- Consolidate `cfg_escalation.chat_routing` and any other pre-existing cfg row that belongs in this
  structure rather than its current narrower home.
- Decide and populate `authoritative_doc` per class (the actual guide-consolidation) —
  `USER-GUIDE.md`/`GOVERNANCE.md`/`BUILD.md`/`README.md`/`CLAUDE.md`/
  `docs/interaction-preferences.md` all currently carry rule-shaped content with no single owner
  per topic.
- Redefine the future procedural-document taxonomy the researcher named: (a) planning/investigatory
  documents, (b) config-extract documents (generated, not hand-authored, for easier digesting of
  cfg_*), (c) history-of-changes (possibly DB/engine-resident rather than a document), (d)
  guidance/baseline instructions.
- Quantify (not yet rectify) how many existing documents/data are affected once each class's rules
  are actually enforced.
- Build the deviation-flagging/ongoing-monitoring mechanism `enforced_by` currently just names as
  missing.
- Any conflicts or gaps surfaced along the way get escalated, not silently resolved or dropped.
