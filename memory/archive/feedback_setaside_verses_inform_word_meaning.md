---
name: feedback-setaside-verses-inform-word-meaning
description: "Set-aside verses (non-inner-being uses of a term) still inform what the word MEANS. They are not noise; they are the word's semantic range that shapes how the inner-being uses are read."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7401fa55-df1f-434c-9ff3-b60b0138422f
---

A verse that is SET-ASIDE for a term because it carries no inner-being content is **still telling us what the word means**. Setting it aside removes it from the cluster's analytical corpus, but it does not remove its evidential weight on the word's semantic profile.

**The researcher's observation (2026-05-18):** H2896A tov has 75 terse set-asides in M04 ("physical_only" and "no_inner_being"). Tov occurs 500+ times across the corpus. The 75 set-asides — plus the much larger set of non-M04 tov uses — demonstrate the word's actual semantic range: "good land", "good appearance", "good news", evaluative goodness, etc. By only studying tov's inner-being subset in M04, we may miss how tov's full polysemy shapes the inner-being uses.

**Why this matters:**

- Cluster analysis carves verses by inner-being relevance; word study analyses a term's full semantic profile.
- The cluster's set-aside record holds analytically valuable information about each term's non-inner-being senses, but currently this information lives only in `verse_context.set_aside_reason` text — not in a structured way that a word study can consume.
- Set-aside reasons should ideally be evidence-based and verse-specific (per §4.5.1), so they can be aggregated to characterise the term's semantic spread.
- A word study (Session C word study) for H2896A tov, or a term-meaning panel in Session B / Session C, should reference all 500+ occurrences and the way each sense relates to the inner-being subset — not just the M04 verses.

**How to apply:**

- Don't treat set-aside as "throw-away." Treat it as "this verse is for the term's semantic record, not the cluster's analytical corpus."
- When authoring set_aside_reason text, write it as a contribution to the term's meaning record (per-verse, evidence-based) — not as a curt dismissal.
- When designing a cluster's findings (T1.2.1 sub-group descriptions, T2 term-meaning panels), reference the set-aside corpus where it illuminates the inner-being-relevant uses.
- The audit's TERSE-SETASIDE check (§4.5.1 compliance) is also a meaning-record-quality check.

**Programme implication (open):** the cluster pipeline currently doesn't have a built-in "word's full semantic profile" view that aggregates the cluster's relevant uses + the cluster's set-aside uses + the term's other-cluster / out-of-scope uses. A future enhancement might add this — e.g., a per-term meaning panel in Session C word studies, or a query that surfaces the full profile to AI during Phase 3 / Phase 5 / Phase 9 synthesis.

Related: [[feedback-inner-being-full-scope]] (set-aside criteria are stricter under v2_5 — only no-inner-being-state qualifies, not "no theological framing").
