# #2381 — Multi-term units in verse_lexical and in the analysis: design v2 (2026-11-07)

Replaces v1. Input: the researcher's answers of 2026-11-07 (#2380: own gloss for affix codes, avoid consumer filters; #2381: (a) the sub-gloss of a strong must not be confused with the meaning of the multi-term item, (b) the multi-term meaning must not be lost and must be visible and clear; brackets alone change nothing because the multi-code construct reaches the analysis as separate lines; an affix whose meaning does not come through is not fixed by another column; the choices D1 to D5 are mine to make). Counts are live from `iba.db` today. Nothing is built; the build waits for approval (B:17, B:105). Collection and group content is model output, so inferential (B:4).

## 1. What the analysis shows today (real sheets built by `iba/app/lib/reading.py _sheets`)

Jer 23:12, position 3, one unit (STEP span `H2519 H9028 H9005 H9038`, rendering "slippery paths"). The sheet holds four lines:

| line | word shown | the code's own STEP gloss |
|---|---|---|
| 1 | slippery paths (H2519) | smoothness |
| 2 | slippery paths (H9028) | their |
| 3 | slippery paths (H9005) | to/for |
| 4 | slippery paths (H9038) | them |

Isa 32:6: `heart (H3820A)` and `heart (H9002)` (and); `busy (H6213A)` and `busy (H9023)` (his); `unsatisfied (H7324)` and `unsatisfied (H9005)` (to/for). Gen 43:27 position 7: `alive (H2416A)`, `still (H5750)`, `alive (H9043)` (he), `alive (H9008)` ([?]).

The fault is the one you named. The word shown on an affix line is the host's word, so an affix reads as the host ("heart (and)"), the unit appears as several lines of the same word, and the unit's meaning ("and his heart") is nowhere stated. `strong_variant` order is not word order, so even the order of the parts is lost.

Scale (live): 544,667 code lines; 378,166 units; 140,144 lines (25.7%) are affix codes; 285,424 lines sit in multi-code units.

## 2. The design: two levels, each readable on its own

**Code level (a row of `verse_lexical`, one code).** `surface` holds only what belongs to that code. The code's own sub-gloss is always shown with it (`strong.stepGloss`, read, not stored).

**Unit level (the span, the multi-term item).** New: its rendering, its parts in word order, its construct. Shown once.

### 2.1 `surface` rules (config: `cfg_setting lexical.span_surface`, no code default)

| Row | `surface` | `surface_kind` |
|---|---|---|
| single-code unit | its own word (unchanged) | `own` |
| the one content code of a unit with affixes ("heart" for H3820A with H9002, H9023) | the unit's word, because that word is its rendering (unchanged) | `own` |
| a content code of a unit with two or more content codes, where the #2326 look-back finds its exact word | that word (as today) | `own` |
| a content code of a unit with two or more content codes, no exact word found | the unit's rendering, unchanged, not guessed | `shared` |
| an affix code (prefix or suffix) in a shared unit | its own STEP gloss (and, to/for, in/on/with, [the], his, them ...), verbatim, never the host's word and never blank | `gloss` |

The bracketed STEP glosses ([the], [to], [emph.?], [-]) are kept as STEP gives them: they say what the code contributes (the article, an emphasis), and the unit's construct shows them in place ("the + old man"). Giving them NULL or leaving the host's word would hide that part of the unit.

### 2.2 New columns (each registered in `cfg_column`)

| Column | Holds |
|---|---|
| `unit_surface` | the unit's whole rendering, on every row of the unit (what `surface` holds today). Name chosen from your two. |
| `surface_kind` | `own`, `shared` or `gloss` (table above) |
| `unit_size` | codes in the unit |
| `unit_role` | `sole`, `head` (the only content code), `content_part` (one of several content codes), `prefix`, `suffix` |

Role of an affix comes from its morph class, which is recorded and checked: prefixes carry morph HC (conjunction, H9002), HTd (article, H9009), HR and HRd (preposition, H9003 to H9008); suffixes carry HSp (pronominal suffix, H9020 and up). The classes are a config setting, not code. Word order of a unit is prefixes, then content parts, then suffixes (Hebrew morphology), with `code_ordinal` as the tie-break inside a group.

### 2.3 The construct, derived and shown

Built at read time from role and own gloss, never stored twice: Jer 23:12 position 3 reads **"to/for + smoothness + their + them"** (prefix H9005, head H2519, suffixes H9028 and H9038) with the rendering "slippery paths" beside it. Isa 32:6 position 3 reads **"and + heart"** (rendering "heart"); position 4 reads **"to make: do + his"** (rendering "busy"). Nothing of an affix's meaning is lost, and the head's own gloss and the unit's rendering are two separately labelled facts, which is your (a) and (b).

### 2.4 One reader, so no consumer rebuilds the rule

`iba/app/lib/lexical.py` gains `unit_view(conn, verse_ids)`: per unit, its rendering, its parts in word order (role, own gloss, surface, `verse_lexical.id`) and its construct. The reading sheet, the scope resolver and the reports call it. Observations and nodes still attach to a part by `verse_lexical.id`, so a pronoun suffix or a preposition can carry an observation when it matters (69 nodes already do).

## 3. What changes in the analysis

| Analysis step | Before | After |
|---|---|---|
| reading sheet (`reading.py _sheets`) | one line per code, host word on affix lines | one line per unit: rendering, construct, parts each with own gloss and role; the unit's head carries the M and T hints; affix parts are listed, not separate lines of the host's word. 544,667 code lines become 378,166 unit lines (30.6% fewer); affix lines (25.7% of all) become parts |
| scope resolver (`versescope.py`) | a word enters through the surface of any code | a word enters through `surface` of rows whose kind is `own`; a `shared` or `gloss` row never brings a verse in as the host's word |
| surface cycle (`surfacemap.py`, `surfacestructure.py` loaders) | surface text from every row | an English word of the ESV comes from `own` and `shared` rows; `gloss` rows (affix glosses such as to/for) are not ESV words and are not terms. One rule in the loaders, read from the column the source set |
| node and observation matching (`noderesolve.py`, `observationrecord.py`) | `(strong, surface)` with the host's word | `(strong, surface)` with the code's own surface; the 69 affix nodes re-point by `verse_lexical_id` |
| `occurrence_surfaces` | re-derives the rule | reads the columns; the second copy of the rule goes |

Existing M-coded pairs in `surface_subgroup` and existing nodes on `shared` rows are unchanged, because `shared` rows keep their surface.

## 4. D1 to D5, decided (with the reason)

- **D1 scope: affix codes now, and a content code of a multi-content unit is `own` only where its word is found exactly, else `shared`.** A word cannot be assigned from STEP's data to one of two content codes without guessing (B:19), so the design shows the unit once with each code's own gloss next to it: the meaning is visible and not attributed wrongly. A closed list of function-word codes is not needed; they appear as parts with their own gloss.
- **D2 bracketed glosses: kept as STEP gives them, shown in the construct.** The analysis issue was the separate host-worded lines, which the unit line removes.
- **D3 affix-only units** (1,459 units): each code has its own gloss and role; the unit has no head; the construct reads from the parts ("from + [emphasis]").
- **D4 name: `unit_surface`.**
- **D5 re-judging: none.** The prompts send only the English word (`{surface}`, `{a}`, `{b}`, `{w}`; checked in all nine active prompts), so group, base and collection judgements are about the word alone and cannot change. All 6,066 surface terms have a content row; 3,564 also touch affix rows; none disappears. What changes is the evidence read from the join: affix strongs leave the collections' strong and verse evidence (5,908 of the 25,715 rows of the #2379 export). Counts and collection states are recomputed; no model call is made.

## 5. Build, in stages (each ends with a check recorded in the escalation)

1. **Data layer.** Schema (4 columns, `cfg_column`, enums `surface_kind`, `unit_role`), settings, `lexical.py` rules, back-fill by re-running `lexical.build` over all 544,667 rows keeping ids (job started outside the session, B:125, log under `Logs/`). Check: kinds and roles sum to 544,667; 131,024 affix rows in shared units are `gloss`; no live id lost; 69 affix nodes re-pointed; the Greek exception (G9315, G9577 are content codes) in config.
2. **Unit reader and the analysis.** `unit_view`, the sheet, the scope resolver, `occurrence_surfaces`, reports. Check: Jer 23:12, Isa 32:6, Gen 43:27 and Job 21:19 sheets as in section 1, by hand against STEP.
3. **Surface cycle.** Loader rule, recompute of counts and links. Check: 6,066 terms unchanged; the #2379 export rebuilt with no affix strong as a host-worded member.
4. **Documents and tests.** BUILD.md, USER-GUIDE, `cfg_table`/`cfg_column`, worksheet if a parameter changes; test plan run per case (each `surface_kind` and `unit_role`, each rule on and off on a fixture verse set, idempotent rerun, real verses above, a synthetic unit with two content codes).

## 6. Not yet established

- Which prompt or generator consumes the reading sheet's `surfaces` list, and what it needs in place of the per-code lines; traced at the start of stage 2 and reported before any change to it.
- The share of multi-content units where the look-back finds exact words (it changed 1,882 rows in October; the rest stay `shared`).
- Whether any collection holds one of the 28 function-word surfaces (only matters if a `gloss` row's text equals one).
- Run time of the full `lexical.build`.
- Word order inside a unit rests on the morph classes; a unit with a code of no class is listed in order of `code_ordinal` and reported.

## 7. What approval means

Approve this design (and the choices in section 4) and I build stages 1 to 4 in order, reporting after each. Say if the sheet in section 3 is not the shape you want before stage 2 starts: that is the one stage whose shape is yours.
