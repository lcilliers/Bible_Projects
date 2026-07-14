# Source-verification of every lexical dimension against the source

**Started 2026-07-14.** Task (researcher): take each dimension for each lexical in Psalms + Proverbs and check
the value **against the source** — no shortcuts, no statistics, no assumptions. Order = **dimension-major**:
D1 for every lexical, then D2 for every lexical, and so on. The judgment is **mine, per value, read against
the verse + Hebrew/Greek lemma + morphology** (STEP when the DB lexicon is insufficient). Scripts only pull
the source and store my verdicts; they compute nothing about correctness.

- **Verdict store (durable):** DB table `ve_lexical_verification` (span, ve_nr, stored_value, verdict, correct_value, note, source_checked, checked_at). Resumable.
- **Puller:** `scripts/_pull_verify_batch_v1_20260714.py --book <id> --ve <nr> --limit N` (skips already-verified).
- **Verdicts:** `correct` · `partial` (right idea, imprecise/conflated) · `wrong`.

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

| dim | book | verified | correct | partial | wrong | researcher-flags |
|---|---|---|---|---|---|---|
| D1 sense(101) | Psalms | 36 / 2168 | 36 | 0 | 0 | 1 (Ps 4:4 ragaz) |

### Running findings
- **D1 sense — clean so far under the passage rule: 36/36 correct, 0 wrong.** (My earlier "31% partial" was a verification-standard error, not a data defect — see the corrected standard above.)
- **1 researcher-flag (interpretive, not a defect):** Ps 4:4 H7264 *ragaz* stored "be angry" — defensible (ESV/LXX), but Hebrew core = *tremble/be agitated* and the passage counsels stillness; "tremble/stand in awe" is a live alternative for your ruling.
- **Role/Screen-0 questions parked for D15** (not sense defects): Ps 3:8 "salvation belongs to the LORD" (God's, not human IB); Ps 4:6 "good"; Ps 5:7 "enter"; Ps 5:9 tongue/throat possible span-merge.

### Method note
Every value read against: the verse text (ESV) + the Hebrew lemma transliteration + lexicon gloss + morphology (`_pull_verify_batch_v1`). STEP consulted where the DB lexicon is thin. Judgments are mine, recorded one-by-one in `ve_lexical_verification`. Pace is deliberately slow (genuine per-word reading); progress is durable and resumable — query the table any time.
