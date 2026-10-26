import sys, re
sys.path.insert(0, "outputs/prior-capture/work")
from cap import Fill
c = Fill(11, "M01")
def cells(n):
    return [re.sub(r"\s+", " ", y.replace("**", "").replace("*", "")).strip() for y in c.by_line[n]["text"].strip().strip("|").split(" | ")]
for n in range(38, 56):
    x = cells(n)
    c.f(f"F{n}", "face", f"Face {x[0]} ({x[1]} hits and verses; surfaces {x[2]}): {x[3]}.".replace("..", "."), [n], basis="read")
c.f("T57", "statement", "Four verses carry two faces (Heb 12:21; Rom 13:3; Mat 10:28; 1Pe 3:6), so the verse column sums to 166.", [57],
    verses=["Heb.12.21", "Rom.13.3", "Matt.10.28", "1Pet.3.6"])
for n in range(63, 68):
    x = cells(n)
    c.f(f"R{n}", "term", f"{x[0]}: {x[1]}. {x[2]}.", [n], basis="stated")
c.f("G69", "term", "The surface \"terrified\" in Mat 14:26 and Mar 6:50, and \"troubled\" in Luk 1:12 and Joh 14:27, is G5015 (tarassō, to trouble, stir), tagged M03 and not M01; it stands beside the M01 words in the same verses.", [69], basis="stated")
for n in range(78, 119):
    c.rec(n, f"fear:FE-{n + 44}")
for n in range(128, 140):
    x = cells(n)
    ids = [int(i) for i in re.findall(r"FE-(\d+)", x[1])]
    c.f(f"C{n}", "link", x[0] + ".", [n], basis="read" if "pairing is R" in x[2] else "stated",
        traced=[c.IDS[f"fear:FE-{i}"] for i in ids])
c.not_(range(147, 153), "pointer with no content", "verses already in the chapters, with where they sit")
c.not_(154, "next-steps list", "two restatements in 10.1 that the Greek reading calls for")
c.not_(range(158, 163), "scope or method or process record", "the open threads checked before the pull and what stays held")
c.not_(164, "scope or method or process record", "the proposed register signpost for G5015; the finding is captured from line 69")
c.not_(165, "scope or method or process record", "the status of claim 9-4 (2Ti 1:7) after the Greek reading")
c.not_([175, 176], "weave or quote-check record", "the quote check by hand for Jude 22-23 and the coverage check")
c.not_(181, "next-steps list", "the decisions put to the researcher")
c.done()
