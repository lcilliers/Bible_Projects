---
name: feedback_verify_contributor_reference_text_first
description: A reference cited by Logos/AI-Chat (esp. out-of-corpus) must be verified against the actual verse TEXT before loading — Logos references are not always good
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ace57f3e-b52e-4cc7-adda-ef61148f91e0
---

When a verse reference enters via a **contributor** (Logos, AI-Chat) — especially one that is **out-of-corpus** (not in the `verse` index, so it can't simply be loaded) — the **first step is to check the actual verse text** and confirm it is a *suitable* reference for the point being made.

**Why:** **Logos references are not always good** (the researcher has repeatedly seen mis-cited / loosely-relevant refs). A reference in a fanout is a *claim*, not yet evidence; the text must confirm it.

**How to apply:** before loading/onboarding an out-of-corpus (or any contributor-cited) reference, fetch and read its text — STEP's `getBibleText` endpoint returns text + morphology for **any** verse (full Bible, not just the corpus). Confirm it actually says what the contributor claims. Only then decide to bring it into the corpus / use it. See [[project_multi_contributor_spiderweb]] (provenance + STATED/INFERRED), the `vr_out_of_corpus` control (catches such refs that got loaded as verse_records), and [[feedback_verse_meaning_grounded_not_imported]].
