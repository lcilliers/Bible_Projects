---
name: feedback_fix_standard_violations_dont_ask
description: "When work deviates from an already-established, documented standard/pattern, fix it immediately — do not ask \"should I fix it?\". Asking is only for genuine judgment calls (data quality, thresholds, architecture direction), never for compliance with a standard that already exists."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7608c281-70c1-41bb-8181-d9ebf468771f
  modified: 2026-07-21T17:10:25.535Z
---

Researcher's correction (2026-07-21), after I asked whether to fix new IBA-app quality checks that
didn't persist their findings to a report file, when the app's own established standard (every other
report — `report.py`/`validation.py`/`cfgreport.py` — writes a persistent `.md`, matching `CLAUDE.md`'s
project-wide "output always goes to a file, never chat/terminal-only" rule) already required it:
**"should you fix it? why ask? why is there a standard if you don't follow it - obviously it must be
fixed. Errors is not optional to fix it."**

**Why:** asking "should I fix this?" is appropriate when there's a genuine judgment call — data
quality thresholds, architecture direction, which of several valid designs to pick. It is NOT
appropriate when the work simply fails to comply with a standard that's already settled and
documented. That's not a decision point, it's a bug. Treating it as an open question wastes the
researcher's attention on something that was never actually optional.

**How to apply:** before asking "should I fix X," check whether X is a deviation from an
already-established, already-documented standard/convention in this project (or the app being
built). If yes — fix it, note that you fixed it and why, and move on. Reserve the question for
things that are genuinely undecided. This generalizes past the IBA app to any project with a
documented convention (CLAUDE.md, a style guide, an established code pattern already used
elsewhere in the same codebase).

**IBA-app-specific instance:** the researcher additionally asked for this codified as an app config,
not just remembered — see `governance.reports_must_persist` (cfg_setting, module=governance) and the
new `configmaint.validate` coherence check enforcing it, so future sessions don't need to rely on
memory alone; the app itself checks compliance. Related: [[feedback_iba_data_judgment_calls_must_escalate_not_silent_report]].
