"""Validate the FLAG classification JSON against the package schema + live FLAG set.

Read-only. Checks: structure, per-entry schema, valid dispositions, valid cluster
codes, t2/set_aside have empty target_clusters, and full/exact coverage of the
433 live FLAG terms (missing / extra / duplicate). Reports distributions.

Output: research/investigations/flag-classification-validation-20260601.md
"""
import json
import os
import sqlite3
from collections import Counter

DB = "database/bible_research.db"
JSONF = "Workflow/Clusters/wa-flag-cluster-classification-v1_0-20260601.json"
OUT = "research/investigations/flag-classification-validation-20260601.md"
DISP = {"cluster", "boundary", "t2", "set_aside"}


def main():
    c = sqlite3.connect(DB, timeout=15); c.row_factory = sqlite3.Row
    valid_clusters = {r["cluster_code"] for r in c.execute("SELECT cluster_code FROM cluster")}
    flag_strongs = {r["strongs_number"] for r in c.execute("SELECT DISTINCT strongs_number FROM mti_terms WHERE cluster_code='FLAG' AND COALESCE(delete_flagged,0)=0")}

    with open(JSONF, encoding="utf-8") as f:
        data = json.load(f)
    rows = data.get("classifications", [])

    errors = []
    seen = Counter()
    disp = Counter()
    target = Counter()
    classified = set()
    for i, r in enumerate(rows):
        sn = r.get("strongs")
        d = r.get("disposition")
        tc = r.get("target_clusters", [])
        seen[sn] += 1
        classified.add(sn)
        if not sn:
            errors.append(f"[{i}] missing strongs"); continue
        if d not in DISP:
            errors.append(f"{sn}: bad disposition '{d}'")
        if not isinstance(tc, list):
            errors.append(f"{sn}: target_clusters not a list")
            tc = []
        if d in ("cluster",) and len(tc) != 1:
            errors.append(f"{sn}: disposition=cluster needs exactly 1 target, got {tc}")
        if d == "boundary" and len(tc) < 2:
            errors.append(f"{sn}: disposition=boundary needs >=2 targets, got {tc}")
        if d in ("t2", "set_aside") and tc:
            errors.append(f"{sn}: disposition={d} must have empty target_clusters, got {tc}")
        for t in tc:
            if t not in valid_clusters:
                errors.append(f"{sn}: invalid cluster code '{t}'")
            target[t] += 1
        if not (r.get("reason") or "").strip():
            errors.append(f"{sn}: missing reason")
        disp[d] += 1

    dups = {s: n for s, n in seen.items() if n > 1}
    missing = flag_strongs - classified
    extra = classified - flag_strongs

    L = ["# FLAG classification — validation", "",
         f"**Source:** `{JSONF}` · package=`{data.get('package')}` · entries={len(rows)}", "",
         "## Coverage vs 433 live FLAG terms",
         f"- classified distinct strongs: {len(classified)}",
         f"- **missing (FLAG term not classified): {len(missing)}**",
         f"- **extra (classified but not a live FLAG term): {len(extra)}**",
         f"- **duplicate strongs in JSON: {len(dups)}**", "",
         "## Disposition distribution",
         *[f"- {k}: {v}" for k, v in disp.most_common()], "",
         f"## Schema errors: {len(errors)}",
         *[f"- {e}" for e in errors[:60]],
         (f"- … (+{len(errors)-60} more)" if len(errors) > 60 else ""), "",
         "## Cluster target distribution (cluster + boundary)",
         *[f"- {k}: {v}" for k, v in target.most_common()], ""]
    if missing:
        L += ["## Missing FLAG terms", "", ", ".join(sorted(missing)), ""]
    if extra:
        L += ["## Extra (not live FLAG)", "", ", ".join(sorted(extra)), ""]
    if dups:
        L += ["## Duplicate strongs", "", ", ".join(f"{s}×{n}" for s, n in dups.items()), ""]

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(x for x in L if x is not None) + "\n")
    print(f"entries={len(rows)} | classified={len(classified)} | missing={len(missing)} | extra={len(extra)} | dups={len(dups)} | errors={len(errors)}")
    print("dispositions:", dict(disp))
    print("wrote:", OUT)
    c.close()


if __name__ == "__main__":
    main()
