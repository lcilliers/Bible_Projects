import sys, re
sys.path.insert(0, "outputs/prior-capture/work")
from cap import Fill, _clean
# ── 35: the unit 1 / unit 2 side split ──
a = Fill(35, "M02")
a.f("m29", "statement", "Meribah as a place name: the verses about the people's quarrel are human (Exo 17:7; Num 20:13, 24; 27:14; Deu 32:51); in Deu 33:8 and Psa 81:7 God does the striving or testing, and these are divine; the pure boundary markers (Eze 47:19; 48:28) have no inner being.", [29])
a.f("m30", "term", "\"Venom\" or \"poison\" (chemah) as a figure for the enemies' malice is human (Deu 32:33; Psa 58:4; 140:3); venom that God sends as literal poison (Deu 32:24) has no inner being; \"My spirit drinks their poison\", from the arrows of the Almighty (Job 6:4), is divine.", [30])
a.f("m63", "statement", "Eze 23:25 is the one verse in the divine set where the agents' own fury is named.", [63])
a.f("m69", "statement", "The verse Mar 10:14 gives the inner operation, anger with grief, in human terms, as Mar 3:5 does (Mar 3:5 is seated).", [69], basis="read")
a.f("m94", "statement", "Jon 4:2 is Jonah's angry prayer quoting \"slow to anger\" back at God, one passage with Jon 4:1, 4 and 9, which are human.", [94])
a.f("m108", "statement", "Luk 15:28, the elder brother, is a human figure of anger, on the human side.", [108])
a.f("m124", "statement", "Rev 12:12 (the devil \"in great wrath\") and Rev 12:17 (the dragon \"became furious\") are anger of neither a human nor God.", [124])
a.f("m125", "statement", "Hab 3:14, \"came like a whirlwind to scatter me\", is enemies rushing in; the word is a figure of motion.", [125])
a.not_([21, 22], "hit count", "counts of verses by side")
a.not_([123], "scope or method or process record", "the verses the pilot already recorded as spurious seat links")
a.not_([n for n in sorted(a.by_line) if n not in a.ANS], "scope or method or process record", "a list assigning verses to a side or to none: a record of the classification, not a finding")
a.done()

# ── 27: the pairing threads whose paired strand is already read ──
c = Fill(27, "M02")
def cells(n):
    return [_clean(y) for y in c.by_line[n]["text"].strip().strip("|").split(" | ")]
def tidy(note):
    note = re.sub(r"\s*;?\s*carried in [^;]*$", "", note).strip()
    note = re.sub(r"\s*\((?:[^()]*(?:10\.\d+|Ch \d+|13\.1)[^()]*)\)\s*$", "", note).strip()
    return note
rows = [n for n in sorted(c.by_line) if c.by_line[n]["text"].startswith("| ") and len(cells(n)) == 4 and cells(n)[2] in ("carried", "parallel", "data", "gap", "forward")]
for n in rows:
    v, face, dec, note = cells(n)
    t = tidy(note)
    if dec in ("gap", "forward") or not t or re.fullmatch(r"(parallel of [\w :.\-]+)", t):
        c.not_(n, "pointer with no content", f"the verse's status in the check ({dec}): where it is carried or read")
    elif dec == "data" and t.lower().startswith("no anger"):
        c.f(f"r{n}", "silence", f"{v}: {t}.", [n], disp="data")
    else:
        c.f(f"r{n}", "statement", f"{v} ({face}): {t}.", [n])
G = {
 139: [("g139a", "Pro 20:2, \"The terror of a king is like the growling of a lion; whoever provokes him to anger forfeits his life\", sets the fear of a ruler beside the anger of the ruler and says what provoking him costs; the verse after says what to do instead, \"It is an honor for a man to keep aloof from strife, but every fool will be quarreling\" (20:3), and the verse before names wine as \"a brawler\" (20:1).", "stated"),
       ("g139b", "What a person does with the terror of a king is left to him, either keeping aloof or quarrelling (Pro 20:1-3).", "read")],
 141: [("g141a", "Job tells his friends \"be afraid of the sword, for wrath brings the punishment of the sword, that you may know there is a judgment\" (Job 19:29) straight after \"I know that my Redeemer lives\" and \"My heart faints within me!\" (19:25, 27), answering \"How we will pursue him!\" and \"The root of the matter is found in him\" (19:28); he tells his accusers to fear, and the reason he gives is that there is a judgment.", "stated"),
       ("g141b", "The one being accused turns the fear of wrath back onto those who pursue him, from the confidence he has just stated (Job 19:29).", "read")],
 143: [("g143a", "In Lam 2:22 the lament speaks to God about his anger, \"Look, O Lord, and see! With whom have you dealt thus?\" (2:20), \"you have killed them in the day of your anger, slaughtering without pity\" (2:21); the figure is a call to a feast, and a festival day gathers people to rejoice, but here what is gathered is \"my terrors on every side\".", "stated"),
       ("g143b", "The speaker of Lam 2:22 does not turn away from God in the terror: he asks him to look, and names what his anger did to those \"I held and raised\".", "read")],
 145: [("g145", "In Psa 76 the fear is the earth's stillness before God's anger: \"But you, you are to be feared!\" (76:7); \"the earth feared and was still, when God arose to establish judgment, to save all the humble of the earth\" (76:8-9): his anger is roused to save the humble.", "stated")],
 147: [("g147", "Two angers stand in one sentence in Rev 11:18: \"The nations raged, but your wrath came\"; in the same verse fear of his name is what is rewarded, \"both small and great\"; the elders say this in worship (11:16-17).", "stated")],
 151: [("g151a", "Deu 31:17 runs the whole course in God's own words, \"my anger will be kindled against them ... I will forsake them and hide my face from them, and they will be devoured\"; the cause stands on both sides of the verse: \"they will forsake me and break my covenant\" (31:16), and \"I will surely hide my face in that day because of all the evil that they have done, because they have turned to other gods\" (31:18).", "stated"),
        ("g151b", "The people's question in Deu 31:17, \"Have not these evils come upon us because our God is not among us?\", names the absence but not the turning that the verses give as its cause.", "read")],
 153: [("g153", "Jer 33:5, \"whom I shall strike down in my anger and my wrath, for I have hidden my face from this city because of all their evil\", is followed by a turn, \"Behold, I will bring to it health and healing, and I will heal them\" (33:6): in two verses the hidden face and the anger are followed straight away by healing.", "stated")],
 155: [("g155a", "Psa 89:46, \"How long, O Lord? Will you hide yourself forever? How long will your wrath burn like fire?\", sets the length of the anger against the length of the psalmist's own life: \"Remember how short my time is!\" (89:47); then \"What man can live and never see death?\" (89:48).", "stated"),
        ("g155b", "The plea in Psa 89:46-48 weighs God's anger against a short life.", "read")],
 157: [("g157", "Zep 2:3, \"Seek the Lord, all you humble of the land, who do his just commands; seek righteousness; seek humility; perhaps you may be hidden on the day of the anger of the Lord\": the call comes before \"the burning anger of the Lord\" (2:2); the people called are already humble and already doing his commands, and are told to seek humility; the verse promises nothing, \"perhaps\"; being hidden is God's act.", "stated")],
 161: [("g161", "Deu 31:29, \"after my death you will surely act corruptly and turn aside from the way that I have commanded you ... provoking him to anger through the work of your hands\": Moses grounds what he knows in what he has seen, \"For I know how rebellious and stubborn you are ... How much more after my death!\" (31:27); the provocation is named as \"the work of your hands\".", "stated")],
 163: [("g163", "Eze 20:33, \"As I live, declares the Lord God, surely with a mighty hand and an outstretched arm and with wrath poured out I will be king over you\", answers a thought, \"What is in your mind shall never happen ... 'Let us be like the nations ... and worship wood and stone'\" (20:32); the wrath poured out goes with bringing out and gathering (20:34), with judgment \"face to face\" (20:35), and with bringing them \"into the bond of the covenant\" (20:37): God answers a thought in the mind with an oath by his own life and with his rule.", "stated")],
 165: [("g165a", "Isa 51:17-22: the call \"Wake yourself, wake yourself, stand up\"; the one who drank, with \"none to guide her ... none to take her by the hand\" among her sons (51:18); \"who will comfort you?\" (51:19); her sons \"full of the wrath of the Lord\" (51:20), \"drunk, but not with wine\" (51:21); the figure is drunkenness: wrath that has been drunk leaves a person staggering and without a guide.", "stated"),
        ("g165b", "The call to wake in Isa 51:17 goes to one who cannot rise without a hand, and the hand that takes the cup is God's, \"who pleads the cause of his people\" (51:22).", "read")],
 167: [("g167", "Pro 11:4, \"Riches do not profit in the day of wrath, but righteousness delivers from death\": the day of wrath tests what a person has relied on; the next verses go on, \"The righteousness of the blameless keeps his way straight\" (11:5), and \"the treacherous are taken captive by their lust\" (11:6).", "stated")],
 169: [("g169a", "Pro 29:8, \"Scoffers set a city aflame, but the wise turn away wrath\": the scoffer's words set a whole city alight, and the wise turn the anger away; around it the fool is set beside the wise: \"the fool only rages and laughs, and there is no quiet\" (29:9); \"A fool gives full vent to his spirit, but a wise man quietly holds it back\" (29:11).", "stated"),
        ("g169b", "The wise man who turns another's wrath away (Pro 29:8) is the same man who holds his own back (29:11).", "read")],
}
for n, items in G.items():
    for key, text, basis in items:
        c.f(key, "statement", text, [n], basis=basis)
c.not_([n for n in sorted(c.by_line) if n not in c.ANS], "scope or method or process record", "the method, the stale lines found in the narrative and the thread records: not findings")
c.done()
