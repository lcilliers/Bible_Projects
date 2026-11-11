import sys, re
sys.path.insert(0, "outputs/prior-capture/work")
from cap import Fill
c = Fill(10, "M01")
def cells(n):
    return [re.sub(r"\s+", " ", y.replace("**", "").replace("*", "")).strip() for y in c.by_line[n]["text"].strip().strip("|").split(" | ")]
for n in range(45, 74):
    x = cells(n)
    c.f(f"F{n}", "face", f"Face {x[0]} ({x[1]} hits and verses; surfaces {x[2]}): {x[3]}.".replace("..", "."), [n], basis="read")
for n in range(86, 121):
    c.rec(n - 5, f"fear:FE-{n}")
for n in range(125, 135):
    x = cells(n)
    ids = [int(i) for i in re.findall(r"FE-(\d+)", x[1])]
    c.f(f"C{n}", "link", x[0] + ".", [n], basis="stated", traced=[c.IDS[f"fear:FE-{i}"] for i in ids])
c.not_(22, "scope or method or process record", "the coverage gap found at the overview pass and where it was closed")
c.not_(range(140, 148), "pointer with no content", "verses already in the chapters, with where they sit")
c.not_([151, 152, 153], "scope or method or process record", "the open threads checked before the pull and what stays held")
c.done()
