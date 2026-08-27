# IBA app — configuration report

> **Generated snapshot of the live config store** (`iba/app/db/iba.db`, tables `cfg_*`). The DB is master — do not hand-edit this file. Change config only via `configmaint.propose` (approval-gated; see GOVERNANCE.md §5A); this report regenerates automatically after an approved change and is overwritten in place.

| field | value |
| --- | --- |
| database | iba |
| config_version | app-0.1.0 |
| generated_at | 2026-08-10T05:44:13Z |
| current_seed_hash | bootstrap:configuration-maintenance-2026-07-21 |

## Contents

- [0. Findings — needing researcher judgement](#0-findings-needing-researcher-judgement)
- [1. Inactive configs — historical record, not a decision](#1-inactive-configs-historical-record-not-a-decision)
- [2. Utilities registry](#2-utilities-registry)
- [3. Connection (STEP)](#3-connection-step)
- [4. Settings — every rule / threshold, grouped by owning module](#4-settings-every-rule-threshold-grouped-by-owning-module)
- [5. STEP apis](#5-step-apis)
- [6. Work packages & steps (the sequence)](#6-work-packages-steps-the-sequence)
- [7. on_fail — condition -> path (the fork rules)](#7-on-fail-condition-path-the-fork-rules)
- [8. Write grants — who may write what](#8-write-grants-who-may-write-what)
- [9. Status flow](#9-status-flow)
- [10. Schema — data tables built from config](#10-schema-data-tables-built-from-config)
- [11. Enums](#11-enums)
- [12. Book order](#12-book-order)
- [13. Change-log — every accepted load (audit)](#13-change-log-every-accepted-load-audit)
- [Reports — full governance per report](#14-reports-full-governance-per-report)

<a id="0-findings-needing-researcher-judgement"></a>
## 0. Findings — needing researcher judgement

_Computed fresh on every regenerate — the full detail behind `configmaint.validate`'s escalation, which references this section by path rather than repeating it. Not errors — advisory. See GOVERNANCE.md §5B._ Items are numbered (running count across every category below) so any one item can be referenced by number, e.g. "item 7" — the numbering is a snapshot of THIS regenerate, not a stable ID across runs. Historical/already-decided records (inactive configs) are §1, not here — everything below is something that actually needs your judgement.

**Orphan configs** (0) — a `cfg_setting`/`cfg_enum` not referenced by any code:
_(none)_

**Settings needing justification** (0) — module already has its own dedicated table:
_(none)_

**Missing report paths** (0) — a quality-check step with nowhere for its findings to persist (governance.reports_must_persist violation):
_(none)_

**Stale filled_by** (0) — cfg_column.filled_by names a now-inactive step:
_(none)_

**Stale governance docs** (1) — GOVERNANCE.md older than the newest applied config change:
1. GOVERNANCE.md was last modified 2026-08-09T09:06:19Z, before the newest applied cfg_change_detail row (2026-08-10T05:44:13Z) — check whether that change needs an entry (GOVERNANCE.md §8's own rule)

**Unregistered lib modules** (0) — iba/app/lib/*.py with no cfg_utility row:
_(none)_

**Low config-density utilities** (0) — NON-EXEMPT cfg_utility module with zero real Cfg-method call sites of its own (see §2 Utilities registry for the full module list, including the 11 already declared config_exempt):
_(none)_

**Orphan book_order** (0) — cfg.book_order() unused, or a duplicate book/ordinal:
_(none)_

**Orphan connection keys** (0) — a cfg_connection key not read via cfg.connection(...) anywhere:
_(none)_

**Orphan candidate rules** (0) — a kind called with zero active rows, or active rows no code asks for:
_(none)_

**Report version clutter** (0) — more than one version of a one-off report simultaneously live in governance.oneoff_report_dir (oneoff_path() found 2026-08-08 to version without archiving, BUILD.md §83) — the rest belong in archive/:
_(none)_

<a id="1-inactive-configs-historical-record-not-a-decision"></a>
## 1. Inactive configs — historical record, not a decision

**Inactive configs** (370 row(s) across 10 table(s)) — deactivated, not deleted; excluded from validation above. 355 from the candidate-system retraction, 2026-07-23 (GOVERNANCE.md §15D; migration/retract_candidate_system.py); 7 from the passage-system retirement, 2026-07-26 (reports/archive/passage-system-retirement-record-20260726.md); **8 UNATTRIBUTED** (not part of a known retirement — needs a look): cfg_step.book-narrative-generate/report.book_narrative_generate, cfg_step.book-narrative-validate/report.book_narrative_validate, cfg_step.chapter-generate/report.verse_span_meaning, cfg_step.verse-analysis-report/report.verse_span_meaning, cfg_work_package.book-narrative-generate, cfg_work_package.book-narrative-validate, cfg_work_package.chapter-generate, cfg_work_package.verse-analysis-report.
- **cfg_setting** (7): `candidate.concept_delimiter_pattern`, `candidate.lemma_base_pattern`, `candidate.load_report_path`, `candidate.quality_report_path`, `candidate.tag_clean_pattern`, `candidate.tag_max_words`, `candidate.transliteration_pattern`
- **cfg_step** (13): `book-narrative-generate/report.book_narrative_generate`, `book-narrative-validate/report.book_narrative_validate`, `candidate-curation/candidate.curate`, `candidate-curation/candidate.load`, `candidate-quality/candidate.validate`, `chapter-generate/report.passage_debate`, `chapter-generate/report.verse_span_meaning`, `passage-debate-report/report.passage_debate`, `passage-debate-sync/passage.debate_sync`, `seed-candidate-report/report.seed_candidate`, `set-candidates/candidate.seed`, `set-candidates/candidate.set`, `verse-analysis-report/report.verse_span_meaning`
- **cfg_work_package** (10): `book-narrative-generate`, `book-narrative-validate`, `candidate-curation`, `candidate-quality`, `chapter-generate`, `passage-debate-report`, `passage-debate-sync`, `seed-candidate-report`, `set-candidates`, `verse-analysis-report`
- **cfg_write_grant** (5): `candidate.curate -> candidate_seed`, `candidate.load -> candidate_seed`, `candidate.seed -> candidate_seed`, `candidate.seed -> lemma_inventory`, `candidate.set -> span_candidate`
- **cfg_report** (3): `candidate.load`, `candidate.validate`, `report.seed_candidate`
- **cfg_report_section** (10): `candidate.load/duplicates`, `candidate.load/exceptions`, `candidate.validate/gloss`, `candidate.validate/orphan_lemmas`, `candidate.validate/seed_tag`, `candidate.validate/span_tag`, `report.seed_candidate/distribution`, `report.seed_candidate/over_time`, `report.seed_candidate/summary`, `report.seed_candidate/top_lemmas`
- **cfg_report_csv_table** (5): `candidate.load/candidate_seed`, `candidate.validate/candidate_seed`, `candidate.validate/lemma_inventory`, `candidate.validate/span_candidate`, `report.seed_candidate/candidate_seed`
- **cfg_enum** (17): `candidate_decision=candidate`, `candidate_decision=exception`, `candidate_decision=rejected`, `candidate_decision=undecided`, `candidate_ib_referent=body_part`, `candidate_ib_referent=characteristic`, `candidate_ib_referent=other_being`, `candidate_source=curated-synonym`, `candidate_source=ib-judgement`, `candidate_source=read-emergent`, `candidate_source=registry-direct`, `candidate_step_status=in_strong`, `candidate_step_status=not_in_step`, `candidate_step_status=step_has_verses_pending`, `candidate_step_status=step_no_verses`, `passage_source=passage-build`, `passage_source=single-verse-emergent`
- **cfg_on_fail** (11): `candidate.curate/change-rejected`, `candidate.curate/invalid-proposal`, `candidate.curate/needs-approval`, `candidate.curate/needs-revision`, `candidate.load/needs-review`, `candidate.seed/no-inventory`, `candidate.set/no-spans`, `candidate.validate/findings-rejected`, `candidate.validate/needs-review`, `candidate.validate/needs-revision`, `passage.build/no-candidates`
- **cfg_candidate_rule** (by kind): accept=289

<a id="2-utilities-registry"></a>
## 2. Utilities registry

**28** registered module(s) — **13** declared `config_exempt` (a legitimate zero for config-setting/enum usage, not a completeness gap), **0** inactive (module removed/merged). See §0 "Low config-density utilities" for any NON-exempt module still flagged.

| module | file | purpose | active | exempt | exempt reason |
| --- | --- | --- | --- | --- | --- |
| cfg | iba/app/lib/cfg.py | cfg.py — the runtime config reader. THE ONLY WAY THE APP READS CONFIG. | ✓ | ✓ | defines .setting()/.enum() itself — the config reader; cannot call its own accessor. |
| cfgcheck | iba/app/lib/cfgcheck.py | cfgcheck.py — the config-maintenance / validation utility for the app config. | ✓ | ✓ | validates the raw seed dict before any Cfg/DB object exists — structurally cannot call .setting()/.enum(). |
| cfgload | iba/app/lib/cfgload.py | cfgload.py — load the JSON SEEDS into the config tables in the DATABASE. | ✓ | ✓ | writes the seed INTO the cfg_* tables (creates + populates them) — same class as migration/ scripts, already excluded from usage-checks for the same reason. |
| cfgquality | iba/app/lib/cfgquality.py | cfgquality.py — shared config-quality checks, used by BOTH handlers/configmaint.py (the | ✓ | ✓ | works directly against a raw sqlite3.Connection (not a Cfg wrapper), by design — usable from both configmaint.py (has a Cfg) and cfgreport.py (doesn't); queries cfg_setting/cfg_enum via raw SQL, not Cfg's convenience methods. Found 2026-07-30 only after fixing this same check's own text-collision false negative for this file — same class of legitimate zero as the other 11, not an oversight. |
| cfgreport | iba/app/lib/cfgreport.py | cfgreport.py — full-visibility config report, generated FROM the config store. | ✓ | ✓ | generates reports by querying cfg_* tables directly; the paths it needs (out_path/db_path) are resolved by its caller (configmaint.report), not read here. |
| db | iba/app/lib/db.py | db.py — the DATA layer. Built FROM the config in the database. | ✓ |  |  |
| dbsnapshot | iba/app/lib/dbsnapshot.py | dbsnapshot.py — pre-write DB snapshots. THE GAP FOUND 2026-07-22: this app had no rollback | ✓ |  |  |
| debateaudit | iba/app/lib/debateaudit.py | debateaudit.py — the shared per-row CRUD audit trail for every debate writer (`hib.set`, | ✓ | ✓ | writes to a fixed table name (debate_change_detail) only -- no cfg.setting()/cfg.enum() usage by design, same shape as other pure DB-write utilities already exempt |
| debaterun | iba/app/lib/debaterun.py | Debate-Run.ps1 readiness checks (mirrors each operations-ingest/build-passages handler own gate) + staging-payload path resolution (passage.debate_staging_path_pattern) | ✓ |  |  |
| escalation | iba/app/lib/escalation.py | escalation.py — util.escalation. The only sanctioned researcher interaction. | ✓ |  |  |
| lexical | iba/app/lib/lexical.py | lexical.py — the the lexical (`verse_lexical`) engine: T1-T3 of the verse-lexical technique | ✓ |  |  |
| lexiconparse | iba/app/lib/lexiconparse.py | lexiconparse.py — the governed parse of the raw lexicon layer (strong_meaning_tree.sense_text, | ✓ |  |  |
| narrativegenerate | iba/app/lib/narrativegenerate.py | report.book_narrative_generate's assembly (debates + governing docs), cost estimate/cap, Anthropic Messages API call, and narrative filing | ✓ |  |  |
| passagedebatereport | iba/app/lib/passagedebatereport.py | passagedebatereport.py — registers the passage-debate method (`WA-passage-read-guidance` + | ✓ |  |  |
| passagetrack | iba/app/lib/passagetrack.py | passagetrack.py — the completion-tracking record for the verse-fanout method (`report. | ✓ | ✓ | receives an already-open cfg/connection from its caller; only checks cfg.may_write(), no settings/enums of its own. |
| registryreport | iba/app/lib/registryreport.py | registryreport.py — evaluate/review the `word_registry`: a summary, its join to `strong` (via | ✓ | ✓ | receives cfg.conn from its caller; no settings/enums of its own. |
| reportkit | iba/app/lib/reportkit.py | reportkit.py — shared report scaffold (title/ToC/sections/footer) + archive-on-write, reading | ✓ |  |  |
| retention | iba/app/lib/retention.py | retention.py — log growth / run-health visibility for the append-only audit tables | ✓ | ✓ | receives cfg.conn from its caller; its own setting (retention.snapshot_keep_count) is read by dbsnapshot.py, not here. |
| schemareport | iba/app/lib/schemareport.py | schemareport.py — the IBA app's own DATA-schema snapshot, one of the four "missing reports" | ✓ | ✓ | receives cfg.conn from its caller; no settings/enums of its own. |
| seedreport | iba/app/lib/seedreport.py | seedreport.py — analysis of `candidate_seed`, one of the four "missing reports" from | ✓ | ✓ | receives cfg.conn from its caller; no settings/enums of its own. |
| spanreport | iba/app/lib/spanreport.py | spanreport.py — analysis of the span layer (`span` + `span_candidate`), one of the four | ✓ | ✓ | receives cfg.conn from its caller; no settings/enums of its own. |
| stepapi | iba/app/lib/stepapi.py | stepapi.py — the three STEP calls. Governed by config, fully. | ✓ |  |  |
| strongreport | iba/app/lib/strongreport.py | strongreport.py — analysis of the meaning-parse layer (`strong` + `strong_lexicon` + | ✓ | ✓ | receives cfg.conn from its caller; no settings/enums of its own. |
| valuequality | iba/app/lib/valuequality.py | valuequality.py — the generic column-level VALUE-QUALITY engine. | ✓ |  |  |
| versespanmeaningreport | iba/app/lib/versespanmeaningreport.py | versespanmeaningreport.py — the governed copy of `tools/build_verse_span_meaning_extract.py`'s | ✓ |  |  |
| wholebookread | iba/app/lib/wholebookread.py | wholebookread.py — registers the whole-book-read step (`report.whole_book_read`) as a real | ✓ |  |  |
| wordregistryspanreport | iba/app/lib/wordregistryspanreport.py | wordregistryspanreport.py — word_registry -> word_strong -> strong -> parse-meaning -> unique | ✓ |  |  |
| words | iba/app/lib/words.py | words.py — registry word normalisation. Config-governed. | ✓ |  |  |

<a id="3-connection-step"></a>
## 3. Connection (STEP)

| key | value |
| --- | --- |
| base_url | http://localhost:8989 |
| timeout_seconds | 30 |
| version | ESV_th |

<a id="4-settings-every-rule-threshold-grouped-by-owning-module"></a>
## 4. Settings — every rule / threshold, grouped by owning module

_Every setting must have a module (enum.config_module) — configmaint.propose enforces this on every new row; see GOVERNANCE.md §5A._
| module | key | value | use |
| --- | --- | --- | --- |
| candidate | candidate.concept_delimiter_pattern | [:/] | a character in a candidate.load input word signalling more than one concept -- split into one sub-item per piece before validating, rather than reject or guess which half is right |
| candidate | candidate.lemma_base_pattern | ^([HG]\d+)([A-Z]?)$ | capture group 1 = the base Strong's (sub-letters stripped) — the lemma key. The seed/stamp key on this. |
| candidate | candidate.load_report_path | iba/app/reports/candidate-load.md | where candidate.load persists its per-run duplicates/exceptions report |
| candidate | candidate.quality_report_path | iba/app/reports/candidate-quality.md | where candidate.validate persists its findings |
| candidate | candidate.tag_clean_pattern | ^[A-Za-z][A-Za-z' -]*$ | a clean candidate_tag: letters/spaces/hyphens/apostrophe only — no parenthetical transliteration, punctuation, or multi-clause gloss text |
| candidate | candidate.tag_max_words | 5 | a candidate.load input word/tag longer than this many space-separated tokens is treated as a sentence, not a concept, and written as an exception row |
| candidate | candidate.transliteration_pattern | ^[a-z]+'[a-z]+$ | STARTER heuristic, tune via configmaint.propose as real cases are seen: a bare lowercase token with no space is a plausible transliteration (e.g. 'asah', 'halak') and gets written as an exception for a human read, not silently accepted -- it cannot distinguish a genuine single-word English gloss ('hearing') from a transliteration by shape alone, so this is a conservative flag-for-review test, not a hard linguistic classifier |
| configmaint | configmaint.auto_report | True | whether an approved configmaint.propose automatically chains to configmaint.report |
| configmaint | configmaint.report_path | iba/app/config/CONFIG-REPORT.md | where configmaint.report writes the snapshot |
| escalation | escalation.list_report_path | iba/app/reports/escalation-list.md |  |
| governance | governance.build_md_on_code_change | any code change under iba/app/** must update iba/app/BUILD.md in the same unit of work — BUILD.md is the build record, not a one-time snapshot | researcher ruling 2026-07-22: BUILD.md/GOVERNANCE.md must stay current, not just be written once |
| governance | governance.governance_md_on_rule_change | any governance/process rule change must be set in cfg_* first (via configmaint.propose), then GOVERNANCE.md updated to reflect it in the same unit of work — GOVERNANCE.md documents the config, it never holds a rule the config does not | researcher ruling 2026-07-22: no rule should exist only in GOVERNANCE.md; the config is the source of truth, GOVERNANCE.md is the overview of it |
| governance | governance.oneoff_report_archive_dir | archive | archive subfolder (relative to governance.oneoff_report_dir) that oneoff_path() moves a superseded one-off report version into before writing the next one -- same shape as write_report/cfg_report.archive_dir, added 2026-08-08 (BUILD.md sec83) once oneoff_path was found to have versioned without ever archiving. |
| governance | governance.oneoff_report_dir | iba/app/reports/ | folder for one-off/investigatory reports — read by lib/reportkit.oneoff_path() |
| governance | governance.oneoff_report_format | md | default file extension for one-off reports |
| governance | governance.oneoff_report_naming_pattern | {topic}-{YYYYMMDD}.{format} | filename pattern for one-off reports ({topic}/{YYYYMMDD}/{format} substituted) — same-day collisions get -v2/-v3/... appended by oneoff_path() itself, per the Bible-study side's docs/file-organisation-rules.md §2.3 convention |
| governance | governance.past_precedent_investigation_signals_missing_config | If executing an already-registered standard instruction (a cfg_work_package/cfg_step routine) requires FIRST INVESTIGATING HOW IT WAS DONE IN THE PAST -- reading BUILD.md/session-log history, diffing prior/archived output files, or otherwise reverse-engineering a missing step from precedent -- rather than being told directly by a live cfg_step/cfg_setting row what to run and what rules apply, that investigation is itself the signal that a required config/mechanism is MISSING, not a puzzle to solve from precedent. STOP the instruction immediately the moment this is recognised -- do not proceed by reconstructing the missing rule from historical output and presenting it as the standard process. The gap must be closed first: the missing step/setting registered in cfg_* and its code built (governance.build_md_on_code_change/governance.governance_md_on_rule_change both apply), config validated clean, and only then may the original instruction be resubmitted. | researcher ruling 2026-07-30: a live session investigated BUILD.md history and archived output files to infer an undocumented passage.debate_status filled transition (report.passage_debate has no registered mechanism for marking a manually-filled scaffold complete) instead of finding that transition in cfg_step/cfg_setting -- doc/output archaeology substituting for a missing config is exactly the inconsistency pattern blamed for this study lacking repeatable results over its 7-month history |
| governance | governance.reports_must_persist | every quality-check or report-producing step must persist its output to a config-defined report path — a terminal print + an escalation row is not sufficient; enforced by lib/cfgquality.find_missing_report_paths, checked in configmaint.validate | the researcher's 2026-07-21 standard: deviations are bugs, not judgement calls — fix, don't ask |
| governance | governance.rules_must_be_config_driven | no operational or process rule may exist only in GOVERNANCE.md, BUILD.md, USER-GUIDE.md, or memory without a backing cfg_* row recording it as data. A doc/memory statement is not a real rule until the code -- or, for AI-facing process rules, init.py at startup -- actually reads it. Found 2026-07-26: the STEP-required rule existed only as a doc/code convention (init.py comments, USER-GUIDE.md prose), with no cfg_setting backing it, and was silently violated as a result. | the researchers 2026-07-26 standard, raised after an unconfigured rule (STEP required) was silently violated |
| governance | governance.scripts_ps_dir | iba/app/ps |  |
| governance | governance.scripts_python_dir | iba/app/tools |  |
| governance | governance.session_log_triggers_commit | completing a session log (any SESSION-LOG-*.md) means the full commit-and-push cycle happens in the same unit of work -- stage the real changes, commit with a proper message, push, confirm clean/pushed. See CLAUDE.md section 12. |  |
| governance | governance.verse_gap_by_design | Researcher ruling 2026-07-29: a verse missing from iba.db's verse table (no `verse` row for that osisId) is BY DESIGN, not a data-integrity error. Verse-existence is gated on prior term discovery (concordance-driven per-Strong's onboarding, iba/app/handlers/raw.py:verses) -- do not escalate, flag, or attempt to backfill a missing verse as a bug. Full extent measured 2026-07-29: 2,049/31,086 verses (6.59%) missing, concentrated in genealogy/list-heavy books (1Chr 44%, Ezra 40%, Neh 31%, Josh 23%, Num 17%); sample read of the missing verses' actual content judged the risk within tolerance for this study (see iba/app/reports/verse-existence-census-20260729.md). Both report.verse_span_meaning (the base extract) and report.passage_debate note each detectable gap inline (report.verse_gap_note) and skip straight to the next available verse -- the missing verses are not pulled into the study. | researcher ruling 2026-07-29, after measuring the full-Bible extent of the term-discovery verse gap (see project_iba_verse_existence_gated_on_term_discovery memory + iba/app/reports/verse-existence-census-20260729.md) |
| lexicon | lexicon.bracket_pairs | {'(': ')', '[': ']', '{': '}'} | open->close bracket pairs classify_row/strip_bracketed treat as nestable — a gloss that is wholly one bracketed aside (e.g. '(obsolete)') classifies as 'not applicable'. |
| lexicon | lexicon.classify_lookup_max_words | 3 | classify_row: a gloss/description with at most this many space-separated words is 'lookup', more is 'description' — same shape as candidate.tag_max_words's word-count threshold. |
| lexicon | lexicon.linebreak_pattern | [\r\n]+ | the only recognised sense-separator in strong_meaning_tree.sense_text/strong_lexicon.lsj/mounce — commas/semicolons/colons are NOT separators (STEP itself displays them as one sense). |
| lexicon | lexicon.lsj_level_tags | ['level1', 'level2', 'level3', 'level4'] | LSJ's own HTML tag names marking an explicit outline-level boundary (<LevelN>). |
| lexicon | lexicon.lsj_sublabel_pattern | ^\d+[a-z]*$ | LSJ sublabels are a bare number + optional letter (e.g. '2', '2a') — combined with the current top-level Roman numeral into 'I.2a'. |
| lexicon | lexicon.lsj_top_level_label_pattern | ^[IVXLCDM]+$ | LSJ top-level sense labels are Roman numerals (I, II, III, ...) — matched to track the current top-level for building compound sublabels like 'I.2'. |
| lexicon | lexicon.non_latin_script_pattern | [Ͱ-Ͽἀ-῿֐-׿] | classify_row: any match forces 'description' regardless of word count — Greek/Hebrew Unicode block ranges STEP's lexicon text uses. |
| lexicon | lexicon.outline_code_pattern | ^(\d+[a-zA-Z0-9]*\))\s*(.*)$ | strong_meaning_tree.sense_text: matches a leading outline code (e.g. '1)', '2a)') when sense_code itself is empty, splitting it from the remaining gloss text. |
| lexicon | lexicon.quality_report_path | iba/app/reports/lexicon-parse.md | where lexicon.validate persists its findings |
| lexicon | lexicon.ref_tag_pattern | <ref=['"]([^'"]*)['"]> | matches STEP's <ref='Act.14.17'>display</ref> markup (a nameless '=value' pseudo-attribute HTMLParser can't parse as a real attribute) so it can be rewritten to a well-formed <ref key="..."> before parsing. |
| method | method.inner_being_narrative_guidance_path | iba/docs/WA-inner-being-narrative-guidance-v1-2026-07-28.md | current version of the inner-being-narrative guidance (the three-channel scope requirement + the required Scope self-check section) — report.book_narrative_validate and any AI writing such a narrative must follow this exact file; bump this setting (not memory) when the guidance revises |
| method | method.interpretation_questions_path | iba/docs/WA-interpretation-questions-v1.4-2026-08-02.md | current version of the Q1-Q10 interrogative + Part B guidance of interpretation — the passage-debate scaffold and any AI applying it must follow this exact file |
| method | method.passage_read_guidance_path | iba/docs/WA-passage-read-guidance-v1.5-2026-08-02.md | current version of the passage read guidance (steps 1-5 + notes, incl. step 2 note (f)) — the passage-debate scaffold and any AI applying it must follow this exact file; bump this setting (not the debates' memory) when the guidance revises |
| narrative | method.narrative_hard_constraints_path | iba/docs/WA-inner-being-narrative-hard-constraints-v1-2026-07-30.md | current version of the book-agnostic hard constraints (nothing invented, open threads stay open, no forced unity, plain language, no self-reference) every generated narrative must follow — bump this setting (not memory) when the doc revises |
| narrative | narrative.generate_max_cost | 3.0 | USD cost cap (from the pre-call ESTIMATE) — over this, report.book_narrative_generate refuses outright (cost-cap-exceeded) rather than pausing for approval; raise it deliberately for a book large enough to need it |
| narrative | narrative.generate_max_output_tokens | 16000 | max_tokens on the Messages API call — the ceiling on how long the generated narrative can be |
| narrative | narrative.generate_model | claude-sonnet-5 | the Anthropic model narrative.generate submits the package to |
| narrative | narrative.output_pattern | WA-{book}-inner-being-narrative.md | filename pattern for the generated narrative, written under report.verse_analysis_output_dir/<book_label>/ — same folder its source debates live in |
| narrative | narrative.rate_input_per_million | 3.0 | USD per million input tokens, at narrative.generate_model's current rate — used for both the pre-call estimate and the real post-call cost; edit if the model default changes to a different price tier |
| narrative | narrative.rate_output_per_million | 15.0 | USD per million output tokens, at narrative.generate_model's current rate |
| narrative | narrative.scope_check_report_path | iba/app/reports/book-narrative-scope-check.md | where report.book_narrative_validate persists its findings |
| narrative | narrative.usage_log_path | iba/app/reports/export/narrative-generate-usage.csv | append-only on-disk ledger of every LIVE call's real tokens/cost — scripts/cost_ledger.py (repo root) only ingests Console CSV exports, not this app's own calls, so this is the audit trail for those |
| notification | notification.header_run_id | run_id       : {run_id} | run-header line — the run's id, for Escalation.ps1 -RunId |
| notification | notification.header_runs_over | runs over    : {runs_over} | run-header line (only book/word-scoped work packages print this) |
| notification | notification.header_step | step         : {step} | run-header line 2 (only scripts with a selectable step print this) |
| notification | notification.header_work_package | work package : {work_package} | run-header line 1 — which work package is running |
| notification | notification.not_initialised | The app is not initialised. Run first:  iba\app\ps\Start-Iba.ps1 | shown by every PS script's readiness guard when the app/DB isn't initialised |
| notification | notification.paused_banner_guided | PAUSED — awaiting your decision. Answer with:   .\Escalation.ps1 -Action AnswerRun -RunId {run_id} -Decision <Approve\|Reject\|Revise> [-Comment ...] then re-run this exact command with -RunId {run_id} to act on the answer. | non-chained single-step work packages' PAUSED banner (candidate-quality, candidate-curation, configuration-maintenance, passage-quality) |
| notification | notification.paused_banner_passthrough | PAUSED — {message} | chained work packages' default PAUSED banner (build-passages, set-candidates) — overridden per work package by cfg_work_package.paused_message when set (e.g. new-word) |
| notification | notification.step_result_line |   {0,-20} {1,-14} {2} | per-step result line format (PowerShell -f) — step/path/message, colour by outcome |
| notification | notification.stopped_banner | STOPPED — {message} | chained work packages' STOPPED banner — uniform across build-passages/set-candidates/new-word |
| passage | passage.debate_run_sequence | [{'work_package': 'operations-ingest', 'step': 'hib.set'}, {'work_package': 'build-passages', 'step': 'passage.build'}, {'work_package': 'operations-ingest', 'step': 'phenomenon.set'}, {'work_package': 'operations-ingest', 'step': 'operation.set'}, {'work_package': 'operations-ingest', 'step': 'closing.set'}] | Ordered step sequence Debate-Run.ps1 walks for one debate scope -- work_package+step pairs against the EXISTING active registrations (no new cfg_step rows; cfg_step.step must be globally unique across work_package). Excludes lexical.build deliberately -- separate, book-scoped, run-ahead-of-time prerequisite. |
| passage | passage.debate_session_chapter_guideline | 3 | Advisory session-scope guideline (not hard-enforced) for report.passage_debate fill-in work: recommended max chapters per Claude Code session before clearing context and starting a fresh one. See iba/app/reports/token-consumption-diagnostic-20260802.md for the incident this responds to (Micah+Hosea, 21 chapters in one unbroken session, ~1.13M tokens moved, exhausted daily+weekly caps). |
| passage | passage.debate_staging_path_pattern | iba/app/staging/operations/{book_lower}-{scope}-{step}.json | Predictable path Debate-Run.ps1 checks for each step payload JSON before pausing. |
| passage | passage.quality_report_path | iba/app/reports/passage-quality.md | where passage.validate persists its findings |
| raw | discovery.follow_related | False | relatedNos is root-family noise (H2519 -> 'to divide', 'Mount Halak'). Not followed. |
| raw | language.greek_prefix | G | a strong starting with this is Greek; else Hebrew |
| raw | meaning.head_marker | :  | a mediumDef starting with this is a SENSE: head + the lemma's tree. Else the code is its own lemma. |
| raw | raw.meaning_tree_clean_pattern | ^(?:[^<]\|<(?!(?i:br\b))[^>]*>)*$ | a clean strong_meaning_tree.sense_text: any text plus complete <ref>...</ref> spans (STEP's own citation markup, tolerated -- BUILD.md notes Greek mediumDef is prose with <ref> tags); any OTHER leftover markup (<br>, <b>, ...) fails -- the same <br> parser bug as strong_sense.head, one level deeper |
| raw | raw.strong_base_pattern | ^([HG]\d+)([A-Z]?)$ | Strongs-code base/sub-letter split - single home for this fact (2026-07-29), replacing three independent copies (handlers/raw.py, lib/versespanmeaningreport.py, and the retired candidate.lemma_base_pattern) |
| registry | registry.duplicate_shared_threshold | 1.0 | fraction of a new words seed strongs an existing word must already hold for registry.create to warn it may be a duplicate/typo (1.0 = must share ALL strongs) |
| registry | registry.strip_ends_pattern | [^A-Za-z] | on entry, strip runs of these from BOTH ends of the word ('[hypocrisy]' -> 'hypocrisy'); internal hyphens/spaces kept. Word matching is case-insensitive. |
| report | report.auto_backfill_before_render | True | report.verse_span_meaning auto-runs raw.backfill_meaning_for() for any span whose strong is not yet registered, for the exact book+range being rendered, before writing the report -- researchers direct 2026-07-26 instruction (do not leave partial-coverage reports as a silent manual follow-up step) |
| report | report.output_dir | iba/app/reports | where report.word writes its output |
| report | report.output_pattern | report-{word}.md | filename pattern for report.word's output ({word} substituted) |
| report | report.passage_debate_naming_pattern | WA-{book}-{range}-debate.md | filename pattern for report.passage_debate ({book}/{range} substituted); stable scheme — reportkit archives the prior version on regenerate, no -vN-/date in the name itself |
| report | report.registry_path | iba/app/reports/registry.md |  |
| report | report.sample_verses | 3 | how many sample verses to show the span layer for |
| report | report.schema_overview_path | iba/app/reports/schema-overview.md | where report.schema_overview persists its output |
| report | report.seed_candidate_path | iba/app/reports/seed-candidate.md | where report.seed_candidate persists its output |
| report | report.show_validation | True | show the validation results (util.validation) for the word |
| report | report.show_verse_text | True | show the verse's plain text above its spans |
| report | report.span_analysis_path | iba/app/reports/span-analysis.md | where report.span_analysis persists its output |
| report | report.span_fields | ['position', 'surface', 'strong_variant', 'morph_code', 'is_particle', 'sense'] | which columns the span table shows |
| report | report.strong_fields | ['stepGloss', 'accentedUnicode', 'stepTransliteration', 'head', 'count', 'verses'] | which columns the L1->L2 strong table shows |
| report | report.strong_meaning_path | iba/app/reports/strong-meaning.md | where report.strong_meaning persists its output |
| report | report.verse_analysis_output_dir | iba/app/verse-analysis | base folder for report.verse_span_meaning, sub-foldered per book at write time |
| report | report.verse_analysis_output_pattern | {book}-{range}-verse-span-meaning.md | filename pattern for report.verse_span_meaning ({book}/{range} substituted) |
| report | report.verse_gap_note | **Verse gap -- by design.** `{ref}` has no verse row in iba.db (no onboarded term's concordance search ever surfaced it -- see governance.verse_gap_by_design). Not an error; continuing with the next available verse. | inline note both report.verse_span_meaning and report.passage_debate insert into their output wherever a verse is structurally known to be missing from iba.db within the rendered range (lib.versespanmeaningreport.detect_verse_gaps) -- {ref} substituted |
| report | report.verse_lexical_output_pattern | {book}-{range}-verse-lexical.md | filename pattern for report.verse_lexical ({book}/{range} substituted) — reuses report.verse_analysis_output_dir for the base folder, same as report.verse_span_meaning did |
| report | report.version_on_regenerate | True | app-wide: when true, reportkit.write_report never overwrites or archives-and-replaces an existing report -- every write gets a fresh, never-reused filename (stem-v{n}-{date}.ext, n = 1 + the highest existing version for that exact stem). Set false to fall back to the old archive-before-overwrite behaviour. Researcher direction 2026-08-05 (debate-analytic-process-digest, B2/Q6): reports must never be overwritten, and this must be one app-wide setting, not a per-step convention. |
| report | report.whole_book_read_naming_pattern | WA-{book}-whole-book-read.md | filename pattern for report.whole_book_read ({book} substituted); stable scheme — reportkit archives the prior version on regenerate, same convention report.passage_debate_naming_pattern already uses |
| report | report.word_registry_span_output_dir | iba/app/verse-analysis/word_registry | base folder for report.word_registry_span output — one file per registry word |
| retention | retention.report_path | iba/app/reports/log-retention.md | where the run/escalation/validation_result log-retention & run-health report is written |
| retention | retention.snapshot_keep_count | 20 | how many pre-run DB snapshots to keep (oldest pruned first) -- lib/dbsnapshot.py, wired into run.py so every NEW run gets a rollback point; built 2026-07-22 after a candidate.load bug corrupted 1029 candidate_seed rows with no fine-grained rollback available |
| step | discovery.particle_pattern | ^[HG]9\d{3}$ | grammar-particle codes; excluded from discovery, flagged on a span |
| step | step.cap | 60 | STEP's hard result cap; > this triggers the forward-walk |
| step | step.expect_gloss_contains | God | STEP preflight known-answer probe |
| step | step.expect_min_verses | 1000 | STEP preflight known-answer probe |
| step | step.probe_strong | H0430 | STEP preflight known-answer probe |
| step | step.required_for_runs | True | STEP is mandatory infra, not optional -- initpys startup preflight and every STEP-dependent tool/handler must refuse rather than degrade when this is true and STEP is down |
| step | step.span_html | <span[^>]*\bmorph='([^']*)'[^>]*\bstrong='([^']*)'[^>]*>([^<]*)</span> | how STEP formats an interlinear span in a verse preview: (morph, strong, surface). The forward-walk and the span parse read it. |
| step | step.walk_end | Rev.22.21 | forward-walk upper bound |
| step | step.walk_max_iter | 400 | forward-walk safety bound |
| step | step.walk_start | Gen.1.1 | forward-walk lower bound |
| table_export | table_export.output_dir | iba/app/reports/export | where table.export writes its CSVs |
| validation | validation.output_dir | iba/app/reports | where validation.word/validation.book write their output |
| validation | validation.show_candidate | True | book report: include the candidate (L4b) section |
| validation | validation.show_delta | True | word report: include the pre/post run-delta section |
| validation | validation.show_expectations | True | word report: include the semantic-expectations section |
| validation | validation.show_health | True | word/book report: include the App & DB health section |
| validation | validation.show_integrity | True | word report: include the config-derived integrity section |
| validation | validation.show_passages | True | book report: include the passages section |
| validation | validation.show_references | True | word report: include the FK-resolvability section |
| validation | validation.show_value_quality | True | word/book report: include the value-quality section (cfg_column.expectation checks, scoped to this word/book) |

<a id="5-step-apis"></a>
## 5. STEP apis

| name | route | input | returns |
| --- | --- | --- | --- |
| call1_meanings | rest/search/masterSearch/version={version}\|meanings={word} | the English word | definitions[] (the seed strongs) + results[] (verses) |
| call2_getInfo | rest/module/getInfo/{version}//{strong}// | a strong | vocabInfos[0] — the detail and the meaning |
| call3_strong | rest/search/masterSearch/strong={strong}\|version={version} | a strong | results[] — verses, each preview a full interlinear |

<a id="6-work-packages-steps-the-sequence"></a>
## 6. Work packages & steps (the sequence)

**book-narrative** — runs over `book` · script `iba/app/ps/Book-Narrative.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.book_narrative_generate | iba.app.handlers.narrative:generate | book | live Anthropic API narrative generation -- same handler as the standalone book-narrative-generate work package (kept active for standalone reruns); ordinal 0 of book-narrative, chained with report.book_narrative_validate which runs automatically against this steps own output path once it completes. |
| 1 | report.book_narrative_validate | iba.app.handlers.narrative:validate | none | structural validation of the just-generated narrative file -- same handler as the standalone book-narrative-validate work package (kept active for standalone reruns); ordinal 1 of book-narrative, receives its -Path from ordinal 0s own output automatically via the scripts custom orchestration. |

**book-narrative-generate** — runs over `book` · script `iba/app/ps/BookNarrative-Generate.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.book_narrative_generate | iba.app.handlers.narrative:generate | book | assembles every filled report.passage_debate output for a book plus the hard-constraints and three-channel guidance docs, submits the package to the Anthropic Messages API (researcher approval required first, pause-continue on the estimated cost), and files the returned narrative under report.verse_analysis_output_dir/<book_label>/ — see lib/narrativegenerate.py |

**book-narrative-validate** — runs over `none` · script `iba/app/ps/BookNarrative-Validate.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.book_narrative_validate | iba.app.handlers.narrative:validate | none | structural presence check on an inner-being narrative file — confirms a '## Scope self-check' section exists and all three required channel labels (non-human<->human, human<->human, physical world<->human) are present with non-empty content; a presence check only, not a judgment of citation quality or content accuracy — see WA-inner-being-narrative-guidance-v1-2026-07-28.md section 4 |

**build-passages** — runs over `book` · script `iba/app/ps/Build-Passages.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | passage.build | iba.app.handlers.passage:build | book | recompute the book's passages from verse_hib (hib-continuity\|maximal); flag >review_over as needs_review. Redefined 2026-08-05 (B4) from the retired candidate-stamp/char-continuity rule -- see debate-analytic-process-digest-20260805.md Step 2. |

**candidate-curation** — runs over `none` · script `iba/app/ps/Candidate-Curate.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | candidate.curate | iba.app.handlers.candidate:curate | none | single-row, approval-gated correction on candidate_seed (tag or decision) -- adding a brand-new candidate lemma is the existing cfg_candidate_rule accept route via configmaint.propose |
| 1 | candidate.load | iba.app.handlers.candidate:load | none | JSON-batch create/update/validate for candidate_seed -- derives lemma/strong_variant from an input English word (no lemma_key in the input), auto-loads items that pass every config-driven check, writes anything that doesn't as an inspectable decision='exception' row, then revalidates the whole existing seed the same way; one escalation total if unresolved exceptions remain |

**candidate-quality** — runs over `none` · script `iba/app/ps/Candidate-Quality.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | candidate.validate | iba.app.handlers.candidate:validate | none | read-only quality check: candidate_tag null/format, lemma_key/strong resolution — one escalation per invocation, standalone (not part of seed/set) |

**chapter-generate** — runs over `book` · script `iba/app/ps/Chapter-Generate.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.verse_span_meaning | iba.app.handlers.reports:verse_span_meaning_report | book | verse:span:meaning base extract -- same handler as the standalone verse-analysis-report work package (kept active for recovery reruns); ordinal 0 of chapter-generate, chained with report.passage_debate as ordinal 1. |
| 1 | report.passage_debate | iba.app.handlers.reports:passage_debate_report | book | passage-debate SCAFFOLD generator -- same handler as the standalone passage-debate-report work package (kept active for recovery reruns); ordinal 1 of chapter-generate. Manual fill-in of the written scaffold happens after this script exits, then PassageDebate-Sync.ps1 (unchanged, separate) is run once -- kept OUT of this chain because re-invoking a chained work package re-runs every ordinal from the top, which would silently overwrite a filled scaffold with a blank one. |

**configuration-maintenance** — runs over `none` · script `iba/app/ps/Config-Maintenance.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | configmaint.validate | iba.app.handlers.configmaint:validate | none | coherence-check the live cfg_* tables — read-only, no approval needed |
| 1 | configmaint.propose | iba.app.handlers.configmaint:propose | none | the only path that may change a cfg_* row — approval-gated (escalation, 3-way) |
| 2 | configmaint.report | iba.app.handlers.configmaint:report | none | regenerate CONFIG-REPORT.md from the live cfg_* tables — read-only |

**lexicon-parse** — runs over `none` · script `iba/app/ps/Lexicon-Parse.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | lexicon.parse | iba.app.handlers.lexicon:parse | none | strong_meaning_tree + strong_lexicon -> strong_meaning_parsed/strong_lsj_parsed/strong_mounce_parsed (corrected 2026-07-25 parse); no network, deterministic, clears and rebuilds |
| 1 | lexicon.related | iba.app.handlers.lexicon:related | none | strong -> strong_related; one live STEP getInfo call per row (relatedNos) |
| 2 | lexicon.validate | iba.app.handlers.lexicon:validate | none | read-only coverage + value-quality check across all 4 tables; persists lexicon.quality_report_path every run; escalates only if findings exist |

**log-retention** — runs over `none` · script `iba/app/ps/Log-Retention.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | retention.report | iba.app.handlers.reports:retention_report | none | run/escalation/validation_result log-retention & run-health report — read-only, no pruning |

**new-word** — runs over `word` · script `iba/app/ps/New-Word.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | registry.exists | iba.app.handlers.registry:exists | word | stop if the word already exists (a refresh run handles that) |
| 1 | registry.create | iba.app.handlers.registry:create | word | create the word, status proposed->approved |
| 2 | raw.discover | iba.app.handlers.raw:discover | word | CALL 1 meanings= -> word_strong (the seed strongs) |
| 3 | raw.detail | iba.app.handlers.raw:detail | word | CALL 2 getInfo per strong -> strong + sense + tree + lexicon (the meaning) |
| 4 | raw.verses | iba.app.handlers.raw:verses | word | CALL 3 per strong -> strong_verse + verse + span (span parsed from preview) |
| 5 | raw.write | iba.app.handlers.raw:write | word | commit; mark raw-complete |
| 6 | raw.validate | iba.app.handlers.raw:validate | word | the parse-check: span vs strong_verse must agree |

**operations-ingest** — runs over `book` · script `iba/app/ps/Operations-Ingest.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | hib.set | iba.app.handlers.operations:hib_set | book | Step 1's HIB register for a whole book -- writes hib/hib_referent_option/verse_hib from a JSON payload (-PayloadPath). Clean re-derivation per book (soft-delete existing, insert fresh), same convention passage.build uses for passage. Fails cleanly (unknown-verse/bad-payload) rather than partially writing. |
| 1 | phenomenon.set | iba.app.handlers.operations:phenomenon_set | book | Step 3's phenomena register for one already-tracked passage (needs -Chapters/-Range), from a JSON payload. Clean re-derivation per passage. Sets passage.phenomena_complete_at itself once the register is complete against verse_hib -- the phase gate operation.set checks. Fails cleanly (no-passage/unresolved-reference/bad-payload). |
| 2 | operation.set | iba.app.handlers.operations:operation_set | book | Step 4-5's operations + parties for the same passage, from a JSON payload. REFUSES (phenomena-incomplete) if passage.phenomena_complete_at is still NULL -- the actual code enforcement of WA-interpretation-questions Part B.12 / the debate digest's Step 3 phase gate. Clean re-derivation per phenomenon set. Fails cleanly on any unresolved reference. |
| 3 | closing.set | iba.app.handlers.operations:closing_set | book | Step 7 (digest) / WA-interpretation-questions-v1.4 Part C sections 4-8 for one already-tracked hib-continuity passage -- writes passage_linkage/passage_insufficiency/passage_emergent_question/passage_validation_note + passage.open_decisions_note from a JSON payload. Refuses (operations-incomplete) until every live phenomenon in the passage has a live operation. Reconciliation-gated per list (BUILD.md ??64 pattern), same as hib.set/phenomenon.set/operation.set. |

**passage-debate-report** — runs over `book` · script `iba/app/ps/PassageDebate-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.passage_debate | iba.app.handlers.reports:passage_debate_report | book | passage-debate scaffold generator — verifies the base verse-span-meaning extract and the current method docs (method.passage_read_guidance_path / method.interpretation_questions_path) exist, resolves output path/naming, and writes a debate-document SKELETON (front-matter, per-verse Observation/Operation/Subject-Source-Target/Interrogative/Decision placeholders, standard closing sections) for the researcher/AI to fill in; does not generate interpretive content itself |

**passage-debate-sync** — runs over `book` · script `iba/app/ps/PassageDebate-Sync.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | passage.debate_sync | iba.app.handlers.passage:debate_sync | book | re-syncs `passage.debate_status` for an already-generated `report.passage_debate` scaffold against its CURRENT on-disk content — read-only against the debate file (does not rewrite or regenerate it), DB-write only to the tracked `passage` row's `debate_status`/`debate_written_at` via the existing `passagetrack.record_debate`; the missing half of the report.passage_debate lifecycle before this (write_scaffold writes, nothing re-checked status after manual fill-in) — GOVERNANCE.md §3B |

**passage-quality** — runs over `none` · script `iba/app/ps/Passage-Quality.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | passage.validate | iba.app.handlers.passage:validate | none | read-only quality check: passage verse_count distribution — one escalation per invocation, standalone (not part of build-passages) |

**raw-backfill** — runs over `book` · script `iba/app/ps/Raw-Backfill.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | raw.backfill_meaning | iba.app.handlers.raw:backfill_meaning | book | for a book (optionally narrowed to one chapter's verse range via -Range C:V-V), find every distinct strong its spans reference that has no `strong` row yet, and pull ONLY the meaning (STEP getInfo -> strong/strong_sense/strong_meaning_tree/strong_lexicon) — not verses. Reuses raw.detail_one() unchanged. Progressive, passage-driven DB coverage growth, not a full-Bible bulk pull. |

**registry-report** — runs over `none` · script `iba/app/ps/Registry-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.registry | iba.app.handlers.reports:registry_report | none | evaluate/review word_registry -- summary, join to strong, sense report grouped by gloss |

**reports** — runs over `none` · script `iba/app/ps/Reports.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.word | iba.app.handlers.reports:word_report | word | the word-raw report (report.py) — content governed by report.* settings |
| 1 | validation.word | iba.app.handlers.reports:validation_word | word | the raw-layer validation report (validation.py) — sections governed by validation.show_* |
| 2 | validation.book | iba.app.handlers.reports:validation_book | book | the base-layer validation report (validation.py) — sections governed by validation.show_* |

**schema-overview-report** — runs over `none` · script `iba/app/ps/SchemaOverview-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.schema_overview | iba.app.handlers.reports:schema_overview_report | none | the IBA app's own data-schema snapshot — every data table, columns, types, PK/FK, indexes, row counts |

**seed-candidate-report** — runs over `none` · script `iba/app/ps/SeedCandidate-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.seed_candidate | iba.app.handlers.reports:seed_candidate_report | none | whole-seed candidate_seed analysis — counts by decision/layer/role, tag/lemma distribution, busiest lemmas, open-vs-resolved over time |

**set-candidates** — runs over `book` · script `iba/app/ps/Set-Candidates.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | candidate.seed | iba.app.handlers.candidate:seed | global | refresh candidate_seed over lemma_inventory (independent net + registry-direct + config); recompute registry_match (the double control) |
| 1 | candidate.set | iba.app.handlers.candidate:set | book | stamp span_candidate on the book's spans whose base-strong is a candidate |

**span-analysis-report** — runs over `none` · script `iba/app/ps/SpanAnalysis-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.span_analysis | iba.app.handlers.reports:span_analysis_report | none | span layer coverage per book, confirmed (span) vs candidate (span_candidate) counts, morph-code distribution |

**strong-meaning-report** — runs over `none` · script `iba/app/ps/StrongMeaning-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.strong_meaning | iba.app.handlers.reports:strong_meaning_report | none | meaning-parse layer coverage — strong/strong_sense/strong_meaning_tree/strong_lexicon gap list, sense-count distribution, lexicon completeness |

**table-export** — runs over `none` · script `iba/app/ps/Export-Tables.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | table.export | iba.app.handlers.reports:table_export | none | CSV dump of every data table, verbatim — excludes cfg_* (configmaint.report already owns that content) |

**verse-analysis-report** — runs over `book` · script `iba/app/ps/VerseSpanMeaning-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.verse_span_meaning | iba.app.handlers.reports:verse_span_meaning_report | book | verse : span : meaning extract for a book/chapter-range — per-span meaning from all three parse tables (meaning_tree/lsj/mounce), live STEP disambiguation for AMBIGUOUS (sibling-shared-base) spans |

**verse-lexical** — runs over `book` · script `iba/app/ps/VerseLexical.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | lexical.build | iba.app.handlers.lexical:build | book | verse : verse_lexical extract — mechanical T1-T3 engine: for every code in a span's (possibly compound) strong_variant, classifies role (content lexical entry vs. grammatical formative), stem/voice-selects the operative sense from strong_meaning_parsed via morph_code (not the whole six-stem/voice paradigm), and flags — never resolves — the sibling/base-fallback ambiguity case versespanmeaningreport.meaning_for_code already detects. Runs independent of T4-T9/passage_debate. Version-aware: soft-deletes the superseded row and inserts fresh on rewrite, same convention every other iba.db table already uses. Replaces report.verse_span_meaning (retired, see BUILD.md). |
| 1 | report.verse_lexical | iba.app.handlers.reports:lexical_report | book | on-demand MD report, generated from verse_lexical (never an independent write) — EV verse text and the resolved lexical reading placed together, per book/passage range. Requires verse_lexical.build to have already run for this exact range. |

**whole-book-read** — runs over `book` · script `iba/app/ps/WholeBookRead-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.whole_book_read | iba.app.handlers.reports:whole_book_read_report | book | whole-book-read gathering report — for a book whose passage debates are (wholly or partly) filled, pulls every debate_status='filled' passage row in reading order, reads each debate file, extracts its Emergent-questions and Passage-level-linkages sections (tolerant heading match, explicit NOT-FOUND if a file's headings don't match), and lays them out per-passage with an empty Resolution slot for the researcher/AI to fill in; does not decide how any emergent question actually resolves itself |

**word-registry-span-report** — runs over `word` · script `iba/app/ps/WordRegistrySpan-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.word_registry_span | iba.app.handlers.reports:word_registry_span_report | word | word_registry : word_strong : strong : strong_meaning_parsed : verse_lexical : span analysis, for one registry word — every linked Strong's with its parse-meaning breakdown and unique surface-span applications (with an example verse) — read-only |

<a id="7-on-fail-condition-path-the-fork-rules"></a>
## 7. on_fail — condition -> path (the fork rules)

**14 of 60 conditions ESCALATE** (pause-continue — the researcher is asked); the rest either stop the run outright (report-stop) or continue with a logged warning (report-continue). Per the researcher's 2026-07-21 rule: any finding that needs a judgement call must be in the first group, not silently in the second or third.

### 5a. Escalates (pause-continue) — the researcher is asked, every time
| step | condition | message |
| --- | --- | --- |
| candidate.curate | needs-approval | a candidate_seed correction needs researcher approval |
| candidate.load | needs-review | candidate.load has unresolved exception row(s) in candidate_seed needing researcher judgement |
| candidate.validate | needs-review | span_candidate has tag/lemma_key quality findings needing researcher judgement |
| configmaint.propose | needs-approval | a config change needs researcher approval |
| configmaint.validate | needs-review | cfg_* has advisory findings (orphans/needs-justification) needing researcher judgement |
| lexicon.validate | needs-review | lexicon-parse coverage/value-quality findings need researcher judgement |
| passage.validate | needs-review | passage verse_count distribution needs researcher judgement |
| raw.detail | no-vocab | a strong returned no vocab from STEP — missing lexical data, worth a decision, not a silent continue |
| raw.discover | zero-strongs | the word maps to no strongs — a researcher question |
| raw.verses | shortfall | STEP returned fewer rows than its own reported total — the exact class of bug BUILD.md §5 found; must not silently continue |
| registry.create | needs-approval | a new word needs researcher approval |
| report.book_narrative_generate | needs-approval | researcher approval required before the live API call is made |
| validation.book | needs-review | validation findings need researcher judgement |
| validation.word | needs-review | validation findings need researcher judgement |

### 5b. Does not escalate — report-stop (hard fail) or report-continue (logged, no ask)
| step | condition | path | message |
| --- | --- | --- | --- |
| candidate.curate | change-rejected | report-stop | researcher rejected the proposed candidate_seed correction |
| candidate.curate | invalid-proposal | report-stop | the proposed correction failed validation -- never escalated |
| candidate.curate | needs-revision | report-stop | researcher asked for revision (see comment) and resubmission |
| candidate.seed | no-inventory | report-stop | lemma_inventory is empty — run the seed migration first |
| candidate.set | no-spans | report-stop | the book has no spans — build its words first |
| candidate.validate | findings-rejected | report-stop | researcher flagged candidate quality findings as needing action |
| candidate.validate | needs-revision | report-stop | researcher asked for more specific investigation (see comment) |
| configmaint.propose | change-rejected | report-stop | the researcher rejected the proposed change |
| configmaint.propose | invalid-proposal | report-stop | the proposed change fails a coherence check — never escalated |
| configmaint.propose | needs-revision | report-stop | the researcher asked for the proposal to be revised (see the comment) and resubmitted |
| configmaint.validate | findings-rejected | report-stop | researcher flagged advisory findings as needing action, not acknowledgement |
| configmaint.validate | invalid | report-stop | the live cfg_* store is incoherent |
| configmaint.validate | needs-revision | report-stop | researcher asked for more specific investigation (see comment) |
| lexical.build | unreachable | report-stop | STEP is down and step.required_for_runs is true — cannot resolve any content-role code's sense without it. |
| lexicon.related | unreachable | report-stop | STEP is not reachable — lexicon.related cannot fetch relatedNos at all |
| lexicon.validate | findings-rejected | report-stop | researcher flagged lexicon-parse quality findings as needing action |
| lexicon.validate | needs-revision | report-stop | researcher asked for more specific investigation (see comment) |
| passage.build | no-candidates | report-stop | the book has no candidate spans — run set-candidates first |
| passage.validate | findings-rejected | report-stop | researcher flagged the passage distribution as needing the rule revisited |
| passage.validate | needs-revision | report-stop | researcher asked for more specific investigation (see comment) |
| raw.backfill_meaning | invalid-range | report-stop | the -Range value could not be parsed |
| raw.backfill_meaning | unreachable | report-stop | STEP is not reachable — cannot pull any meaning |
| raw.discover | follow-related-not-built | report-stop | discovery.follow_related is true but relatedNos expansion was never implemented |
| raw.validate | parse-mismatch | report-stop | span does not recover strong_verse |
| registry.create | word-rejected | report-stop | the researcher rejected the word |
| registry.exists | word-exists | report-stop | the word already exists; use a refresh run, not new-word |
| report.book_narrative_generate | api-error | report-stop | the Messages API returned a non-2xx response |
| report.book_narrative_generate | api-key-missing | report-stop | ANTHROPIC_API_KEY not found in the environment or repo-root .env |
| report.book_narrative_generate | cost-cap-exceeded | report-stop | the pre-call cost estimate exceeds narrative.generate_max_cost |
| report.book_narrative_generate | declined | report-stop | researcher rejected the escalation |
| report.book_narrative_generate | guidance-doc-missing | report-stop | a method.* cfg_setting points to a file that does not exist on disk |
| report.book_narrative_generate | needs-revision | report-stop | researcher asked for a change first (see comment) |
| report.book_narrative_generate | no-debates-found | report-stop | no filled report.passage_debate exists yet for this book |
| report.book_narrative_validate | guidance-doc-missing | report-stop | method.inner_being_narrative_guidance_path points to a file that does not exist on disk — the config is stale relative to iba/docs/ |
| report.book_narrative_validate | narrative-file-missing | report-stop | the given -Path does not exist on disk |
| report.book_narrative_validate | no-path-given | report-stop | -Path is required — the narrative file to check |
| report.book_narrative_validate | scope-check-incomplete | report-stop | one or more required channel labels are missing or left as an unfilled placeholder |
| report.book_narrative_validate | scope-check-missing | report-stop | no '## Scope self-check' section found — add one per the guidance doc section 3 |
| report.verse_lexical | no-readings | report-stop | no verse_lexical rows exist yet for this exact book/range — run lexical.build first (it is ordinal 0 of this same work package, run automatically before this step unless called standalone). |
| report.whole_book_read | no-debates-found | report-stop | no debate_status='filled' passage row exists yet for this book — run at least one report.passage_debate pass and fill it in first |
| report.word | word-not-found | report-stop | the requested word is not in the registry |
| report.word_registry_span | word-not-found | report-stop | the requested word is not in the registry |
| validation.book | findings-rejected | report-stop | researcher flagged the validation findings as needing action, not just acknowledgement |
| validation.book | needs-revision | report-stop | researcher asked for more specific investigation (see comment) |
| validation.word | findings-rejected | report-stop | researcher flagged the validation findings as needing action, not just acknowledgement |
| validation.word | needs-revision | report-stop | researcher asked for more specific investigation (see comment) |

<a id="8-write-grants-who-may-write-what"></a>
## 8. Write grants — who may write what

| writer | tables |
| --- | --- |
| call1_meanings | word_strong |
| call2_getInfo | strong, strong_lexicon, strong_meaning_tree, strong_sense |
| call3_strong | span, strong_verse, verse |
| candidate.curate | candidate_seed |
| candidate.load | candidate_seed |
| candidate.seed | candidate_seed, lemma_inventory |
| candidate.set | span_candidate |
| closing.set | debate_change_detail, passage, passage_emergent_question, passage_insufficiency, passage_linkage, passage_validation_note |
| configmaint.propose | cfg_api, cfg_book_order, cfg_candidate_rule, cfg_change_detail, cfg_change_log, cfg_column, cfg_connection, cfg_enum, cfg_meta, cfg_on_fail, cfg_report, cfg_report_csv_table, cfg_report_section, cfg_setting, cfg_status_flow, cfg_step, cfg_table, cfg_unique, cfg_utility, cfg_work_package, cfg_write_grant |
| escalation | escalation, word_registry |
| hib.set | debate_change_detail, hib, hib_referent_option, verse_hib |
| lexical.build | verse_lexical |
| lexicon.parse | strong_lsj_parsed, strong_meaning_parsed, strong_mounce_parsed |
| lexicon.related | strong_related |
| migration | candidate_seed, lemma_inventory, word_strong |
| operation.set | debate_change_detail, operation, operation_party |
| passage.build | debate_change_detail, passage, verse_passage |
| phenomenon.set | debate_change_detail, passage, phenomenon |
| raw.validate | validation_result |
| raw.write | word_registry |
| registry.create | word_registry |
| report.debate | passage |
| run | escalation, run, validation_result, word_registry |

<a id="9-status-flow"></a>
## 9. Status flow

| entity | order | status | set_by |
| --- | --- | --- | --- |
| word | 0 | proposed | registry (on new word, before approval) |
| word | 1 | approved | registry.create |
| word | 2 | raw-complete | raw.write |
| word | 3 | signed-off | registry.signoff (not in this slice) |
| word | 4 | rejected | escalation (researcher declines) |

<a id="10-schema-data-tables-built-from-config"></a>
## 10. Schema — data tables built from config

### word_registry
_one row per English inner-being word_ — the study's entry point; scope of a new-word run
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| word | TEXT |  | ✓ | ✓ |  | the English word | run.param.Word |
| source | TEXT |  |  |  |  | why it was registered — the growth trigger | run.param.Source |
| status | TEXT |  |  |  |  | registry processing stage | registry+raw+signoff |
| created_at | TEXT |  |  |  |  | when registered | registry.create |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### word_strong
_one row per (word, strong) the STEP word-search returned_ — L1 — the discovery record: which strongs a word maps to. These strongs are the basis for L2. Carries the link only, no strong detail.
dedup key: `word_id, strong`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| word_id | INTEGER |  | ✓ |  | word_registry.id | the word | run.context.word_id |
| strong | TEXT |  | ✓ |  | strong.strongNumber | a strong the word returned | call1.definitions[].strongNumber |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### strong
_one row per strong — unique, global to the study_ — L2 — the strong's identity. The meaning is normalised out (O4): it lives in strong_sense / strong_meaning_tree / strong_lexicon.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| strongNumber | TEXT | ✓ |  |  |  | the resolved Strong's code — the key | call2.vocabInfos[0].strongNumber |
| accentedUnicode | TEXT |  |  |  |  | the actual Hebrew/Greek word | call2.vocabInfos[0].accentedUnicode |
| stepGloss | TEXT |  |  |  |  | short English sense | call2.vocabInfos[0].stepGloss |
| stepTransliteration | TEXT |  |  |  |  | romanised form; never shown without the gloss | call2.vocabInfos[0].stepTransliteration |
| language | TEXT |  |  |  |  | Hebrew/Greek from the code prefix | derived:call2.strongNumber |
| count | INTEGER |  |  |  |  | STEP token frequency — NOT a verse count, may be capped | call2.vocabInfos[0].count |
| freqList | TEXT |  |  |  |  | raw frequency distribution | call2.vocabInfos[0].freqList |
| created_at | TEXT |  |  |  |  | when first fetched | raw.detail |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### strong_sense
_one row per strong — the sense HEAD_ — the span's meaning, read constantly. The head is the first line of mediumDef (the sense); is_own_lemma marks a code that is its own lemma, where the gloss carries the sense.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| strong | TEXT | ✓ |  |  | strong.strongNumber | the strong |  |
| head | TEXT |  |  |  |  | the sense — THE SPAN'S MEANING | derived:call2.mediumDef.head |
| is_own_lemma | INTEGER |  |  |  |  | 1 = no ': ' head; the code is its own lemma and the gloss is the sense | derived:call2.mediumDef |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### strong_meaning_tree
_one row per sense-node of a LEMMA's definition tree_ — the lemma's full range — read rarely, only when the broader context is needed. Keyed on the lemma (shared across its senses, which the prototype proved).
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| lemma_key | TEXT |  | ✓ |  |  | the base code the tree belongs to | derived:call2.strongNumber.base |
| sense_code | TEXT |  |  |  |  | the tree position: 1), 1a), 1b1) | derived:call2.mediumDef.tree |
| sense_text | TEXT |  |  |  |  | the sense line | derived:call2.mediumDef.tree |
| sort | INTEGER |  |  |  |  | order within the tree | derived:call2.mediumDef.tree |
| deleted | INTEGER |  |  |  |  | soft delete |  |
| strong_variant |  |  |  |  | strong.strongNumber |  |  |

### strong_lexicon
_one row per strong that has LSJ/Mounce (Greek)_ — the large lexicon text — separate because rarely scanned
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| strong | TEXT | ✓ |  |  | strong.strongNumber | the strong |  |
| lsj | TEXT |  |  |  |  | LSJ entry (Greek) | call2.vocabInfos[0].lsjDefs |
| mounce | TEXT |  |  |  |  | Mounce short def (Greek) | call2.vocabInfos[0].shortDefMounce |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### verse
_one row per verse — unique. Does NOT belong to a strong._ — L3 — the addressable verse. preview is the full interlinear, kept verbatim so span is re-derivable.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| osisId | TEXT |  | ✓ | ✓ |  | the machine key, e.g. Matt.23.28 | call3.results[].osisId |
| reference | TEXT |  |  |  |  | human reference, e.g. Mat 23:28 | call3.results[].key |
| preview | TEXT |  |  |  |  | the full interlinear HTML — the source of span | call3.results[].preview |
| step_version | TEXT |  |  |  |  | provenance — which STEP module | run.context.step_version |
| created_at | TEXT |  |  |  |  | when first built | raw.verses |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### strong_verse
_one row per (strong, verse) — unique. The m:m index._ — the source's assertion 'this strong is in this verse'. The check side against span (what the parse found).
dedup key: `strong, verse_id`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| strong | TEXT |  | ✓ |  | strong.strongNumber | the strong searched | call3.query.strong |
| verse_id | INTEGER |  | ✓ |  | verse.id | the verse returned | call3.results[].osisId |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### span
_ONE ROW PER HTML <span> TAG of a verse (O3) - a tag's codes are a combined unit as STEP itself presents them_ — L4a - SOURCE, immutable. A parse of verse.preview. position is the running TAG index; (verse, position) is the key. strong_variant/morph_code may hold more than one space-separated code when STEP's own HTML combines them on one tag (corrected 2026-07-25 - see migration/rebuild_span_combined_units.py; the old one-row-per-code model split a combined unit and misattributed surface text).
dedup key: `verse_id, position`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| verse_id | INTEGER |  | ✓ |  | verse.id | the verse | parse:verse.preview |
| position | INTEGER |  | ✓ |  |  | running code index in the verse — the key with verse_id | parse:verse.preview |
| surface | TEXT |  |  |  |  | the English word this code belongs to; repeats across a word's codes | parse:verse.preview |
| strong_variant | TEXT |  |  |  |  | one or more strong codes, space-separated - STEP's HTML <span> tag as-is (e.g. G1722 G0054 for one preposition+noun unit); was wrongly declared as ONE code with an FK to strong.strongNumber, which does not hold for a combined value | parse:verse.preview |
| morph_code | TEXT |  |  |  |  | the grammatical layer — one, aligned with the code | parse:verse.preview |
| is_particle | INTEGER |  |  |  |  | 1 only if EVERY code on the tag is a grammar-particle code (H9xxx/G9xxx) - a tag mixing a real content word with attached particles is not itself a pure particle | derived:strong_variant |
| built_at | TEXT |  |  |  |  | raw time | raw.verses |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### run
_one row per work-package run — the control record_ — what ran, pinned to a config version, and RESUMABLE (O7): state + resume_point persisted so a pause survives the process.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| run_id | TEXT |  | ✓ | ✓ |  | the run identifier | run.start |
| work_package | TEXT |  |  |  |  | which package | run.start |
| params | TEXT |  |  |  |  | JSON of the run params | run.start |
| runs_over | TEXT |  |  |  |  | the scope value, e.g. the word | run.start |
| config_version | TEXT |  |  |  |  | the config that ran — pinned before any work | run.start |
| state | TEXT |  |  |  |  | running \| paused \| done \| failed | run |
| resume_point | TEXT |  |  |  |  | the step to resume at on continue | run |
| started_at | TEXT |  |  |  |  | start | run.start |
| ended_at | TEXT |  |  |  |  | end | run.end |
| outcome | TEXT |  |  |  |  | the final result | run.end |

### validation_result
_one row per check a validate step ran_ — util.validation — the outcome of a check, persisted so it can be inspected and reported. A passed check is a recorded fact, not just an advancing run.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| run_id | TEXT |  | ✓ |  | run.run_id | the run that ran the check |  |
| word | TEXT |  |  |  |  | the word the check was over | validate |
| step | TEXT |  |  |  |  | the step that ran it | validate |
| check_name | TEXT |  |  |  |  | which check | validate |
| result | TEXT |  |  |  |  | pass \| fail | validate |
| detail | TEXT |  |  |  |  | the specifics — counts, what failed | validate |
| ran_at | TEXT |  |  |  |  | when | validate |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### escalation
_one row per researcher interaction — the pause_ — the only sanctioned researcher interaction. A pause, not a fork: the run resumes at resume_point when answered.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| run_id | TEXT |  | ✓ |  | run.run_id | the paused run |  |
| word | TEXT |  |  |  |  | the word this interaction is about — durable across runs | escalation.raise |
| at_step | TEXT |  |  |  |  | where to resume — makes it a pause not a fork | escalation.raise |
| type | TEXT |  |  |  |  | prompted \| interactive | escalation.raise |
| question | TEXT |  |  |  |  | the question | escalation.raise |
| preset | TEXT |  |  |  |  | the context that lets it be answered (JSON) | escalation.raise |
| tried | TEXT |  |  |  |  | what the app attempted before asking | escalation.raise |
| state | TEXT |  |  |  |  | raised \| answered \| resumed | escalation |
| answer | TEXT |  |  |  |  | the researcher's decision | escalation.answer |
| answered_at | TEXT |  |  |  |  | when | escalation.answer |
| raised_at | TEXT |  |  |  |  | when raised | escalation.raise |
| comment | TEXT |  |  |  |  | researcher feedback on a 'revise' answer (or any answer) | escalation.answer_for_run |

### lemma_inventory
_one row per corpus lemma (base Strong's) — the INDEPENDENT substrate the seed net runs over_ — L4b seed substrate; imported from the old study, NOT derived from the registry, so the seed is a real completeness control
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| lemma_key | TEXT |  | ✓ | ✓ |  | base Strong's, sub-letters stripped | import:lemma-inventory |
| gloss | TEXT |  |  |  |  | the lemma's English gloss — the meaning the net matches on | import:lemma-inventory |
| language | TEXT |  |  |  |  | Hebrew/Greek | derived:lemma_key |
| source | TEXT |  |  |  |  | import provenance | migration |
| created_at | TEXT |  |  |  |  | when imported | migration |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### candidate_seed
_one row per assessed lemma — the over-inclusive Axis-A candidate assessment_ — L4b seed decision (potential, not definite); the lexical stage is the real test. registry_match NULL on a candidate = a candidate MISSING registry word (the double control)
dedup key: `lemma_key, strong_variant, sense_seq`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| lemma_key | TEXT |  | ✓ |  | lemma_inventory.lemma_key | the assessed lemma |  |
| decision | TEXT |  |  |  |  | DORMANT - candidate.seed retired 2026-07-23; no active mechanism populates this column |  |
| layer | TEXT |  |  |  |  | DORMANT - candidate.seed retired 2026-07-23; no active mechanism populates this column |  |
| registry_match | TEXT |  |  |  |  | DORMANT - candidate.seed retired 2026-07-23; no active mechanism populates this column |  |
| tag | TEXT |  |  |  |  | DORMANT - candidate.seed retired 2026-07-23; no active mechanism populates this column |  |
| assessed_at | TEXT |  |  |  |  | DORMANT - candidate.seed retired 2026-07-23; no active mechanism populates this column |  |
| deleted | INTEGER |  |  |  |  | soft delete |  |
| strong_variant | TEXT |  | ✓ |  | strong.strongNumber | the specific sub-lettered Strongs variant this row's tag reflects (e.g. H0639G), or the lemma_key itself when the tag applies to the whole base lemma (no sub-strong split decided yet -- the default for existing rows) | candidate.seed / candidate.curate |
| sense_seq | INTEGER |  | ✓ | ✓ |  | DORMANT - candidate.load retired 2026-07-23; no active mechanism populates this column |  |
| step_status | TEXT |  |  |  |  | DORMANT - candidate.load retired 2026-07-23; no active mechanism populates this column |  |
| ib_referent_type | TEXT |  |  |  |  | DORMANT - candidate.load retired 2026-07-23; no active mechanism populates this column |  |

### span_candidate
_one row per CANDIDATE span (existence = candidate) — the L4b stamp over the L4a span_ — over-inclusive candidate stamp; the lexical stage later tests each in context
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| span_id | INTEGER |  | ✓ | ✓ | span.id | the L4a span stamped |  |
| lemma_key | TEXT |  |  |  |  | base Strong's of the span (denormalised for continuity/join) | derived:span.strong_variant |
| candidate_tag | TEXT |  |  |  |  | the IB label from the seed | candidate_seed.tag |
| seed_source | TEXT |  |  |  |  | DORMANT - candidate.set retired 2026-07-23; no active mechanism populates this column |  |
| set_at | TEXT |  |  |  |  | DORMANT - candidate.set retired 2026-07-23; no active mechanism populates this column |  |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### passage
_one row per passage — a reading frame (global, per book)_ — extends a characteristic's context to adjacent verses for assessing movement/process/qualifying spans; NOT a thematic unit
dedup key: `book, start_chapter, start_verse, end_chapter, end_verse`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| feasibility_note | TEXT |  |  |  |  | Step 2's own self-assessment record: why this scope was judged readable as a whole without quality loss (or, if the call was refused, why not -- though a refused call writes no passage row at all, so a live row's feasibility_note is always the 'yes, and here's why' case). | passage.build |
| open_decisions_note | TEXT |  |  |  |  | Part C section 8 -- short free-text summary of open decisions/next steps for this passage. Stays a single field, not its own table (design doc: normally short prose, not a repeating structured list, unlike sections 4-7). |  |
| phenomena_complete_at | TEXT |  |  |  |  | NULL until the debate digest Step 3 phase gate is confirmed complete for the whole passage (every verse_hib pair for this passage has a matching phenomenon row); set only by an explicit control check, never by trust. operation writes are blocked in code while this is NULL (schema built, gate-enforcing writer not yet built -- see b3-b5-operations-schema-design-20260805.md). |  |
| story_summary | TEXT |  |  |  |  | Step 2's high-level story synthesis for this passage's scope, read in light of the identified HIBs -- the researcher's own 2026-08-06 redefinition of what Step 2 actually produces. Written once per passage registration, updated only via reconciliation. | passage.build |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| book | TEXT |  | ✓ |  |  | OSIS book code | derived:verse.osisId |
| anchor_verse_id | INTEGER |  | ✓ |  | verse.id | first verse of the run — the anchor |  |
| start_chapter | INTEGER |  |  |  |  | range start chapter - now populated by the verse-fanout tracking mechanism, not passage.build | report.verse_span_meaning / report.passage_debate (via lib/passagetrack.py) |
| start_verse | INTEGER |  |  |  |  | range start verse - now populated by the verse-fanout tracking mechanism, not passage.build | report.verse_span_meaning / report.passage_debate (via lib/passagetrack.py) |
| end_chapter | INTEGER |  |  |  |  | range end chapter - now populated by the verse-fanout tracking mechanism, not passage.build | report.verse_span_meaning / report.passage_debate (via lib/passagetrack.py) |
| end_verse | INTEGER |  |  |  |  | range end verse - now populated by the verse-fanout tracking mechanism, not passage.build | report.verse_span_meaning / report.passage_debate (via lib/passagetrack.py) |
| ref | TEXT |  |  |  |  | human range - now populated by the verse-fanout tracking mechanism, not passage.build | report.verse_span_meaning / report.passage_debate (via lib/passagetrack.py) |
| verse_count | INTEGER |  |  |  |  | count of verses in the range - now populated by the verse-fanout tracking mechanism, not passage.build | report.verse_span_meaning / report.passage_debate (via lib/passagetrack.py) |
| rule | TEXT |  |  |  |  | char-continuity \| maximal - DORMANT since passage.build retired 2026-07-26; NULL on every live row; no active mechanism populates this column |  |
| source | TEXT |  |  |  |  | passage-build \| single-verse-emergent - DORMANT since passage.build retired 2026-07-26; NULL on every live row; no active mechanism populates this column |  |
| needs_review | INTEGER |  |  |  |  | 1 when verse_count > passage.review_over (passage.build only) - DORMANT since passage.build retired 2026-07-26; NULL on every live row; passage.validate reports the live distribution directly instead |  |
| created_at | TEXT |  |  |  |  | when this passage row was created - now populated by the verse-fanout tracking mechanism, not passage.build | report.verse_span_meaning / report.passage_debate (via lib/passagetrack.py) |
| deleted | INTEGER |  |  |  |  | soft delete |  |
| book_label | TEXT |  |  |  |  | human-facing subfolder name (e.g. 'Daniel') used by the verse-analysis report writers; defaults to `book` if the caller never supplied one | DORMANT -- report.verse_span_meaning retired (superseded by report.verse_lexical / lexical.build, BUILD.md §56-59); not carried into the input-scope passage model (BUILD.md §67) -- no live writer as of 2026-08-06 (confirmed against handlers/passage.py:build directly, researcher-approved dormant per CONFIG-REPORT-v34) |
| verse_span_meaning_path | TEXT |  |  |  |  | path to this range's report.verse_span_meaning output, written by that step on success | DORMANT -- report.verse_span_meaning retired (superseded by report.verse_lexical / lexical.build, BUILD.md §56-59); not carried into the input-scope passage model (BUILD.md §67) -- no live writer as of 2026-08-06 (confirmed against handlers/passage.py:build directly, researcher-approved dormant per CONFIG-REPORT-v34) |
| verse_span_meaning_written_at | TEXT |  |  |  |  | UTC timestamp of the last report.verse_span_meaning write for this range | DORMANT -- report.verse_span_meaning retired (superseded by report.verse_lexical / lexical.build, BUILD.md §56-59); not carried into the input-scope passage model (BUILD.md §67) -- no live writer as of 2026-08-06 (confirmed against handlers/passage.py:build directly, researcher-approved dormant per CONFIG-REPORT-v34) |
| debate_path | TEXT |  |  |  |  | path to this range's report.passage_debate output (scaffold or filled — see debate_status), written by that step on success | report.passage_debate (legacy, passage.rule IS NULL) or report.debate (new-model, passage.rule='input-scope' -- tools/build_debate_report.py) |
| debate_written_at | TEXT |  |  |  |  | UTC timestamp of the last report.passage_debate write for this range | report.passage_debate (legacy, passage.rule IS NULL) or report.debate (new-model, passage.rule='input-scope' -- tools/build_debate_report.py) |
| debate_status | TEXT |  |  |  |  | 'scaffold' (auto-generated, still has unreplaced <!-- fill in --> placeholders) or 'filled' (none remain) — a coarse, mechanically-derived completion signal only; NOT a digestion of the debate's analytical content, which is a separate, not-yet-designed question | report.passage_debate (legacy, passage.rule IS NULL: scaffold\|filled) or report.debate (new-model, passage.rule='input-scope': empty\|in-progress\|complete) -- tools/build_debate_report.py |

### verse_passage
_one row per verse-in-a-passage — passage membership (L4b), keeps the raw verse pristine_ — which passage a verse belongs to; a verse is in at most one passage
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| passage_id | INTEGER |  | ✓ |  | passage.id | the passage |  |
| verse_id | INTEGER |  | ✓ | ✓ | verse.id | the verse (unique — one passage per verse) |  |
| is_anchor | INTEGER |  |  |  |  | 1 on the anchor verse - now populated by the verse-fanout tracking mechanism, not passage.build | report.verse_span_meaning / report.passage_debate (via lib/passagetrack.py) |
| created_at | TEXT |  |  |  |  | when this link was created - now populated by the verse-fanout tracking mechanism, not passage.build | report.verse_span_meaning / report.passage_debate (via lib/passagetrack.py) |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### cfg_change_detail
_one row per configmaint.propose write_ — row-level audit of every cfg_* change actually applied — what cfg_change_log's whole-reload shape could not record
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| run_id | TEXT |  | ✓ |  | run.run_id | the run that made the change | configmaint.propose |
| table_name | TEXT |  | ✓ |  |  | which cfg_* table changed | configmaint.propose |
| op | TEXT |  | ✓ |  |  | insert \| update \| delete | configmaint.propose |
| where_json | TEXT |  |  |  |  | the row's natural key (JSON) | configmaint.propose |
| set_json | TEXT |  |  |  |  | the new values written (JSON) | configmaint.propose |
| before_json | TEXT |  |  |  |  | the row's prior state, for update/delete (JSON, null for insert) | configmaint.propose |
| applied_at | TEXT |  | ✓ |  |  | when the write committed | configmaint.propose |

### strong_meaning_parsed
_one row per gloss segment of a strong_meaning_tree lemma (2026-07-25 corrected parse)_ — L2b — the parsed meaning layer over strong_meaning_tree (raw). Segment-scoped: refs/note belong to the exact <b> span they followed, not pooled across the whole source row (the original extract's bug, fixed before this table existed). Comma/semicolon are NOT sense separators here — only a literal line break splits a gloss further.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| lemma_key | TEXT |  | ✓ |  |  | the base code this parsed sense belongs to (never a sub-entry letter) | derived:strong_meaning_tree.lemma_key |
| sort | INTEGER |  |  |  |  | order within the source sense tree | parsed:strong_meaning_tree.sort |
| sense_code | TEXT |  |  |  |  | the tree position, e.g. 1a1a) — or the sense_code column value verbatim | parsed:strong_meaning_tree.sense_code |
| gloss | TEXT |  |  |  |  | one exploded gloss term, kept whole (no comma/semicolon splitting) | parsed:strong_meaning_tree.sense_text |
| verse_refs | TEXT |  |  |  |  | verse citations scoped to this gloss's own <b> span, semicolon-joined | parsed:strong_meaning_tree.sense_text |
| note | TEXT |  |  |  |  | commentary scoped to this gloss's own segment, not pooled across the row | parsed:strong_meaning_tree.sense_text |
| row_type | TEXT |  |  |  |  | lookup / description / not applicable — lexicon_split_common.classify_row() | derived:gloss |
| deleted | INTEGER |  |  |  |  | soft delete |  |
| strong_variant |  |  |  |  | strong.strongNumber |  |  |

### strong_lsj_parsed
_one row per LSJ sense of a strong_lexicon.lsj entry (2026-07-25 corrected parse)_ — L2b — the parsed classical-Greek lexicon layer over strong_lexicon.lsj (raw). Sense blocks split on LSJ's own <LevelN>/<br> structure; gloss kept whole within a block, not exploded on internal commas.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| strong | TEXT |  | ✓ |  | strong.strongNumber | the full strong code this LSJ sense belongs to | derived:strong_lexicon.strong |
| sense_label | TEXT |  |  |  |  | LSJ sense position, e.g. I / I.2 / II.2.b, or 'headword' | parsed:strong_lexicon.lsj |
| gloss | TEXT |  |  |  |  | the sense's bold-span gloss text, kept whole (no comma splitting); may legitimately be blank when a block carries only dialect/citation notes | parsed:strong_lexicon.lsj |
| note | TEXT |  |  |  |  | dialect/grammar labels, connective prose — everything in the block but the gloss | parsed:strong_lexicon.lsj |
| row_type | TEXT |  |  |  |  | headword for the entry's own headword row(s), lookup for every sense row | derived:sense_label |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### strong_mounce_parsed
_one row per Mounce sense of a strong_lexicon.mounce entry (2026-07-25 corrected parse)_ — L2b — the parsed Greek lexicon layer over strong_lexicon.mounce (raw). Split ONLY on <br> (the source's real line breaks); comma/semicolon within one line are punctuation inside a sense, not sense separators.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| strong | TEXT |  | ✓ |  | strong.strongNumber | the full strong code this Mounce line belongs to | derived:strong_lexicon.strong |
| mounce_parsed | TEXT |  |  |  |  | one <br>-delimited line of Mounce's entry, kept whole (no comma splitting) | parsed:strong_lexicon.mounce |
| row_type | TEXT |  |  |  |  | lookup / description — lexicon_split_common.classify_row() | derived:mounce_parsed |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### strong_related
_one row per (strong, related strong) pair STEP's getInfo returned (fetched 2026-07-25)_ — L2b — NOT derived from any raw table; fetched live from STEP per full strong code (lib.stepapi.Step.call2_getInfo, vocabInfos[0].relatedNos) since no raw table captures this. related_strong is unconstrained — STEP can name a code this app has never onboarded via raw.detail.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| strong | TEXT |  | ✓ |  | strong.strongNumber | the full code of the SOURCE term STEP was asked about | fetched:STEP.getInfo |
| related_strong | TEXT |  | ✓ |  |  | the full code of the RELATED term — may have no strong row of its own yet | fetched:STEP.getInfo.relatedNos.strongNumber |
| related_form | TEXT |  |  |  |  | the related term's native-script form | fetched:STEP.getInfo.relatedNos.matchingForm |
| related_transliteration | TEXT |  |  |  |  | the related term's transliteration | fetched:STEP.getInfo.relatedNos.stepTransliteration |
| related_gloss | TEXT |  |  |  |  | the related term's own short gloss | fetched:STEP.getInfo.relatedNos.gloss |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### verse_lexical
_one row per Strong's code within a span (span_id, code_ordinal) — a compound span yields several rows, one per component code_ — L4b — DERIVED, version-aware. The mechanical T1-T3 reading: role classification + stem/voice-selected sense + named-not-resolved ambiguity, per code. Read by report.verse_lexical and, downstream, by T4-T9 — never by re-deriving from span/strong/strong_meaning_parsed directly.
dedup key: `span_id, code_ordinal`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK | migration/bootstrap_span_reading.py |
| span_id | INTEGER |  | ✓ |  | span.id | which span this reading is for — a span may carry several code_ordinal rows here (one per code in its compound strong_variant) | migration/bootstrap_span_reading.py |
| verse_id | INTEGER |  | ✓ |  | verse.id | denormalized from span, matches verse_passage's own precedent — query without joining through span | migration/bootstrap_span_reading.py |
| code_ordinal | INTEGER |  | ✓ |  |  | position of this code within the span's space-joined strong_variant, 0-based | migration/bootstrap_span_reading.py |
| strong | TEXT |  |  |  | strong.strongNumber | the single code this row resolves — may be NULL only if strong_variant itself is empty (should not occur in practice) | migration/bootstrap_span_reading.py |
| morph_code | TEXT |  |  |  |  | this code's own morph slice (space-split from span.morph_code in the same order) | migration/bootstrap_span_reading.py |
| role | TEXT |  | ✓ |  |  | 'content' (independent lexical item) or 'function' (grammatical formative, e.g. Hebrew H9xxx). Classification metadata only -- does NOT gate resolution (corrected 2026-08-05: H9xxx codes DO carry a real stepGloss/strong_meaning_parsed row, an earlier version wrongly skipped resolving them). | migration/bootstrap_span_reading.py |
| status | TEXT |  | ✓ |  |  | 'resolved' (strong row found, sense pulled -- content or function role alike) or 'unregistered' (no strong row yet -- a genuine coverage gap, regardless of role). | migration/bootstrap_span_reading.py |
| resolved_sense | TEXT |  |  |  |  | stem/voice-selected sense text for 'resolved' rows (content or function role alike); NULL only for 'unregistered' rows -- a real gap, not a hedge. | migration/bootstrap_span_reading.py |
| ambiguity_note | TEXT |  |  |  |  | set only when the sibling/base-fallback ambiguity check fires — live senses named, not resolved (T4's job, not this table's) | migration/bootstrap_span_reading.py |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC | migration/bootstrap_span_reading.py |
| deleted | INTEGER |  | ✓ |  |  | version-aware soft-delete — rewriting a (span_id, code_ordinal) inserts a fresh row and flips the superseded row's deleted to 1, same convention as verse/span/strong | migration/bootstrap_span_reading.py |

### hib
_hib_ — one row per Human Inner Being identified in a scope (debate digest Step 1) -- scope-wide, not passage-scoped: the same HIB recurs across many passages of a book.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| book | TEXT |  | ✓ |  |  | OSIS book code, same convention as verse.osisId's book segment |  |
| label | TEXT |  | ✓ |  |  | e.g. 'Daniel', 'the four youths', 'King Belshazzar' |  |
| kind | TEXT |  | ✓ |  |  | named_individual \| unnamed_individual \| named_collection \| unnamed_collection \| implicit_individual \| implicit_collection -- six types, two orthogonal axes: plurality (individual\|collection) x specificity (named\|unnamed\|implicit). Researcher training pass nahum-1-inner-being-training-20260803.md; debate digest Step 1 (presumptive-candidate / collective / referential rules). |  |
| first_verse_id | INTEGER |  |  |  | verse.id | anchor -- where this HIB was first identified |  |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  |  | version-aware soft-delete, standard convention |  |

### hib_referent_option
_hib_referent_option_ — one row per grammatically-live referent-crux reading (T4), child of hib.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| hib_id | INTEGER |  | ✓ |  | hib.id | the HIB this referent-crux reading belongs to |  |
| reading_text | TEXT |  | ✓ |  |  | one grammatically-live candidate reading (T4) -- e.g. one option for 'we' in Obad 1 |  |
| textual_grounds | TEXT |  |  |  |  | why this reading is live |  |
| adopted | INTEGER |  | ✓ |  |  | exactly one row per hib_id should be 1 -- the explicit choice (T4: 'adopt one explicitly') |  |
| ordinal | INTEGER |  | ✓ |  |  |  |  |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  |  | version-aware soft-delete |  |

### verse_hib
_verse_hib_ — one row per HIB present/a presumptive candidate in a given verse (Step 1's per-verse sweep) -- the input B4's future HIB-continuity passage-boundary rule reads from.
dedup key: `verse_id, hib_id`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| verse_id | INTEGER |  | ✓ |  | verse.id |  |  |
| hib_id | INTEGER |  | ✓ |  | hib.id | this HIB is present/a presumptive candidate in this verse (debate digest Step 1) -- also the table B4's future HIB-continuity passage-boundary rule reads from |  |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  |  | version-aware soft-delete |  |

### phenomenon
_phenomenon_ — the phenomena register (Step 3 output) -- one row per HIB per verse per passage.
dedup key: `passage_id, verse_id, hib_id, ordinal`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| passage_id | INTEGER |  | ✓ |  | passage.id |  |  |
| verse_id | INTEGER |  | ✓ |  | verse.id |  |  |
| hib_id | INTEGER |  | ✓ |  | hib.id |  |  |
| description | TEXT |  | ✓ |  |  | the phenomenon: a state, disposition, or characteristic of this HIB's inner life (debate digest Step 3) |  |
| textual_warrant | TEXT |  |  |  |  | the verb/clause/stated-silence that grounds it (WA-passage-read-guidance step 3b) |  |
| status | TEXT |  | ✓ |  |  | 'stated' \| 'inferred' \| 'silent' -- 'no phenomenon found, silent' is itself a valid row (WA-interpretation-questions Part B.4), never an omitted one |  |
| ordinal | INTEGER |  | ✓ |  |  | allows more than one phenomenon for the same HIB in the same verse (v1.5 step3 note c) |  |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  |  | version-aware soft-delete |  |

### operation
_operation_ — the operation for a registered phenomenon (Step 4-5 output) -- phenomenon_id NOT NULL enforces Part B.12 at the DB level.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| phenomenon_id | INTEGER |  | ✓ |  | phenomenon.id | NOT NULL by design -- the DB-level enforcement of WA-interpretation-questions Part B.12: an operation may only originate from an already-registered phenomenon |  |
| process | TEXT |  |  |  |  | state/status, or a movement (come from/go to/impact on/emerge/go away/become evident) -- v1.4 Q6 |  |
| action_type | TEXT |  |  |  |  | short verb-based label (Q11) -- a label, not a controlled vocabulary (Part B.10) |  |
| decision | TEXT |  |  |  |  | 'retain' \| 'set_aside' \| 'retain_referential' \| 'recorded_silence' |  |
| observation_text | TEXT |  |  |  |  | what the text/span-data states, Strong's codes cited |  |
| description_text | TEXT |  |  |  |  | debate digest Step 5's descriptive write-up |  |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  |  | version-aware soft-delete |  |

### operation_party
_operation_party_ — one row per source/target of an operation (plural-capable, v1.5 step1 note a), child of operation.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| operation_id | INTEGER |  | ✓ |  | operation.id |  |  |
| role | TEXT |  | ✓ |  |  | 'source' \| 'target' |  |
| kind | TEXT |  | ✓ |  |  | 'self' \| 'human' \| 'non_human' \| 'object_situation' \| 'none' |  |
| detail | TEXT |  |  |  |  | which human/object, if named |  |
| enablement_only | INTEGER |  | ✓ |  |  | role='source' rows only -- Part B.5's source-of-state vs source-of-enablement distinction, kept structurally separate rather than folded into kind |  |
| ordinal | INTEGER |  | ✓ |  |  | a phenomenon's operation can have multiple sources/targets (v1.5 step1 note a) |  |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC |  |
| hib_id | INTEGER |  |  |  | hib.id | which registered HIB this source/target party IS, when it is one -- nullable: self/non_human/object_situation/none parties genuinely have no HIB to link. Added 2026-08-07 (Finding 2, debate-schema-traceability-gap-findings-20260807.md): 'detail' alone gave no structural traceability back to the hib register. |  |
| deleted | INTEGER |  | ✓ |  |  | version-aware soft-delete |  |

### passage_linkage
_passage_linkage_ — Part C section 4 (Q7) -- linkages between two specific, already-registered operations in the same passage, and surfaced non-linkages.
dedup key: `passage_id, ordinal`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| passage_id | INTEGER |  | ✓ |  | passage.id |  |  |
| from_operation_id | INTEGER |  | ✓ |  | operation.id | Part C section 4 / Q7 -- a linkage connects two SPECIFIC, already-registered operations in the same passage, never a pattern across a range |  |
| to_operation_id | INTEGER |  | ✓ |  | operation.id |  |  |
| note | TEXT |  | ✓ |  |  | what the linkage is -- also where a Q7 SURFACED ABSENCE gets recorded (row with from=to=the same operation, note explains the absence) rather than passed over silently |  |
| ordinal | INTEGER |  | ✓ |  |  | natural key within passage_id for the reconciliation writer |  |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  |  | version-aware soft-delete |  |

### passage_insufficiency
_passage_insufficiency_ — Part C section 5 (Q9/B.7) -- data the base extract does not carry, named not filled.
dedup key: `passage_id, ordinal`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| passage_id | INTEGER |  | ✓ |  | passage.id |  |  |
| verse_id | INTEGER |  |  |  | verse.id | nullable -- an insufficiency can be passage-wide, not always tied to one verse |  |
| note | TEXT |  | ✓ |  |  | Part C section 5 / Q9 / Part B.7 -- data the base extract does not carry, named not filled from outside knowledge |  |
| ordinal | INTEGER |  | ✓ |  |  | natural key within passage_id for the reconciliation writer |  |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  |  | version-aware soft-delete |  |

### passage_emergent_question
_passage_emergent_question_ — Part C section 6 (Q10/B.9/B.12) -- interpretive forks and genuine literary/structural observations, tracked per passage, never merged across passages.
dedup key: `passage_id, ordinal`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| passage_id | INTEGER |  | ✓ |  | passage.id |  |  |
| verse_id | INTEGER |  |  |  | verse.id | nullable -- an emergent question can span the whole passage |  |
| question_text | TEXT |  | ✓ |  |  | Part C section 6 / Q10 -- interpretive forks (Part B.9) and genuine literary/structural observations (Part B.12, T5) both land here, never in the phenomena register or an operation |  |
| kind | TEXT |  | ✓ |  |  | 'interpretive_fork' \| 'literary_structural' \| 'other' |  |
| ordinal | INTEGER |  | ✓ |  |  | natural key within passage_id for the reconciliation writer |  |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  |  | version-aware soft-delete |  |

### passage_validation_note
_passage_validation_note_ — Part C section 7 (Phase 3) -- the closing re-examination of the passage's own phenomena/operations, corrected before the debate is considered filled.
dedup key: `passage_id, ordinal`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| passage_id | INTEGER |  | ✓ |  | passage.id |  |  |
| phenomenon_id | INTEGER |  |  |  | phenomenon.id | nullable -- a validation finding can be about the passage's debate generally, not always one phenomenon |  |
| finding_text | TEXT |  | ✓ |  |  | Part C section 7 / Phase 3 step 6 -- is this genuinely an inner-being phenomenon, does its Phase 1 justification warrant it, does its Phase 2 operation track faithfully back to it |  |
| corrected | INTEGER |  | ✓ |  |  | WA-passage-read-guidance v1.5 step 6: a failure found here is corrected before the debate is considered filled, not merely logged for later -- this flag records that the correction actually happened, not just that a finding was noted |  |
| ordinal | INTEGER |  | ✓ |  |  | natural key within passage_id for the reconciliation writer |  |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  |  | version-aware soft-delete |  |

### cfg_method_rule
_cfg_method_rule_ — One row per discrete, nameable analytical rule governing a debate-pipeline step -- config, not only prose docs (researcher, 2026-08-06).
dedup key: `step, rule_key`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| step | TEXT |  | ✓ |  |  | which pipeline step this rule governs, e.g. 'hib.set', 'phenomenon.set' |  |
| rule_key | TEXT |  | ✓ |  |  | short slug, unique within a step, e.g. 'presumptive-candidate' |  |
| rule_text | TEXT |  | ✓ |  |  | the rule's own exact wording -- the operational source of truth from here on |  |
| source_doc | TEXT |  |  |  |  | provenance -- which doc/section this was transcribed from |  |
| enforced_by | TEXT |  |  |  |  | code location that mechanically checks this rule, if any -- NULL if it's analyst judgement, not a SQL-checkable condition |  |
| ordinal | INTEGER |  | ✓ |  |  | display order within a step |  |
| active | INTEGER |  | ✓ |  |  | supersede by setting 0 and inserting a new row, rather than editing/deleting -- history kept |  |

### cfg_quality_check
_cfg_quality_check_ — Config-defined reasonability/existence self-check questions per debate-pipeline step (researcher, 2026-08-06). Draft content, not yet wired to any writer's enforcement.
dedup key: `step, check_key`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| step | TEXT |  | ✓ |  |  | which pipeline step this check applies to |  |
| check_key | TEXT |  | ✓ |  |  | short slug, unique within a step |  |
| question | TEXT |  | ✓ |  |  | the actual self-check question a reading pass must ask itself for each candidate item |  |
| test_kind | TEXT |  | ✓ |  |  | 'existence' \| 'non_existence' \| 'reasonableness' (researcher's own three kinds, 2026-08-06) |  |
| required | INTEGER |  | ✓ |  |  | 1 = should eventually block a write until answered; 0 = advisory only. NOT YET ENFORCED for any row by any writer -- see module docstring |  |
| enforced_by | TEXT |  |  |  |  | code location that mechanically checks this, if any |  |
| ordinal | INTEGER |  | ✓ |  |  |  |  |
| active | INTEGER |  | ✓ |  |  | supersede by setting 0 and inserting a new row -- history kept |  |

### cfg_index
_cfg_index_ — Secondary (non-unique) indexes to build per data table -- closes the gap left by build_data_tables() only ever emitting FK/UNIQUE, never plain indexes (schema-remediation-design-20260807.md).
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| table_name | TEXT |  | ✓ |  |  | which data table this index is built on |  |
| name | TEXT |  | ✓ |  |  | index name (unique DB-wide, SQLite requirement) -- convention: idx_{table}_{col} |  |
| col | TEXT |  | ✓ |  |  | one column of this index; multiple rows sharing (table_name, name) form one composite index |  |
| ordinal | INTEGER |  | ✓ |  |  | column order within a composite index |  |

### debate_change_detail
_hib_change_detail_ — one row per hib/hib_referent_option/verse_hib/passage/verse_passage/phenomenon/operation/operation_party/passage_linkage/passage_insufficiency/passage_emergent_question/passage_validation_note row inserted, updated, or soft-deleted by hib.set/passage.build/phenomenon.set/operation.set/closing.set -- the per-run CRUD audit trail shared by every debate writer (researcher direction 2026-08-08).
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| run_id | TEXT |  | ✓ |  | run.run_id | which run made this change -- same fk convention as escalation.run_id/validation_result.run_id |  |
| table_name | TEXT |  | ✓ |  |  | 'hib' \| 'hib_referent_option' \| 'verse_hib' -- which table this row's change touched |  |
| op | TEXT |  | ✓ |  |  | 'insert' \| 'update' \| 'delete' -- free text, matching cfg_change_detail.op's own precedent |  |
| where_json | TEXT |  |  |  |  | identifies the row touched, e.g. {"id": 47} |  |
| set_json | TEXT |  |  |  |  | the new values written (insert/update only) |  |
| before_json | TEXT |  |  |  |  | prior row state (update/delete only), NULL on insert |  |
| applied_at | TEXT |  | ✓ |  |  | ISO-8601 UTC |  |
| writer | TEXT |  | ✓ |  |  | which step made this change -- 'hib.set' \| 'passage.build' \| 'phenomenon.set' \| 'operation.set' \| 'closing.set' | migration/add_debate_change_detail_writer_column_20260808.py |

<a id="11-enums"></a>
## 11. Enums

| enum | values |
| --- | --- |
| candidate_decision | candidate, rejected, undecided, exception |
| candidate_ib_referent | characteristic, other_being, body_part |
| candidate_source | registry-direct, curated-synonym, ib-judgement, read-emergent |
| candidate_step_status | in_strong, step_no_verses, not_in_step, step_has_verses_pending |
| cfg_change_op | insert, update, delete |
| config_module | registry, raw, step, report, candidate, passage, configmaint, validation, governance, retention, notification, table_export, escalation, lexicon, method, narrative |
| escalation_answer | approve, reject, revise |
| escalation_state | raised, answered, paused, retracted |
| escalation_type | prompted, interactive, report-stop, crash |
| hib_kind | named_individual, unnamed_individual, named_collection, unnamed_collection, implicit_individual, implicit_collection |
| narrative_required_channel | Non-human ↔ human, Human ↔ human, Physical world ↔ human |
| on_fail | report-continue, pause-continue, report-stop, self-heal |
| operation_decision | retain, set_aside, retain_referential, recorded_silence |
| passage_debate_status | scaffold, filled, empty, in-progress, complete |
| passage_source | passage-build, single-verse-emergent |
| run_state | running, paused, done, failed |
| step_kind | operations, utility |
| word_status | proposed, approved, raw-complete, signed-off, rejected |
| word_status_built | raw-complete, signed-off |
| writer_identity | run, escalation, migration, call1_meanings, call2_getInfo, call3_strong, report.debate |

<a id="12-book-order"></a>
## 12. Book order

66 books, canonical order — first `Gen`, last `Rev`.

<a id="13-change-log-every-accepted-load-audit"></a>
## 13. Change-log — every accepted load (audit)

| # | loaded_at | config_version | seed_hash | validated |
| --- | --- | --- | --- | --- |
| 1 | 2026-07-18T03:26:55Z | app-0.1.0 | 6d99b2d0554df65e | 1 |
| 2 | 2026-07-18T03:27:45Z | app-0.1.0 | 6d99b2d0554df65e | 1 |
| 3 | 2026-07-18T03:27:46Z | app-0.1.0 | 6d99b2d0554df65e | 1 |
| 4 | 2026-07-18T07:30:27Z | app-0.1.0 | 6fb4416dec799109 | 1 |
| 5 | 2026-07-18T09:28:06Z | app-0.1.0 | 3fb2bd8ae7d47887 | 1 |
| 6 | 2026-07-18T15:36:16Z | app-0.1.0 | 7d5d2ff1c8ba067f | 1 |
| 7 | 2026-07-18T17:41:53Z | app-0.1.0 | 86468beaae09fe28 | 1 |
| 8 | 2026-07-21T14:20:25Z | app-0.1.0 | bootstrap:configuration-maintenance-2026-07-21 | 1 |
| 9 | 2026-07-21T14:20:30Z | app-0.1.0 | bootstrap:configuration-maintenance-2026-07-21 | 1 |
| 10 | 2026-07-21T14:22:11Z | app-0.1.0 | bootstrap:configuration-maintenance-2026-07-21 | 1 |
| 11 | 2026-07-21T14:24:17Z | app-0.1.0 | bootstrap:configuration-maintenance-2026-07-21 | 1 |
| 12 | 2026-07-21T14:25:14Z | app-0.1.0 | bootstrap:configuration-maintenance-2026-07-21 | 1 |

<a id="14-reports-full-governance-per-report"></a>
## 14. Reports — full governance per report

_One block per registered report — everything that governs it, joined from `cfg_report`, `cfg_report_section`, `cfg_report_csv_table`, `cfg_work_package`, and `cfg_on_fail`. The ownership ledger (which config item governs what) is in GOVERNANCE.md._

### `candidate.load`
**candidate.load report** — output `md+csv` · naming `stable` · archived to `archive/` · ToC on
work package `candidate-curation` → `iba/app/ps/Candidate-Curate.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | duplicates | ## Duplicates skipped (not written) | Duplicates skipped (not written) | ✓ |
| 1 | exceptions | ## Exception rows | Exception rows | ✓ |
CSV pairing: `candidate_seed` (this run's decision='exception' rows)

| condition | path | route | message |
| --- | --- | --- | --- |
| needs-review | pause-continue | terminal | candidate.load has unresolved exception row(s) in candidate_seed needing researcher judgement |

### `candidate.validate`
**Candidate quality report** — output `md+csv` · naming `stable` · archived to `archive/` · ToC on
work package `candidate-quality` → `iba/app/ps/Candidate-Quality.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | span_tag | ## span_candidate.candidate_tag (the stamp) | span_candidate.candidate_tag (the stamp) | ✓ |
| 1 | seed_tag | ## candidate_seed.tag (the seed decision — a worklist, not a verdict) | candidate_seed.tag (the seed decision — a worklist, not a verdict) | ✓ |
| 2 | gloss | ## lemma_inventory.gloss (the independent substrate) | lemma_inventory.gloss (the independent substrate) | ✓ |
| 3 | orphan_lemmas | ## Lemmas with no strong entry yet (by frequency) | Lemmas with no strong entry yet (by frequency) | ✓ |
CSV pairing: `candidate_seed`; `lemma_inventory`; `span_candidate`

| condition | path | route | message |
| --- | --- | --- | --- |
| findings-rejected | report-stop | terminal | researcher flagged candidate quality findings as needing action |
| needs-review | pause-continue | terminal | span_candidate has tag/lemma_key quality findings needing researcher judgement |
| needs-revision | report-stop | terminal | researcher asked for more specific investigation (see comment) |

### `configmaint.report`
**IBA app — configuration report** — output `md+csv` · naming `stable` · archived to `archive/` · ToC on
work package `configuration-maintenance` → `iba/app/ps/Config-Maintenance.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | findings | ## 0. Findings — needing researcher judgement | 0. Findings — needing researcher judgement | ✓ |
| 1 | inactive_configs | ## 1. Inactive configs — historical record, not a decision | 1. Inactive configs — historical record, not a decision | ✓ |
| 2 | utilities | ## 2. Utilities registry | 2. Utilities registry | ✓ |
| 3 | connection | ## 3. Connection (STEP) | 3. Connection (STEP) | ✓ |
| 4 | settings | ## 4. Settings — every rule / threshold, grouped by owning module | 4. Settings — every rule / threshold, grouped by owning module | ✓ |
| 5 | apis | ## 5. STEP apis | 5. STEP apis | ✓ |
| 6 | work_packages | ## 6. Work packages & steps (the sequence) | 6. Work packages & steps (the sequence) | ✓ |
| 7 | on_fail | ## 7. on_fail — condition -> path (the fork rules) | 7. on_fail — condition -> path (the fork rules) | ✓ |
| 8 | write_grants | ## 8. Write grants — who may write what | 8. Write grants — who may write what | ✓ |
| 9 | status_flow | ## 9. Status flow | 9. Status flow | ✓ |
| 10 | schema | ## 10. Schema — data tables built from config | 10. Schema — data tables built from config | ✓ |
| 11 | enums | ## 11. Enums | 11. Enums | ✓ |
| 12 | book_order | ## 12. Book order | 12. Book order | ✓ |
| 13 | change_log | ## 13. Change-log — every accepted load (audit) | 13. Change-log — every accepted load (audit) | ✓ |
| 14 | report_governance | ## 14. Reports — full governance per report | Reports — full governance per report | ✓ |
CSV pairing: `cfg_*` (every cfg_* table, one CSV per table — the config store's own verbatim dump)

### `lexicon.validate`
**Lexicon-parse quality report** — output `md+csv` · naming `stable` · archived to `archive/` · ToC on
work package `lexicon-parse` → `iba/app/ps/Lexicon-Parse.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | summary | ## Summary | Summary | ✓ |
| 1 | coverage | ## Coverage — strong_lexicon/strong rows with no parsed/related output | Coverage — strong_lexicon/strong rows with no parsed/related output | ✓ |
| 2 | value_quality | ## Value quality — gloss findings | Value quality — gloss findings | ✓ |
CSV pairing: `strong_lsj_parsed`; `strong_meaning_parsed`; `strong_mounce_parsed`; `strong_related`

| condition | path | route | message |
| --- | --- | --- | --- |
| findings-rejected | report-stop | terminal | researcher flagged lexicon-parse quality findings as needing action |
| needs-review | pause-continue | terminal | lexicon-parse coverage/value-quality findings need researcher judgement |
| needs-revision | report-stop | terminal | researcher asked for more specific investigation (see comment) |

### `passage.validate`
**Passage quality report** — output `md+csv` · naming `stable` · archived to `archive/` · ToC on
work package `passage-quality` → `iba/app/ps/Passage-Quality.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | dist | ## verse_count distribution | verse_count distribution | ✓ |
| 1 | by_book | ## By book | By book | ✓ |
CSV pairing: `passage`; `verse_passage`

| condition | path | route | message |
| --- | --- | --- | --- |
| findings-rejected | report-stop | terminal | researcher flagged the passage distribution as needing the rule revisited |
| needs-review | pause-continue | terminal | passage verse_count distribution needs researcher judgement |
| needs-revision | report-stop | terminal | researcher asked for more specific investigation (see comment) |

### `report.book_narrative_generate`
**{book_label} — Inner-Being Narrative** — output `md` · naming `stable` · archived to `archive/` · ToC off · footer: *Generated by `report.book_narrative_generate` from the book's filled passage debates — see `WA-inner-being-narrative-hard-constraints-v1-2026-07-30.md` and `WA-inner-being-narrative-guidance-v1-2026-07-28.md` for the governing instructions. Run `BookNarrative-Validate.ps1` against this file next.*
work package `book-narrative` → `iba/app/ps/Book-Narrative.ps1` (chained=1)
- on completion: _narrative generated and structurally validated._
- next-step hint: _none -- narrative + validation both complete_
- paused override: _cost/token estimate printed above -- answer the escalation (Approve/Reject/Revise) then re-run this exact command with the same -RunId to make the live API call and continue automatically to validation._

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| _(none)_ | _(none)_ | _(none)_ | _(none)_ | _(none)_ |

| condition | path | route | message |
| --- | --- | --- | --- |
| api-error | report-stop | terminal | the Messages API returned a non-2xx response |
| api-key-missing | report-stop | terminal | ANTHROPIC_API_KEY not found in the environment or repo-root .env |
| cost-cap-exceeded | report-stop | terminal | the pre-call cost estimate exceeds narrative.generate_max_cost |
| declined | report-stop | terminal | researcher rejected the escalation |
| guidance-doc-missing | report-stop | terminal | a method.* cfg_setting points to a file that does not exist on disk |
| needs-approval | pause-continue | terminal | researcher approval required before the live API call is made |
| needs-revision | report-stop | terminal | researcher asked for a change first (see comment) |
| no-debates-found | report-stop | terminal | no filled report.passage_debate exists yet for this book |

### `report.book_narrative_validate`
**Book-Narrative Scope Self-Check — {path}** — output `md` · naming `stable` · archived to `archive/` · ToC on
work package `book-narrative` → `iba/app/ps/Book-Narrative.ps1` (chained=1)
- on completion: _narrative generated and structurally validated._
- next-step hint: _none -- narrative + validation both complete_
- paused override: _cost/token estimate printed above -- answer the escalation (Approve/Reject/Revise) then re-run this exact command with the same -RunId to make the live API call and continue automatically to validation._

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | findings | ## Findings | Findings | ✓ |

| condition | path | route | message |
| --- | --- | --- | --- |
| guidance-doc-missing | report-stop | terminal | method.inner_being_narrative_guidance_path points to a file that does not exist on disk — the config is stale relative to iba/docs/ |
| narrative-file-missing | report-stop | terminal | the given -Path does not exist on disk |
| no-path-given | report-stop | terminal | -Path is required — the narrative file to check |
| scope-check-incomplete | report-stop | terminal | one or more required channel labels are missing or left as an unfilled placeholder |
| scope-check-missing | report-stop | terminal | no '## Scope self-check' section found — add one per the guidance doc section 3 |

### `report.registry`
**Registry evaluation report** — output `md+csv` · naming `stable` · archived to `archive/` · ToC on
work package `registry-report` → `iba/app/ps/Registry-Report.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | summary | ## Summary | Summary | ✓ |
| 1 | by_strong | ## Registry word joined to strong | Registry word joined to strong | ✓ |
| 2 | sense_report | ## Sense report -- registry word by gloss/broad meaning | Sense report by gloss | ✓ |
| 3 | listing | ## Registry listing (all words) | Registry listing (all words) | ✓ |
CSV pairing: `registry` (plain word_registry listing, no join -- one row per registry word regardless of word_strong linkage; CSV mirror of the listing report section (BUILD.md sec89)); `word_registry` (joined to word_strong/strong/strong_sense)

### `report.schema_overview`
**Schema overview** — output `md` · naming `stable` · archived to `archive/` · ToC on
work package `schema-overview-report` → `iba/app/ps/SchemaOverview-Report.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | overview | ## Table inventory | Table inventory | ✓ |
| 1 | tables | ## Every data table, in full | Every data table, in full | ✓ |

### `report.seed_candidate`
**Seed-candidate report** — output `md+csv` · naming `stable` · archived to `archive/` · ToC on
work package `seed-candidate-report` → `iba/app/ps/SeedCandidate-Report.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | summary | ## Summary | Summary | ✓ |
| 1 | distribution | ## Distribution — tag length and rows per lemma | Distribution — tag length and rows per lemma | ✓ |
| 2 | top_lemmas | ## Top lemmas by candidate-row count | Top lemmas by candidate-row count | ✓ |
| 3 | over_time | ## Open vs resolved over time | Open vs resolved over time | ✓ |
CSV pairing: `candidate_seed` (joined to lemma_inventory.gloss)

### `report.span_analysis`
**Span-analysis report** — output `md+csv` · naming `stable` · archived to `archive/` · ToC on
work package `span-analysis-report` → `iba/app/ps/SpanAnalysis-Report.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | by_book | ## Coverage by book | Coverage by book | ✓ |
| 1 | morph_distribution | ## morph_code distribution | morph_code distribution | ✓ |
| 2 | particle_split | ## Particle vs non-particle spans | Particle vs non-particle spans | ✓ |
CSV pairing: `span`; `span_candidate`

### `report.strong_meaning`
**Strong-meaning report** — output `md+csv` · naming `stable` · archived to `archive/` · ToC on
work package `strong-meaning-report` → `iba/app/ps/StrongMeaning-Report.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | gap_list | ## strong rows with no strong_sense yet (by usage count) | strong rows with no strong_sense yet (by usage count) | ✓ |
| 1 | sense_distribution | ## Sense-count distribution (strong_meaning_tree) | Sense-count distribution (strong_meaning_tree) | ✓ |
| 2 | sense_by_registry | ## Sense distribution by registered word (with gloss) | Sense distribution by registered word (with gloss) | ✓ |
| 3 | lexicon_completeness | ## Lexicon completeness (lsj / mounce) | Lexicon completeness (lsj / mounce) | ✓ |
CSV pairing: `strong_meaning_tree` (joined to strong.stepGloss via lemma_key); `strong_sense` (joined to strong.stepGloss)

### `report.verse_lexical`
**{book} {range} — verse : verse_lexical extract** — output `md` · naming `stable` · archived to `archive/` · ToC on
work package `verse-lexical` → `iba/app/ps/VerseLexical.ps1` (chained=1)
- on completion: _lexical built and rendered for '{book}'._

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | coverage | ## Reading coverage (content-role codes, this range) | Reading coverage (content-role codes, this range) | ✓ |
| 1 | verses | ## Verses | Verses | ✓ |

| condition | path | route | message |
| --- | --- | --- | --- |
| no-readings | report-stop | terminal | no verse_lexical rows exist yet for this exact book/range — run lexical.build first (it is ordinal 0 of this same work package, run automatically before this step unless called standalone). |

### `report.whole_book_read`
**{book} -- Whole-Book Read** — output `md` · naming `stable` · archived to `archive/` · ToC on
work package `whole-book-read` → `iba/app/ps/WholeBookRead-Report.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | coverage | ## Coverage | Coverage | ✓ |
| 1 | carried_forward | ## Carried forward per passage | Carried forward per passage | ✓ |
| 2 | not_found | ## Sections not found — verify heading | Sections not found — verify heading | ✓ |
| 3 | closing | ## Closing synthesis | Closing synthesis | ✓ |

| condition | path | route | message |
| --- | --- | --- | --- |
| no-debates-found | report-stop | terminal | no debate_status='filled' passage row exists yet for this book — run at least one report.passage_debate pass and fill it in first |

### `report.word`
**Raw layer — `{word}`** — output `md+csv` · naming `dated` · archived to `archive/` · ToC on
work package `reports` → `iba/app/ps/Reports.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | validation | ## Validation | Validation | ✓ |
| 1 | strongs | ## The strongs and their meaning (L1 → L2) | The strongs and their meaning (L1 → L2) | ✓ |
| 2 | sample_verses | ## Sample verses — the span layer (one row per code) | Sample verses — the span layer (one row per code) | ✓ |
CSV pairing: `span` (word-scoped); `word_strong` (word-scoped)

| condition | path | route | message |
| --- | --- | --- | --- |
| word-not-found | report-stop | terminal | the requested word is not in the registry |

### `report.word_registry_span`
**{word} — linked Strong's, parse meaning, span analysis** — output `md` · naming `dated` · archived to `archive/` · ToC on
work package `word-registry-span-report` → `iba/app/ps/WordRegistrySpan-Report.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | overview | ## Overview | Overview | ✓ |
| 1 | strongs | ## Linked Strong's — parse meaning & span analysis | Linked Strong's — parse meaning & span analysis | ✓ |

| condition | path | route | message |
| --- | --- | --- | --- |
| word-not-found | report-stop | terminal | the requested word is not in the registry |

### `retention.report`
**Log retention & run-health report** — output `md+csv` · naming `stable` · archived to `archive/` · ToC on
work package `log-retention` → `iba/app/ps/Log-Retention.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | summary | ## Summary | Summary | ✓ |
| 1 | stuck_chained | ## Stuck chained runs (archival candidates — not relabelled; see lib/retention.py) | Stuck chained runs (archival candidates — not relabelled; see lib/retention.py) | ✓ |
| 2 | open_escalations | ## Open escalations (oldest first) | Open escalations (oldest first) | ✓ |
| 3 | recent_failed | ## Recent failed runs (last 50) | Recent failed runs (last 50) | ✓ |
| 4 | stuck_nonchained | ## Stuck non-chained runs (unambiguous crash signal -- safe to re-submit; see lib/retention.py) | Stuck non-chained runs (unambiguous crash signal -- safe to re-submit; see lib/retention.py) | ✓ |
CSV pairing: `escalation`; `run`; `validation_result`

### `validation.book`
**Base validation report — book '{book}'** — output `md+csv` · naming `dated` · archived to `archive/` · ToC on
work package `reports` → `iba/app/ps/Reports.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | app_db | ## 1. App & DB | 1. App & DB | ✓ |
| 1 | candidate | ## 3. Candidate (L4b) | 3. Candidate (L4b) | ✓ |
| 2 | passages | ## 4. Passages | 4. Passages | ✓ |
| 3 | value_quality | ## 6. Value quality | 6. Value quality | ✓ |
CSV pairing: `candidate_seed` (book-scoped); `passage` (book-scoped); `verse_passage` (book-scoped)

| condition | path | route | message |
| --- | --- | --- | --- |
| findings-rejected | report-stop | terminal | researcher flagged the validation findings as needing action, not just acknowledgement |
| needs-review | pause-continue | terminal | validation findings need researcher judgement |
| needs-revision | report-stop | terminal | researcher asked for more specific investigation (see comment) |

### `validation.word`
**Validation report — '{word}'** — output `md+csv` · naming `dated` · archived to `archive/` · ToC on
work package `reports` → `iba/app/ps/Reports.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | app_db | ## 1. App & DB | 1. App & DB | ✓ |
| 1 | pre_post | ## 2. Pre/post | 2. Pre/post | ✓ |
| 2 | integrity | ## 3. Integrity | 3. Integrity | ✓ |
| 3 | references | ## 4. References | 4. References | ✓ |
| 4 | expectations | ## 5. Expectations | 5. Expectations | ✓ |
| 5 | value_quality | ## 6. Value quality | 6. Value quality | ✓ |
CSV pairing: `span` (word-scoped, same slice report.word checks); `word_strong` (word-scoped)

| condition | path | route | message |
| --- | --- | --- | --- |
| findings-rejected | report-stop | terminal | researcher flagged the validation findings as needing action, not just acknowledgement |
| needs-review | pause-continue | terminal | validation findings need researcher judgement |
| needs-revision | report-stop | terminal | researcher asked for more specific investigation (see comment) |
