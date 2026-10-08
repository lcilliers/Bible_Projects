# M64 × M47: 29 verses marked for deeper analysis and reading

**Date:** 2026-10-06 · **Escalation:** #1978 · **Status:** marked for deeper analysis and reading (researcher, 2026-10-06). **Completed 2026-10-08 under #1989:** see [`m64-m47-marked-verses-completion-v1-20261008.md`](m64-m47-marked-verses-completion-v1-20261008.md).

**The verses.** These are the 29 uncited M64 × M47 shared verses that have no "same word pair, cited elsewhere" lead ([`m64-m47-uncited-verses-v1-20261006.md`](m64-m47-uncited-verses-v1-20261006.md)).
- Data: [`m64-m47-marked-verses-v2-20261008.csv`](m64-m47-marked-verses-v2-20261008.csv), with a `status` column and, since v2 (2026-10-08, #1989), the final status of each verse. v1 is in `archive/`.
- Script: [`m64-m47-marked-verses-m47-trace-v1-20261006.py`](m64-m47-marked-verses-m47-trace-v1-20261006.py), read-only.

## 1. Was the M47 folder searched?

**Not at first.** The cross-reference searched only the narrative chapters and the open threads register. This file adds a search of the M47 folder (`_analytics/Clusters/M47 - inner-seat/`): every current reading file (.md), section by section. Archived versions and the data CSVs were checked as well. Each verse is in the data CSVs (`cluster-M47-other-m-code-cooccurrence-*`, `*-pairs-with-distance-*`), so all 29 were in the M47 data.

**A search fault found and fixed on the way.** The citation reader did not know the short forms **1Co** and **2Co**, which the M47 files use. Script v2 (`verse-narrative-ot-crossref-v2-20261006.py`, v1 archived) adds them, and Php too. The narrative cross-reference was re-run with v2. The result is unchanged: the same 21 verses are cited and the same 35 are not.

## 2. Where the 29 are in the M47 work

| Route | Verses |
| --- | --- |
| **Read**: quoted in an M47 reading section | 25 |
| of which the section **is** a recorded source for a chapter | 15 |
| of which the section is **not** recorded as a source for any chapter | 10 |
| **Set aside**: only in data notes, the cluster cross-reference or a ruling item | 3 (2Sa 23:17, 1Ch 11:19, Isa 49:7) |
| **Not quoted**: in the M47 data only | 1 (Deu 18:6) |

**17 of the 29 are quoted in batch C §2, "Will, resolve, planning and choosing (M64)".** That is the M47 reading of exactly this pairing: §2.1 the heart plans and devises; §2.2 the intention of the heart; §2.3 choosing, soul and heart; §2.4 the mind-set of flesh and Spirit; §2.5 spirit and resolve.

## 3. Why they were missed: what the record shows

1. **Batch C §2 is not recorded as a source for any chapter.**
   - The narrative index ([`00-index-and-status-v1-20260930.md`](../../essay/spirit_soul_body/inner-being-narrative/00-index-and-status-v1-20260930.md), column "Built from (M47)") names batch C only once, as **C §1**, for Ch 5 *The soul*.
   - 10.6 *Wanting* and 10.7 *Choosing and setting direction*, where this material belongs by activity, are recorded only as "as Ch 10 v1". Part 10 as a whole is recorded as built from "cross-cutting §s of batches A–F".
   - Other §2 verses are cited, but in chapters with other recorded sources:
     - Gen 6:5, Pro 16:9 and Psa 140:2 in 10.4 *Thinking*, recorded as built from the origin-of-thought strand
     - Gen 8:21 in Ch 4, 11 and 12
     - Rom 8:6–7, 8:27 in Ch 2, 7, 10.9 and 12
     - Isa 42:1, Job 7:15 and Phili 1:22 in Ch 2, 7, 9 and 11
   - So the M64 section of the M47 reading had no chapter in the build record. Its verses reached the narrative only where another source brought them in.
2. **The M47 reset kept no verse-level record of what was used or left out.**
   - The index records sources by section only. No list says, verse by verse, where each M47 reading was placed, or that it was set aside.
   - The verse-level "Woven — where" record began with the strand ledgers, under #1918 ("every observation from a strand gets a recorded placement"). That came after the M47 batch reading (2026-09-27/28) and the first reset (2026-09-30).
   - So even where a verse sat in a recorded source section (15 verses, see the table in §4), choosing other verses from that section left no trace, and nothing flagged the ones not chosen.
3. **Some were set aside in the M47 reading itself, as tag mismatches or idioms.** Batch C §0 (data notes):
   - 2Sa 23:17 and 1Ch 11:19: H0014 as "he would not drink it". Kept only where it is the heart's or the spirit's refusal.
   - Jon 1:4: the ship "threatened" (*thought*) to break up, "a lexical curiosity only".
   - Lev 7:18: "credited".
   - Psa 35:4: "seek my life" as an idiom (§0.2), though it is also quoted in §2.1.
   - Isa 49:7 appears only in a ruling item about the *servant* tag (batch E §R2).
   - These were set aside for the cluster reading, not judged against an M64 × M47 question.
4. **Deu 18:6 was never quoted.**
   - Batch C says "896 pairs in 578 verses; all read". Its sections list chosen verses, not every verse, so an unlisted verse has no visible reading.
   - Deu 18:6 is the Levite who comes "when he desires" (*nephesh*) to "the place that the Lord will choose".

**In short:** the 29 were mostly read in M47, but read as M47 cluster material. The section that reads the M64 pairing (batch C §2) was never mapped to a chapter. The reset also recorded only which sections fed each chapter, not which verses were used or left out. None of this judges whether the verses add insight; that is the deeper reading now marked.

## 4. The 29 verses

### Exo 10:27 · read

> But the Lord hardened Pharaoh’s heart, and he would not let them go.

- **M64:** H0014 be willing "he would"
- **M47:** H3820A heart "heart"
- **In M47:** G §3.3 One verb: courage or hardening (*ḥāzaq*); C §0. Data notes; C §9.3 Hardening
- **Recorded chapter source:** none

### Exo 35:5 · read

> Take from among you a contribution to the Lord. Whoever is of a generous heart, let him bring the Lord’s contribution: gold, silver, and bronze;

- **M64:** H5081G noble: willing "generous"
- **M47:** H3820A heart "heart"
- **In M47:** dep §2.1 Heart (H3820A, H3824, H3821, H3825, H3826, H7907, G2588; with G258; D §R4 — H5081G "willing / generous" in M09 Humility & Lowliness; D §10.4 Willing heart and willing spirit (R4)
- **Recorded chapter source:** dep §2.1 -> Ch 4

### Exo 35:22 · read

> So they came, both men and women. All who were of a willing heart brought brooches and earrings and signet rings and armlets, all sorts of gold objects, every man dedicating an offering of gold to the Lord.

- **M64:** H5081G noble: willing "willing"
- **M47:** H3820A heart "heart"
- **In M47:** dep §2.1 Heart (H3820A, H3824, H3821, H3825, H3826, H7907, G2588; with G258; D §R4 — H5081G "willing / generous" in M09 Humility & Lowliness; D §10.4 Willing heart and willing spirit (R4)
- **Recorded chapter source:** dep §2.1 -> Ch 4

### Lev 7:18 · read

> If any of the flesh of the sacrifice of his peace offering is eaten on the third day, he who offers it shall not be accepted, neither shall it be credited to him. It is tainted, and he who eats of it shall bear his iniquity.

- **M64:** H2803H to devise: count "credited"
- **M47:** H1320 flesh "flesh"; H5315I soul: myself "he"
- **In M47:** D §3.1 The soul as the one who sins; D §8.4 Flesh / body uncleanness; C §0. Data notes
- **Recorded chapter source:** none

### Deu 18:6 · not quoted

> “And if a Levite comes from any of your towns out of all Israel, where he lives —and he may come when he desires — to the place that the Lord will choose,

- **M64:** H0977 to choose "choose"
- **M47:** H5315L soul: appetite "desires"
- **In M47:** data CSVs only
- **Recorded chapter source:** none

### 2Sa 23:17 · set aside

> and said, “ Far be it from me, O Lord, that I should do this. Shall I drink the blood of the men who went at the risk of their lives?” Therefore he would not drink it. These things the three mighty men did.

- **M64:** H0014 be willing "he would"
- **M47:** H5315H soul: life "lives"
- **In M47:** C §X. Cluster cross-reference — where each cluster appears in this file; C §0. Data notes
- **Recorded chapter source:** none

### 1Ki 8:48 · read

> if they repent with all their heart and with all their soul in the land of their enemies, who carried them captive, and pray to you toward their land, which you gave to their fathers, the city that you have chosen, and the house that I have built for your name,

- **M64:** H0977 to choose "chosen"
- **M47:** H3824 heart "heart"; H5315G soul "soul"
- **In M47:** dep §3.2 Totality and wholeness formulas; E §13. Cross-cutting observations for Batch E [Claude reading]; C §2.3 Choosing — soul and heart; C §8.1 Returning with heart and soul; C §11. Cross-cutting observations for Batch C [Claude reading]
- **Recorded chapter source:** dep §3.2 -> Ch 3; E §13 -> Part 10 ("cross-cutting §s of batches A-F"); C §11 -> Part 10 ("cross-cutting §s of batches A-F")

### 1Ki 12:33 · read

> He went up to the altar that he had made in Bethel on the fifteenth day in the eighth month, in the month that he had devised from his own heart. And he instituted a feast for the people of Israel and went up to the altar to make offerings.

- **M64:** H0908 to devise "devised"
- **M47:** H3820A heart "from"
- **In M47:** C §2.1 The heart plans and devises
- **Recorded chapter source:** none

### 1Ch 11:19 · set aside

> and said, “ Far be it from me before my God that I should do this. Shall I drink the lifeblood of these men? For at the risk of their lives they brought it.” Therefore he would not drink it. These things did the three mighty men.

- **M64:** H0014 be willing "he would"
- **M47:** H5315H soul: life "risk"; H5315H soul: life "lives"
- **In M47:** C §X. Cluster cross-reference — where each cluster appears in this file; C §0. Data notes
- **Recorded chapter source:** none

### 2Ch 6:38 · read

> if they repent with all their heart and with all their soul in the land of their captivity to which they were carried captive, and pray toward their land, which you gave to their fathers, the city that you have chosen and the house that I have built for your name,

- **M64:** H0977 to choose "chosen"
- **M47:** H3820A heart "heart"; H5315G soul "soul"
- **In M47:** dep §3.2 Totality and wholeness formulas; C §2.3 Choosing — soul and heart; C §8.1 Returning with heart and soul
- **Recorded chapter source:** dep §3.2 -> Ch 3

### 2Ch 7:16 · read

> For now I have chosen and consecrated this house that my name may be there forever. My eyes and my heart will be there for all time.

- **M64:** H0977 to choose "chosen"
- **M47:** H3820A heart "heart"
- **In M47:** D §7.4 The OT inner seat and the holy; C §2.3 Choosing — soul and heart; C §11. Cross-cutting observations for Batch C [Claude reading]
- **Recorded chapter source:** C §11 -> Part 10 ("cross-cutting §s of batches A-F")

### 2Ch 29:31 · read

> Then Hezekiah said, “You have now consecrated yourselves to the Lord. Come near; bring sacrifices and thank offerings to the house of the Lord.” And the assembly brought sacrifices and thank offerings, and all who were of a willing heart brought burnt offerings.

- **M64:** H5081G noble: willing "willing"
- **M47:** H3820A heart "heart"
- **In M47:** D §R4 — H5081G "willing / generous" in M09 Humility & Lowliness; D §10.4 Willing heart and willing spirit (R4)
- **Recorded chapter source:** none

### Neh 6:8 · read

> Then I sent to him, saying, “ No such things as you say have been done, for you are inventing them out of your own mind.”

- **M64:** H0908 to devise "inventing"
- **M47:** H3820A heart "mind"
- **In M47:** dep §2.1 Heart (H3820A, H3824, H3821, H3825, H3826, H7907, G2588; with G258; C §2.1 The heart plans and devises
- **Recorded chapter source:** dep §2.1 -> Ch 4

### Psa 17:3 · read

> You have tried my heart, you have visited me by night, you have tested me, and you will find nothing; I have purposed that my mouth will not transgress.

- **M64:** H2161 to plan "purposed"
- **M47:** H3820A heart "heart"
- **In M47:** E §8.1 God tests the heart; C §2.2 The intention of the heart
- **Recorded chapter source:** none

### Psa 35:4 · read

> Let them be put to shame and dishonor who seek after my life! Let them be turned back and disappointed who devise evil against me!

- **M64:** H2803I to devise: devise "devise"
- **M47:** H5315H soul: life "life"
- **In M47:** C §0. Data notes; C §2.1 The heart plans and devises; C §7.5 "Seek my life" — the soul-life hunted (§0.2)
- **Recorded chapter source:** none

### Pro 10:20 · read

> The tongue of the righteous is choice silver; the heart of the wicked is of little worth.

- **M64:** H0977 to choose "choice"
- **M47:** H3820A heart "heart"
- **In M47:** C §2.3 Choosing — soul and heart
- **Recorded chapter source:** none

### Isa 49:7 · set aside

> Thus says the Lord, the Redeemer of Israel and his Holy One, to one deeply despised, abhorred by the nation, the servant of rulers: “ Kings shall see and arise; princes, and they shall prostrate themselves; because of the Lord, who is faithful, the Holy One of Israel, who has chosen you.”

- **M64:** H0977 to choose "chosen"
- **M47:** H5315J soul: person "one"
- **In M47:** E §R2 — H5650 *ʿeved* "servant / slave" in M36 Worship & Service
- **Recorded chapter source:** none

### Isa 66:3 · read

> “He who slaughters an ox is like one who kills a man; he who sacrifices a lamb, like one who breaks a dog’s neck; he who presents a grain offering, like one who offers pig’s blood; he who makes a memorial offering of frankincense, like one who blesses an idol. These have chosen their own ways, and their soul delights in their abominations;

- **M64:** H0977 to choose "chosen"
- **M47:** H5315G soul "soul"
- **In M47:** D §2.3 The soul and wickedness; H §4.4 ◆ Fringe (M76); C §1.10 Evil desire of the soul; C §2.3 Choosing — soul and heart
- **Recorded chapter source:** C §1.10 -> Ch 5

### Eze 3:7 · read

> But the house of Israel will not be willing to listen to you, for they are not willing to listen to me: because all the house of Israel have a hard forehead and a stubborn heart.

- **M64:** H0014 be willing "willing"; H0014 be willing "willing"
- **M47:** H3820A heart "heart"
- **In M47:** A §R4 — H7186 "severe" in M24 Faintness & Despair; A §0. Notes on the data before reading; B §3.2 A hardened heart does not listen; G §3.3 One verb: courage or hardening (*ḥāzaq*); C §0. Data notes; C §9.3 Hardening
- **Recorded chapter source:** none

### Eze 14:7 · read

> For any one of the house of Israel, or of the strangers who sojourn in Israel, who separates himself from me, taking his idols into his heart and putting the stumbling block of his iniquity before his face, and yet comes to a prophet to consult me through him, I the Lord will answer him myself.

- **M64:** H5144A to dedicate "separates"
- **M47:** H3820A heart "heart"
- **In M47:** dep §2.1 Heart (H3820A, H3824, H3821, H3825, H3826, H7907, G2588; with G258; G §9.3 Stumbling of heart — one noun, several objects (*mikšôl*); D §3.3 Sin and the heart; C §7.6 Illegitimate and restless seeking
- **Recorded chapter source:** dep §2.1 -> Ch 4

### Dan 5:21 · read

> He was driven from among the children of mankind, and his mind was made like that of a beast, and his dwelling was with the wild donkeys. He was fed grass like an ox, and his body was wet with the dew of heaven, until he knew that the Most High God rules the kingdom of mankind and sets over it whom he will.

- **M64:** H6634 to will "he will"
- **M47:** H3825 heart "mind"
- **In M47:** dep §2.1 Heart (H3820A, H3824, H3821, H3825, H3826, H7907, G2588; with G258; dep §4. Fringe observations collected (quick list); G §12.1 The heart lifted, glory taken; C §2.5 ◆ Spirit and resolve — fringe
- **Recorded chapter source:** dep §2.1 -> Ch 4

### Dan 6:3 · read

> Then this Daniel became distinguished above all the other high officials and satraps, because an excellent spirit was in him. And the king planned to set him over the whole kingdom.

- **M64:** H6246 to plan "planned"
- **M47:** H7308 spirit "spirit"
- **In M47:** C §2.5 ◆ Spirit and resolve — fringe
- **Recorded chapter source:** none

### Jon 1:4 · read

> But the Lord hurled a great wind upon the sea, and there was a mighty tempest on the sea, so that the ship threatened to break up.

- **M64:** H2803I to devise: devise "threatened"
- **M47:** H7307H spirit: breath "wind"
- **In M47:** dep §2.3 Spirit — *rûaḥ / pneuma* (H7307 G–J, H7308, G4151 G/H; with G4152,; C §X. Cluster cross-reference — where each cluster appears in this file; C §0. Data notes
- **Recorded chapter source:** dep §2.3 -> Ch 6

### Mat 12:18 · read

> “ Behold, my servant whom I have chosen, my beloved with whom my soul is well pleased. I will put my Spirit upon him, and he will proclaim justice to the Gentiles.

- **M64:** G0140 to choose "chosen"
- **M47:** G5590G soul "soul"; G4151G spirit/breath: spirit "Spirit"
- **In M47:** dep §3.10 God, animals and things — the vocabulary is not limited to humans; H §6.5 ◆ Fringe (M26); C §1.12 Divine desire and delight; C §2.3 Choosing — soul and heart
- **Recorded chapter source:** C §1.12 -> Ch 5

### Act 11:23 · read

> When he came and saw the grace of God, he was glad, and he exhorted them all to remain faithful to the Lord with steadfast purpose,

- **M64:** G4286 purpose "steadfast"
- **M47:** G2588 heart "purpose"
- **In M47:** C §2.2 The intention of the heart
- **Recorded chapter source:** none

### 1Cor 4:5 · read

> Therefore do not pronounce judgment before the time, before the Lord comes, who will bring to light the things now hidden in darkness and will disclose the purposes of the heart. Then each one will receive his commendation from God.

- **M64:** G1012 plan "purposes"
- **M47:** G2588 heart "heart"
- **In M47:** dep §2.1 Heart (H3820A, H3824, H3821, H3825, H3826, H7907, G2588; with G258; B §7. Reasoning, judging and interpreting (M63); E §3.3 Glory, the Spirit and the heart (NT); exaltation; C §2.2 The intention of the heart
- **Recorded chapter source:** dep §2.1 -> Ch 4

### 1Cor 12:11 · read

> All these are empowered by one and the same Spirit, who apportions to each one individually as he wills.

- **M64:** G1014 to plan "wills"
- **M47:** G4151G spirit/breath: spirit "Spirit"
- **In M47:** C §2.4 The mind-set of flesh and Spirit (*phronēma*); C §11. Cross-cutting observations for Batch C [Claude reading]
- **Recorded chapter source:** C §11 -> Part 10 ("cross-cutting §s of batches A-F")

### 2Cor 1:17 · read

> Was I vacillating when I wanted to do this? Do I make my plans according to the flesh, ready to say “ Yes, yes ” and “ No, no ” at the same time?

- **M64:** G1011 to plan "wanted"; G1011 to plan "make"; G1011 to plan "plans"
- **M47:** G4561 flesh "flesh"
- **In M47:** dep §2.4 Flesh and body — *bāśār / sarx* (H1320, H1321, H7607, G4561); C §2.4 The mind-set of flesh and Spirit (*phronēma*)
- **Recorded chapter source:** dep §2.4 -> Ch 7

### 2Th 2:13 · read

> But we ought always to give thanks to God for you, brothers beloved by the Lord, because God chose you as the firstfruits to be saved, through sanctification by the Spirit and belief in the truth.

- **M64:** G0138 to choose "chose"
- **M47:** G4151G spirit/breath: spirit "Spirit"
- **In M47:** D §7.2 Holiness of the human inner seat; E §11.1 The soul redeemed; salvation spoken to the soul (M79); C §2.3 Choosing — soul and heart
- **Recorded chapter source:** E §11.1 -> Ch 14
