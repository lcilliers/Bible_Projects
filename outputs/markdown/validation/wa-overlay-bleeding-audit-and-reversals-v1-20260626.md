# Read-API overlay "bleeding" — audit + reversals (verse-bounded rule)

- **File:** wa-overlay-bleeding-audit-and-reversals-v1-20260626.md · **2026-06-26 · Author:** Claude Code.
- **Rule applied:** the lexical captures ONLY what THE VERSE says; a value with no basis in the verse is an error → reverse out (researcher 2026-06-26). `feedback_lexical_strictly_verse_bounded_no_implied_evidence`.

## 1. Where the bleeding is (provenance map)
Engine-derived items (`sense, type, object, experiencer, how, from-source, cause_clause, compound, purpose, instrument, quality-bearer, operation, intensity, relational, immediate-response, isolable, discovery`) are grounded by construction. The **read-API (LLM) overlays** are the bleeding suspects:

| item | read-API rows | engine rows |
|---|---:|---:|
| valence | 26,788 | 205 |
| object-type | 12,102 | 7,926 |
| divine-involvement | 3,739 | 6,588 |
| cause | 3,431 | 2,264 |
| location | 31 | 6,633 |

## 2. Reversals done this session (all reversible — backups + snapshots + soft-delete)
- **divine-involvement:** 860 ungrounded role assertions (no divine name in verse). Snapshot `ve_lexical_divinv_pre_reverse_20260626`. (rule a; role-clarity rule b still pending on the 5,187 grounded.)
- **object-type = "God" with no divine name in verse:** 383.
- **object-type with no `object` on the unit (type with no referent):** 745.
- **cause (read-API) sharing no content word with the verse:** 259.
- **location (read-API) seat-not-in-verse:** 0 (all 31 grounded).
- Combined overlay snapshot `ve_lexical_overlay_reverse_20260626` (1,387 rows). DB backups: `bible_research_pre-divinv-reverse_20260626.db`, `…_pre-overlay-reverse_20260626.db`.

## 3. valence — the largest bleeding (DECISION NEEDED)
`valence` is **99.2% read-API** (26,788/26,993) and is an **interpretive moral-evaluation overlay, not verse evidence**:
- Imperative/jussive/cohortative grammar rate by value: commanded 28% · forbidden 29% · righteous 22% · sinful 30% · **neutral 29%**. Identical base rate → valence **does not track verse grammar**; "commanded" is no more on a real command than "neutral".
- Samples: Gen 3:10 "I was afraid because I was naked" → `sinful` (verse states fear; sinful = imported); Exo 18:21 "men who fear God" → `commanded` (descriptive, not a command).
- Under rule (a) almost the whole field is implied evidence. `righteous`/`sinful` (13,236) are moral judgements never stated by the verse; `commanded`/`forbidden` (3,253) don't track command grammar; `neutral` (10,504) asserts moral-neutrality (a weak judgement).

### Disposition options
1. **Reverse out valence wholesale** (treat as interpretive overlay, fully out per rule a). Cleanest; re-derive later as a grounded field if wanted. ~26.8k rows soft-deleted (reversible).
2. **Reverse the evaluative bulk, re-derive grounded deontic.** Remove righteous/sinful/neutral + ungrounded commanded; keep/re-derive only `forbidden`/`commanded` where the inner-being TERM itself stands in an imperative/prohibition (e.g. "Fear not" → fear forbidden). Smaller grounded remnant; needs a derivation pass.
3. **Quarantine, don't delete.** Move valence to a clearly-labelled `valence-interpretive` provenance so it never reads as verse-evidence, pending a later decision.

**Recommendation:** option 1 — valence as stored is not verse-grounded and doesn't even track grammar; reverse it out now (reversible), and if a moral/deontic signal is wanted later, build it as a grammar-grounded field (option 2's remnant) from scratch. Awaiting your call before touching 26.8k rows.

## 4. Still open
- divine-involvement **rule (b)** role-clarity on the 5,187 grounded rows (mention true, role only if clear).
- faculty `…-inferred-seat` tier (1,492) — re-check under (b) for over-stated binding.
- Provenance/repro: scripts `_apply_divine_involvement_reverse_ungrounded_v1_20260626.py`, `_apply_reverse_ungrounded_overlays_v1_20260626.py`; divine audit `wa-divine-involvement-grounding-audit-v1-20260626.md`.
