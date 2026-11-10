# Escalation deep history

## #2366 — Port judge work-period cycle to group.judge
type=task source=Claude

**v1** (2026-11-06T17:41:22Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Port judge work-period cycle to group.judge
> **comment (set this version):** Surface-Judge.ps1 still runs the group judging through batch files, with the work-period cycle (work minutes, cool-down, progress, stop flag, restart; lib/surfacejudge.run_cycle). Surface-Group.ps1 -Action Judge (#2361 stage 4) asks through the AI client and writes tables but runs one batch per call. Next: give group.judge the same unattended cycle (settings surface_judge.cycle_*, run_batch rows, stop flag), then retire the Surface-Judge.ps1 file route and the setting surface_judge.word_prompt. A design question (where the cycle lives for all AI steps) goes to the researcher before building.
