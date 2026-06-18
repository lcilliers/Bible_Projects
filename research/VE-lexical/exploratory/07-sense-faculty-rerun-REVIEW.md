# Sense + faculty value-rerun — for review (2026-06-15)

> Done per direction while you're out: fixed **sense** (per-occurrence subgloss), kept **sense+type paired**, re-derived **faculty** against the signal-list in the verse context (not generic). **Meaning NOT touched** (as instructed). All reversible. Stopping here for your review.

## 1. Sense (VE1) — set to the per-occurrence subgloss
`scripts/_apply_sense_from_subgloss.py`. Of 29,546 VE1 rows: **28,355 corrected** to `wa_verse_term_links.step_subgloss_label`, **466 already correct**, **725 → UNRESOLVED** (no per-occurrence subgloss source — sub-entry join gaps). The prior value is preserved in `notes` (`sense<-subgloss; was: …`).

**Why it changed so much:** the migrated values were **narrative read-senses** (e.g. *"terror of death; dread that enslaves"*, *"reverential awe; holy wonder"*) — that is **meaning**, not sense. The actual STEP sense is **"fear"**. Sense is now the clean per-occurrence subgloss.

**To review:**
- For poly-sense / coarse-ceiling terms the subgloss is uniform (e.g. *fobos* → "fear" everywhere). That's the mechanical floor; the nuance moves to the meaning. Confirm that's the intended behaviour, or where a finer sense is wanted.
- The 725 UNRESOLVED — sub-entry term_inv linkage; worth a look.

## 2. Sense + type — paired
Both sit on the same `verse_context_id` (one sense + one type per term-in-verse today), so they are implicitly paired. No type values were changed. The **multi sense+type pairs** (a verse with >1 sense, each its own type) is a structural capability for the next pass, not present in the current data.

## 3. Faculty (VE7) — RE-DERIVED against the verse context (the fix you flagged)
`scripts/_apply_faculty_rederive_v1.py`. The previous faculties were **generic, not tested against the verse**. Replaced: **14,490 generic retired → 25,154 rule-derived** rows (one per faculty actually signalled). **Present-only** — a faculty is assigned only where one of its signal words occurs (word-boundary) in the term gloss or the verse text.

| confidence | source | rows | meaning |
|---|---|---|---|
| **high** | direct (the term's own gloss is a faculty word) | **7,694** | the term *is* that faculty act (e.g. a "know" term → cognition) |
| **candidate** | indirect (a faculty word appears in the verse) | **17,460** | the verse engages the faculty — but may not be *this* term → **review** |

Distribution: affect 7,836 · perception 5,380 · cognition 4,513 · moral-evaluation 3,008 · conscience 1,648 · memory 808 · volition 734 · relational 689 · creativity 301 · agency 237. Each row's `notes` shows `direct/indirect: <matched words>`.

**To review (this is iteration 1):**
- **The indirect (17,460) are the risk** — a faculty word anywhere in a verse currently assigns that faculty to *every* analysed term in the verse (verse-level, not term-specific). This is the main thing to validate/tighten (restrict to faculty words syntactically tied to the term).
- **Signal-lists are seed lists** (`FACULTIES` in the script) — refine words; watch overlaps (love→affect; guilt→conscience+moral; make→creativity).
- The direct (7,694) are solid (term-gloss based).

## Reversibility
- Sense: prior value in `notes`; or restore from the soft-deleted source findings.
- Faculty: `UPDATE ve_lexical SET delete_flagged=0 WHERE ve_nr=7 AND source_provenance IS NULL` (restore generic) + `…delete_flagged=1 WHERE source_provenance='rule_v1'` (drop rule rows).

## Not done (as instructed)
- **Meaning** (the templated narrative) — left for after you've reviewed sense + faculty.
- Type re-derivation, the other VE fields' value-validation — pending your review of the approach on these two.
