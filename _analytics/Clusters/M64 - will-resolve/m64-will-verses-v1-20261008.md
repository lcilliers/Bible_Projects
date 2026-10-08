# M64 "will" set: verse pull (v1, 2026-10-08)

**Escalation:** #1986 (successor to #1978) · **Status:** data pull only, no reading

Researcher, verbatim: *"still working on M64. Create a new escalation to focus on the 'will', 'willing' terms in this cluster. … isolate the verses associated with these terms in a separate csv"*.

- **CSV:** [`m64-will-verses-v1-20261008.csv`](m64-will-verses-v1-20261008.csv). One row per verse, in canonical order. Columns: reference, hits, hit_words (Strong's, ESV surface, morph, position), other_m_words, narrative_n, narrative_refs, esv_text.
- **Script:** [`m64-choose-verses-pull-v3-20261008.py`](m64-choose-verses-pull-v3-20261008.py), run as `H0014 H6634 H5081G G1014 G1013 --tag will`. It is read-only against iba.db. v3 only changes the output name so a new set gets its own dated file; v2 is archived.

## 1. Which terms are in the set

The M64 terms were taken from the quick summary (§3) and checked against `verse_lexical.surface` (the ESV word) for every live M64 Strong's.

| Strong's | Gloss | Why it is in | Hits | Verses | ESV surface (top) |
| --- | --- | --- | --- | --- | --- |
| H0014 | be willing | gloss | 54 | 52 | would 14, willing 13, he would 8, unwilling 3, consent 3, will 2, I would 2, and would 2 |
| H6634 | to will | gloss | 10 | 7 | he will 4, he would 4, to his will 1, desired to 1 |
| H5081G | noble: willing | gloss | 5 | 5 | willing 3, willing man 1, generous 1 |
| G1014 | to plan | surface | 34 | 34 | want 5, wishing 3, wished 3, I would 3, desiring 2, wanted 2, desire 2, will 2 (also willing, wills, wish, wishes) |
| G1013 | plan | surface | 2 | 2 | plan 1, will 1 |

- **G1014 and G1013 are in on their surface, not their gloss.** The step gloss "to plan" / "plan" does not show it, but the ESV renders most G1014 hits as want, wish, will or would. Drop them if you want the set held to the three "will" glosses. The CSV can be re-run with only those three.
- **Left out:** G1011 *to plan* ("wanted" 3 of 9 hits; the rest are plan words), and every other M64 Strong's (no will, willing, would, wish or want surface).
- **Outside M64:** G2309 *thelō* and G2307 *thelēma*, the usual Greek "will" words, are tagged M18, not M64. They are not in this pull.

## 2. Scale

- **99 verses, 105 hits.** Act 27:43 holds two of the terms (G1014 and G1013); every other verse holds one Strong's.
- **All 99 verses are in scope for the will reading.** 8 of them appear somewhere in the narrative, but a citation says only that the verse is quoted, not that its will word has been dealt with (§3).
- **9 of the 29 marked M64 × M47 verses** (`m64-m47-marked-verses-v1-20261006`) are in this set: Exo 10:27, Exo 35:5, Exo 35:22, 2Sa 23:17, 1Ch 11:19, 2Ch 29:31, Eze 3:7, Dan 5:21, 1Co 12:11.
- **9 verses carry no other M-code.**
- **Other M-codes in the same verses (by verses):** M41 19, M15 16, M72 13, M47 11, M23 9, M45 8, M65 7, M30 6, M55 6, M18 6.

## 3. The 8 verses the narrative quotes, and for what

Researcher, 2026-10-08, verbatim: *"You mention Act 25:20 is quoted in the narrative. The quote is in a completely different context. focussing in on the context of 'will' or 'wanted to' (the ESV term) is not the context of the narrative quote. The narrative is not wrong. but assuming the verse is already in the narrative and therefore should be ignored, is wrong."*

The `narrative_n` / `narrative_refs` columns find a citation of the **verse**. They say nothing about which word or which act in the verse the narrative is using. Checked by hand against the chapter text:

| Verse | Will word | Narrative place | What the narrative quotes | Will word quoted? |
| --- | --- | --- | --- | --- |
| Deu 1:26 | "would" (not go up) | 10.5 Speaking, *Grumbling* | "you would not go up, but rebelled", as what went with grumbling | yes, but for grumbling |
| Deu 2:30 | "would" (not let us pass) | Ch 6, Ch 9, Ch 11 | "hardened his spirit and made his heart obstinate" | no |
| 1Sa 31:4 | "would" (not) | 10.7, *Fear and choosing* | "his armor-bearer would not, for he feared greatly" | yes, for fear beside a choice |
| Psa 51:12 | "willing" (spirit) | Ch 6, *The human spirit* | "Uphold me with a willing spirit", for the spirit | yes, for the spirit |
| Pro 6:35 | "refuse" | 10.1, Ch 11 §4 | "He will accept no compensation" (jealousy) | no |
| Dan 5:19 | "he would" (×4) | 10.10, *Fear that arrives with a person* | "Whom he would, he killed", for the fear his power brought | yes, for fear |
| Act 25:20 | "wanted" | 10.2, *Perplexity* | "being at a loss how to investigate these questions" | no |
| 1Ti 2:8 | "desire" | 10.4, 10.13, Ch 11 | "lifting holy hands without anger or quarreling" | no |

- In 4 verses the narrative quotes another part of the verse; the will word is not in the quote.
- In the other 4 the will word is in the quote, but the narrative uses it for something else (grumbling, fear, the spirit). None of the 8 is an account of willing.
- So none of the 8 is set aside. Each is read for its will word like the other 91.

No verse has been read. Nothing here is interpreted or woven.
