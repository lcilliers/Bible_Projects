---
name: feedback_lexical_strictly_verse_bounded_no_implied_evidence
description: "GOVERNING (2026-06-26) — the lexical captures ONLY what THE VERSE says; any value with no basis in the verse itself (even if true from other verses/context/theology) is an ERROR and must be reversed out. Applies to ALL ve_lexical items. Divine: mention true if named, but don't overstate role."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ace57f3e-b52e-4cc7-adda-ef61148f91e0
---

GOVERNING RULE (researcher, 2026-06-26), two parts:

**(a) The lexical is strictly verse-bounded — applies to ALL items.** A ve_lexical value that has **no basis in the verse itself is an ERROR and must be reversed out**, even if it is true when read in the context of other verses. Cross-verse / contextual / theological truth is real but is **NOT the role of the lexical** — the whole intent of the lexical is a clear picture of what *this verse* says. (This is the same principle as [[feedback_faculty_only_if_explicit_or_inferred_on_verse]], now generalised to every item.)

**Why:** implied/imported evidence silently injects bias and "innovative assumptions" the verse doesn't support, corrupting the base picture. Context-reading belongs to a later synthesis layer, not the lexical.

**(b) Graded grounding (divine-involvement is the worked example):** distinguish two separable facts —
- **mention/presence** in the verse (e.g. an explicit divine name): if present, true → keep.
- **role** (agent/object/possessor/giver/addressee…): assert ONLY if the role is **clear in the verse**. If the verse names God but the role is not clear, record the mention but mark the **role unclear** — never overstate a role that isn't evident in the verse.

**How to apply:**
- For each item, define "basis in the verse" (divine-involvement: a divine name token in the verse; object: the object present; cause: the cause present; etc.). A value lacking that basis = reverse out (soft-delete, reversible, provenance-tagged).
- A pronoun whose referent is only knowable from context (e.g. "I" = God in divine speech) is NOT in-verse basis → reverse out / leave unresolved.
- Where the read-API (LLM) pass produced values, it is the prime suspect for implied evidence — audit its rows first (divine-involvement: 100% of ungrounded rows came from `divine_involvement_read_api`, the engine produced none).
- This implies a programme-wide grounding sweep across all items (each needs its own per-item grounding test). Divine-involvement done first; faculty already conforms (verse-grounded); the faculty `…-inferred-seat` tier must be re-checked under (b) for over-stated binding.

**2026-06-26 cleanup done:** divine-involvement 860 ungrounded role-assertions reversed; object-type=God-no-divine 383 + object-type-no-object 745 + cause-not-in-verse 259 reversed; **valence QUARANTINED** (26,993 rows — interpretive moral overlay, not verse evidence; doesn't track verse grammar; retained+flagged, not deleted). **Root cause insight:** valence was a previous **clustering driver**, so its interpretive bias shaped the cluster (M-code) structure itself — a likely source of the prior bias/diversions; future clustering must use verse-grounded signals only. Remaining identified fixes: **origin** (single-value, broken), **object-type taxonomy remap**, **divine-involvement rule (b)** role-clarity, **faculty seat-inferred tier** re-check.

Audits: `wa-divine-involvement-grounding-audit-v1-20260626.md`, `wa-overlay-bleeding-audit-and-reversals-v1-20260626.md`, `wa-ve-lexical-item-sanity-scan-v1-20260626.md`. Connects [[feedback_faculty_only_if_explicit_or_inferred_on_verse]], [[project_superstructure_eisegesis_validation_20260624]], [[feedback_verse_meaning_grounded_not_imported]], [[project_RESET_characteristics_to_movements_changeover]].
