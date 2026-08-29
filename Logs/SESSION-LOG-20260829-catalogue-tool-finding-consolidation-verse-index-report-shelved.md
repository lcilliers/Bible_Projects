# Session Log — 2026-08-29

**Scope, one line:** built the catalogue-tool foundation (#1007) — identified and consolidated the
observation-question catalogue and its findings tables, connected legacy findings to `iba.db`'s
own verse/term data for the first time, found and fixed two real bugs along the way (one in the
new migration, one in shared config/escalation infrastructure) — then, on prototyping the actual
report, concluded with the researcher that the legacy findings are incidental (not leading) value
for inner-being analysis and shelved the report direction; the underlying data-connection work
stands regardless (#1005, bundled and closed out this session).

## Escalations touched

**Closed/completed:**
- **#1009** — `table_export.output_dir` split per-database (JSON map, `iba`/`bible_research`).
- **#1012/#1013/#1014** — 3 new `governance.*` settings backing the PS-worksheet-sync rule.
- **#1018** — `wa_flag_type_question_link` marked inactive (dead: orphaned flag types, all-redundant questions).
- **#1019/#1020/#1021** — `wa_session_b_findings` inactive; `wa_finding_catalogue_links.session_b_note` inactive; `wa_prose_section_citations.cited_qa_link_id` inactive.
- **#1023** — new filing rule: escalation-tied reports get an id prefix + preamble mention, going forward only.
- **#1024–#1037** (14, batched) — `cluster_finding`/`wa_finding_catalogue_links` marked inactive; 11 new columns registered in `cfg_column`; migration script registered in `cfg_utility`.
- **#1043** — second migration script registered in `cfg_utility`.
- **#1044** — new `cfg_behaviour_rule`: inactive tables/columns are never live inputs to reports/analysis (one-time migration reads exempted). Also saved to Claude's persistent memory per direct instruction.
- **#1005** — bundled and closed out this session (see below) — full narrative in its own resolution.
- **#1010, #1040, #1045, #1046, #1047, #1048, #1049, #1050, #1051** — nine self-correctable CLI-sequencing/code mistakes, found and fixed within the same turn each time, no researcher decision needed. Two were genuine code bugs I introduced and fixed: **#1051** (Pass 1's verse-link resolution — see below) and the `escalation.open_duplicate()` fix (folded into #1008/#1038's withdrawal, no separate self-correctable number since it surfaced via a researcher question, not a crash).
- **#1008, #1011, #1015, #1016, #1038, #1039** — withdrawn as stale/superseded snapshots of the same recurring "cfg_* coherent" notice, once the underlying `open_duplicate()` bug (see below) was fixed and dedup started working correctly.

**Still open, awaiting researcher decision (not closed here):**
- **#1006** — Cluster analysis framework / the windows debate, seeded from #1005's prior closing synthesis. Not started this session.
- **#1007** — catalogue-tool foundation, `ready_for_approval` (resolution covers the full body of work below).
- **#1017** — dispatcher-tied vs. manual escalation actions, answered in full (`outputs/escalation/1017-dispatcher-tied-vs-manual-explainer-20260829.md`), `review`.
- **#1022** — citations mechanism (`finding_citation` never cites the live `finding` table), untouched this session beyond being raised.
- **#1041** — verse-lexical definition, `ready_for_approval` (the join-into-`iba.verse_lexical` decision captured; component-display question folded into the now-shelved report work).
- **#1042** — current, accurate "cfg_* coherent" advisory notice (3 pre-existing tracked findings), `review`.

## What was built (full technical detail: `iba/app/BUILD.md` §200–§207, `iba/app/GOVERNANCE.md` §64)

1. **§200/#1007** — `table.export` extended with `-Database`, so it can dump `bible_research.db`
   tables, not just `iba.db`'s own. First deliverable: the 5 catalogue tables identified and
   CSV-extracted for review.
2. **§201/#1009** — `table_export.output_dir` split into a per-database JSON map after the first
   cross-database run landed in an undifferentiated folder; caught and corrected a filing mistake
   of my own along the way (a CSV briefly misfiled to `iba/docs/`, moved to the governed location).
3. **§202/#1012-1014** — a new `configmaint.validate` check (`find_ps_worksheet_drift`/
   `find_escalation_worksheet_drift`) enforcing the researcher's rule that PS-script parameter
   changes must show up in the two Excel tool worksheets. First live run found 28+1 false
   positives from two bugs in the check itself (a PowerShell `$true` literal mis-parsed as a param
   name; a case-sensitivity mismatch) — fixed, then found and fixed the one genuine drift
   (`Export-Tables.ps1` missing `-Database` on its own tab).
4. **§203** — `cluster_finding` + `wa_finding_catalogue_links` folded into `finding`/
   `finding_question_link` — a single findings table and a single catalogue-link table where there
   were four, with structural links (`characteristic_id`, `cluster_subgroup_id`, `vcg_scope`)
   retained as new columns per instruction, not dropped.
5. **§204** — a real, structural bug in `escalation.open_duplicate()` found while investigating why
   7 near-identical advisory notices piled up in one session: it matched against a field
   (`short_description`) that structurally could never contain what it was searching for, and only
   checked one state (`raised`), missing the researcher's own documented workaround. Fixed both;
   verified live.
6. **§205/§207** — `finding_verse_index` (M:N, direct to `iba.verse.id`) and `finding.strong_number`
   built via a 3-pass migration, replacing `finding.verse_context_id`/`mti_term_id`'s dependence on
   two already-inactive legacy tables. **A real bug in this same migration** was found the next
   session-turn, prompted by the researcher's own diagnostic question ("does the old system's own
   chain resolve correctly") — `wa_verse_records.verse_id`, the bridge column the structural pass
   relied on, was wrong for every single one of 434,427 rows (only 5.5% of its populated values
   even point to the correct book). Traced by hand to the exact broken column, fixed by resolving
   via `wa_verse_records.reference` text instead (the same mechanism already verified for the
   migration's other two passes), and re-verified at scale.
7. **§206** — the live, governed `iba.verse_lexical`/`report.verse_lexical` mechanism identified and
   distinguished from the older, unrelated, already-inactive `bible_research.ve_lexical` — a real
   usability gap fixed along the way (`VerseLexical.ps1 -Step`, letting a built range be viewed
   without re-running the build).
8. **`.gitignore`** — added an exclusion for the new per-database `Workflow/schema/{bible_research,
   iba}/` table-export CSVs before this session's commit; `finding.csv` alone is ~98MB, close
   enough to GitHub's 100MB hard limit to have already blocked a push once on this project
   (2026-07-13).
9. **Report design and prototyping (#1007 continuation)** — a filter/layout design was drafted
   (verse/cluster/strong/question, compoundable), then two real-data prototypes built (Gen 1:2, Dan
   10:12) specifically so the researcher could react to actual density rather than a description of
   it. Building them surfaced the §207 bug directly, and eventually the researcher's own
   conclusion: the report was organised around the wrong axis entirely (book/verse reading order,
   when the study's actual object is the inner being read *through* verses, not a book-reading
   aid), and separately, that the bulk of the underlying findings (`l2_api`/`l2_mechanical`,
   332,175 rows, confirmed 100% linked to just 28 catalogue questions) are mechanical restatements
   of what `iba.verse_lexical` now provides more precisely — incidental value, not leading value.
   **Decision: the report is not being taken further; no further normalising/fixing of the legacy
   findings will be attempted standalone — revisit during the analysis phase, in context.**

## Decisions

**Researcher's own:**
- The verse lexical for any future report = `iba.verse_lexical` via `report.verse_lexical`,
  never re-derived (#1041).
- `cluster_finding`/`wa_finding_catalogue_links` fold into `finding`/`finding_question_link`, with
  historic groupings retained as columns, source tables marked inactive not dropped (#1005
  continuation).
- Inactive tables/columns are never live inputs to reports/analysis, one-time migration reads
  excepted — now `cfg_behaviour_rule` and Claude's own persistent memory (#1044).
- Any change to a PS script's parameters must show up in the two Excel worksheets going forward
  (#1012-1014).
- Escalation-tied one-off reports get an id-prefixed filename + preamble mention, going forward
  only (#1023).
- **The report built on legacy findings is shelved; the findings themselves are not to be
  normalised/fixed standalone — this session's closing decision (#1005).**

**Self-correctable, found and fixed directly, no researcher decision needed:** the `open_duplicate()`
bug (§204), the Pass-1 verse-link bug (§207/#1051), and 9 CLI-sequencing mistakes (#1010, #1040,
#1045-1050 minus the two already counted) — all logged, fixed, and resolved in the same unit of
work each time.

## Open items carried into the next session

- **#1006** — the windows/T0-T7 catalogue-question debate — not started, the real next-step thread.
- **#1007, #1041** — `ready_for_approval`, awaiting the researcher's own sign-off.
- **#1017** — answered, awaiting the researcher's read and any follow-up on the worksheet's
  "Despatcher-tied"/"Correction" stub sections.
- **#1022** — citations mechanism, untouched.
- **#1042** — the current advisory-findings notice (3 pre-existing tracked items), awaiting
  acknowledgement.
- **Standing, low-priority:** the ps-tools-worksheet's `-BookLabel` hint should get the same
  correction as the docstring (§ this session, VerseLexical.ps1) — deferred until the file is
  confirmed closed, per the standing rule about editing it while open in Excel.

## Files created or changed (selected — full list in the commit diff)

- `scripts/_apply_finding_catalogue_consolidation_v1_20260829.py`,
  `scripts/_apply_finding_verse_term_index_v1_20260829.py` (new, one-off migrations, both registered
  in `cfg_utility`, `inactive=1`).
- `iba/app/lib/escalation.py` (`open_duplicate()` fix), `iba/app/lib/cfgquality.py` (2 new drift
  checks + PS-automatic-var/case-insensitivity fixes), `iba/app/handlers/configmaint.py`,
  `iba/app/lib/cfgreport.py` (both wired/mirrored), `iba/app/handlers/reports.py`,
  `iba/app/tools/export_tables_csv.py`, `iba/app/ps/Export-Tables.ps1` (`-Database`),
  `iba/app/ps/VerseLexical.ps1` (`-Step`, corrected docstring example).
- `iba/app/BUILD.md` (§200–§207), `iba/app/GOVERNANCE.md` (§64).
- `iba/docs/ps tools worksheet.xlsx` (Export-Tables, VerseLexical tabs corrected).
- `.gitignore` (new exclusion for per-database table-export CSVs).
- `.claude/commands/open-excel-tools.md` (new slash command).
- `C:\Users\lerouxc\.claude\projects\...\memory\feedback_inactive_tables_never_active_inputs.md`,
  `feedback_warn_before_editing_excel_tool_interface.md` (new persistent-memory files).
- `outputs/finding-tables-landscape-review-20260829.md`,
  `outputs/cluster-finding-to-finding-migration-plan-20260829.md`,
  `outputs/flag-type-question-catalogue-review-20260829.md`,
  `outputs/escalation/1007-*.md` (5 files — analysis, plan, two prototypes, standard-report design),
  `outputs/escalation/1017-dispatcher-tied-vs-manual-explainer-20260829.md`.

## Git state

<!-- filled in after commit+push, per governance.session_log_required_content -->
