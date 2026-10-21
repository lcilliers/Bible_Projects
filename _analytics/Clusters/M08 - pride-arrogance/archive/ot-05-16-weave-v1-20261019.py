"""OT-05.16 weave (#2160 group C): 10.15 v2 -> v3, Ch 4 v21 -> v22, 10.6 v27 -> v28, 10.7 v33 -> v34,
Ch 11 v38 -> v39, 10.10 v34 -> v35.

Researcher, chat 2026-10-19 (verbatim): "proceed with C". Proposal: ot-05-16-self-glory-reading-v1-20261019.md
("Weave now"). One change from the proposal: Php 3:19's "minds set on earthly things" goes to 10.7 beside
Rom 8:6 (where the set mind is already told), not 10.4, which has no account of it. Each edit replaces an
exact block; the script stops if a block is not found exactly once. Old versions are moved to archive/.
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


# ── 10.15 Pride ───────────────────────────────────────────────────────────────────────────────
P_HAND_OLD = """I read pride here as crediting to itself what was done through it.
"""
P_HAND_NEW = """I read pride here as crediting to itself what was done through it.

**It gives itself the glory.** The great city "glorified herself and lived in luxury" (Revelation 18:7). The Greek verb is the one used where people give glory to God: "so that they may see your good works and give glory to your Father who is in heaven" (Matthew 5:16). Here she is the one who gives the glory and the one who receives it. What it brings her is in *Where it ends*, below.
"""
P_LOSS_OLD = """The fear that others felt fed what Edom told itself.
"""
P_LOSS_NEW = """The fear that others felt fed what Edom told itself.

**It tells itself that loss will not come.** Babylon in Isaiah says more than "I am". She says, "I shall not sit as a widow or know the loss of children" (Isaiah 47:8). Before it: "You said, 'I shall be mistress forever,' so that you did not lay these things to heart or remember their end" (47:7). The answer: "These two things shall come to you in a moment, in one day" (47:9). Revelation gives the great city the same voice: "in her heart she says, 'I sit as a queen, I am no widow, and mourning I shall never see'" (Revelation 18:7). And the same answer: "For this reason her plagues will come in a single day, death and mourning and famine" (18:8). I read Revelation as taking up Isaiah's words. Pride's heart says that it will not be moved from where it sits, and that nothing will be taken from it. The verse in Isaiah names what goes with it: the end is not laid to heart.
"""
P_SHAME_OLD = """A boast is shut out because what is held was given.
"""
P_SHAME_NEW = """A boast is shut out because what is held was given.

**In shame.** Paul names many who "walk as enemies of the cross of Christ. Their end is destruction, their god is their belly, and they glory in their shame, with minds set on earthly things" (Philippians 3:18–19). The word is "glory" (*doxa*), not the boast word. I read it as doing the boast's work, saying what a person stands on, and as turned upside down: it rests on what should shame. Paul tells it "even with tears" (3:18; 10.10). Against it he sets, "But our citizenship is in heaven", and a Savior who "will transform our lowly body to be like his glorious body" (3:20–21). "Glorious" is the same word. Their glory is in their shame, and the glory awaited is his.
"""
P_END_OLD = """Death brings it down too: "Your pomp is brought down to Sheol" (Isaiah 14:11).
"""
P_END_NEW = """Death brings it down too: "Your pomp is brought down to Sheol" (Isaiah 14:11).

**A like measure.** "As she glorified herself and lived in luxury, so give her a like measure of torment and mourning" (Revelation 18:7). The measure of what comes to the city is the measure of the glory she gave herself and the luxury she lived in. The mourning she said she would never see is what she is given. The verse before says the same of her deeds: "Pay her back as she herself has paid back others … mix a double portion for her in the cup she mixed" (18:6). Those who shared her luxury "will stand far off, in fear of her torment" (18:9–10). And before it all comes a call: "Come out of her, my people, lest you take part in her sins, lest you share in her plagues" (18:4).
"""
edit("10-15-pride-v2-20261019.md", "10-15-pride-v3-20261019.md", [
    (P_HAND_OLD, P_HAND_NEW), (P_LOSS_OLD, P_LOSS_NEW), (P_SHAME_OLD, P_SHAME_NEW), (P_END_OLD, P_END_NEW)])

# ── Ch 4 The heart speaks to itself ──────────────────────────────────────────────────────────
H_OLD = """"Who will bring me down to the ground?" (Obadiah 3).
"""
H_NEW = """"Who will bring me down to the ground?" (Obadiah 3). "I sit as a queen, I am no widow, and mourning I shall never see" (Revelation 18:7; 10.15).
"""
edit("04-the-heart-v21-20261019.md", "04-the-heart-v22-20261019.md", [(H_OLD, H_NEW)])

# ── 10.6 Wanting that owns the one who wants ─────────────────────────────────────────────────
W_OLD = """I read these as one act seen from different sides: the want leads, and the one who wants follows."""
W_NEW = """It is served as a god. Some "walk as enemies of the cross of Christ … their god is their belly" (Philippians 3:18–19). The same Greek word is "appetites" where Paul writes of those who "do not serve our Lord Christ, but their own appetites" (Romans 16:18). I read the belly as the appetite, set in the place of God and served. I read these as one act seen from different sides: the want leads, and the one who wants follows."""
edit("10-06-wanting-v27-20261019.md", "10-06-wanting-v28-20261019.md", [(W_OLD, W_NEW)])

# ── 10.7 A purpose held: the set mind ────────────────────────────────────────────────────────
M_OLD = """*"For the mind that is set on the flesh is hostile to God"* (8:7). Chapter 7 gives the flesh.
"""
M_NEW = """*"For the mind that is set on the flesh is hostile to God"* (8:7). Chapter 7 gives the flesh.
- The verb of the same word names a mind set downward: *"their god is their belly, and they glory in their shame, with minds set on earthly things"* (Philippians 3:19). The next verse turns it: *"But our citizenship is in heaven"* (3:20). And the call uses the same verb: *"Set your minds on things that are above, not on things that are on earth"* (Colossians 3:2).
"""
edit("10-07-choosing-and-setting-direction-v33-20261019.md", "10-07-choosing-and-setting-direction-v34-20261019.md", [(M_OLD, M_NEW)])

# ── Ch 11 §4 One word, opposite values: glory ────────────────────────────────────────────────
G_OLD = """What differs is where the height comes from, and which way it faces (10.15).
"""
G_NEW = """What differs is where the height comes from, and which way it faces (10.15).
- **Glory.** The verb that gives glory to God (Matthew 5:16) is the great city's own: she "glorified herself" (Revelation 18:7). The noun is the glory some take "in their shame" (Philippians 3:19), and two verses later the glory of the body to come, "like his glorious body" (3:21). The same word names glory taken where it does not belong and glory given (10.15).
"""
edit("11-other-sides-of-the-inner-being-v38-20261019.md", "11-other-sides-of-the-inner-being-v39-20261019.md", [(G_OLD, G_NEW)])

# ── 10.10 Pride over another: wept over ──────────────────────────────────────────────────────
R_OLD = """The one under it carries it: "Our soul has had more than enough of the scorn of those who are at ease, of the contempt of the proud" (Psalm 123:4).
"""
R_NEW = """The one under it carries it: "Our soul has had more than enough of the scorn of those who are at ease, of the contempt of the proud" (Psalm 123:4).

Another's pride can also be wept over. "But if you will not listen, my soul will weep in secret for your pride" (Jeremiah 13:17). Paul writes of many "of whom I have often told you and now tell you even with tears, walk as enemies of the cross of Christ" (Philippians 3:18), who "glory in their shame" (3:19). He tells it with tears, and he still tells it: "keep your eyes on those who walk according to the example you have in us" (3:17).
"""
edit("10-10-relating-to-others-v34-20261019.md", "10-10-relating-to-others-v35-20261019.md", [(R_OLD, R_NEW)])
