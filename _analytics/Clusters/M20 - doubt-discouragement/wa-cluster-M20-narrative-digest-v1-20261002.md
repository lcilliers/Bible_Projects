# M20 Doubt & Discouragement — digest into the narrative (v1)

**Date:** 2026-10-02 · **Author:** Claude Code · **Status:** **approved and woven** (researcher, verbatim 2026-10-02: *"ns-d1: select A; I reviewed the edited files, looks good."*). 10.11 created from §4. The second pass in §5 is done; see the index Structure log. Earlier status: for researcher review. Escalation #1931. Nothing has been written to the DB.
**Source (not re-derived):** `wa-cluster-M20-phenomena-v3-20260928.md` (this folder; approved under #1885), its ledger `wa-cluster-M20-phenomena-ledger-v1-20260928.csv`, and the seat map in v3 §20.
**Researcher direction (verbatim, 2026-10-02, #1931):** *"do a session close and commit, then clear, and then we will proceed with digesting m20 in the same way. M20 was already analysed, so first check the folder."* And this session: *"proceed with M20 - similar to the previous session. read the m20 folder for the previous analysis"*.
**Method:** as the fear rework (#1930) and the CLAUDE.md banner "Weaving carries meaning, not lists". Each phenomenon gets **one coherent account** in the activity it belongs to: what Scripture says it is, its forms from the words themselves, why they differ, and how it is met. Other sections carry only what belongs to them, and point back. Full verse lists stay in v3 and its ledger.

## 1. What was done in this pass

Four chapter files were written, each with one or more accounts. Prior versions are in `archive/`.

| Chapter | New version | Accounts added |
|---|---|---|
| 10.1 Feeling | v7 | **Anxiety** (the words; what it does; care that is good; meeting anxiety); **Losing heart** |
| 10.2 Knowing and hearing | v6 | **Perplexity**; **Understanding that is hidden**; **Doubt** |
| 10.5 Speaking | v7 | **Grumbling**; **Whispering** |
| 10.9 Relating to God | v8 | **When God hides his face** |

Checks done:
- **Quote check:** `fear-quote-check-v1-20261001.py --prose` on all four. 10.1: 182 quotes, 0 failures. 10.2: 62, 0. 10.9: 127, 0. 10.5: 83, 1 flag. The flag is the two-verse quote of Psalm 106:24–25, which the checker does not join; it was checked by hand and matches the ESV. The draft in §4 below: 0 failures. The checker's other 5 flags in this file are section titles and working-file phrases, not quotations.
- **Counted, not assumed:**
  - "used five times" (losing heart). *kāʾāh* has 3 verses, *kāʾeh* 1 and *athumeō* 1 in iba.db `verse_lexical`.
  - "Where the verses tell a person not to be anxious, they never leave it there." Checked against all 9 commands in the set: Mat 6:25, 31, 34; Luk 12:22, 29; Mat 10:19; Luk 12:11; Phili 4:6; 1Pe 5:7.
  - "In several of these scenes" (perplexity). It ends with someone arriving in 5 of the 11 verses: Luk 24:4; Act 5:24–25; Act 2:14; Act 10:17–19; Dan 5:12.
- **Let-Scripture-speak cuts made while writing:**
  - "What the perplexed lacked, the one who came had." This joined five scenes into one rule, and was cut.
  - "out of the leaders' hearing" ("in your tents"). No verse says it, and it was cut.
  - "it reaches every part of him" (the hidden face). It became the four places the verses name.
  - "The verses never tell an anxious person simply to stop." This was uncounted, and was restated as the counted sentence above.
- **Marked "I read":** one place, in 10.2: doubt as a different thing from perplexity.
- **No project terms** in the chapter text. "Seat" was found in a draft line in 10.2 and taken out.

## 2. Placement of every phenomenon

Codes and section numbers are those of v3.

| v3 § | Phenomenon | Verses | Account | Carried elsewhere | State |
|---|---|---|---|---|---|
| 11 | Anxiety and care (AX) | 40 | **10.1 "Anxiety"**. All eight strands are used: provision (a), speaking under trial (b), divided care (c), care for others (d), cares that choke (e), handed over (f), dread of a coming harm (g), and anxiety eaten (h, pointer to Ch 13) | 10.1 "When feeling changes character" (new bullet); Ch 11 §4 (2nd pass) | **woven** |
| 12 | Losing heart (LH) | 5 | **10.1 "Losing heart"**. All five verses | 10.10 (2nd pass: done to a person by another) | **woven** |
| 9 | Perplexity (PX) | 11 | **10.2 "Perplexity"**. All 11 verses are cited or covered | Ch 15 already cites Act 10:17 | **woven** |
| 8 | Understanding closed from outside (UC) | 13 | **10.2 "Understanding that is hidden"** | — | **woven** |
| 10 | Doubt: the divided soul (DB) | 4 | **10.2 "Doubt"**. All four verses, with Luk 24:38 pointing to 10.4 | 10.9 Connections | **woven** |
| 13 | Grumbling (GR) | 17 | **10.5 "Grumbling"** | Ch 12 (2nd pass?); Ch 14 (Isa 29:24, 2nd pass) | **woven** |
| 14 | Whispering (WH) | 4 | **10.5 "Whispering"** | 10.10 (2nd pass: separates friends) | **woven** |
| 5 | God's face hidden, as the human bears it (FH) | 31 | **10.9 "When God hides his face"** | Ch 13 (Isa 54:8 is already there through anger); Ch 12 (Psa 10:11 already there) | **woven** |
| 1 | Hiding from God's presence (HG) | 7 | **Proposed: 10.11 "Hiding and disclosing"** (§3 below) | — | **woven (10.11)** |
| 2 | Hiding oneself from human danger (HS) | 40 | as above | 10.10 (2nd pass) | **woven (10.11)** |
| 3 | Being hidden by another: shelter (SH) | 23 | as above | Ch 13 (Isa 26:20 already there); Ch 14 (Col 3:3, 2nd pass) | **woven (10.11)** |
| 4 | Longing to be hidden (HW) | 3 | as above | 10.3 (Job 14:13 already there) | **woven (10.11)** |
| 6 | Nothing is hidden: exposure before God (EX) | 11 | as above | Ch 3 "The heart is hidden, and God sees it" (2nd pass) | **woven (10.11)** |
| 7 | Concealing and disclosing what one holds (CD) | 29 | as above | 10.5 already has 1Sa 3:15–18 and Job 31:33–34 | **woven (10.11)** |
| 15 | The hidden trap (TR) | 9 | as above | Ch 12 (the heart hides intent; 2nd pass) | **woven (10.11)** |
| 16 | The sluggard's buried hand (SL) | 2 | as above (one line, under the word *ṭāman*) | — | **woven (10.11)** |
| 17 | No inner phenomenon (NO) | 26 | none, by design. A verse that says nothing about the inner being stays in the data (#1930) | — | **stays in data** |

**Reverse audit (style guide §8.1).** Every phenomenon §1–§16 has a placement, and the woven ones carry their key verses. 10.1, 10.2, 10.5 and 10.9 do **not** reproduce v3's seat blocks. Where a seat block says something about the inner being, it is carried as a verse in the account, for example Psa 13:2, 102:4, 69:20, 51:10–11, 27:8 and Dan 11:28. The seat analysis itself stays in v3.

## 3. Structure proposal NS-D1: where hiding belongs

**The problem.** Hiding and concealing make up about 180 of M20's 275 verses (v3 §1–§8, §15–§16). They describe the whole person taking himself, or something he holds, out of sight. Part 10 has no activity section where that belongs.
- Splitting it would break the account into pieces: hiding from God would go to 10.9, hiding from people to 10.10, concealing in speech to 10.5, and concealing wrong to 12. That runs against "one coherent account per phenomenon" (#1930).
- By the weave rule (#1918), "does not fit" means the structure changes.

**Options:**

| | Option | For | Against |
|---|---|---|---|
| **A** | **New 10.11 "Hiding and disclosing"**, after Relating to others | One account in one place. Its parts face both God and others, so it follows 10.9 and 10.10 naturally. No renumbering. | Part 10 grows by one file |
| B | New section placed after 10.5 Speaking, with 10.6–10.10 renumbered to 10.7–10.11 | Puts it next to the disclosure-in-speech material | Renumbering last time touched 53 cross-references (#1920) |
| C | Split by party: 10.9, 10.10, 10.5 and Ch 12 | No new file | Breaks the account into pieces, which is what #1930 ruled against |

**Recommendation: A.** The other sections then carry only what belongs to them, and point to 10.11.

## 4. Draft account for 10.11 "Hiding and disclosing" (for review, not yet placed)

*Written to the chapter standard. Quotes checked against the ESV (see §1). On approval of NS-D1 it becomes `10-11-hiding-and-disclosing-v1-{date}.md`, and the pointers in §2 are added.*

---

The first thing the man and woman did after they ate was hide. "They heard the sound of the Lord God walking in the garden in the cool of the day, and the man and his wife hid themselves from the presence of the Lord God among the trees of the garden" (Genesis 3:8). Asked where he was, Adam gave the reason: "I heard the sound of you in the garden, and I was afraid, because I was naked, and I hid myself" (3:10). From then on, hiding runs through Scripture. People hide themselves, hide others, hide things, hide what they have done, and hide what they mean.

### The words

The Hebrew has several words for hiding, and each is used mostly for its own kind of hiding.
- ***Ḥāvāʾ*, "to hide oneself".** A person takes his own body out of sight. Adam (Genesis 3:10). Israel under the Philistines "hid themselves in caves and in holes and in rocks and in tombs and in cisterns" (1 Samuel 13:6). Saul on the day he was made king: "he has hidden himself among the baggage" (1 Samuel 10:22).
- ***Ṭāman*, "to hide, bury".** A thing is put into or under something. Achan's plunder is "hidden in the earth inside my tent" (Joshua 7:21). Moses "hid him in the sand" (Exodus 2:12). An enemy's net is hidden in the path (Psalm 140:5). It is also the word for the sluggard who "buries his hand in the dish and will not even bring it back to his mouth" (Proverbs 19:24).
- ***Kāḥad*, "to hide, withhold".** Something known or done is kept back. "Tell me now what you have done; do not hide it from me" (Joshua 7:19). "Do not hide it from me" (1 Samuel 3:17). The same word also means to be cut off: "you would have been cut off from the earth" (Exodus 9:15).
- ***Sātar*, "to hide, conceal".** This is the widest of them. It is used of hiding from danger, of hiding someone else to keep him safe, of things hidden from understanding (10.2), and of God hiding his face (10.9).
- The Greek ***kruptō***, "to hide", covers all of these.

### Hiding from God

In each scene where a person hides from God, something of God is perceived first: a sound (Genesis 3:10), God naming himself (Exodus 3:6), "the terror of the Lord, and … the splendor of his majesty" (Isaiah 2:10), "the face of him who is seated on the throne, and … the wrath of the Lamb" (Revelation 6:16).
- Adam hid because he knew he was naked (Genesis 3:10).
- Moses "hid his face, for he was afraid to look at God" (Exodus 3:6), and no wrong is named.
- At the end, people call "to the mountains and rocks, 'Fall on us and hide us'", for "who can stand?" (Revelation 6:16–17).

Job names the one condition on which he will not hide: "Only grant me two things, then I will not hide myself from your face: withdraw your hand far from me, and let not dread of you terrify me" (Job 13:20–21). In his words, it is the dread that makes a person hide.

None of it works. "Can a man hide himself in secret places so that I cannot see him? declares the Lord. Do I not fill heaven and earth?" (Jeremiah 23:24). "There is no gloom or deep darkness where evildoers may hide themselves" (Job 34:22). Isaiah names what the attempt does: "Ah, you who hide deep from the Lord your counsel … and who say, 'Who sees us? Who knows us?' You turn things upside down! Shall the potter be regarded as the clay" (Isaiah 29:15–16).

That nothing is hidden from God is the same fact for everyone, and it falls very differently.
- For the one who suffers it is comfort: "O Lord, all my longing is before you; my sighing is not hidden from you" (Psalm 38:9).
- For the one being made it is wonder: "My frame was not hidden from you, when I was being made in secret" (Psalm 139:15), and the psalmist answers, "my soul knows it very well" (139:14).
- For the one who has done wrong it is judgement: "I know Ephraim, and Israel is not hidden from me; for now, O Ephraim, you have played the whore" (Hosea 5:3).

### Hiding from people

Much of the hiding in Scripture is from people who could do harm, and in these verses it is the weaker side that hides. "When the wicked rise, people hide themselves" (Proverbs 28:28). "The poor of the earth all hide themselves" (Job 24:4). When Israel hid in the caves, "all the people followed him trembling" (1 Samuel 13:7).

Often the verse records not the feeling of the one who hides but someone else's counsel to hide.
- Jonathan: "Saul my father seeks to kill you … Stay in a secret place and hide yourself" (1 Samuel 19:2).
- God to Elijah: "hide yourself by the brook Cherith" (1 Kings 17:3).

Where the feeling is named, it is fear.
- Jacob fled from Laban "secretly", and he said why: "Because I was afraid" (Genesis 31:27, 31).
- Joseph of Arimathea was "a disciple of Jesus, but secretly for fear of the Jews". The same verse ends with him going to Pilate and taking away the body (John 19:38).

Hiding can be good sense: "The prudent sees danger and hides himself, but the simple go on and suffer for it" (Proverbs 22:3). It ends when the news changes. The men who had hidden in the hills "heard that the Philistines were fleeing, they too followed hard after them in the battle" (1 Samuel 14:22).

And sometimes hiding is refused, or impossible.
- The servant chooses not to hide: "I gave my back to those who strike … I hid not my face from disgrace and spitting" (Isaiah 50:6).
- No one can hide from a friend who turns: "it is not an adversary who deals insolently with me — then I could hide from him. But it is you, a man, my equal, my companion, my familiar friend" (Psalm 55:12–13).

### Hiding another

To hide someone else is to keep him alive, and the verses say what moved the one who did it.
- **Rahab** hid the spies, and gave her reason: "as soon as we heard it, our hearts melted … for the Lord your God, he is God in the heavens above and on the earth beneath" (Joshua 2:11). All Jericho's hearts melted. It was her confession that turned her to hide them.
- **Obadiah** "took a hundred prophets and hid them by fifties in a cave and fed them with bread and water" (1 Kings 18:4).
- **Moses's parents** hid him "because they saw that the child was beautiful, and they were not afraid of the king's edict" (Hebrews 11:23).

God hides people too, and those he hides ask for it.
- "Hide me in the shadow of your wings" (Psalm 17:8).
- "You hide them from the plots of men; you store them in your shelter from the strife of tongues" (Psalm 31:20).
- The servant is hidden to be used later: "in the shadow of his hand he hid me; he made me a polished arrow; in his quiver he hid me away" (Isaiah 49:2).
- At the last, a life is hidden in someone: "your life is hidden with Christ in God" (Colossians 3:3).

There is a false shelter too: "we have made lies our refuge, and in falsehood we have taken shelter" (Isaiah 28:15).

### Hiding what I hold

A person can hide what he has done. Achan tells it in order: "when I saw … then I coveted them and took them. And see, they are hidden in the earth inside my tent" (Joshua 7:21). Joshua had to ask him first: "do not hide it from me" (7:19).

What happens next differs.
- **It fails, and fear follows.** Moses "struck down the Egyptian and hid him in the sand" (Exodus 2:12). When it came out, "Moses was afraid, and thought, 'Surely the thing is known'" (2:14).
- **Conscience turns it round.** The lepers hid the plunder, and then "said to one another, 'We are not doing right. This day is a day of good news. If we are silent … punishment will overtake us'" (2 Kings 7:8–9).
- **It can be kept because it is enjoyed.** "Though evil is sweet in his mouth, though he hides it under his tongue, though he is loath to let it go" (Job 20:12–13).
- **It can be not hidden at all.** "They proclaim their sin like Sodom; they do not hide it. Woe to them! For they have brought evil on themselves" (Isaiah 3:9).

What God has done is not to be hidden. "I have not concealed your steadfast love and your faithfulness from the great congregation" (Psalm 40:10). "We will not hide them from their children, but tell to the coming generation the glorious deeds of the Lord" (Psalm 78:4). In his pain, Job's comfort is that "I have not denied the words of the Holy One" (Job 6:10). Some things cannot be hidden: "A city set on a hill cannot be hidden" (Matthew 5:14). And a hidden good is worth less than a visible one: "Better is open rebuke than hidden love" (Proverbs 27:5).

Two men in Jesus's parables hide something in the ground, and they hide it for different reasons. One finds "treasure hidden in a field, which a man found and covered up. Then in his joy he goes and sells all that he has" (Matthew 13:44). The other says, "I was afraid, and I went and hid your talent in the ground" (Matthew 25:25). One hid it in joy, the other in fear.

### The hidden trap

In the Psalms a purpose is hidden in order to catch someone. "They hold fast to their evil purpose; they talk of laying snares secretly, thinking, 'Who can see them?'" (Psalm 64:5). The next verse says where the purpose was hidden first: "For the inward mind and heart of a man are deep" (64:6).

The one it is set for prays out of his weakness. "When my spirit faints within me, you know my way! In the path where I walk they have hidden a trap for me" (Psalm 142:3). "No one cares for my soul" (142:4). It is worse when it comes from those he had prayed for: "Yet they have dug a pit for my life. Remember how I stood before you to speak good for them" (Jeremiah 18:20).

And the trap turns. "In the net that they hid, their own foot has been caught" (Psalm 9:15). The soul the pit was dug for (Psalm 35:7) is the soul that rejoices: "Then my soul will rejoice in the Lord" (35:9). The one taken "out of the net they have hidden for me" says, "Into your hand I commit my spirit" (Psalm 31:4–5).

### Longing to be hidden

Job in his pain wishes he had been hidden from life itself, cursing the night that did not "hide trouble from my eyes" (Job 3:10). Later the same wish becomes a hope: "Oh that you would hide me in Sheol, that you would conceal me until your wrath be past, that you would appoint me a set time, and remember me!" (Job 14:13; section 10.3).

### What changes it

The same act of hiding can be fear, good sense, care for another, or joy, depending on a few things the verses name.
- **Who hides whom.** God hiding a person is safety. God hiding his face from a person is dismay. The two are four verses apart in one psalm (Psalm 27:5, 9; 10.9).
- **What is hidden, and why.** A treasure in joy, a talent in fear (Matthew 13:44; 25:25).
- **Where the fear stands.** It comes before the hiding (Genesis 3:10; Matthew 25:25) or after it fails (Exodus 2:14). Those who hide another are, in one verse, "not afraid" (Hebrews 11:23).
- **Whether there is anywhere to hide.** From an enemy, yes. From a friend, no (Psalm 55:12–13). From God, never (Jeremiah 23:24).

---

## 5. Second pass (after review)

These follow once the researcher has read 10.1, 10.2, 10.5 and 10.9 in context and ruled on NS-D1. That is the same order as #1930.
- **Ch 11 §4**: faces and factors.
  - *merimnaō*: care for self or for others
  - *dāʾag*: dread, a father's anxiety for his son, sorrow for sin
  - *sātar*: shelter or hidden face
  - *rāgan*: murmuring or whispering
  - hiding: joy or fear
- **10.10**: losing heart done by another; whispering separates friends; hiding from people (pointer).
- **Ch 12**: the hidden trap and the deep heart (Psa 64:6; 140:2); concealed wrong.
- **Ch 3**: "The heart is hidden, and God sees it", pointing to 10.11.
- **Ch 14**: Isa 29:24 (murmurers accept instruction); Col 3:3; Eze 39:29.
- **Ch 15**: check the existing perplexity and whisperer lines against the new accounts.
- **10.0**: add 10.11 to the activity map, if NS-D1 is approved.
- **Index and claim register**: done in this pass for the four chapters (see the index Structure log and claim register v6).

## 6. External parties (style guide §7a)

| Account | Parties, as the verses give them |
|---|---|
| Anxiety | God (feeds, knows, cares, gives peace, searches); the Spirit (speaks through, teaches); riches and pleasures (choke the word); other people (the churches, the father's son); drought (Jer 17:8) |
| Losing heart | a father, false prophets, an oppressor, a persecutor, ships of Kittim. In every case it is someone or something else |
| Perplexity | messengers, Peter, the Spirit, the queen and Daniel: whoever arrives |
| Understanding hidden | God hides and reveals (Mat 11:25; Isa 29:14) |
| Doubt | the wind (seen); Jesus (rescues, asks) |
| Grumbling | Moses and Aaron (re-aim it at God); the spies (their report); God (provides, judges, gives a sign) |
| Whispering | the hearer, who takes the words in like food |
| Hidden face | God, who hides and does not hide; enemies; comforters who are absent; God's Spirit poured out (Eze 39:29) |
| Hiding (draft) | God (seen, sees, shelters); enemies and kings; counsellors (Jonathan, God); the one hidden by another; a friend |
