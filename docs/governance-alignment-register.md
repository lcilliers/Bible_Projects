# Governance Alignment Register

> **★ RETIRED 2026-08-18 — superseded by the escalation table.** Researcher instruction, 2026-08-18:
> "you should retire the open register. The authoritative task and open item system is the
> escalation table" — matching `governance.escalation.scope` (already live: *"all open items,
> discovery of anomalies, clarifications and other forms of escalation must be recorded in
> escalation using escalation rules"*). This file is kept for provenance (history of the
> 2026-08-15 alignment plan and how each item was actually worked) — not deleted, per
> [[feedback_single_living_register]] — but is no longer the live tracker: don't add new rows here,
> don't read it at session start. Every open item, past or future, lives in `escalation` from now
> on (`iba/app/ps/Escalation.ps1 -Action List`). `CLAUDE.md` and `start-project` updated to point
> to the escalation table instead of this file.
>
> **Correlation of each numbered item below to its actual escalation row** (verified against the
> live `escalation` table 2026-08-18, not assumed):
>
> | Register # | Escalation | State | Note |
> |---|---|---|---|
> | 1 | #687 | completed | Direct match. |
> | 2 | #650 | **on-hold** | #688 (a later duplicate registration of the same item) was closed 2026-08-17 "duplicate of 650" — #650 is the substantive row, still on-hold pending the researcher's deeper filing review. |
> | 3 | — | acknowledged, no action item | Practice change, never tracked as its own escalation — correctly so, nothing to close. |
> | 4 | #689 | completed | Resolved via #5/#690 per the register's own note. |
> | 5 | #690 | completed | Direct match. |
> | 6 | #691 | **completed** | Direct match — and this corrects the register's own stale text below ("B: Proposed... not started"): #691's resolution shows part B (content-index round B) was actually built and run for real 2026-08-17, 7,869 files / 14.1M rows. The register file was not updated after the fact; the escalation row is what's current. |
> | 6, minor loose thread (retire `build_file_manifest.py`) | #730 | raised (new, 2026-08-18) | Not covered by #691 — had no escalation row until this retirement pass surfaced it. |
> | 7 | #648 / #698 / #699 | all complete | Direct match, register's own text already current. |
> | "Not yet surveyed" section | #714/#715 (partial) + #731 (new, 2026-08-18) | in-progress / raised | #714/#715 cover only the narrower 6-unhomed-global-rule subset (GR-DB-001/PROC-001/REF-001/PROG-001/PROG-002/PROG-009); the broader systematic sweep of `Workflow/Instructions/`, `docs/interaction-preferences.md`, `README.md` had no escalation row until #731. |
>
> Two gaps found and closed during this retirement (per `governance.escalation.scope` — an open
> item cannot be allowed to fall out of tracking just because its container document is retired):
> escalations **#730** and **#731** raised 2026-08-18, both `raised`/unanswered, assigned to
> Researcher.

> Living register for the project-wide governance/documentation alignment work (step 1 of the
> 2026-08-15 consolidation plan — see
> [`outputs/markdown/project-review-response-2-20260815.md`](../outputs/markdown/project-review-response-2-20260815.md)).
> The researcher authorised proceeding on this step 2026-08-15, explicitly as a controlled,
> ongoing process — not a one-shot edit: **keep this register current, surface every conflict or
> point of confusion found, ask before each change lands, expect this to take a considerable
> time.** Update in place (per [[feedback_single_living_register]]); strike/annotate reversed
> items rather than deleting history.

## Purpose

`iba/app/GOVERNANCE.md` already works and is being followed in practice (confirmed by the
2026-08-15 sanity check: clean git state, `governance.build_md_on_code_change` and
`governance_md_on_rule_change` both live and actually applied). The main project's governance
documents (`CLAUDE.md` foremost) have not caught up to the architecture the researcher confirmed
2026-08-15 — `iba.db` now owns process control + the base data layer; `bible_research.db` keeps
prose + analytic findings. This register tracks bringing the two into one coherent, enforced set
of rules across the whole project, per the researcher's stated end goal ("the IBA App should
become the project processing engine and all the rules defined in the governance should equally
apply for the entire project, not only for the IBA branch. Ultimately the filing in the IBA
branch must be consolidated with the main project").

## How to use this register

- One row per identified conflict/gap. Status: `Proposed` (awaiting researcher approval) →
  `Approved` → `Applied` → `Verified`, or `Declined`/`Redirected` if the researcher chooses
  differently.
- **No item moves past `Proposed` without an explicit researcher decision recorded here.**
- When applying an `Approved` item, record the commit/file touched and re-verify against the live
  docs before marking `Verified` — don't take the edit's own success as proof it's coherent with
  everything around it.
- Conflicts found while working an item go in as new rows, not silently folded into the fix.

## Register

| # | Date raised | Area | Conflict / gap | Proposed resolution | Status | Notes |
|---|---|---|---|---|---|---|
| 1 | 2026-08-15 | `CLAUDE.md` §4 (Engine), §5 (STEP client), §7 (Word Study Pipeline), §8 (Data Flow) | Present the old `engine/` / STEP pipeline as the live, authoritative route for base-layer work (word initiation → verse-lexical). Per the 2026-08-15 architecture correction, that layer is now owned entirely by `iba.db`/`iba/app/`; these sections are stale, not current — a session reading `CLAUDE.md` cold would route new base-layer work to the wrong system. | Add a superseded-by banner over §4/§5/§7/§8 (same pattern as the existing method-reset banners at the top of the file) stating the base layer moved to IBA, pointing to `iba/app/USER-GUIDE.md`, marking these sections **provenance-only** (accurate history, not live instruction). Not a rewrite/deletion — matches the file's own established convention for prior pivots. | **Applied** | Approved 2026-08-17 (escalation #687, "as suggested"). Top-of-file banner added, plus a short inline pointer under each of §4/§5/§7/§8's own headers (matching §3's existing inline-note convention) so the flag is visible at point of use, not only at the top. Content not deleted — marked provenance-only. |
| 2 | 2026-08-15 | Filing & archiving rules (`docs/file-organisation-rules.md` vs. IBA's config-driven governance model) | Researcher: filing/archiving rules "should be defined in the configs" from an application perspective — current main-project filing rules live only as prose in `docs/`, with no `cfg_*` equivalent, unlike IBA's own filing conventions (which are config-registered per the IBA governance model). | Not yet scoped. Recommended: fold into the file-store-consolidation step (step 2 of the alignment plan) rather than run as a standalone thread, since it's really "what should the consolidated filing rule be" applied to the whole project, config-defined for IBA's own use. | **Proposed** | Researcher note (2026-08-15): agreed this belongs inside step 2's plan, not a separate fifth item. Scoping now underway alongside #6 (manifest/content-search) below — both are step 2's concrete content. |
| 3 | 2026-08-15 | Session-start engagement with IBA governance | Researcher: "the first step in the alignment plan is to ensure that you right from the start fully engage with the governance defined in the app" — i.e. every session, not just IBA-specific ones, should read and be bound by `iba/app/GOVERNANCE.md`'s live rules, not just consult it when doing IBA work. | Reflected in memory (`feedback_iba_session_start_read_live_docs_not_memory`, extended); no doc change proposed yet — this is an operating-practice commitment, not a document edit. Flag here so it isn't lost as the register grows. | **Acknowledged — no action item** | Practice change, effective immediately per the researcher's instruction; not a `cfg_*`/doc edit to track through the workflow above. |

| 4 | 2026-08-15 | `wa_rule_registry` GR-LOAD-001 + GR-OBS-001 (category `session_startup`) vs. CLAUDE.md §9 | Both rules live in the DB with `obsolete=0`, `applies_to="all sessions..."` — literally unretired. But the rule text addresses "Claude AI" by name (the old chat-based analytical role) and its rationale ("Claude AI forgets between sessions") doesn't fit Claude Code's tool/file-access model. `last_modified` 2026-04-21/04-27 — unrevised across the 2026-06-25 reset, 2026-07-02 verse-first pivot, 2026-08-03 old-method closure, and 2026-08-15 IBA architecture correction. CLAUDE.md §9 already defines this session's actual interaction protocol and never references either rule. | Superseded by item #5's broader resolution — the whole table is now obsolete, not just these two rows. | **Resolved via #5** | Folded into #5's blanket decision rather than answered narrowly; see #5. |
| 5 | 2026-08-15 | `wa_rule_registry` (all categories, not just `session_startup`) / `Workflow/Global_rules/*` vs. `iba/app/GOVERNANCE.md` | Researcher directive: the global rules generally — not only GR-LOAD-001/GR-OBS-001 (item #4 is one concrete instance of this) — need to be revised and brought into alignment with the IBA App's governance. | **Resolved 2026-08-17** (escalation #696, researcher decision): *"the table wa-rule-register must be set to inactive. the rules in this table are replace with configs in iba and this table is therefore no longer operational. references in code, claude.md or other memory to this table should be replaced with pointing to cfg.* configs."* Applied: all 59 `wa_rule_registry` rows (34 previously active) set `obsolete=1`, `superseded_by='iba.db cfg_* configuration system'`. `CLAUDE.md` §3/§9/§10 updated — the `wa_rule_registry` table-group row struck through, the `wa-global-general-rules` document-architecture row marked superseded, all three `GR-REF-002` citations replaced with a direct statement of the `[current]`-token convention (which CLAUDE.md already fully defines inline — losing the DB citation doesn't lose the rule). Full review that preceded the decision: [`outputs/markdown/wa-rule-registry-full-review-v1-20260817.md`](../outputs/markdown/wa-rule-registry-full-review-v1-20260817.md) (34-rule triage) + its `governance.*` cross-reference addendum. | **Applied** | Note for a future pass, not fixed here: the review had found `GR-DB-001`/`GR-REF-001`/`GR-PROC-001`/`GR-PROG-001`/`GR-PROG-002`/`GR-PROG-009` still describing genuinely-live principles with no `cfg_*` equivalent yet (the review's "Keep" bucket) — the researcher's blanket decision supersedes that finer triage; those principles now have no operational home anywhere, not even the obsoleted table, until/unless re-homed into a live doc or `cfg_*`. |
| 6 | 2026-08-15 | Manifest management (build/update/search) + project-file content search — currently a main-repo script (`scripts/build_file_manifest.py`) and a not-yet-built content-search capability, neither governed by IBA | Researcher: the rules, user guide, and methods to use/update/search the manifest must be built into the IBA App; separately, content search across the project's non-prose `.md` files (project-wide, including `archive/`) is needed for the upcoming detail-design/findings review-and-consolidation phase feeding prose summaries. Prose search (`prose_section_fts`) and any future `bible_research.db` analytic-findings reports are explicitly out of scope. | **A built and verified 2026-08-15** — `manifest.rebuild`/`manifest.search`, `iba/app/lib/manifest.py`, `bootstrap_file_manifest.py`, PS entry points, `USER-GUIDE.md` §13a, `BUILD.md` §112. Ran for real: 18,653 files indexed, field + free-text search both confirmed correct, `configmaint.validate` clean on everything this migration touched. One own-bug found+fixed mid-build (missing `config_module` enum value); two **pre-existing, unrelated** `cfg_report_csv_table` errors surfaced incidentally (`report.registry`/`report.cluster` naming non-existent tables) — left open as escalation #642 for researcher judgement, not fixed here (out of scope). **B (content search) not started** — plan at [`outputs/markdown/manifest-and-content-search-into-iba-plan-v1-20260815.md`](../outputs/markdown/manifest-and-content-search-into-iba-plan-v1-20260815.md) stands as scoped. | **A: Applied — B: Proposed** | Open follow-up not yet decided: whether/when to retire `scripts/build_file_manifest.py` + `database/file_manifest.json` now that IBA owns this (same superseded-by-banner question as register item #1, not yet raised for a decision). |

| 7 | 2026-08-16 | Project-wide config-driven-rule sweep (escalation #648) — scripts across the WHOLE project (not only `iba/app/`) with hardcoded variables/rules/lookups that should be `cfg_*`-driven | Raised 2026-08-16, held "until further instruction," approved 2026-08-17 ("implement as suggested"). Traced before touching anything: **this is not a new item** — it's Phase 2/3 of the already-approved `engine-controls-migration-plan-v4` (`iba/app/reports/engine-controls-migration-plan-v4-20260817.md`), which the researcher's own prior answer on #672 explicitly gated: *"phase 2 and phase 3 is on hold until phase 0 and 1 is completed."* Phase 1 (`engine/`, 11 files) is done (BUILD.md §127). Phase 0 (the `governance.new_utility_registration_timing` rule + its enforcement check, `cfgquality.find_unregistered_project_scripts`) has its CODE built and verified (343 unregistered files confirmed live, 331 under `scripts/`, 9 under `iba/`, 2 under `research/` — `engine/`'s own 11 no longer counted, already resolved) but its `cfg_setting` row was never actually applied — blocked behind #671, which is now clear. | Phase 0 (`#698`) approved and applied for real. Phase 2/3 (`#699`) approved as option (b) — register all 343, mark any not clearly alive inactive — and executed as one governed batch (not 343 individual proposals): `cfg_utility` 48→391 rows, 202 active/141 inactive, `purpose` from each file's own docstring, `inactive` only where a filename carries a version+date one-off stamp. Full detail: `iba/app/BUILD.md` §132, `iba/app/reports/unregistered-scripts-batch-registration-20260817.md`. | **#648/#698/#699 all complete** | **2026-08-17, later still**: `#648`'s actual content review delivered — `iba/app/reports/hardcoded-constants-sweep-20260817.md`, 232 scripts scanned via `ast.parse`, 105 files/263 real candidate constants (Tier 1) vs. 177 files/423 structural false-positives correctly excluded (Tier 2). Full record: `BUILD.md` §135. Migrating any specific Tier 1 candidate into `cfg_setting` is separate, un-started follow-on work — this register entry covers the review only. Earlier history: `find_unregistered_project_scripts()` confirmed 0 remaining after `#699`'s write; one own-mistake mid-flight on `#698`'s first attempt (malformed JSON), self-corrected via escalation #697; one bug caught before writing any of the 343 rows (a DOTALL regex swallowing past the real docstring — rewritten to use `ast.get_docstring()`, verified by spot-check before the batch write, not after). |

## Not yet surveyed

The full `Workflow/Instructions/` set, `docs/interaction-preferences.md`, `README.md`, `wa_rule_registry`
in full (all categories, not just `session_startup`), and the IBA `GOVERNANCE.md`/`BUILD.md` pair
have not been swept end-to-end for conflicts — items #1 and #4 above were each surfaced
individually, not by a systematic pass. Item #5 now formally owns the `wa_rule_registry` /
`Workflow/Global_rules/*` half of that sweep; scoping it (and confirming the approach with the
researcher before running it) is the next piece of work under this step.
