"""OT-07.3 weave (#2160): 10.13 v12 -> v13, 10.12 v14 -> v15, 10.10 v32 -> v33, Ch 2 v27 -> v28,
Ch 12 v25 -> v26.

Researcher, chat 2026-10-19 (verbatim): "OT-07.3: weave as proposed in section 3 (the Judg 14:19
correction, 2Ki 3:27, Anger in the body, the other placements), then read OT-98.2 and OT-98.3."
Proposal: section 3 of ot-07-3-anger-ledger-m-reading-v1-20261019.md. Each edit replaces an exact
block; the script stops if a block is not found exactly once. Old versions are moved to archive/.
"""
import pathlib
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8")
D = pathlib.Path(__file__).resolve().parents[3] / "_analytics/essay/spirit_soul_body/inner-being-narrative"


def edit(old_name, new_name, pairs):
    src = D / old_name
    text = src.read_text(encoding="utf-8")
    for old, new in pairs:
        n = text.count(old)
        if n != 1:
            sys.exit(f"{old_name}: block found {n} times: {old[:70]!r}")
        text = text.replace(old, new)
    (D / new_name).write_text(text, encoding="utf-8")
    shutil.move(str(src), str(D / "archive" / old_name))
    print(f"{old_name} -> {new_name}")


# ── 10.13 ─────────────────────────────────────────────────────────────────────────────────────
A_RISE_OLD = """- **Something within.** "What causes quarrels and what causes fights among you? Is it not this, that your passions are at war within you?" (James 4:1).
"""
A_RISE_NEW = """- **Being outwitted through someone close.** Samson's riddle was got out of him through his wife's tears (Judges 14:15–17; 10.10). When the men of the city answered it, he said, "If you had not plowed with my heifer, you would not have found out my riddle" (14:18). The Spirit rushed upon him for the striking at Ashkelon, and then, "In hot anger he went back to his father's house" (14:19). "And Samson's wife was given to his companion, who had been his best man" (14:20).
- **Something within.** "What causes quarrels and what causes fights among you? Is it not this, that your passions are at war within you?" (James 4:1).
"""
A_BODY_OLD = """Ahab, refused Naboth's vineyard, "lay down on his bed and turned away his face and would eat no food" (1 Kings 21:4).

### What it does next
"""
A_BODY_NEW = """Ahab, refused Naboth's vineyard, "lay down on his bed and turned away his face and would eat no food" (1 Kings 21:4).

### Anger in the body

Anger shows, and the verses see it in the teeth.
- "The wicked man sees it and is angry; he gnashes his teeth and melts away" (Psalm 112:10).
- "The wicked plots against the righteous and gnashes his teeth at him" (Psalm 37:12).
- At Stephen's speech, "they were enraged, and they ground their teeth at him" (Acts 7:54). The Greek of "enraged" is *sawn through in their hearts* (Chapter 4). The heart and the teeth are named in one sentence.
- Enemies gloat with it: "All your enemies rail against you; they hiss, they gnash their teeth, they cry: 'We have swallowed her!'" (Lamentations 2:16). Mockers do the same: "like profane mockers at a feast, they gnash at me with their teeth" (Psalm 35:16).
- Job says it of God's anger as he feels it: "He has torn me in his wrath and hated me; he has gnashed his teeth at me" (Job 16:9). It is how the anger looks to the one under it (*Living under God's anger*, below).

The face carries it too. *ʾAph*, anger's own Hebrew word, is also the nostril and the face (Chapter 11). Fear shows in the hands (10.12, *Fear in the body*). The weeping and gnashing of teeth at the judgment is in Chapter 2.

### What it does next
"""
A_SPIRIT_OLD = """The Spirit rushed upon Samson, and he went down to Ashkelon and struck down thirty men; after it, "In hot anger he went back to his father's house" (Judges 14:19)."""
A_SPIRIT_NEW = """When the Spirit rushed upon Samson, the verse joins it to the striking at Ashkelon; his hot anger afterwards has its ground in being outwitted through his wife (Judges 14:18–19; *What it rises at*, above)."""
A_SPOKEN_OLD = """- **In the New Testament,** it is revealed (Romans 1:18), stored up (Romans 2:5), it remains (John 3:36), and it is finished (Revelation 15:1).
"""
A_SPOKEN_NEW = """- **In the New Testament,** it is revealed (Romans 1:18), stored up (Romans 2:5), it remains (John 3:36), and it is finished (Revelation 15:1).
- **Once, with no bearer named.** At the siege, when the king of Moab "saw that the battle was going against him", he "took his oldest son who was to reign in his place and offered him for a burnt offering on the wall. And there came great wrath against Israel. And they withdrew from him and returned to their own land" (2 Kings 3:26–27). Elsewhere the same words, wrath coming upon a people, follow a breach, and once the wrath is then named "the wrath of the Lord" (2 Chronicles 32:25–26). Here no breach is named, and Elisha had said, "He will also give the Moabites into your hand" (3:18). I read the verse as leaving open whose wrath it was. The king gave up his own heir at the point of defeat, and the campaign ended short of the word.
"""
A_REV_OLD = """*Thymos* is God's wrath and Babylon's passion (Revelation 14:8, 10)."""
A_REV_NEW = """*Thymos* is God's wrath and Babylon's passion (Revelation 14:8, 10): "For all nations have drunk the wine of the passion of her sexual immorality" (18:3)."""
A_HELD_OLD = """- The verse with no source named for the wrath, "And there came great wrath against Israel" (2 Kings 3:27), is held.
"""
edit("10-13-anger-v12-20261018.md", "10-13-anger-v13-20261019.md", [
    (A_RISE_OLD, A_RISE_NEW), (A_BODY_OLD, A_BODY_NEW), (A_SPIRIT_OLD, A_SPIRIT_NEW),
    (A_SPOKEN_OLD, A_SPOKEN_NEW), (A_REV_OLD, A_REV_NEW), (A_HELD_OLD, "")])

# ── 10.12 Dread laid on others: Eze 21:15 ─────────────────────────────────────────────────────
F_OLD = """- "Put them in fear, O Lord! Let the nations know that they are but men!" (Psalm 9:20).
"""
F_NEW = """- "Put them in fear, O Lord! Let the nations know that they are but men!" (Psalm 9:20).
- "that their hearts may melt, and many stumble. At all their gates I have given the glittering sword" (Ezekiel 21:15). The melting heart is what the sword is given for (*Fear in the body*, above).
"""
edit("10-12-fear-v14-20261019.md", "10-12-fear-v15-20261019.md", [(F_OLD, F_NEW)])

# ── 10.10 Making others afraid: Samson's wife ─────────────────────────────────────────────────
R_OLD = """he does justice "so that man who is of the earth may strike terror no more" (Psalm 10:18).
"""
R_NEW = """he does justice "so that man who is of the earth may strike terror no more" (Psalm 10:18).

Fear can be passed on as pressure. At Samson's wedding the guests threatened his wife: "Entice your husband to tell us what the riddle is, lest we burn you and your father's house with fire" (Judges 14:15). She pressed him with tears and with a charge against his love: "You only hate me; you do not love me" (14:16). "She wept before him the seven days that their feast lasted, and on the seventh day he told her, because she pressed him hard" (14:17). I read the fear laid on her as becoming the weeping she laid on him. His anger at the end is in 10.13.
"""
edit("10-10-relating-to-others-v32-20261019.md", "10-10-relating-to-others-v33-20261019.md", [(R_OLD, R_NEW)])

# ── Ch 2 Life, and judgment: weeping and gnashing of teeth ────────────────────────────────────
L_OLD = """Christ Jesus "is to judge the living and the dead" (2 Timothy 4:1).
"""
L_NEW = """Christ Jesus "is to judge the living and the dead" (2 Timothy 4:1).

Jesus speaks of what the shut-out feel. "In that place there will be weeping and gnashing of teeth, when you see Abraham and Isaac and Jacob and all the prophets in the kingdom of God but you yourselves cast out" (Luke 13:28). The saying comes seven times (Matthew 8:12; 13:42, 50; 22:13; 24:51; 25:30; Luke 13:28). In Luke the weeping and gnashing come at a sight: others inside, oneself outside. I read the gnashing as standing with the weeping. The verses do not say whether it is anguish or rage (10.13, *Anger in the body*).
"""
edit("02-life-breath-and-death-v27-20261019.md", "02-life-breath-and-death-v28-20261019.md", [(L_OLD, L_NEW)])

# ── Ch 12: Num 20:13 beside Exo 17:7 ──────────────────────────────────────────────────────────
M_OLD = """The quarrel at Meribah is told in the wilderness story without naming any inner word (Exodus 17:7)."""
M_NEW = """The quarrel at Meribah is told in the wilderness story without naming any inner word (Exodus 17:7). The place keeps the name: "These are the waters of Meribah, where the people of Israel quarreled with the Lord, and through them he showed himself holy" (Numbers 20:13)."""
edit("12-when-the-inner-being-goes-wrong-v25-20261018.md", "12-when-the-inner-being-goes-wrong-v26-20261019.md", [(M_OLD, M_NEW)])
