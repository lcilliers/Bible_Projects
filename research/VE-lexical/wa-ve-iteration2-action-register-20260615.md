# VE / narration — iteration-2 action register (living)

> **One living register** for the fixes/decisions arising from verse-by-verse review of the mechanical rebuild + narration. Update **in place** (add examples, change status, close items) — do not spawn parallel docs. Detail for the first example is in [wa-ve-narration-feedback-vc1630-20260615.md](wa-ve-narration-feedback-vc1630-20260615.md). Started 2026-06-15 from vc=1630 (2Sa 1:9).
>
> Nothing in the data has changed from this review yet — these are queued actions awaiting researcher direction / more examples.

## Status key
`DECISION` = needs researcher design call · `READY` = agreed, implement on go · `INVESTIGATE` = data check first · `DONE`

## Open design decisions (block the related actions)
- **D-A — object/target.** Relational ("directed for …") has no object. Add a **new VE "object/target"** (the node the term acts on), or fold the object into VE13? → *pending*
- **D-B — the "how"/governing predicate.** The qualifier verb ("seized") isn't stored (only analysed terms get spans). Capture it by (i) re-parsing STEP's full verse HTML for the span's governing verb, (ii) treat as a read field, or (iii) leave `UNRESOLVED`? → *pending*

## Action items

| ID | Source | Issue | Class | Action | Status |
|---|---|---|---|---|---|
| A1 | vc=1630 | transliteration shown alone (`ne.phesh(M25)`) | render | co-term renders with gloss: `ne.phesh "soul: life" (M25)` — VE3 value + narration + all outputs ([[feedback_translit_always_with_gloss]]) | READY |
| A2 | vc=1630 | location missed though seat-term present | VE5 logic | VE5 adds co-occurring **constitutional-seat TERMS** as signals (strong's→seat map: H5315/H5315H→soul, H3820/H3824→heart, H7307→spirit, …) | READY |
| A3 | vc=1630 | relational = bare preposition, no object | VE13 / new VE | per **D-A**: relational = direction + object; drop object-less bare prepositions | DECISION |
| A4 | vc=1630 | qualifier "agony seized the inner being" absent | data + design | per **D-B**: capture the governing predicate ("how") | DECISION |
| A5 | vc=1630 | legit T2 qualifier (`od` "still lingers") soft-deleted | data integrity | check why active T2 qualifier occurrences are soft-deleted (od: 170 active / 306 soft-del); is the web being thinned? | INVESTIGATE |

## Further verse reviews — add examples here

> As you review more verses, drop them in this table; recurring patterns escalate an action or open a new one.

| vc / ref | term | observation | maps to action |
|---|---|---|---|
| 1630 / 2Sa 1:9 | sha.vats "agony" | (the worked example above) | A1–A5 |
| | | | |
| | | | |

## Batching note
A1 + A2 are deterministic re-derivations (cheap; ve_lexical + narration findings rebuild from primary inputs). Recommend implementing them in **one combined re-run** once you've gathered more examples, so we regenerate once rather than per-fix.
