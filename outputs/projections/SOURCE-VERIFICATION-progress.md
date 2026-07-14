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

## Locked verdict standards (stated so my OWN judgment cannot drift)

**D1 sense(101):** `correct` = faithfully conveys THIS span's word-meaning in context (same-verse manner/adverbials and completive synonym-pairs like "lie down and sleep" are allowed). `partial` = core meaning right but **welds a distinct parallel verb** (scope-bleed across the couplet) OR **imports content from another verse / an inferred overlay not lexically present**. `wrong` = mistaken meaning.

## Progress

| dim | book | verified | correct | partial | wrong | notes |
|---|---|---|---|---|---|---|
| D1 sense(101) | Psalms | 36 / 2168 | 25 | 11 | 0 | ~31% partial — systematic scope-bleed/import in poetic couplets |

### Running findings (patterns to watch)
- **D1 sense — dominant failure mode = scope-bleed / import** (not mistaken meaning; 0 wrong so far). The stored sense frequently (a) welds a distinct parallel verb from the couplet (Ps 2:10 sakal+yasar; Ps 4:2 ahav+baqash; Ps 4:4 amar+damam; Ps 5:3 arak+tsaphah; Ps 5:7 bo+shachah+yare), (b) imports content from an adjacent verse (Ps 5:2 "morning" is from v3), or (c) overlays an inferred inner-state not in the word (Ps 4:6 "crave"; Ps 5:8 "longing"; Ps 3:5 "in trust"). **Consequence:** the sense is not cleanly per-span — it can't always be attributed to the one lexical, which matters for any span-keyed analysis.
- **One substantive meaning question:** Ps 4:4 H7264 *ragaz* stored "be angry" — the Hebrew core is *tremble/be agitated* (DB gloss "to tremble"); "be angry" follows LXX/ESV but the verse context (be silent, ponder on beds) favours awe. Flagged for the researcher.
- **Role/Screen-0 questions surfaced in passing** (to resolve at D15): Ps 3:8 "salvation belongs to the LORD" (God's, not human IB); Ps 4:6 "good"; Ps 5:7 "enter"; Ps 5:8 petition to God.

### Method note
Every value read against: the verse text (ESV) + the Hebrew lemma transliteration + lexicon gloss + morphology (`_pull_verify_batch_v1`). STEP consulted where the DB lexicon is thin. Judgments are mine, recorded one-by-one in `ve_lexical_verification`. Pace is deliberately slow (genuine per-word reading); progress is durable and resumable — query the table any time.
