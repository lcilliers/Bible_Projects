# Document index — every file/document referenced across #753's branch

> Built 2026-08-26 for escalation #857, from a fresh `Escalation.ps1 -Action History -Id 753` run
> (`iba/app/reports/escalation-753-history.md`, 46 escalation sections, 1,501 lines). Every
> section's comment/context/resolution/tried text was scanned for repo-relative file paths;
> nothing summarised or pre-filtered before the tiering below.

## How the branch was actually computed (read this before the tables)

`-Action History`'s own algorithm (per its `cfg_step.does` text) pulls: the target item, its
**downward chain** (real `from_id` children — structural genealogy), **plus every item its
`related_activity` text names or is named by** — and that third leg turned out to walk *any*
`#NNN` mention anywhere in an item's free text, transitively, not just the structured
`related_activity` field. Checked live against the actual `from_id` column for all 46 returned
IDs (§below) to separate genuine genealogy from text-reference bleed. Three tiers result:

- **Tier 1 (22 items)** — real descendants: `from_id` chases back to 753.
- **Tier 2 (12 items)** — escalation-tooling items, same subject matter, but `from_id` does
  **not** connect them to 753 (mostly `-1` or `None`) — pulled in by a `#NNN` mention somewhere.
- **Tier 3 (11 items)** — the entire prose-management branch (#784 and its descendants). These
  are pulled in **only** because #857's own comments this session (mine) cited escalation numbers
  like #829/#833/#836/#851/#854/#855 in free prose while answering the researcher's questions —
  not because they relate to #753's subject (the escalation utility) at all. **Flagged, not
  pruned** — this is a real side-effect of the History report's own text-scanning worth the
  researcher's attention in its own right (a `#NNN` mention in prose is being treated as a
  structural link), separate from the document-index task itself.

## Tier 1 — genealogical descendants of #753 (`from_id` chain)

| Escalation | State | from_id | Title | Files referenced |
|---|---|---|---|---|
| #753 | in-progress | — (root) | Escalation utility Refinement | `iba/app/lib/cfgquality.py`; `iba/docs/escalation-config-review-v1-20260820.md`; `iba/docs/escalation-config-review-v2-20260820.md`; `iba/docs/escalation-decision-vs-defect-axis-proposal-v1-20260822.md` |
| #6 | completed | 753 | Escalation rebuild follow-ups outstanding, per #753 | `BUILD.md`/`GOVERNANCE.md`/`CLAUDE.md` (3 files, run together in source text — see data-quality notes); `iba/docs/escalation-design-decision-register-v2`…`v6-20260821.md` (5 files); `iba/docs/escalation-design-plan-v1`…`v3-20260820.md` (3 files); `iba/app/migration/fix_from_id_closed_items_20260821.py` |
| #750 | completed | 753 | cfg_write_grant Orphan (writer=run) | `iba/app/migration/fix_from_id_closed_items_20260821.py` |
| #754 | completed | 753 | Escalation.ps1 Positional-Binding Bug | `iba/app/migration/fix_from_id_closed_items_20260821.py` |
| #755 | completed | 753 | Escalation-Module Config Review | `iba/docs/escalation-config-review-v1-20260820.md`; `iba/docs/escalation-config-review-v2-20260820.md`; `iba/app/migration/fix_from_id_closed_items_20260821.py` |
| #759 | completed | 753 | escalation.short_description Column-Spec Violation | `iba/app/migration/fix_escalation_short_description_and_columns_20260820.py`; `iba/app/migration/fix_from_id_closed_items_20260821.py` |
| #798 | completed | 753 | Escalation core model: decision-vs-defect axis | `iba/app/lib/escalation.py` + `iba/app/run.py` (joined in source, see notes); `iba/docs/escalation-decision-vs-defect-axis-proposal-v1`…`v5-20260822.md` (5 files) |
| #857 | in-progress | 753 | escalation actions governance (this item) | `iba/app/handlers/reports.py`; `iba/app/lib/escalation.py`; + the 5 report files this thread itself produced (`escalation-comment-context-resolution-config-rules`, `escalation-governance-rules-and-enums-full-extract`, `escalation-reports-config-rules`, `escalation-review-action-config-rules`, `escalation-table-column-rules-full-extract`, all `-20260826.md`) |
| #8 | completed | 6 | PS scripts bypassing run.py are outside governance | `iba/app/migration/add_ps_scripts_dispatch_through_run_py_rule_20260821.py`; `iba/app/BUILD.md` §44 (mis-parsed as a path fragment, see notes) |
| #743 | completed | 6 | Escalation.ps1 Manual-Verb Wrapper Gap | `iba/app/lib/escalation.py`; `iba/app/migration/fix_from_id_closed_items_20260821.py` |
| #744 | completed | 6 | GOVERNANCE.md / USER-GUIDE.md Escalation Drift | `iba/app/migration/fix_from_id_closed_items_20260821.py` |
| #745 | completed | 6 | escalation_history Write-Grant Gap | `iba/app/migration/fix_escalation_history_write_grant_20260820.py`; `iba/app/migration/fix_from_id_closed_items_20260821.py` |
| #747 | completed | 6 | write_history_report() Entry-Point Gap | `iba/app/lib/escalation.py`; `iba/app/migration/fix_from_id_closed_items_20260821.py` |
| #763 | completed | 6 | from_id built immutable, contradicting recorded instruction | `iba/app/lib/escalation.py`; `iba/app/migration/fix_from_id_mutability_20260821.py` |
| #767 | completed | 8 | PS scripts still bypassing run.py after #8 | `iba/app/migration/fix_from_id_closed_items_20260821.py` |
| #768 | on-hold | 767 | Mismatched-pairing check only catches one direction | `iba/app/lib/escalation.py` |
| #769 | withdraw | 767 | escalation CLI crashed: an update carrying comment/context… | (none) |
| #773 | completed | 767 | from_id=0 sentinel is indistinguishable from NULL | `iba/app/lib/escalation.py` |
| #774 | completed | 767 | update() cannot correct a closed escalation at all | `iba/app/lib/escalation.py` |
| #765 | withdraw | 750 | escalation CLI crashed: next_action='ready_for_approval'… | (none) |
| #746 | completed | 759 | cfg_escalation Rule-Table Staleness | `iba/docs/escalation-system-mechanics-20260818.md`; `iba/app/migration/fix_module_blocking_enforced_by_20260821.py` |
| #799 | completed | 798 | Build: escalation decision-vs-defect axis (#798) | `iba/app/handlers/base.py`; `iba/app/lib/cfgquality.py`; `iba/app/lib/prosestore.py`; `iba/docs/escalation-decision-vs-defect-axis-proposal-v5-20260822.md`; `iba/app/migration/bootstrap_decision_vs_defect_axis_v1_20260822.py` |

## Tier 2 — escalation-tooling items, topically related, NOT genealogically under #753

| Escalation | State | from_id | Title | Files referenced |
|---|---|---|---|---|
| #794 | completed | -1 | CORRECTION (re-raised, supersedes withdrawn #793)… | (none) |
| #795 | completed | 794 | Dispatcher AnswerRun collapses approve/reject/revise | `iba/app/BUILD.md`; `iba/app/GOVERNANCE.md`; `iba/app/handlers/reports.py`; `iba/app/lib/escalation.py`; `iba/app/lib/prosestore.py`; `iba/app/migration/fix_dispatcher_answerrun_795_20260822.py`; `iba/docs/escalation-795-outstanding-review-v1-20260822.md`; `iba/docs/escalation-decision-vs-defect-axis-proposal-v1-20260822.md`; `iba/docs/escalation-type-routing-proposal-v1-20260822.md` |
| #797 | completed | 795 | escalation CLI crashed: 'Review' is not a member of cfg_enum… | (none) |
| #819 | completed | 795 | escalation CLI crashed: next_action='ready_for_approval'… | `iba/app/BUILD.md`; `iba/app/lib/escalation.py`; `iba/app/migration/fix_dispatcher_answerrun_795_20260822.py`; `iba/docs/escalation-type-routing-proposal-v1-20260822.md` |
| #790 | completed | — | raise_() skips cfg_escalation_requirement entirely | `iba/app/lib/escalation.py` (referenced twice, once short-form) |
| #791 | completed | 790 | escalation CLI crashed: next_action='approved' requires resolution… | (none) |
| #828 | completed | — | Governance anchor: test plan per module/utility | `iba/app/GOVERNANCE.md`; `iba/app/migration/anchor_test_plan_governance_rule_20260822.py` |
| #851 | raised | — | noted has no authority check unlike approved | `iba/app/lib/escalation.py` |
| #855 | raised | — | Correction lacks the decision_required carve-out Update has | `iba/app/lib/escalation.py` |
| #736 | on-hold | -1 | Main-Project / IBA Filing Consolidation | `outputs/markdown/iba-table-review-response-v1-20260816.md` |
| #737 | on-hold | -1 | IBA Debate-Pipeline to research_db Migration (Gated) | (none) |
| #738 | on-hold | -1 | Cluster-Assignment Backfill Exceptions | `iba/app/reports/cluster-assign-v2-20260817.md` |

## Tier 3 — prose-management branch (text-reference bleed, not related to #753's subject)

| Escalation | State | from_id | Title | Files referenced |
|---|---|---|---|---|
| #784 | re-assigned | -1 | Prose Management | 25 files — `docs/prose-store-architecture.md`; `iba/app/handlers/prose.py`; `iba/app/handlers/lexical.py`; `iba/app/lib/prosestore.py`; 8× `iba/docs/prose-*.md`; `outputs/markdown/prose-edit-programme-chapter-2/3-20260822.md`; `iba/app/ps/Prose.ps1`; `research/discovery/prose-config-extract-20260821.md`; `research/discovery/prose-files-inventory-20260821.md`; 5× `scripts/*prose*.py` |
| #785 | withdraw | 784 | Prose Management | (none) |
| #786 | raised | 784 | Programme Prose Chapter 4 | (none) |
| #787 | completed | — | New cfg_setting 'prose.extractor_version'… | `iba/docs/prose-store-iba-incorporation-plan-v2-20260822.md`; `scripts/build_programme_prose_extract.py` |
| #829 | in-progress | 784 | Prose management: IBA first-layer plan + build | 19 files — `Logs/SESSION-LOG-20260824-829-…md`; `archive/patches/test-829-write-path-forward.json`; `docs/prose-store-architecture.md`; `iba/app/handlers/prose.py`; `iba/app/migration/flag_management_build_v1_20260823.py`; `iba/app/migration/prose_change_log_build_v1_20260824.py`; 9× `iba/docs/prose-management-iba-first-layer-proposal-v1`…`v9`; `iba/docs/flag-management-prose-*.md` (2); `iba/docs/prose-management-784-conversation-capture-v1-20260823.md`; `iba/docs/prose-store-iba-incorporation-plan-v4-20260822.md` |
| #831 | re-assigned | 784 | Prose add/edit operational rules layer | `iba/docs/prose-management-784-conversation-capture-v1-20260823.md`; `iba/docs/prose-management-iba-first-layer-proposal-v1-20260823.md`; `iba/docs/prose-management-iba-first-layer-proposal-v8-20260824.md` |
| #832 | raised | 784 | prose_section family: schema/data-hygiene defects found | `docs/prose-store-architecture.md`; `iba/docs/prose-management-iba-first-layer-proposal-v2-20260823.md` |
| #833 | re-assigned | 784 | Flag Management | `backups/bible_research_pre_flagmgmt_20260823_162030.db`; `database/bible_research.db` + `iba/app/db/iba.db` (joined in source, see notes); `iba/app/migration/flag_management_build_v1_20260823.py`; `iba/docs/flag-management-current-status-v1-20260823.md`; `iba/docs/flag-management-proposal-v1-20260823.md`; `iba/docs/flag-management-prose-quality-repurpose-capture-v1-20260823.md`; `iba/docs/prose-management-iba-first-layer-proposal-v3-20260823.md` |
| #835 | on-hold | — | Prose quality-flag fix utility (angle b) | `iba/docs/prose-management-iba-first-layer-proposal-v5-20260823.md` |
| #836 | completed | — | Prose change log design (versioning integrity) | 18 files — `docs/prose-store-architecture.md`; `iba/app/GOVERNANCE.md`; `iba/app/lib/prosestore.py`; `iba/app/migration/prose_change_log_build_v1_20260824.py`; 9× `iba/docs/prose-change-log-design-v1`…`v9-20260824.md`; 3× `iba/docs/prose-change-log-proposal-v1`…`v3-20260824.md`; `iba/docs/prose-management-iba-first-layer-proposal-v5-20260823.md`; `scripts/apply_session_patch.py` |
| #854 | raised | — | 3 prose_section_type enums have no real enforcement | (none) |

## Data-quality notes surfaced while building this index

> **★ 2026-08-26 CORRECTION, found on self-review:** items 1 and 3 below originally claimed "9
> duplicate-prefix pairs" and "93 distinct real files." Re-run programmatically against the actual
> extracted text rather than asserted from memory of the project's file layout — **only 3 of the
> claimed 9 pairs are real**; the other 6 (`handlers/prose.py`, `ps/Prose.ps1`, and 4 of the
> `migration/fix_*` names) have **no full-path counterpart anywhere in the 46-escalation text at
> all** — I assumed a duplicate existed because I knew the full path from working on this project,
> without checking whether that full form actually appeared in this specific extracted text. A
> few table rows above (e.g. #784's "25 files" list) also silently show the assumed full path
> rather than the literally-extracted short form for the same reason — the table cells are a
> compressed summary; the underlying `escalation-753-history.md` (unedited) remains the accurate
> source for exact wording. Corrected counts below.

1. **Short-form vs. full-path duplicates — corrected to 3, not 9.** `governance` rule
   `full_path_file_references` (`cfg_escalation` id 7) requires the full repo-relative path.
   Checked programmatically (basename collision across the 102 distinct extracted strings): only
   **3 genuine pairs** exist where both a short and a full form of the same file are separately
   present in the text — `escalation.py` (`lib/escalation.py` in #743/#747/#763/#768/#773/#774/
   #790/#798 vs. `iba/app/lib/escalation.py` in #857/#795/#819/#851/#855/#790), `prosestore.py`
   (`lib/prosestore.py` in #784 vs. `iba/app/lib/prosestore.py` in #799/#795/#836), and
   `fix_from_id_closed_items_20260821.py` (`migration/...` in #6/#750/#754/#755/#759/#744/#745/
   #747/#767 vs. `iba/app/migration/...` in the same file's own registration record). `ps/
   Prose.ps1`, `handlers/prose.py`, and the other 4 `migration/fix_*`/`bootstrap_*` names appear
   **only** in short form anywhere in this text — real duplication was not established for those,
   despite the original claim. Still a live instance of the same rule being weakly followed, just
   a smaller one than first stated.
2. **Four regex artifacts, not real filenames** — `BUILD/GOVERNANCE/CLAUDE.md` (three files named
   together in prose without full paths — really `BUILD.md`, `GOVERNANCE.md`, `CLAUDE.md`),
   `escalation.py/run.py` (two files, `escalation.py` and `run.py`, joined by a colon in source),
   `bible_research.db/iba.db` (the two project databases, joined by a slash in prose, not a path),
   `sec44/BUILD.md` (a section reference, "§44," misread as a directory). Flagged here rather than
   silently corrected or silently dropped — unaffected by the item-1/3 correction.
3. **Total distinct real files — corrected to 99, not 93.** 102 raw distinct extracted strings,
   minus the **3 confirmed** duplicate pairs from item 1 = **99**. The 4 regex-artifact strings
   from item 2 are left as-is in this count (each is one string in the 102, not a real single
   path, but resolving each into its true constituent file(s) — e.g. is "run.py" here
   `iba/app/run.py`? — would require a judgement call this index doesn't make); 99 is the honest,
   directly-computed figure, not a fully resolved one.
