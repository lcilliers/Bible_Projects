import sys, re
sys.path.insert(0, "outputs/prior-capture/work")
from cap import Fill
c = Fill(13, "M01")
def clean(n):
    return re.sub(r"\s+", " ", c.by_line[n]["text"].replace("**", "").replace("*", "")).strip()
def cells(n):
    return [y.strip() for y in clean(n).strip("|").split(" | ")]
for n in [k for k in range(62, 71) if k in c.by_line]:
    x = cells(n)
    c.f(f"L{n}", "link", f"Fear and {x[0]}: in {x[1]} verses ({x[2]} within three words) the commonest near pairs are {x[3]}.", [n], basis="stated")
ROOTS = {(85, 91): 'H3372H "to fear: revere"', (97, 100): 'H3372G "to fear"', (104, 106): 'H3373 "afraid"',
         (110, 116): "The Greek fear words G5401 and G5399", (122, 128): 'H7264 rāgaz "to tremble"', (134, 136): 'H6342 "to dread"',
         (140, 143): 'H2729 "to tremble"', (146, 148): 'H1481C "to dread"', (152, 153): 'H6343 "dread"'}
for (a, b), root in ROOTS.items():
    for n in range(a, b + 1):
        if n in c.by_line:
            t = clean(n).lstrip("- ").strip()
            c.f(f"T{n}", "term", f"{root} is rendered {t}.".replace("..", "."), [n], basis="stated")
for n in [k for k in range(176, 189) if k in c.by_line]:
    x = cells(n)
    c.f(f"N{n}", "term", f"{x[0]} is tagged M01 but the English renders another face: {x[1]} ({x[2]}).", [n], basis="stated")
c.f("A214", "link", "Fear and anger meet in Psa 90:11: \"the power of your anger ... your wrath according to the fear of you\".", [214], verses=["Ps.90.11"])
c.not_([198, 199], "scope or method or process record", "where fear stands in the narrative now, with the chapters that name it")
c.done()
