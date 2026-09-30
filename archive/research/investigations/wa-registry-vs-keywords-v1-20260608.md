# Registry (214 anchor words) vs keyword vocabulary — why some are missing

> READ-ONLY (`scripts/_assess_registry_vs_keywords.py`). Keywords are derived from **term glosses**, not from the registry, so an anchor word is a keyword only if a term's gloss uses it. Categories: PRESENT · FILTERED (a filter removed an existing token — *possible bug*) · FORM-VARIANT (stem present, exact word not) · ABSENT (word not in any gloss). No DB writes.

**215 registry words · PRESENT 177 · FILTERED 3 · FORM-VARIANT 9 · ABSENT 26.**

## FILTERED — token exists in glosses but a filter removed it (review: did we drop signal?)

| registry word | filter that removed it |
|---|---|
| meaning | **ANALYTIC** |
| might | **STOP** |
| will | **STOP** |

## ABSENT — the anchor word appears in NO term gloss (lexicon uses other vocabulary)

awareness, blamelessness, boastfulness, brokenness, consciousness, darkening, deadness, deadness, division, hopelessness, identity, ingratitude, intuition, loyalty, manipulation, personality, personhood, recognition, resentment, resentment, self-awareness, sorcery, surrender, vulnerability, vulnerability, whoredom

## FORM-VARIANT — stem present, exact anchor word not (e.g. abundance↔abundant)

anointing, betrayal, consecration, seeking, sexuality, sloth, stupor, worth, yearning
