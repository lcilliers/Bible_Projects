"""OT-98.2 weave (#2160): the 30 verses closed as data, read outward, placed in 16 chapters.

Researcher, chat 2026-10-19 (verbatim): "OT-98.2: weave as proposed in section 2; add 1Sa 25 and
2Ki 18-19 / Isa 36-37 as verse items for later strands; then close OT-98.2 and OT-98.10."
Proposal: section 2 of ot-98-2-data-verses-reading-v1-20261019.md.

Each block is appended at the END of its named section: before the next heading of the same or a
higher level, and before a '---' working-note block inside the section. The script stops if a
heading is not found exactly once. Each touched chapter gets the next version; old versions go to
archive/.
"""
import pathlib
import re
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8")
D = pathlib.Path(__file__).resolve().parents[3] / "_analytics/essay/spirit_soul_body/inner-being-narrative"


def add_end(text: str, heading: str, block: str) -> str:
    lines = text.split("\n")
    idx = [i for i, l in enumerate(lines) if l.strip() == heading]
    if len(idx) != 1:
        sys.exit(f"heading {heading!r} found {len(idx)} times")
    i = idx[0]
    level = len(heading) - len(heading.lstrip("#"))
    end = len(lines)
    for j in range(i + 1, len(lines)):
        m = re.match(r"^(#{1,6}) ", lines[j])
        if m and len(m.group(1)) <= level:
            end = j
            break
        if lines[j].strip() == "---":
            end = j
            break
    k = end
    while k > i + 1 and lines[k - 1].strip() == "":
        k -= 1
    new = lines[:k] + ["", block.strip("\n"), ""] + lines[k:end] + lines[end:]
    return "\n".join(new)


def bump(name: str) -> str:
    m = re.match(r"(.*)-v(\d+)-\d{8}\.md$", name)
    return f"{m.group(1)}-v{int(m.group(2)) + 1}-20261019.md"


def weave(stem: str, edits):
    name = sorted((p.name for p in D.glob(stem + "-v*.md")), key=lambda n: int(re.search(r"-v(\d+)-", n).group(1)))[-1]
    text = (D / name).read_text(encoding="utf-8")
    for heading, block in edits:
        text = add_end(text, heading, block)
    new = bump(name)
    (D / new).write_text(text, encoding="utf-8")
    shutil.move(str(D / name), str(D / "archive" / name))
    print(f"{name} -> {new}")


weave("10-09-relating-to-god", [
    ("## Under rule, and longing for his", """Under rulers who make injustice into law, a psalmist asks, "Can wicked rulers be allied with you, those who frame injustice by statute? They band together against the life of the righteous and condemn the innocent to death" (Psalm 94:20–21). The verses around the question carry its answer. "When I thought, 'My foot slips,' your steadfast love, O Lord, held me up. When the cares of my heart are many, your consolations cheer my soul" (94:18–19). "But the Lord has become my stronghold, and my God the rock of my refuge" (94:22). The thought of falling was met before the question was asked."""),
    ("## Knowing who rules", """Trust in God can be attacked from outside, and the attack is aimed at the trust itself. Sennacherib's servants asked the besieged city, "On what are you trusting, that you endure the siege in Jerusalem? Is not Hezekiah misleading you, that he may give you over to die by famine and by thirst, when he tells you, 'The Lord our God will deliver us from the hand of the king of Assyria'?" (2 Chronicles 32:10–11). They set their record against it: "Do you not know what I and my fathers have done to all the peoples of other lands?" (32:13). The words go for the people's trust by casting doubt on the one who leads them and by naming a past of power."""),
])

weave("11-other-sides-of-the-inner-being", [
    ("### Authority as a standing", """Rule can be turned into injustice: "Can wicked rulers be allied with you, those who frame injustice by statute?" (Psalm 94:20; 10.9). And power can be given for a time and used at will. The two witnesses "have power over the waters to turn them into blood and to strike the earth with every kind of plague, as often as they desire", during "the days of their prophesying" (Revelation 11:6)."""),
    ("## 8. God has a heart and a soul", """God names his heart with a place. "I have consecrated this house that you have built, by putting my name there forever. My eyes and my heart will be there for all time" (1 Kings 9:3; 13.1, *Choosing*)."""),
])

weave("10-02-knowing-and-hearing", [
    ("## Doubt", """God's own call can go unanswered. "Why, when I came, was there no man; why, when I called, was there no one to answer? Is my hand shortened, that it cannot redeem?" (Isaiah 50:2). Two verses on, the servant speaks: "Morning by morning he awakens; he awakens my ear to hear as those who are taught" (50:4). The people who did not answer and the ear that was awakened stand in one passage."""),
])

weave("13-01-divine", [
    ("## Ruling", """He asks it of a people who did not answer him: "Is my hand shortened, that it cannot redeem? Or have I no power to deliver? Behold, by my rebuke I dry up the sea" (Isaiah 50:2)."""),
])

weave("10-10-relating-to-others", [
    ("### Fear that arrives with a person", """Bathsheba met Adonijah, the brother who had lost the throne, with the same question. "Do you come peacefully?" He said, "Peacefully" (1 Kings 2:13; 10.6)."""),
    ("## Plotting against another", """The plot can come back on the one who made it. Harbona told the king of "the gallows that Haman has prepared for Mordecai, whose word saved the king", and the king said, "Hang him on that." "So they hanged Haman on the gallows that he had prepared for Mordecai. Then the wrath of the king abated" (Esther 7:9–10).

Absalom gave the reason for the burned field when Joab came: "Why have I come from Geshur? It would be better for me to be there still. Now therefore let me go into the presence of the king, and if there is guilt in me, let him put me to death" (2 Samuel 14:32). I read the fire as a demand to be seen by his father. "So he came to the king and bowed himself on his face to the ground before the king, and the king kissed Absalom" (14:33)."""),
    ("## Holding authority over another", """The one who holds power holds life for those under it. "A king's wrath is a messenger of death, and a wise man will appease it. In the light of a king's face there is life, and his favor is like the clouds that bring the spring rain" (Proverbs 16:14–15). In Jesus' parable the king uses that power to release: "And out of pity for him, the master of that servant released him and forgave him the debt" (Matthew 18:27). The same servant then refused his fellow servant, and the master's anger followed (18:33–34; 10.13)."""),
    ("## Loyalty and honour", """Loyalty can fail at its post. David called across to Saul's guard: "Why then have you not kept watch over your lord the king? For one of the people came in to destroy the king your lord. This thing that you have done is not good. As the Lord lives, you deserve to die, because you have not kept watch over your lord, the Lord's anointed" (1 Samuel 26:15–16). David had refused to strike Saul himself (26:9–11). He showed the spear and the jar as proof and asked Saul, "Why does my lord pursue after his servant? For what have I done? What evil is on my hands?" (26:18).

Honour can be yielded. Joab, about to take Rabbah, sent for David: "encamp against the city and take it, lest I take the city and it be called by my name" (2 Samuel 12:28). The crown of the city's king "was placed on David's head" (12:30).

Honour can be shown upward by the one on the throne. When Bathsheba came, "the king rose to meet her and bowed down to her. Then he sat on his throne and had a seat brought for the king's mother, and she sat on his right" (1 Kings 2:19). He promised, "Make your request, my mother, for I will not refuse you" (2:20). Then he refused it (2:22; 10.5)."""),
    ("## Friends, company and care", """A gift can be judged and resented between friends. Solomon gave Hiram twenty cities, "But when Hiram came from Tyre to see the cities that Solomon had given him, they did not please him. Therefore he said, 'What kind of cities are these that you have given me, my brother?'" (1 Kings 9:12–13)."""),
])

weave("10-13-anger", [
    ("### What it rises at", """Anger can rise at contempt for a request that rested on good done. David's men asked Nabal for "whatever you have at hand", and gave the ground: "your shepherds have been with us, and we did them no harm" (1 Samuel 25:7–8). Nabal answered, "Who is David? Who is the son of Jesse?" (25:10). David said, "Every man strap on his sword!" (25:13). I have not yet read the rest of the chapter, where Abigail meets him.

Anger can rest on a misreading and still decide. When the king came back from the garden, Haman "was falling on the couch where Esther was", begging for his life, and the king said, "Will he even assault the queen in my presence, in my own house?" (Esther 7:8). When the gallows had done its work, "the wrath of the king abated" (7:10)."""),
])

weave("10-12-fear", [
    ("## Fear that comes upon a person", """Fear can come with seeing what has been decided. Haman "stayed to beg for his life from Queen Esther, for he saw that harm was determined against him by the king" (Esther 7:7)."""),
])

weave("10-06-wanting", [
    ("## Coveting", """Coveting can add until it leaves the coveter alone. "Woe to those who join house to house, who add field to field, until there is no more room, and you are made to dwell alone in the midst of the land." The answer is sworn: "Surely many houses shall be desolate, large and beautiful houses, without inhabitant" (Isaiah 5:8–9)."""),
    ("## A person", """Wanting a person can be read as wanting something else. Adonijah had said of the throne, "the kingdom has turned about and become my brother's, for it was his from the Lord". Then he asked through Bathsheba for Abishag as his wife (1 Kings 2:15–17). Solomon heard it as the throne asked for again: "Ask for him the kingdom also, for he is my older brother" (2:22). The verses give Solomon's reading. They do not give Adonijah's heart."""),
    ("## Possessions", """A king's desire can be carried out by other people's labour. Solomon built "all that Solomon desired to build" (1 Kings 9:1), and "whatever Solomon desired to build in Jerusalem, in Lebanon, and in all the land of his dominion". The peoples left in the land "Solomon drafted to be slaves, and so they are to this day" (9:19, 21). When he had finished, the Lord appeared to him a second time (9:1–3; Chapter 11)."""),
])

weave("10-07-choosing-and-setting-direction", [
    ("## Planning", """Joseph's counsel to Pharaoh plans against a famine he has been shown. "Let Pharaoh select a discerning and wise man", gather the food of the good years "under the authority of Pharaoh", and keep it as "a reserve for the land against the seven years of famine", "so that the land may not perish" (Genesis 41:33–36). "This proposal pleased Pharaoh and all his servants" (41:37)."""),
    ("## Willing", """The visions picture the same will. The ram "did as he pleased and became great" (Daniel 8:4), and the horn after it "became great, even as great as the Prince of the host" (8:11; 10.15)."""),
])

weave("10-15-pride", [
    ("## Where it ends", """In Daniel's vision the horn "became great, even as great as the Prince of the host" (Daniel 8:11), as the ram before it "did as he pleased and became great" (8:4; 10.7)."""),
])

weave("10-03-remembering-and-forgetting", [
    ("## Forgetting lets anger go, and remembering brings it back", """What others do with a king's remembering is part of it. After his anger abated and "he remembered Vashti", his young men answered with a search: "Let beautiful young virgins be sought out for the king", and "let the young woman who pleases the king be queen instead of Vashti." "This pleased the king, and he did so" (Esther 2:1–4). I read the remembering as turned aside by a pleasure offered. The young women's own wishes are not asked."""),
])

weave("10-01-feeling", [
    ("## How a feeling rises", """Before the king's merry heart gave its command, the feast had set every guest free: "There is no compulsion", "to do as each man desired" (Esther 1:8, 10)."""),
])

weave("10-04-thinking", [
    ("## What thinking does", """A wrong expectation can be what a teaching answers. Jesus told the parable of the nobleman and the minas "because he was near to Jerusalem, and because they supposed that the kingdom of God was to appear immediately" (Luke 19:11)."""),
])

weave("10-05-speaking", [
    ("## The oath", """A promise can be given and then overridden by an oath. Solomon told his mother, "Make your request, my mother, for I will not refuse you". When he heard it, he swore, "God do so to me and more also if this word does not cost Adonijah his life!" (1 Kings 2:20, 23; 10.6)."""),
])

weave("04-the-heart", [
    ("## The heart judges itself", """Solomon calls on Shimei's own heart as the witness: "You know in your own heart all the harm that you did to David my father. So the Lord will bring back your harm on your own head" (1 Kings 2:44)."""),
])

weave("02-life-breath-and-death", [
    ("## Where life flows from", """Life is also said to flow from another's face: "In the light of a king's face there is life, and his favor is like the clouds that bring the spring rain" (Proverbs 16:15; 10.10)."""),
    ("## Facing death", """Barzillai, at eighty, asks to go home to die: "Please let your servant return, that I may die in my own city near the grave of my father and my mother. But here is your servant Chimham" (2 Samuel 19:37). He gives his place at court to another (10.7)."""),
])
