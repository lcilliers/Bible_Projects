import sys
sys.path.insert(0, "outputs/prior-capture/work")
from cap import Fill
fid = int(sys.argv[1]); cl = sys.argv[2] if len(sys.argv) > 2 else "M02"
c = Fill(fid, cl)
print(c.auto())
for n, a in sorted(c.ANS.items()):
    if "not_an_observation" in a:
        print("PASS", n, c.by_line[n]["text"][:150].encode("ascii", "replace").decode())
print("NEWID", [f["key"] for f in c.F if f.get("stable_key")])
c.done()
