# Escalation deep history

## #2228 — Reading process forces a whole-strand rebuild per subset
type=issue source=researcher

**v1** (2026-10-22T13:03:50Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **short description (set this version):** Reading process forces a whole-strand rebuild per subset
> **comment (set this version):** Researcher, chat 2026-10-22 (verbatim): "nope. Then the analytic build is not correct.  We cannot go into a complete rebuild everytime a subset is being visited or revisited.  there is something materially wrong in how the whole infrastructure is fitting together and how the analytic process is recorded." Raised from #2172: recording 26 anger inner-seat rows (a subset of 43 verses) could only be carried to claims, open items and narrative by running Map over all 178 blocks related to the anger strand and Derive over all 352 of its observations (outputs/strand-reading/anger/anger-gather-v1-20261022.md).
> **context (set this version):** iba/app/lib/strandreading.py; iba/app/ps/Strand-Reading.ps1; outputs/strand-reading/anger/anger-gather-v1-20261022.md; #2172; #2219

**v2** (2026-10-22T13:04:59Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **context (set this version):** outputs/escalation/2228-subset-rebuild-diagnosis-v1-20261022.md; iba/app/lib/strandreading.py
> **resolution (set this version):** Decision sought (outputs/escalation/2228-subset-rebuild-diagnosis-v1-20261022.md): four causes found in iba/app/lib/strandreading.py -- (1) the strand is the only unit of work and Map refuses unless every related block (178 for anger) is mapped; (2) a mapping is not kept as a state, so every visit remaps; (3) observations live in one strand's silo, grounded only on that strand's words; (4) done exists only as the strand close gate, not per verse or observation. Choose which directions to design (1 scope per step, 2 mapping as state, 3 observations grounded on every inner word, 4 done per verse and observation), and whether to design now or review the table fit more widely first. Nothing built (rule 105).

**v3** (2026-10-22T13:15:10Z, Researcher) state=in-progress next_action=revise assigned_to=Claude
> **comment (set this version):** Researcher, chat 2026-10-22 (verbatim): "It looks like you are not looking at all at work already done in the _analytics folder, and rereading of anything should be restricted to items that have not been read or need a revised reading, and the scope of the analysis is determined by what it requested, this could be a variety of things, by cluster, for a set of verses, for a single verse, for a open item, for a specific claim - looks like you missed the boat."

**v4** (2026-10-22T13:16:36Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **context (set this version):** outputs/escalation/2228-subset-rebuild-diagnosis-v2-20261022.md; v1 archived at outputs/escalation/archive/2228-subset-rebuild-diagnosis-v1-20261022.md; iba/app/lib/strandreading.py
> **resolution (set this version):** Decision sought (outputs/escalation/2228-subset-rebuild-diagnosis-v2-20261022.md, rewritten on the researcher's correction of v3): (1) is the statement of what an analysis must do right -- start from work already done (tables and _analytics), read only the unread or what needs revision, scope from the request (cluster, verse set, verse, open item, claim)? Measured against it, the build reads no _analytics file, keeps October work only as notes (352 anger observations draft), has no done-state for blocks or observations and no revision trigger, and takes only a strand as scope. (2) Next step: Claude maps what already exists (the analytic tables and the kinds of _analytics work and how each names its verses), then a design for review. Nothing built.

**v5** (2026-10-22T14:41:53Z, Researcher) state=in-progress next_action=revise assigned_to=Claude
> **comment (set this version):** Researcher, chat 2026-10-22 (verbatim): "#2228 is sort of in the right direction.  but i can see it will just lead to another disaster.  we need to break it down and working in a standard session is not the place to do it.  so I am again placing the study on hold because you are not ready and did not build the code as expected.  I am going to close this session and start up a developer session again to first fix it." Next: in a Developer Mode session, break #2228 down (outputs/escalation/2228-subset-rebuild-diagnosis-v2-20261022.md as the starting statement) before anything is built. Study on hold again (#2229, #2230 proposals).

**v6** (2026-10-22T14:46:45Z, Claude) state=in-progress next_action=revise assigned_to=Claude
> **comment (set this version):** Researcher, chat 2026-10-22 (verbatim): "both approved in terminal - for your action" (#2226, #2227: study re-opened) and later "#2229 and #2230 approved in terminal." (study on hold again, the reason being this item). All four applied with their -RunIds.
