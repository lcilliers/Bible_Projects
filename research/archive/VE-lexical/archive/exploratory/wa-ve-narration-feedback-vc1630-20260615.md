# Narration feedback — worked example vc=1630 (2Sa 1:9) — 2026-06-15

> Researcher comments on the rebuild results, each grounded against the verse data. Verse: *"And he said to me, 'Stand beside me and kill me, **for anguish has seized me**, and yet **my life still lingers**.'"* Term: **sha.vats** "agony" (H7661, M01, noun). Current output: sense=agony · type=status · compound=ne.phesh(M25) · relational="for". No location, no qualifier, no object.

## The six issues

| # | Comment | What the data shows | Class | Fix |
|---|---|---|---|---|
| **1** | Transliteration never in isolation — `ne.phesh(M25)` should carry the gloss | gloss "soul: life" is available; we just didn't render it | **template/render** | render co-term as `ne.phesh "soul: life" (M25)` in VE3 value **and** narration |
| **2** | "directed **for** ?????" — relational has no object; *maybe a missing VE* | VE13 captured the bare preposition "for"; the object ("me") is the governed noun, not captured | **design decision** | relational must be **direction + object**; bare prepositions alone are noise. Add an **object/target VE** (the recipient the term acts on) — see below |
| **3** | The real qualifier is *"agony **seized** the inner being"* — not in the lexical | **"seized" is NOT tagged** in the DB at all — only analysed terms get spans; the governing verb (the "how") is absent | **data gap + design** | the "how"/predicate needs STEP's full verse parse (governing verb of the span) or a read — not currently stored |
| **4** | Expected *"my life still lingers"* — life (term) + still-lingers (qualifier) | **`od` (H5750, T2, "still" / "still lingers") IS tagged but `delete_flagged=1`** at this verse (170 active / 306 soft-deleted corpus-wide) | **data integrity** | the active-only pass missed it because this qualifier occurrence is soft-deleted — investigate why legit T2 qualifiers are soft-deleted |
| **5** | Location not captured | **ne.phesh "soul: life" (M25) co-occurs** = the inner being is present; VE5 keyed on the English word "soul" but the text says "life" → missed | **VE-logic** | VE5 should treat co-occurring **constitutional-seat TERMS** (nephesh→soul, lev/levav→heart M47, ruach→spirit) as location signals — stronger than English string-matching |

## The pattern (connects to [[project_verse_extraction_cause_side_gap]])

The mechanical pass is solid on the **registered-term lexical facts** (sense, type, mode, the co-term web) but weak exactly where the earlier cause-side analysis predicted:
- **the "how" / governing predicate** ("seized") — not in the DB,
- **the object / target** ("me", the inner being acted on) — not captured,
- **qualifiers** — present in the data but some are **soft-deleted** (od),
- **location via the constitutional term** (nephesh), not just an English seat word.

So the term-in-isolation facts are right; the **relationship/qualifier/object web** — the verse's actual *meaning dynamics* — is the part still missing.

## Recommended iteration-2 (for your direction — nothing changed yet)

**A — clear fixes, ready to implement (one combined re-run of VE3/VE5 + narration regenerate):**
- **Issue 1**: co-term renders with gloss everywhere.
- **Issue 5**: VE5 location adds co-occurring constitutional-seat **terms** as signals (build a strong's→seat map: H5315/H5315H→soul, H3820/H3824→heart, H7307→spirit, …).

**B — design decisions I need from you:**
- **Issue 2 — object/target.** Add a new VE **"object/target"** (the node the term's action is directed at), so relational = *direction + object* ("directed **for** *him*"). Mechanically the object is the noun governed by the preposition / the verb's complement — often only resolvable by a read ⇒ `UNRESOLVED` when not mechanical. Confirm: new VE, or fold object into VE13?
- **Issue 3 — the "how"/predicate ("seized").** This needs the **governing verb of the term's span**, which STEP tags but we don't store. Options: (i) re-parse STEP's full verse HTML to capture the governing verb as the qualifier; (ii) treat the "how" as a read field; (iii) leave `UNRESOLVED`. Which?

**C — investigate (data integrity):**
- **Issue 4**: why are legitimate T2 qualifier occurrences (od at 2Sa 1:9) soft-deleted? If the verse-uniqueness/XREF cleanup over-reached, the whole qualifier web is thinned. Targeted check before deciding.

## Note
A regenerates cheaply (both ve_lexical and the narration findings rebuild deterministically from primary inputs), so batching A's fixes into one re-run is the cost-aware path — hence proposing rather than doing piecemeal.
