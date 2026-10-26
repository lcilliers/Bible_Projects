import sys, re
sys.path.insert(0, "outputs/prior-capture/work")
from cap import Fill
c = Fill(9, "M01")
for n in (20, 21, 22, 23):
    x = [re.sub(r"\s+", " ", y.replace("**", "").replace("*", "")).strip() for y in c.by_line[n]["text"].strip().strip("|").split(" | ")]
    c.f(f"F{n}", "face", f"Face {x[0]} (H4172A, môrāʾ; {x[1]} hits and verses): the word rendered {x[2]}.", [n], basis="read")
for n, k in {29: 163, 30: 164, 31: 165, 32: 166, 33: 167}.items():
    c.rec(n, f"fear:FE-{k}")
c.not_([8, 14], "scope or method or process record", "the coverage gap and how it was closed: a record of what was read, not a finding")
c.not_(42, "scope or method or process record", "an open thread held (OT-08), recorded as held")
c.done()
