import sys
sys.path.insert(0, "outputs/prior-capture/work")
from cap import Fill, _clean
WHY = "a record of the work: placements, scope, handling and fan-out of verses to threads: not a finding"
for fid in (60, 61):
    c = Fill(fid, "M09")
    c.not_(sorted(c.by_line), "scope or method or process record", WHY)
    c.done()
# 63: the placement proposal keeps the one block that states what the verses name
import re
c = Fill(63, "M09")
FL = open(c.d["file"]["path"], encoding="utf-8").read().replace("\r", "").split("\n")
i = 31
blk = []
while i <= len(FL) and FL[i - 1].strip():
    blk.append(i)
    i += 1
lines = [n for n in blk if n in c.by_line]
text = _clean(FL[30]).rstrip(".:;") + (": " + "; ".join(_clean(FL[n - 1]).lstrip("- ").rstrip(".") for n in blk[1:]) if len(blk) > 1 else "") + "."
c.f("g31", "statement", text, lines)
c.not_([n for n in sorted(c.by_line) if n not in c.ANS], "scope or method or process record", WHY)
c.done()
