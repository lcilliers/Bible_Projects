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

**DECISION (researcher 2026-06-26): QUARANTINE (option 3).** Done — 26,993 active valence rows snapshotted to `ve_lexical_valence_quarantine_20260626`, `delete_flagged=1` + QUARANTINE note (excluded from active reads, retained, recoverable). DB backup `bible_research_pre-valence-quarantine_20260626.db`.

### Root-cause insight (researcher, 2026-06-26)
**Valence was a clustering driver in the previous work** — so its interpretive bias was not confined to a field; it shaped the cluster (M-code) structure itself. This is a likely root cause of the bias/diversions in the prior clustering, and reinforces why the RESET treats the clusters as scaffolding/legacy (`project_RESET_characteristics_to_movements_changeover`). Any future clustering must be driven by verse-grounded signals only, never an interpretive overlay.

## 4. Remaining identified fixes — ALL CLEARED 2026-06-26 (verse is king)
Script `_apply_clear_remaining_lexical_fixes_v1_20260626.py`; backup `bible_research_pre-remaining-fixes_20260626.db`; per-fix snapshots. All reversible.
- 🔴 **origin** — ✅ QUARANTINED (3,623 rows → `ve_lexical_origin_quarantine_20260626`, flagged out). Single non-grounded interpretive stamp.
- 🟠 **object-type taxonomy** — ✅ REMAPPED. `{thing, abstract, thing/abstract}` (9,534) → `impersonal`. Clean vocab now: impersonal · person · God · situation · spiritual-being · threat. Snapshot `ve_lexical_objtype_premap_20260626`. (Residual: some person-objects under the old engine hedge remain coarsely typed — accuracy, not grounding; future re-derive from the object noun.)
- **divine-involvement rule (b)** — ✅ DONE. 5,187 grounded roles demoted to `present` (mention is verse-true; role not mechanically clear). Roles preserved in `ve_lexical_divinv_roles_premap_20260626`. UNRESOLVED (5,140) untouched.
- **faculty `…-inferred-seat`** — ✅ REVERSED. 1,492 proximity-inferred seat faculties soft-deleted (`ve_lexical_faculty_seat_reverse_20260626`); faculty now purely explicit faculty-words (20,636). Seats get a faculty only where the verse names one.
- (Known backlog, not a grounding fix: divine-involvement ~46% UNRESOLVED.)

## 5. Still open
- divine-involvement **rule (b)** role-clarity on the 5,187 grounded rows (mention true, role only if clear).
- faculty `…-inferred-seat` tier (1,492) — re-check under (b) for over-stated binding.
- Provenance/repro: scripts `_apply_divine_involvement_reverse_ungrounded_v1_20260626.py`, `_apply_reverse_ungrounded_overlays_v1_20260626.py`; divine audit `wa-divine-involvement-grounding-audit-v1-20260626.md`.
