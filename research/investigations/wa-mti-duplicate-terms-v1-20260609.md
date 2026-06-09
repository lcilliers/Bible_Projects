# mti_terms duplicate-term assessment (OT-DBR-009, dedup angle)

> READ-ONLY (`scripts/_assess_mti_duplicate_terms.py`). Groups mti_terms by base Strong's; within each base, flags a sibling as a DUPLICATE when ≥90% of its active verses are contained in the largest sibling. Genuine sub-entries (disjoint verses) are NOT flagged. No DB writes.

**41 duplicate term rows** across **39 base Strong's**.  They carry **2209 duplicated active verse_context rows** and **5049 of 145720 l2_mechanical findings (3%)** — all redundant copies.

## Duplicate clusters — ranked by duplicated verses

| base | keeper (kept) | sense on keeper | duplicate rows (verses, %inside) |
|---|---|---|---|
| H5971 | H5971H am (FLAG, 430v) | ? | H5971I (430, 100%), H5971L (430, 100%) |
| H2416 | H2416B chay (M25, 207v) | kinsfolk | H2416D (207, 100%), H2416A (207, 100%) |
| H2617 | H2617A che.sed (M05, 240v) | goodness, kindness, faithfulness | H2617B (169, 100%) |
| H0352 | H0352C a.yil (T2, 139v) | ? | H0352D (139, 100%) |
| H3722 | H3722B ka.phar (M38, 93v) |  | H3722A (81, 100%) |
| H7311 | H7311A rum (M08, 181v) |  | H7311B (74, 100%) |
| H2603 | H2603B cha.nan (FLAG, 72v) | ? | H2603A (72, 100%) |
| H2654 | H2654A cha.phets (M04, 69v) | of men to take pleasure in, delight in to del | H2654B (67, 100%) |
| H5355 | H5355A na.qi (M12, 39v) | clean, free from, exempt, clear, innocent fre | H5355B (39, 100%) |
| H2530 | H2530B cha.mu.dah (M28, 20v) | desirableness, preciousness | H2530A (18, 100%) |
| H6186 | H6186B a.rakh (M26, 67v) |  | H6186A (17, 100%) |
| H6087 | H6087B a.tsav (FLAG, 15v) | ? | H6087A (13, 100%) |
| H5273 | H5273A na.im (M04, 13v) | pleasant, delightful, sweet, lovely, agreeabl | H5273B (11, 100%) |
| H4172 | H4172A mo.rah (M01, 11v) | fear, reverence, terror fear, terror reverenc | H4172B (11, 100%) |
| H7423 | H7423A re.miy.yah (M14, 10v) | deceit, treachery | H7423B (10, 100%) |
| H1524 | H1524A gil (M04, 9v) | a rejoicing | H1524B (8, 100%) |
| H2532 | H2532A chem.dah (M28, 9v) | desire, that which is desirable | H2532B (8, 100%) |
| H2836 | H2836A cha.shaq (M28, 8v) | to love, be attached to, long for | H2836B (8, 100%) |
| H6105 | H6105A a.tsom (M23, 6v) | to be mighty to be numerous | H6105B (6, 100%) |
| H6089 | H6089A e.tsev (M03, 6v) | pain, hurt, toil, sorrow, labour, hardship pa | H6089B (5, 100%) |
| H4888 | H4888A mish.chah (T2, 4v) | ? | H4888B (4, 100%) |
| H5356 | H5356A niq.qa.von (M07, 4v) | innocency freedom from guilt, innocency freed | H5356B (4, 100%) |
| H2258 | H2258A cha.vol (FLAG, 3v) | ? | H2258B (3, 100%) |
| H5730 | H5730A e.den (T2, 3v) | ? | H5730B (3, 100%) |
| H3512 | H3512A ka.ah (M20, 4v) |  | H3512B (3, 100%) |
| H2892 | H2892A to.har (M12, 3v) | purity, purification, purifying purity purify | H2892B (3, 100%) |
| H6090 | H6090A o.tsev (M03, 3v) | pain, sorrow | H6090B (3, 100%) |
| G4151 | G4151G pneuma (M25, 341v) | wind, breath, things which are commonly perce | G4151H (3, 100%) |
| G5545 | G5545 chrisma (T2, 2v) | ? | G5545B (2, 100%) |
| H2616 | H2616B cha.sad (M05, 3v) |  | H2616A (2, 100%) |
| H7442 | H7442B ra.nan (M42, 53v) |  | H7442A (2, 100%) |
| H4937 | H4937A mish.an (M19, 2v) | support, staff Also means: mish.en (מִשְׁעֵן  | H4937B (2, 100%) |
| H3520 | H3520A ka.vod (M22, 2v) | glorious | H3520B (2, 100%) |
| H1793 | H1793A dak.ka (M09, 2v) | adj contrite | H1793B (2, 100%) |
| H6696 | H6696B tsur (M02, 32v) |  | H6696A (1, 100%) |
| H7067 | H7067H qan.na (M02, 5v) | jealous (only of God) | H7067G (1, 100%) |
| H0197 | H0197H u.lam (FLAG, 1v) | ? | H0197I (1, 100%) |
| H0193 | H0193A ul (M23, 1v) | prominence body, belly (contemptuous) | H0193B (1, 100%) |
| H4206 | H4206A me.zach (FLAG, 1v) | ? | H4206B (1, 100%) |

## Wrong sense labels riding on duplicates (keeper vs duplicate sense)

| base | keeper sense | duplicate | duplicate sense |
|---|---|---|---|
| H2416 | kinsfolk | H2416D | community |
| H2416 | kinsfolk | H2416A | adj 1) living, alive 1a) green (of vegetation |
| H2617 | goodness, kindness, faithfulness | H2617B | a reproach, shame |
| H3722 |  | H3722A | to be covered |
| H2603 |  | H2603A | to be shown favour, be shown consideration |
| H5355 | clean, free from, exempt, clear, innocent fre | H5355B | innocent Another spelling of na.qi (נָקִי "in |
| H2530 | desirableness, preciousness | H2530A | to be desirable 1c) |
| H6087 |  | H6087A | to be in pain, be pained, be grieved |
| H5273 | pleasant, delightful, sweet, lovely, agreeabl | H5273B | singing, sweetly sounding, musical |
| H4172 | fear, reverence, terror fear, terror reverenc | H4172B | appoint terror (i.e. some awe-inspiring exhib |
| H7423 | deceit, treachery | H7423B | laxness, slackness, slackening |
| H2532 | desire, that which is desirable | H2532B | desirableness, preciousness |
| H5356 | innocency freedom from guilt, innocency freed | H5356B | bluntness) |
| H5730 |  | H5730B | delight |
| H3512 |  | H3512B | be cowed |
| H2892 | purity, purification, purifying purity purify | H2892B | clearness, lustre |
| H2616 |  | H2616A | to show kindness to oneself |
| H4937 | support, staff Also means: mish.en (מִשְׁעֵן  | H4937B | support, staff Another spelling of mish.an (מ |
| H3520 | glorious | H3520B | abundance, riches, wealth |
| H6696 |  | H6696A | to confine, secure to shut in, beseige to shu |
| H0193 | prominence body, belly (contemptuous) | H0193B | nobles, wealthy men |
