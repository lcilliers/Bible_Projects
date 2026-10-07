# M64 pinpointed pull and reading: "to choose" (H0977 with G0830, H7148, G0140, G4401; v2 adds H0972, G0138, G1586, G1588, G1589)

**Date:** 2026-10-07 · **Escalation:** #1978 · **Status:** reading summary for the researcher. Nothing is woven into the narrative.

**Version 3.** Every verse is now routed (§8), and the verses for Ch 13 "Other beings" are isolated. The researcher asked, verbatim: *"proceed to revise the choose reading work to isolate all the verses that will be captured in Ch13"*. The rule followed is `cfg_behaviour_rule` 72 (GOVERNANCE.md §90). §1–§7 are unchanged from v2.

**Version 2.** v1 is archived. The researcher asked, verbatim: *"pull H0972 and G0138,G1586,G1588, and G1589 next with the same script and add it to the csv files and md"*.
- The 63 new verses are written into the sections they belong to, not kept as an appendix.
- Three groups are new: Jesus chooses; the chosen / the elect (NT); God chooses the foolish, weak, low and poor.
- Three groups are widened: men selected for a task; choosing between death and life; places of honour.

**Sources:**
- the verses: [`m64-choose-verses-v2-20261007.csv`](m64-choose-verses-v2-20261007.csv). This is the pull: ESV text, the hits, the other M-cluster words in the verse, and the narrative citations.
- the pull script: [`m64-choose-verses-pull-v2-20261007.py`](m64-choose-verses-pull-v2-20261007.py). It is read-only against iba.db and takes any list of Strong's.
  - v2 reads one-chapter references (stored as "2Jo 13") as chapter 1 for the narrative lookup.
- the placement and routing of every verse: [`m64-choose-reading-v3-20261007.csv`](m64-choose-reading-v3-20261007.csv). It has the columns `route`, `ch13_sections`, `route_basis` and `flag`. It is made in two steps:
  - [`m64-choose-reading-placement-v2-20261007.py`](m64-choose-reading-placement-v2-20261007.py) places each verse in a group (output now in `archive/`)
  - [`m64-choose-routing-v1-20261007.py`](m64-choose-routing-v1-20261007.py) routes it. It reads the placement, makes no DB query (rule 71), and asserts that every verse it names is in the pull.

## 1. Scale

| Strong's | Gloss | Cluster | Verses | Rows | Form |
| --- | --- | --- | --- | --- | --- |
| H0977 *bāḥar* | to choose | M64 | 164 | 171 | Qal 164, Niphal 7 |
| H0972 *bāḥîr* | chosen (one) | M64 | 13 | 13 | adjective, as a name: "my chosen", "his chosen ones" |
| H7148 *qārîʾ* | chosen (called, summoned) | M64 | 2 | 2 | adjective |
| G1586 *eklegomai* | to choose, select | T3 | 19 | 22 | verb, middle |
| G1588 *eklektos* | chosen, elect | T2 | 21 | 21 | adjective, often as a name: "the elect" |
| G1589 *eklogē* | choosing, election | T2 | 7 | 7 | noun |
| G0138 *haireomai* | to choose | M64 | 3 | 3 | verb, middle |
| G0140 *hairetizō* | to choose | M64 | 1 | 1 | aorist |
| G4401 *procheirotoneō* | to choose (beforehand) | M64 | 1 | 1 | perfect passive participle |
| G0830 *authairetos* | self-chosen | M64 | 2 | 2 | adjective, rendered "of (his/their) own accord" |

- **232 verses, 243 rows.** Eleven verses carry two hits:
  - 2Sa 10:9 and 1Ch 19:10: "chose … the best"
  - 1Ki 8:16, 2Ch 6:5 and 2Ch 6:6: a city and a man
  - 1Ch 28:4: "me" and "Judah"
  - 2Ch 13:3: both armies
  - Isa 66:4: God's choosing and theirs
  - Mar 13:20: "the elect, whom he chose"
  - Joh 15:16: "You did not choose me, but I chose you"
  - 1Cor 1:27: "God chose … God chose"
  - None of the five new words shares a verse with the first five.
- **Who chooses:**
  - God, the Lord or Jesus: **157 verses**. This includes the 26 verses on "the elect / chosen", which are God's ("God's elect", Rom 8:33).
  - people: **75 verses**
- **Narrative:** 10 verses are cited.
  - Deu 30:19 in Ch 2 and 10.7
  - Job 7:15 and Jer 8:3 in Ch 2 ("Wanting to die")
  - Pro 1:29 in 10.2
  - Isa 66:4 in 10.12
  - Act 10:41 in Ch 2
  - new in v2:
    - Psa 106:23 in 10.13 ("Pleading, and standing in the breach")
    - Isa 42:1 in Ch 9
    - Luk 10:42 in 10.1 ("What anxiety does")
    - Phili 1:22 in Ch 7
  - The other 222 are uncited. 10.7 *Choosing and setting direction* carries only Deu 30:19 from these words.
- **M47 words in the same verse:** 19 verses (§4).

## 2. The groups (every verse placed)

The groups go by **who chooses and what is chosen, as the verse states it**. They sort the verses. They are not a scheme that the verses state. "v1" is the count before the five new words were added.

| Group | Verses | v1 |
| --- | --- | --- |
| God chooses a place for his name | 44 | 44 |
| God chooses a person for a task or office | 40 | 29 |
| God chooses a people | 29 | 19 |
| The chosen / the elect (NT) | 26 | new |
| Men selected (for battle, leadership or a task) | 24 | 21 |
| A person chooses the Lord, life, his ways, the good | 13 | 11 |
| A person chooses other gods, their own ways, what God does not delight in | 11 | 11 |
| A person's own decision, desire or accord | 8 | 8 |
| Jesus chooses | 6 | new |
| God chooses what he wants (a fast, a response, whom he appoints) | 6 | 6 |
| A thing or place chosen for oneself (by sight, use or honour) | 6 | 5 |
| "Choice": the best, preferred over | 6 | 6 |
| A person chooses a king or takes a side | 4 | 4 |
| God chooses the foolish, weak, low and poor | 3 | new |
| A person chooses between death and life | 3 | 2 |
| God sets a choice before a person | 2 | 2 |
| God tries (ESV "tried") | 1 | 1 |

## 3. What choosing is and does, from the verses

### 3.1 God chooses: a place, so that his name dwells there (44)

The phrase repeats through Deuteronomy: "the place that the Lord your God will choose, to make his name dwell there" (Deu 12:11; also 14:23, 16:2, 16:6, 16:11, 26:2).

- **Kings and Chronicles narrow it:**
  - from "I chose no city out of all the tribes of Israel" (1Ki 8:16, 2Ch 6:5)
  - to "I have chosen Jerusalem that my name may be there" (2Ch 6:6)
- **The choice carries God's own presence and attention:** "For now I have chosen and consecrated this house that my name may be there forever. My eyes and my heart will be there for all time" (2Ch 7:16).
- **People's acts are directed to the chosen place:**
  - worship, eating, rejoicing: "you shall rejoice before the Lord your God … at the place that the Lord your God will choose" (Deu 16:11)
  - judgement: Deu 17:8, 17:10
  - reading the law: Deu 31:11
  - prayer in repentance: "if they repent with all their heart and with all their soul … and pray to you toward … the city that you have chosen" (1Ki 8:48; 2Ch 6:38)
- **Learning is stated as a purpose:** "that you may learn to fear the Lord your God always" (Deu 14:23).
- **The chosen city can be cast off, and chosen again:**
  - "I will cast off this city that I have chosen, Jerusalem" (2Ki 23:27)
  - "the Lord will again comfort Zion and again choose Jerusalem" (Zec 1:17; also Zec 2:12)
  - The choice is named against an accuser: "The Lord who has chosen Jerusalem rebuke you!" (Zec 3:2)

### 3.2 God chooses a people (29)

- **The verses give love as the ground, and deny number as the ground:**
  - "because he loved your fathers and chose their offspring after them" (Deu 4:37)
  - "It was not because you were more in number … that the Lord set his love on you and chose you, for you were the fewest of all peoples" (Deu 7:7)
  - "the Lord set his heart in love on your fathers and chose their offspring" (Deu 10:15)
  - "Mount Zion, which he loves" (Psa 78:68)
  - "the pride of Jacob whom he loves" (Psa 47:4)
- **What the choosing makes them:**
  - "a people for his treasured possession" (Deu 7:6, 14:2)
  - "his heritage" (Psa 33:12)
  - "his own possession" (Psa 135:4)
- **"Chosen" becomes their name (H0972):**
  - "O offspring of Israel his servant, children of Jacob, his chosen ones!" (1Ch 16:13; Psa 105:6)
  - "So he brought his people out with joy, his chosen ones with singing" (Psa 105:43)
  - "that I may look upon the prosperity of your chosen ones, that I may rejoice in the gladness of your nation" (Psa 106:5)
  - "to give drink to my chosen people" (Isa 43:20)
- **Purpose:**
  - "my servant whom I have chosen, that you may know and believe me and understand that I am he" (Isa 43:10)
  - Cyrus is called "For the sake of my servant Jacob, and Israel my chosen … though you do not know me" (Isa 45:4).
- **What the chosen will have:**
  - "my chosen shall possess it, and my servants shall dwell there" (Isa 65:9)
  - "my chosen shall long enjoy the work of their hands" (Isa 65:22)
  - against those who "shall leave your name to my chosen for a curse" (Isa 65:15)
- **The verses pair the choosing with not casting off, with comfort, and with help:**
  - "I have chosen you and not cast you off" (Isa 41:9)
  - "Fear not, O Jacob my servant, Jeshurun whom I have chosen" (Isa 44:2)
  - "the Lord will have compassion on Jacob and will again choose Israel" (Isa 14:1)
- **Rejection stands beside choosing:**
  - "He rejected the tent of Joseph; he did not choose the tribe of Ephraim, but he chose the tribe of Judah" (Psa 78:67–68)
  - Others can say the choice has been withdrawn: "The Lord has rejected the two clans that he chose" (Jer 33:24).
- **God's choosing is linked to his oath:** "On the day when I chose Israel, I swore to the offspring of the house of Jacob" (Eze 20:5).
- **Retold in the NT:** "The God of this people Israel chose our fathers and made the people great" (Act 13:17).

### 3.3 The chosen, the elect (NT, 26)

The NT speaks of a body of people called "the elect" or "chosen", and says what God's choosing of them is.

- **Its ground, as the verses state it:**
  - "chose us in him before the foundation of the world, that we should be holy and blameless before him" (Eph 1:4)
  - "in order that God's purpose of election might continue, not because of works but because of him who calls" (Rom 9:11; said of the twins "not yet born")
  - "a remnant, chosen by grace" (Rom 11:5)
  - "brothers loved by God, that he has chosen you" (1Th 1:4)
  - "God chose you as the firstfruits to be saved, through sanctification by the Spirit and belief in the truth" (2Th 2:13, G0138)
- **What it makes them:**
  - "a chosen race, a royal priesthood, a holy nation, a people for his own possession, that you may proclaim the excellencies of him who called you" (1Pe 2:9). This is near the wording of Deu 7:6.
  - "Put on then, as God's chosen ones, holy and beloved, compassionate hearts, kindness, humility, meekness, and patience" (Col 3:12). Being chosen is followed by what to put on.
- **Called and chosen are not the same:**
  - "For many are called, but few are chosen" (Mat 22:14)
  - "those with him are called and chosen and faithful" (Rev 17:14)
  - The person's part: "be all the more diligent to confirm your calling and election, for if you practice these qualities you will never fall" (2Pe 1:10).
- **God's care for the elect:**
  - "for the sake of the elect, whom he chose, he shortened the days" (Mar 13:20; Mat 24:22)
  - The elect are a target: false christs arise "to lead astray, if possible, even the elect" (Mat 24:24; Mar 13:22).
  - The elect are gathered: "they will gather his elect from the four winds" (Mat 24:31; Mar 13:27).
  - "will not God give justice to his elect, who cry to him day and night?" (Luk 18:7)
  - "Who shall bring any charge against God's elect? It is God who justifies" (Rom 8:33)
- **Others work for the elect:**
  - "Therefore I endure everything for the sake of the elect, that they also may obtain the salvation" (2Ti 2:10)
  - "for the sake of the faith of God's elect and their knowledge of the truth" (Tit 1:1)
- **Israel and election:**
  - "Israel failed to obtain what it was seeking. The elect obtained it, but the rest were hardened" (Rom 11:7)
  - "as regards election, they are beloved for the sake of their forefathers" (Rom 11:28)
- **Persons named so:**
  - "Rufus, chosen in the Lord" (Rom 16:13)
  - "the elect lady" (2Jo 1) and "your elect sister" (2Jo 13)
  - "the elect angels" (1Ti 5:21)

### 3.4 God chooses the foolish, weak, low and poor (3)

- "God chose what is foolish in the world to shame the wise; God chose what is weak in the world to shame the strong" (1Cor 1:27)
- "God chose what is low and despised in the world, even things that are not, to bring to nothing things that are" (1Cor 1:28)
- "has not God chosen those who are poor in the world to be rich in faith and heirs of the kingdom, which he has promised to those who love him?" (Jam 2:5)
- The verses give purposes: "to shame", "to bring to nothing", "to be rich in faith".
- This stands beside "not because you were more in number" (Deu 7:7, §3.2).

### 3.5 God chooses a person for a task or office (40)

- **Priesthood and Levites:**
  - "the Lord your God has chosen him … to stand and minister in the name of the Lord" (Deu 18:5)
  - also Deu 21:5, 1Ch 15:2, 2Ch 29:11
  - Choosing goes with bringing near: "The one whom he chooses he will bring near to him" (Num 16:5); "Blessed is the one you choose and bring near, to dwell in your courts!" (Psa 65:4).
  - The choice is shown, not argued: "the staff of the man whom I choose shall sprout" (Num 17:5).
- **King:**
  - "a king over you whom the Lord your God will choose" (Deu 17:15)
  - Samuel's sons of Jesse are passed over one by one: "Neither has the Lord chosen this one" (1Sa 16:8, 16:9, 16:10). Verse 7, about the heart, lies outside the pull.
  - David: "who chose me above your father … to appoint me as prince over Israel, the people of the Lord —and I will celebrate before the Lord" (2Sa 6:21)
  - "He chose David his servant and took him from the sheepfolds" (Psa 78:70)
  - "I have made a covenant with my chosen one; I have sworn to David my servant" (Psa 89:3)
  - Solomon "whom alone God has chosen, is young and inexperienced, and the work is great" (1Ch 29:1). Being chosen is followed by a charge: "the Lord has chosen you to build a house for the sanctuary; be strong and do it" (1Ch 28:10).
  - Sonship: "I have chosen him to be my son, and I will be his father" (1Ch 28:6)
  - Saul is named "the chosen of the Lord" by the Gibeonites, in the demand for his sons (2Sa 21:6).
- **The chosen one stands between:** "had not Moses, his chosen one, stood in the breach before him, to turn away his wrath from destroying them" (Psa 106:23). **This is an OT-62 verse (anger face 2J).**
- **Others:**
  - Abram (Neh 9:7)
  - Moses and Aaron (Psa 105:26)
  - Zerubbabel, "like a signet ring, for I have chosen you" (Hag 2:23)
  - the despised one whom kings will bow to, "because of the Lord, who is faithful … who has chosen you" (Isa 49:7)
- **The servant:** "Behold my servant, whom I uphold, my chosen, in whom my soul delights; I have put my Spirit upon him" (Isa 42:1). Mat 12:18 carries the same words with G0140: "my servant whom I have chosen, my beloved with whom my soul is well pleased. I will put my Spirit upon him".
- **The Son:**
  - from the cloud: "This is my Son, my Chosen One; listen to him!" (Luk 9:35)
  - mocked at the cross: "let him save himself, if he is the Christ of God, his Chosen One!" (Luk 23:35)
  - "a living stone rejected by men but in the sight of God chosen and precious" (1Pe 2:4)
  - "a cornerstone chosen and precious, and whoever believes in him will not be put to shame" (1Pe 2:6)
  - Chosen by God and rejected by men are stated together.
- **Apostles and witnesses:**
  - "us who had been chosen by God as witnesses" (Act 10:41, *beforehand*)
  - "You, Lord, who know the hearts of all, show which one of these two you have chosen" (Act 1:24). They pray to know a choice already made.
  - Paul: "he is a chosen instrument of mine to carry my name before the Gentiles and kings and the children of Israel" (Act 9:15)
  - Peter: "God made a choice among you, that by my mouth the Gentiles should hear the word of the gospel and believe" (Act 15:7)

### 3.6 Jesus chooses (6)

- "he called his disciples and chose from them twelve, whom he named apostles" (Luk 6:13)
- "the apostles whom he had chosen" (Act 1:2), given commands "through the Holy Spirit"
- **The one who chooses initiates:** "You did not choose me, but I chose you and appointed you that you should go and bear fruit and that your fruit should abide" (Joh 15:16)
- **Chosen out of, and hated for it:** "I chose you out of the world, therefore the world hates you" (Joh 15:19)
- **Chosen, and still one betrays:**
  - "Did I not choose you, the twelve? And yet one of you is a devil" (Joh 6:70)
  - "I know whom I have chosen. But the Scripture will be fulfilled, 'He who ate my bread has lifted his heel against me'" (Joh 13:18)

### 3.7 God chooses what he wants (6)

- **A fast:** "Is not this the fast that I choose: to loose the bonds of wickedness … to let the oppressed go free" (Isa 58:6), against a fast of bowing the head (Isa 58:5).
- **A response that answers their choice:** "I also will choose harsh treatment for them … because when I called, no one answered … and chose that in which I did not delight" (Isa 66:4). The same word is used for God's choosing and theirs.
- **What is "more acceptable":** "To do righteousness and justice is more acceptable to the Lord than sacrifice" (Pro 21:3, Niphal).
- **Appointing:** "I will appoint over her whomever I choose. For who is like me?" (Jer 49:19; Jer 50:44).

### 3.8 God sets a choice before a person (2), and a person chooses (13 + 11 + 3)

- **God offers the choice:** "Three things I offer you. Choose one of them, that I may do it to you" (2Sa 24:12; 1Ch 21:10).
- **Choosing life, the Lord, his ways:**
  - "I have set before you life and death … Therefore choose life" (Deu 30:19)
  - "choose this day whom you will serve" (Jos 24:15); the choice is then witnessed: "You are witnesses against yourselves that you have chosen the Lord" (Jos 24:22)
  - "I have chosen the way of faithfulness; I set your rules before me" (Psa 119:30)
  - "for I have chosen your precepts" (Psa 119:173)
  - "who choose the things that please me and hold fast my covenant" (Isa 56:4)
  - Preference is stated:
    - "I would rather be a doorkeeper in the house of my God than dwell in the tents of wickedness" (Psa 84:10)
    - Moses: "choosing rather to be mistreated with the people of God than to enjoy the fleeting pleasures of sin" (Heb 11:25, G0138)
  - "Mary has chosen the good portion, which will not be taken away from her" (Luk 10:42), set against her sister's anxiety (narrative 10.1).
- **Choosing needs knowing and instruction:**
  - "when he knows how to refuse the evil and choose the good" (Isa 7:15, 7:16)
  - "Who is the man who fears the Lord? Him will he instruct in the way that he should choose" (Psa 25:12)
  - It can be done together: "Let us choose what is right; let us know among ourselves what is good" (Job 34:4).
- **Choosing against:**
  - "they hated knowledge and did not choose the fear of the Lord" (Pro 1:29)
  - "Do not envy a man of violence and do not choose any of his ways" (Pro 3:31)
  - "your iniquity teaches your mouth, and you choose the tongue of the crafty" (Job 15:5)
  - "do not turn to iniquity, for this you have chosen rather than affliction" (Job 36:21)
  - "These have chosen their own ways, and their soul delights in their abominations" (Isa 66:3)
  - "when I called, you did not answer … and chose what I did not delight in" (Isa 65:12)
  - Gods: "When new gods were chosen, then war was in the gates" (Judg 5:8); "Go and cry out to the gods whom you have chosen; let them save you" (Judg 10:14)
  - The idol and its chooser: "an abomination is he who chooses you" (Isa 41:24); the maker "chooses wood that will not rot" (Isa 40:20)
  - Shame follows: "you shall blush for the gardens that you have chosen" (Isa 1:29)
- **Choosing between death and life:**
  - "so that I would choose strangling and death rather than my bones" (Job 7:15; the M47 tag on "I" is *nephesh*)
  - "Death shall be preferred to life by all the remnant" (Jer 8:3)
  - Paul: "If I am to live in the flesh, that means fruitful labor for me. Yet which I shall choose I cannot tell" (Phili 1:22, G0138)
  - All three stand against "choose life" (Deu 30:19). In Job and Jeremiah death is preferred out of suffering. In Philippians the choice is held open, with no answer given.

### 3.9 Choosing a king or a side (4)

- "your king, whom you have chosen for yourselves, but the Lord will not answer you in that day" (1Sa 8:18)
- "behold the king whom you have chosen, for whom you have asked; behold, the Lord has set a king over you" (1Sa 12:13). Both the people's choosing and the Lord's setting are stated.
- Loyalty: "whom the Lord and this people and all the men of Israel have chosen, his I will be, and with him I will remain" (2Sa 16:18).
- Choosing a friend draws anger: "Saul's anger was kindled against Jonathan … do I not know that you have chosen the son of Jesse to your own shame" (1Sa 20:30). **This is an OT-62 verse (anger face 3O).**

### 3.10 One's own decision, desire, accord (8)

- **The word is rendered as decision and desire:**
  - "whatever my lord the king decides" (2Sa 15:15)
  - "all that you desire of me I will do for you" (2Sa 19:38)
- **The choice is placed on the person:** "For you must choose, and not I" (Job 34:33).
- **Choosing words before God:** "How then can I answer him, choosing my words with him?" (Job 9:14).
- **Choosing a way for others:** "I chose their way and sat as chief" (Job 29:25).
- **The escaped slave:** "in the place that he shall choose within one of your towns, wherever it suits him" (Deu 23:16).
- **G0830, of one's own accord:**
  - "they gave according to their means, as I can testify, and beyond their means, of their own accord" (2Cor 8:3)
  - "being himself very earnest he is going to you of his own accord" (2Cor 8:17)

### 3.11 Selecting by quality, sight, use or honour (24 + 6 + 6)

- **"Chosen men":**
  - the passive participle as a mark of fitness: "300,000 choice men, fit for war, able to handle spear and shield" (2Ch 25:5)
  - "700 chosen men who were left-handed; every one could sling a stone at a hair and not miss" (Judg 20:16)
  - leaders: "Moses chose able men out of all Israel and made them heads" (Exo 18:25)
  - H7148: "chosen from the assembly, well-known men" (Num 16:2; Num 26:9), the men who contended against Moses and Aaron
- **The church selects men for a task:**
  - "what they said pleased the whole gathering, and they chose Stephen, a man full of faith and of the Holy Spirit" (Act 6:5)
  - "it seemed good to the apostles and the elders, with the whole church, to choose men from among them" (Act 15:22)
  - "having come to one accord, to choose men" (Act 15:25)
  - The verses state the choosing as agreed together.
- **By sight:**
  - "the sons of God saw that the daughters of man were attractive. And they took as their wives any they chose" (Gen 6:2)
  - "Lot chose for himself all the Jordan Valley … Thus they separated from each other" (Gen 13:11)
  - David "chose five smooth stones from the brook" (1Sa 17:40)
  - the contest bulls (1Ki 18:23, 18:25)
- **For honour:** "he noticed how they chose the places of honor" (Luk 14:7). The parable that follows lies outside the pull.
- **"Choice" as value preferred over another:**
  - "To get understanding is to be chosen rather than silver" (Pro 16:16)
  - "A good name is to be chosen rather than great riches" (Pro 22:1)
  - "The tongue of the righteous is choice silver; the heart of the wicked is of little worth" (Pro 10:20)
  - also Pro 8:10, 8:19, Song 5:15

### 3.12 One verse apart

"Behold, I have refined you, but not as silver; I have tried you in the furnace of affliction" (Isa 48:10). The ESV renders H0977 here as "tried". It is the only verse in the pull where the word is rendered as testing.

## 4. Inner-being words in the same verse (M47, 19 verses)

| Verse | M47 word | What the verse says |
| --- | --- | --- |
| 2Ch 7:16 | heart (God's) | "My eyes and my heart will be there for all time" |
| 1Ki 8:48; 2Ch 6:38 | heart, soul | repenting "with all their heart and with all their soul" and praying toward the chosen city |
| Isa 66:3 | soul | "chosen their own ways, and their soul delights in their abominations" |
| Job 7:15 | soul ("I") | "I would choose strangling and death rather than my bones" |
| Pro 10:20 | heart | choice silver of the righteous tongue; "the heart of the wicked is of little worth" |
| Isa 58:5 | soul ("himself") | the fast God does not choose: "a day for a person to humble himself" |
| Isa 49:7 | soul ("one") | "one deeply despised" whom the Lord "has chosen" |
| Deu 12:21; Deu 18:6 | soul (appetite) | "whenever you desire"; the Levite who comes "when he desires" |
| Mat 12:18 | soul (God's), Spirit | "with whom my soul is well pleased. I will put my Spirit upon him" |
| Isa 42:1 | soul (God's), Spirit | "my chosen, in whom my soul delights; I have put my Spirit upon him" |
| Act 1:24 | heart-knower | "You, Lord, who know the hearts of all, show which one of these two you have chosen" |
| Act 1:2; Act 6:5 | Spirit | commands "through the Holy Spirit" to the chosen apostles; Stephen "full of faith and of the Holy Spirit" |
| 2Th 2:13 | Spirit | "chose you … through sanctification by the Spirit and belief in the truth" |
| Mat 24:22; Mar 13:20 | flesh ("human being") | "no human being would be saved. But for the sake of the elect" |
| Phili 1:22 | flesh | "If I am to live in the flesh … which I shall choose I cannot tell" |

## 5. Faces of choosing: where the character changes (#1919)

Each row is the verses' own wording. No mechanism is added. The rows marked v2 are new.

| Face | Who | Circumstance in the verses | Verses |
| --- | --- | --- | --- |
| Choosing out of love, not for number | God | "set his love on you and chose you, for you were the fewest" | Deu 4:37, 7:7, 10:15 |
| Choosing the low to shame the strong (v2) | God | "chose what is weak in the world to shame the strong"; "chosen those who are poor" | 1Cor 1:27–28, Jam 2:5 |
| Choosing before birth, not by works (v2) | God | "not yet born … not because of works but because of him who calls"; "before the foundation of the world" | Rom 9:11, Eph 1:4 |
| Choosing by grace (v2) | God | "a remnant, chosen by grace" | Rom 11:5 |
| Choosing to dwell, to put a name | God | "to make his name dwell there"; "my eyes and my heart will be there" | Deu 12–16, 2Ch 7:16 |
| Choosing that brings near | God | "whom he chooses he will bring near to him" | Num 16:5, Psa 65:4 |
| Choosing that charges with a task | God, Jesus | "has chosen you to build … be strong and do it"; "chose you and appointed you that you should go and bear fruit" | 1Ch 28:10, Deu 18:5, Joh 15:16 |
| Chosen as a name (v2) | God | "his chosen ones"; "my chosen"; "the elect" | Psa 105:6, Isa 65:9, Rom 8:33 |
| Chosen and then told how to live (v2) | God, then the person | "Put on then, as God's chosen ones … compassionate hearts"; "confirm your calling and election" | Col 3:12, 2Pe 1:10 |
| Called is not chosen (v2) | God | "many are called, but few are chosen" | Mat 22:14, Rev 17:14 |
| Chosen and still betraying (v2) | Jesus | "Did I not choose you, the twelve? And yet one of you is a devil" | Joh 6:70, 13:18 |
| Chosen by God, rejected or hated by men (v2) | God, Jesus | "rejected by men but in the sight of God chosen"; "I chose you out of the world, therefore the world hates you"; scoffed "his Chosen One" | 1Pe 2:4, Joh 15:19, Luk 23:35 |
| The chosen one stands between (v2) | God's chosen | "Moses, his chosen one, stood in the breach" | Psa 106:23 |
| Choosing that is guarded (v2) | God | "for the sake of the elect … he shortened the days"; "Who shall bring any charge against God's elect?" | Mar 13:20, Rom 8:33 |
| Choosing withdrawn, and renewed | God | "cast off this city that I have chosen"; "again choose Jerusalem" | 2Ki 23:27, Zec 1:17, Isa 14:1 |
| Choosing that answers a choice | God | "I also will choose … because … they chose" | Isa 66:4 |
| Choosing asked for in prayer (v2) | people, of God | "who know the hearts of all, show which one … you have chosen" | Act 1:24 |
| Choice set before a person | God, then the person | "I have set before you … choose life"; "Three things I offer you" | Deu 30:19, 2Sa 24:12 |
| Choosing that needs knowing | person | "knows how to refuse the evil and choose the good"; "him will he instruct in the way" | Isa 7:15, Psa 25:12 |
| Choosing that is witnessed and binding | person | "witnesses against yourselves that you have chosen the Lord" | Jos 24:22 |
| Choosing together, as it seems good (v2) | the church | "pleased the whole gathering"; "it seemed good … having come to one accord" | Act 6:5, 15:22, 15:25 |
| Choosing taught by iniquity, or under envy | person | "iniquity teaches your mouth, and you choose"; "do not envy … do not choose" | Job 15:5, Pro 3:31 |
| Choosing with the soul's delight | person | "chosen their own ways, and their soul delights" | Isa 66:3 |
| Choosing death in suffering | person | "I would choose strangling and death"; "death shall be preferred" | Job 7:15, Jer 8:3 |
| Choice held open between living and dying (v2) | person | "which I shall choose I cannot tell" | Phili 1:22 |
| Choosing to escape affliction | person | "this you have chosen rather than affliction" | Job 36:21 |
| Choosing affliction over pleasure (v2) | person | "choosing rather to be mistreated … than to enjoy the fleeting pleasures of sin" | Heb 11:25 |
| Choosing the one thing (v2) | person | "Mary has chosen the good portion, which will not be taken away" | Luk 10:42 |
| Choosing by the eye | person | "saw … attractive … any they chose" | Gen 6:2, Gen 13:11 |
| Choosing for honour (v2) | person | "how they chose the places of honor" | Luk 14:7 |
| Choosing as preference / worth | person | "to be chosen rather than silver" | Pro 16:16, 22:1, Psa 84:10 |
| Choosing as one's own will | person | "you must choose, and not I"; "of his own accord" | Job 34:33, 2Cor 8:17 |
| Choosing as testing | God | "tried you in the furnace of affliction" | Isa 48:10 |

## 6. Open threads touched

- **OT-62** (anger × M64): 2 of its 7 verses are now read.
  - 1Sa 20:30 (H0977, face 3O; §3.9)
  - Psa 106:23 (H0972, face 2J; §3.5)
  - The other five use other M64 words (*willing*, *desire*, *purposed*, *wanted*), so OT-62 stays open.
- **OT-09** ("gold nuggets" pass before M64): not triggered by this pull.
- **Cluster tags:** G1586 is tagged T3, and G1588 and G1589 are tagged T2, not M64. They were pulled on your instruction and are read here with the M64 words. No re-tag is raised (#1970).

## 7. For the researcher

1. The 222 uncited verses and the faces in §5 are available for 10.7 *Choosing and setting direction*. 10.7 now carries only Deu 30:19 from these words. Weaving waits for your instruction.

## 8. Routing: the verses for Ch 13 "Other beings"

The routes (rule 72):
- **A:** another being in its own right. These go to Ch 13: 13.1 Divine, 13.2 Angels, 13.3 Other spirits, 13.4 Nature.
- **B:** the human inner being, including another being acting with it.
- **A+B:** both, described from different angles.
- **C:** no inner-being and no other-being bearing. These are assessed here but stay out of the narrative.

### 8.1 The basis used (for you to correct)

- A verse where God, the Lord or Jesus chooses, or where "chosen" or "elect" names those God chose, is **A (13.1)**.
- It is also **B** when the verse itself names a human inner activity or state, for example rejoice, fear, desire, know, believe, hear, pray, repent, love, despise, be strong, be careful or humble. The CSV `route_basis` column names the element.
- A verse where a person chooses is **B**. It is also **A** when the verse states God's own act or verdict, for example "the Lord will not answer you" (1Sa 8:18).
- "Chosen men", "chosen chariots", "choice silver" and "choice as the cedars" are **C** when they mark quality only, with no act of choosing and no inner bearing in the verse.

### 8.2 Count

| Route | Verses |
| --- | --- |
| A | 91 |
| A+B | 75 |
| B | 52 |
| C | 14 |
| **Ch 13 (A and A+B)** | **166** |
| flagged for you (§8.5) | 14 |

By group:

| Group | A | A+B | B | C |
| --- | --- | --- | --- | --- |
| "Choice": the best, preferred over | 0 | 0 | 4 | 2 |
| A person chooses a king or takes a side | 0 | 3 | 1 | 0 |
| A person chooses between death and life | 0 | 0 | 3 | 0 |
| A person chooses other gods, their own ways, what God does not delight in | 0 | 3 | 8 | 0 |
| A person chooses the Lord, life, his ways, the good | 0 | 3 | 10 | 0 |
| A person's own decision, desire or accord | 0 | 0 | 8 | 0 |
| A thing or place chosen for oneself (by sight, use or honour) | 0 | 0 | 6 | 0 |
| God chooses a people | 20 | 9 | 0 | 0 |
| God chooses a person for a task or office | 23 | 17 | 0 | 0 |
| God chooses a place for his name | 30 | 14 | 0 | 0 |
| God chooses the foolish, weak, low and poor | 2 | 1 | 0 | 0 |
| God chooses what he wants (a fast, a response, whom he appoints) | 4 | 2 | 0 | 0 |
| God sets a choice before a person | 0 | 2 | 0 | 0 |
| God tries (ESV "tried") | 0 | 1 | 0 | 0 |
| Jesus chooses | 1 | 5 | 0 | 0 |
| Men selected (for battle, leadership or a task) | 0 | 0 | 12 | 12 |
| The chosen / the elect (NT) | 11 | 15 | 0 | 0 |

### 8.3 The Ch 13 verses, by sub-chapter

**13.1 Divine.** God's choosing, in his own right. Route A only means the verse shows nothing of a human inner being.

| Group | Route A only | Route A+B (the inner element is in the CSV) |
| --- | --- | --- |
| God chooses a person for a task or office (40) | Num 16:5, Num 16:7, Deu 17:15, Deu 18:5, Deu 21:5, 1Sa 2:28, 1Sa 16:8, 1Sa 16:9, 1Sa 16:10, 1Ch 15:2, 1Ch 28:4, 1Ch 28:5, 1Ch 28:6, Neh 9:7, Psa 78:70, Psa 89:3, Psa 89:19, Psa 105:26, Isa 42:1, Hag 2:23, Mat 12:18, Act 9:15, Act 10:41 | Num 17:5, 1Sa 10:24, 2Sa 6:21, 2Sa 21:6, 1Ki 11:34, 1Ch 28:10, 1Ch 29:1, 2Ch 29:11, Psa 65:4, Psa 106:23, Isa 49:7, Luk 9:35, Luk 23:35, Act 1:24, Act 15:7, 1Pe 2:4, 1Pe 2:6 |
| God chooses a people (29) | Deu 4:37, Deu 7:6, Deu 7:7, Deu 10:15, Deu 14:2, 1Ki 3:8, 1Ch 16:13, Psa 33:12, Psa 47:4, Psa 78:67, Psa 78:68, Psa 105:6, Psa 135:4, Isa 14:1, Isa 41:8, Isa 41:9, Isa 43:20, Isa 65:9, Eze 20:5, Act 13:17 | Psa 105:43, Psa 106:5, Isa 43:10, Isa 44:1, Isa 44:2, Isa 45:4, Isa 65:15, Isa 65:22, Jer 33:24 |
| God chooses a place for his name (44) | Deu 12:5, Deu 12:11, Deu 12:14, Deu 12:26, Deu 14:24, Deu 14:25, Deu 15:20, Deu 16:2, Deu 16:6, Deu 16:7, Deu 16:16, Deu 17:8, Deu 26:2, Jos 9:27, 1Ki 8:16, 1Ki 11:13, 1Ki 11:32, 1Ki 11:36, 1Ki 14:21, 2Ki 21:7, 2Ki 23:27, 2Ch 6:5, 2Ch 6:6, 2Ch 7:16, 2Ch 12:13, 2Ch 33:7, Psa 132:13, Zec 1:17, Zec 2:12, Zec 3:2 | Deu 12:18, Deu 12:21, Deu 14:23, Deu 16:11, Deu 16:15, Deu 17:10, Deu 18:6, Deu 31:11, 1Ki 8:44, 1Ki 8:48, 2Ch 6:34, 2Ch 6:38, 2Ch 7:12, Neh 1:9 |
| A person chooses the Lord, life, his ways, the good (3) | — | Deu 30:19, Psa 25:12, Isa 56:4 |
| A person chooses other gods, their own ways, what God does not delight in (3) | — | Judg 10:14, Isa 41:24, Isa 65:12 |
| A person chooses a king or takes a side (3) | — | 1Sa 8:18, 1Sa 12:13, 2Sa 16:18 |
| God sets a choice before a person (2) | — | 2Sa 24:12, 1Ch 21:10 |
| God chooses what he wants (a fast, a response, whom he appoints) (6) | Pro 21:3, Isa 58:6, Jer 49:19, Jer 50:44 | Isa 58:5, Isa 66:4 |
| God tries (ESV "tried") (1) | — | Isa 48:10 |
| The chosen / the elect (NT) (26) | Mat 22:14, Mat 24:22, Mat 24:31, Mar 13:20, Mar 13:27, Rom 8:33, Rom 9:11, Rom 11:5, Rom 16:13, 1Ti 5:21, 2Jo 13 | Mat 24:24, Mar 13:22, Luk 18:7, Rom 11:7, Rom 11:28, Eph 1:4, Col 3:12, 1Th 1:4, 2Th 2:13, 2Ti 2:10, Tit 1:1, 1Pe 2:9, 2Pe 1:10, 2Jo 1, Rev 17:14 |
| Jesus chooses (6) | Act 1:2 | Luk 6:13, Joh 6:70, Joh 13:18, Joh 15:16, Joh 15:19 |
| God chooses the foolish, weak, low and poor (3) | 1Cor 1:27, 1Cor 1:28 | Jam 2:5 |

**13.2 Angels** (3): Mat 24:31 (he will send out his angels); Mar 13:27 (he will send out the angels); 1Ti 5:21 (the elect angels). These verses are also in 13.1. More candidates are in §8.5.

**13.3 Other spirits** (1): Zec 3:2 (Satan rebuked). These verses are also in 13.1. More candidates are in §8.5.

**13.4 Nature** (1): Isa 43:20 (the wild beasts will honor me). These verses are also in 13.1. More candidates are in §8.5.

### 8.4 Route C: assessed here, kept out of the narrative (14)

Exo 14:7 ("chosen chariots"); Judg 20:15 ("chosen men"); Judg 20:16 ("chosen men"); Judg 20:34 ("chosen men"); 1Sa 24:2 ("chosen men"); 1Sa 26:2 ("chosen men"); 2Sa 6:1 ("chosen men"); 1Ki 12:21 ("chosen warriors"); 2Ch 11:1 ("chosen warriors"); 2Ch 13:3 ("chosen men"); 2Ch 13:17 ("chosen men"); 2Ch 25:5 ("choice men"); Pro 8:19 ("choice silver"); Song 5:15 ("choice as the cedars").

The other "men selected" verses are route B, because a person's act of choosing is stated. Examples are Exo 17:9 "Choose for us men", 2Sa 10:9 "he chose some of the best men", and the church's choosing in Acts.

### 8.5 Flagged: your call (14)

These are routed in the CSV by the basis above. The question is whether they also, or instead, belong in a Ch 13 section.

| Verse | Route now | Question |
| --- | --- | --- |
| Gen 6:2 | B | who are "the sons of God"? The verse does not say. A (13.2/13.3) or B only? |
| Jos 24:15 | B | gods chosen: do chosen gods/idols belong in 13.3 Other spirits? |
| Judg 5:8 | B | gods chosen: do chosen gods/idols belong in 13.3 Other spirits? |
| Judg 10:14 | A+B | gods chosen: do chosen gods/idols belong in 13.3 Other spirits? |
| Isa 40:20 | B | an idol chosen and made: 13.3? |
| Isa 41:24 | A+B | God addresses the idols ("you are nothing"): 13.3? |
| Jer 49:19 | A | God likens himself to a lion: is a simile from nature 13.4? |
| Jer 50:44 | A | God likens himself to a lion: is a simile from nature 13.4? |
| Luk 6:13 | A+B | Jesus choosing: 13.1 Divine, or the human inner being of Jesus, or both? |
| Joh 6:70 | A+B | Jesus choosing; and "one of you is a devil": 13.3? |
| Joh 13:18 | A+B | Jesus choosing: 13.1 Divine, human, or both? |
| Joh 15:16 | A+B | Jesus choosing: 13.1 Divine, human, or both? |
| Joh 15:19 | A+B | Jesus choosing: 13.1 Divine, human, or both? |
| Act 1:2 | A | Jesus choosing: 13.1 Divine, human, or both? |

### 8.6 What has not been done

- **Nothing is woven into Ch 13 or 10.7.** The narrative routing of the choosing verses waits for the researcher's direction (OT-92).
- **Route A is not yet read for what each verse says of God's character.** That reading comes when 13.1 is built.
- **The image question is parked (#1984).**

