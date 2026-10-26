import sys, re
sys.path.insert(0, "outputs/prior-capture/work")
from cap import Fill
c = Fill(17, "M02")
def cl(s):
    s = re.sub(r"\s+", " ", s.replace("**", "").replace("~~", "").replace("*", "")).strip()
    return re.sub(r"^\((v[23])\)\s*", "", s)
def cells(n):
    return [cl(y) for y in c.by_line[n]["text"].strip().strip("|").split(" | ")]
def rows(a, b):
    return [n for n in range(a, b + 1) if n in c.by_line]
def g(x, i):
    return x[i] if len(x) > i else ""
P = lambda s: s.rstrip(".") + "."
# A: what the verses say anger is
for n in rows(79, 87):
    x = cells(n); c.f(f"A{n}", "statement", P(f"{x[0]}: {x[1]}"), [n])
x = cells(103); c.f("A103", "term", P(f"{x[0]}: {x[1]}"), [103])
c.f("A107", "statement", "The verses speak of anger in the same words for God and for people, and keep some words almost wholly for God (ḥārôn, zaʿam, qeṣep̄, and orgē in the Greek); the same pictures (kindled, burning, poured, drunk) are used on both sides, and where the verses mark a difference they mark it in restraint: \"for I am God and not a man\" (Hos 11:9).", [107], basis="read")
# B: forms by party
for a, b in ((133, 147), (153, 156), (162, 167), (173, 173), (179, 181), (187, 208), (214, 216)):
    for n in rows(a, b):
        x = cells(n)
        c.f(f"B{n}", "face", P(f"Form of anger, {x[0]} ({x[2]} hits and verses; faces {x[1]}; units {x[3]})"), [n], basis="read")
# C: factors
for n in rows(236, 259):
    x = cells(n); c.f(f"C{n}", "statement", P(f"{x[1]}: {x[2]}"), [n])
# D.1 / D.2 / D.3 / D.4
for n in rows(278, 291):
    x = cells(n); c.f(f"D1{n}", "statement", P(f"God's anger leads to {x[0][0].lower() + x[0][1:]}: {x[1]}"), [n])
for n in rows(297, 313):
    x = cells(n); c.f(f"D2{n}", "statement", P(f"A person's anger leads to {x[0][0].lower() + x[0][1:]}: {x[1]}"), [n])
c.f("D2b", "link", "The same outcome is named on both sides: terror or fear (Psa 2:5; 2Sa 6:9), shame (Jer 12:13; Isa 45:24), and the body (Psa 38:3; 1Ki 21:4); no verse draws the parallel.", [315])
for n in rows(323, 344):
    x = cells(n); c.f(f"D3{n}", "statement", P(f"A person responds to God's anger by {x[0]}: {x[2]}"), [n])
for n in rows(354, 368):
    x = cells(n); c.f(f"D4{n}", "statement", P(f"{x[0]}: {x[1]}"), [n])
# E held
c.f("E375", "silence", "Source not named: \"there came great wrath against Israel\" (2Ki 3:27); held.", [375], disp="held", verses=["2Kgs.3.27"])
c.f("E376", "statement", "The friends' explanations of suffering by God's anger (Eliphaz, Zophar, Elihu) are a named speaker's statement, not Scripture's own, under God's verdict \"you have not spoken of me what is right\" (Job 42:7); Job's \"my adversary\" (Job 16:9) is held beside the same verdict, unreconciled.", [376], disp="held", verses=["Job.42.7", "Job.16.9"])
# F.1 sequences
for n in rows(402, 465):
    x = cells(n); c.f(f"F1{n}", "link", P(f"Sequence in {x[0]}: {x[1]}"), [n])
c.f("F1a", "statement", "The answer the texts give to human anger is most often a question or a reframing, not a rebuke: God's question to Cain (Gen 4:6) and to Jonah (Jon 4:4, 9); Joseph's \"not you ... but God\" (Gen 45:8); the father's \"this your brother\" (Luk 15:32); Nathan's parable turned round (2Sa 12:7); in two of these, Jonah and the elder brother, the text ends before the angry one answers.", [473, 474, 475, 476], basis="read")
c.f("F1b", "statement", "The anger is repeatedly said to end, or to have a purpose past itself: knowledge (Eze 5:13), calm (Eze 16:42), an appointed end (Dan 8:19), \"finished\" (Rev 15:1), deliverance (1Th 1:10).", [484])
# F.3 joining
c.f("F3a", "link", "One characteristic leads to another where the verse says so, set against with \"but\": \"A soft answer turns away wrath, but a harsh word stirs up anger\" (Pro 15:1).", [543])
c.f("F3b", "link", "Anger is named together with another characteristic in one breath or list: \"the anger and envy that you showed\" (Eze 35:11); \"with anger, grieved at their hardness of heart\" (Mar 3:5).", [544])
for n in rows(551, 572):
    x = cells(n); c.f(f"F3{n}", "link", P(f"Anger and {x[0]}: {x[2]}"), [n])
for n in rows(580, 592):
    x = cells(n); c.f(f"F4{n}", "link", P(f"Anger and {x[0]}, side by side with fear: fear side, {x[1]}; anger side, {x[2]}"), [n])
c.f("F4b", "link", "The two strands share a verse in Deu 9:19, Psa 90:11, Dan 11:30 and Heb 11:27, and in 2Cor 7:11, where indignation and fear stand in one list.", [594])
# G chains
for n in rows(609, 618):
    x = cells(n); c.f(f"G{n}", "link", P(f"{x[0]}: {x[1]}"), [n])
# H emerged
for n in rows(630, 655):
    x = cells(n); c.f(f"H{n}", "statement", P(re.sub(r"^H\.\d+\s*", "", x[1])), [n], basis="read")
# I appendix
for n in rows(665, 675):
    x = cells(n)
    if len(x) >= 5:
        c.f(f"I{n}", "statement", P(f"{x[3]} ({x[1]}: {x[2]})"), [n], basis="stated")
# M slips
for n in rows(707, 714):
    x = cells(n); c.f(f"M{n}", "term", P(f"{x[0]}: the reading says {x[1]}; the ESV says {x[2]}; the text carries {x[3]}"), [n])
c.f("M717", "statement", "Four of the eight slips are not misreadings: the seat word (lēḇ, nep̄eš) is in the text and the ESV renders it \"myself\", \"grew proud\", \"distressed\" or \"himself\"; one (Est 1:18) and the AG-241 reference are true slips; two are wording only.", [717])
# not observations
c.not_([49, 68, 114, 656, 738, 740, 741], "scope or method or process record", "the method and result of the reconciliation, the plan and the points put to the researcher: not findings")
c.not_(rows(506, 533), "hit count", "co-occurrence counts of M-codes with anger faces: data that points to verses to read, with no verse stated")
c.not_([374], "scope or method or process record", "the life and death sides held (OT-08): a record of what was held")
c.not_([721, 722, 724, 725, 726, 748, 751, 752, 753, 755, 757], "weave or quote-check record", "the quote check of the overview and its corrections")
c.done()
