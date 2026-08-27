# Escalation deep history

## #746 — cfg_escalation Rule-Table Staleness
type=issue source=claude related_activity=escalation-redesign-followups-20260820 -- module_blocking references escalations_old #646 (the item that wired it); the title-correction convention mentioned in this item's own comment references live #759 from_id=759

**v1** (2026-08-21T11:44:23Z, Claude) state=raised next_action=review assigned_to=Claude
> **short description (set this version):** cfg_escalation Rule-Table Staleness
> **comment (set this version):** cfg_escalation (the rule table governing escalation.py itself, 7 rows) still describes the pre-redesign single-table mechanism -- duplicate_suppression/chat_routing/document_reference_grouping etc. need review against the new raise_new/update split.

[data corrected 2026-08-20, escalation #759: short_description reshaped to a <=60-char title; prior full text redistributed into context (background) / comment (what needs to be done) / resolution (what was actually done) per the researcher's column-spec correction. No prior escalation_history row altered.]

[title corrected 2026-08-20, escalation #759 round 2: round 1's short_description was a compressed sentence, not a composed title -- researcher: "it looks like you just cut whatever was there previous to 57 chars". Redone as an actual noun-phrase title, matching #753's own style. comment/context/resolution from round 1 are unchanged.]
> **context (set this version):** Also contains a known-stale row: module_blocking.enforced_by still reads 'not yet wired' though it has been live in run.py since escalation #646 (2026-08-17) -- found during the mechanics investigation (iba/docs/escalation-system-mechanics-20260818.md), never fixed.
> **related activity (set this version):** escalation-redesign-followups-20260820

**v2** (2026-08-21T12:43:08Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** proceed to check if this is still relevant, if so then fix.  also, if there is a another escalation it refers to, then complete the related columns

**v3** (2026-08-21T12:46:00Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Checked, one real staleness found and fixed, related-column question noted above.
> **resolution (set this version):** Checked all 10 active cfg_escalation rows individually against today's live code, not assumed. 9 of 10 accurate as written (several explicitly document their own 2026-08-20 corrections -- source_classification, document_reference_grouping; the rest correctly self-describe as 'session practice, not mechanically enforced' where that's true). One genuinely stale: module_blocking.enforced_by read 'not yet wired -- scheduled as a task escalation', but the mechanism has been live since 2026-08-17 -- run.py:run_step()'s third dispatch gate, citing escalation #646 explicitly (confirmed reading the code directly, lines ~135-154). escalations_old #646 (completed, frozen) is literally the item that built the wiring -- its own text says 'enforced_by currently says not yet wired', meaning the correction was never carried back once #646 closed. Fixed via migration/fix_module_blocking_enforced_by_20260821.py.

On 'complete the related columns': this item's own comment references escalation #759 (live, in-table, id unchanged from this session's D1 load) for the title-correction convention it mentions, and escalations_old #646 (frozen, not in the live table) for the module_blocking wiring itself. Could NOT literally set from_id -- it's immutable-after-Raise by this session's own D14 design (no update() parameter exists for it at all), so an already-raised item like this one can't be retroactively linked that way. Noting the reference here in resolution/related_activity instead, the field that stays editable. Worth flagging as its own question for later: from_id's immutability is deliberate (matches run_id/source/at_step/type/raised_at), but it does mean 'go back and link an existing item to something it turns out relates to' -- exactly this task -- has no mechanical path at all right now.
> **related activity (set this version):** escalation-redesign-followups-20260820 -- module_blocking references escalations_old #646 (the item that wired it); the title-correction convention mentioned in this item's own comment references live #759

**v4** (2026-08-21T12:56:17Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** from_id now settable post-raise (escalation #763 fixed this) -- linking to #759 for real, closing the gap flagged in this item's own previous resolution.

## #759 — escalation.short_description Column-Spec Violation
type=issue source=iba.app.lib.escalation related_activity=escalation-utility-refinement, related #753 from_id=

**v1** (2026-08-21T11:44:23Z, Researcher) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** escalation.short_description Column-Spec Violation
> **comment (set this version):** short_description across the 23 post-redesign items averages 247 characters (max 516) -- full paragraphs, not a label/title. Needs a raise-time length/shape check going forward, and a decision on whether any residually-imperfect rows are left as historical fact.

[data corrected 2026-08-20, escalation #759: short_description reshaped to a <=60-char title; prior full text redistributed into context (background) / comment (what needs to be done) / resolution (what was actually done) per the researcher's column-spec correction. No prior escalation_history row altered.]
Data repair complete -- leaving next_action=review for your sign-off given the scale (23 rows touched), rather than self-closing.

[title corrected 2026-08-20, escalation #759 round 2: round 1's short_description was a compressed sentence, not a composed title -- researcher: "it looks like you just cut whatever was there previous to 57 chars". Redone as an actual noun-phrase title, matching #753's own style. comment/context/resolution from round 1 are unchanged.]
Guardrail built and tested -- ready for your sign-off.
> **context (set this version):** cfg_column spec: 'label/title -- what this item is about'. By source: claude-authored avg 275 chars (11 rows), configmaint(system)-authored avg 320.5 (2 rows), researcher-authored avg 199.6 (8 rows). Root cause: raise_new()/raise_() store -Question verbatim with no length/shape check at write time. This data-repair pass (migration/fix_escalation_short_description_and_columns_20260820.py) corrects the 22 other affected rows' current state; the raise-time guardrail itself is still open, tracked here.
> **related activity (set this version):** escalation-utility-refinement, related #753

**v2** (2026-08-21T11:44:23Z, Researcher) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **resolution (set this version):** Guardrail added, closing the loop -- data was fixed in v2/v3 of this item, recurrence now prevented in code. Added _title_shape_error() to escalation.py: rejects (manual Raise, hard reject -- ValueError) or sanitises (dispatcher-tied, since it fires from inside a crash handler and can't afford to error) a short_description that is over 60 chars, contains '--' (this project's own clause-connector convention -- present in every violation found live, absent from your own #753 example), or contains a newline. Dispatcher-tied sanitising never loses data -- the full original is preserved in context.full_message whenever shaping actually changes anything.

Also fixed in the same pass, found before it could bite: escalation.py's own CLI crash-wrapper (built for finding 2) was calling raise_new() with the raw exception message as the title -- which the new guardrail would have hard-rejected, and since that call is wrapped in except:pass (so a recording failure can't mask the real crash), it would have silently swallowed the crash record instead of raising it. Fixed to sanitise first, like the dispatcher-tied path.

Tested on a scratch DB copy: manual raise correctly rejects >60/--/newline and accepts a real title; dispatcher-tied correctly sanitises a long+dashed message to <=60 chars with the full text preserved, and passes an already-clean title through untouched; the CLI-crash-wrapper interaction specifically verified with both a self-referential case and a genuine unrelated crash -- both recorded cleanly, neither swallowed. write_list_report() still renders against the mixed data. Full detail: BUILD.md sec160.

**downward chain (spawned from #759):** #746

## #753 — Escalation utility Refinement
type=task source=researcher related_activity= from_id=

**v1** (2026-08-21T11:44:23Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Escalation utility Refinement
> **comment (set this version):** the escalation utility was completely redesigned in 18-20 Aug 2026. this is first review since it has gone live. This task will serve as the entry point for all the issues and tasks that about escalation that relates to it.

This task will stay open until all the aspects covered in this note have been fully covered and signed off.


prepare an detail report of all the existing configs related to escalation utility before any changes are made

validate that all the existing configs are used, aligns with the intent, and are complete. I have already notice issues in that the new columns use does not align with the design or expectations; and are not convinced that the rules for the new functionality is actually encapsulated in the configs and comply with the governance standards.
Configs report done and filed: iba/docs/escalation-config-review-v1-20260820.md. Table/column registration and cfg_setting usage are complete and correct -- no gaps there. Four real gaps found and raised as their own item, #755 (state-machine rules not in cfg_status_flow, escalation_next_action vocabulary-merge validation gap, both reports bypass the app's reportkit/cfg_report standard entirely, one orphan write-grant) -- section 5 of the report proposes concrete fixes for your decision, nothing built yet per your "before any changes are made".

One item from your notes I can't act on without clarification: "escalation History: short-description does not comply with" cuts off mid-sentence in the notes file, no object stated -- what should it comply with?

Holding on the remaining buckets (Open-escalations report layout -- now root-caused by #755 finding 3, not a separate fix; User Guide pass) until #755's proposals are decided, so the guide describes the settled shape once, not twice.
Recording a real failure in the #755 config review, per your correction: the review checked cfg_table/cfg_column/cfg_enum/cfg_write_grant/cfg_utility/cfg_escalation/cfg_setting/cfg_report/cfg_status_flow row-by-row and reported 4 specific findings, but never asked the actual question -- is the operational rule set that governs VALIDATING and COMPLETING an escalation, and the automation that executes it, represented in config at all. It is not, almost entirely, and I did not report that.

Concretely, none of the following exist in any cfg_* table -- every one of them lives ONLY in escalation.py Python code:
- which fields are required for which action (comment required at Raise; resolution required when next_action=approved; state required as withdraw|supersede when next_action=reject; tried required when next_action_assigned_to=Claude after a failed correction) -- _check_next_action()/update()'s own inline checks
- the auto-state derivation rules AND THEIR PRIORITY ORDER (plan v3 sec3's 6-rule table, first-match-wins) -- _derive_state()
- the two-stage approval semantics (ready_for_approval -> approved -> completed) and who is allowed to set which next_action -- nowhere, just the plan doc + code
- duplicate suppression, module blocking, resolution precedence, chat routing (cfg_escalation's 7 rows DO exist for these, but per #746 they are stale and not reviewed against the redesign)

Finding 1 in #755 only flagged that cfg_status_flow (which could hold PART of this -- the status-target mapping) was empty. That is one symptom. It is not the finding that the whole validation/authorization/ordering rule engine for this module has no config representation at all -- a much larger, more fundamental gap that I should have generalised to and did not.

Governance rule violated by how I actually responded once this surfaced (checked, not guessed -- cfg_behaviour_rule id, class=development, rule_key=root-fix-not-one-off): "A defect that is an instance of a class ... is fixed at the shared mechanism so every future case is correct, not remediated case-by-case while the mechanism stays broken." The short_description migrations (round 1, round 2) and even the raise-time guardrail were exactly this -- per-item/per-symptom patches on top of a mechanism (config-driven validation) that still does not exist. The guardrail stops ONE symptom (a bad title) from recurring; it does nothing for the other undocumented, unconfigured rules above, which can drift or break silently the same way short_description did.

Next: redoing the #755 config work properly -- not table-by-table presence-checking, but an explicit inventory of every validate/complete rule this module enforces, config or code, before proposing the root-cause fix.
Config work redone properly -- full report: iba/docs/escalation-config-review-v2-20260820.md. Read every function in escalation.py line by line, catalogued every validate/complete rule against whether any cfg_* row actually drives it. Findings:

A. Field-requirement rules (comment required at Raise, resolution required at approved, state required at reject, tried required after a failed Claude correction) -- ALL hardcoded, zero config. The "tried" rule was never even implemented in code, despite being in your own v1/v2 review comments.
B. State-derivation: the TARGET VALUES are partially config-backed (cfg_status_flow, once #756 clears) but the priority-ordered branching logic itself cannot be represented in that table's schema at all (entity/status/set_by has no room for a condition or an order) -- 100% Python regardless of whether #756 is approved.
C. The two-stage approval handshake (ready_for_approval -> approved) has NO check anywhere, config or code, that the two parties are actually different people.
D. cfg_escalation's own 7 rule rows -- 2 of 7 (document_reference_grouping, half of source_classification) claim enforcement by escalation.raise_manual, a function that no longer exists anywhere in the codebase. Concrete, not just "stale" as #746 already said in general terms.
E. The root cause of the originator-misattribution bug you caught: "Researcher" as a default answered_by/originator, hardcoded in 4 separate places, zero config, zero justification -- caused >=39 misattributed rows this session including #753 v4 itself, written 2 messages before I found this.

Root-cause fix (a real config representation for these rules that code actually reads, matching how cfg_on_fail drives run.py or cfg_step drives handler resolution) is NOT built in this pass -- it needs a design, and given how this same module's last redesign went (3 review rounds before anything was built), that design should get the same treatment, not another rushed patch. Awaiting your direction before proposing one.
> **context (set this version):** Escalation functionality is supported by the following design documents 

Workflow\Chat_responses\archive\comments - escalation-system-mechanics
iba\docs\archive\escalation-redesign-plan-v1-20260818.md
iba\docs\escalation-redesign-plan-v3-20260819.md



**v2** (2026-08-21T12:54:28Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** this is the master for the escalation utility revision, this can be prepared for sign off when all the related fixes have been completed
