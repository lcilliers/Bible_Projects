# WR-19 Investigation — Parse Warnings (soul, registry 182)
**Date:** 2026-03-23  
**Source:** `wa_meaning_parsed` join `wa_term_inventory`, file_id=36  
**Trigger:** WR-19 audit check fired REVIEW — 16 terms have `parse_warnings` with no corresponding `NOTE` quality flag

---

## What WR-19 checks

For every term in the word study that has a `parse_warnings` value in `wa_meaning_parsed`:  
does a `NOTE` quality flag exist for that term in `wa_data_quality_flags`?  
If not → WR-19 fires REVIEW so the researcher knows there are low-confidence meaning records with no visible marker on the term.

---

## The warning: PROSE_ONLY

All 16 terms carry **exactly one warning: `PROSE_ONLY`**.

`PROSE_ONLY` is set by `meaning_parser.py` when the STEP `medium_def` field for a term
contains **no structured sense numbering** — no `1.`, `2.`, Hiphil/Niphal/Qal stem labels,
no domain brackets, no subdivisions. The parser captured the entire definition as a single
prose block and stored it as one sense record.

The data is not wrong. It is what STEP provides. The issue is that `flag_engine` did not
write a `NOTE` flag to document this, so WR-19 has no flag to find when it checks.

---

## The 16 terms

| Code | Gloss | Occurrences | Senses stored | Parsed definition (truncated) |
|---|---|---|---|---|
| G0674 | to faint | 1 | 1 | "to faint (some translate 'to die') — primarily to breathe out, faint away, die; metaphorically…" |
| G0895 | lifeless | 1 | 1 | "lifeless, inanimate — void of life, or sense, inanimate, 1Cor. 14:7" |
| G1374 | double-minded | 2 | 1 | "double-minded, inconstant, fickle, Jas. 1:8; 4:8" |
| G1634 | to expire | 6 | 1 | "to die, expire — to expire, give up one's spirit, Acts 5:5, 10; 12:23" |
| G2174 | be glad | 1 | 1 | "to be cheerful, glad — to be animated, encouraged, in good spirits, Phil. 2:19" |
| G2473 | like-minded | 2 | 1 | "like, of like soul, heart or mind minded — likeminded, of the same mind and spirit, Phil. 2…" |
| G3642 | fainthearted | 7 | 1 | "timid, fainthearted, discouraged — fainthearted, timid, discouraged 1Thes. 5:14" |
| G4861 | harmonious | 1 | 1 | "united in spirit, harmonious — united in mind, at unity, Phil. 2:2" |
| G5590G | soul | 825 | 1 | "life, soul; heart, mind; a person; the immaterial (and eternal) part of inner person…" |
| G5590H | soul: life | 42 | 1 | same as G5590G (shared parent medium_def) |
| G5590I | soul: myself | 6 | 1 | same as G5590G |
| G5590J | soul: person | 10 | 1 | same as G5590G |
| G5590K | soul: animal | 1 | 1 | same as G5590G |
| G5591 | natural | 6 | 1 | "pertaining to the natural state: physical, unspiritual, without the Spirit…" |
| H5314 | be refreshed | 3 | 1 | "(Niphal) to take breath, refresh oneself" |
| H5317 | honey | 5 | 1 | "flowing honey, honey from the comb, a dropping down, honey, honeycomb" |

---

## Why the G5590 sub-glosses all show PROSE_ONLY

STEP returns the same parent `medium_def` for G5590G, H, I, J, K — the sub-glosses do not
have individual definitions in the STEP API response. The parser stored the shared prose
block once per sub-gloss. This is expected behaviour, not a data error.

---

## Why H5314 and H5317 appear

H5314 (*be refreshed*, Niphal stem) — the stem label is present in the definition text
`"(Niphal) to take breath…"` but the parser did not recognise it as a structured stem
separator (it requires a standalone `Niphal:` or `Hiphil:` prefix, not a parenthetical).
Single stem, stored as prose.

H5317 (*honey*, 5 occurrences) — simple concrete noun with a single prose gloss. No
structure to parse.

---

## Why the low-frequency Greek terms appear

G0674, G0895, G1374, G1634, G2174, G2473, G3642, G4861, G5591 — all have ≤7 occurrences
and simple single-sense definitions from Mounce/STEP. None have numbered subdivisions.
PROSE_ONLY is the expected outcome for terms with a single semantic sense and minimal
lexical data.

---

## What needs to happen

**No action is required on the meaning data.** The stored definitions are correct and
complete as far as STEP provides.

**The fix is in `engine/flag_engine.py`:** when a term's `wa_meaning_parsed.parse_warnings`
contains `PROSE_ONLY`, write a `NOTE` quality flag with a description such as:

> *Meaning stored as single prose block. STEP medium_def contains no structured sense
> numbering for this term. No subdivisions available.*

This will silence WR-19 on the next audit run without changing any meaning data.

---

## Current status

WR-19 remains REVIEW until `flag_engine.py` is updated. This does not block researcher
use of the soul data — the meanings are correctly stored, just undocumented as prose-only.
The fix should be applied before the next word is audited so WR-19 does not fire for
every word with low-frequency Greek G2 terms.
