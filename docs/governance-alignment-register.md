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
| 2 | 2026-08-15 | Filing & archiving rules (`docs/file-organisation-rules.md` vs. IBA's config-driven governance model) | Researcher: filing/archiving rules "should be defined in the configs" from an application perspective — current main-project filing rules live only as prose in `docs/`, with no `cfg_*` equivalent, unlike IBA's own filing conventions (which are config-registered per the IBA governance model). | Not yet scoped. Recommended: fold into the file-store-consolidation step (step 2 of the alignment plan) rather than run as a standalone thread, since it's really "what should the consolidated filing rule be" applied to the whole project, config-defined for IBA's own use. | **Proposed** | Researcher note (2026-08-15): agreed this belongs inside step 2's plan, not a separate fifth item. |
| 3 | 2026-08-15 | Session-start engagement with IBA governance | Researcher: "the first step in the alignment plan is to ensure that you right from the start fully engage with the governance defined in the app" — i.e. every session, not just IBA-specific ones, should read and be bound by `iba/app/GOVERNANCE.md`'s live rules, not just consult it when doing IBA work. | Reflected in memory (`feedback_iba_session_start_read_live_docs_not_memory`, extended); no doc change proposed yet — this is an operating-practice commitment, not a document edit. Flag here so it isn't lost as the register grows. | **Acknowledged — no action item** | Practice change, effective immediately per the researcher's instruction; not a `cfg_*`/doc edit to track through the workflow above. |

## Not yet surveyed

The full `Workflow/Instructions/` set, `docs/interaction-preferences.md`, `README.md`, and the
IBA `GOVERNANCE.md`/`BUILD.md` pair have not been swept end-to-end for conflicts — item #1 above
was surfaced by the 2026-08-15 sanity check, not by a systematic pass. A systematic sweep is the
next piece of work under this step, to be scoped and confirmed with the researcher rather than
run as an open-ended background task.
