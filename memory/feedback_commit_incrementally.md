---
name: feedback_commit_incrementally
description: "Commit units of work incrementally throughout a session, not only at session end; commit and push always go together"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: eae3184c-630b-48c2-9ac1-b0b494ccf689
---

Commit regularly throughout a session — do not leave changes uncommitted for long stretches and do not save committing for the end of a session only.

**Why:** On 2026-05-31 the working tree had ~50 uncommitted files spanning three sessions (05-28/29/30) because prior sessions only committed at the end (or not at all). A computer restart could have lost or muddled that work, and a single end-of-session commit makes the history hard to read.

**How to apply:**
- Commit each logical **unit of work** as it completes (e.g. one cluster phase, one script, one report set), not just at session boundaries.
- In-progress commits are fine and encouraged — a `session YYYYMMDD: <desc> (in progress)` commit to lock in partial work beats leaving it open.
- Group related untracked files into coherent commits rather than one mega-commit; match the existing `session YYYYMMDD: brief description` message format (see [[feedback_version_discipline]] and CLAUDE.md §12).
- Still respect the standing rule: only commit/push when the user has asked, or when it is the natural close of a unit they directed — but once authorised, prefer several scoped commits over one.
- **Commit and push always go together** (researcher rule, 2026-06-03): never leave a local commit unpushed. As soon as you commit, `git push origin main` in the same step — do not stop at the commit and ask separately about pushing. The 06-03 DB-loss incident (see [[project_db_loss_blocker_20260603]]) drove this home: work that lives only locally shares one failure domain; the remote is the safety net.
- Leave `_tmp_*` throwaway dumps uncommitted (CLAUDE.md §6).
