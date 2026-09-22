# Escalation deep history

## #1805 — Build science-question answers (D9/D11.2/D12.1)
type=task source=researcher

**v1** (2026-09-20T16:29:09Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Build science-question answers (D9/D11.2/D12.1)
> **comment (set this version):** Researcher instruction, verbatim, this chat turn: 'create a new escalation to build the science question answers.' 4 active catalogue questions -- D9.1.1 (neuroscience/physiology mechanism), D9.2.1 (generational transmission per scientific literature), D11.2.1 (genetics/evolutionary-biology innate-endowment), D12.1.1 (behavioural-science social expression) -- are currently EXCLUDED from char-answers' battery by charanswergenerate.py's own explicit filter (question_text NOT LIKE %science extract%), because the science-extract file/data isn't wired into the pipeline at all. Confirmed via the full pipeline trace (escalation #1804): this is a documented, deliberate exclusion in the current build (module docstring: the checklist's own Stage 4 status names this wiring not decided or built), not a bug in the existing code -- but it IS a real, zero-coverage gap against the live catalogue (0/4 answered, confirmed live) that needs an actual design and build to close. Not designed here -- what the science-extract source data actually is (a file per cluster? a shared corpus resource? researcher-authored?), how it gets associated with a cluster/subgroup, and how it's fed into the char-answers payload are all open.
> **context (set this version):** Directly tied to escalation #1804 (full pipeline trace) Finding 4 and this chat's own coverage reconciliation. Companion escalation raised the same turn: redesign verse-context (the other, larger coverage gap).

**v2** (2026-09-20T16:32:42Z, Claude) state=in-progress next_action=review assigned_to=Researcher
> **comment (set this version):** Design reference for the build: outputs/cluster-reading-pipeline-full-trace-20260920-v2.md (escalation #1804) -- section 4 (Stage 4/char-answers, including the exact battery_questions() exclusion filter this gap sits behind) and Finding 4 (the coverage reconciliation that surfaced this). Build on that document, not from scratch.
