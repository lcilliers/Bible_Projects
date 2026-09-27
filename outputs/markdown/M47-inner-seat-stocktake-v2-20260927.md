# M47 Inner Seat — Step 1 stock-take (membership, counts, variant senses) — v2

**Date:** 2026-09-27
**Supersedes:** `archive/M47-inner-seat-stocktake-v1-20260925.md`. v1 was built from `cluster_code_m47_verses.csv`, which was incomplete on the Hebrew side.
**Source (only):** the researcher-supplied revised CSV `cluster-M47-surface-forms-20260927.csv`. It has 3,175 data rows and the same columns as before: `cluster_code, short_name, description, strongNumber, stepGloss, surface, reference, text`.
**Brief:** `M47-handoff-brief.md` §7 step 1.
**Not used:** the database. No DB is present in this cloud checkout, so everything below is counted from the CSV alone.

Tags: **[verify]** = not confirmed against the DB. **[lexical]** = outside knowledge, not from the data. **[Claude reading]** = my own interpretation.

---

## 1. Headline numbers (v1 → v2)

| Measure | v1 CSV | v2 CSV |
|---|---|---|
| Data rows | 1,992 | **3,175** |
| Strong's codes | 38 (2 with no verses) | **38, all with verses** |
| Distinct verses | 1,765 | **2,688** |
| Verses with 2+ distinct M47 codes | 111 | **211** |
| Repeated (Strong's, verse) rows | 113 | 269 |

**Checks on the revision:**
- **The same 38 codes are in both files.** No code was added or dropped.
- **Nothing was lost.** Every (Strong's, verse) pair in v1 is also in v2.
- **Repeated rows are genuine.** There are 184 groups of rows repeating the same (Strong's, verse, surface), 208 extra rows in all. In every group, the verse text contains that surface word at least as many times as it is repeated (checked by word match on the ESV text). So these reflect a word occurring more than once in the verse, not duplicate records. Counts below use **distinct verses**.
- **One row has no surface:** G4151G at 1Jo 5:7, whose ESV text is "For there are three that testify:". **[Claude reading; verify]** This is probably a versification difference, where the Greek tag sits on a verse whose ESV wording doesn't contain "spirit" (the ESV has "the Spirit" in 5:8).

**Brief's test verses — all now present:**

| Verse | Codes in v2 |
|---|---|
| 1 Ki 3:9 | H3820A (v1: missing) |
| 1 Sam 1:13 | H3820A (v1: missing) |
| Ps 14:1 | H3820A (v1: missing) |
| Deut 6:5 | H3824, H5315G |
| Deut 8:17 | H3824 |
| Heb 4:12 | G2588, G5590G, G4151G |
| Mark 7:21 · Heb 8:10 · Heb 10:16 · Rom 1:21 · Phil 4:7 | G2588 |
| Prov 16:9 · Prov 19:21 · Jer 4:14 | H3820A |
| 1 Chr 29:18 | H3824 |
| Ps 146:4 | H7307H |

**Completeness now [lexical; verify]:**
- **Hebrew heart:** H3820A has 550 verses and H3824 has 230. The usual counts are about 600 occurrences for *lēv* and about 250 for *lēvāv*. Occurrences exceed verses where the word repeats in a verse, so these figures look broadly consistent.
- **Hebrew soul:** H5315 G–N together cover 691 verses, against about 750 occurrences of *nephesh*.

I have **not** confirmed completeness against the DB.

## 2. Membership by Strong's (distinct verses)

| Strong's | stepGloss | v2 | v1 | Main ESV surfaces (v2 row counts) |
|---|---|---|---|---|
| H3820A | heart | **550** | 314 | heart 426, hearts 42, **mind 24, sense 16**, kindly 4, himself 4, well 4 |
| G4151G | spirit/breath: spirit | 340 | 339 | Spirit 245, spirit 95, spirits 32 |
| H1320 | flesh | 241 | 115 | flesh 177, body 40, **meat 36**, thin 3, plump 2 |
| H3824 | heart | 230 | 127 | heart 188, hearts 32, **mind 11**, consider 5, understanding 3 |
| H5315G | soul | 230 | 159 | soul 209, souls 13, heart 8, life 4, mind 2 |
| H7307G | spirit | 194 | 84 | spirit 127, Spirit 80, mind 3 |
| H5315H | soul: life | 180 | 83 | life 154, lives 31, lifeblood 2 |
| G2588 | heart | 149 | 145 | heart 87, hearts 63 |
| H7307H | spirit: breath | 137 | 80 | **wind 93**, breath 35, winds 10, blast 2 |
| G4561 | flesh | 126 | 117 | flesh 118, human being 4, body 4, earthly 3 |
| H5315I | soul: myself | 126 | 55 | reflexive pronouns (himself, herself, yourselves …) |
| H5315J | soul: person | 83 | 31 | person 42, persons 23, anyone 7 |
| G5590G | soul | 46 | 41 | soul 23, souls 14, minds 2 |
| H5315L | soul: appetite | 45 | 20 | appetite 11, desire 9, greed 2, hunger 2, will 2 |
| G5590H | soul: life | 33 | 33 | life 34, lives 5 |
| G4893 | conscience | 29 | 28 | conscience 26 |
| G4152 | spiritual | 21 | 20 | spiritual |
| H2436G | bosom: embrace | 19 | 6 | arms 5, bosom 4, breast 2, heart 2 |
| H7607 | flesh | 16 | 6 | relative 3, flesh 3, close 2, meat 2 |
| H5315M | soul: dead | 13 | 2 | dead body 5, dead 4, body 3 |
| H5315K | soul: animal | 12 | 7 | creature(s) |
| H7308 | spirit (Aram.) | 11 | 6 | spirit 9 |
| H7307J | spirit: temper | 10 | 6 | anger 3, spirit 3, temper, self-control |
| G5590J | soul: person | 8 | 7 | |
| H7307I | spirit: side | 7 | 4 | side(s) |
| G2293 · H3826 | take heart · heart (Aram.) | 7 each | 7 / 6 | |
| G1573 · G5590I · H3825 | lose heart · soul: myself · heart (Aram.) | 6 each | 6 / 5 / 4 | H3825: mind 5, heart 2 |
| G4151H | spirit/breath: breath | 4 | 4 | |
| H1321 · G4641 | flesh (Aram.) · hardness of heart | 3 each | | |
| G3050 · G2589 · H5315N | spiritual · heart-knower · soul: neck | 2 each | | |
| H3821 · H7907 | heart (Aram.) · heart | 1 each | 0 | H3821 "heart"; H7907 "mind" |

**Families:**
- **heart:** H3820A, H3824, H3821, H3825, H3826, H7907, G2588, G2589, G4641, G2293, G1573
- **soul:** H5315 G–N, G5590 G–J
- **spirit:** H7307 G–J, H7308, G4151 G/H, G4152, G3050
- **flesh:** H1320, H1321, H7607, G4561
- **conscience:** G4893
- **bosom:** H2436G

**Where the revision added verses:** almost entirely Hebrew. The Greek codes barely changed: G2588 went from 145 to 149 and G4151G from 339 to 340.

## 3. Variant-sense observations (from surfaces; [Claude reading])

- **Heart rendered as "mind":**
  - H3820A: mind 24, sense 16, plus kindly, himself and well.
  - H3824: mind 11, consider 5, understanding 3.
  - H3825 (Aramaic): mind 5 of 7 rows.
  - H7907: its single row is "mind".

  This is direct surface evidence for the brief's open question on heart vs M15 mind. The ESV itself moves *lēv* between "heart" and "mind".
- **Soul (H5315, 691 verses) splits by sense:**
  - Only **H5315G (230)** is "soul" on its face.
  - The other senses make up 461 verses: life 180, myself 126, person 83, appetite 45, dead 13, animal 12, neck 2.
  - The Greek G5590 follows the same pattern (G 46 vs H/I/J 47).
- **Spirit (H7307) splits by sense:**
  - H7307H is mostly **wind** (93 of 137 verses' surfaces).
  - H7307I is "side".
  - H7307J is temper or anger.
  - H7307G (194) is the "spirit" sense, and 80 of its surfaces are capitalised "Spirit".
- **Flesh:** H1320 includes meat 36 and body 40. Leviticus is prominent overall (99 verses), which suggests sacrificial and purity contexts [verify by reading].
- **G4151G:** 245 of its surfaces are "Spirit" (Holy Spirit). It is the largest Greek member, but mostly divine rather than human spirit.

## 4. M47 internal co-occurrence (verses sharing 2+ distinct codes)

| Pair | v2 | v1 |
|---|---|---|
| G4151G spirit × G4561 flesh | 25 | 25 |
| H3824 heart × H5315G soul | 23 | 14 |
| H3820A heart × H7307G spirit | **18** | 5 |
| G2588 heart × G4151G spirit | 12 | 12 |
| H1320 flesh × H3820A heart | 11 | 3 |
| H3820A heart × H5315G soul | 11 | 6 |
| G2588 heart × G5590G soul | 9 | 9 |
| H1320 × H5315H (flesh × life) · H1320 × H7307G (flesh × spirit) | 8 each | |
| H3820A × H3824 (both heart forms) | 7 | |
| H1320 × H7307H (flesh × breath/wind) · H3820A × H5315I (heart × self) | 6 each | |
| G4151G × G5590G (spirit × soul) | 5 | 5 |
| H3824 × H7307G · H5315G × H7307G · H3820A × H7307H · H1320 × H5315G/I/J · H1320 × H7607 | 4 each | |
| G2588 × G4561 · G2588 × G4893 | 3 each | |

[Claude reading; each point needs verse reading before it is treated as an observation]
- **Hebrew heart–spirit is now the second-strongest Hebrew pair (18).** It was hidden in v1, with only 5. A "new heart / new spirit" pattern (Ezekiel) is a likely contributor [verify].
- **Flesh pairs with life, spirit and breath (H1320 × H5315H / H7307G / H7307H).** This points to a "flesh animated by breath/life" usage, distinct from Greek spirit-vs-flesh opposition [verify].
- **Heart–soul (H3824 × H5315G, 23)** remains the characteristic Hebrew pairing, largely the Deuteronomic formula [verify].

**Top books (distinct verses):** Psa 316 · Pro 164 · Jer 136 · Isa 129 · Eze 123 · Job 106 · Act 104 · Lev 99 · Gen 89 · Exo 79 · Num 75 · Deu 74.

## 5. Open items carried forward

1. **Scope of senses.** Should the senses that aren't about the inner seat stay in the observation set or be set aside? These are wind, side, meat, neck, dead body, animal, and possibly Holy Spirit.
2. **1Jo 5:7 blank-surface row** — confirm how the tag is versified [verify].
3. **Queries B, C and D** need the DB. They must be run locally, or I can supply exact SQL.
