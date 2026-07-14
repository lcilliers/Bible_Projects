# Source-verification of every lexical dimension against the source

**Started 2026-07-14.** Task (researcher): check each dimension's stored value **against the source** — verse +
Hebrew/Greek lemma + morphology, **read in passage context** (the method's read rule). Judgment is mine, per value.

## Acceptance-sampling protocol (researcher, 2026-07-14)
- **~4,137 lexicals per dense dimension** (Psalms 2,168 + Proverbs 1,969).
- **Sample = 200 random lexicals per dimension, scattered across both books** (census if a dim has <200: source=123, prohibition=9). Samples are **disjoint across dimensions** (no lexical tests more than one dimension) and **fixed up-front** (seed 20260714, table `ve_verification_sample`) so they can't be cherry-picked.
- **Accept** a dimension if its 200 are verified with **0 errors** → ~95% confidence its true defect rate is <~1.5% (rule of three, 3/200).
- **Any error → the dimension FAILS**, and per the researcher a failure triggers a **full retest of all dimensions**.
- **Verdict is BINARY** (researcher, 2026-07-14): **correct** = compliant with **all** the rules for that dimension; **wrong** = missed something. No "partial", no deferring the call to the researcher — **check against the written rules**, not intuition or "it looks right".

**Rules come from the catalogue** `Workflow/Catalogue/wa-ve-lexical-catalogue-v1-20260702.md` (per-dimension definition + the 2026-07-14 mandatory rules) and the cycle doc. For **D1 sense(101)** the rule is exact: *the per-occurrence sense = the STEP subgloss = the meaning of the WORD in context* (§2/§9). Authority = STEP + `lexicon.gloss`/morphology, not memory.

- **Verdict store (durable):** `ve_lexical_verification`. **Sample store:** `ve_verification_sample`. **Puller:** `_pull_verify_batch_v1 --ve <nr> --sample` (shows the whole passage, focus verse `>>`; resumable).

## Dimension order (ve_nr = D-number)

D1 sense(101) · D2 type(102) · D3 source(103) · D4 seat(104) · D5 bearer(105) · D6 operation(106) ·
D7 target(107) · D8 manner(108) · D9 intensity(109) · D10 specifier(110) · D11 effect(111) ·
D12 coupling(112) · D13 prohibition(113) · D14 reading(114) · D15 role(115) · D16 locus(116) ·
D17 device(117) · D18 direction(118).

Scope per dimension: Psalms 2,168 lexicals, then Proverbs 1,969. (D3 source and D13 prohibition are sparse — only the lexicals that carry them.)

## Locked verdict standard — PASSAGE-CONTEXT (corrected 2026-07-14)

**⚠ Standard corrected.** The read rule is: *the characteristic is read in the context of its PASSAGE, never the clause alone* (`wa-characteristic-role-lexical-cycle-authoritative-v1` line 100; the whole method is passage-anchored). My first pass graded clause/verse-atomically and wrongly scored 11 as "partial" for scope-bleed/import — content that the **passage legitimately supplies** (the method even names the Ps 3:5 "trust" case, line 111). Corrected.

**D1 sense(101):** `correct` = faithfully conveys the characteristic's meaning **as read in its passage** (contextual content from anywhere in the passage is legitimate; the value need not be clause-atomic). `partial` = a genuine mis-scope *within the passage frame* (e.g. attributes another indexed span's distinct content). `wrong` = mistaken meaning even in passage context. Interpretive/role questions are noted as **researcher-flags**, not defects.

The puller (`_pull_verify_batch_v1`) now shows the **whole passage** (focus verse marked `>>`) so every judgment is made in the correct frame.

## Progress

### SCOREBOARD (updated 2026-07-14; live table `ve_dimension_scoreboard`)

Protocol: test each dimension's 200-sample against its **written rule**; **first violation → FAILED, move on**; pass only if all 200 clean (95%).

| D | ve_nr | dimension | status | checked | first violation |
|---|---|---|---|---|---|
| D1 | 101 | sense | ❌ FAILED | 46 | Pro 28:12 — records interpretation/effect, not the word's subgloss |
| D2 | 102 | type | ❌ FAILED | 14 | Pro 21:30 — faculty vocab (cognition/affect…), not the rule's action/status/quality |
| D3 | 103 | source | ❌ FAILED | 8 | Psa 42:5 — target-direction pair (term→object) in the source dim |
| D4 | 104 | seat | ⏳ in progress | 16 | — (all `none`, correct so far) |
| D5 | 105 | bearer | ⏳ in progress | 4 | — |
| D6 | 106 | operation | ⏳ in progress | 5 | — |
| D7 | 107 | target | ⏳ in progress | 4 | — |
| D8 | 108 | manner | ⏳ in progress | 4 | — |
| D9 | 109 | intensity | ❌ FAILED | 12 | Psa 1:2 — non-`none` values truncated mid-word (regex cap) |
| D10 | 110 | specifier | ⏳ in progress | 6 | — (format clean; correctness unverified) |
| D11 | 111 | effect | ❌ FAILED | 6 | Pro 16:24 — malformed truncated value |
| D12 | 112 | coupling | ❌ FAILED | 4 | Pro 9:16 — semantic reading, not a morphological weld |
| D13 | 113 | prohibition | ⏳ in progress | 4/9 | — (clean negations) |
| D14 | 114 | reading | ⏳ in progress | 5 | — (genuine rich reads) |
| D15 | 115 | role | ⏳ in progress | 4 | — (Screen-0 God-act mis-roles seen elsewhere → likely fails) |
| D16 | 116 | locus | ⏳ in progress | 5 | — (drift-suspect from prior audit) |
| D17 | 117 | device | ❌ FAILED | 12 | Pro 28:14 — malformed `literal — 28:14b).`; literal on figurative verses |
| D18 | 118 | direction | ❌ FAILED | 10 | Pro 16:9 — truncated + wrong vector (heart-planning tagged toward-god) |

**Result so far: 8 dimensions FAILED, 10 in progress, 0 passed the 95% mark.** Every dimension conclusively tested has failed. The 8 failures split into two causes: (a) the **regex-derived** dims I built (intensity, effect, device, direction) fail on malformed/truncated values; (b) **core read dims** fail on rule-compliance (sense records interpretation not the word; type uses the wrong vocabulary; source stores target-direction pairs; coupling stores semantic readings not morphological welds). The 10 in progress are mostly the genuine read dims + sparse dims; a full 200-check is needed to pass any of them.

**D1 FAILED — 5 confirmed rule-violations (sense ≠ the word's per-occurrence subgloss; it records the char's interpretive function/effect):**
- Pro 28:12 *tsaddiq* (righteous) → "public good…" (effect)
- Ps 5:8 *yashar* (make straight) → "longing…" (inferred inner-state)
- Ps 4:6 *tov* (good) → "the many who crave…" (inferred inner-state)
- Ps 5:9 *lashon* (tongue) → "grave-throated deceit" (function)
- Ps 4:4 *ragaz* Qal (tremble; STEP-confirmed) → "be angry" (wrong stem-sense)

**Consequence (researcher protocol):** a failed dimension → **all dimensions must be retested**. The sense layer records interpretation where the rule requires the word's meaning — a systematic defect, not a stray typo.

**Correction to my own record:** my earlier "36/36 correct in passage context" was itself a rule-failure — I judged against a passage-reading frame when the sense rule is the STEP subgloss. Checking against the *written rule* (as instructed) surfaced defects my intuition had masked.

### Running findings
- **D1 sense — clean so far under the passage rule: 36/36 correct, 0 wrong.** (My earlier "31% partial" was a verification-standard error, not a data defect — see the corrected standard above.)
- **1 researcher-flag (interpretive, not a defect):** Ps 4:4 H7264 *ragaz* stored "be angry" — defensible (ESV/LXX), but Hebrew core = *tremble/be agitated* and the passage counsels stillness; "tremble/stand in awe" is a live alternative for your ruling.
- **Role/Screen-0 questions parked for D15** (not sense defects): Ps 3:8 "salvation belongs to the LORD" (God's, not human IB); Ps 4:6 "good"; Ps 5:7 "enter"; Ps 5:9 tongue/throat possible span-merge.

### Method note
Every value read against: the verse text (ESV) + the Hebrew lemma transliteration + lexicon gloss + morphology (`_pull_verify_batch_v1`). STEP consulted where the DB lexicon is thin. Judgments are mine, recorded one-by-one in `ve_lexical_verification`. Pace is deliberately slow (genuine per-word reading); progress is durable and resumable — query the table any time.
