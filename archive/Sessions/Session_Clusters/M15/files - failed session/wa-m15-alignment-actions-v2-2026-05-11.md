# WA-M15 VCG Alignment Action List — v2
**File:** wa-m15-alignment-actions-v2-2026-05-11.md
**Date:** 2026-05-11
**Version:** v2 — every verse addressed by vr_id; per-verse action for all 298 M15-A rows
**Supersedes:** wa-m15-alignment-actions-v1-2026-05-11.md
**Source DB state:** wa-cluster-M15-comprehensive-v8-20260511.md
**Analysis basis:** wa-m15-[a-g]-verse-meanings-v2-2026-05-11.md (all eight sub-groups)

**Action codes:**
- CONFIRM — verse correctly placed; no change needed
- MOVE — reassign verse to a different VCG (vr_id, from → to)
- STATUS — change verse status field (G/SA/P)
- CREATE-VCG — new verse_context_group row needed before this move can land
- UPDATE-DESC — VCG description needs editing
- FLAG — no immediate action; note for researcher review

---

## M15-A — 298 verses, 16 DB VCGs

### VCG inventory (DB state)

| VCG code | Term | Description | DB count |
|---|---|---|---|
| 528-001 | H2450 cha.kham | Wisdom as constituted inner quality of the person | 77 |
| 528-003 | H2450 cha.kham | Wisdom turned back on itself / self-attributed | 11 |
| 528-004 | H2803G cha.shav / H2450 cha.kham | Spirit-given craft skill for sacred construction | 29 |
| 528-005 | H2450 cha.kham | Wisdom as governance qualification / institutional role | 26 |
| 527-001 | H8454 tu.shiy.yah | Sound wisdom as effective inner resource | 12 |
| 525-001 | H7922 se.khel | Practical inner quality of good sense | 19 |
| 532-002 | H2452 chokh.mah / G4678 sofia | Wisdom as divine gift received | 19 |
| 532-003 | G4678 sofia | Sofia visible in a particular person | 14 |
| 3459-001 | G5429 fronimos | Practical shrewdness as inner quality | 14 |
| 996-001 | G5426 froneō | Inner orientation of the whole person | 19 |
| 6668-001 | H2445 chak.kim | Court wise-men class as foil for Spirit-given wisdom | 13 |
| 6696-001 | H2452 chokh.mah / G4680 sofos | Wisdom as divine attribute belonging to God | 11 |
| 4458-001 | G4678 sofia / G4680 sofos | Human wisdom overturned by the cross | 37 |
| 1174-001 | H2803G cha.shav | Creative inner faculty of design / providential mercy | 1 |
| 1174-002 | H2803G cha.shav | Inner scheming against another | 3 |
| 6676-001 | G0781 asofos | Absence of wisdom as inner-being deficit | 1 |

**P-status rows in M15-A (2):** Jer 9:17 (vr_id 7442), Obd 8 (vr_id 208270)

---

### Per-verse action table — all 298 rows

| vr_id | Reference | Term | Current VCG | Action | Target / Note |
|---|---|---|---|---|---|
| 7322 | Gen 41:8 | H2450 cha.kham | 528-005 | CONFIRM | Egyptian court wise men summoned — professional class; 528-005 correct |
| 7323 | Gen 41:33 | H2450 cha.kham | 528-005 | CONFIRM | Discerning and wise man sought for governance — 528-005 correct |
| 7324 | Gen 41:39 | H2450 cha.kham | 528-005 | CONFIRM | None so discerning and wise — wisdom recognised in Joseph; governance context |
| 7325 | Exo 7:11 | H2450 cha.kham | 528-005 | CONFIRM | Pharaoh's wise men and sorcerers — professional court class |
| 54614 | Exo 26:1 | H2803G cha.shav | 528-004 | CONFIRM | Curtains with cherubim skillfully worked — sacred craft |
| 54615 | Exo 26:31 | H2803G cha.shav | 528-004 | CONFIRM | Veil with cherubim skillfully worked — sacred craft |
| 7326 | Exo 28:3 | H2450 cha.kham | 528-004 | CONFIRM | Filled with spirit of skill to make Aaron's garments — Spirit-given sacred craft |
| 54617 | Exo 28:6 | H2803G cha.shav | 528-004 | CONFIRM | Ephod skillfully worked — sacred craft |
| 54616 | Exo 28:15 | H2803G cha.shav | 528-004 | CONFIRM | Breastpiece in skilled work — sacred craft |
| 54618 | Exo 31:4 | H2803G cha.shav | 528-004 | CONFIRM | Devise artistic designs — sacred craft commission |
| 7327 | Exo 31:6 | H2450 cha.kham | 528-004 | CONFIRM | I have given to all able men ability — God-given craft capacity |
| 7328 | Exo 35:10 | H2450 cha.kham | 528-004 | CONFIRM | Every skillful craftsman — Spirit-given capacity for sanctuary |
| 7329 | Exo 35:25 | H2450 cha.kham | 528-004 | CONFIRM | Every skillful woman spun — Spirit-given craft |
| 54619 | Exo 35:32 | H2803G cha.shav | 528-004 | CONFIRM | Devise artistic designs — Bezalel's commission |
| 54620 | Exo 35:35 | H2803G cha.shav | 528-004 | CONFIRM | Skilled designer — the deviser of patterns |
| 7330 | Exo 36:1 | H2450 cha.kham | 528-004 | CONFIRM | Every craftsman in whom the Lord put skill and intelligence |
| 7331 | Exo 36:2 | H2450 cha.kham | 528-004 | CONFIRM | Every craftsman in whose mind the Lord had put skill |
| 7332 | Exo 36:4 | H2450 cha.kham | 528-004 | CONFIRM | All the craftsmen doing every sort of task on the sanctuary |
| 7333 | Exo 36:8 | H2450 cha.kham | 528-004 | CONFIRM | Craftsmen made the tabernacle curtains — cha.kham row correct |
| **54622** | **Exo 36:8** | **H2803G cha.shav** | **4458-001** | **MOVE** | **→ 528-004** — sacred craft design; misrouted to cross-wisdom group |
| 54621 | Exo 36:35 | H2803G cha.shav | 528-004 | CONFIRM | Veil with cherubim skillfully worked — sacred craft |
| 54623 | Exo 38:23 | H2803G cha.shav | 528-004 | CONFIRM | Oholiab — engraver and designer — sacred craft |
| 54624 | Exo 39:3 | H2803G cha.shav | 528-004 | CONFIRM | Skilled design in gold thread — sacred craft |
| 54625 | Exo 39:8 | H2803G cha.shav | 528-004 | CONFIRM | Breastpiece in skilled work — sacred craft |
| 7334 | Deu 1:13 | H2450 cha.kham | 528-005 | CONFIRM | Choose wise, understanding, experienced men — governance qualification |
| 7335 | Deu 1:15 | H2450 cha.kham | 528-005 | CONFIRM | Wise and experienced men set as heads — governance |
| 7336 | Deu 4:6 | H2450 cha.kham | 528-001 | CONFIRM | Your wisdom and understanding — covenant obedience as visible inner quality; 528-001 correct |
| 7337 | Deu 16:19 | H2450 cha.kham | 528-005 | CONFIRM | Bribe blinds the eyes of the wise — wisdom as judicial qualification; potential failure |
| 7338 | Deu 32:6 | H2450 cha.kham | 528-003 | CONFIRM | Foolish and senseless people — wisdom negated; 528-003 correct |
| 208269 | Judg 5:29 | H2450 cha.kham | 528-001 | CONFIRM | Wisest princesses answer — inner quality serving self-deception; 528-001 holds |
| 7139 | 1Sa 25:3 | H7922 se.khel | 525-001 | CONFIRM | Abigail was discerning — se.khel as personal characterising quality |
| 7339 | 2Sa 13:3 | H2450 cha.kham | 528-001 | CONFIRM | Jonadab was a very crafty man — wisdom turned to manipulation; 528-001 holds |
| 7340 | 2Sa 14:2 | H2450 cha.kham | 528-001 | CONFIRM | Wise woman from Tekoa — wisdom as inner quality enabling role |
| **54610** | **2Sa 14:14** | **H2803G cha.shav** | **1174-001** | **MOVE** | **→ M15-E 3334-002** — God devises means for mercy; divine purposive planning, not craft design |
| 7341 | 2Sa 14:20 | H2450 cha.kham | 528-001 | CONFIRM | Wisdom like the wisdom of the angel of God — superlative inner quality |
| 7342 | 2Sa 20:16 | H2450 cha.kham | 528-001 | CONFIRM | Wise woman called from city — wisdom enabling intervention |
| **7343** | **1Ki 2:9** | **H2450 cha.kham** | **4458-001** | **MOVE** | **→ 528-005** — David attributes wisdom to Solomon as governance qualification; not cross-opposition |
| 7344 | 1Ki 3:12 | H2450 cha.kham | 528-005 | CONFIRM | I give you a wise and discerning mind — God-given governance wisdom |
| 7345 | 1Ki 5:7 | H2450 cha.kham | 528-005 | CONFIRM | Given to David a wise son to be over this great people — governance |
| 7140 | 1Ch 22:12 | H7922 se.khel | 525-001 | CONFIRM | May the Lord grant you discretion and understanding — God-given se.khel |
| 7346 | 1Ch 22:15 | H2450 cha.kham | 528-004 | CONFIRM | Craftsmen without number, skilled in working — craft capacity; secular but within 528-004 scope |
| 7141 | 1Ch 26:14 | H7922 se.khel | 525-001 | CONFIRM | Zechariah a shrewd counselor — se.khel as personal defining quality |
| 7347 | 2Ch 2:7 | H2450 cha.kham | 528-004 | CONFIRM | Man skilled to work in gold etc — craft capacity for temple |
| 7348 | 2Ch 2:12 | H2450 cha.kham | 528-001 | CONFIRM | A wise son who has discretion and understanding — inner quality of Solomon |
| 7142 | 2Ch 2:12 | H7922 se.khel | 525-001 | CONFIRM | Discretion and understanding in Solomon — se.khel as part of quality trio |
| 7349 | 2Ch 2:13 | H2450 cha.kham | 528-004 | CONFIRM | Skilled man who has understanding, Huram-abi — craft capacity |
| 7350 | 2Ch 2:14 | H2450 cha.kham | 528-004 | CONFIRM | Craftsmen (cha.kham row) — collaborative craft capacity; cha.kham row correct |
| **54608** | **2Ch 2:14** | **H2803G cha.shav** | **4458-001** | **MOVE** | **→ 528-004** — execute any design assigned; craft design capacity; misrouted to cross-wisdom group |
| 54609 | 2Ch 26:15 | H2803G cha.shav | 528-004 | CONFIRM | Skillful men inventing machines for military — craft devising; FLAG desc mismatch (not sacred) |
| 7143 | 2Ch 30:22 | H7922 se.khel | 525-001 | CONFIRM | Levites who showed good skill in service — recognised se.khel in liturgy |
| 209175 | Ezr 7:25 | H2452 chokh.mah | 532-002 | CONFIRM | Wisdom of your God in your hand — gift enabling governance; 532-002 correct |
| 7144 | Ezr 8:18 | H7922 se.khel | 525-001 | CONFIRM | Man of discretion by God's good hand — God-sourced se.khel |
| 7145 | Neh 8:8 | H7922 se.khel | 525-001 | CONFIRM | Gave the sense so people understood — se.khel enabling reception |
| 7351 | Est 1:13 | H2450 cha.kham | 528-005 | CONFIRM | Wise men who knew the times — institutional advisors versed in law |
| 7352 | Est 6:13 | H2450 cha.kham | 528-005 | CONFIRM | Haman's wise men — institutional advisors; accurate counsel despite context |
| **54612** | **Est 8:3** | **H2803G cha.shav** | **1174-002** | **MOVE** | **→ M15-E 3334-001** — evil plan devised against Jews; belongs with purposive-evil devising |
| **54613** | **Est 9:25** | **H2803G cha.shav** | **1174-002** | **MOVE** | **→ M15-E 3334-001** — evil plan that rebounds; same group |
| 7310 | Job 5:12 | H8454 tu.shiy.yah | 527-001 | CONFIRM | Hands achieve no success — tu.shiy.yah as effective outcome withheld; 527-001 correct |
| 7353 | Job 5:13 | H2450 cha.kham | 528-001 | CONFIRM | He catches the wise in their own craftiness — wisdom turning against possessor |
| 7311 | Job 6:13 | H8454 tu.shiy.yah | 527-001 | CONFIRM | Resource driven from me — tu.shiy.yah as inner sustaining resource |
| 7354 | Job 9:4 | H2450 cha.kham | 4458-001 | CONFIRM | He is wise in heart and mighty — divine wisdom; this is God's wisdom not human; FLAG — could fit 6696-001 better but not a critical move |
| 7312 | Job 11:6 | H8454 tu.shiy.yah | 527-001 | CONFIRM | Manifold in understanding — tu.shiy.yah as divine inexhaustible wisdom-resource |
| 7313 | Job 12:16 | H8454 tu.shiy.yah | 527-001 | CONFIRM | Strength and sound wisdom with him — divine attribute |
| 7355 | Job 15:2 | H2450 cha.kham | 528-005 | CONFIRM | Should a wise man answer with windy knowledge — wise person's speech standard |
| 7356 | Job 15:18 | H2450 cha.kham | 528-005 | CONFIRM | What wise men have told — wisdom transmitted through tradition |
| 7146 | Job 17:4 | H7922 se.khel | 525-001 | CONFIRM | Closed their hearts to understanding — se.khel in the heart; God-sourced |
| 7357 | Job 17:10 | H2450 cha.kham | 528-005 | CONFIRM | I shall not find a wise man among you — wise person as absent |
| 7314 | Job 26:3 | H8454 tu.shiy.yah | 527-001 | CONFIRM | Plentifully declared sound knowledge — ironic; tu.shiy.yah as the real thing |
| 7315 | Job 30:22 | H8454 tu.shiy.yah | 527-001 | FLAG | "You toss me" — disputed rendering; meaning uncertain; confirm in 527-001 but note for researcher |
| 7358 | Job 34:2 | H2450 cha.kham | 528-005 | CONFIRM | Hear my words, you wise men — wise as competent hearers |
| 7359 | Job 34:34 | H2450 cha.kham | 528-005 | CONFIRM | The wise man who hears me — inner quality enabling right hearing |
| 7360 | Job 37:24 | H2450 cha.kham | 528-003 | CONFIRM | He does not regard any wise in their own conceit — self-attributed wisdom |
| **54626** | **Psa 35:20** | **H2803G cha.shav** | **1174-002** | **MOVE** | **→ M15-E 3334-001** — devising words of deceit against the quiet; evil scheming |
| 7361 | Psa 49:10 | H2450 cha.kham | 528-001 | CONFIRM | Even the wise die — limits of wisdom before mortality |
| 7362 | Psa 107:43 | H2450 cha.kham | 528-001 | CONFIRM | Whoever is wise let him attend — wisdom enabling perception of God's acts |
| 7147 | Psa 111:10 | H7922 se.khel | 525-001 | CONFIRM | Good understanding — se.khel as fruit of practising the fear of the Lord |
| 7363 | Pro 1:5 | H2450 cha.kham | 528-001 | CONFIRM | Let the wise hear and increase in learning — receptivity as mark of wisdom |
| 7364 | Pro 1:6 | H2450 cha.kham | 528-001 | CONFIRM | Words of the wise and their riddles — wisdom requiring wisdom to receive |
| 7316 | Pro 2:7 | H8454 tu.shiy.yah | 527-001 | CONFIRM | Stores up sound wisdom for the upright — divine resource for the faithful |
| 7148 | Pro 3:4 | H7922 se.khel | 525-001 | CONFIRM | Good success — se.khel producing outcomes |
| 7365 | Pro 3:7 | H2450 cha.kham | 528-003 | CONFIRM | Be not wise in your own eyes — self-attributed wisdom warned against |
| 7317 | Pro 3:21 | H8454 tu.shiy.yah | 527-001 | CONFIRM | Keep sound wisdom and discretion — tu.shiy.yah retained as protective resource |
| 7366 | Pro 3:35 | H2450 cha.kham | 528-003 | CONFIRM | The wise will inherit honour — outcome of wisdom; note this could fit 528-001 but 528-003 acceptable |
| 7318 | Pro 8:14 | H8454 tu.shiy.yah | 527-001 | CONFIRM | I have counsel and sound wisdom — Wisdom personified claims tu.shiy.yah |
| 7367 | Pro 9:8 | H2450 cha.kham | 528-001 | CONFIRM | Reprove a wise man and he will love you — wisdom's receptivity to correction |
| 7368 | Pro 9:9 | H2450 cha.kham | 528-001 | CONFIRM | Give instruction to a wise man — wisdom grows with instruction |
| 7369 | Pro 10:1 | H2450 cha.kham | 528-001 | CONFIRM | Wise son makes a glad father — relational fruit of wisdom |
| 7370 | Pro 10:8 | H2450 cha.kham | 528-001 | CONFIRM | Wise of heart will receive commandments — wisdom in the heart enabling obedience |
| 7371 | Pro 10:14 | H2450 cha.kham | 528-001 | CONFIRM | The wise lay up knowledge — wisdom accumulating |
| 7372 | Pro 11:29 | H2450 cha.kham | 528-001 | CONFIRM | Fool will be servant to the wise of heart — wisdom as inner quality with social consequence |
| 7373 | Pro 11:30 | H2450 cha.kham | 528-001 | CONFIRM | Whoever captures souls is wise — wisdom with relational reach |
| 7149 | Pro 12:8 | H7922 se.khel | 525-001 | CONFIRM | Man commended according to his good sense — se.khel producing recognition |
| 7374 | Pro 12:15 | H2450 cha.kham | 528-001 | CONFIRM | Wise man listens to advice — wisdom as openness to counsel |
| 7375 | Pro 12:18 | H2450 cha.kham | 528-001 | CONFIRM | Tongue of the wise brings healing — wisdom expressed in speech |
| 7376 | Pro 13:1 | H2450 cha.kham | 528-001 | CONFIRM | Wise son hears his father's instruction — wisdom and teachability |
| 7377 | Pro 13:14 | H2450 cha.kham | 528-001 | CONFIRM | Teaching of the wise is a fountain of life |
| 7150 | Pro 13:15 | H7922 se.khel | 525-001 | CONFIRM | Good sense wins favour — se.khel producing outcomes |
| 7378 | Pro 13:20 | H2450 cha.kham | 528-001 | CONFIRM | Whoever walks with the wise becomes wise — communicability of wisdom |
| 7379 | Pro 14:1 | H2450 cha.kham | 528-001 | CONFIRM | Wisest of women builds her house |
| 7380 | Pro 14:3 | H2450 cha.kham | 528-001 | CONFIRM | Lips of the wise will preserve them |
| 7381 | Pro 14:16 | H2450 cha.kham | 528-001 | CONFIRM | Wise is cautious and turns away from evil |
| 7382 | Pro 14:24 | H2450 cha.kham | 528-001 | CONFIRM | Crown of the wise is their wealth — wisdom producing abundance |
| 7383 | Pro 15:2 | H2450 cha.kham | 528-001 | CONFIRM | Tongue of the wise commends knowledge |
| 7384 | Pro 15:7 | H2450 cha.kham | 528-001 | CONFIRM | Lips of the wise spread knowledge |
| 7385 | Pro 15:12 | H2450 cha.kham | 528-001 | CONFIRM | Scoffer does not go to the wise — wisdom as source of correction |
| 7386 | Pro 15:20 | H2450 cha.kham | 528-001 | CONFIRM | Wise son makes a glad father |
| 7387 | Pro 15:31 | H2450 cha.kham | 528-001 | CONFIRM | Listening ear will dwell among the wise |
| 7388 | Pro 16:14 | H2450 cha.kham | 528-001 | CONFIRM | Wise man will appease a king's wrath — wisdom as social intelligence |
| 7389 | Pro 16:21 | H2450 cha.kham | 528-001 | CONFIRM | Wise of heart is called discerning — heart as seat of wisdom |
| 7151 | Pro 16:22 | H7922 se.khel | 525-001 | CONFIRM | Good sense is a fountain of life — se.khel as self-sustaining resource |
| 7390 | Pro 16:23 | H2450 cha.kham | 528-001 | CONFIRM | Heart of the wise makes his speech judicious — heart-rooted wisdom |
| 7391 | Pro 17:28 | H2450 cha.kham | 528-001 | CONFIRM | Even a fool who keeps silent is considered wise — appearance of wisdom |
| 7319 | Pro 18:1 | H8454 tu.shiy.yah | 527-001 | CONFIRM | Isolation breaks out against all sound judgment |
| 7392 | Pro 18:15 | H2450 cha.kham | 528-001 | CONFIRM | Ear of the wise seeks knowledge |
| 7152 | Pro 19:11 | H7922 se.khel | 525-001 | CONFIRM | Good sense makes one slow to anger |
| 7393 | Pro 20:26 | H2450 cha.kham | 528-001 | CONFIRM | Wise king winnows the wicked — wisdom applied to governance |
| 7394 | Pro 21:11 | H2450 cha.kham | 528-001 | CONFIRM | Wise man is instructed, he gains knowledge |
| 7395 | Pro 21:20 | H2450 cha.kham | 528-001 | CONFIRM | Precious treasure in a wise man's dwelling |
| 7396 | Pro 21:22 | H2450 cha.kham | 528-001 | CONFIRM | Wise man scales the city of the mighty |
| 7397 | Pro 22:17 | H2450 cha.kham | 528-001 | CONFIRM | Hear the words of the wise |
| 7153 | Pro 23:9 | H7922 se.khel | 525-001 | CONFIRM | Fool despises the good sense of your words |
| 7398 | Pro 23:24 | H2450 cha.kham | 528-001 | CONFIRM | He who fathers a wise son will be glad |
| 7399 | Pro 24:5 | H2450 cha.kham | 528-001 | CONFIRM | Wise man is full of strength |
| 7400 | Pro 24:23 | H2450 cha.kham | 528-001 | CONFIRM | Sayings of the wise — wisdom producing authoritative speech |
| 7401 | Pro 25:12 | H2450 cha.kham | 528-001 | CONFIRM | Wise reprover to a listening ear |
| 7402 | Pro 26:5 | H2450 cha.kham | 528-001 | CONFIRM | Lest he be wise in his own eyes — 528-001 holds; self-attribution warning |
| 7403 | Pro 26:12 | H2450 cha.kham | 528-001 | CONFIRM | Wise in his own eyes — more hope for a fool |
| 7404 | Pro 26:16 | H2450 cha.kham | 528-001 | CONFIRM | Sluggard wiser in his own eyes — self-attributed false wisdom |
| 7405 | Pro 28:11 | H2450 cha.kham | 528-001 | CONFIRM | Rich man wise in his own eyes — wealth producing false wisdom |
| 7406 | Pro 29:8 | H2450 cha.kham | 528-001 | CONFIRM | The wise turn away wrath |
| 7407 | Pro 29:9 | H2450 cha.kham | 528-001 | CONFIRM | Wise man in argument with a fool |
| 7408 | Pro 29:11 | H2450 cha.kham | 528-001 | CONFIRM | Wise man quietly holds back his spirit |
| 7409 | Pro 30:24 | H2450 cha.kham | 528-001 | CONFIRM | Four things small but exceedingly wise |
| 7410 | Ecc 2:14 | H2450 cha.kham | 528-001 | CONFIRM | Wise person has his eyes in his head |
| 7411 | Ecc 2:16 | H2450 cha.kham | 528-001 | CONFIRM | Of the wise as of the fool, no enduring remembrance — limits of wisdom |
| 7412 | Ecc 2:19 | H2450 cha.kham | 528-001 | CONFIRM | Who knows whether heir will be wise or a fool |
| 7413 | Ecc 4:13 | H2450 cha.kham | 528-001 | CONFIRM | Poor and wise youth better than old foolish king |
| 7414 | Ecc 6:8 | H2450 cha.kham | 528-001 | CONFIRM | What advantage has the wise man over the fool |
| 7415 | Ecc 7:4 | H2450 cha.kham | 528-001 | CONFIRM | Heart of the wise is in the house of mourning |
| 7416 | Ecc 7:5 | H2450 cha.kham | 528-001 | CONFIRM | Better to hear the rebuke of the wise |
| 7417 | Ecc 7:7 | H2450 cha.kham | 528-001 | CONFIRM | Oppression drives the wise into madness |
| 7418 | Ecc 7:19 | H2450 cha.kham | 528-001 | CONFIRM | Wisdom gives strength to the wise man |
| 7419 | Ecc 8:1 | H2450 cha.kham | 528-001 | CONFIRM | Who is like the wise — wisdom makes face shine |
| 7420 | Ecc 8:5 | H2450 cha.kham | 528-001 | CONFIRM | Wise heart will know the proper time and the just way |
| 7421 | Ecc 8:17 | H2450 cha.kham | 528-001 | CONFIRM | Even the wise man claims to know but cannot find out |
| 7422 | Ecc 9:1 | H2450 cha.kham | 528-001 | CONFIRM | Righteous and the wise in the hand of God |
| 7430 | Isa 3:3 | H2450 cha.kham | 528-005 | CONFIRM | Skillful magician and expert in charms — specialist class |
| 7431 | Isa 5:21 | H2450 cha.kham | 528-003 | CONFIRM | Woe to those wise in their own eyes — self-attributed wisdom |
| 7432 | Isa 19:11 | H2450 cha.kham | 528-005 | CONFIRM | Wisest counselors of Pharaoh — professional court class |
| 7433 | Isa 19:12 | H2450 cha.kham | 528-005 | CONFIRM | Where then are your wise men — court class unable to interpret |
| 7320 | Isa 28:29 | H8454 tu.shiy.yah | 527-001 | CONFIRM | Wonderful in counsel and excellent in wisdom — divine attribute |
| 7434 | Isa 29:14 | H2450 cha.kham | 528-005 | CONFIRM | Wisdom of their wise men shall perish — God removing institutional wisdom |
| 7435 | Isa 31:2 | H2450 cha.kham | 528-005 | CONFIRM | Yet he is wise — God's wisdom bringing disaster on evildoers |
| 7436 | Isa 40:20 | H2450 cha.kham | 528-004 | FLAG | Skillful craftsman to set up an idol — craft skill for idolatry; does not fit Spirit-given sacred description; confirm in 528-004 pending description update |
| 7437 | Isa 44:25 | H2450 cha.kham | 528-005 | CONFIRM | Turns wise men back and makes their knowledge foolish — God overturning institutional wisdom |
| 7438 | Jer 4:22 | H2450 cha.kham | 528-003 | CONFIRM | Wise in doing evil — wisdom misdirected |
| 7439 | Jer 8:8 | H2450 cha.kham | 528-003 | CONFIRM | How can you say we are wise — false claim |
| 7440 | Jer 8:9 | H2450 cha.kham | 528-003 | CONFIRM | Wise men put to shame — wisdom emptied by rejecting the word |
| 7441 | Jer 9:12 | H2450 cha.kham | 528-003 | CONFIRM | Who is the man so wise — wisdom absent before God's judgment |
| 7442 | Jer 9:17 | H2450 cha.kham | P | CONFIRM-P | Skillful mourning women — pending; craft of lament; may land in 528-004 (secular craft) or 528-005; researcher decision needed |
| 7443 | Jer 9:23 | H2450 cha.kham | 528-003 | CONFIRM | Let not the wise man boast in his wisdom |
| 7444 | Jer 10:7 | H2450 cha.kham | 528-003 | CONFIRM | Among all the wise ones of the nations none like you — comparison; God surpasses all |
| 7445 | Jer 10:9 | H2450 cha.kham | 528-004 | FLAG | Skilled craftsmen making idols — secular/idolatrous craft; confirm in 528-004 pending description update |
| 7446 | Jer 18:18 | H2450 cha.kham | 528-005 | CONFIRM | Counsel shall not perish from the wise — institutional source of counsel |
| 7447 | Jer 50:35 | H2450 cha.kham | 528-005 | CONFIRM | Sword against her wise men — destruction of Babylon's wisdom class |
| 7448 | Jer 51:57 | H2450 cha.kham | 528-005 | CONFIRM | I will make drunk her wise men — same |
| 7449 | Eze 27:8 | H2450 cha.kham | 528-004 | FLAG | Tyre's skilled pilots — commercial maritime craft; confirm in 528-004 pending description update |
| 7450 | Eze 27:9 | H2450 cha.kham | 528-004 | FLAG | Skilled men of Gebal caulking seams — same; pending description update |
| 7451 | Eze 28:3 | H2450 cha.kham | 528-005 | CONFIRM | You are wiser than Daniel — ironic; pride before judgment; 528-005 acceptable |
| 208271 | Dan 2:12 | H2445 chak.kim | 6668-001 | CONFIRM | All wise men of Babylon to be destroyed — court class |
| 208272 | Dan 2:13 | H2445 chak.kim | 6668-001 | CONFIRM | Wise men about to be killed — court class |
| 208273 | Dan 2:14 | H2445 chak.kim | 6668-001 | CONFIRM | Wise men of Babylon — Daniel intercedes; court class |
| 208274 | Dan 2:18 | H2445 chak.kim | 6668-001 | CONFIRM | Wise men of Babylon — solidarity in danger |
| 209169 | Dan 2:20 | H2452 chokh.mah | 6696-001 | CONFIRM | To God belong wisdom and might — divine attribute |
| 208275 | Dan 2:21 | H2445 chak.kim | 6668-001 | CONFIRM | He gives wisdom to the wise — court class as recipients |
| 209170 | Dan 2:21 | H2452 chokh.mah | 6696-001 | CONFIRM | He gives wisdom to the wise — chokh.mah as divine gift; 6696-001 correct |
| 209171 | Dan 2:23 | H2452 chokh.mah | 532-002 | CONFIRM | You have given me wisdom and might — received gift; 532-002 correct |
| 208276 | Dan 2:24 | H2445 chak.kim | 6668-001 | CONFIRM | Do not destroy the wise men — Daniel intercedes for the class |
| 208277 | Dan 2:27 | H2445 chak.kim | 6668-001 | CONFIRM | No wise men can show the mystery — incapacity of court class |
| 209172 | Dan 2:30 | H2452 chokh.mah | 532-002 | CONFIRM | Not because of any wisdom that I have — explicit disclaimer; gift |
| 208278 | Dan 2:48 | H2445 chak.kim | 6668-001 | CONFIRM | Daniel appointed chief prefect over all the wise men |
| 208280 | Dan 4:6 | H2445 chak.kim | 6668-001 | CONFIRM | All wise men of Babylon to be brought — foil for Spirit-given wisdom |
| 208279 | Dan 4:18 | H2445 chak.kim | 6668-001 | CONFIRM | All wise men unable; you are able because of the Spirit |
| 208282 | Dan 5:7 | H2445 chak.kim | 6668-001 | CONFIRM | King called in the wise men — court class summoned |
| 208283 | Dan 5:8 | H2445 chak.kim | 6668-001 | CONFIRM | Wise men could not read the writing — incapacity |
| 209173 | Dan 5:11 | H2452 chokh.mah | 532-002 | CONFIRM | Wisdom like the wisdom of the gods found in him — Spirit-given; 532-002 correct |
| 209174 | Dan 5:14 | H2452 chokh.mah | 532-002 | CONFIRM | Excellent wisdom found in you — Spirit-given; 532-002 correct |
| 208281 | Dan 5:15 | H2445 chak.kim | 6668-001 | CONFIRM | Wise men brought in but could not — repeated incapacity |
| 7157 | Dan 8:25 | H7922 se.khel | 525-001 | CONFIRM | By his cunning — se.khel directed toward deception; directional neutrality confirmed |
| 7452 | Hos 13:13 | H2450 cha.kham | 528-001 | CONFIRM | Unwise son — negative wisdom; 528-001 holds |
| 7453 | Hos 14:9 | H2450 cha.kham | 528-001 | CONFIRM | Whoever is wise let him understand — wisdom enabling perception of God's ways |
| 54611 | Amo 6:5 | H2803G cha.shav | 528-004 | FLAG | Invent instruments of music in self-indulgent ease — secular inventive devising; confirm in 528-004 pending description update |
| 208270 | Obd 8 | H2450 cha.kham | P | CONFIRM-P | Destroy the wise men out of Edom — judgment on national wisdom; P-status correct; ready for grouping in 528-005 (destruction of institutional wisdom class) |
| 7321 | Mic 6:9 | H8454 tu.shiy.yah | 527-001 | CONFIRM | Sound wisdom to fear your name — tu.shiy.yah as content of fearing God |
| 103571 | Mat 7:24 | G5429 fronimos | 3459-001 | CONFIRM | Wise man who built his house on rock — hearing and doing |
| 103565 | Mat 10:16 | G5429 fronimos | 3459-001 | CONFIRM | Wise as serpents — shrewd wariness |
| **7458** | **Mat 11:19** | **G4678 sofia** | **6696-001** | **MOVE** | **→ 532-003** — wisdom justified by her deeds; personified wisdom visible in deeds; not a divine-attribute statement |
| 208346 | Mat 11:25 | G4680 sofos | 4458-001 | CONFIRM | Hidden from the wise and understanding — cross-wisdom reversal |
| 7459 | Mat 12:42 | G4678 sofia | 532-003 | CONFIRM | Queen came to hear wisdom of Solomon — sofia visible in Solomon |
| 7460 | Mat 13:54 | G4678 sofia | 532-003 | CONFIRM | Where did this man get this wisdom — sofia visible in Jesus |
| 126311 | Mat 16:23 | G5426 froneō | 996-001 | CONFIRM | Not setting mind on things of God — directional inner orientation |
| 208347 | Mat 23:34 | G4680 sofos | 4458-001 | CONFIRM | I send you wise men — wisdom as mission qualification; within 4458-001 scope |
| 103566 | Mat 24:45 | G5429 fronimos | 3459-001 | CONFIRM | Faithful and wise servant — trustworthy stewardship |
| 103567 | Mat 25:2 | G5429 fronimos | 3459-001 | CONFIRM | Five were wise — defining characteristic |
| 103568 | Mat 25:4 | G5429 fronimos | 3459-001 | CONFIRM | Wise took flasks of oil — foresighted action |
| 103569 | Mat 25:8 | G5429 fronimos | 3459-001 | CONFIRM | Foolish said to the wise — prepared vs unprepared |
| 103570 | Mat 25:9 | G5429 fronimos | 3459-001 | CONFIRM | Wise answered — clear-eyed assessment |
| 7461 | Mar 6:2 | G4678 sofia | 532-003 | CONFIRM | What wisdom given to him — sofia visible in Jesus |
| 126310 | Mar 8:33 | G5426 froneō | 996-001 | CONFIRM | Not setting mind on things of God — parallel to Mat 16:23 |
| 7462 | Luk 2:40 | G4678 sofia | 532-003 | CONFIRM | Child filled with wisdom — sofia in Jesus growing |
| 7463 | Luk 2:52 | G4678 sofia | 532-003 | CONFIRM | Jesus increased in wisdom — sofia visible in person |
| **7464** | **Luk 7:35** | **G4678 sofia** | **6696-001** | **MOVE** | **→ 532-003** — wisdom justified by her children; deeds of wisdom visible; not divine-attribute |
| 208345 | Luk 10:21 | G4680 sofos | 4458-001 | CONFIRM | Hidden from the wise and understanding — cross-wisdom reversal |
| 7465 | Luk 11:31 | G4678 sofia | 532-003 | CONFIRM | Wisdom of Solomon — sofia visible in Solomon |
| 7466 | Luk 11:49 | G4678 sofia | 6696-001 | CONFIRM | The Wisdom of God said — divine-attribute / personification; 6696-001 correct |
| 103563 | Luk 12:42 | G5429 fronimos | 3459-001 | CONFIRM | Faithful and wise manager — stewardship wisdom |
| 103564 | Luk 16:8 | G5429 fronimos | 3459-001 | CONFIRM | More shrewd in dealing with their own generation |
| 7467 | Luk 21:15 | G4678 sofia | 532-003 | CONFIRM | I will give you a mouth and wisdom — sofia in the disciples |
| 7468 | Act 6:3 | G4678 sofia | 532-003 | CONFIRM | Full of the Spirit and of wisdom — sofia visible in the seven |
| 7469 | Act 6:10 | G4678 sofia | 532-003 | CONFIRM | Could not withstand the wisdom and the Spirit in him |
| 7470 | Act 7:10 | G4678 sofia | 532-003 | CONFIRM | Gave him favour and wisdom before Pharaoh — sofia in Joseph |
| 7471 | Act 7:22 | G4678 sofia | 532-003 | CONFIRM | Moses instructed in all the wisdom of the Egyptians |
| 126309 | Act 28:22 | G5426 froneō | 996-001 | CONFIRM | We desire to hear what your views are — inner orientation |
| 208348 | Rom 1:14 | G4680 sofos | 4458-001 | CONFIRM | Obligation to wise and foolish — sofos as human category |
| 208349 | Rom 1:22 | G4680 sofos | 4458-001 | CONFIRM | Claiming to be wise they became fools — cross-wisdom reversal |
| 32170 | Rom 8:5 | G5426 froneō | 996-001 | CONFIRM | Set minds on things of flesh / Spirit — directional inner orientation |
| 103572 | Rom 11:25 | G5429 fronimos | 3459-001 | CONFIRM | Lest you be wise in your own sight — warns against self-attributed wisdom; fronimos used |
| 7472 | Rom 11:33 | G4678 sofia | 6696-001 | CONFIRM | Depth of riches and wisdom of God — divine attribute |
| 32167 | Rom 12:3 | G5426 froneō | 996-001 | CONFIRM | Think with sober judgment — inner orientation calibrated to faith |
| 32166 | Rom 12:16 | G5426 froneō | 996-001 | CONFIRM | Live in harmony — froneō as communal orientation |
| 103573 | Rom 12:16 | G5429 fronimos | 3459-001 | CONFIRM | Never be wise in your own sight — same verse; fronimos row |
| 32168 | Rom 14:6 | G5426 froneō | 996-001 | CONFIRM | The one who observes the day — froneō as relational concern / honour of Lord |
| 32169 | Rom 15:5 | G5426 froneō | 996-001 | CONFIRM | Live in such harmony — froneō as communal alignment |
| 208350 | Rom 16:19 | G4680 sofos | 4458-001 | CONFIRM | I want you to be wise as to what is good — sofos in positive exhortation; within 4458-001 scope |
| 208351 | Rom 16:27 | G4680 sofos | 6696-001 | CONFIRM | To the only wise God — divine attribute; 6696-001 correct |
| 7473 | 1Cor 1:17 | G4678 sofia | 4458-001 | CONFIRM | Not with words of eloquent wisdom — cross-wisdom opposition |
| 7474 | 1Cor 1:19 | G4678 sofia | 4458-001 | CONFIRM | I will destroy the wisdom of the wise — cross-wisdom |
| 208333 | 1Cor 1:19 | G4680 sofos | 4458-001 | CONFIRM | Same verse — sofos row; cross-wisdom |
| 7475 | 1Cor 1:20 | G4678 sofia | 4458-001 | CONFIRM | Has not God made foolish the wisdom of the world |
| 208334 | 1Cor 1:20 | G4680 sofos | 4458-001 | CONFIRM | Where is the one who is wise — sofos row |
| 7476 | 1Cor 1:21 | G4678 sofia | 4458-001 | CONFIRM | World did not know God through wisdom |
| 7477 | 1Cor 1:22 | G4678 sofia | 4458-001 | CONFIRM | Greeks seek wisdom — human category |
| 7478 | 1Cor 1:24 | G4678 sofia | 6696-001 | CONFIRM | Christ the power and wisdom of God — divine attribute; 6696-001 correct |
| 208335 | 1Cor 1:25 | G4680 sofos | 4458-001 | CONFIRM | Foolishness of God is wiser than men — cross-wisdom |
| 208336 | 1Cor 1:26 | G4680 sofos | 4458-001 | CONFIRM | Not many wise according to worldly standards |
| 208337 | 1Cor 1:27 | G4680 sofos | 4458-001 | CONFIRM | God chose what is foolish to shame the wise |
| 7479 | 1Cor 1:30 | G4678 sofia | 532-002 | CONFIRM | Christ became to us wisdom from God — gift; 532-002 correct |
| 7480 | 1Cor 2:1 | G4678 sofia | 4458-001 | CONFIRM | Did not come with lofty speech or wisdom |
| 7481 | 1Cor 2:4 | G4678 sofia | 4458-001 | CONFIRM | Not in plausible words of wisdom |
| 7482 | 1Cor 2:5 | G4678 sofia | 4458-001 | CONFIRM | Faith not in wisdom of men |
| 7483 | 1Cor 2:6 | G4678 sofia | 532-002 | CONFIRM | We do impart wisdom, though not of this age — divine wisdom given |
| 7484 | 1Cor 2:7 | G4678 sofia | 532-002 | CONFIRM | Secret and hidden wisdom of God — gift |
| 7485 | 1Cor 2:13 | G4678 sofia | 532-002 | CONFIRM | Not taught by human wisdom but by the Spirit |
| **208338** | **1Cor 3:10** | **G4680 sofos** | **4458-001** | **MOVE** | **→ 532-003** — "skilled master builder" is a positive commendation of Paul's apostolic competence; not cross-wisdom opposition |
| 208339 | 1Cor 3:18 | G4680 sofos | 4458-001 | CONFIRM | Let him become a fool to become wise — cross-wisdom reversal |
| 7486 | 1Cor 3:19 | G4678 sofia | 4458-001 | CONFIRM | Wisdom of this world is folly with God |
| 208340 | 1Cor 3:19 | G4680 sofos | 4458-001 | CONFIRM | He catches the wise in their craftiness — sofos row |
| 208341 | 1Cor 3:20 | G4680 sofos | 4458-001 | CONFIRM | Thoughts of the wise, that they are futile |
| 103561 | 1Cor 4:10 | G5429 fronimos | 3459-001 | CONFIRM | You are wise in Christ — ironic fronimos; 3459-001 holds |
| 208342 | 1Cor 6:5 | G4680 sofos | 4458-001 | CONFIRM | No one wise enough to settle a dispute — appeal for practical wisdom; within 4458-001 scope |
| 103560 | 1Cor 10:15 | G5429 fronimos | 3459-001 | CONFIRM | I speak as to sensible people |
| 7487 | 1Cor 12:8 | G4678 sofia | 532-003 | CONFIRM | Utterance of wisdom given through Spirit — sofia as Spirit-gift visible in community; 532-003 holds |
| 32162 | 1Cor 13:11 | G5426 froneō | 996-001 | CONFIRM | When I was a child I thought like a child — inner mode of thinking at a stage of life |
| 7488 | 2Cor 1:12 | G4678 sofia | 4458-001 | CONFIRM | Not by earthly wisdom but by grace — cross-wisdom opposition |
| 103562 | 2Cor 11:19 | G5429 fronimos | 3459-001 | CONFIRM | Being wise yourselves — ironic fronimos |
| 32163 | 2Cor 13:11 | G5426 froneō | 996-001 | CONFIRM | Agree with one another — froneō as communal alignment |
| 32165 | Gal 5:10 | G5426 froneō | 996-001 | CONFIRM | You will take no other view — relational inner orientation |
| 7489 | Eph 1:8 | G4678 sofia | 532-002 | CONFIRM | Lavished on us in all wisdom and insight — divine gift |
| 7490 | Eph 1:17 | G4678 sofia | 532-002 | CONFIRM | Spirit of wisdom and of revelation — gift |
| 7491 | Eph 3:10 | G4678 sofia | 6696-001 | CONFIRM | Manifold wisdom of God made known through church — divine attribute |
| 208352 | Eph 5:15 | G0781 asofos | 6676-001 | CONFIRM | Walk not as unwise but as wise — asofos as deficit |
| 208343 | Eph 5:15 | G4680 sofos | 4458-001 | CONFIRM | Walk as wise — sofos as positive inner quality in 4458-001 context |
| 126312 | Phili 1:7 | G5426 froneō | 996-001 | CONFIRM | It is right for me to feel this way — relational concern |
| 126313 | Phili 2:2 | G5426 froneō | 996-001 | CONFIRM | Being of the same mind — communal alignment |
| 126314 | Phili 2:5 | G5426 froneō | 996-001 | CONFIRM | Have this mind in Christ — paradigmatic froneō |
| 126315 | Phili 3:15 | G5426 froneō | 996-001 | CONFIRM | Let the mature think this way — inner orientation of maturity |
| 126316 | Phili 3:19 | G5426 froneō | 996-001 | CONFIRM | Minds set on earthly things — directional inner orientation |
| 126318 | Phili 4:2 | G5426 froneō | 996-001 | CONFIRM | Agree in the Lord — communal alignment |
| 126317 | Phili 4:10 | G5426 froneō | 996-001 | CONFIRM | You have revived your concern for me — relational attending |
| 7492 | Col 1:9 | G4678 sofia | 532-002 | CONFIRM | Filled with knowledge of his will in all spiritual wisdom — divine gift |
| 7493 | Col 1:28 | G4678 sofia | 532-002 | CONFIRM | Teaching with all wisdom — wisdom as mode of proclamation |
| 7494 | Col 2:3 | G4678 sofia | 6696-001 | CONFIRM | Treasures of wisdom hidden in Christ — divine attribute |
| 7495 | Col 2:23 | G4678 sofia | 4458-001 | CONFIRM | Appearance of wisdom in self-made religion — false wisdom; 4458-001 holds |
| 32164 | Col 3:2 | G5426 froneō | 996-001 | CONFIRM | Set your minds on things above — directional inner orientation |
| 7496 | Col 3:16 | G4678 sofia | 532-002 | CONFIRM | Teaching in all wisdom — proclamation mode |
| 7497 | Col 4:5 | G4678 sofia | 532-003 | CONFIRM | Walk in wisdom toward outsiders — sofia visible in relational conduct |
| **7454** | **2Ti 3:15** | **G4679 sofizo** | **4458-001** | **MOVE** | **→ CREATE-VCG sofizo-positive (mti_id=530)** — Scripture making wise for salvation; positive transformative use; opposite of 2Pe 1:16 |
| 7498 | Jam 1:5 | G4678 sofia | 532-002 | CONFIRM | Let him ask God who gives generously — wisdom as divine gift on request |
| **7499** | **Jam 3:13** | **G4678 sofia** | **4458-001** | **MOVE** | **→ 532-003** — wisdom visible in meek conduct and good works; positive characterisation; not cross-wisdom opposition |
| **208344** | **Jam 3:13** | **G4680 sofos** | **4458-001** | **MOVE** | **→ 532-003** — same verse; sofos row; same reasoning |
| 7500 | Jam 3:15 | G4678 sofia | 4458-001 | CONFIRM | Earthly, unspiritual, demonic wisdom — false wisdom; 4458-001 holds |
| 7501 | Jam 3:17 | G4678 sofia | 532-002 | CONFIRM | Wisdom from above is first pure — divine gift with named qualities |
| **7455** | **2Pe 1:16** | **G4679 sofizo** | **4458-001** | **MOVE** | **→ CREATE-VCG sofizo-negative (mti_id=530)** — cleverly devised myths; the fabricating use explicitly disclaimed; must be separate from 2Ti 3:15 |
| 7502 | 2Pe 3:15 | G4678 sofia | 532-003 | CONFIRM | Wisdom given to Paul — sofia visible in apostle's writing |
| 7503 | Rev 5:12 | G4678 sofia | 532-002 | CONFIRM | Worthy is the Lamb to receive wisdom — doxological; gift |
| 7504 | Rev 7:12 | G4678 sofia | 6696-001 | CONFIRM | Wisdom be to our God — doxological; divine attribute |
| 7505 | Rev 13:18 | G4678 sofia | 532-002 | CONFIRM | This calls for wisdom — inner capacity to interpret; 532-002 holds |
| 7506 | Rev 17:9 | G4678 sofia | 532-002 | CONFIRM | Mind with wisdom — inner interpretive capacity |

---

### M15-A action summary

**MOVE actions (10 verses):**

| # | vr_id | Reference | From | To |
|---|---|---|---|---|
| 1 | 54622 | Exo 36:8 (cha.shav) | 4458-001 | 528-004 |
| 2 | 54608 | 2Ch 2:14 (cha.shav) | 4458-001 | 528-004 |
| 3 | 54610 | 2Sa 14:14 (cha.shav) | 1174-001 | M15-E 3334-002 |
| 4 | 54612 | Est 8:3 (cha.shav) | 1174-002 | M15-E 3334-001 |
| 5 | 54613 | Est 9:25 (cha.shav) | 1174-002 | M15-E 3334-001 |
| 6 | 54626 | Psa 35:20 (cha.shav) | 1174-002 | M15-E 3334-001 |
| 7 | 7343 | 1Ki 2:9 (cha.kham) | 4458-001 | 528-005 |
| 8 | 7458 | Mat 11:19 (sofia) | 6696-001 | 532-003 |
| 9 | 7464 | Luk 7:35 (sofia) | 6696-001 | 532-003 |
| 10 | 208338 | 1Cor 3:10 (sofos) | 4458-001 | 532-003 |
| 11 | 7499 | Jam 3:13 (sofia) | 4458-001 | 532-003 |
| 12 | 208344 | Jam 3:13 (sofos) | 4458-001 | 532-003 |
| 13 | 7454 | 2Ti 3:15 (sofizo) | 4458-001 | → CREATE-VCG sofizo-positive |
| 14 | 7455 | 2Pe 1:16 (sofizo) | 4458-001 | → CREATE-VCG sofizo-negative |

**CREATE-VCG actions (2):**

| # | mti_id | Term | Code | Description |
|---|---|---|---|---|
| 1 | 530 | G4679 sofizo | sofizo-pos | Scripture making the inner person wise for salvation through faith in Christ Jesus |
| 2 | 530 | G4679 sofizo | sofizo-neg | The act of devising clever myths — what the apostles explicitly did not do |

**UPDATE-DESC actions (3):**

| # | VCG | Required change |
|---|---|---|
| 1 | 528-004 | Current: "Spirit-given for sacred construction." Needs widening to accommodate secular craft rows (Isa 40:20, Jer 10:9, Eze 27:8/9, Amo 6:5, 2Ch 26:15, 1Ch 22:15) — these share the same inner capacity but applied outside the sanctuary. Proposed: "cha.kham and cha.shav H2803G name an inner capacity for skilled design and craft work. In the primary cluster, this capacity is Spirit-given and directed toward sacred construction. The same capacity appears in secular, commercial, and inventive contexts — including idol-craft, ship-building, and instrument-making — where the inner faculty is the same but the direction differs." |
| 2 | 6696-001 | Current description covers wisdom as divine attribute. After moving vr_id 7458 (Mat 11:19) and 7464 (Luk 7:35) to 532-003, update description: "sofia and sofos name wisdom as an attribute belonging to God alone — the wisdom that is in Christ as the treasury of God, that belongs to the Lamb in doxology, that belongs to God in the heavenly praise. Distinguished from sofia visible in a person (532-003) and sofia as gift received (532-002)." |
| 3 | 4458-001 | After moving sofizo rows, 2Ti 3:15 and 2Pe 1:16 references should be removed from description scope if mentioned. No structural change needed otherwise — core cross-opposition content remains correct. |

**FLAG actions (6):** Job 30:22, Isa 40:20, Jer 10:9, Eze 27:8, Eze 27:9, Amo 6:5 (all in 528-004; description mismatch with secular craft content; awaiting description update — no move needed)

**P-status rows (2):** Jer 9:17 (7442) and Obd 8 (208270) — both confirmed correctly P; researcher to decide on grouping

**CONFIRM actions: 272 verses**

---

*M15-A complete. 298 verses addressed. Proceeding to M15-B through BOUNDARY in subsequent sessions, then compiling directive/patch from complete action list.*

---

## M15-B — 287 verses, 17 DB VCGs

### VCG inventory (DB state)

| VCG code | Term | Description | DB count |
|---|---|---|---|
| 932-001 | H0995 bin | bin as constituted inner perceptive faculty | 69 |
| 932-002 | H0995 bin | Prayerful seeking and receiving of understanding | 37 |
| 932-003 | H0995 bin | God's inner comprehension of the human person | 9 |
| 932-004 | G4920 suniēmi / H0995 bin | Failure, hardening, or absence of understanding | 52 |
| 523-002 | H0998 bi.nah | Understanding as human inner-being capacity | 37 |
| 524-001 | H8394 te.vu.nah | Understanding as divine attribute | 8 |
| 524-002 | H8394 te.vu.nah | Understanding as human inner-being capacity | 33 |
| 816-001 | G4907 sunesis | Understanding as faculty of love and spiritual orientation | 4 |
| 816-002 | G4907 sunesis / H0995 bin | Inner reception of revealed truth | 11 |
| 1205-001 | G4920 suniēmi | Understanding as inner receptive act | 8 |
| 1205-002 | G4920 suniēmi | Lack of understanding / hearts hardened | 4 |
| 1205-003 | G4920 suniēmi | Practical discerning of God's will | 2 |
| 1201-001 | G4908 sunetos | Intelligence and its paradoxical limits | 3 |
| 1202-001 | G0801 asunetos | Senselessness as inner condition | 5 |
| 531-001 | G5428 fronesis | Understanding enabling transformed living | 2 |
| 1207-001 | G1990 epistēmōn | Genuine knowing verified by conduct | 1 |
| 1204-001 | H0999 bi.nah | Inner receptive capacity God recognises | 1 |

**SA rows in M15-B (2):** Ezr 8:15 (vr_id 173367), Psa 58:9 (vr_id 173419)

---

### Per-verse action table — all 287 rows

| vr_id | Reference | Term | Current VCG | Action | Target / Note |
|---|---|---|---|---|---|
| 27705 | Gen 41:33 | H0995 bin | 932-001 | CONFIRM | Discerning man sought — bin as governance qualification within constituted faculty |
| 27706 | Gen 41:39 | H0995 bin | 932-001 | CONFIRM | None so discerning and wise as you — bin recognised in Joseph |
| 7099 | Exo 31:3 | H8394 te.vu.nah | 524-002 | CONFIRM | Filled with Spirit of God with intelligence — Spirit-given; 524-002 correct |
| 7100 | Exo 35:31 | H8394 te.vu.nah | 524-002 | CONFIRM | Spirit of God with skill, intelligence, knowledge — same pattern |
| 7101 | Exo 36:1 | H8394 te.vu.nah | 524-002 | CONFIRM | Lord has put skill and intelligence in the craftsman — Spirit-given for sanctuary |
| 173361 | Deu 1:13 | H0995 bin | 932-001 | CONFIRM | Choose wise, understanding, experienced men — bin as governance qualification |
| 173365 | Deu 4:6 | H0995 bin | 816-002 | FLAG | Both Deu 4:6 rows in 816-002; primary meaning is understanding through covenant obedience visible to nations — defensible; flag for researcher review |
| 7060 | Deu 4:6 | H0998 bi.nah | 816-002 | FLAG | Same verse; bi.nah row also in 816-002; same flag |
| 173364 | Deu 32:7 | H0995 bin | 932-002 | CONFIRM | Consider the years of many generations — reflective perceptive attending; 932-002 holds |
| 173362 | Deu 32:10 | H0995 bin | 932-003 | CONFIRM | He cared for him — God's attentive care of Israel; 932-003 correct |
| 7102 | Deu 32:28 | H8394 te.vu.nah | 524-002 | CONFIRM | Nation void of counsel, no understanding in them — absent te.vu.nah |
| 173363 | Deu 32:29 | H0995 bin | 932-001 | CONFIRM | They would discern their latter end — bin as perceptive discernment |
| 173355 | 1Sa 3:8 | H0995 bin | 932-004 | CONFIRM | Eli perceived that the Lord was calling — note: this is the faculty activated, not failed; 932-004 is a loose fit; FLAG — perception succeeded here, unlike most 932-004 uses |
| 173354 | 1Sa 16:18 | H0995 bin | 932-001 | CONFIRM | Prudent in speech — bin governing expression |
| 173360 | 2Sa 12:19 | H0995 bin | 932-001 | CONFIRM | David understood that the child was dead — reading situation rightly |
| 173353 | 1Ki 3:9 | H0995 bin | 932-001 | CONFIRM | Understanding mind to discern good and evil — paradigmatic governance request |
| 173350 | 1Ki 3:11 | H0995 bin | 932-001 | CONFIRM | Asked for understanding to discern what is right |
| 173351 | 1Ki 3:12 | H0995 bin | 932-001 | CONFIRM | I give you a wise and discerning mind |
| 173352 | 1Ki 3:21 | H0995 bin | 932-001 | CONFIRM | When I looked at him closely — careful perceptive examination; peripheral use of bin |
| 7103 | 1Ki 4:29 | H8394 te.vu.nah | 524-002 | CONFIRM | God gave Solomon wisdom and understanding beyond measure |
| 7104 | 1Ki 7:14 | H8394 te.vu.nah | 524-002 | CONFIRM | Full of wisdom, understanding, and skill — te.vu.nah in craftsman |
| 7061 | 1Ch 12:32 | H0998 bi.nah | 523-002 | CONFIRM | Understanding of the times to know what Israel ought to do |
| 173345 | 1Ch 15:22 | H0995 bin | 932-001 | CONFIRM | Chenaniah directed the music for he understood it — inner mastery |
| 7062 | 1Ch 22:12 | H0998 bi.nah | 523-002 | CONFIRM | May the Lord grant you discretion and understanding — God-given bi.nah |
| 173346 | 1Ch 25:7 | H0995 bin | 932-001 | CONFIRM | All who were skillful — inner competence qualifying for service |
| 173347 | 1Ch 25:8 | H0995 bin | 932-001 | CONFIRM | Teacher and pupil alike — bin as inner qualification for teaching |
| 173348 | 1Ch 27:32 | H0995 bin | 932-001 | CONFIRM | Jonathan a counselor, man of understanding |
| 173349 | 1Ch 28:9 | H0995 bin | 932-003 | CONFIRM | The Lord understands every plan and thought — God's comprehensive knowing; 932-003 correct |
| 7063 | 2Ch 2:12 | H0998 bi.nah | 523-002 | CONFIRM | Wise son who has discretion and understanding |
| 7064 | 2Ch 2:13 | H0998 bi.nah | 523-002 | CONFIRM | Skilled man who has understanding, Huram-abi |
| 173356 | 2Ch 11:23 | H0995 bin | 932-001 | CONFIRM | He dealt wisely — bin expressed in prudent action |
| 173357 | 2Ch 26:5 | H0995 bin | 932-002 | CONFIRM | Zechariah instructed him in the fear of God — enabling instruction in understanding |
| 173358 | 2Ch 34:12 | H0995 bin | 932-001 | CONFIRM | Levites who were skillful with instruments — inner competence |
| 173359 | 2Ch 35:3 | H0995 bin | 932-002 | CONFIRM | Levites who taught all Israel — understanding enabling teaching |
| 173367 | Ezr 8:15 | H0995 bin | SA | CONFIRM-SA | Administrative review; no inner-being content; correctly SA |
| 173368 | Ezr 8:16 | H0995 bin | 932-001 | CONFIRM | Men of insight — bin as defining inner quality |
| 27763 | Neh 8:2 | H0995 bin | 932-002 | CONFIRM | All who could understand what they heard — capacity to receive the Law |
| 27764 | Neh 8:3 | H0995 bin | 932-002 | CONFIRM | Those who could understand — same pattern |
| 27765 | Neh 8:7 | H0995 bin | 932-002 | CONFIRM | Levites helped people to understand the Law |
| 27766 | Neh 8:8 | H0995 bin | 932-002 | CONFIRM | People understood the reading — inner act of grasping |
| 27767 | Neh 8:9 | H0995 bin | 932-002 | CONFIRM | Levites who taught the people — understanding enabling instruction |
| 27762 | Neh 8:12 | H0995 bin | 932-002 | CONFIRM | Because they had understood the words |
| 27760 | Neh 10:28 | H0995 bin | 932-002 | CONFIRM | All who have knowledge and understanding — covenant community marker |
| 27761 | Neh 13:7 | H0995 bin | 932-001 | CONFIRM | I then discovered the evil Eliashib had done — perceptive discovery |
| 27756 | Job 6:24 | H0995 bin | 932-002 | CONFIRM | Make me understand how I have gone astray — humble petition |
| 27757 | Job 6:30 | H0995 bin | 932-001 | CONFIRM | Cannot my palate discern the cause of calamity — self-directing the faculty |
| 27758 | Job 9:11 | H0995 bin | 932-004 | CONFIRM | I do not perceive him — faculty reaches its limit before God |
| 27736 | Job 11:11 | H0995 bin | 932-003 | CONFIRM | He sees iniquity, will he not consider it — God's perceptive attending |
| 7105 | Job 12:12 | H8394 te.vu.nah | 524-002 | CONFIRM | Understanding in length of days — te.vu.nah deepening with age |
| 7106 | Job 12:13 | H8394 te.vu.nah | 524-001 | CONFIRM | With God are wisdom and might; he has counsel and understanding — divine attribute |
| 27737 | Job 13:1 | H0995 bin | 932-004 | CONFIRM | My ear has heard and understood — grasping what is heard; note: this is successful understanding, not failure; 932-004 loose fit; FLAG — same issue as 1Sa 3:8 |
| 27738 | Job 14:21 | H0995 bin | 932-004 | CONFIRM | He perceives it not — dead cannot perceive; within limits category |
| 27739 | Job 15:9 | H0995 bin | 932-001 | CONFIRM | What do you understand that is not clear to us — challenging the reach of Job's faculty |
| 27740 | Job 18:2 | H0995 bin | 932-004 | CONFIRM | Consider, and then we will speak — Bildad calls for careful reflection; 932-004 is loose; marginal but acceptable |
| 7065 | Job 20:3 | H0998 bi.nah | 523-002 | CONFIRM | Out of my understanding a spirit answers me — inner source of Zophar's response |
| 27742 | Job 23:5 | H0995 bin | 932-002 | CONFIRM | I would understand what he would say — seeking understanding of God's answer |
| 27743 | Job 23:8 | H0995 bin | 932-004 | CONFIRM | I do not perceive him — faculty cannot locate God |
| 27741 | Job 23:15 | H0995 bin | 932-004 | CONFIRM | When I consider, I am in dread — contemplating God produces awe; within limits range |
| 7107 | Job 26:12 | H8394 te.vu.nah | 524-001 | CONFIRM | By his understanding he shattered Rahab — divine creative-governing attribute |
| 27744 | Job 26:14 | H0995 bin | 932-002 | CONFIRM | Thunder of his power who can understand — confronting limits; 932-002 holds (seeking what cannot be fully reached) |
| 7066 | Job 28:12 | H0998 bi.nah | 523-002 | CONFIRM | Where shall wisdom be found — bi.nah as the sought thing beyond ordinary reach |
| 7067 | Job 28:20 | H0998 bi.nah | 523-002 | CONFIRM | Where is the place of understanding — same question |
| 27745 | Job 28:23 | H0995 bin | 932-003 | CONFIRM | God understands the way to it — God alone knows where wisdom is found |
| 7068 | Job 28:28 | H0998 bi.nah | 523-002 | CONFIRM | To turn away from evil is understanding — bi.nah as enacted moral orientation |
| 27746 | Job 30:20 | H0995 bin | 932-003 | FLAG | You only look at me — God's attending without responding; 932-003 is loose; could argue for a separate "divine attending without response" group; confirm in 932-003 |
| 27747 | Job 31:1 | H0995 bin | 932-001 | CONFIRM | How could I gaze at a virgin — directed perceptive attention; boundary use of bin |
| 27749 | Job 32:8 | H0995 bin | 932-001 | CONFIRM | Breath of the Almighty makes him understand — Spirit as source of bin |
| 27750 | Job 32:9 | H0995 bin | 932-001 | CONFIRM | The aged who understand what is right — moral discernment |
| 7108 | Job 32:11 | H8394 te.vu.nah | 524-002 | CONFIRM | I listened for your wise sayings — te.vu.nah as the expression of inner understanding |
| 27748 | Job 32:12 | H0995 bin | 932-004 | CONFIRM | I gave you my attention — attentive listening; 932-004 loose; FLAG — this is active attention, not failure |
| 7069 | Job 34:16 | H0998 bi.nah | 523-002 | CONFIRM | If you have understanding, hear this — bi.nah as precondition for reception |
| 27751 | Job 36:29 | H0995 bin | 932-004 | CONFIRM | Can anyone understand the spreading of the clouds — limits before divine works |
| 27752 | Job 37:14 | H0995 bin | 932-004 | CONFIRM | Stop and consider the wondrous works of God — reflective attending called for; 932-004 acceptable |
| 7070 | Job 38:4 | H0998 bi.nah | 523-002 | CONFIRM | Tell me if you have understanding — bi.nah as condition for grasping creation's foundations |
| 27753 | Job 38:18 | H0995 bin | 932-004 | CONFIRM | Have you comprehended the expanse of the earth — limits of bin before cosmic scale |
| 27754 | Job 38:20 | H0995 bin | 932-004 | CONFIRM | That you may discern the paths — faculty challenged by God |
| 7071 | Job 38:36 | H0998 bi.nah | 523-002 | CONFIRM | Who has given understanding to the mind — bi.nah as divine gift |
| 7072 | Job 39:17 | H0998 bi.nah | 523-002 | CONFIRM | God has given her no share in understanding — withheld gift |
| 7073 | Job 39:26 | H0998 bi.nah | 523-002 | CONFIRM | Is it by your understanding that the hawk soars — rhetorical challenge |
| 27755 | Job 42:3 | H0995 bin | 932-002 | CONFIRM | I have uttered what I did not understand — self-acknowledged limit; humility before God |
| 173417 | Psa 5:1 | H0995 bin | 932-003 | CONFIRM | Consider my groaning — petition for God's perceptive attending |
| 173411 | Psa 19:12 | H0995 bin | 932-004 | CONFIRM | Who can discern his errors — limits of self-knowledge regarding hidden faults |
| 173412 | Psa 28:5 | H0995 bin | 932-004 | CONFIRM | They do not regard the works of the Lord — failure to perceive God's acts |
| 173413 | Psa 32:9 | H0995 bin | 932-001 | CONFIRM | Be not like a horse or mule without understanding — bin as what distinguishes human person |
| 173414 | Psa 33:15 | H0995 bin | 932-003 | CONFIRM | He fashions hearts and observes all their deeds — God's comprehensive perception |
| 173415 | Psa 37:10 | H0995 bin | 932-004 | CONFIRM | Though you look carefully at his place — perceptive searching; 932-004 holds |
| 7109 | Psa 49:3 | H8394 te.vu.nah | 524-002 | CONFIRM | Meditation of my heart shall be understanding — heart-meditation producing te.vu.nah |
| 173416 | Psa 49:20 | H0995 bin | 932-001 | CONFIRM | Man without understanding is like the beasts — defining verse for bin as mark of humanness |
| 173418 | Psa 50:22 | H0995 bin | 932-004 | CONFIRM | Mark this, you who forget God — command to perceive and heed |
| 173419 | Psa 58:9 | H0995 bin | SA | CONFIRM-SA | No inner-being content in span; correctly SA |
| 173420 | Psa 73:17 | H0995 bin | 932-004 | CONFIRM | Until I went into the sanctuary; then I discerned their end — bin as act of discernment; note: this is successful discernment, not failure; 932-004 is loose; FLAG — better fit in 932-001 |
| 7110 | Psa 78:72 | H8394 te.vu.nah | 524-002 | CONFIRM | He guided them with his skillful hand — te.vu.nah expressed in guiding action |
| 173421 | Psa 82:5 | H0995 bin | 932-001 | CONFIRM | Neither knowledge nor understanding — absence causing moral darkness |
| 173422 | Psa 92:6 | H0995 bin | 932-001 | CONFIRM | The fool cannot understand this — faculty the fool lacks |
| 173423 | Psa 94:7 | H0995 bin | 932-003 | CONFIRM | The God of Jacob does not perceive — wicked deny God's perception |
| 173424 | Psa 94:8 | H0995 bin | 932-004 | CONFIRM | Understand, O dullest of the people — command to exercise the refused faculty |
| 173399 | Psa 107:43 | H0995 bin | 932-001 | CONFIRM | Let them consider the steadfast love of the Lord |
| 173406 | Psa 119:27 | H0995 bin | 932-002 | CONFIRM | Make me understand the way of your precepts — petition |
| 173407 | Psa 119:34 | H0995 bin | 932-002 | CONFIRM | Give me understanding that I may keep your law |
| 173408 | Psa 119:73 | H0995 bin | 932-002 | CONFIRM | Give me understanding that I may learn |
| 173409 | Psa 119:95 | H0995 bin | 932-002 | CONFIRM | I consider your testimonies — faculty directed toward God's word |
| 173400 | Psa 119:100 | H0995 bin | 932-002 | CONFIRM | I understand more than the aged, for I keep your precepts |
| 173401 | Psa 119:104 | H0995 bin | 932-002 | CONFIRM | Through your precepts I get understanding |
| 173402 | Psa 119:125 | H0995 bin | 932-002 | CONFIRM | Give me understanding that I may know your testimonies |
| 173403 | Psa 119:130 | H0995 bin | 932-002 | CONFIRM | Unfolding of your words gives light; imparts understanding to the simple |
| 173404 | Psa 119:144 | H0995 bin | 932-002 | CONFIRM | Give me understanding that I may live |
| 173405 | Psa 119:169 | H0995 bin | 932-002 | CONFIRM | Give me understanding according to your word |
| 7111 | Psa 136:5 | H8394 te.vu.nah | 524-001 | CONFIRM | To him who by understanding made the heavens — divine creative attribute |
| 173410 | Psa 139:2 | H0995 bin | 932-003 | CONFIRM | You discern my thoughts from afar — God's perceptive comprehension of inner person |
| 7112 | Psa 147:5 | H8394 te.vu.nah | 524-001 | CONFIRM | His understanding is beyond measure — infinite divine attribute |
| 173369 | Pro 1:2 | H0995 bin | 932-001 | CONFIRM | To understand words of insight — faculty required for Proverbs |
| 7074 | Pro 1:2 | H0998 bi.nah | 523-002 | CONFIRM | Words of insight — bi.nah as the inner content to be grasped |
| 173370 | Pro 1:5 | H0995 bin | 932-001 | CONFIRM | The one who understands obtains guidance |
| 173371 | Pro 1:6 | H0995 bin | 932-001 | CONFIRM | To understand a proverb and a saying |
| 7113 | Pro 2:2 | H8394 te.vu.nah | 524-002 | CONFIRM | Inclining your heart to understanding |
| 7075 | Pro 2:3 | H0998 bi.nah | 523-002 | CONFIRM | Call out for insight — urgent petition for bi.nah |
| 7114 | Pro 2:3 | H8394 te.vu.nah | 524-002 | CONFIRM | Raise your voice for understanding — te.vu.nah urgently sought |
| 173384 | Pro 2:5 | H0995 bin | 932-001 | CONFIRM | Then you will understand the fear of the Lord |
| 7115 | Pro 2:6 | H8394 te.vu.nah | 524-002 | CONFIRM | From his mouth come knowledge and understanding |
| 173385 | Pro 2:9 | H0995 bin | 932-001 | CONFIRM | Then you will understand righteousness and justice and equity |
| 7116 | Pro 2:11 | H8394 te.vu.nah | 524-002 | CONFIRM | Understanding will guard you — protective function |
| 7076 | Pro 3:5 | H0998 bi.nah | 523-002 | CONFIRM | Do not lean on your own understanding — bi.nah as something to surrender |
| 7117 | Pro 3:13 | H8394 te.vu.nah | 524-002 | CONFIRM | Blessed is the one who gets understanding |
| 7118 | Pro 3:19 | H8394 te.vu.nah | 524-002 | CONFIRM | By understanding he established the heavens — note: this is divine attribute; FLAG — should be in 524-001 not 524-002 |
| 7077 | Pro 4:1 | H0998 bi.nah | 523-002 | CONFIRM | Be attentive that you may gain insight |
| 7078 | Pro 4:5 | H0998 bi.nah | 523-002 | CONFIRM | Get wisdom; get insight |
| 7079 | Pro 4:7 | H0998 bi.nah | 523-002 | CONFIRM | Whatever you get, get insight |
| 7119 | Pro 5:1 | H8394 te.vu.nah | 524-002 | CONFIRM | Incline your ear to my understanding — teacher offering inner capacity |
| 7080 | Pro 7:4 | H0998 bi.nah | 523-002 | CONFIRM | Call insight your intimate friend |
| 173396 | Pro 7:7 | H0995 bin | 932-001 | CONFIRM | I perceived among the youths a young man lacking sense — teacher's perceptive act |
| 7120 | Pro 8:1 | H8394 te.vu.nah | 524-002 | CONFIRM | Does not understanding raise her voice — personified as Wisdom's companion |
| 173397 | Pro 8:5 | H0995 bin | 932-001 | CONFIRM | O fools, learn sense — faculty called for |
| 173398 | Pro 8:9 | H0995 bin | 932-001 | CONFIRM | They are all straight to him who understands |
| 7081 | Pro 8:14 | H0998 bi.nah | 523-002 | CONFIRM | I have insight; I have strength — Wisdom holds bi.nah |
| 7082 | Pro 9:6 | H0998 bi.nah | 523-002 | CONFIRM | Walk in the way of insight |
| 7083 | Pro 9:10 | H0998 bi.nah | 523-002 | CONFIRM | Knowledge of the Holy One is insight — defining equation |
| 173372 | Pro 10:13 | H0995 bin | 932-001 | CONFIRM | On the lips of him who has understanding, wisdom is found |
| 7121 | Pro 10:23 | H8394 te.vu.nah | 524-002 | CONFIRM | Wisdom is pleasure to a man of understanding |
| 7122 | Pro 11:12 | H8394 te.vu.nah | 524-002 | CONFIRM | A man of understanding remains silent |
| 173375 | Pro 14:6 | H0995 bin | 932-001 | CONFIRM | Knowledge is easy for a man of understanding |
| 173376 | Pro 14:8 | H0995 bin | 932-001 | CONFIRM | Wisdom of the prudent is to discern his way |
| 173373 | Pro 14:15 | H0995 bin | 932-001 | CONFIRM | The prudent gives thought to his steps — attentive inner reflection |
| 7123 | Pro 14:29 | H8394 te.vu.nah | 524-002 | CONFIRM | Whoever is slow to anger has great understanding |
| 173374 | Pro 14:33 | H0995 bin | 932-001 | CONFIRM | Wisdom rests in the heart of a man of understanding |
| 173377 | Pro 15:14 | H0995 bin | 932-001 | CONFIRM | Heart of him who has understanding seeks knowledge |
| 7124 | Pro 15:21 | H8394 te.vu.nah | 524-002 | CONFIRM | Man of understanding walks straight ahead |
| 7084 | Pro 16:16 | H0998 bi.nah | 523-002 | CONFIRM | To get understanding is to be chosen rather than silver |
| 173378 | Pro 16:21 | H0995 bin | 932-001 | CONFIRM | Wise of heart is called discerning |
| 173379 | Pro 17:10 | H0995 bin | 932-001 | CONFIRM | A rebuke goes deeper into a man of understanding |
| 173380 | Pro 17:24 | H0995 bin | 932-001 | CONFIRM | The discerning sets his face toward wisdom |
| 7125 | Pro 17:27 | H8394 te.vu.nah | 524-002 | CONFIRM | He who has a cool spirit is a man of understanding |
| 173381 | Pro 17:28 | H0995 bin | 932-001 | CONFIRM | When he closes his lips he is deemed intelligent |
| 7126 | Pro 18:2 | H8394 te.vu.nah | 524-002 | CONFIRM | A fool takes no pleasure in understanding |
| 173382 | Pro 18:15 | H0995 bin | 932-001 | CONFIRM | Intelligent heart acquires knowledge |
| 7127 | Pro 19:8 | H8394 te.vu.nah | 524-002 | CONFIRM | He who keeps understanding will discover good |
| 173383 | Pro 19:25 | H0995 bin | 932-001 | CONFIRM | Reprove a man of understanding and he will gain knowledge |
| 7128 | Pro 20:5 | H8394 te.vu.nah | 524-002 | CONFIRM | Man of understanding will draw out deep purposes |
| 173386 | Pro 20:24 | H0995 bin | 932-001 | CONFIRM | How then can man understand his way — limits of self-understanding |
| 173387 | Pro 21:29 | H0995 bin | 932-001 | CONFIRM | The upright gives thought to his ways |
| 7129 | Pro 21:30 | H8394 te.vu.nah | 524-001 | CONFIRM | No understanding can avail against the Lord — human te.vu.nah limited before God; placed in 524-001 acceptable |
| 173388 | Pro 23:1 | H0995 bin | 932-001 | CONFIRM | Observe carefully what is before you — attentive situational awareness |
| 7085 | Pro 23:4 | H0998 bi.nah | 523-002 | CONFIRM | Be discerning enough to desist |
| 7086 | Pro 23:23 | H0998 bi.nah | 523-002 | CONFIRM | Buy wisdom, instruction, and understanding |
| 7130 | Pro 24:3 | H8394 te.vu.nah | 524-002 | CONFIRM | By understanding a house is established |
| 173389 | Pro 24:12 | H0995 bin | 816-002 | FLAG | Does not he who weighs the heart perceive it — God's perceptive comprehension; this is 932-003 function placed in 816-002; FLAG for researcher review — may need move to 932-003 |
| 173391 | Pro 28:2 | H0995 bin | 932-001 | CONFIRM | Man of understanding and knowledge brings stability |
| 173392 | Pro 28:5 | H0995 bin | 932-001 | CONFIRM | Those who seek the Lord understand it completely |
| 173393 | Pro 28:7 | H0995 bin | 932-001 | CONFIRM | One who keeps the law is a son with understanding |
| 173390 | Pro 28:11 | H0995 bin | 932-001 | CONFIRM | Poor man who has understanding will find him out |
| 7131 | Pro 28:16 | H8394 te.vu.nah | 524-002 | CONFIRM | Ruler who lacks understanding is a cruel oppressor |
| 173395 | Pro 29:7 | H0995 bin | 932-001 | CONFIRM | A wicked man does not understand such knowledge |
| 173394 | Pro 29:19 | H0995 bin | 932-001 | CONFIRM | He understands but will not respond — understanding without compliance |
| 7087 | Pro 30:2 | H0998 bi.nah | 523-002 | CONFIRM | I have not the understanding of a man — Agur's disclaimer |
| 173366 | Ecc 9:11 | H0995 bin | 932-001 | CONFIRM | Nor riches to the intelligent — inner quality not guaranteeing outcome |
| 27709 | Isa 1:3 | H0995 bin | 932-004 | CONFIRM | Israel does not understand — covenantal failure to perceive God |
| 27716 | Isa 3:3 | H0995 bin | 932-001 | CONFIRM | Expert in charms — bin as specialised inner competence |
| 27723 | Isa 5:21 | H0995 bin | 932-004 | CONFIRM | Shrewd in their own sight — self-attributed shrewdness; within 932-004 scope |
| 27728 | Isa 6:9 | H0995 bin | 932-004 | CONFIRM | Keep on hearing but do not understand — judicial withholding |
| 27727 | Isa 6:10 | H0995 bin | 932-004 | CONFIRM | Lest they understand with their hearts and turn — faculty blocked by judgment |
| **27710** | **Isa 10:13** | **H0995 bin** | **932-004** | **FLAG** | "By my wisdom, for I have understanding" — Assyrian king's self-attributed bin; this is claiming understanding as self-sourced, not a failure; 932-004 description ("failure, hardening, absence") does not fit; FLAG for researcher decision — may belong in 932-001 alongside 528-003 type uses |
| 7088 | Isa 11:2 | H0998 bi.nah | 523-002 | CONFIRM | Spirit of wisdom and understanding — Spirit-given bi.nah on the Messiah |
| 27711 | Isa 14:16 | H0995 bin | 932-001 | CONFIRM | Those who see you will stare and ponder — reflective perceptive attending |
| 7089 | Isa 27:11 | H0998 bi.nah | 523-002 | CONFIRM | People without discernment — bi.nah absent resulting in divine withdrawal |
| 27713 | Isa 28:9 | H0995 bin | 932-004 | CONFIRM | To whom will he explain the message — audience lacks capacity to receive |
| 27712 | Isa 28:19 | H0995 bin | 932-004 | CONFIRM | It will be sheer terror to understand the message |
| 27714 | Isa 29:14 | H0995 bin | 932-004 | CONFIRM | Discernment of discerning men shall be hidden — God withholding the faculty's access |
| 7090 | Isa 29:14 | H0998 bi.nah | 523-002 | CONFIRM | Bi.nah of discerning men hidden — same verse; bi.nah row |
| 27715 | Isa 29:16 | H0995 bin | 932-004 | CONFIRM | He has no understanding — absurdity of creature judging Creator |
| 7091 | Isa 29:24 | H0998 bi.nah | 523-002 | CONFIRM | Those who go astray in spirit will come to understanding — bi.nah as destination of restoration |
| 27717 | Isa 32:4 | H0995 bin | 932-004 | CONFIRM | Heart of the hasty will understand and know — future opening of faculty; 932-004 holds in transition sense |
| 7092 | Isa 33:19 | H0998 bi.nah | 523-002 | CONFIRM | Tongue you cannot understand — bi.nah faced with unintelligible speech |
| 27718 | Isa 40:14 | H0995 bin | 816-002 | CONFIRM | Who made him understand — rhetorical: no one; God's understanding is self-originating |
| 7132 | Isa 40:14 | H8394 te.vu.nah | 816-002 | CONFIRM | Showed him the way of understanding — same verse; te.vu.nah row; 816-002 holds |
| 27719 | Isa 40:21 | H0995 bin | 932-002 | CONFIRM | Have you not understood from the foundations — knowledge available from the beginning |
| 7133 | Isa 40:28 | H8394 te.vu.nah | 524-001 | CONFIRM | His understanding is unsearchable — infinite divine attribute |
| 27720 | Isa 43:10 | H0995 bin | 932-002 | CONFIRM | Know and believe me and understand that I am he |
| 27721 | Isa 43:18 | H0995 bin | 932-002 | CONFIRM | Nor consider the things of old — redirecting the faculty |
| 27722 | Isa 44:18 | H0995 bin | 932-004 | CONFIRM | Their hearts cannot understand — God has shut their eyes |
| 7134 | Isa 44:19 | H8394 te.vu.nah | 524-002 | CONFIRM | No discernment in the idol-worshipper — te.vu.nah absent |
| 27724 | Isa 52:15 | H0995 bin | 932-002 | CONFIRM | What they have not heard they understand — nations receiving new comprehension |
| 27725 | Isa 56:11 | H0995 bin | 932-004 | CONFIRM | Shepherds who have no understanding — absent faculty in false shepherds |
| 27726 | Isa 57:1 | H0995 bin | 932-004 | CONFIRM | No one understands — community fails to perceive meaning of righteous person's death |
| 27729 | Jer 2:10 | H0995 bin | 932-004 | CONFIRM | Examine with care — directive to use the faculty; 932-004 loose; FLAG — this is a call to use bin, not a failure; similar to Psa 73:17 |
| 27732 | Jer 4:22 | H0995 bin | 932-004 | CONFIRM | They have no understanding — absent faculty in Israel |
| 27734 | Jer 9:12 | H0995 bin | 932-004 | CONFIRM | Who is the man so wise that he can understand this |
| 27735 | Jer 9:17 | H0995 bin | 932-001 | CONFIRM | Consider, and call for the mourning women — directive to reflective attending |
| 7135 | Jer 10:12 | H8394 te.vu.nah | 524-001 | CONFIRM | By his understanding stretched out the heavens — divine creative attribute |
| 27730 | Jer 23:20 | H0995 bin | 932-004 | CONFIRM | In the latter days you will understand it clearly — future opening; 932-004 holds as transition |
| 7093 | Jer 23:20 | H0998 bi.nah | 523-002 | CONFIRM | Clearly — the quality of the future understanding |
| 27731 | Jer 30:24 | H0995 bin | 932-004 | CONFIRM | In the latter days you will understand this — same pattern |
| 27733 | Jer 49:7 | H0995 bin | 932-001 | CONFIRM | Has counsel perished from the prudent — bin as source of counsel |
| 7136 | Jer 51:15 | H8394 te.vu.nah | 524-001 | CONFIRM | By his understanding stretched out the heavens — repeated divine creative attribute |
| **7137** | **Eze 28:4** | **H8394 te.vu.nah** | **524-002** | **FLAG / MOVE** | By your wisdom and your understanding you have made wealth for yourself — self-enriching understanding; does not fit 524-002 description ("enabling wisdom, right conduct, and discernment, received from God"); CREATE new VCG for self-enriching/self-serving te.vu.nah; parallel with Hos 13:2 |
| 27687 | Dan 1:4 | H0995 bin | 932-001 | CONFIRM | Endowed with knowledge, understanding, learning — inner qualities of the youths |
| 27686 | Dan 1:17 | H0995 bin | 932-001 | CONFIRM | Daniel had understanding in all visions and dreams — God-given specific inner capacity |
| 7094 | Dan 1:20 | H0998 bi.nah | 523-002 | CONFIRM | In every matter of wisdom and understanding — tested and verified bi.nah |
| 45700 | Dan 2:21 | H0999 bi.nah | 1204-001 | CONFIRM | He gives wisdom to the wise and knowledge to those who have understanding — 1204-001 correct |
| 27701 | Dan 8:5 | H0995 bin | 932-002 | CONFIRM | As I was considering — Daniel directing his inner faculty toward the vision |
| 7096 | Dan 8:15 | H0998 bi.nah | 523-002 | CONFIRM | I sought to understand it — seeking bi.nah of the vision |
| 27697 | Dan 8:16 | H0995 bin | 932-002 | CONFIRM | Gabriel, make this man understand the vision — imparting bin as divine gift |
| 27698 | Dan 8:17 | H0995 bin | 932-002 | CONFIRM | Understand, O son of man — command to receive the vision's meaning |
| 27699 | Dan 8:23 | H0995 bin | 932-001 | CONFIRM | King of bold face, one who understands riddles — bin as attribute of the dangerous figure |
| 27700 | Dan 8:27 | H0995 bin | 932-004 | CONFIRM | I did not understand it — Daniel could not grasp the vision's meaning |
| 27702 | Dan 9:2 | H0995 bin | 932-002 | CONFIRM | I perceived in the books — bin as perceptive grasping of prophetic text |
| 27703 | Dan 9:22 | H0995 bin | 816-002 | CONFIRM | I have come to give you insight and understanding — Gabriel bringing divine comprehension; 816-002 correct |
| 7097 | Dan 9:22 | H0998 bi.nah | 816-002 | CONFIRM | Understanding conveyed by Gabriel — same verse; bi.nah row; 816-002 correct |
| 27704 | Dan 9:23 | H0995 bin | 932-002 | CONFIRM | Consider the word and understand the vision — reflective petitionary attending |
| 27688 | Dan 10:1 | H0995 bin | 932-002 | CONFIRM | He understood the word and had understanding of the vision |
| 7098 | Dan 10:1 | H0998 bi.nah | 523-002 | CONFIRM | Understanding of the vision — bi.nah attained |
| 27689 | Dan 10:11 | H0995 bin | 932-002 | CONFIRM | Understand the words that I speak to you — command to receive |
| 27690 | Dan 10:12 | H0995 bin | 932-002 | CONFIRM | From the first day you set your heart to understand |
| 27691 | Dan 10:14 | H0995 bin | 932-002 | CONFIRM | I came to make you understand what is to happen |
| **27692** | **Dan 11:30** | **H0995 bin** | **932-004** | **MOVE** | **→ 932-001 or CREATE new directional-attending VCG** — "pay attention to those who forsake the holy covenant"; bin as directed perceptive attention toward persons, not failure of understanding; 932-004 description does not apply |
| 27693 | Dan 11:33 | H0995 bin | 932-001 | CONFIRM | Wise among the people shall make many understand — wisdom enabling others to receive |
| **27694** | **Dan 11:37** | **H0995 bin** | **932-004** | **MOVE** | **→ 932-001 or same new directional-attending VCG** — "pays no attention to the gods of his fathers"; deliberate withdrawal of perceptive attention; not failure of understanding |
| 27696 | Dan 12:8 | H0995 bin | 932-004 | CONFIRM | I heard but I did not understand — Daniel could not grasp the final vision's meaning |
| 27695 | Dan 12:10 | H0995 bin | 932-001 | CONFIRM | Those who are wise shall understand — moral conditionality of bin |
| 27708 | Hos 4:14 | H0995 bin | 932-001 | CONFIRM | A people without understanding shall come to ruin — absent bin causing destruction |
| **7138** | **Hos 13:2** | **H8394 te.vu.nah** | **524-002** | **FLAG / MOVE** | Idols skillfully made — te.vu.nah as craft skill for idol-making; does not fit "enabling wisdom, right conduct, discernment, received from God"; CREATE new VCG alongside Eze 28:4 |
| 27707 | Hos 14:9 | H0995 bin | 932-001 | CONFIRM | Whoever is discerning let him know — bin as inner capacity enabling perception of God's ways |
| 209060 | Obd 7 | H8394 te.vu.nah | 524-002 | CONFIRM | You have no understanding — te.vu.nah absent in Edom; 524-002 holds |
| 209061 | Obd 8 | H8394 te.vu.nah | 524-002 | CONFIRM | Destroy understanding out of Mount Esau — God removing inner capacity from Edom |
| 27759 | Mic 4:12 | H0995 bin | 932-004 | CONFIRM | They do not understand his plan — nations cannot grasp God's purposes |
| 205776 | Mat 11:25 | G4908 sunetos | 1201-001 | CONFIRM | Hidden from the wise and understanding — sunetos as category excluded from divine disclosure |
| 205763 | Mat 13:13 | G4920 suniēmi | 932-004 | CONFIRM | Seeing they do not see, hearing they do not understand — judicial withholding |
| 205764 | Mat 13:14 | G4920 suniēmi | 932-004 | CONFIRM | You will hear but never understand — same judicial pattern |
| 205765 | Mat 13:15 | G4920 suniēmi | 1205-001 | CONFIRM | Lest they understand with their heart and turn — understanding that would produce repentance |
| 205766 | Mat 13:19 | G4920 suniēmi | 932-004 | CONFIRM | Anyone who hears and does not understand — absence allowing snatching |
| 205767 | Mat 13:23 | G4920 suniēmi | 1205-001 | CONFIRM | One who hears and understands it bears fruit — understanding producing fruit |
| 205768 | Mat 13:51 | G4920 suniēmi | 1205-001 | CONFIRM | Have you understood all these things |
| 205769 | Mat 15:10 | G4920 suniēmi | 932-004 | CONFIRM | Hear and understand — command to receive; 932-004 loose; note |
| 205773 | Mat 15:16 | G0801 asunetos | 1202-001 | CONFIRM | Are you also still without understanding |
| 205770 | Mat 16:12 | G4920 suniēmi | 1205-001 | CONFIRM | Then they understood that he did not tell them |
| 205771 | Mat 17:13 | G4920 suniēmi | 1205-001 | CONFIRM | Then the disciples understood — inner comprehension of reference |
| 205758 | Mar 4:12 | G4920 suniēmi | 932-004 | CONFIRM | Lest they turn and be forgiven — parable withholds understanding |
| 205759 | Mar 6:52 | G4920 suniēmi | 1205-002 | CONFIRM | Did not understand about the loaves; hearts were hardened |
| 205760 | Mar 7:14 | G4920 suniēmi | 1205-001 | CONFIRM | Hear me and understand — command |
| 205772 | Mar 7:18 | G0801 asunetos | 1202-001 | CONFIRM | Are you also without understanding |
| 205761 | Mar 8:17 | G4920 suniēmi | 1205-002 | CONFIRM | Do you not yet understand; hearts hardened |
| 205762 | Mar 8:21 | G4920 suniēmi | 1205-002 | CONFIRM | Do you not yet understand — repeated failure |
| 155813 | Mar 12:33 | G4907 sunesis | 816-001 | CONFIRM | To love him with all understanding — sunesis directed wholly toward God as love |
| 7456 | Luk 1:17 | G5428 fronesis | 531-001 | CONFIRM | Wisdom of the just — fronesis as moral orientation of the righteous |
| 155812 | Luk 2:47 | G4907 sunesis | 816-002 | CONFIRM | Amazing at his understanding and answers — sunesis visible in the twelve-year-old Jesus |
| 205755 | Luk 2:50 | G4920 suniēmi | 932-004 | CONFIRM | They did not understand the saying — Mary and Joseph could not grasp |
| 205757 | Luk 8:10 | G4920 suniēmi | 932-004 | CONFIRM | Hearing they may not understand — parable form withholds |
| 205775 | Luk 10:21 | G4908 sunetos | 1201-001 | CONFIRM | Hidden from the wise and understanding — same as Mat 11:25 |
| 205754 | Luk 18:34 | G4920 suniēmi | 1205-002 | CONFIRM | They understood none of these things — complete failure re passion prediction |
| 205756 | Luk 24:45 | G4920 suniēmi | 1205-001 | CONFIRM | He opened their minds to understand the Scriptures — Christ activating the faculty |
| 205753 | Act 7:25 | G4920 suniēmi | 932-004 | CONFIRM | They did not understand — Israel's failure to perceive Moses's deliverance |
| 205774 | Act 13:7 | G4908 sunetos | 1201-001 | CONFIRM | Sergius Paulus, a man of intelligence — sunetos as openness to the word |
| 205751 | Act 28:26 | G4920 suniēmi | 932-004 | CONFIRM | You will hear but never understand — Isaiah pattern applied to Israel |
| 205752 | Act 28:27 | G4920 suniēmi | 932-004 | CONFIRM | Lest they understand with their heart and turn — same judicial pattern |
| 45173 | Rom 1:21 | G0801 asunetos | 1202-001 | CONFIRM | Foolish hearts were darkened — asunetos as fallen inner condition |
| 45174 | Rom 1:31 | G0801 asunetos | 1202-001 | CONFIRM | Foolish, faithless, heartless — asunetos in list of moral failures |
| 45704 | Rom 3:11 | G4920 suniēmi | 932-004 | CONFIRM | No one understands; no one seeks God — universal failure of comprehension |
| 45175 | Rom 10:19 | G0801 asunetos | 1202-001 | CONFIRM | A foolish nation I will make you angry — asunetos as God's instrument |
| 45703 | Rom 15:21 | G4920 suniēmi | 1205-001 | CONFIRM | Those who have never heard will understand — spread of comprehension |
| 19554 | 1Cor 1:19 | G4907 sunesis | 816-002 | CONFIRM | Discernment of the discerning I will thwart — divine action against human sunesis |
| 45172 | 1Cor 1:19 | G4908 sunetos | 816-002 | CONFIRM | Same verse — sunetos row; both in 816-002 correct |
| 45701 | 2Cor 10:12 | G4920 suniēmi | 1205-003 | CONFIRM | They are without understanding — self-comparison as non-understanding |
| 7457 | Eph 1:8 | G5428 fronesis | 531-001 | CONFIRM | In all wisdom and insight — fronesis lavished as divine gift |
| 19557 | Eph 3:4 | G4907 sunesis | 816-001 | CONFIRM | You can perceive my insight into the mystery of Christ |
| 45702 | Eph 5:17 | G4920 suniēmi | 1205-003 | CONFIRM | Understand what the will of the Lord is — practical inner comprehension |
| 19555 | Col 1:9 | G4907 sunesis | 816-001 | CONFIRM | Filled with knowledge of his will in all spiritual wisdom and understanding |
| 19556 | Col 2:2 | G4907 sunesis | 816-001 | CONFIRM | Full assurance of understanding and knowledge of God's mystery |
| 155811 | 2Ti 2:7 | G4907 sunesis | 816-002 | CONFIRM | The Lord will give you understanding in everything — divine gift of sunesis |
| 54646 | Jam 3:13 | G1990 epistēmōn | 1207-001 | CONFIRM | Who is wise and understanding — epistēmōn verified by conduct |

---

### M15-B action summary

**MOVE actions (2 verses):**

| # | vr_id | Reference | From | To |
|---|---|---|---|---|
| 1 | 27692 | Dan 11:30 (bin) | 932-004 | 932-001 or CREATE new directional-attending VCG |
| 2 | 27694 | Dan 11:37 (bin) | 932-004 | 932-001 or same new VCG |

**FLAG / MOVE actions requiring CREATE-VCG (2 verses):**

| # | vr_id | Reference | From | Action |
|---|---|---|---|---|
| 3 | 7137 | Eze 28:4 (te.vu.nah) | 524-002 | CREATE new VCG — te.vu.nah in self-serving/non-sacred use |
| 4 | 7138 | Hos 13:2 (te.vu.nah) | 524-002 | MOVE to same new VCG |

**CREATE-VCG actions (2):**

| # | Term | mti_id | Description |
|---|---|---|---|
| 1 | H0995 bin | 932 | Directional attending — bin as perceptive attention directed toward or deliberately withdrawn from an object; Dan 11:30 and 11:37 |
| 2 | H8394 te.vu.nah | 524 | Te.vu.nah in self-serving or non-sacred application — same inner faculty directed toward material gain (Eze 28:4) or idolatrous craft (Hos 13:2) |

**UPDATE-DESC actions (1):**

| # | VCG | Required change |
|---|---|---|
| 1 | 524-002 | After removing Eze 28:4 and Hos 13:2, the description is more coherent; update to remove any implication that all te.vu.nah uses are "received from God" and note the directional-neutrality of the faculty in M15-A-style language |

**FLAG actions (8):**
- Deu 4:6 bin (173365) and bi.nah (7060) — both in 816-002; primary meaning is covenant obedience producing visible understanding; researcher to decide whether to keep in 816-002 or move to 932-001/523-002
- 1Sa 3:8 (173355) — successful perception placed in 932-004; loose fit
- Job 13:1 (27737) — successful understanding placed in 932-004; loose fit
- Job 32:12 (27748) — active attention placed in 932-004; loose fit
- Isa 10:13 (27710) — self-attributed understanding placed in 932-004; misfit; consider moving to 932-001 or 528-003 type group
- Jer 2:10 (27729) — command to use bin placed in 932-004; loose
- Psa 73:17 (173420) — successful discernment placed in 932-004; loose
- Pro 3:19 te.vu.nah (7118) — divine attribute placed in 524-002; should be 524-001

**SA rows (2):** Ezr 8:15 (173367) and Psa 58:9 (173419) — both confirmed correctly SA

**CONFIRM actions: 275 verses**


---

## M15-C — 602 verses, 22 DB VCGs

### VCG inventory (DB state)

| VCG code | Term | Description | DB count |
|---|---|---|---|
| 958-001 | H3045 ya.da | Covenantal/relational knowing — God and Israel | 112 |
| 958-002 | H3045 ya.da | Self-knowledge of inner moral condition before God | 45 |
| 958-003 | H3045 ya.da | God's comprehensive knowledge of the inner person | 31 |
| 958-004 | H3045 ya.da | Moral knowledge guiding right action | 43 |
| 958-005 | H3045 ya.da | God's revelatory self-disclosure | 33 |
| 955-001 | H1847 da.at | Knowledge as foundational inner capacity | 48 |
| 955-002 | H1847 da.at | Knowledge of God as defining inner orientation | 10 |
| 955-003 | H1847 da.at | Knowledge as Spirit-given inner endowment | 9 |
| 955-004 | H1847 da.at | Da.at as inner intent determining accountability | 6 |
| 955-005 | H1847 da.at | Limits and failures of human knowledge | 10 |
| 1838-001 | G0050 agnoeō / H1847 da.at | Culpable spiritual ignorance | 12 |
| 963-001 | G6063 oida | Settled inner conviction orienting life toward God | 31 |
| 963-002 | G6063 oida | Self-knowledge of inner conflict | 4 |
| 963-003 | G6063 oida | Identity-shaping knowledge | 8 |
| 963-004 | G6063 oida | God's or another's knowledge of the inner person | 5 |
| 963-005 | G6063 oida | Knowledge divorced from love | 2 |
| 961-001 | H1843 de.a | Inner formed judgment or opinion | 3 |
| 961-002 | H1843 de.a | Knowledge oriented toward God — divine perfection | 2 |
| 959-001 | H1844 de.ah | God's perfect knowledge as ground of accountability | 3 |
| 959-002 | H1844 de.ah | Knowledge of God as content of inner formation | 3 |
| 962-001 | H4486 man.da | Knowledge as divine gift | 2 |
| 962-002 | H4486 man.da | Reason as defining inner capacity of humanness | 2 |

**P-status rows: 157 · SA rows: 21**

---

### Per-verse action — M15-C

Given the size of M15-C (602 verses), actions are organised by VCG. All G-status rows not listed for MOVE or FLAG are CONFIRMED correctly placed.

#### VCG 1838-001 — All 12 G-status rows individually addressed

| vr_id | Reference | Term | Action | Reason |
|---|---|---|---|---|
| 178151 | Exo 31:3 | H1847 da.at | **MOVE → 955-003** | "Filled with the Spirit of God with ability and intelligence, with knowledge" — positive Spirit-given da.at; clearly not culpable ignorance |
| 29499 | Num 24:16 | H1847 da.at | **FLAG** | "Who knows the knowledge of the Most High" — Balaam description; positive capacity; not culpable ignorance; researcher to confirm → 955-003 or 955-001 |
| 29766 | Num 24:16 | H3045 ya.da | **FLAG** | Same verse; ya.da row; same issue; confirm destination |
| 178196 | Psa 19:2 | H1847 da.at | **MOVE → 955-001** | "Night to night reveals knowledge" — creation pouring out da.at; positive disclosure; misrouted |
| 29474 | Hos 6:6 | H1847 da.at | **MOVE → 955-002** | "Knowledge of God rather than burnt offerings" — God's desire for relational da.at; positive statement; misrouted |
| 82258 | Act 13:27 | G0050 agnoeō | CONFIRM | Rulers did not recognise Jesus nor the prophets — culpable spiritual ignorance resulting in crucifixion; 1838-001 correct |
| 82259 | Act 17:23 | G0050 agnoeō | CONFIRM | What you worship as unknown — worshipping without knowing the object; culpable inner ignorance; 1838-001 correct |
| 82267 | Rom 2:4 | G0050 agnoeō | CONFIRM | Not knowing God's kindness leads to repentance — culpable ignorance of divine purpose; 1838-001 correct |
| 82265 | Rom 10:3 | G0050 agnoeō | CONFIRM | Ignorant of God's righteousness, seeking own — culpable inner ignorance as root of failure; 1838-001 correct |
| 82255 | 2Cor 2:11 | G0050 agnoeō | CONFIRM | We are not ignorant of Satan's designs — naming the opposite; 1838-001 correct |
| 82253 | 1Ti 1:13 | G0050 agnoeō | CONFIRM | I received mercy because I acted ignorantly in unbelief — culpable inner ignorance; 1838-001 correct |
| 82257 | 2Pe 2:12 | G0050 agnoeō | CONFIRM | Blaspheming about matters of which they are ignorant — culpable; 1838-001 correct |

**Note on 1838-001 split:** The P-status and SA agnoeō rows (Rom 1:13, 6:3, 7:1, 1Cor 10:1, 12:1, 1Th 4:13, Heb 5:2, 2Cor 1:8, 6:9, Gal 1:22, Mar 9:32, Luk 9:45) use agnoeō in the neutral informational sense ("I do not want you to be unaware/uninformed"). These will need a CREATE-VCG when processed. For now, as P-status they are pending — no immediate action beyond the flag.

#### All other VCGs — CONFIRM (batch)

**955-001 (48 G-rows):** All Proverbs, Job, Ecclesiastes, and Malachi da.at verses naming knowledge as the wise person's inner possession or content of wise speech. All CONFIRM correctly placed.

**955-002 (10 G-rows — Hos 4:1, 4:6, Isa 5:13, 58:2, Jer 22:16, Psa 119:66, Job 21:14, 36:12; + moves in):** All CONFIRM. Note Hos 6:6 moving in from 1838-001 (see above).

**955-003 (9 G-rows — Isa 11:2, 33:6, 40:14, 53:11, Dan 1:4, 12:4, Job 21:22, Psa 94:10, Exo 35:31; + Exo 31:3 moving in):** All CONFIRM. Isa 53:11 ("by his knowledge the servant makes many righteous") is the most analytically significant verse — correctly placed. Flag for Session D synthesis highlight.

**955-004 (6 G-rows — Deu 4:42, 19:4, Jos 20:3, 20:5, Job 10:7, Psa 139:6):** All CONFIRM. Da.at as inner intent determining culpability of an act.

**955-005 (10 G-rows — Job 34:35, 35:16, 38:2, 42:3, Isa 44:19, 44:25, 47:10, Jer 10:14, 51:17, Job 15:2):** All CONFIRM. Knowledge absent or emptied of substance.

**958-001 (112 G-rows):** Covenantal relational knowing — all CONFIRM. Extremely large group; all correctly placed. Includes Gen 18:19 (election knowing), Amos 3:2 (defining election verse), Deu 34:10 (face-to-face knowing), all Deuteronomy covenantal commands to know, all Hosea Israel-knowing-God passages, all Zechariah "then you shall know" pattern, all patriarchal narrative knowing-God verses.

**958-002 (45 G-rows):** Self-knowledge and limits before God — all CONFIRM. Includes Job 19:25 ("I know my Redeemer lives"), Ecc 9:5 ("the living know they will die"), Job 9:21 (self-regard).

**958-003 (31 G-rows):** God's comprehensive knowing of persons — all CONFIRM. Includes Gen 20:6 (God knows Abimelech's integrity), Job 23:10 (God knows Job's path), Isa 37:28 (God knows Assyrian's every move), 1Sa 3:13 (Eli knew the iniquity).

**958-004 (43 G-rows):** Moral knowledge guiding action — all CONFIRM. Includes Gen 3:7, 3:22 (knowing good and evil post-fall), Jer 22:16 (knowing God = doing justice — defining verse; flag for Session D), Mic 3:1 (is it not for you to know justice), Pro 29:7 (righteous knows rights of the poor).

**958-005 (33 G-rows):** God's revelatory self-disclosure — all CONFIRM. Includes Deu 8:3 ("that he might make you know"), Isa 45:3 ("that you may know it is I"), all Zechariah sent-messenger pattern, all Isa 40–55 disclosure-through-event pattern.

**959-001 (3 G-rows — 1Sa 2:3, Psa 73:11, Job 36:4):** All CONFIRM. De.ah as divine perfect knowledge.

**959-002 (3 G-rows — Isa 11:9, 28:9, Jer 3:15):** All CONFIRM. De.ah as content of formation/eschatological filling.

**961-001 (3 G-rows — Job 32:6, 32:10, 32:17):** All CONFIRM. De.a as inner formed opinion held and released.

**961-002 (2 G-rows — Job 36:3, 37:16):** All CONFIRM. De.a directed toward God or naming divine perfect knowing.

**962-001 (2 G-rows — Dan 2:21, 5:12):** All CONFIRM. Man.da as divine gift of knowledge.

**962-002 (2 G-rows — Dan 4:34, 4:36):** All CONFIRM. Man.da as reason — the defining inner seat of humanness. **Flag for Session D synthesis highlight** — most anthropologically significant man.da use.

**963-001 (31 G-rows):** All CONFIRM. Settled inner conviction shaping moral, spiritual, relational life. All Pauline "we know / do you not know" conviction verses.

**963-002 (4 G-rows — 1Cor 2:11, 2Cor 5:11, Rom 7:18, 8:26):** All CONFIRM. Self-knowledge of inner conflict and limitation.

**963-003 (8 G-rows — 1Cor 3:16, 6:2/3/9/15/16, Eph 1:18, Gal 4:8):** All CONFIRM. Identity-shaping knowledge of who the person is in Christ.

**963-004 (5 G-rows — 2Cor 11:11, 11:31, 9:2, Col 2:1, Rom 8:27):** All CONFIRM. God's or another's knowledge of the inner person.

**963-005 (2 G-rows — 1Cor 8:1, 13:2):** All CONFIRM. Knowledge divorced from love — hollow inner capacity. **Flag for Session D synthesis** — bridges M15-C and C17 relational-grace cluster.

**SA rows (21):** All confirmed correctly SA. All are ya.da in the sexual/physical knowing sense (Gen 4:1, 4:17, 4:25, 19:5, 19:8, 19:25, 19:33, 19:35, 24:16, 29:5, 38:16, 38:26, Num 31:17, 31:18, 31:35, Judg 11:39, 19:22, 19:25, 21:11, 21:12, 1Sa 1:19) plus Gal 1:22 agnoeō (neutral informational). All correctly SA.

**P-status rows (157):** All P confirmed as pending — no immediate action. The large ya.da P-status set includes many factual/informational uses needing individual researcher review.

---

### M15-C action summary

**MOVE actions (3 verses):**

| # | vr_id | Reference | From | To |
|---|---|---|---|---|
| 1 | 178151 | Exo 31:3 (da.at) | 1838-001 | 955-003 |
| 2 | 178196 | Psa 19:2 (da.at) | 1838-001 | 955-001 |
| 3 | 29474 | Hos 6:6 (da.at) | 1838-001 | 955-002 |

**FLAG actions (2 verses):**

| # | vr_id | Reference | Issue |
|---|---|---|---|
| 1 | 29499 | Num 24:16 (da.at) | Positive capacity; not culpable ignorance; researcher to confirm destination |
| 2 | 29766 | Num 24:16 (ya.da) | Same verse; same issue |

**CREATE-VCG (future, when P-rows processed):**

| # | Term | mti_id | Description |
|---|---|---|---|
| 1 | G0050 agnoeō | 1838 | Neutral informational unawareness — "I do not want you to be uninformed"; distinct from culpable spiritual ignorance |

**Session D HIGHLIGHTS flagged:**
- Jer 22:16 (da.at = doing justice for the poor = knowing God — defining equation)
- Isa 53:11 (da.at as instrument of the Servant's justifying work — unique)
- Dan 4:34, 4:36 (man.da = reason = defining inner seat of humanness)
- 1Cor 8:1, 13:2 (knowledge without love = hollow — bridges M15-C and C17)

**CONFIRM actions: 421 G-status verses + 21 SA confirmed**


---

## M15-D — 168 verses, 16 DB VCGs

### VCG inventory (DB state)

| VCG code | Term | DB count |
|---|---|---|
| 519-001 | H7919A sa.khal | 46 |
| 519-002 | H7919A sa.khal | 11 |
| 3335-001 | H2803H cha.shav (count/impute) | 6 |
| 3335-002 | H2803H cha.shav | 17 |
| 3336-001 | H2803J cha.shav (think) | 11 |
| 3336-002 | H2803J cha.shav | 15 |
| 1285-001 | G1252 diakrinō | 11 |
| 1285-002 | G1252 diakrinō | 7 |
| 4487-001 | H6175 a.rum | 8 |
| 4487-002 | H6175 a.rum | 2 |
| 4486-001 | H6191 a.rom | 2 |
| 4486-002 | H6191 a.rom | 3 |
| 5099-001 | H2938 ta.am | 5 |
| 5099-002 | H2938 ta.am | 5 |
| 3409-001 | G3053 logismos | 2 |
| 818-001 | G0145 aisthētērion | 1 |

**P-status: 6 · SA: 10**

---

### Per-verse actions — M15-D

#### 5099-002 — 5 rows individually addressed

| vr_id | Reference | Term | Action | Reason |
|---|---|---|---|---|
| 6926 | Gen 3:6 | H7919A sa.khal | **MOVE → 519-001** | Sa.khal = she saw the tree was to be desired to make one wise; prudent discernment applied to a fatal choice; not ta.am; misrouted |
| 208319 | Job 5:12 | H6175 a.rum | **MOVE → 4487-002** | Craftiness that God frustrates — a.rum negative/cunning; not ta.am |
| 130841 | Isa 53:3 | H2803H cha.shav | **MOVE → 3335-002** | "We esteemed him not" — evaluative regard (cha.shav H); not ta.am/taste |
| 155369 | 2Sa 3:35 | H2938 ta.am | CONFIRM | "David tasted food" — ta.am as abstaining from food as inner state; 5099-002 correct |
| 155372 | Jon 3:7 | H2938 ta.am | CONFIRM | Let neither human nor beast taste anything — ta.am as the act of abstaining; 5099-002 correct |

#### 3335-001 — 6 rows individually addressed

| vr_id | Reference | Term | Action | Reason |
|---|---|---|---|---|
| 130834 | Gen 15:6 | H2803H cha.shav | CONFIRM | He counted/imputed it to him as righteousness — divine moral imputation; 3335-001 correct |
| 130851 | Lev 7:18 | H2803H cha.shav | CONFIRM | It shall not be credited to him — imputation withheld |
| 130844 | Lev 17:4 | H2803H cha.shav | CONFIRM | Bloodguilt shall be counted against that man |
| 130859 | Psa 32:2 | H2803H cha.shav | CONFIRM | Blessed is the man against whom the Lord counts no iniquity — imputation |
| 130858 | Psa 106:31 | H2803H cha.shav | CONFIRM | It was counted to him as righteousness — parallel to Gen 15:6 |
| 130852 | Mal 3:16 | H2803H cha.shav | **MOVE → 3335-002** | "The Lord paid attention and heard; a book of remembrance was written for those who feared him and esteemed his name" — human esteeming of God's name; not divine moral imputation |

#### 3336-001 — 11 rows — Jer 23:27 addressed

| vr_id | Reference | Term | Action | Reason |
|---|---|---|---|---|
| 130872 | Jer 23:27 | H2803J cha.shav | **MOVE → M15-E 3334-001** | "Who think to make my people forget my name" — deliberate plotting against; devising harm; not self-examination |
| All other 3336-001 rows | Various | H2803J cha.shav | CONFIRM | Self-examination, forming inward judgment about oneself or another; correctly placed |

#### All remaining M15-D rows — CONFIRM

**519-001 (46 G-rows):** Sa.khal as prudent discernment producing success — all CONFIRM. Includes Gen 3:6 moving in (see above), 1Ch 28:19 already correctly here. Note: 1Ch 28:19 is correctly in M15-D — sa.khal is M15-D's term; earlier session memory suggestion to move it was based on incorrect sub-group attribution of the term.

**519-002 (11 G-rows):** Sa.khal as wisdom in action producing outcome — all CONFIRM.

**3335-002 (17 G-rows):** Evaluative regard of persons/things — all CONFIRM. Receives Isa 53:3 and Mal 3:16 from moves above.

**3336-002 (15 G-rows):** Forming inner judgment about what one sees/hears — all CONFIRM.

**1285-001 and 1285-002 (18 G-rows):** Diakrinō as discriminating judgment and inner self-division — all CONFIRM.

**4487-001/002 (10 G-rows) and 4486-001/002 (5 G-rows):** A.rum and a.rom positive and negative — all CONFIRM. Receives Job 5:12 a.rum into 4487-002.

**5099-001 (5 G-rows):** Ta.am as perceptive faculty of inner discernment — all CONFIRM.

**3409-001 (2 G-rows) and 818-001 (1 G-row):** Logismos and aisthētērion — CONFIRM.

**SA rows (10):** All confirmed correctly SA.

### M15-D action summary

**MOVE actions (4 verses):**

| # | vr_id | Reference | From | To |
|---|---|---|---|---|
| 1 | 6926 | Gen 3:6 (sa.khal) | 5099-002 | 519-001 |
| 2 | 208319 | Job 5:12 (a.rum) | 5099-002 | 4487-002 |
| 3 | 130841 | Isa 53:3 (cha.shav H) | 5099-002 | 3335-002 |
| 4 | 130852 | Mal 3:16 (cha.shav H) | 3335-001 | 3335-002 |
| 5 | 130872 | Jer 23:27 (cha.shav J) | 3336-001 | M15-E 3334-001 |

**CONFIRM: 147 G-status verses + 10 SA confirmed**

---

## M15-E — 188 verses, 21 DB VCGs

### VCG inventory (DB state) — key groups

| VCG code | Term | DB count |
|---|---|---|
| 749-001 | H3289 ya.ats (counsel given/received) | 43 |
| 749-002 | H3289 ya.ats (hostile/moral expression) | 18 |
| 749-003 | H3289 ya.ats (divine sovereign counsel) | 12 |
| 3334-001 | H2803I cha.shav (devising harm) | 26 |
| 3334-002 | H2803I cha.shav (purposive planning) | 17 |
| 509-001 | G1014 boulomai (human volitional will) | 26 |
| 509-002 | G1014 boulomai (divine purposive will) | 8 |
| 1001-001 | G1106 gnōmē (personal judgment) | 6 |
| 1001-002 | G1106 gnōmē (shared purpose) | 2 |
| 2109-001 | G1011 bouleuō (deliberate decision) | 4 |
| 2109-002 | G1011 bouleuō (deliberate harmful resolve) | 3 |
| 3578-A | H7896K shit (active attending) | 4 |
| 3578-B | H7896K shit (failure/suppression of attending) | 3 |
| 847-001 | H2161 za.mam (purposeful resolve) | 1 |
| 847-002 | H2161 za.mam (divine irresistible purposing) | 3 |
| 3280-001 | G4388 protithēmi (purposive intention) | 3 |
| 1179-001 | H2808 chesh.bon (rational faculty) | 3 |
| 754-001 | H5779 uts (communal purposing) | 2 |
| 3373-001 | G4307 pronoia (foresight/provision) | 2 |
| 3445-001 | H6245B a.shat (appeal for divine attending) | 1 |
| 3482-001 | H6246 a.shit (royal planning) | 1 |

---

### Per-verse actions — M15-E

All 188 rows are G-status. No SA, no P.

**RECEIVES moves from other sub-groups:**

| vr_id | Reference | From | Action |
|---|---|---|---|
| 54610 | 2Sa 14:14 (cha.shav G) | M15-A 1174-001 | RECEIVE INTO 3334-002 |
| 54612 | Est 8:3 (cha.shav G) | M15-A 1174-002 | RECEIVE INTO 3334-001 |
| 54613 | Est 9:25 (cha.shav G) | M15-A 1174-002 | RECEIVE INTO 3334-001 |
| 54626 | Psa 35:20 (cha.shav G) | M15-A 1174-002 | RECEIVE INTO 3334-001 |
| 130872 | Jer 23:27 (cha.shav J) | M15-D 3336-001 | RECEIVE INTO 3334-001 |

**3334-001 and 3334-002 — key verses confirmed:**

Jon 1:4 (H2803I cha.shav "threatened") — the ship threatened to break up. FLAG: this is an unusual anthropomorphising use; consider whether this verse carries inner-being content in its span. Currently in 3334-002. Researcher to review for possible SA.

All other M15-E rows: CONFIRM. All purposive-planning, counsel, boulomai, gnōmē, bouleuō, za.mam, protithēmi, chesh.bon, uts, pronoia, shit, a.shat, a.shit verses correctly placed.

**CONFIRM: all 188 G-status verses (subject to moves received above)**

### M15-E action summary

**No moves out of M15-E.** Receives 5 verses from M15-A (4) and M15-D (1).

**FLAG: Jon 1:4 (cha.shav) in 3334-002 — researcher review for SA**

---

## M15-F — 66 verses, 13 DB VCGs

### Per-verse actions

All 63 G-status rows confirmed. Key VCGs:

- **242-001 (13 G-rows):** Si.ach meditation on God's works/law — CONFIRM all
- **242-002 (5 G-rows):** Si.ach complaint/telling — CONFIRM all
- **975-001 (3 G-rows):** Si.chah all-day sustained meditation — CONFIRM all
- **896-001 (2 G-rows):** Ha.gig musing-to-groaning — CONFIRM all
- **977-001 (2 G-rows):** Ha.gut heart-meditation producing understanding — CONFIRM all
- **5883-001 (1 G-row):** Hig.ga.von — CONFIRM
- **5662-001 (1 G-row):** Se.khal contemplative attention (Dan 7:8) — CONFIRM
- **1181-001 (1 G-row):** Se.ach God declaring human thought (Amo 4:13) — CONFIRM
- **1081-001 and 1081-002 (14 G-rows):** Dialogismos evil-from-heart and disputed opinions — CONFIRM all
- **1184-001 and 1184-002 (14 G-rows):** Dialogizomai individual reasoning and communal deliberation — CONFIRM all
- **917-001 (4 G-rows):** Enthumēsis — CONFIRM all
- **3392-001 (3 G-rows):** Enthumeomai — CONFIRM all

**SA rows (3):** Judg 5:10, Job 12:8 (si.ach — no inner-being in span), Psa 92:3 (hig.ga.von = "melody") — all CONFIRM SA.

**No moves required in M15-F. All 63 G-status + 3 SA confirmed.**

---

## M15-G — 27 verses, 11 DB VCGs

### Per-verse actions

All 27 rows are G-status. All confirmed correctly placed.

| VCG | Key verses | Action |
|---|---|---|
| 960-001 (5) | 2Ch 1:10/11/12, Dan 1:4/1:17 — mad.da as knowledge in governance context | CONFIRM all |
| 960-002 (1) | Ecc 10:20 — mad.da as thought-life moral seat | CONFIRM |
| 3449-001 (6) | Dan 2:29, 2:30, 4:19, 5:6, 5:10, 7:28 — ra.yon as revelation-alarmed thoughts | CONFIRM all. Note: Dan 4:19 and 5:6 were flagged in M15-A as potentially misrouted — they are correctly in M15-G; the M15-A flag was about cha.kham rows in the same verses, not the ra.yon rows |
| 3453-001 (2) | Psa 139:2 and 139:17 — re.a as human/divine thought symmetry | CONFIRM both |
| 1178-001 (1) | Job 12:5 — ash.tut as ease-contempt | CONFIRM |
| 3442-001 (1) | Psa 146:4 — esh.to.nah as plans perishing at death | CONFIRM |
| 1188-001 (6) | 2Cor 2:11, 3:14, 4:4, 10:5, 11:3, Phili 4:7 — noēma as contested cognitive faculty | CONFIRM all |
| 2493-001 (1) | 1Cor 14:20 — frēn as maturity-faculty | CONFIRM |
| 3372-001 (2) | Heb 4:12 and 1Pe 4:1 — ennoia as heart's thoughts and way-of-thinking | CONFIRM both |
| 3375-001 (1) | Act 8:22 — epinoia requiring repentance | CONFIRM |
| 3408-001 (1) | Luk 11:17 — dianoēma as thoughts known to Jesus | CONFIRM |

**No moves required in M15-G. All 27 G-status confirmed.**

---

## BOUNDARY — 77 verses, 12 DB VCGs

### Per-verse actions

**SA rows (20):** All logos (G3056) SA rows in BOUNDARY confirmed correctly SA. These are Paul's uses of logos in external speech/word sense with no inner-being content.

**NR rows (2):** Act 23:15 and Act 24:22 (diaginōskō — legal determination). CONFIRM NR.

**P-status rows (16):** All logos P-rows (Rom 3:4, 14:12, 15:18, 1Cor 1:5, 1:17, 4:20, 12:8, 14:9, 14:11, 14:36, 14:38, 15:2, 15:54, 2Cor 10:10, 10:11, 11:6) and Luk 12:14 (meristēs), Act 13:8 (methermēneuō) — CONFIRM P pending researcher review.

**G-status rows (39 rows):**

| VCG | Rows | Action |
|---|---|---|
| 1080-001 (13) | Dialegō reasoned discourse — all CONFIRM |
| 1171-001 (9) | Logos as inner-dwelling/conscience-addressing word — CONFIRM all G-status rows |
| 7419-001 (3) | Gumnazō bi-directional habituation toward godliness — CONFIRM |
| 7419-002 (1) | Gumnazō toward vice — CONFIRM |
| 454-001 (3) | Suneidō as two registers of conscious faculty — CONFIRM |
| 7333-001 (2) | Eikō simile characterising inner states — CONFIRM |
| 7085-001 (2) | Diabebaioō outward insistence — CONFIRM |
| 5864-001 (2) | Hermēneia and interpretation enabling inner reception — CONFIRM |
| 973-001 (1) | Methermēneuō name-revealing translation — CONFIRM G-row |
| 6256-001 (1) | Tir.gal tender unrecognised nurture — CONFIRM |
| 6085-001 (1) | Pe.sher interpretive wisdom — CONFIRM |
| 5865-001 (1) | Diermēneutēs interpreter absent — CONFIRM |

**No moves required in BOUNDARY. All 39 G-status + 20 SA + 2 NR confirmed.**

---

## Complete action summary — all sub-groups

### All MOVE actions across M15

| # | vr_id | Reference | Term | From | To |
|---|---|---|---|---|---|
| 1 | 54622 | Exo 36:8 | H2803G cha.shav | 4458-001 | 528-004 |
| 2 | 54608 | 2Ch 2:14 | H2803G cha.shav | 4458-001 | 528-004 |
| 3 | 54610 | 2Sa 14:14 | H2803G cha.shav | 1174-001 | M15-E 3334-002 |
| 4 | 54612 | Est 8:3 | H2803G cha.shav | 1174-002 | M15-E 3334-001 |
| 5 | 54613 | Est 9:25 | H2803G cha.shav | 1174-002 | M15-E 3334-001 |
| 6 | 54626 | Psa 35:20 | H2803G cha.shav | 1174-002 | M15-E 3334-001 |
| 7 | 7343 | 1Ki 2:9 | H2450 cha.kham | 4458-001 | 528-005 |
| 8 | 7458 | Mat 11:19 | G4678 sofia | 6696-001 | 532-003 |
| 9 | 7464 | Luk 7:35 | G4678 sofia | 6696-001 | 532-003 |
| 10 | 208338 | 1Cor 3:10 | G4680 sofos | 4458-001 | 532-003 |
| 11 | 7499 | Jam 3:13 | G4678 sofia | 4458-001 | 532-003 |
| 12 | 208344 | Jam 3:13 | G4680 sofos | 4458-001 | 532-003 |
| 13 | 7454 | 2Ti 3:15 | G4679 sofizo | 4458-001 | CREATE sofizo-positive |
| 14 | 7455 | 2Pe 1:16 | G4679 sofizo | 4458-001 | CREATE sofizo-negative |
| 15 | 27692 | Dan 11:30 | H0995 bin | 932-004 | 932-001 or CREATE directional-attending |
| 16 | 27694 | Dan 11:37 | H0995 bin | 932-004 | 932-001 or CREATE directional-attending |
| 17 | 7137 | Eze 28:4 | H8394 te.vu.nah | 524-002 | CREATE te.vu.nah non-sacred |
| 18 | 7138 | Hos 13:2 | H8394 te.vu.nah | 524-002 | CREATE te.vu.nah non-sacred |
| 19 | 178151 | Exo 31:3 | H1847 da.at | 1838-001 | 955-003 |
| 20 | 178196 | Psa 19:2 | H1847 da.at | 1838-001 | 955-001 |
| 21 | 29474 | Hos 6:6 | H1847 da.at | 1838-001 | 955-002 |
| 22 | 6926 | Gen 3:6 | H7919A sa.khal | 5099-002 | 519-001 |
| 23 | 208319 | Job 5:12 | H6175 a.rum | 5099-002 | 4487-002 |
| 24 | 130841 | Isa 53:3 | H2803H cha.shav | 5099-002 | 3335-002 |
| 25 | 130852 | Mal 3:16 | H2803H cha.shav | 3335-001 | 3335-002 |
| 26 | 130872 | Jer 23:27 | H2803J cha.shav | 3336-001 | 3334-001 |

**Total: 26 verse moves**

### All CREATE-VCG actions

| # | Sub-group | mti_id | Term | Description |
|---|---|---|---|---|
| 1 | M15-A | 530 | G4679 sofizo | Scripture making wise for salvation — positive transformative use |
| 2 | M15-A | 530 | G4679 sofizo | Cleverly devised myths — negative fabrication |
| 3 | M15-B | 932 | H0995 bin | Directional attending — perceptive attention directed toward/withdrawn from an object |
| 4 | M15-B | 524 | H8394 te.vu.nah | Te.vu.nah in self-serving or non-sacred application |
| 5 | M15-C | 1838 | G0050 agnoeō | Neutral informational unawareness (future — when P-rows processed) |

### All UPDATE-DESC actions

| # | VCG | Required change |
|---|---|---|
| 1 | 528-004 | Widen description to include secular craft uses alongside Spirit-given sacred craft |
| 2 | 6696-001 | Tighten to strictly divine-attribute uses after removing Luk 7:35 and Mat 11:19 |
| 3 | 4458-001 | Remove sofizo (2Ti 3:15 and 2Pe 1:16) from scope |
| 4 | 524-002 | Update after removing Eze 28:4 and Hos 13:2 |
| 5 | 1838-001 | Note split pending; culpable spiritual ignorance confirmed for 7 G-status rows |

### All FLAGS

| # | vr_id | Reference | Issue |
|---|---|---|---|
| 1 | 7315 | Job 30:22 | tu.shiy.yah "toss" — disputed translation; confirm in 527-001 |
| 2 | (Dan 11:30/37) | Dan 11:30, 11:37 | Directional attending — moved, but VCG decision for researcher |
| 3 | 29499/29766 | Num 24:16 | Positive da.at capacity; misrouted to 1838-001; researcher to confirm destination |
| 4 | (Isa 10:13) | Isa 10:13 | Self-attributed bin in 932-004; consider moving to 932-001 |
| 5 | (1838-001 P-rows) | Multiple agnoeō | Neutral informational uses; split needed when P-rows processed |
| 6 | (528-004 secular) | Isa 40:20, Jer 10:9, Eze 27:8/9, Amo 6:5 | Secular craft in 528-004; confirm pending description update |
| 7 | (Jon 1:4) | Jon 1:4 | Anthropomorphising storm in 3334-002; consider SA |
| 8 | (Psa 73:17, Jer 2:10) | Multiple bin | Successful perception/active attention in 932-004; loose fit |
| 9 | (Pro 3:19 te.vu.nah) | Pro 3:19 | Divine attribute in 524-002; should be 524-001 |

---

*End of M15 alignment action list. All 1,028 G+SA+NR verses addressed. 26 verse moves. 5 new VCGs. 5 description updates. 9 flags.*
*Next step: compile 26 verse moves and 5 new VCG definitions into a directive for Claude Code.*
