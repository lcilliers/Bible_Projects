# Read-layer dedup estimate (from mechanical findings)

> READ-ONLY (`scripts/_assess_read_dedup.py`). How much the read would duplicate: distinct signatures vs total term-in-verses. Read once per signature → apply to all members.

**28464 term-in-verses total.**

| signature | distinct | reads saved | dedup % | read-once cost |
|---|---|---|---|---|
| **S1 term only** | 1623 | 26841 | **94%** | 1623 reads |
| **S2 term + sense** | 1940 | 26524 | **93%** | 1940 reads |
| **S3 term + sense + co-occur-clusters** | 16684 | 11780 | **41%** | 16684 reads |

**Reading:** term/sense-invariant read fields (faculty · origin · base nature) → read once per **S2 (1940)**, applied to all 28464 verses = **93% saved**. Context fields (attributed-to-God · produces · response · direction) → S3-grained (16684) or per-verse, but near-dups still cluster.

## Biggest duplicate groups (term + sense) — read once, applies to N verses

| term | verses | sample sense |
|---|---|---|
| ya.da | 368 | to know to know, learn to know to perceive to pe |
| pneuma | 341 | wind, breath, things which are commonly perceive |
| tov | 306 | adj 1) good, pleasant, agreeable 1a) pleasant, a |
| che.sed | 296 | a reproach, shame |
| qa.ra | 275 | 1a1) to call, cry, utter a loud sound 1a2) to ca |
| che.sed | 243 | goodness, kindness, faithfulness |
| hagios | 210 | holy holy, sacred, pure persons |
| chay | 209 | adj 1) living, alive 1a) green (of vegetation) 1 |
| chay | 207 | kinsfolk |
| chay.yah | 207 | community |
| sha.mar | 190 | 1a1) to keep, have charge of 1a2) to keep, guard |
| tsad.diq | 184 | just, lawful, righteous just, righteous (in gove |
| ra.sha | 180 | wicked, criminal guilty one, one guilty of crime |
| ya.re | 179 | 1a1) to fear, be afraid 1a2) to stand in awe of, |
| ka.vod | 179 | glory, honour, glorious, abundance abundance, ri |
| cha.yah | 179 | to live to have life to continue in life, remain |
| ba.rakh | 175 | to bless |
| ba.qash | 170 | to seek to find to seek to secure to seek the fa |
| cha.ta | 163 | to miss to sin, miss the goal or path of right a |
| a.von | 162 | : crime 1) perversity, depravity, iniquity, guil |

_Singletons (must read individually): S2 = 489 (2% of verses unique by term+sense); S3 = 13550 (48%)._