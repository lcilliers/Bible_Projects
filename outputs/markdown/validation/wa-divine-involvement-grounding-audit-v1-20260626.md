# divine-involvement — grounding audit (is it verse-evidence or assumption?)

- **File:** wa-divine-involvement-grounding-audit-v1-20260626.md · **2026-06-26 · Author:** Claude Code · read-only.
- **Researcher's suspicion:** divine-involvement carries a lot of bias / innovative assumption that has nothing to do with verse evidence.
- **Verdict:** substantiated, with nuance. ~1 in 5 resolved values is not anchored to any divine reference in the verse, and every ungrounded row was produced by the LLM read pass, none by the engine. The field is also an interpretive role-overlay whose *correctness* is unverified even where it is grounded.

## 1. What the field is + where it comes from
- ve_nr 8. Values: agent, object, possessor, addressee, giver, UNRESOLVED.
- **Two provenances:** `v2_engine_iter1` (6,588 rows — mostly UNRESOLVED) + `divine_involvement_read_api` (4,599 rows — the resolved roles, note = "resolved by read pass").
- So the *resolved* content is overwhelmingly an **LLM read-pass overlay**, not a mechanical derivation — the layer most exposed to theological assumption.

## 2. Grounding test (excl T2)
A role assignment is "grounded" if the verse it sits on actually contains an explicit divine name (strict set: YHWH, Elohim, El, Eloah, Adonai, Yah, Elyon, Shaddai, theos).

| | count | share of resolved |
|---|---:|---:|
| resolved divine-involvement | 5,796 | — |
| grounded (divine name in the verse) | 4,718 | 81% |
| ungrounded (no divine name in verse) | 1,078 | 19% |
| — but divine ref in adjacent context | 90 | — |
| — **no divine ref in verse or context** | **988** | **17%** |

- **All 1,078 ungrounded rows are `divine_involvement_read_api`; the engine produced none.**
- Pure-assumption set by role: agent 486 · possessor 184 · addressee 119 · object 109 · giver 90.

## 3. Concrete examples (ungrounded)
- **Legitimate (God is the speaker, pronoun):** 1Ch 17:13 "I will not take my steadfast love from him" → possessor=God (God is the "I"); 1Ch 28:6 "I have chosen him" → agent=God. Defensible context-reads, but **not evidenced in the verse text**.
- **Pure assumption (no divine actor at all):** 1Ch 29:28 "Then he [David] died … full of days, riches, and honor" → tagged `giver` (God gave the riches/honor). The verse has no divine reference and no divine action — "riches come from God" is imported doctrine. This is the bias the researcher flagged.

## 4. Two honest caveats
1. **17% is an upper bound** on pure assumption. Some of the 988 are divine-speech pronoun cases (God = "I"/"you"/"him") my English-context check can't detect. The genuine-assumption floor is lower but non-zero and real.
2. **Grounding ≠ correctness.** The 81% "grounded" only means a divine name appears somewhere in the verse. It does not verify that (a) the assigned role (agent/object/possessor/giver) is right, or (b) God's involvement actually bears on the inner-being term rather than being incidental to the verse. Role-correctness is a separate, deeper audit.

## 5. Options (for decision — nothing actioned yet)
1. **Restrict to grounded-only.** Keep divine-involvement only where a divine name is in the verse; soft-delete/flag the 1,078 ungrounded read-pass rows. Conservative, evidence-only. (Mirrors the faculty rule.)
2. **Two-tier provenance** (like faculty's explicit/inferred). Keep all, but split: `divine-involvement-explicit` (divine name in verse) vs `divine-involvement-inferred` (no divine name) — inference labeled and independently removable.
3. **Full verse-grounded reset.** Re-derive mechanically: assert divine-involvement only when a divine name co-occurs with (and grammatically relates to) the inner-being term; everything else UNRESOLVED/empty; defer role-correctness to a depth pass.
4. **Role-correctness sub-audit first.** Before deciding, sample N grounded rows and check whether the assigned role matches the verse — to learn whether the problem is only the ungrounded 19% or also wrong roles within the 81%.

**Recommendation:** given the rule already set for faculty (verse-evidence only), option 1 or 3 fits the programme; but I'd run option 4's quick role-correctness sample first so the decision is made on the full extent of the problem, not just the grounding slice.

## 6. Provenance / repro
- Read-only. divine names matched against `verse_morphology` (canonical zero-padded Strong's); context via `wa_verse_records.context_before/after`.
- Related: `feedback_faculty_only_if_explicit_or_inferred_on_verse` (the verse-evidence rule), `wa-faculty-state-diagnosis-v1-20260626.md`.
