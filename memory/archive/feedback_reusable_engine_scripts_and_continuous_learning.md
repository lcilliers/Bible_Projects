---
name: feedback_reusable_engine_scripts_and_continuous_learning
description: "FEEDBACK (2026-07-02): lexical/analysis scripts must be REUSABLE, PARAMETER-DRIVEN engine components — NOT one-off scripts. Vary scenario by parameters (book, chapter, term, genre, mode), never by editing the script. Cast the pipeline as a continuously-learning process: keep updating the method/rules to get better. Rerunning earlier work is fine — the processes are repeatable by design."
metadata:
  node_type: memory
  type: feedback
  originSessionId: bf6ef2d7-5b5c-4775-88f2-f2ca15223daa
---

**Researcher direction, 2026-07-02 (standing governance for the verse-analysis pipeline).**

**Scripts are engine components, not throwaways.** Every build/analysis script must be **reusable across scenarios via PARAMETERS** (e.g. `--book`, `--chapter`, `--term`, genre/mode), so a new scenario is a new *invocation*, never an *edit*. Do NOT write term-specific/one-off scripts (the ruthlessness `_apply_*_ruthlessness_v3/v4` with hardcoded `H6531`/DISP-sets were the anti-pattern). The poetic builder `scripts/_apply_poetic_chapter_lexical_v1_20260702.py` (parameterised `--book=Psa --chapter=1`) is the model to follow. Direction of travel: fold these into the engine proper so they're first-class, parameter-invoked modes — keep configuration (seat/disposition/intensity lists, genre treatment) as data/parameters, not inline literals.

**Why:** repeatable processes mean earlier work can be **re-run** whenever the method improves — so improving the process is always worth it, and nothing is "locked in" by a one-off. This is the counterpart to [[project_cluster_rework_phase_started]] and [[feedback_no_rework_paid_twice]] (re-run > rebuild).

**Continuous learning is part of the pipeline.** Cast the whole thing as a continuously-improving process: after each run, read back, evaluate for sensibility, and **update the method/rules** (per [[project_term_driven_genre_aware_lexical_method]] "read-back + adjust rules is VITAL"). Keep the learning current in the method doc + catalogue so each run is better than the last. Concrete example of the discipline paying off: building the *reusable* poetic script on Psalm 1 immediately surfaced a cursor-reuse bug (inner `cur.execute` truncating the outer tagged-term loop to the first term/verse) that a one-off would have hidden.

**How to apply:** when a task needs a script, first ask "what are the parameters that make this general?" and write it that way (backup + dry-run + verify + inspection-view still apply). When the method learns something, update `Workflow/Instructions/wa-verse-analysis-method-v1-*` and `Workflow/Catalogue/wa-ve-lexical-catalogue-v1-*`, and be willing to re-run prior terms/chapters. Cf. [[feedback_single_living_register]], [[feedback_source_of_truth_is_written_record]].
