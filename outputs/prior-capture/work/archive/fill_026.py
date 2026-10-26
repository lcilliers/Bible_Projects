import sys, re
sys.path.insert(0, "outputs/prior-capture/work")
from cap import Fill
c = Fill(26, "M02")
def cl(s):
    return re.sub(r"\s+", " ", s.replace("**", "").replace("~~", "").replace("*", "")).strip()
def cells(n):
    return [cl(y) for y in c.by_line[n]["text"].strip().strip("|").split(" | ")]
AN = {}
for n in c.by_line:
    m = re.match(r"\|\s*(AN-\d+)\s*\|", c.by_line[n]["text"])
    if m:
        AN[n] = m.group(1)
for n, an in AN.items():
    k = "anger:" + an
    if k in c.IDS:
        c.rec(n, k)
        continue
    x = cells(n)
    if len(x) == 6:      # id | observation | verses | basis | touches | disposition
        text, basis, touches, disp = x[1], x[3], x[4], x[5]
    else:                # id | link | verses | touches | disposition
        text, basis, touches, disp = x[1], "S", x[3], x[4]
    c.f(an, "statement", text + ".", [n], basis=("read" if basis.startswith("R") else "stated"), stable=k, disp="told",
        note=f"{disp}; touches {touches}")
# L.1 aph faces
for n in range(202, 212):
    if n in c.by_line:
        x = cells(n)
        c.f(f"aph{n}", "face", f"Face of aph (H0639), {x[0]}: {x[2]} ({x[1]}). {x[3]}.".replace("..", "."), [n], basis="stated")
# L.2 the other words
for n in range(219, 232):
    if n in c.by_line:
        x = cells(n)
        c.f(f"w{n}", "term", f"{x[0]}: {x[1]} ({x[2]}). {x[3]}.".replace("..", "."), [n], basis="stated")
# L.3 factors tested
for n in range(239, 253):
    if n in c.by_line:
        x = cells(n)
        c.f(f"fac{n}", "statement", f"Factor {x[0]}: {x[1]}. {x[2]}.".replace("..", "."), [n], basis="stated")
c.f("H4", "silence", "B5 verses are still open (2Ki 3:27): the bearer of the anger is not given; recorded, not interpreted.", [263], disp="held", verses=["2Kgs.3.27"])
for n in (291, 292, 293, 294):
    x = cl(c.by_line[n]["text"]).lstrip("- ").strip()
    c.f(f"rem{n}", "statement", ("Remembering and forgetting: " if n == 291 else "") + x.rstrip(".") + ".", [n], basis="stated")
c.not_([233], "scope or method or process record", "a word held back from the pull (zēlos), not a finding")
c.not_([260, 261, 264], "scope or method or process record", "items held by ruling and why: a record of what was not woven")
c.not_([319, 327, 328, 334], "weave or quote-check record", "the weave plan: what goes into which chapter")
c.not_([398, 399, 400, 401, 402, 404], "weave or quote-check record", "quotations corrected after the check")
c.done()
