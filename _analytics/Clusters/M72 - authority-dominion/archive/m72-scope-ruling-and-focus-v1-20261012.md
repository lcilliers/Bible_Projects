# M72 Authority & Dominion: scope ruling and focus sets

**Date:** 2026-10-12 · **Escalation:** #1998 · **Status:** ruling recorded; focus sets pulled. No verse read.

## 1. The ruling

**Researcher, chat 2026-10-12, verbatim:** *"M72 need to be treated with care. Group A and C words should all be treated at most as a qualifyer. These verses should only be read in full within the context of the primary M-code. D and E is likely to be mostly about divine, and should be read only in as much as it describes the character of God. It seems that B is the main focus for the purposes of the study, with D where, it applies to humans."*

The gloss groups are those of the overview, [`m72-cluster-overview-v1-20261012.md`](m72-cluster-overview-v1-20261012.md) §3.

| Group | Words | How M72 treats it |
|---|---|---|
| **A** king, reign, kingdom, throne, palace (2,582 verses) | at most a **qualifier** | Not read for M72. The verse is read in full only when its primary M-code is read. The M72 word then has the role of qualifier, which most often means it names who acts or who decides. |
| **C** officials, leaders, masters (651 verses) | at most a **qualifier** | As A. |
| **E** Lord of hosts, Most High (283 verses) | divine | Read **only as far as the verse describes the character of God** (13.1). |
| **D** hand as power (510 verses) | mostly divine | Where the hand is God's, read as E. **Where the hand is a human's, D is in focus.** |
| **B** rule, dominion, authority, lordship (275 verses) | **main focus** | Read in depth, by role (rule 73). |
| F *archē*, *hēgeomai*, *kanōn* (86 verses) | not named in the ruling | Their gloss is away from authority ("beginning", "count, consider", "influence"). In each verse the role decides: a qualifier or a verb of reckoning is read with its primary M-code. A verse where one of them names ruling ("rulers", "leaders") is read with B. |

## 2. The focus sets

Script: [`m72-focus-pull-v1-20261012.py`](m72-focus-pull-v1-20261012.py). One row per verse, with the group's words, the other M72 words (qualifiers at most), the other M-codes, the narrative citations and open-thread rows, and whether the verse is one of the 182 M18 verses (OT-98).

| Set | Verses | Cited in the narrative | In OT-16 (M02) | In the M18 182 | Shared with M47 |
|---|---|---|---|---|---|
| **B** [`m72-group-B-verses-v1-20261012.csv`](m72-group-B-verses-v1-20261012.csv) | 275 (NT 110) | 33 | 4 | 18 | 28 |
| **D** [`m72-group-D-verses-v1-20261012.csv`](m72-group-D-verses-v1-20261012.csv) | 510 | 59 | 19 | 29 | 49 |

Seven verses hold both B and D.

**B, by Strong's:** G1849 *exousia* "authority" 102, H4910 *māšal* "rule" 81, H7287A *rādāh* "rule, dominion" 22, H4475 *memšālāh* "dominion" 17, H7985 *šolṭān* 14, H7990 10, H7980 *šālaṭ* "domineer" 8, G2961 *kurieuō* "lord over" 7, H7981 7, and 16 smaller.

**D, whose hand.** The ruling puts D in focus only where the hand is a human's. A working aid, `hand_holder_aid`, looks at the word after the hand word when it is in construct ("hand of …"). It is a pointer to read, not a decision:
- divine: 48 hits
- human or corporate: 107 hits
- not resolved mechanically: 423 hits

So 98 verses show a human holder and 41 show only God's. Most are not resolved: "his hand", "your hand", "into the hand of the …". A sample shows why the reading must decide. In *"He will also give the Moabites into your hand"* (2Ki 3:18), the hand is the king's, but the giving is God's. *"all the mighty power … that Moses did"* (Deu 34:12) is Moses' power. *"strong is your hand"* (Psa 89:13) is God's. So the first step on D is a light read of each verse for who holds the hand. Only the human-held verses then go to the in-depth reading.

## 3. What the ruling does to the threads carried in

- **OT-16 (M02 × M72, 100 verses).** In 65 the only M72 words are A or C. Those are qualifiers, and M02 is their primary M-code, so the anger readings already cover them and they need no M72 reading. 12 hold only E: they are read for God's character only, and the anger faces of God's wrath already read them. **23 hold a B or D word** (B 4, D 15, A/C with D 4), and these stay open for M72.
- **OT-98 (M18 × M72, 182 verses).** Of the 7 marked forward to M72:
  - Gen 31:29, Laban's power to harm, held back by God's word: **D, human**. In focus.
  - Ezr 7:9; 8:18; Neh 2:8; 2:18, "the good hand of my God": D, divine. Read for God's character only (13.1).
  - Isa 52:7, *"Your God reigns"*: an A word said of God. Read for God's character only.
  - 1Sa 15:28, *"The Lord has torn the kingdom of Israel from you"*: an A word, a qualifier. The act is God's, after *"you have rejected the word of the Lord"* (15:26). Read for God's character only.

  The other 175 are already placed by their M18 decisions.
- **The M47 check (#1979).** It narrows to the M47 verses in the focus sets: 28 in B, and the human-held verses among the 49 in D.
- **Signpost #1893 (hands).** The God's-hand pass reads God's hand. Under this ruling that is "the character of God". It is not opened by this step.

## 4. Proposed next step

1. **B, a trial batch** (guide §5.6: *"Trial a few verses and have them checked before running the whole set"*). About 8 verses across the main words would be read in their passages by role: G1849 "authority", H4910 "rule", H7287A "dominion", H7980 "domineer", G2961/G2634 "lord it over". The batch would include at least one where the ruler is God, to test where the "character of God only" line falls inside B.
2. **D, the hand-holder pass**: a light read of the 510 verses, one decision each (God's hand, a human's, or another being's), so that the human-held set is fixed before it is read in depth.
3. Then B in full, then D-human. Nothing is woven without your instruction.
