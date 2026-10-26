import sys, re
sys.path.insert(0, "outputs/prior-capture/work")
from cap import Fill
c = Fill(7, "M01")


def cells(n):
    t = c.by_line[n]["text"].strip().strip("|")
    return [re.sub(r"\s+", " ", x.replace("**", "").replace("*", "")).strip() for x in t.split(" | ")]


# A. what the verses say fear is (R headings, S statements)
for n in range(33, 41):
    x = cells(n)
    c.f(f"A{n}", "statement", f"{x[0]}: {x[1]}", [n], basis="stated")
c.f("A42", "statement", "The verses speak of fear in two ways that do not reduce to each other: fear happens to a person, who is "
    "acted on; and fear of God is a standing that is required, learned, given and owed. Exo 20:20 puts both in one "
    "sentence (FE-20). No verse says they are two kinds.", [42], basis="read")
# B. faces across units 1-4
for n in list(range(56, 74)) + list(range(79, 84)) + list(range(89, 95)) + list(range(100, 104)) + [109, 110]:
    x = cells(n)
    what = f": {x[3]}" if len(x) > 3 and x[3] else ""
    c.f(f"B{n}", "face", f"Face {x[0]} ({x[1]} hits and verses, units {x[2]}){what}", [n], basis="read")
# C. what influences its nature
for n in [k for k in range(129, 148) if k in c.by_line]:
    x = cells(n)
    c.f(f"C{n}", "statement", f"{x[1]}: {x[2]}", [n], basis="stated")
# D. what fear leads to
for n in range(164, 181):
    x = cells(n)
    c.f(f"D{n}", "statement", f"Fear leads to {x[0].lower()}: {x[1]}", [n], basis="stated")
c.f("E189", "statement", "FE-92 is a named speaker's statement, not Scripture's own: Bildad and Zophar speak, and Job 42:7 stands over them.",
    [189], disp="held")
c.f("E190", "silence", "Jude 23: the object of the fear is unstated; data only.", [190], disp="data")
# F. fear and the other characteristics
for n in range(211, 232):
    x = cells(n)
    c.f(f"F{n}", "link", f"Fear and {x[0]}: {x[2]} (verses shared or near: {x[1]}).", [n], basis="stated")
c.not_(188, "scope or method or process record", "what was held, and why (OT-07), not a finding")
c.not_(246, "next-steps list", "the comparison with 10.1 proposed as the next step")
c.not_(range(254, 259), "weave or quote-check record", "the result of the quote check and its corrections")
c.done()
