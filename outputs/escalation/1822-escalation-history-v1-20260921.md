# Escalation deep history

## #1822 — 'The primary term' in M0.5.2/3 is undefined
type=task source=Claude

**v1** (2026-09-21T10:57:00Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** 'The primary term' in M0.5.2/3 is undefined
> **comment (set this version):** Researcher question, this chat turn, verbatim: 'what is regarded as the primary term in M0.5.2 and M0.5.3'. Checked precisely -- there is no operational definition anywhere. Confirmed by code search (zero hits for 'primary' in any live stage-generator module) and empirically (every one of M49's 5 owned strongs, including one that occurs in a single verse, got its own separate M0.5.2/M0.5.3 answer -- no selection is happening).
> **context (set this version):** M0.5.1 genuinely names two primary terms ('the primary Hebrew and Greek terms' -- one per testament, cluster-level). M0.5.2/M0.5.3 inherit the singular 'the primary term' phrasing but are answered under the current per-strong front-loading mechanism (#1723, 2026-09-17): versereadinggenerate.py's own instruction says 'answer for EVERY strong listed in meaning_sources_by_strong -- not just this cluster's own member strongs' with no designation of which one (if any) is primary. Each strong's own M0.5.2/M0.5.3 answer is written framed as if IT were the primary term. The wording predates the per-strong redesign and was never updated to match -- same underlying pattern as Finding 13 (a question worded as scoped to one thing, mechanically repeated across every strong), but a distinct instance: this one is a wording/scope mismatch in the catalogue text itself, not a missing skip-check. Also relevant: the #1814 wording review marked M0.5.2/M0.5.3 COMPLIANT under the 'definitional-category' bucket without catching this ambiguity -- worth a note there too, not corrected in that review's own text here.

**v2** (2026-09-21T11:14:51Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):**  fix the redundant terminology 
> **context (set this version):**   
