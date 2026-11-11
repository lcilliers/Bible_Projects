import sys, re
sys.path.insert(0, "outputs/prior-capture/work")
from cap import Fill, _clean
c = Fill(32, "M02")
kinds = {"bullet": 0, "head": 0, "an": 0, "proc": 0, "other": []}
def strip(t):
    t = re.sub(r"^-\s*U[12]\s+L\d+\s*\(not carried:[^)]*\):\s*", "", t)
    t = re.sub(r"\s*\(([A-Z]\d?\s*v\d+\s*\S*\s*[\d.]*(?:;\s*[A-Z]\d?\s*v\d+\s*\S*\s*[\d.]*)*)\)", "", t)
    return _clean(t)
for n in sorted(c.by_line):
    t = c.by_line[n]["text"]
    if 427 <= n <= 477 and t.startswith("|"):
        x = [_clean(y) for y in t.strip().strip("|").split(" | ")]
        c.f(x[0], "statement", x[2].rstrip(".") + ".", [n], basis="stated", stable=f"anger:{x[0]}-d2", disp="told", note=f"{x[3]}") if False else \
            c.f(x[0] + "d2", "statement", x[2].rstrip(".") + ".", [n], basis="stated")
        kinds["an"] += 1
    elif 496 <= n <= 1030:
        if t.startswith("- "):
            s = strip(t)
            if len(s) < 25:
                c.not_(n, "scope or method or process record", "a fragment of a recovery list")
                kinds["proc"] += 1
            else:
                c.f(f"b{n}", "statement", s.rstrip(".") + ".", [n], basis="stated")
                kinds["bullet"] += 1
        elif t.startswith("**"):
            c.not_(n, "reference list", "the heading of a phenomenon with its list of verses")
            kinds["head"] += 1
        else:
            kinds["other"].append(n)
    else:
        c.not_(n, "scope or method or process record", "how the reading was done, context lists and bearing on earlier work: a record of the process")
        kinds["proc"] += 1
print({k: (v if k != "other" else v[:10]) for k, v in kinds.items()})
for n in kinds["other"]:
    c.not_(n, "scope or method or process record", "a line of the recovery list that states no finding")
c.done()
