"""Escalation #2000, build step 7: compare the generated open threads register with the frozen
hand-kept one, row by row. Read-only.

For every OT row in the frozen register, the thread, raised and comes-back-when cells must equal
the generated ones exactly (the import carried them whole: proposal v3 sec3.1). The status cell is
generated (state, each item with its latest response, then the old status text), so it is not
compared cell for cell; instead the old status text must appear whole inside the new status cell.

Usage:
    python escalation-2000-register-export-compare-v1-20261012.py FROZEN.md GENERATED.md
"""
import pathlib
import re
import sys

SPLIT = re.compile(r"(?<!\\) \| ")


def rows(path):
    out = {}
    for line in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        if not line.startswith("| OT-") and not line.startswith("| ~~OT-"):
            continue
        cells = [c.replace("\\|", "|").replace("<br>", "\n").strip()
                 for c in SPLIT.split(line.strip()[2:-2])]
        key = cells[0].split(" · ")[0].replace("~", "").strip()
        out[key] = cells
    return out


def main(frozen_path, generated_path) -> int:
    frozen, gen = rows(frozen_path), rows(generated_path)
    print(f"frozen rows {len(frozen)}, generated rows {len(gen)}")
    print(f"only generated: {sorted(set(gen) - set(frozen), key=lambda k: int(k[3:]))}")
    print(f"only frozen: {sorted(set(frozen) - set(gen))}")
    names = {1: "thread", 2: "raised", 3: "comes back when"}
    bad = {n: [] for n in names.values()}
    status_missing = []
    for key, f in frozen.items():
        g = gen.get(key)
        if g is None or len(f) != 5 or len(g) != 5:
            print(f"  {key}: cell count frozen {len(f)} generated {len(g) if g else '-'}")
            continue
        for i, name in names.items():
            if f[i] != g[i]:
                bad[name].append(key)
        if f[4] not in g[4]:
            status_missing.append(key)
    for name, keys in bad.items():
        print(f"{name}: {len(frozen) - len(keys)} equal, {len(keys)} differ {keys[:10]}")
    print(f"old status text carried whole: {len(frozen) - len(status_missing)} of {len(frozen)}"
          f"{'; missing ' + str(status_missing[:10]) if status_missing else ''}")
    return 1 if any(bad.values()) or status_missing else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
