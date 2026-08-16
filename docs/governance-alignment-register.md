# Governance Alignment Register

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
| 1 | 2026-08-15 | `CLAUDE.md` §4 (Engine), §5 (STEP client), §7 (Word Study Pipeline), §8 (Data Flow) | Present the old `engine/` / STEP pipeline as the live, authoritative route for base-layer work (word initiation → verse-lexical). Per the 2026-08-15 architecture correction, that layer is now owned entirely by `iba.db`/`iba/app/`; these sections are stale, not current — a session reading `CLAUDE.md` cold would route new base-layer work to the wrong system. | Add a superseded-by banner over §4/§5/§7/§8 (same pattern as the existing method-reset banners at the top of the file) stating the base layer moved to IBA, pointing to `iba/app/USER-GUIDE.md`, marking these sections **provenance-only** (accurate history, not live instruction). Not a rewrite/deletion — matches the file's own established convention for prior pivots. | **Proposed** | Awaiting researcher approval before any edit to `CLAUDE.md`. |
| 2 | 2026-08-15 | Filing & archiving rules (`docs/file-organisation-rules.md` vs. IBA's config-driven governance model) | Researcher: filing/archiving rules "should be defined in the configs" from an application perspective — current main-project filing rules live only as prose in `docs/`, with no `cfg_*` equivalent, unlike IBA's own filing conventions (which are config-registered per the IBA governance model). | Not yet scoped. Recommended: fold into the file-store-consolidation step (step 2 of the alignment plan) rather than run as a standalone thread, since it's really "what should the consolidated filing rule be" applied to the whole project, config-defined for IBA's own use. | **Proposed** | Researcher note (2026-08-15): agreed this belongs inside step 2's plan, not a separate fifth item. Scoping now underway alongside #6 (manifest/content-search) below — both are step 2's concrete content. |
| 3 | 2026-08-15 | Session-start engagement with IBA governance | Researcher: "the first step in the alignment plan is to ensure that you right from the start fully engage with the governance defined in the app" — i.e. every session, not just IBA-specific ones, should read and be bound by `iba/app/GOVERNANCE.md`'s live rules, not just consult it when doing IBA work. | Reflected in memory (`feedback_iba_session_start_read_live_docs_not_memory`, extended); no doc change proposed yet — this is an operating-practice commitment, not a document edit. Flag here so it isn't lost as the register grows. | **Acknowledged — no action item** | Practice change, effective immediately per the researcher's instruction; not a `cfg_*`/doc edit to track through the workflow above. |

| 4 | 2026-08-15 | `wa_rule_registry` GR-LOAD-001 + GR-OBS-001 (category `session_startup`) vs. CLAUDE.md §9 | Both rules live in the DB with `obsolete=0`, `applies_to="all sessions..."` — literally unretired. But the rule text addresses "Claude AI" by name (the old chat-based analytical role) and its rationale ("Claude AI forgets between sessions") doesn't fit Claude Code's tool/file-access model. `last_modified` 2026-04-21/04-27 — unrevised across the 2026-06-25 reset, 2026-07-02 verse-first pivot, 2026-08-03 old-method closure, and 2026-08-15 IBA architecture correction. CLAUDE.md §9 already defines this session's actual interaction protocol and never references either rule. | Researcher decision needed: (a) apply full obslog discipline (verbatim capture, three-step startup gate, versioned obslog files) to Claude Code sessions going forward, or (b) mark both `obsolete=1` in `wa_rule_registry` (superseded_by → CLAUDE.md §9 + the living-register pattern), since the role split and method pivots have left them stale. | **Proposed** | Raised when the researcher asked directly whether Claude Code is bound by the global startup rules; not decided either way pending this answer. |
| 5 | 2026-08-15 | `wa_rule_registry` (all categories, not just `session_startup`) / `Workflow/Global_rules/*` vs. `iba/app/GOVERNANCE.md` | Researcher directive: the global rules generally — not only GR-LOAD-001/GR-OBS-001 (item #4 is one concrete instance of this) — need to be revised and brought into alignment with the IBA App's governance. Scope not yet a systematic pass: how many `wa_rule_registry` categories/rows exist, which are still `obsolete=0`, which conflict with (or duplicate, or are already superseded by) a live `cfg_*`/`GOVERNANCE.md` rule in `iba/app/`, has not been surveyed. | Not yet scoped — this is the researcher's stated goal for the "align governance/docs" step, not a specific fix proposed for approval. Next piece of work: a systematic pass over `wa_rule_registry` (all categories) cross-referenced against `iba/app/GOVERNANCE.md`'s live `cfg_*` rules, producing one register row per conflict found (same pattern as item #1/#4), rather than a single blanket rewrite. | **Directed — not yet scoped** | Researcher instruction, 2026-08-15: "the global rules need to be revised and aligned with the IBA App." Supersedes/broadens the "Not yet surveyed" note below — that systematic sweep is now this item's scope, not an open-ended future task. |
| 6 | 2026-08-15 | Manifest management (build/update/search) + project-file content search — currently a main-repo script (`scripts/build_file_manifest.py`) and a not-yet-built content-search capability, neither governed by IBA | Researcher: the rules, user guide, and methods to use/update/search the manifest must be built into the IBA App; separately, content search across the project's non-prose `.md` files (project-wide, including `archive/`) is needed for the upcoming detail-design/findings review-and-consolidation phase feeding prose summaries. Prose search (`prose_section_fts`) and any future `bible_research.db` analytic-findings reports are explicitly out of scope. | **A built and verified 2026-08-15** — `manifest.rebuild`/`manifest.search`, `iba/app/lib/manifest.py`, `bootstrap_file_manifest.py`, PS entry points, `USER-GUIDE.md` §13a, `BUILD.md` §112. Ran for real: 18,653 files indexed, field + free-text search both confirmed correct, `configmaint.validate` clean on everything this migration touched. One own-bug found+fixed mid-build (missing `config_module` enum value); two **pre-existing, unrelated** `cfg_report_csv_table` errors surfaced incidentally (`report.registry`/`report.cluster` naming non-existent tables) — left open as escalation #642 for researcher judgement, not fixed here (out of scope). **B (content search) not started** — plan at [`outputs/markdown/manifest-and-content-search-into-iba-plan-v1-20260815.md`](../outputs/markdown/manifest-and-content-search-into-iba-plan-v1-20260815.md) stands as scoped. | **A: Applied — B: Proposed** | Open follow-up not yet decided: whether/when to retire `scripts/build_file_manifest.py` + `database/file_manifest.json` now that IBA owns this (same superseded-by-banner question as register item #1, not yet raised for a decision). |

## Not yet surveyed

The full `Workflow/Instructions/` set, `docs/interaction-preferences.md`, `README.md`, `wa_rule_registry`
in full (all categories, not just `session_startup`), and the IBA `GOVERNANCE.md`/`BUILD.md` pair
have not been swept end-to-end for conflicts — items #1 and #4 above were each surfaced
individually, not by a systematic pass. Item #5 now formally owns the `wa_rule_registry` /
`Workflow/Global_rules/*` half of that sweep; scoping it (and confirming the approach with the
researcher before running it) is the next piece of work under this step.
