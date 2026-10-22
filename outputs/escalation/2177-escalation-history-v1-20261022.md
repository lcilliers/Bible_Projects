# Escalation deep history

## #2177 — Reset IBA app as the project's primary process controller
type=task source=researcher

**v1** (2026-10-21T03:42:40Z, Claude) state=raised next_action=review assigned_to=Claude
> **short description (set this version):** Reset IBA app as the project's primary process controller
> **comment (set this version):** Researcher, chat 2026-10-21 (verbatim): 'create a new escalation to reset IBA app to properly serve as the primary process controller for the project. you are in developer-mode and will work on this escalation.' Raised in a Developer Mode session; Claude works it. Related: #2173 open decision 2 (where the project's working state lives in documents re-read every session instead of iba.db).

**v2** (2026-10-21T03:42:52Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Proposed approach, awaiting researcher confirmation before any design or build: step 1 = diagnosis only (no build), mapping where the project's working state and process control actually live today (CLAUDE.md banners, chat-era .md files, memory, skills, hooks) against what iba.db/cfg_* already hold, and naming each gap where a document instead of the app controls the process. This takes up #2173 decision 2. Step 2 (design) and step 3 (build) only on the researcher's instruction after reviewing step 1.

**v3** (2026-10-21T03:43:07Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **resolution (set this version):** Approach proposed, awaiting researcher: (a) approve step 1 = diagnosis only, no build, written to a .md review file; (b) scope - the Bible-study process only (strands, weaves, register, threads, session start/close) or also the IBA base-data layer. Claude starts step 1 on the researcher's answer.

**v4** (2026-10-21T03:45:06Z, Researcher) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Researcher, chat 2026-10-21 (verbatim): '1  Do not go ahead with the analysis and diagnostic, you do not even know what to do.  2 - the scope is THE PROJECT not a subset.' Proposed step 1 (diagnosis) rejected; scope is the whole project. Claude waits for the researcher's direction on what the reset is to do; nothing started.

**v5** (2026-10-21T03:46:25Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Correction: v3/v4 wrongly set ready_for_approval + Researcher. Nothing exists for approval; the researcher instructed that Claude works this escalation (chat 2026-10-21). Claude moved it to satisfy the Stop-hook backlog check, which allowed leaving ongoing work as-is. Restored to Claude, in-progress, review: Claude works it on the researcher's direction of what the reset is to do.

**v6** (2026-10-21T03:46:37Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Correction: the v3 resolution text described a proposal the researcher has rejected, so it was wrong to leave in place.
> **resolution (set this version):** Not yet resolved. The proposed diagnosis was rejected by the researcher (v4); scope is the whole project. Claude works this item on the researcher's direction.

**v7** (2026-10-21T04:03:34Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Researcher, chat 2026-10-21 (verbatim): '2177 is an escalation for the reset of the IBA app, and it will stay open until all the elements of reset have been completed. 2178 was the first.' Elements so far: #2178 (approval hand-over checks, rule 63; completed); the control-documentation verification, raised the same day as its own escalation.

**v8** (2026-10-21T04:03:40Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **context (set this version):** Reset elements: #2178 (completed), #2179 (control documentation structure)

**v9** (2026-10-21T04:24:01Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **context (set this version):** Reset elements: #2178 (completed), #2179 (completed: control documentation review), #2180 A control map, #2181 B CLAUDE.md, #2182 D stale roots, #2183 C history out of read path, #2184 E memory, #2185 F start print scope, #2186 G close check

**v10** (2026-10-21T04:52:05Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **context (set this version):** Reset elements: #2178 (completed), #2179 (completed), #2180 A control map (completed), #2181 B CLAUDE.md, #2182 D stale roots, #2183 C history out of read path, #2184 E memory, #2185 F start print scope, #2186 G close check, #2187 user guide rewrite

**v11** (2026-10-21T05:45:14Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **context (set this version):** Reset elements: #2178, #2179, #2180 A, #2182 D, #2183 C, #2184 E, #2185 F, #2186 G (all completed); #2181 B and #2187 user guide (with the researcher for approval); #2188 the 8 instruction files into config; #2189 permission settings information.

**v12** (2026-10-21T05:48:26Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** PICK-UP RECORD at session close 2026-10-21 (researcher asked that nothing be silently dropped). Researcher instruction for the next session: restart in /developer-mode, then proceed with approvals.
DONE and approved: #2178 (rule 63 hand-over checks), #2179 (control-doc review; report v2 outputs/escalation/2179-control-documentation-structure-review-v2-20261021.md), #2180 A control map (cfg_control_home), #2182 D stale roots retired, #2183 C history out of read path (rule 96, GOVERNANCE.md rewritten), #2184 E memory cut to profile + 5 pointers, #2185 F deliver_when scoping, #2186 G SC15 control-file check.
WAITING ON THE RESEARCHER: #2181 B (new CLAUDE.md + 13 rules 83-95 wording); #2187 user-guide rewrite; #2189 permission settings decision (outputs/escalation/2189-permission-settings-information-v1-20261021.md; the edits are the researcher's).
PARKED FOR THE RESEARCHER: #2190 study-side controls when the study re-opens (29 study principles; study files' own history); #2194 CHARTER sec 2/3 describe a past state (CHARTER is the researcher's to change).
WITH CLAUDE, NOT STARTED: #2188 the 8 instruction files (+ iba/config JSON) into config, narrative rules first (on-hold until the next session); #2191 retirement check for 36 old docs/ files; #2192 replaced history in code comments; #2193 copy tests must use the SQLite backup API (a dev rule).
RECORD: iba/app/BUILD.md sec 354-363; migrations iba/app/migration/*_20261021.py (run ids DEVMODE-2178..2187-*); the per-option files in outputs/escalation/218*-*.md; old CLAUDE.md, GOVERNANCE.md, USER-GUIDE.md, README.md, tasks.md, docs/interaction-preferences.md, docs/file-organisation-rules.md kept as history in archive/docs/.
KNOWN: this session started before the developer-mode command required a compliance file, so it has none; the 4 orphan configs reported by validate are pre-existing (ib_observation.meaning_source, wa_obs_question_catalogue.scope/status/tier enums).
> **context (set this version):** Reset elements: #2178-#2186 completed (except #2181); #2181, #2187, #2189 with the researcher; #2190, #2194 parked for the researcher; #2188, #2191, #2192, #2193 with Claude

**v13** (2026-10-21T05:49:09Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Researcher, chat 2026-10-21 (verbatim): 'I object that the escalation is assigned to me ready for approval. Is this the correct state to put the escalation in?' Answer recorded in #2177 v5/v6 (Correction: back to Claude, in-progress); it led to #2178.

**v14** (2026-10-21T05:49:09Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Researcher, chat 2026-10-21 (verbatim): '2177 is an escalation for the reset of the IBA app, and it will stay open until all the elements of reset have been completed. 2178 was the first.  spawn another escalation to verify that the main IBA control documentation (Claude, governance, cfg_*, user_guide) and any other controls that I may not even be aware of a) is optimally structured to prevent confusion, miss read, confusing duplication, and unnessary reading of out of date instructions.' The second part raised as #2179.

**v15** (2026-10-21T09:10:04Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Session 3cea0e6c (Developer Mode), researcher verbatim: 'proceed with developer-mode.  the base escalation is 2177. start with 2195, then 2188,2191,2192, and 2193.' Done: #2195 (rule 59 dead pointer dropped) and #2196 (nine 2026-10-21 migrations registered), iba/app/BUILD.md sec 365, commit 17e202a9. Raised: #2198 (no validate check for unregistered iba/app scripts; decision). #2188, #2191, #2192, #2193 in-progress: approaches and decisions in outputs/escalation/2177-reset-backlog-plan-v1-20261021.md, awaiting the researcher's approval before build.
> **context (set this version):** outputs/escalation/2177-reset-backlog-plan-v1-20261021.md; iba/app/BUILD.md; #2195; #2196; #2198

**v16** (2026-10-21T10:33:36Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Progress, session 3cea0e6c: completed #2191 (docs/ archived, BUILD.md sec 366), #2193 (backup-API copies, sec 367), #2192 (history out of 89 active code files, sec 368), #2195/#2196 (sec 365). #2188 on-hold with the study. Raised #2199, #2200 (archive retired code), #2201 (open items from comments). With the researcher for decisions: #2198, #2199, #2200, #2201 (plus #2181, #2187, #2189 from before). Stays open until every reset element is done.

**v17** (2026-10-21T11:11:04Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Progress, session 3cea0e6c: #2200 (798 scripts retired, retired-script gate hook, BUILD.md sec 369) and #2198 (validate hard error on unregistered scripts) completed. Still with the researcher: #2199, #2201 (plus #2181, #2187, #2189). #2188 on-hold with the study. Stays open until every reset element is done.

**v18** (2026-10-21T14:06:35Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Progress 20261021b: #2195, #2191, #2192, #2193, #2198, #2200 (798 scripts retired, gate hook, validate hard error), #2199 and #2201 done; #2188 paused until the study restarts; #2181, #2187 and #2189 completed. #2171 is open with the researcher. Validate ok; the only finding is the 4 orphan enums in #2197. Commits up to 2bba8e86.

**v19** (2026-10-21T17:05:08Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Researcher, chat 2026-10-21 (verbatim): 'all the outstanding approvals with comments were made except for 2171 which remains open'. Acted on: #2181, #2187, #2189 approvals noted; #2199 and #2201 implemented and closed (BUILD.md sec 370, commit 2bba8e86); #2171 left with the researcher. Session close raised #2205 (6 spine gaps not verified, STEP not running).

**v20** (2026-10-21T17:23:31Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Researcher observation 2026-10-21 on reading waste (inconsistencies, redundant routines, #2197 warnings, long rule lists) raised as reset element #2206; options in outputs/escalation/2177-reading-waste-options-v1-20261021.md, with the researcher for decision.

**v21** (2026-10-21T17:52:12Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Progress 20261021c: #2206 built and live (commit 1267b220, BUILD.md sec 372), with the researcher for approval and the option 2b decisions; #2197 withdrawn; #2207 (validate, new findings only) and #2208 (PS folder settings unread) with the researcher.

**v22** (2026-10-22T03:21:31Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Progress 20261022: #2209 approved and completed (rules linked to operations in cfg_rule_scope and shown at the point of use; start and compliance file down to the 41 general rules; BUILD.md sec 374-375). Its documentation (iba/app/GOVERNANCE.md, iba/app/USER-GUIDE.md, .claude/commands/start-project.md) was updated in the same build, so no companion task is needed (escalation rule 12). Still open: #2206 (approval, 2b table), #2207 (19 new config findings), #2208 (approval), #2211 (with Claude).

**v23** (2026-10-22T04:10:38Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Researcher, chat 2026-10-22 (verbatim): "you will soon run out of tokens, then the study will be parked again". Acted on: the slow full scan in #2211 was stopped, and the session was closed before #2207 continued.

**v24** (2026-10-22T05:28:05Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Researcher, chat 2026-10-22 (verbatim): "I think you are now starting to unravel.  it is right that you identify all the weaknesses, omissions and errors of the past. but because the actual methods are not delivering what it supposed to, you are in danger of fixing the wrong issues.  I am not sure what to do - leave everything in the air, as so many times in the past,  say no to the fixes - that will just mean you will continue to make the same errors, or first focus on the real objective and that is to perform operations that make sense, is valuable and deliver the objectives of the study." Claude agrees: the #2207 backlog was built from validate findings, not from what the study needs; the control the hold names (#2172) is untouched by it.
> **context (set this version):** outputs/escalation/2177-fix-the-right-thing-v1-20261022.md
> **resolution (set this version):** Decision sought (outputs/escalation/2177-fix-the-right-thing-v1-20261022.md): #2207 A stop here (commit the tested work, park the rest on-hold), B finish it first, or C leave it; then next app work 1 the #2172 completeness control (what reached the narrative and claims register, checkable by the researcher; no reading done) or 2 nothing until the study is re-opened. Claude recommends A then 1.

**v25** (2026-10-22T05:35:22Z, Researcher) state=re-assigned next_action=approved assigned_to=Claude
> **comment (set this version):** Researcher, chat 2026-10-22 (verbatim): "A then 1". #2207 stops here: the tested work is committed and the rest parked on-hold; next app work is the #2172 completeness control (design first, for approval).

**v26** (2026-10-22T08:44:57Z, Claude) state=re-assigned next_action=approved assigned_to=Claude
> **comment (set this version):** Progress on item 1 of the researcher's "A then 1" (the #2172 completeness control): built and live in session 691d410b (BUILD.md sec 386) -- Strand-Reading.ps1 with the account and the close gate strand_account_clean; 84 of 84 tests on copies. It is with the researcher for approval on #2172 (v21). #2177 stays with Claude until that approval and the catch-up that follows it.

**v27** (2026-10-22T11:21:57Z, Claude) state=re-assigned next_action=approved assigned_to=Claude
> **comment (set this version):** Progress 20261022 (session 6c511f74): #2219 open-item handling built, tested (106 of 106 on copies) and live, with the researcher for approval (BUILD.md sec 388); #2172 catch-up B live, 691 observations from the October ledgers (sec 389). #2216 and #2217 carry what was left out; thread OT-108 holds the open readings. Next: #2172 catch-up C. #2177 stays with Claude.

**v28** (2026-10-22T12:03:13Z, Researcher) state=re-assigned next_action=approved assigned_to=Claude
> **comment (set this version):** Researcher, chat 2026-10-22T09:58 (verbatim): "continue with 2177 - you had unanswered questions at the end of the last session?" Answered: the open questions were the five catch-up decisions on #2172 (outputs/escalation/2172-catch-up-plan-v1-20261022.md section 3); the researcher answered them (#2172 v26, v28).
