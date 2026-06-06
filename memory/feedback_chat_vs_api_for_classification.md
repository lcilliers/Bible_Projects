---
name: Chat vs API for batch classification
description: Default to chat (paid subscription) for one-shot batch read/classify; reserve API for atomic high-volume work or pipeline-fed output
type: feedback
originSessionId: 0b9d95eb-ab3c-4fd3-9dd9-6341794c07de
---
For batch interpretive tasks (classification, characterisation, sub-group cuts, property tagging) where the input data fits in a single chat context, **default to recommending the user paste the data into a chat session** instead of building an API automation script.

**Why:** The user has a paid chat subscription. Chat is at zero marginal cost; API runs at ~$0.003–0.005 per verse. Demonstrated 2026-05-09 on M26-A subject classification — 589 records cost $2.44 via API (claude-sonnet-4-6, ~23 min), where pasting the JSONL into chat produced the same result in seconds at no incremental cost. User flagged the misalignment directly.

**How to apply:**
- Before writing an `_apply_*` script for a classification/property task, ask: "Could this be done by pasting the prepared data into chat once?" If yes — propose that path FIRST.
- API automation is justified only when:
  - Input data genuinely exceeds chat working context (rare; 868 records of ~200 tokens each fits)
  - Output must feed automated downstream code without human review
  - The same operation will repeat across many clusters/runs and the per-run cost is amortised by automation
- My job in the chat path: prepare clean input artefacts (JSONL/markdown extracts), build read-only inspection/render helpers that consume the user's chat-produced output, and stay out of the loop in between.
- Step A (per-verse meaning extraction across 868 atomic calls with resumable JSONL) is the borderline case where API may still be right because of structured output + atomicity. Step B onward (one-shot batch reads over the assembled JSONL) is squarely chat territory.
