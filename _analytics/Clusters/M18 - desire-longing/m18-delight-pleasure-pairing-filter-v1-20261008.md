# M18 delight and pleasure: pairing filter before reading

**Date:** 2026-10-08 · **Escalation:** #1993 · **Status:** a mechanical filter for your decision. No verse has been read.

**Asked (researcher, verbatim):** *"lets focus for a moment on delight and pleasure. you grouped it as 640 verses. it looks like 2/3 of the verses are pleasant but the surface is indicative of meanings that good rather be a qualifyer (describe another characteristic) than a actual characteristic - pairing might help to break this down."*

**Scope:** group B of the overview ([`m18-cluster-overview-v1-20261008.md`](m18-cluster-overview-v1-20261008.md) §3B): 19 Strong's, 640 hits, 595 verses. H2896A *ṭôb* ("pleasant", mostly "good") has 408 of them.

**Files:**
- Pull (read-only, iba.db): [`m18-delight-pleasure-pairing-pull-v1-20261008.py`](m18-delight-pleasure-pairing-pull-v1-20261008.py). Output: [`m18-delight-pleasure-pairing-v1-20261008.csv`](m18-delight-pleasure-pairing-v1-20261008.csv), one row per hit, with the ESV text.
- Filter (no DB query): [`m18-delight-pleasure-filter-v1-20261008.py`](m18-delight-pleasure-filter-v1-20261008.py). Output: [`m18-delight-pleasure-filter-v1-20261008.csv`](m18-delight-pleasure-filter-v1-20261008.csv), the same rows with a `filter_bucket` column.

## 1. How the pairing was done

The pairing is mechanical. It is a way of deciding what needs reading, not a reading.

For each hit, the script records:
- **The form**, from the morph code: adjective, verb or noun.
- **The pair:** the content word the hit attaches to, in ESV word order.
  - An adjective directly before a noun pairs with that noun ("good land").
  - Any other adjective pairs with the content word before it ("the light was good").
  - A verb pairs with the word after it.
- **The pair's codes:** the M- or T-code of the paired word, from `cluster_strong`.
- **Markers in the verse:** "than" after the hit; "eyes" within 3 words; "evil" within 4 words; "do" next to it; heart, soul or spirit within 2 words; God named anywhere in the verse.

A **pattern** is then given by fixed rules, in this order (the first that matches):
1. comparison (better, best, than)
2. judged good by someone (eyes, seems, suits)
3. good set beside evil
4. doing good or doing well
5. qualifies the next noun (good X)
6. said of something (X is good)
7. verb (delight, please, be pleasant)
8. noun (delight, pleasure)

Spot checks show the patterns hold for most rows, with clear errors at the edges:
- Psa 118:29 "for he is good": a verb, paired by the rule with "steadfast love". The LORD is the one said to be good.
- Est 9:22 "holiday": counted under "doing good".
- H2896A in its verb form ("it was good", "it shall be well with") falls under "verb (delight …)", although it is not delighting.

## 2. Three buckets

Each hit is put in one bucket, by these rules (first match wins):
1. **Inner-being candidate:**
   - judged good by someone ("seems good to you", "in your sight")
   - or heart, soul or spirit within 2 words ("glad of heart", "cheerful of heart")
   - or a delight or pleasure verb or noun outside the two *ṭôb* Strong's (H2896A, H2895)
2. **Qualifies another characteristic:** the paired word carries an M-code.
3. **Qualifies a thing, person, place or act:** everything else.

| Bucket | All 19 Strong's | H2896A *ṭôb* | The other 18 |
| --- | --- | --- | --- |
| 1. inner-being candidate | 254 | 60 | 194 |
| 2. qualifies another characteristic | 117 | 100 | 17 |
| 3. qualifies a thing, person, place or act | 269 | 248 | 21 |
| **Total** | **640** | **408** | **232** |

This confirms what you saw. Of the 408 *ṭôb* hits, 348 (85%) are in buckets 2 and 3: "good" or "better" said of something else. Of the other 18 Strong's, 194 of 232 (84%) are in bucket 1: delighting, being pleased, pleasure.

"God named in the verse" is carried as a flag only: bucket 1 has 88, bucket 2 has 47 and bucket 3 has 92. It does not show whether God is the one delighting. That needs reading, and then the rule 72 routing (13.1).

### 2.1 Bucket 3 (269): *ṭôb* said of things, people and acts

| Pattern | H2896A | Others |
| --- | --- | --- |
| qualifies the next noun (good X) | 92 | 4 |
| comparison (better, than) | 74 | 2 |
| said of something (X is good) | 54 | 8 |
| good set beside evil | 11 | 0 |
| verb | 10 | 5 |
| other (doing good, noun) | 7 | 2 |

The pairs most often found: land (16), LORD (15), appearance (8), man (7), "to see" (7), "to be" (6), God (4), pasture (4), Israel (4), fig (4), grey hair (4).

**Not all of bucket 3 is a thing.** Two sets in it are about God:
- **LORD (15) and God (4):** mostly *ṭôb* said of the LORD, for example 1Ch 16:34 and Psa 136:1 "for he is good", and Psa 135:3 "for the Lord is good". This is God's own character (route A, 13.1), not a qualifier of a thing. Not every row is like this. In 1Sa 26:16 ("This thing that you have done is not good. As the Lord lives") the pairing only picked up the next name.
- **"to see" (7):** mostly Gen 1, "And God saw that it was good": God judging his work good, the divine counterpart of bucket 1's "judged good by someone". Ecc 5:18 ("what I have seen to be good") is the Preacher's own judgement, which is a bucket 1 kind of row.

These need to come out of bucket 3 before anything is parked. The rule could not separate them because the paired word, LORD or God, carries a T-code.

Examples:
- Deu 4:21 "the good land"
- 2Sa 18:27 "He is a good man"
- Pro 15:17 "Better is a dinner of herbs where love is than a fattened ox and hatred with it"
- Gen 41:22 "seven ears … full and good"

### 2.2 Bucket 2 (117): the paired word carries an M-code

This is where *ṭôb* may describe another characteristic, as you suggested. The paired M-codes most often found: M72 (12), M50 (10), M65 (10), M12 (7), M58 (7), M15 (7), M76 (6), M25 (5).

**Caution:** an M-code on the paired word does not mean the pair is an inner-being characteristic. Some of these M-tags are loose (#1970): "king" (8, M72), "hand: power" (3), "word" (3). Others are inner characteristics, for example:
- "kindness" (9): "good kindness"
- "understanding" (3): Psa 111:10 "all those who practice it have a good understanding"
- "to seek refuge": Psa 118:8 "It is better to take refuge in the Lord than to trust in man"
- "to hear: obey": 1Sa 15:22 "to obey is better than sacrifice"
- "be poor", "be humiliated", "mourning"

The full list of 117 rows, with the paired word and the text, is in the filter CSV.

### 2.3 Bucket 1 (254): inner-being candidates

| Source | Hits |
| --- | --- |
| delight or pleasure verbs (H2654A 73, G2106 21, H6026 10, H5276 8, H8173B 6, H2895 and others) | 117 |
| delight or pleasure nouns (H2656 38, H8191 9, H5278 7, G2237 5, others) | 57 |
| judged good by someone (H2896A 46, others 9) | 55 |
| heart, soul or spirit next to the word, and other edge rows | 25 |

Examples:
- Jer 40:4 "If it seems good to you to come with me to Babylon"
- Est 5:9 "joyful and glad of heart"
- Mat 3:17 "with whom I am well pleased" (God's own pleasure: route A)

## 3. For your decision

1. **Bucket 3 (269 hits, 248 of them *ṭôb*):** should these be parked as qualifiers of things, as was done with the 41 M64 choose verses with no other M-code (OT-93)? They stay in the data. Before parking, the God rows (§2.1: LORD, God, "God saw that it was good") would be taken out for 13.1, and the rest looked over once to catch rows the rules put there wrongly, for example the *ṭôb* verb rows "it shall be well with you".
2. **Bucket 2 (117 hits):** these could be read as pairs, one verse at a time: what is *ṭôb* saying about the other characteristic? Or they could be held for the strand of the paired characteristic. The loose M-tags ("king", "word", "hand") would then fall back to bucket 3.
3. **Bucket 1 (254 hits):** read in their passages as the delight and pleasure set, with God's own delight routed to 13.1 after reading.

If this split works for delight and pleasure, the same pairing could also be run on the other gloss groups. Group C *thelō* is the one where "would" and "want" may also be acting as qualifiers.
