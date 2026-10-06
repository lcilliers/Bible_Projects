# Life and death: strand observation ledger, unit 2 (v1)

**Date:** 2026-10-02 · **Author:** Claude Code · **Strand:** life and death, M25 (approved #1932) · **Unit:** 2, dying and death · **Status:** **approved and woven** (#1939, researcher 2026-10-03: *"proceed to weave in"*); see "Woven — where" at the end. · Follows `life-death-strand-candidate-v2-20261002.md` §5 unit 2 and §7 (questions Q1–Q4), and the format of `life-death-observation-ledger-unit1-v1-20261002.md`.

**Threads this unit may bear on** (`../../cross-cluster-web/open-threads-register.md`, checked before the pull):
- **OT-02** (Q1, What is death?): this unit is its main source
- **OT-03** (Q2, spirit and soul at death) and **OT-04** (Q3, the heart after death): touched
- **OT-05** (Q4, the body): the "corruption" verses only
- **OT-08** (life and death over the inner being): what each word is set against

**Scope of unit 2**

| Strong | Gloss | Hits | Surfaces (ESV) |
| --- | --- | --- | --- |
| H4191 | to die | 840 | die · died · dead · death · put to death · kill(ed) · dies · surely · shall · dying · slay · murder · forever … |
| H4194 | death | 156 | death · die(s) · died · pestilence · dead · deathly · deadly |
| G2288 | death | 120 | death · mortal · must surely · die(d) · pestilence · death penalty · deadly peril |
| G0599 | to die | 110 | died · die · dies · dead · dying · death · drowned · killed · mortal |
| G1312 | corruption | 6 | corruption |
| G3499 | to put to death | 3 | put to death · (as good as) dead |
| G4881 · G2253 | to perish with · half-dead | 1 + 1 | perish · half dead |

**1,237 hits in 1,045 verses**, all read, **grouped by surface**.

**Data**
- **The pull:** `life-death-unit2-dying-death-pull-v1-20261002.csv`. One row per hit, with the full ESV text and a face. **Every hit has a face**, and no verse text is missing.
- **How it was built:** from iba.db (read-only) by the new reusable script `strand-unit-pull-v1-20261002.py`. It writes the same columns as the unit 1 pull, and merges faces in afterwards.
- **The faces as data:** `life-death-unit2-face-assign-v1-20261002.py`. It refuses to run if any hit is left without a face, or if any assignment matches no hit.
  - Hits that read as plain notices, sentences or killings fall back to D01, D02 or D03. These were read too, and the misfits were listed and corrected by verse (28 of them).

**Basis:** **S** = the verse states it · **R** = my reading, kept labelled ("I read").

**Disposition (proposed):** **W** weave where it touches · **RS** reshapes existing text · **NS** new structure needed · **H** held · **D** stays in data.

**Checks**
- **Surface alignment.** "surely", "shall", "be", "certainly" and "must" are the doubled Hebrew verb or the auxiliary of "put to death". They sit on the same verse as the death hit. "forever" (Psa 48:14) is H4191 in the source text and is left in the data (D27).
- **One duplicated hit.** 1Ki 2:42 has two `verse_lexical` rows at position 18, from the same span (code_ordinals 0 and 2). Both carry the doubled verb "know for certain … you shall die". This is not an error, and both rows are kept.
- **Quotes:** every quote is checked against iba.db `verse` (§G).

---

## A. The faces in unit 2 (change of character, #1919)

| Face | Hits / verses | What differs | Example verses |
| --- | --- | --- | --- |
| **D01. Death notices, lifespans, burial** | 174 / 165 | "and he died"; "after the death of"; "till the day of his death"; burying the dead; a man dying childless | Gen 5; Gen 23; Judg 10–12; 1Ch 1 |
| **D02. Put to death under law or sentence** | 123 / 80 | "shall surely be put to death"; "deserves death"; stoning; witnesses | Exo 21; Lev 20; Num 35; Deu 17; Act 25:25 |
| **D03. Killed or spared by people** | 201 / 171 | Murder, war, plots, execution by kings, suicide; "you shall not die" from a king | 1Sa 19; 2Sa 11; 2Ki 11; 2Ki 15; Jer 26; Jer 38 |
| **D04. Struck down by God; death as judgement** | 139 / 120 | Plague, fire, the word of a prophet; "by the sword, by famine, and by pestilence" | Gen 38:7; Lev 10:2; 2Sa 6:7; Jer 21:9; Eze 6:12 |
| **D05. Near the holy: "lest you die"** | 35 / 31 | The sanctuary statutes; hearing God's voice; seeing God | Exo 20:19; Lev 16:2; Num 4:20; Judg 13:22 |
| **D06. Dying of hunger, thirst, sickness or danger** | 39 / 33 | "that we may live and not die"; "at the point of death"; "before my child dies" | Gen 42:2; 2Ki 7:4; 2Ki 20:1; Joh 4:47 |
| **D07. Before I die** | 21 / 21 | Last words, blessing, burial wishes, a request | Gen 27:4; Gen 46:30; Gen 50:24; Pro 30:7 |
| **D08. What death is: the common lot** | 60 / 53 | All die; the wise like the fool; man like the beast; the day of death; "gathered to his people" | 2Sa 14:14; Job 14:10; Ecc 2:16; 9:5; Heb 9:27 |
| **D09. The dead** | 20 / 19 | The dead do not praise; inquiring of the dead; "not dead but sleeping"; going to the dead | Psa 6:5; 115:17; Isa 8:19; Mat 9:24; 2Sa 12:23 |
| **D10. Mourning and grief at a death** | 28 / 22 | Weeping, fasting, longing, "would I had died instead of you" | 2Sa 12:18–23; 18:33; Gen 44:31; Joh 11:32 |
| **D11. Fear and anguish facing death** | 21 / 20 | The terrors of death; the soul sorrowful to death; a step from death | Psa 55:4; Heb 2:15; Mat 26:38; 1Sa 20:3 |
| **D12. Wanting to die; wishing one had died** | 30 / 24 | Longing for death, preferring it, wishing for it, "better to die" | Job 3:21; Jon 4:3; Rev 9:6; Num 14:2 |
| **D13. Ready to die for or with another** | 20 / 16 | Loyalty that reaches to death | Rut 1:17; Act 21:13; Rev 12:11 |
| **D14. Death and sin** | 50 / 34 | Death entering through sin; dying for one's own sin; sin producing death | Gen 2:17; Rom 5:12; 6:23; Jam 1:15; Eze 18:4 |
| **D15. The way to death (wisdom)** | 31 / 30 | Paths, snares and ways; what kills a person from within; the tongue | Pro 14:12; 18:21; 21:25; Job 5:2 |
| **D16. Turn and do not die (Ezekiel)** | 26 / 17 | God's will for life; the watchman's warning | Eze 3:18–20; 18:21–32; 33:8–18 |
| **D17. Death as a power, realm or enemy** | 24 / 23 | Cords, snares, gates, reign, keys; the last enemy; compared with love and greed | Psa 18:5; Rom 5:14; 1Cor 15:26; Song 8:6; Hab 2:5 |
| **D18. Delivered from death** | 16 / 16 | God redeems, lifts up, delivers; a person brings a sinner back | Psa 68:20; Hos 13:14; 2Cor 1:10; Jam 5:20 |
| **D19. Life beyond death** | 13 / 13 | Never see death; death swallowed up; death abolished | Joh 8:51; 11:26; 2Ti 1:10; Isa 25:8 |
| **D20. The second death** | 5 / 5 | Judgement beyond death | Rev 2:11; 20:14; 21:8; Isa 66:24 |
| **D21. Christ's death** | 47 / 40 | Died for sins, for the ungodly, for all; the kind of death; the trials | 1Cor 15:3; Rom 5:8; Phili 2:8; Heb 2:9; Isa 53:12 |
| **D22. Died with Christ** | 12 / 12 | Dying to sin and to the law; putting to death what is earthly | Rom 6:2–8; Gal 2:19; Col 3:5; Rom 7:6 |
| **D23. Death at work in the living** | 16 / 14 | The mind set on the flesh; abiding in death; worldly grief; the body of death | Rom 7:9–13, 24; 8:6; 1Jo 3:14; 2Cor 7:10 |
| **D24. Like the dead** | 12 / 12 | The living likened to the dead; the heart that died; "dead dog" | Psa 88:5; 143:3; 1Sa 25:37; 2Sa 9:8; Rom 4:19 |
| **D25. Living and dying to the Lord** | 26 / 22 | Death that belongs to the Lord; the death of the upright; dying in faith | Rom 14:7–8; Phili 1:20–21; Psa 116:15; Heb 11:13 |
| **D26. Uncleanness from the dead** | 13 / 11 | Touching the dead (law) | Num 19; Lev 21:11; Eze 44:25 |
| **D27. Not the inner being** | 29 / 26 | Fish, livestock, frogs, flies, a tree stump, the beast's wound, idiom | Exo 7:21; Exo 9:6; Ecc 10:1; Job 14:8; Rev 13:3 |
| **D28. Corruption** | 6 / 6 | The body seeing decay, or not | Act 2:27, 31; 13:34–37 |

**Proportions.** D01–D04 hold 637 of the 1,237 hits. D26 and D27 hold another 42. These are accounted for and stay in the data. The rest are read below.

---

## B. Observations (LD-43 onward)

### B.1 What death is (faces D08, D09): Q1

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-43 | **Death comes to all, and is not reversed by people.** "We must all die; we are like water spilled on the ground, which cannot be gathered up again. But God will not take away life, and he devises means so that the banished one will not remain an outcast". "How the wise dies just like the fool!"; "he sees that even the wise die"; "a time to be born, and a time to die"; "it is appointed for man to die once, and after that comes judgment" | 2Sa 14:14; Ecc 2:16; Psa 49:10; Ecc 3:2; Heb 9:27 | S | **2 "What death is"** | W |
| LD-44 | **The same death, met differently.** "One dies in his full vigor, being wholly at ease and secure"; "Another dies in bitterness of soul, never having tasted of prosperity". Of the wicked: "they have no pangs until death". "Why should you die before your time?" | Job 21:23, 25; Psa 73:4; Ecc 7:17 | S | 2, 5 (bitterness of soul) | W |
| LD-45 | **What does not go with the dead.** "For when he dies he will carry nothing away; his glory will not go down after him"; "When the wicked dies, his hope will perish, and the expectation of wealth perishes too" | Psa 49:17; Pro 11:7 | S | 2, 10.6 | W |
| LD-46 | **The dead, seen from this side.** "But a man dies and is laid low; man breathes his last, and where is he?"; "For the living know that they will die, but the dead know nothing, and they have no more reward, for the memory of them is forgotten"; "a living dog is better than a dead lion". The dead do not praise: "For in death there is no remembrance of you; in Sheol who will give you praise?"; "The dead do not praise the Lord, nor do any who go down into silence"; "Do the departed rise up to praise you?"; "death does not praise you; those who go down to the pit do not hope for your faithfulness" | Job 14:10; Ecc 9:5, 4; Psa 6:5; 115:17; 88:10; Isa 38:18 | S | **2 "After death"**, Q1, **Q2** | **RS** (with LD-47; see the decision in §F) |
| LD-47 | **The dead, with God.** "The poor man died and was carried by the angels to Abraham's side". "Blessed are the dead who die in the Lord from now on." The Spirit adds, "that they may rest from their labors, for their deeds follow them!" Paul: "For to me to live is Christ, and to die is gain". David, of his dead child: "I shall go to him, but he will not return to me" | Luk 16:22; Rev 14:13; Phili 1:21; 2Sa 12:23 | S. Set beside LD-46; **no reconciliation drawn** | **2 "After death"**, **Q2** | **RS** (LD-46 and LD-47 side by side, the way Luk 24:39 and 1Cor 15:50 stand in "Christ first") |
| LD-48 | **Death spoken of as sleep.** "the girl is not dead but sleeping. And they laughed at him"; "Now Jesus had spoken of his death, but they thought that he meant taking rest in sleep"; "through Jesus, God will bring with him those who have fallen asleep"; "David, after he had served the purpose of God in his own generation, fell asleep and was laid with his fathers and saw corruption" | Mat 9:24 (Mar 5:39; Luk 8:52); Joh 11:13; 1Th 4:14; Act 13:36 | S | 2 "What death is", Q1 | W |
| LD-49 | **The day of death.** "I am old; I do not know the day of my death"; "his day will come to die"; "A good name is better than precious ointment, and the day of death than the day of birth" | Gen 27:2; 1Sa 26:10; Ecc 7:1 | S | 2 | W |
| LD-50 | **"See death" and "taste death"** as idiom for dying: "he would not see death before he had seen the Lord's Christ"; "some standing here who will not taste death until they see the Son of Man coming in his kingdom" | Luk 2:26; Mat 16:28 (Mar 9:1; Luk 9:27) | S | — | D (idiom; Luk 2:26 is already in the Simeon passage of 10.9) |

### B.2 Death and sin (face D14)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-51 | **The first word about death, and its first denial.** "but of the tree of the knowledge of good and evil you shall not eat, for in the day that you eat of it you shall surely die". "But the serpent said to the woman, 'You will not surely die.'" | Gen 2:17; 3:4 | S | **2 "What death is"**, 10.5 | **NS** (Ch 2 has no account of death and sin) |
| LD-52 | **Death entered through sin, and reigns.** "Therefore, just as sin came into the world through one man, and death through sin, and so death spread to all men because all sinned"; "death reigned from Adam to Moses"; "as sin reigned in death, grace also might reign through righteousness leading to eternal life"; "For the wages of sin is death, but the free gift of God is eternal life in Christ Jesus our Lord"; "The sting of death is sin, and the power of sin is the law"; "For as by a man came death, by a man has come also the resurrection of the dead" | Rom 5:12, 14, 21; 6:23; 1Cor 15:56, 21 | S | **2 "What death is"**, 12, 14 | **NS** |
| LD-53 | **The inner sequence, in the verses' own words.** "Then desire when it has conceived gives birth to sin, and sin when it is fully grown brings forth death"; "our sinful passions, aroused by the law, were at work in our members to bear fruit for death"; "I was once alive apart from the law, but when the commandment came, sin came alive and I died"; "The very commandment that promised life proved to be death to me"; "It was sin, producing death in me through what is good" | Jam 1:15; Rom 7:5, 9, 10, 13 | S (the order is the verses' own, not built across them) | **2**, **10.6**, 12 | **NS** |
| LD-54 | **Each dies for his own sin.** "the soul who sins shall die"; "each one shall die for his own sin"; "everyone shall die for his own iniquity"; the daughters of Zelophehad say that their father "died for his own sin" | Eze 18:4, 20; 2Ki 14:6 (Deu 24:16; 2Ch 25:4); Jer 31:30; Num 27:3 | S | 2, 12 (Eze 18:4 is already in Ch 5, 9 and 12) | W (pointer) |
| LD-55 | **To die in one's sins, and sin that leads to death.** "I told you that you would die in your sins, for unless you believe that I am he you will die in your sins". "If anyone sees his brother committing a sin not leading to death, he shall ask, and God will give him life … There is sin that leads to death; I do not say that one should pray for that"; "All wrongdoing is sin, but there is sin that does not lead to death" | Joh 8:24; 1Jo 5:16, 17 | S. The verse does not say which sin leads to death, and nothing is drawn | 2, 10.9 (asking for a brother) | W (quote and stop) |
| LD-56 | **Sin put away, and a death still to come.** "The Lord also has put away your sin; you shall not die. Nevertheless, because by this deed you have utterly scorned the Lord, the child who is born to you shall die". The widow at Zarephath reads her son's death as a remembering of her sin: "You have come to me to bring my sin to remembrance and to cause the death of my son!" | 2Sa 12:13–14; 1Ki 17:18 | S (1Ki 17:18 is her reading, as the verse gives it) | 10.3, 10.9, 13 | W |

### B.3 Death at work in the living, and the living like the dead (faces D23, D24)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-57 | **Death named inside a living person.** "For to set the mind on the flesh is death, but to set the mind on the Spirit is life and peace"; "Whoever does not love abides in death"; "worldly grief produces death"; "Wretched man that I am! Who will deliver me from this body of death?"; "For the end of those things is death"; to a church: "strengthen what remains and is about to die"; of false teachers: "fruitless trees in late autumn, twice dead, uprooted" | Rom 8:6; 1Jo 3:14; 2Cor 7:10; Rom 7:24; 6:21; Rev 3:2; Jude 12 | S | **2 "What death is"** (widens the bullet "The living can be called dead"), 10.4 (the mind; Rom 8:6 is already in Ch 7), 10.1 (grief), 10.10 (love), 12 | RS |
| LD-58 | **The living likened to the dead.** "like one set loose among the dead, like the slain that lie in the grave, like those whom you remember no more, for they are cut off from your hand"; "For the enemy has pursued my soul; he has crushed my life to the ground; he has made me sit in darkness like those long dead"; "among those in full vigor we are like dead men"; of Miriam: "Let her not be as one dead". "for those dwelling in the region and shadow of death, on them a light has dawned" | Psa 88:5; 143:3 (Lam 3:6); Isa 59:10; Num 12:12; Mat 4:16 (Luk 1:79) | S | 2 (with Psa 31:12, already there), 10.1 | W |
| LD-59 | **"A dead dog": how a person rates himself or another.** Mephibosheth: "What is your servant, that you should show regard for a dead dog such as I?"; David to Saul: "After a dead dog! After a flea!"; Abishai of Shimei: "Why should this dead dog curse my lord the king?" | 2Sa 9:8; 1Sa 24:14; 2Sa 16:9 | S | 10.10 | W |
| LD-60 | **A body "as good as dead", and faith that considers it.** "He did not weaken in faith when he considered his own body, which was as good as dead (since he was about a hundred years old), or when he considered the barrenness of Sarah's womb"; "from one man, and him as good as dead, were born descendants as many as the stars of heaven" | Rom 4:19; Heb 11:12 | S | 10.4 (considering), 10.9 | W |

### B.4 Death as a power (face D17)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-61 | **Death pictured as cords, waves, gates, a shepherd.** "For the waves of death encompassed me, the torrents of destruction assailed me; the cords of Sheol entangled me; the snares of death confronted me"; "Have the gates of death been revealed to you, or have you seen the gates of deep darkness?"; "Like sheep they are appointed for Sheol; death shall be their shepherd"; "the firstborn of death consumes his limbs"; "For death has come up into our windows; it has entered our palaces" | 2Sa 22:5–6 (Psa 18:4–5); Job 38:17; Psa 49:14; Job 18:13; Jer 9:21 | S | 2 "Delivered from death" (Psa 116:3 is already there) | W |
| LD-62 | **Death as a ruler that is overthrown.** "death no longer has dominion over him"; "God raised him up, loosing the pangs of death, because it was not possible for him to be held by it"; "that through death he might destroy the one who has the power of death, that is, the devil"; "The last enemy to be destroyed is death"; "I died, and behold I am alive forevermore, and I have the keys of Death and Hades"; "For I am sure that neither death nor life, nor angels nor rulers" | Rom 6:9; Act 2:24; Heb 2:14; 1Cor 15:26; Rev 1:18; Rom 8:38 | S | **2 "Changed"**, 14 | W |
| LD-63 | **The inner being measured against death.** "for love is strong as death, jealousy is fierce as the grave"; of the arrogant man: "His greed is as wide as Sheol; like death he has never enough"; "And I find something more bitter than death: the woman whose heart is snares and nets, and whose hands are fetters" | Song 8:6; Hab 2:5; Ecc 7:26 | S | 10.6 (greed, love), 10.10, 11 §4 | W (Isa 28:15, "a covenant with death", is already in 10.11) |

### B.5 Facing death (faces D11, D05)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-64 | **The fear of death, as slavery.** Christ shared flesh and blood "that through death he might destroy the one who has the power of death, that is, the devil, and deliver all those who through fear of death were subject to lifelong slavery" | Heb 2:14–15 | S | **10.1 "Fear"**, 2 | W |
| LD-65 | **The heart and the soul as death comes near.** "My heart is in anguish within me; the terrors of death have fallen upon me"; "My soul is very sorrowful, even to death"; "his soul was vexed to death"; "there is but a step between me and death"; "Surely the bitterness of death is past"; "light up my eyes, lest I sleep the sleep of death"; "you lay me in the dust of death"; "my heart is wrung within me … in the house it is like death" | Psa 55:4; Mat 26:38 (Mar 14:34); Judg 16:16; 1Sa 20:3; 1Sa 15:32; Psa 13:3; 22:15; Lam 1:20 | S (Mat 26:38 is already in Ch 5 and 7; Judg 16:16 in Ch 5) | **2 (new section)**, 10.1, **Q3** (the heart *before* death) | **NS** |
| LD-66 | **What the felt nearness of death was for.** "Indeed, we felt that we had received the sentence of death. But that was to make us rely not on ourselves but on God who raises the dead". Jesus "offered up prayers and supplications, with loud cries and tears, to him who was able to save him from death, and he was heard because of his reverence" | 2Cor 1:9; Heb 5:7 (already in Ch 7) | S | 2, 10.9 | W |
| LD-67 | **The fear of dying shapes what people do.** Isaac, of his wife: "Because I thought, 'Lest I die because of her.'" Judah held back his son, "for he feared that he would die, like his brothers". The people to Samuel: "Pray for your servants to the Lord your God, that we may not die, for we have added to all our sins this evil". And God: "who are you that you are afraid of man who dies, of the son of man who is made like grass" | Gen 26:9; 38:11; 1Sa 12:19; Isa 51:12 | S | 10.11 (Gen 26:9), 10.1 | W |
| LD-68 | **"Lest we die" before God, and a reasoned answer.** "You speak to us, and we will listen; but do not let God speak to us, lest we die"; Manoah: "We shall surely die, for we have seen God." His wife: "If the Lord had meant to kill us, he would not have accepted a burnt offering and a grain offering at our hands, or shown us all these things". To Gideon: "Peace be to you. Do not fear; you shall not die" | Exo 20:19 (Deu 5:25; 18:16); Judg 13:22–23; Judg 6:23 | S | 10.9 (with LD-35), **10.4** (reasoning from what God has done), 10.1 | W |

### B.6 Wanting to die (face D12): Ch 2 already has the section

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-69 | **Death longed for and not found.** "who long for death, but it comes not, and dig for it more than for hidden treasures"; "Why did I not die at birth, come out from the womb and expire?"; "people will seek death and will not find it. They will long to die, but death will flee from them"; "Death shall be preferred to life by all the remnant that remains of this evil family"; "I thought the dead who are already dead more fortunate than the living who are still alive" | Job 3:21, 11 (Jer 20:17); Rev 9:6; Jer 8:3; Ecc 4:2 | S | **2 "Wanting to die"** | RS |
| LD-70 | **The wish in other settings.** Rachel, envying her sister: "Give me children, or I shall die!" Job's wife: "Do you still hold fast your integrity? Curse God and die." Abimelech, wounded: "Draw your sword and kill me, lest they say of me, 'A woman killed him.'" And "his young man thrust him through, and he died". Israel in the wilderness: "it would have been better for us to serve the Egyptians than to die in the wilderness" | Gen 30:1; Job 2:9; Judg 9:54; Exo 14:12 (Num 14:2; 20:4; 21:5) | S | **2 "Wanting to die"**, 10.6 (Rachel) | **RS. Two Ch 2 claims need restating** (claim register): (a) "Only twice is the wish granted". Abimelech's request is granted too (Judg 9:54), so the count is wrong. (b) "the wish belongs almost always to the soul". Of the 24 wish verses in this pull, 7 carry *nephesh* (1Ki 19:4; 2Sa 1:9; Job 7:15; Jon 4:3, 8; Judg 16:30; Num 21:5), and the other 17 carry no inner word (soul, spirit or heart) |

### B.7 Before I die, and ready to die (faces D07, D13)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-71 | **What is asked or given before dying.** Isaac: "that my soul may bless you before I die"; Jacob: "Now let me die, since I have seen your face and know that you are still alive"; Joseph: "I am about to die, but God will visit you and bring you up out of this land"; "Two things I ask of you; deny them not to me before I die"; "By faith Jacob, when dying, blessed each of the sons of Joseph, bowing in worship over the head of his staff" | Gen 27:4; 46:30; 50:24 (48:21); Pro 30:7; Heb 11:21 | S | **2 (new section)**, 10.6, 10.9 | NS (with LD-79, LD-80) |
| LD-72 | **Loyalty that reaches to death.** Ruth: "Where you die I will die, and there will I be buried. May the Lord do so to me and more also if anything but death parts me from you". "In life and in death they were not divided". Ittai: "wherever my lord the king shall be, whether for death or for life, there also will your servant be". Peter: "Even if I must die with you, I will not deny you!" Thomas: "Let us also go, that we may die with him". Paul: "What are you doing, weeping and breaking my heart? For I am ready not only to be imprisoned but even to die in Jerusalem for the name of the Lord Jesus". "they loved not their lives even unto death"; "Be faithful unto death, and I will give you the crown of life". "For one will scarcely die for a righteous person—though perhaps for a good person one would dare even to die" | Rut 1:17; 2Sa 1:23; 2Sa 15:21; Mat 26:35; Joh 11:16; Act 21:13; Rev 12:11; Rev 2:10; Rom 5:7 | S | **10.10**, 10.7, 2 (pointer) | W |

### B.8 Delivered from death, and life beyond it (faces D18, D19, D28)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-73 | **More deliverance from death.** "Our God is a God of salvation, and to God, the Lord, belong deliverances from death"; "O you who lift me up from the gates of death"; "In famine he will redeem you from death"; "The Lord has disciplined me severely, but he has not given me over to death"; "He delivered us from such a deadly peril, and he will deliver us". A person may do it too: "whoever brings back a sinner from his wandering will save his soul from death"; "Rescue those who are being taken away to death" | Psa 68:20; 9:13; Job 5:20; Psa 118:18; 2Cor 1:10; Jam 5:20; Pro 24:11 | S | **2 "Delivered from death"**, 10.10 (Jam 5:20) | W |
| LD-74 | **Ransomed from Death, and death abolished.** "I shall ransom them from the power of Sheol; I shall redeem them from Death. O Death, where are your plagues? O Sheol, where is your sting?" Christ "abolished death and brought life and immortality to light through the gospel" | Hos 13:14; 2Ti 1:10 | S | **2 "Changed"** (1Cor 15:55 is already there and echoes Hos 13:14) | W |
| LD-75 | **Never to see death.** "if anyone keeps my word, he will never see death"; "everyone who lives and believes in me shall never die. Do you believe this?"; "so that one may eat of it and not die"; Enoch "was taken up so that he should not see death"; "We know that we have passed out of death into life, because we love the brothers" | Joh 8:51; 11:26; 6:50; Heb 11:5; 1Jo 3:14 | S | **2 "Made alive"** (Joh 5:24 and 11:25 are already there), 10.10 (1Jo 3:14) | W |
| LD-76 | **Corruption.** "For you will not abandon my soul to Hades, or let your Holy One see corruption"; "For David, after he had served the purpose of God in his own generation, fell asleep and was laid with his fathers and saw corruption, but he whom God raised up did not see corruption" | Act 2:27; 13:36–37 (2:31; 13:34–35) | S | **2 "Christ first"** (Psa 16:10 is already in "Delivered from death"), **Q4** | W |

### B.9 Christ's death, and dying with him (faces D21, D22)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-77 | **Christ's death, as the verses state it.** "that Christ died for our sins in accordance with the Scriptures"; "while we were still sinners, Christ died for us"; "he poured out his soul to death and was numbered with the transgressors; yet he bore the sin of many"; "he humbled himself by becoming obedient to the point of death, even death on a cross"; "so that by the grace of God he might taste death for everyone"; "we were reconciled to God by the death of his Son" | 1Cor 15:3; Rom 5:8; Isa 53:12; Phili 2:8; Heb 2:9; Rom 5:10 | S | **2 "Made alive"** (short), 14 | W |
| LD-78 | **What his death is for those who live.** "For the love of Christ controls us, because we have concluded this: that one has died for all, therefore all have died; and he died for all, that those who live might no longer live for themselves but for him who for their sake died and was raised". "By what you eat, do not destroy the one for whom Christ died" | 2Cor 5:14–15; Rom 14:15 (1Cor 8:11) | S | 10.7, 10.10 | W |
| LD-79 | **Dying to sin and to the law; putting to death.** "How can we who died to sin still live in it?"; "For one who has died has been set free from sin"; "For through the law I died to the law, so that I might live to God"; "we are released from the law, having died to that which held us captive, so that we serve in the new way of the Spirit"; "Put to death therefore what is earthly in you: sexual immorality, impurity, passion, evil desire, and covetousness, which is idolatry"; "if by the Spirit you put to death the deeds of the body, you will live" | Rom 6:2, 7; Gal 2:19; Rom 7:6; Col 3:5; Rom 8:13 | S | **14**, 2 "Made alive" (Rom 6:4 and Col 3:3 are already there), 10.6 (Col 3:5) | W |

### B.10 Living and dying to the Lord (face D25)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-80 | **A death that belongs to the Lord.** "For none of us lives to himself, and none of us dies to himself. For if we live, we live to the Lord, and if we die, we die to the Lord. So then, whether we live or whether we die, we are the Lord's"; "Christ will be honored in my body, whether by life or by death. For to me to live is Christ, and to die is gain"; "I die every day!"; "For we who live are always being given over to death for Jesus' sake, so that the life of Jesus also may be manifested in our mortal flesh"; "as dying, and behold, we live" | Rom 14:7–8; Phili 1:20–21; 1Cor 15:31; 2Cor 4:11; 6:9 | S | **2 (new section)** | **NS** |
| LD-81 | **The death of the upright.** "Precious in the sight of the Lord is the death of his saints"; Balaam: "Let me die the death of the upright, and let my end be like his!"; "the righteous finds refuge in his death"; to Zedekiah: "You shall die in peace"; "These all died in faith, not having received the things promised"; Abel: "through his faith, though he died, he still speaks"; "unless a grain of wheat falls into the earth and dies, it remains alone; but if it dies, it bears much fruit" | Psa 116:15; Num 23:10; Pro 14:32; Jer 34:5; Heb 11:13; 11:4; Joh 12:24 | S | **2 (new section)**, 10.9 | NS (with LD-80) |

### B.11 The way to death (faces D15, D16)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-82 | **Death set before a person as a way.** "See, I have set before you today life and good, death and evil"; "Behold, I set before you the way of life and the way of death"; "There is a way that seems right to a man, but its end is the way to death"; "In the path of righteousness is life, and in its pathway there is no death"; "Whoever is steadfast in righteousness will live, but he who pursues evil will die"; "righteousness delivers from death"; "Death and life are in the power of the tongue, and those who love it will eat its fruits" | Deu 30:15; Jer 21:8; Pro 14:12 (16:25); Pro 12:28; 11:19; 10:2 (11:4); Pro 18:21 | S | **2 "Life set before a person"** (it has the life side only), 10.5 (Pro 18:21), 10.7 | RS |
| LD-83 | **What kills a person from within.** "Surely vexation kills the fool, and jealousy slays the simple"; "The desire of the sluggard kills him, for his hands refuse to labor"; "He dies for lack of discipline, and because of his great folly he is led astray"; "fools die for lack of sense"; "whoever hates reproof will die"; "he who despises his ways will die" | Job 5:2; Pro 21:25; 5:23; 10:21; 15:10; 19:16 | S | 10.1 (vexation, jealousy), **10.6** (desire), 10.2 (reproof), 12 | W |
| LD-84 | **Answerable for another's death.** "If I say to the wicked, 'You shall surely die,' and you give him no warning … that wicked person shall die for his iniquity, but his blood I will require at your hand". "But if you warn the wicked, and he does not turn from his wickedness … you will have delivered your soul" | Eze 3:18–19 (33:8–9) | S | 10.10 | W (Eze 18 and 33, God's will for life, are already in Ch 2) |
| LD-85 | **Discipline and a child's death.** "Discipline your son, for there is hope; do not set your heart on putting him to death"; "if you strike him with a rod, he will not die" | Pro 19:18; 23:13 | S | — | D |

### B.12 Mourning (face D10)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-86 | **Grief at a death, in its forms.** David, after the child died: "But now he is dead. Why should I fast? Can I bring him back again? I shall go to him, but he will not return to me"; "the spirit of the king longed to go out to Absalom, because he was comforted about Amnon, since he was dead"; "Weep not for him who is dead, nor grieve for him, but weep bitterly for him who goes away"; Hagar: "Let me not look on the death of the child"; Judah of Jacob: "as soon as he sees that the boy is not with us, he will die"; Mary: "Lord, if you had been here, my brother would not have died"; to Ezekiel: "Sigh, but not aloud; make no mourning for the dead" | 2Sa 12:23; 13:39; Jer 22:10; Gen 21:16; Gen 44:31; Joh 11:32; Eze 24:17 | S (2Sa 18:33 is already in 10.1 and Ch 11) | **10.1** (grief), 10.3, 2 | W |

### B.13 Death as God's judgement (faces D04, D20)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-87 | **Judgement where the verse names the inner cause.** "But Er, Judah's firstborn, was wicked in the sight of the Lord, and the Lord put him to death"; "the anger of the Lord was kindled against Uzzah, and God struck him down there because of his error"; "So Saul died for his breach of faith. He broke faith with the Lord"; "He made a path for his anger; he did not spare them from death"; "the men who brought up a bad report of the land— died by plague before the Lord" | Gen 38:7; 2Sa 6:7; 1Ch 10:13; Psa 78:50; Num 14:37 | S | **13** | W |
| LD-88 | **The second death.** "But as for the cowardly, the faithless, the detestable, as for murderers, the sexually immoral, sorcerers, idolaters, and all liars, their portion will be in the lake that burns with fire and sulfur, which is the second death"; "The one who conquers will not be hurt by the second death"; "Then Death and Hades were thrown into the lake of fire. This is the second death, the lake of fire"; "For their worm shall not die, their fire shall not be quenched" | Rev 21:8; 2:11; 20:14; Isa 66:24 | S | **2 "Life, and judgment"**, 13, 10.1 ("the cowardly") | W |

### B.14 The dead inquired of (face D09)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-89 | **Turning to the dead instead of God.** "should not a people inquire of their God? Should they inquire of the dead on behalf of the living?"; "or a medium or a necromancer or one who inquires of the dead"; "they yoked themselves to the Baal of Peor, and ate sacrifices offered to the dead". And kindness that reaches the dead: "May he be blessed by the Lord, whose kindness has not forsaken the living or the dead!" | Isa 8:19; Deu 18:11; Psa 106:28; Rut 2:20 | S | 10.9, 10.10 | W |

### B.15 Choices made in the face of death

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-90 | **Esau.** "I am about to die; of what use is a birthright to me?" | Gen 25:32 | S | 10.6, 10.7 | W |
| LD-91 | **Remaining data.** Notices, genealogies, reigns and burials (D01). Legal sentences (D02). Killings, plots, executions and suicides (D03, except the inner-being cases above). Judgement by sword, famine and pestilence (D04, except LD-87). The sanctuary statutes (D05, except LD-68). Survival in famine and siege (D06). Uncleanness from the dead (D26). Animals, plants, objects and idiom (D27) | faces D01–D06, D26, D27 | S | — | D |

---

## C. Change of character: what differs between the faces (#1919, for Ch 11 §4)

- **"Die" and "death" (H4191, H4194, G0599, G2288)** move between:
  - the body's end ("and he died", Gen 5)
  - a sentence passed by people ("shall surely be put to death", Lev 20)
  - a judgement from God (Gen 38:7; 2Sa 6:7)
  - the end of a way taken ("its end is the way to death", Pro 14:12)
  - something that happens inside a living person ("sin came alive and I died", Rom 7:9; "abides in death", 1Jo 3:14; Nabal's heart, 1Sa 25:37)
  - a power that reigns, holds and is destroyed (Rom 5:14; Act 2:24; 1Cor 15:26)
  - a death undergone on purpose ("died to sin", Rom 6:2; "I died to the law", Gal 2:19)
  - a death that belongs to the Lord ("if we die, we die to the Lord", Rom 14:8)

  **What differs is what produces the death and who acts in it.** The verses name sin (Rom 5:12; Jam 1:15), vexation and jealousy (Job 5:2), the sluggard's desire (Pro 21:25), God (Deu 32:39) and Christ, who "tastes death for everyone" (Heb 2:9). The word stays the same. *(R: the grouping is mine; each verse names its own cause.)*
- **"Put to death" (H4191 hiphil, G3499)** is used of executing a person (Num 35) and of "what is earthly in you" (Col 3:5). The same Greek root gives a body "as good as dead" (Rom 4:19; Heb 11:12). *(R: noted as the range of the word. No verse sets these side by side.)*
- **"Dead" as a measure of worth:** "a dead dog such as I" (2Sa 9:8) is said of oneself in lowliness. "this dead dog" (2Sa 16:9) is said of another in contempt.
- **Death and sleep:** Jesus calls death sleep, and the hearers mishear it ("they thought that he meant taking rest in sleep", Joh 11:13).
- **The dead and praise:** "The dead do not praise the Lord" (Psa 115:17) and "Blessed are the dead who die in the Lord" (Rev 14:13) stand in different books and settings. The narrative is to set them side by side without reconciling them (LD-46, LD-47).

## D. The researcher's questions: what unit 2 shows

- **Q1 What is death?** (OT-02, main source.) The verses give:
  - the common lot: "We must all die; we are like water spilled on the ground" (2Sa 14:14); "it is appointed for man to die once, and after that comes judgment" (Heb 9:27)
  - its entry through sin: "death through sin, and so death spread to all men because all sinned" (Rom 5:12); "the wages of sin is death" (Rom 6:23)
  - the warning and its denial: "you shall surely die" (Gen 2:17); "You will not surely die" (Gen 3:4)
  - sleep: "not dead but sleeping" (Mat 9:24)
  - a power that holds and is overthrown: "not possible for him to be held by it" (Act 2:24); "the last enemy to be destroyed is death" (1Cor 15:26)
  - death in the living: "Whoever does not love abides in death" (1Jo 3:14)
  - the dead seen from this side: "the dead know nothing" (Ecc 9:5), "where is he?" (Job 14:10)
  - the dead with God: "carried by the angels to Abraham's side" (Luk 16:22); "they may rest from their labors" (Rev 14:13)
- **Q2 Spirit and soul at death** (OT-03, touched):
  - "he poured out his soul to death" (Isa 53:12)
  - "My soul is very sorrowful, even to death" (Mat 26:38)
  - "carried by the angels" (Luk 16:22), with no inner word named
  - "to die is gain" (Phili 1:21)
  - against these, "the dead know nothing" (Ecc 9:5) and "the dead do not praise" (Psa 115:17)
  - These name no destination for spirit or soul. **The focused pull for Q2 is still needed.**
- **Q3 The heart after death** (OT-04, touched):
  - The heart *before* death: "My heart is in anguish within me; the terrors of death have fallen upon me" (Psa 55:4); "my heart is wrung within me … in the house it is like death" (Lam 1:20); "breaking my heart" (Act 21:13).
  - The heart in the living, before going to the dead: "madness is in their hearts while they live, and after that they go to the dead" (Ecc 9:3).
  - **Unit 2 has no verse on the heart after death.** The focused pull is still needed.
- **Q4 The body** (OT-05): only the corruption verses (LD-76). Act 13:36–37 adds David seeing corruption and the one God raised up not seeing it. The rest was done in the Q4 pull (#1938).
- **OT-08 (what life and death are set against):** in this unit, death is set against life by God (Deu 30:15; Jer 21:8), by the way a person walks (Pro 12:28), by the tongue (Pro 18:21), by the mind (Rom 8:6) and by love (1Jo 3:14).

## E. Already in the chapters (pointer only)

- **Ch 2** already has: Psa 104:29; 1Ki 17:17; 1Ki 2:2; Gen 25:8; Psa 89:48; Zec 1:5; Gen 3:22; Job 14:14; Col 2:13; Eph 2:5; 1Ki 19:4; Jon 4:3, 9; Job 7:15–16; 2Sa 1:9; Exo 16:3; Num 21:8; Judg 16:30; Gen 35:18; 1Sa 4:20; 1Sa 25:37–38; Psa 31:12; Psa 116:3–9; 56:13; 16:10; 118:17; Eze 18 and 33; Joh 5:24; Rom 6:4; Col 3:3; Joh 11:25; 1Cor 15:21–22, 54–55; Isa 25:8; Luk 20:36; Rev 21:4.
- **Elsewhere:** Mat 26:38 (Ch 5, 7); Rom 8:6 (Ch 7); Heb 5:7 (Ch 7); Judg 16:16 (Ch 5); Pro 8:36 (Ch 5, 12); Eze 18:4 (Ch 5, 9, 12); Eze 18:31 (Ch 14); Isa 28:15 (10.11); 2Sa 18:33 (10.1, 11); 2Sa 14:14 (10.4).

Chapter numbers are the current ones (the file number is the chapter number: Ch 5 the soul, Ch 7 flesh).

## F. Proposed weave (after approval)

**Ch 2 (main):**
- **"What death is"**, widened with three short sub-sections, in the way "The body raised" was given sub-sections in the Q4 weave:
  - *The lot of all* (LD-43 to LD-45, LD-48, LD-49)
  - *Through sin* (LD-51 to LD-54, with LD-55 quoted and stopped)
  - *Death in the living* (LD-57, LD-58, added to the two existing bullets)
- **NS "Facing death"**, placed before "Wanting to die" (LD-64 to LD-66). Pointer to 10.1.
- **RS "Wanting to die"**: add LD-69 and LD-70, and **restate the two claims** in LD-70:
  - "Only twice is the wish granted" becomes: where the wish is granted (Samson, Saul, Abimelech), it is at the end of a life already lost
  - "the wish belongs almost always to the soul" becomes: in the words of Elijah, Jonah, Saul, Samson and Job the Hebrew is *nephesh*; most other wishes name no inner word
- **"Delivered from death"**: add LD-61 and LD-73.
- **"Made alive"**: add LD-75 and LD-77 (short), and a pointer for LD-79 to Ch 14.
- **NS "Dying to the Lord"**, after "Made alive" (LD-71, LD-80, LD-81). This is the counterpart of "Life asked for": what is asked before dying, and a death that belongs to the Lord.
- **"The body raised"**:
  - "Christ first": add LD-76
  - "Changed": add LD-62 and LD-74
  - "Life, and judgment": add LD-88
- **"After death"**: **RS**. Set LD-46 (the dead seen from this side) beside LD-47 (the dead with God), unreconciled.
- **"Life set before a person"**: **RS**, adding the death side (LD-82).

**Elsewhere:**
- **10.1 Feeling:**
  - "Fear": LD-64 (Heb 2:15), LD-67
  - grief: LD-86
  - "Where it turns": LD-83 (vexation, jealousy)
  - pointer to LD-88 ("the cowardly")
- **10.3:** LD-56 (sin brought to remembrance)
- **10.4:** LD-60 (he "considered his own body"), LD-68 (Manoah's wife's reasoning)
- **10.5:** LD-51 (the serpent's denial), LD-82 (Pro 18:21)
- **10.6:** LD-53 (desire conceives), LD-63 (greed like death, love as strong as death), LD-70 (Rachel), LD-83 (the sluggard's desire), LD-90 (Esau), LD-79 (Col 3:5)
- **10.7:** LD-78, LD-82, LD-90
- **10.9:** LD-55 (asking for a brother), LD-66, LD-68, LD-89
- **10.10:** LD-59, LD-72, LD-73 (Jam 5:20), LD-75 (1Jo 3:14), LD-78, LD-84, LD-89
- **10.11:** LD-67 (Gen 26:9)
- **11 §4:** §C
- **12:** LD-52, LD-53, LD-57, LD-83
- **13:** LD-56, LD-87, LD-88
- **14:** LD-77, LD-79

**Held:** none proposed. **Data:** LD-50, LD-85, LD-91.

**Decision for the researcher:**
- LD-46 and LD-47 are proposed **side by side** in Ch 2 "After death", unreconciled, the way Luk 24:39 and 1Cor 15:50 already stand. The other choice is to **hold** them in the register (OT-03) until the Q2 focused pull is done.

**Register at approval:**
- OT-02: touched (LD-43 to LD-58, LD-61 to LD-62)
- OT-03: touched (LD-46, LD-47, LD-65)
- OT-04: touched (LD-65; no answer)
- OT-05: touched (LD-76)
- OT-08: touched (§D)
- No new thread, unless LD-46 and LD-47 are held.

## G. Quote check

Run: `../../Clusters/M01 - fear-awe/fear-quote-check-v1-20261001.py life-death-observation-ledger-unit2-v1-20261002.md`. Result 2026-10-02: **213 quotes checked in table rows. One flag, and it is not a failure.** Jude 12 is cited without a chapter ("Jude 12"), so the checker cannot read the reference. The quote "fruitless trees in late autumn, twice dead, uprooted" was checked by hand against iba.db `verse` 'Jude 12', and it matches.

---

## Woven — where (2026-10-03, #1939)

The researcher approved this, verbatim: *"proceed to weave in"*. That approved the weave in §F as proposed, including LD-46 and LD-47 side by side.

| LD | Woven in |
| --- | --- |
| LD-43–LD-45, LD-48, LD-49 | Ch 2 "What death is" (the common lot, the manner, the day, sleep) |
| LD-46, LD-47 | Ch 2 "After death" (side by side, unreconciled) |
| LD-51–LD-55 | Ch 2 "What death is" › *Death and sin*; 10.5 (Gen 3:4); 10.6 (Jam 1:15); 10.9 (1Jo 5:16); Ch 12 (Jam 1:15) |
| LD-56 | Ch 2 *Death and sin* (2Sa 12:13–14); 10.3 (1Ki 17:18, 20); Ch 13 (pointer) |
| LD-57, LD-58 | Ch 2 › *Death in the living*; Ch 12 (1Jo 3:14) |
| LD-59 | 10.10; Ch 11 §4 |
| LD-60 | 10.4 |
| LD-61, LD-73 | Ch 2 "Delivered from death"; 10.10 (Jam 5:20) |
| LD-62, LD-74 | Ch 2 "Christ first" (Act 2:24), "Changed" |
| LD-63 | 10.6 |
| LD-64–LD-67 | Ch 2 "Facing death"; 10.1 (Heb 2:14–15); 10.9 (2Cor 1:9); 10.11 (Gen 26:9) |
| LD-68 | 10.9; 10.4 |
| LD-69, LD-70 | Ch 2 "Wanting to die" (two claims restated); 10.6 (Gen 30:1) |
| LD-71, LD-80, LD-81 | Ch 2 "Dying to the Lord" |
| LD-72 | 10.10; Ch 2 "Dying to the Lord" (Rut 1:17) |
| LD-75, LD-77 | Ch 2 "Made alive"; 10.10 (1Jo 3:14); Ch 14 (Rom 5:10; 2Cor 5:15) |
| LD-76 | Ch 2 "Christ first" |
| LD-78 | Ch 2 "Made alive" (2Cor 5:15); 10.7; 10.10 (Rom 14:15) |
| LD-79 | Ch 14; Ch 2 "Made alive" (Rom 6:2; Col 3:5); 10.6 (Col 3:5) |
| LD-82, LD-83 | Ch 2 "Life set before a person"; 10.1 (Job 5:2); 10.5 (Pro 18:21); 10.6 (Pro 21:25); 10.7; Ch 12 (Job 5:2) |
| LD-84 | 10.10 |
| LD-86 | 10.1 |
| LD-87 | Ch 13 "Reading the ruin" |
| LD-88 | Ch 2 "Life, and judgment"; 10.1; Ch 13 |
| LD-89 | 10.9 (Isa 8:19); 10.10 (Rut 2:20) |
| LD-90 | 10.6; 10.7 |
| §C | Ch 11 §4 "What brings it about, and who acts" |
| LD-50, LD-85, LD-91 | data |

**Not carried:**
- **LD-44, Ch 5 pointer.** "bitterness of soul" (Job 21:25) is in Ch 2. Ch 5 already has bitterness of soul from other verses, so no pointer was added.
- **LD-54:** the Deu 24:16 and 2Ch 25:4 parallels stay in the data, because 2Ki 14:6 carries the line.

**New quotes:** checked against iba.db `verse` (`--prose`). All new verse quotes pass. The only new flags are section titles in quotation marks. **Claim register:** v10. **Linkage map:** updated. **Register:** OT-02 to OT-05 updated.
