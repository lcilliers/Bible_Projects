# Escalation deep history

## #1778 — Audit/update stage between char-answers and char-synergy
type=task source=researcher

**v1** (2026-09-19T03:39:38Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Audit/update stage between char-answers and char-synergy
> **comment (set this version):** Researcher's own pivot, verbatim (superseding #1769, the filler-obs_text validation item): 'I changed my mind around to management of observations that is not correct. I will design a new audit and update stage that sits between char-answers and char-synergy. This routine will use a set of rules (to be designed) that will run through observations and make direct updates to observations without the need of rerunning the entire pipeline.' A rules-based post-answer correction pass, not a re-run -- rules to be designed. #1769's own concrete finding (id 4655, obs_text='placeholder', 1 row corpus-wide) becomes one example this new stage should catch, not a case handled separately by broadening a regex.
> **context (set this version):** Supersedes #1769. Related open items in the same area: #1768 (front-loaded observation content not fed to the LLM, cross-cluster tagging), #1770 (tag system review from scratch), #1771 (meaning_source enforcement redesign, approved) -- this new audit/update stage may end up as the natural home for some of those corrections too, not decided yet.

**v2** (2026-09-19T09:18:44Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):**  this audit functionality is based on a set of rules (to be define) that will run the the observations and nodes to improve the alignment of the data after the completion of the llm work.  The rules will progressively be defined and added, as gaps are discovered in the data.  the aim is for you to create a untility that can use input to update the related table.  the input will be generated follow user driven exploration to identify actions to be taken 
> **context (set this version):**   

**v3** (2026-09-19T09:22:53Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Proposal filed per your direction -- not built. Reading your instruction precisely: you want the mechanism (a utility that applies an externally-supplied rule), not me inventing the rules. Covers rule shape (selector + update), a new correction-log table for audit trail, preview-then-live discipline matching every other write script tonight, and 4 real open questions (rule storage format, selector language scope, whether this is the mechanism that finally drives ib_observation.status's dormant lifecycle from #1753 B2, manual vs scheduled).
> **resolution (set this version):** iba/docs/1778-correction-rule-utility-proposal-v1-20260919.md. #1769's own placeholder-obs_text finding (id 4655) proposed as the first real rule once the utility exists, closing that loose end for real. Nothing built -- waiting on your answers to the 4 open questions.

**v4** (2026-09-20T07:18:03Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Proposal doc revised in place per your 4 points this chat turn: (1) rule storage corrected to a cfg_* table (cfg_observation_enhancer_rule) -- offering a JSON-file option alongside it was a governance.rules_must_be_config_driven deviation, acknowledged and fixed, no good reason for it; (2) selector is now a real SQL SELECT, safety is per-rule researcher confirmation via -Preview before it ever runs live, not a restricted grammar; (3) ib_observation.status bug split out to its own escalation, #1782, since this utility will drive that field; (4) v1 manual/on-demand, graduating to an automatic pipeline step once rules stabilise -- confirmed, no design change needed for that later step. Utility renamed observation_enhancer throughout (was misnamed 'correction').
> **context (set this version):** Revised doc: iba/docs/1778-correction-rule-utility-proposal-v1-20260919.md (filename unchanged this round per feedback_spec_review_edits_in_situ_not_versioned -- edited in place during an open review cycle, not re-versioned until you approve). Companion escalation: #1782 (ib_observation.status hardcoded, lifecycle never wired up).
> **resolution (set this version):** All 4 original open questions now answered in the doc. Waiting on your go to build items 1-4 (tables, handler, PS wrapper, cfg_step/cfg_utility registration) in one pass; the first real rule (#1769 id 4655) will come back to you for confirmation before it runs live, per the new per-rule confirmation discipline.

**v5** (2026-09-20T07:28:02Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):**  proceed with the build as planned 
> **context (set this version):**   
