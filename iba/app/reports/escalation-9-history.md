# Escalation deep history

## #9 — Claude's gap-discovery is reactive, not systematic
type=issue source=researcher related_activity=iba-governance-compliance-sweep from_id=

**v1** (2026-08-20T16:42:40Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Claude's gap-discovery is reactive, not systematic
> **comment (set this version):** Researcher, direct: 'We are a long way off having IBA being governance compliant. There is a lot of hidden omissions, and work arounds that you are still not consistently discovering. Unless I poke, it does not surface.' Accurate, checked against this session's own record: every finding (stale cfg_table.use text #4, id collision #5, dropped directives #6, run.py bypass #8) was found by depth-first-following ONE thread the researcher pointed at, not by a general sweep asking 'where else does this shape of defect exist'. No systematic pass has been run project-wide for any of these defect classes outside the escalation module specifically. Proposed concrete, mechanically-groundable sweeps (not vague 'be more thorough'): (1) run.py-bypass -- DONE for iba/app/ps this session (8/45), not yet done for whether the underlying Python handlers/tools themselves have equivalent gaps beyond their PS wrapper; (2) stale/contradictory cfg_table.use text -- cross-reference each table's use text against its module's most recent BUILD.md section, flag tables whose text predates a redesign; (3) GOVERNANCE.md coverage -- list every config-driven rule-engine-shaped cfg_* table (priority/condition matching, not static settings: cfg_on_fail, cfg_status_flow, cfg_candidate_rule, cfg_escalation_transition, etc.) and check each is actually described in GOVERNANCE.md, not just registered; (4) unregistered reports -- grep every report-writing function for whether it routes through reportkit.render_scaffold()/cfg_report, project-wide, not just escalation's two; (5) silently-narrowed explicit instructions -- search BUILD.md/design docs for 'explicitly deferred'/'out of scope'/'not built' language and check whether each has a corresponding open escalation, or whether (like directives 2/3 this session) it was narrated as a design choice with no flag back. Awaiting direction on whether/which of these to actually run, and at what scope -- this is a genuinely large piece of work, not a quick check.
> **related activity (set this version):** iba-governance-compliance-sweep

**v2** (2026-08-20T16:46:14Z, Researcher) state=on-hold next_action=review assigned_to=Researcher
> **comment (set this version):** Parked -- design plan (#6 thread) still in progress, this comes back after.

**v3** (2026-08-21T13:49:35Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** confirm this is now adequately covered in governance rules
