# Term-anchor v2 — meaning-cluster overlay applied

**Generated:** 2026-05-04T19:05:00Z  
**Source meaning clusters:** `wa-meaning-clusters-v1-2026-05-04.json` (45 named-characteristic clusters)  
**Source v1 anchor:** `wa-term-anchor-20260504.json`  

## Headline

- Total terms in v2: **2,491**
- Reassigned to meaning clusters (M01..M46): **1,555**
- Kept on legacy v1 cluster (no meaning-cluster home): **936**

## Meaning-cluster catalogue (45 named characteristics)

| ID | Name | Members |
|---|---|---:|
| M01 | Fear, Dread and Terror | 91 |
| M02 | Anger, Wrath and Indignation | 42 |
| M03 | Grief, Sorrow and Mourning | 82 |
| M04 | Joy, Gladness and Delight | 58 |
| M05 | Love, Compassion and Kindness | 85 |
| M06 | Hate, Contempt and Hostility | 30 |
| M07 | Shame, Disgrace and Humiliation | 35 |
| M08 | Pride, Arrogance and Boasting | 47 |
| M09 | Humility, Meekness and Submission | 17 |
| M10 | Guilt, Sin and Transgression | 86 |
| M11 | Repentance, Forgiveness and Restoration | 14 |
| M12 | Purity, Holiness and Consecration | 46 |
| M13 | Truth, Faithfulness and Integrity | 26 |
| M14 | Deceit, Hypocrisy and Falsehood | 40 |
| M15 | Wisdom, Understanding and Knowledge | 86 |
| M16 | Folly, Madness and Foolishness | 27 |
| M17 | Counsel, Planning and Purpose | 17 |
| M18 | Hope, Expectation and Waiting | 26 |
| M19 | Trust, Confidence and Security | 30 |
| M20 | Doubt, Despair and Anxiety | 11 |
| M21 | Prayer, Worship and Devotion | 31 |
| M22 | Praise, Thanksgiving and Glory | 41 |
| M23 | Strength, Power and Dominion | 104 |
| M24 | Weakness, Vulnerability and Suffering | 61 |
| M25 | Life, Vitality and Existence | 14 |
| M26 | Righteousness and Justice | 35 |
| M27 | Evil, Wickedness and Abomination | 14 |
| M28 | Envy, Greed and Lust | 34 |
| M29 | Desire, Longing and Will | 11 |
| M30 | Obedience and Disobedience | 22 |
| M31 | Faith, Belief and Unbelief | 13 |
| M32 | Conscience and Self-Awareness | 6 |
| M33 | Peace, Rest and Quietness | 42 |
| M34 | Perseverance, Endurance and Steadfastness | 21 |
| M35 | Testing, Temptation and Trial | 24 |
| M36 | Service, Slavery and Labour | 18 |
| M37 | Calling, Election and Vocation | 20 |
| M38 | Salvation, Redemption and Deliverance | 13 |
| M39 | Blessing, Favour and Grace | 15 |
| M41 | Remembrance and Memory | 30 |
| M42 | Speech, Voice and Cry | 34 |
| M43 | Prophecy and Revelation | 13 |
| M44 | Relational Disposition | 17 |
| M45 | Transformation and Renewal | 14 |
| M46 | Abundance, Prosperity and Wealth | 12 |

## Legacy clusters still holding terms (top 20)

These are the v1 H/G-prefix clusters that retain terms not yet assigned to a meaning characteristic. Useful for deciding whether to extend the meaning-cluster set.

| Legacy cluster | Terms still on it |
|---|---:|
| None | 332 |
| H019 | 120 |
| H036 | 42 |
| H028 | 31 |
| H008 | 21 |
| G029 | 19 |
| H050 | 17 |
| H001 | 16 |
| G005 | 16 |
| H009 | 13 |
| G014 | 13 |
| H034 | 11 |
| H005 | 10 |
| H006 | 9 |
| H026 | 9 |
| H044 | 9 |
| G030 | 9 |
| G003 | 8 |
| G026 | 8 |
| H021 | 7 |

## Bucket distribution after overlay

| Bucket | Count |
|---|---:|
| T1 | 1752 |
| T2 | 491 |
| GENERICS | 97 |
| QUALIFIERS | 54 |
| EXTRACTION-NOISE | 37 |
| LOCI | 36 |
| FLAG | 24 |

## Cluster-source breakdown

| Source | Count |
|---|---:|
| meaning_v1 | 1555 |
| legacy_v1 | 936 |

## Schema (v2 term anchor records)

```
{
  "strong":              "H0056",
  "lang":                "H" | "G",
  "transliteration":     "a.val",
  "gloss":               "to mourn",
  "verse_count":         38,
  "multi_term_pct":      84.2,
  "bucket":              "T1" | "T2" | "FLAG" | "EXTRACTION-NOISE",
  "cluster_id":          "M03" | "H011" | ...,
  "cluster_label":       "Grief, Sorrow and Mourning" | ...,
  "cluster_source":      "meaning_v1" | "legacy_v1",
  "legacy_cluster_id":   "H011",
  "legacy_cluster_label":"mourning/mourn/weep"
}
```
