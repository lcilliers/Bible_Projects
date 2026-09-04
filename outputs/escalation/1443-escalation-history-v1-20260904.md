# Escalation deep history

## #1443 — Recurring verse-structure finding has no checklist slot
type=issue source=Claude

**v1** (2026-09-03T10:37:17Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Recurring verse-structure finding has no checklist slot
> **comment (set this version):** Found in 3+ of 5 passages in the validation run (Workflow/Catalogue/1383-verse-lexical-window1-validation-applied-v1-20260903.md): Deut 6:7's four-infinitive merism (sit/walk/lie-down/rise); Prov 3:5-6's antithetic parallelism (trust-vs-lean); Gal 5:17's exact chiasm (flesh-against-Spirit / Spirit-against-flesh, confirmed cell-by-cell in the case-morph data in the calibration doc); John 1:4's life/light paired image. None of the checklist's current per-code items (idiom, pronoun, noun, verb, chain, causal, related-words, polarity, entity-link, data-quality, inert) has a slot for a VERSE-LEVEL rhetorical-structure fact that isn't reducible to any single code -- it's a relationship between multiple codes/positions, a different grain than everything else the checklist currently captures. Recurring across both languages and at least 3 genres in this run alone, not a one-off. Needs a decision: is this a new checklist item (verse/passage-level structure, a different grain than the per-code items), out of Window-1 scope entirely (a Window-2/synthesis concern), or something else? Not decided here -- previously only gestured at as 'reconciliation pass' material with no actual disposition, which is itself part of what prompted this correction.

**v2** (2026-09-03T14:48:47Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **resolution (set this version):** Split per researcher correction (2026-09-03): this finding was a mixture of word/verse work and HIB work, wrongly treated as one undifferentiated question. Resolved: DETECTING a structural pattern (merism/chiasm/antithetic-parallelism/paired-image -- a fact about how specific spans/codes in a verse relate to each other, derivable from morph/syntax data alone) is Stage 1's job -- added as a new verse_lexical_note note_type ('structural_pattern'), design doc revised (Section 5.3). INTERPRETING what such a pattern means for the inner being is Stage 2's job, out of Stage 1's table entirely -- not decided or built here, parked for Stage 2's own design cycle. Proposing this as the resolution -- confirm to close.

**v3** (2026-09-04T11:12:07Z, Researcher) state=completed next_action=approved assigned_to=Claude
> **comment (set this version):**  noted.  Spawn a new escalation from this to extract all verse word analytic methods 
