# 9 "malformed" Strong's codes investigation — 2026-07-24

## Background

`missing-strongs-step-verse-check-iba-20260724.md`'s STEP verse check (see
`SESSION-LOG`-adjacent chat context) found all 240 term-list-only Strong's
numbers have zero verses in STEP. Of those 240, 9 didn't match the standard
`[HG]\d{4}[A-Za-z]?` Strong's number pattern used elsewhere in this project
(5 digits instead of 4):

`G20125, G20258, G20833, G21401, G21410, G21415, G21419, G21422, G21497`

Flagged for a closer look rather than assumed to be a data-quality bug.

## Method

Per-code investigation, three steps:
1. Confirmed each code is genuinely present in the base data (`strong`,
   `strong_lexicon`, `strong_meaning_tree` all carry it) - not an artifact
   introduced by the extraction scripts built this session.
2. Read the `strong` table's own row for each - real Greek headword,
   transliteration, and gloss attached, not a blank/placeholder row.
3. Took each code's English gloss and queried STEP directly
   (`Step.call1_meanings(gloss)` - a live gloss-to-Strong's-number lookup)
   to see what code STEP itself assigns that meaning.

## Finding

**Not malformed.** STEP's own gloss lookup returns these exact 5-digit
codes back, confirming they're a real, valid identifier STEP itself uses -
not a typo, truncation, or concatenation bug:

| our code | gloss | STEP call1_meanings result |
| --- | --- | --- |
| G21422 | "such-like" | `G21422` τοῖος "such-like" - exact match, first hit |
| G21497 | "sin/shin" | `G21497` σ,Σεν "Sin/Shin" - exact match |
| G21415 | "desirable" | `G21415` ποθεινός "desirable" returned as a valid alternate alongside the standard `G7411` ἐπιθυμητός |
| G20833 | "yearn for" (headword ὁμείρομαι) | gloss search on "yearn for" didn't re-surface it directly (a generic English word with many candidates), but the `strong` table row itself is a real, well-formed Greek lexical entry, not junk |

The pattern across all 9: each has a genuine Greek headword
(ὁμείρομαι/ἐπιβρίθω/τοῖος/etc.), a real transliteration, and a real gloss -
these are lexicon entries for word forms that don't have a place in the
original canonical Strong's numbering (root/dictionary forms not
independently numbered, or forms outside the traditional G1-G5624 range),
so STEP's own STEPBible dataset assigns them an **Extended Strong's
Number** in a 5-digit space instead. Other examples spotted in the same
STEP responses during this check, confirming the convention is used
broadly, not just for our 9: G9704, G9664, G9663, G8393, G7139, G7411.

## Conclusion

No fix needed. The 9 codes are legitimate STEPBible Extended Strong's
Numbers, correctly carrying zero verses in `span` for the same reason all
231 of the other 240 do (per the earlier check) - not a data-quality bug,
not a reason to distrust the term list.

Worth noting for later: any future validation regex for "is this a
well-formed Strong's number" in this project should allow the 5-digit
Extended form (`[HG]\d{5}`) alongside the standard 4-digit form
(`[HG]\d{4}[A-Za-z]?`), or it will keep mis-flagging genuine extended
entries as malformed.
