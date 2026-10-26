import sys, re
sys.path.insert(0, "outputs/prior-capture/work")
from cap import Fill
c = Fill(19, "M02")
def cl(s):
    return re.sub(r"\s+", " ", s.replace("**", "").replace("~~", "").replace("*", "")).strip()
miss = []
for n, l in sorted(c.by_line.items()):
    m = re.match(r"\|\s*(MS-\d+)\s*\|", l["text"])
    if not m:
        continue
    k = "anger:" + m.group(1)
    if k in c.IDS:
        c.rec(n, k)
    else:
        x = [cl(y) for y in l["text"].strip().strip("|").split(" | ")]
        miss.append(m.group(1))
        c.f(m.group(1), "statement", x[1], [n], basis="stated", stable=k, disp="told", note=f"placement {x[4]}; from {x[3]}")
c.f("E69", "statement", "Where the angry person's own heart or spirit is named: in the narratives it is rare (2Ki 6:11; Est 5:9; Act 7:54; Act 17:16; Eze 3:14), and in the wisdom books frequent (Job 36:13; Pro 6:14; 14:29; 16:32; 19:3; Ecc 2:23; 7:3; 7:9; 11:10); the narratives show anger by what is done.", [69], basis="stated")
c.f("E70", "statement", "In the narratives the seat is often named by someone else: Eliab names David's heart (1Sa 17:28); Jesus' anger is at his opponents' hardened heart (Mar 3:5).", [70], basis="stated")
print("unrecorded:", miss)
c.done()
