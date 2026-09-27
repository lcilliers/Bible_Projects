# M47 × other M-clusters — assessment of the co-occurrence file (v1)

**Date:** 2026-09-27
**File assessed:** `cluster-M47-other-m-code-cooccurrence-20260927.csv`
- Columns: `reference, m47_strong, m47_gloss, m47_surface, other_m_clusters, other_m_words, text`
- 2,832 rows

**Question from the researcher:** is this list too broad, and should it be broken down or carry more information?

**Researcher rulings recorded this turn** (on the depiction doc §7):
1. Heart as integrating centre — explore later.
2. Distinguish divine / human / other spirits where the evidence is clear; where it is not, say so explicitly.
3. Exclude bones, kidneys, bowels, *nous* and "inner being" for now.
4. The tag/surface misalignment note is sufficient; no further logging.

---

## 1. What the file contains (measured)

| Measure | Value |
|---|---|
| Distinct verses | **2,404** — 89% of the 2,688 M47 verses |
| Other M-clusters present | **79** |
| Distinct other Strong's codes | **1,443** |
| Verses by number of other clusters present | 1: 603 · 2: 700 · 3: 535 · 4: 311 · 5: 156 · 6: 69 · 7: 20 · 8: 8 · 9: 2 |

So this is not a subset of M47. It is **almost all of M47 again**, now tagged with other-cluster words.

**The verse text itself adds nothing new.** I have already read every one of these verses (depiction v1). What is new is the **tagging of the other words**.

## 2. Where the file is too broad

Volume is not the problem; I can process 2,404 verses. The problem is **signal**. Much of the co-occurrence comes from words that are not inner-being words, or from set phrases:

| Cluster (verses) | Main words behind it (sample of rows where the mapping is unambiguous) | Comment |
|---|---|---|
| M72 Authority & Dominion (235) | king, hand, hosts, kingdom | Narrative setting; "Lord of **hosts**" is a set phrase |
| M42 Prayer & Petition (268) | **declares**, speak, spoke, said, called | Mostly "declares the Lord" and ordinary speech verbs, not prayer [verify cluster membership] |
| M61 Purity & Holiness (182) | **Holy** (80 of the sample) | Mostly the name "Holy Spirit", not a holiness co-occurrence |
| M65 Speech & Tongue (183) | words, word, told, things | Generic |
| M25 Life & Death (212) | life, live, living | Largely overlaps nephesh "life" and rûaḥ "breath" — near-synonym, not a separate concept |
| M45 Renewal & Transformation (140) | deliver, satisfied, save, help, new | Mixed |
| M24 Faintness & Despair (216) | broken, afflict, poor, disaster, distress, faint | Mostly genuine inner-being signal |
| M41 Being Heard (124) | hear, heard, listen, obey | Genuine — the hearing thread from the brief |

This matches the brief's warning: *"Narrative settings inflate counts (king, gold, silver …)"*.

## 3. Structural issue in the file

`other_m_clusters` and `other_m_words` are separate lists. In **566 of 2,404 verses** they don't line up one-to-one: clusters are de-duplicated, words are not. So the file does not say directly which word belongs to which cluster.

**This is workable without a new export:**
- In the verses that do line up, every Strong's code maps to exactly one cluster (0 conflicts).
- The cluster list appears to be in first-appearance order of the words.

I can reconstruct the word → cluster mapping [verify on a sample].

## 4. What would make it more useful — additional information

In priority order:

1. **Word position / span index** for both the M47 word and the other word, or simply the distance between them. This is the most valuable addition. It lets me tell a *grammatical* relation from mere presence in the same verse:
   - direct: "my heart **rejoices**", "**broken** spirit"
   - distant: a clause away, or a different subject
   Without it, every verse must be judged by reading, which I can do, but the cluster tag adds little beyond what the reading already gives.
2. **One row per (M47 word × other word)**, with the other word's cluster in its own column. This removes the alignment problem in §3.
3. **Cluster description, plus a flag for inner-being vs other clusters.** For example, M72 Authority or M46 Wealth vs M24 Faintness or M18 Desire. This lets narrative-setting clusters be set aside or handled separately without guessing.
4. **Text column not needed**: I already hold the verse text. Dropping it would cut the file from ~817 KB to a small fraction [optional].

Items 2–4 I can largely derive myself from the current file. **Item 1 needs the DB.**

## 5. Recommendation — break it down by theme, not by frequency

Since you want the fringe as well as the dominant relations, I'd **not** rank clusters by count. Instead I'd work in **thematic batches**. Each batch would be read verse by verse and written up as "how M47 relates to this area":

| Batch | Clusters (current file) |
|---|---|
| A. Feeling | M01 Fear, M02 Anger, M03 Grief, M04 Joy, M24 Faintness/Despair, M20 Doubt, M48 Astonishment, M07 Shame, M53 Dishonor |
| B. Knowing / thinking / speaking | M15 Knowing, M16 Wisdom, M63 Reasoning, M81 Memory, M65 Speech, M41 Being Heard, M43 Prophecy/Vision, M82 Reminder |
| C. Willing / desiring / orientation | M18 Desire, M64 Will/Resolve, M28 Envy/Greed, M69 Self-Control, M34 Patience, M68 Hope, M83 Seeking, M11 Turning/Repentance, M30 Rebellion, M75 Disobedience, M66 Madness, M67 Sloth |
| D. Moral condition | M12 Righteousness, M58 Wickedness, M56 Sin, M14 Deceit, M57 Corruption, M62 Truth, M61 Purity (after removing "Holy Spirit"), M10c Defilement, M08 Pride, M09 Humility |
| E. Relating to God | M13 Faith, M31 Faith, M19 Trust, M36 Worship, M22 Praise, M49 Thanksgiving, M42 Prayer (after removing "declares"/"said"), M21 Fasting, M54 Torah, M44/M32 Covenant, M35 Tested, M60 Confession, M50 Grace, M79 Salvation, M59 Release, M45 Renewal, M80 Blessing, M39 Gift |
| F. Relating to others | M05 Kindness, M51 Love, M06 Malice, M10 Violence, M33 Rest/Peace, M52 Encouragement, M84 Outcry |
| G. Life, body, condition | M25 Life/Death, M23 Strength/Courage, M73 Sickness, M55 Destruction, M77 Stumbling, M70 Lifting/Bearing, M71 Glory, M37 Firstborn |
| H. Setting / narrative (low priority, scan for fringe only) | M72 Authority, M46 Wealth, M78 Slavery, M76 Walk/Conduct, M74 Keeping, M26 Judgment |

The grouping is mine, from the cluster names only [Claude reading]. You may want to regroup.

**Pre-filters I would apply and report (not silently):**
- "Holy" inside "Holy Spirit"
- "declares the Lord"
- "Lord of hosts"

**Spirit distinction (ruling 2) should be done first,** so every batch can say whether a relation involves the human spirit, God's Spirit, another spirit, or "not determinable". I'd do this as depiction v2 §2.3, classifying all G4151G / H7307G / H7308 verses.

## 6. Decision needed

- **(a)** Proceed with the current file, using the derived word → cluster mapping and the thematic batches in §5, starting with the spirit classification. Or:
- **(b)** Wait for a re-export with span positions (item 1) before the batches.

My recommendation is **(a) now**, with **(b) as an improvement** if the export is cheap for you.
