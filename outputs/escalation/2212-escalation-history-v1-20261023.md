# Escalation deep history

## #2212 — Prose patches name a retired apply script
type=issue source=researcher

**v1** (2026-10-22T04:10:39Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Prose patches name a retired apply script
> **comment (set this version):** Found at session close 2026-10-22: iba/app/USER-GUIDE.md (Prose section) tells the patch-generating Prose.ps1 steps (ImportChapter, SetStatus, FlagFixApply) to apply their PROSE patch with scripts/apply_session_patch.py. That script was retired on 2026-10-22 (#2207, the researcher ruling of 2026-08-18), now at scripts/archive/apply_session_patch.py. So applying a prose patch has no live path. Decide whether prose patches are still produced, and if so what applies them.
> **context (set this version):** iba/app/USER-GUIDE.md; scripts/archive/apply_session_patch.py; iba/app/ps/Prose.ps1; #2207
