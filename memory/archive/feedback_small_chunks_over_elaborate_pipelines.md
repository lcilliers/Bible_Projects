---
name: Small chunks over elaborate AI pipelines
description: While analytic methodology is still being figured out, break work into the smallest atomic chunks and run them in chat — don't build elaborate instruction sets or end-to-end automation
type: feedback
originSessionId: 0b9d95eb-ab3c-4fd3-9dd9-6341794c07de
---
When the analytic methodology for a piece of work is not yet fully specified, **default to the smallest atomic chunk that produces a clear intermediate result**. Do not build elaborate multi-phase instruction sets or large end-to-end API automations on the assumption that the methodology is settled.

**Why:** The user is still discovering what the right cuts and properties are at the cluster-analysis level. The wa-sessionb-cluster-instruction prescribed a 10-phase pipeline (read → cluster → assign → characterise → finalise) that assumes the analytic logic is known. The 2026-05-09 M26 modelling attempt demonstrated the cost of that assumption: a "big-picture" Phase 4+5+6 prompt consumed $0.50 with zero output (max_tokens burned on adaptive thinking); subsequent atomic per-verse meaning extraction (Step A) produced clean output but required a redesign; the user-led subject classification in chat (after rejecting a $2.44 API run) produced immediately useful structure. Volume of attempts + accumulated cost ($5.66+ on M26 alone, much of it wasted) reinforces preference for small, user-orchestrated chunks.

User's own articulation: *"I am leaning toward moving away from the approach until I know where I have an elaborate instruction set, and let AI loose on it. I need to focus breaking down the analytics in small chunks and pass it into AI to deal with it in the chat, but without expecting these big picture analytic results."*

**How to apply:**
- When a task involves multi-step analytic work whose end-state isn't fully specified, propose the SMALLEST atomic chunk that produces a useful intermediate. Stop. Present. Await direction.
- Don't write `_apply_*` API automation scripts with elaborate system prompts when a user-driven chat sequence would work.
- Stay sceptical of prompts that ask AI to do clustering + grouping + characterisation + assignment in one go — those are usually the wrong-size bite.
- My role on cluster/registry analytics:
  1. Prepare data extracts (JSONL / .md slices) sized for one chat chunk
  2. Build read-only renderers that consume the user's chat output
  3. Stop reaching for `_apply_*` API scripts as the default
- Ask: *"What's the smallest output that would let you decide the next move?"* Build that, stop.
- The wa-sessionb-cluster-instruction's elaborate phase architecture should be treated as a placeholder — not gospel — until the small-chunks experimentation has clarified what each phase should actually do.
