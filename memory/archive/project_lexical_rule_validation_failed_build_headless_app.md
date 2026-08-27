---
name: project_lexical_rule_validation_failed_build_headless_app
description: "Lexical layer FAILED rule-validation (8/18 dims fail, 0 pass); decision = build a headless validator + Claude-API re-read app, stop interactive-chat cycling."
metadata: 
  node_type: memory
  type: project
  originSessionId: 6b56630f-0f9e-4733-abf8-f856527e68ee
---

★ LIVE (2026-07-14). **The re-read lexical layer does not hold against its own rules.** Acceptance-sampling test (200 random lexicals/dimension, both books, checked BINARY against the catalogue rule in passage context, STEP/gloss as authority): **8 dimensions FAILED, 10 in-progress, 0 passed the 95% mark.**

- **FAILED (rule-grounded):** D1 sense (records interpretation/effect, not the word's STEP subgloss — tsaddiq→"public good"), D2 type (faculty vocab cognition/affect/disposition, not the rule's action/status/quality-from-POS), D3 source (stores target-direction pairs term→object), D9 intensity + D11 effect + D17 device + D18 direction (the **regex-derived** retrofit dims — malformed/truncated-mid-word values, wrong classifications), D12 coupling (semantic readings, not the morphological weld the rule requires).
- **IN-PROGRESS (genuine read dims, look better, need full 200):** D4 seat, D5 bearer, D6 operation, D7 target, D8 manner, D10 specifier, D13 prohibition, D14 reading, D15 role (⚠ Screen-0 God-act mis-roles seen — Pro 8:28 "God made firm the skies" roled characteristic), D16 locus (drift-suspect).
- Per researcher rule: **any failed dimension must be redone in total.**

**DECISION (researcher, 2026-07-14): stop cycling in the interactive chat; build a standalone app.** Two parts: (1) a **deterministic rule-validator** (encode every mechanizable catalogue rule per ve_nr — shape/enum-domain/self-interpretable-no-truncation/pair-direction/mandatory-not-silently-none/POS→type — runs over all ~4,137 lexicals in seconds, no session); (2) a **headless re-read harness** (Claude API / Agent SDK, PowerShell-schedulable) that per passage pulls source (morphology+STEP+passage) → model produces rule-shaped lexicals → validator gates → retry on violation → bank on pass → auto-advance, unattended. **Cost:** the interactive chat is the most expensive engine (re-sends full growing context every cycle); the API harness is several-fold cheaper (lean constant prompt + cache the static rules once). **Next session = plan + develop this app.**

**Durable artifacts (all on disk / in DB):** rulebook = `Workflow/Catalogue/wa-ve-lexical-catalogue-v1-20260702.md` (per-dim rules §2/§9 + 2026-07-14 mandatory self-interpretable rule) + cycle doc `wa-characteristic-role-lexical-cycle-authoritative-v1` (passage read rule line 100). Findings + scoreboard = `outputs/projections/SOURCE-VERIFICATION-progress.md`. DB tables: `ve_dimension_scoreboard` (per-dim status), `ve_lexical_verification` (per-value verdicts), `ve_verification_sample` (the fixed seed-20260714 samples). Verifier tooling: `_pull_verify_batch_v1` (passage-context puller), `_check_lexical_content_validity_v1`, `_check_dimension_band_drift_v1`. Related: [[feedback_test_dimensions_for_reader_drift]], [[project_reread_success_gates_and_scored_audit]] (completeness≠validity≠consistency), [[project_book_lexical_readiness_assessment]].
