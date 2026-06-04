# Anchor verses with meaning + keywords — exploratory analytics

> **Read-only exploration, 2026-06-04.** Source: `verse_context` (anchors with both a Pass-A
> `analysis_note` *and* `keywords`), joined to `wa_verse_records` / `books` / `mti_terms` / `cluster`.
> Script: `scripts/_exploratory_anchor_meaning_analytics_v1_20260604.py`.

## Headline

- **226** anchor verses carry **both** meaning and keywords — out of **4153** live anchors (**5.4%**).
- These 226 anchors yield **1207** keyword instances (**1033** distinct phrases; **922** distinct tokens).
- So ~**95%** of anchor verses are *not yet* Pass-A enriched — a direct measure of how much verse-meaning groundwork remains on the anchors specifically.

## By cluster (5 clusters represented)

| Cluster | Name | Anchors |
|---|---|---|
| M10 | Sin | 69 |
| M38 | Salvation | 45 |
| M11 | Repentance | 43 |
| M10b | Wickedness | 42 |
| M10c | Defilement | 27 |

## By Testament

| Testament | Anchors |
|---|---|
| OT | 145 |
| NT | 81 |

## By Book (43 books)

| Book | T | Anchors |
|---|---|---|
| Leviticus | OT | 30 |
| Psalms | OT | 20 |
| Matthew | NT | 19 |
| Romans | NT | 13 |
| Isaiah | OT | 11 |
| Jeremiah | OT | 9 |
| Genesis | OT | 8 |
| Proverbs | OT | 8 |
| Exodus | OT | 7 |
| Revelation | NT | 7 |
| Numbers | OT | 6 |
| Ezekiel | OT | 6 |
| Mark | NT | 6 |
| Luke | NT | 6 |
| Deuteronomy | OT | 5 |
| Job | OT | 5 |
| 1 Samuel | OT | 4 |
| 1 Kings | OT | 4 |
| Hosea | OT | 4 |
| John | NT | 4 |
| 2 Corinthians | NT | 4 |
| Ephesians | NT | 4 |
| Hebrews | NT | 4 |
| 2 Samuel | OT | 3 |
| 2 Chronicles | OT | 3 |
| Acts | NT | 3 |
| 1 Corinthians | NT | 3 |
| 2 Kings | OT | 2 |
| Titus | NT | 2 |
| James | NT | 2 |
| 1 John | NT | 2 |
| Joshua | OT | 1 |
| 1 Chronicles | OT | 1 |
| Ezra | OT | 1 |
| Lamentations | OT | 1 |
| Daniel | OT | 1 |
| Amos | OT | 1 |
| Jonah | OT | 1 |
| Habakkuk | OT | 1 |
| Zechariah | OT | 1 |
| Malachi | OT | 1 |
| Colossians | NT | 1 |
| 2 Peter | NT | 1 |

## By keyword — top 40 phrases

| Keyword phrase | Count |
|---|---|
| salvation eschatological | 16 |
| atoned | 10 |
| faith exercised | 7 |
| ransomed | 7 |
| rescued | 6 |
| god-saving | 6 |
| rescue physical | 6 |
| god saving | 6 |
| will turning | 6 |
| hope sustained | 5 |
| endangered | 5 |
| christ saving | 5 |
| priest mediating | 5 |
| salvation present | 4 |
| forgiven | 4 |
| delivered | 4 |
| conscience cleared | 4 |
| violation inadvertent | 4 |
| heart corrupted | 3 |
| christ-saving | 3 |
| will refusing | 3 |
| forgiveness sought | 3 |
| guilt surfacing | 3 |
| conscience suppressed | 3 |
| sin persistent | 3 |
| guilt removed | 3 |
| impurity contact | 3 |
| wrath averted | 3 |
| sin-laden resolved | 3 |
| standing restored | 3 |
| will oriented evil | 2 |
| divine revulsion | 2 |
| boundary transgressed | 2 |
| divine rejection | 2 |
| inner corruption | 2 |
| will captive | 2 |
| enmity ended | 2 |
| will persisting | 2 |
| human inability | 2 |
| healing spiritual | 2 |

## What jumps out

1. **Enrichment is concentrated in a single cluster family.** All 226 meaning+keyword anchors live in the
   **sin → repentance → salvation arc**: M10 Sin (69), M38 Salvation (45), M11 Repentance (43),
   M10b Wickedness (42), M10c Defilement (27). This is exactly where recent analytic work happened
   (M10c/M10b closed, M11/M38 worked) — so *Pass-A keyword enrichment is a faithful proxy for "where
   analysis has actually reached."* The other ~43 clusters have **zero** enriched anchors yet.
2. **The faculty language is dominated by the WILL.** Top tokens: **will (70)**, guilt (46), inner (36),
   heart (29), conscience (29), self (27), soul (10). Across this arc the inner life is being read
   overwhelmingly through the **volitional faculty** and the **guilt/conscience** axis — theologically
   coherent for sin/repentance/salvation, and a real inner-being signal rather than mere vocabulary.
3. **OT-weighted, and Leviticus leads** (OT 145 / NT 81; Leviticus 30, Psalms 20, Matthew 19). The
   Levitical spike is the **defilement / atonement** ritual layer (M10c); Psalms carries the penitential
   voice; Matthew/Romans carry the NT salvation language.
4. **Top phrases trace the doctrine, not just words:** *salvation eschatological* (16), *atoned* (10),
   *faith exercised* (7), *ransomed* (7), *rescued / delivered*, *will turning*, *conscience cleared*,
   *wrath averted* — the keyword layer is already carrying compact theological readings.

## Caveat (matters for the verse-meaning audit)

The keyword vocabulary is **not normalised** — the same concept splits on hyphenation/spacing:
*god-saving* (6) vs *god saving* (6); *christ-saving* (3) vs *christ saving* (5); *sin-laden* vs *sin laden*.
So cross-verse keyword grouping is noisy, and any future keyword-based clustering should canonicalise
first. This is a small, concrete example of the kind of meaning-layer hygiene the upcoming
**verse-meaning audit** will want to surface.

## By keyword — top 40 tokens (phrases split into words, stopwords removed)

| Token | Count |
|---|---|
| will | 70 |
| guilt | 46 |
| divine | 41 |
| sin | 40 |
| inner | 36 |
| heart | 29 |
| conscience | 29 |
| self | 27 |
| salvation | 26 |
| moral | 23 |
| saving | 21 |
| evil | 18 |
| eschatological | 18 |
| defilement | 18 |
| absent | 16 |
| god | 16 |
| judgment | 16 |
| atonement | 14 |
| forgiveness | 14 |
| removed | 13 |
| rescue | 13 |
| transgression | 13 |
| corrupted | 12 |
| corruption | 11 |
| faith | 11 |
| restored | 11 |
| active | 11 |
| covered | 11 |
| received | 10 |
| turning | 10 |
| soul | 10 |
| atoned | 10 |
| character | 9 |
| refused | 9 |
| corrupt | 9 |
| love | 9 |
| covenant | 9 |
| iniquity | 9 |
| lost | 8 |
| identity | 8 |

