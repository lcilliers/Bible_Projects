# M47 Inner Seat — Step 1 stock-take (membership, counts, variant senses)

**Date:** 2026-09-25
**Source (only):** the researcher-supplied CSV `cluster_code_m47_verses.csv` (1,992 data rows; columns `cluster_code, short_name, description, strongNumber, stepGloss, surface, reference, text`).
**Brief:** `M47-handoff-brief.md` (from "The Origin of Thought" session), step 7.1.
**Not used:** the database. `bible_research.db` / `iba.db` are not present in this cloud checkout, so nothing below has been checked against the DB. Everything is counted from the CSV alone.

Tags follow the brief: **[verify]** = not confirmed against the DB. **[Claude reading]** = my own interpretation.

---

## 1. Headline numbers

| Measure | Value |
|---|---|
| Data rows | 1,992 |
| Strong's codes listed as M47 | 38 (36 with verses; **H7907** and **H3821** have no verse rows) |
| Distinct verses | 1,765 |
| Repeated (Strong's, verse) rows | 113. These are the same word occurring twice in one verse (e.g. H3824 in 1Ch 29:17, both "heart"). They are not duplicate records. |
| Verses with 2+ distinct M47 codes | 111 |
| Top books | Psa 219 · Pro 110 · Act 103 · Isa 83 · Jer 79 · Luk 66 · Eze 64 · Rom 61 · Job 60 · 1Cor 57 |

## 2. Membership by Strong's (distinct verses in the CSV)

| Strong's | stepGloss | Verses | Main ESV surfaces |
|---|---|---|---|
| G4151G | spirit/breath: spirit | 339 | Spirit 245, spirit 95, spirits 32 |
| H3820A | heart | 314 | heart 254, hearts 26, **sense 14, mind 8**, well 4, understanding 3 |
| H5315G | soul | 159 | soul 148, heart 3 |
| G2588 | heart | 145 | heart 87, hearts 62 |
| H3824 | heart | 127 | heart 106, hearts 16, mind 5 |
| G4561 | flesh | 117 | flesh 115, body 4 |
| H1320 | flesh | 115 | flesh 83, body 24, **meat 10** |
| H7307G | spirit | 84 | spirit 60, Spirit 25, mind 2 |
| H5315H | soul: life | 83 | life 69, lives 12 |
| H7307H | spirit: breath | 80 | **wind 55**, breath 15, winds 7 |
| H5315I | soul: myself | 55 | pronouns (you, yourself, I, himself …) |
| G5590G | soul | 41 | soul 23, souls 14, minds 2 |
| G5590H | soul: life | 33 | life 34 |
| H5315J | soul: person | 31 | persons/person |
| G4893 | conscience | 28 | conscience 25 |
| G4152 | spiritual | 20 | spiritual |
| H5315L | soul: appetite | 20 | appetite 8, desire 3 |
| G5590J · G2293 · H5315K | soul: person · take heart · soul: animal | 7 each | |
| H2436G · G1573 · H7308 · H7307J · H3826 · H7607 | bosom: embrace · lose heart · spirit (Aram.) · spirit: temper · heart (Aram.) · flesh | 6 each | |
| G5590I · H3825 · H7307I · G4151H | soul: myself · heart (Aram.) · spirit: side · spirit/breath: breath | 4–5 | |
| G4641 · G2589 · H1321 · H5315M · H5315N · G3050 | hardness of heart · heart-knower · flesh (Aram.) · soul: dead · soul: neck · spiritual | 1–3 | |
| H7907 · H3821 | heart | **0** | no verse rows |

**Families:** heart (H3820A, H3824, H3821, H3825, H3826, H7907, G2588, G2589, G4641, G2293, G1573) · soul (H5315 G–N, G5590 G–J) · spirit (H7307 G–J, H7308, G4151 G/H, G4152, G3050) · flesh (H1320, H1321, H7607, G4561) · conscience (G4893) · bosom (H2436G).

## 3. Variant-sense observations (from surfaces; [Claude reading])

- **H5315 is split into 8 senses** (G soul, H life, I myself, J person, K animal, L appetite, M dead, N neck). Only **H5315G (159)** is the "inner seat" sense on its face. H/I/J/K/M/N (180 verses together) are mostly life, reflexive, person or body uses. G5590 H/I/J follows the same pattern in Greek.
- **H7307 is split by sense.** H7307H "breath" is mostly **wind** (55 of 80), and H7307I is "side" (of the compass). These are not inner-seat uses.
- **H1320 flesh** includes "meat" (10) and "body" (24). Much of the Leviticus content (24 verses) is likely sacrificial or physical [verify by reading].
- **G4151G** includes the Holy Spirit (245 of the capitalised "Spirit" surfaces). This is the largest M47 member, but most of it is about divine Spirit, not human inner spirit. It needs to be separated before any count-based comparison [Claude reading].
- **H3820A is rendered "mind", "sense" or "understanding" 25 times.** This bears on the brief's open question about heart vs M15 mind.

## 4. ⚠ Completeness concern — the CSV looks partial for the Hebrew heart words [verify]

Several verses the brief itself cites as heart verses are **absent** from the CSV:

| Verse | Brief's point | In CSV? |
|---|---|---|
| 1 Ki 3:9 | "hearing heart" (lēv) | **no M47 row** |
| 1 Sam 1:13 | Hannah "speaking in her heart" | **no M47 row** |
| Ps 14:1 | "said in his heart" | **no M47 row** |
| Deut 6:5 | heart + soul | yes (H3824, H5315G) |
| Heb 4:12 | heart / soul / spirit | yes (G2588, G5590G, G4151G) |
| Mark 7:21 · Prov 16:9 | heart | yes |

Also, H3820A has only **2 Deuteronomy verses** and 1 in Numbers. H3824 has 30 in Deuteronomy.

My general lexical knowledge (**[lexical]**, not from the data) is that *lēv*/*lēvāv* together occur in the OT several hundred times more than the 441 verses here (314 + 127), and that *nephesh* occurs roughly 750 times. By contrast, G2588 (145) and G4151 (343) are close to the usual NT counts. So the gap appears to be **Hebrew-side**.

**I can't tell from the CSV why the rows are missing.** Possible reasons include the export query, the tagging in `verse_lexical`, or the variant-suffix mapping (e.g. lēv tagged under another suffix or a combined code, which the brief's §6 already flags). I have not assumed a cause.

**Consequence:** until this is resolved, any M47 counts and the co-occurrence numbers (queries B, C, D) will under-count Hebrew heart and soul.

## 5. M47 internal co-occurrence (verses sharing 2+ codes, from the CSV)

| Pair | Verses |
|---|---|
| G4151G spirit × G4561 flesh | 25 |
| H3824 heart × H5315G soul | 14 |
| G2588 heart × G4151G spirit | 12 |
| G2588 heart × G5590G soul | 9 |
| H3820A heart × H5315G soul | 6 |
| H3820A heart × H5315I soul: myself | 5 |
| H3820A heart × H7307G spirit | 5 |
| G4151G spirit × G5590G soul | 5 |
| G2588 heart × G4893 conscience | 3 |
| H1320 flesh × H3820A heart · H5315G × H7307G | 3 each |

[Claude reading] Two patterns stand out:
- In Greek, the strongest pairing is **spirit–flesh**, which is oppositional (Pauline).
- In Hebrew, it is **heart–soul (lēvāv + nephesh)**. That pairing looks formulaic and concentrated in Deuteronomy, e.g. "with all your heart and with all your soul" [verify by reading the 14].

## 6. What I need from you before step 2

1. **Completeness:** is the CSV meant to be the full M47 verse set? If so, the missing 1 Ki 3:9 / 1 Sam 1:13 / Ps 14:1 rows need investigating on your machine, since the DB is not available here. If not, can you send the full export, or run query A against `verse_lexical` locally?
2. **Scope of senses:** should the non-seat senses be kept in the observation set or set aside? These are wind, side, meat, neck, dead, animal, and possibly Holy Spirit.
3. Queries B, C and D need the DB. Can you run them locally and send me the CSVs, or should I prepare exact SQL for you to run?
