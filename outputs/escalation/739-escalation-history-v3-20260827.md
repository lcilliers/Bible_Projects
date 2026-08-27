# Escalation deep history

## #739 — Programme Prose Realignment (Ch. 4-6)
type=task source=researcher

**v1** (2026-08-21T11:44:23Z, Claude) state=raised next_action=review assigned_to=Claude
> **short description (set this version):** Programme Prose Realignment (Ch. 4-6)
> **comment (set this version):** Read chapters 4-6 (Data architecture / Data integrity & governance / Instruction corpus) plus the root README against live GOVERNANCE.md/CLAUDE.md/the actual DB split; identify what's stale; revise or supersede.

[data corrected 2026-08-20, escalation #759: short_description reshaped to a <=60-char title; prior full text redistributed into context (background) / comment (what needs to be done) / resolution (what was actually done) per the researcher's column-spec correction. No prior escalation_history row altered.]

[title corrected 2026-08-20, escalation #759 round 2: round 1's short_description was a compressed sentence, not a composed title -- researcher: "it looks like you just cut whatever was there previous to 57 chars". Redone as an actual noun-phrase title, matching #753's own style. comment/context/resolution from round 1 are unchanged.]
> **context (set this version):** cfg_prose_chapter status='not_yet_aligned' for these 3 chapters -- content likely predates the 2026-08-15 iba.db/bible_research.db architecture correction. Carried over from escalations_old #725 -- was in-progress, next_action=approve: 'I would not be surprised to find discrepancies between what is set in prose, and what is still lingering and inconsistent in the governance and claude.' Reference: iba/app/reports/gr-prog-001-prose-canonical-authority-plan-20260818.md

**v2** (2026-08-21T12:29:19Z, Researcher) state=re-assigned next_action=review assigned_to=Researcher
> **comment (set this version):** on hold must be scheduled before analysis phase

**v3** (2026-08-21T12:38:56Z, Researcher) state=on-hold next_action=review assigned_to=Researcher
> **comment (set this version):** on hold must be scheduled before analysis phase

**v4** (2026-08-21T15:29:04Z, Claude) state=on-hold next_action=review assigned_to=Researcher
> **comment (set this version):** from_id set to -1 (checked, no discoverable spawn parent -- escalation #767 v3's full audit; sentinel decided by researcher, escalation #773 v2).

**v5** (2026-08-27T04:39:59Z, Researcher) state=re-assigned next_action=review assigned_to=Claude
> **comment (set this version):** 739 and 786 can be done together

**v6** (2026-08-27T05:04:56Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Chapters 4-6 rewritten and applied live (31 prose_section rows superseded); 3 cfg_prose_chapter status-update proposals paused awaiting your approval (see context for run ids).
> **context (set this version):** Companion item: #786 (chapter 4 done together with these). Pending config approvals: RUN-20260827_060344_431-CONFIGMAINT (ch4), RUN-20260827_060402_125-CONFIGMAINT (ch5), RUN-20260827_060406_397-CONFIGMAINT (ch6) -- each pauses a cfg_prose_chapter.status update to 'reviewed'; answer via Escalation.ps1 -Action AnswerRun -RunId <id> -Decision Approve|Reject|Revise|Hold|Noted, then re-run the same Config-Maintenance Propose command to commit.
> **resolution (set this version):** Chapters 4-6 rewritten in full against live facts (not prior-doc precedent): queried cfg_table/cfg_column in iba.db directly to establish which of the old bible_research.db tables (word_registry, verse, mti_terms, wa_term_inventory, wa_verse_records, wa_file_index, wa_rule_registry, wa_addendum_registry, term_fetch_log) are marked inactive/retired vs which iba.db tables are their live replacements, and read GOVERNANCE.md/CHARTER.md/CLAUDE.md for the current cfg_*-governed mechanism. Ch4 (Data architecture, 11 sections): rewritten around the two-database split (iba.db base-data/process-control canonical, bible_research.db prose/findings), the new term/lexical chain (word_strong/strong/span/span_candidate/candidate_seed/lemma_inventory/verse_lexical), the cluster_strong Strong's-direct cluster model replacing OWNER/XREF, the book-by-book debate pipeline (hib/phenomenon/operation/passage, 49 of 18,558 passages debated across 6 books) replacing verse_context, and an honest state of finding (438k rows, ~92% delete_flagged, ~35k live) and Session D (0 runs). Ch5 (governance, 7 sections): rewritten around cfg_* + Config-Maintenance.ps1 -Step Propose as the sanctioned rule-change path, escalation as the project-wide open-item system (resolution_kind decision_required/self_correctable), cfg_on_fail routing, per-database backup/versioning (schema_version + apply_session_patch.py backups for bible_research.db; cfg_meta/run.py snapshots for iba.db), and the four governance.* rules that now enforce doc/config alignment. Ch6 (instruction corpus, 13 sections): retires the Session A-D instruction set as historical (each section states plainly what superseded it and what still has no live equivalent -- e.g. no live registry-management guide, no live per-word publication mechanism), keeps Patches/Directives current (scoped to bible_research.db, PROSE added as an active operation type), and names wa_rule_registry/wa_addendum_registry's retirement. All 31 sections applied live via Prose.ps1 ExportChapter -> edit -> ImportChapter -> apply_session_patch.py (dry-run then live each time), backed up automatically each apply. cfg_prose_chapter.status update to 'reviewed' for all 3 chapters proposed via Config-Maintenance.ps1 -Step Propose -- 3 runs PAUSED awaiting your AnswerRun decision (run ids in context). Not self-approved: a cfg_* write needs your explicit decision per governance, and this is a real content judgement (is the rewrite actually accurate/complete), not a mechanical follow-on.

**v7** (2026-08-27T05:15:22Z, Researcher) state=completed next_action=approved assigned_to=Researcher
> **comment (set this version):** I approve that you have done something.  If the work is not correct, then I will raise another escalation
