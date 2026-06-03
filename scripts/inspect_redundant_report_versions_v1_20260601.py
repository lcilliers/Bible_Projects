"""Read-only sweep: find superseded version-siblings among reports / Workflow docs.

Per docs/file-organisation-rules.md §2.3/§4: files differing only by version (-vN)
or date are the same logical document; only the latest stays active, older →
the folder's archive/. This script IDENTIFIES candidates; it makes NO changes.

Scope: outputs/, Workflow/, research/, Logs/. EXCLUDES Sessions/ and any path
already under an archive/ folder. Excludes code (.py) and the file manifest.

Output: a categorised report to research/investigations/ —
  (1) HIGH-CONFIDENCE: explicit -vN version-siblings (older = archive).
  (2) DATE-ONLY siblings: same base, differ only by date (lower confidence;
      session logs / snapshots may be intentional history — flag, don't assume).
Single-version / version-less files are left out (nothing to archive).

  python scripts/inspect_redundant_report_versions_v1_20260601.py
"""
import os
import re
from collections import defaultdict
from datetime import datetime

ROOTS = ["outputs", "Workflow", "research", "Logs"]
EXTS = {".md", ".json", ".docx", ".pdf", ".txt", ".jsonl", ".csv"}
SKIP_PARTS = {"archive", "Sessions", "__pycache__"}

VER_RE = re.compile(r"[-_]v(\d+)(?:_(\d+))?", re.IGNORECASE)
DATE_RE = re.compile(r"[-_](\d{8})|[-_](\d{4}-\d{2}-\d{2})")


def parse(fname):
    stem, ext = os.path.splitext(fname)
    ver = VER_RE.search(stem)
    vmaj = int(ver.group(1)) if ver else None
    vmin = int(ver.group(2)) if (ver and ver.group(2)) else 0
    dm = DATE_RE.search(stem)
    date = (dm.group(1) or (dm.group(2) or "").replace("-", "")) if dm else None
    base = VER_RE.sub("", stem)
    base = DATE_RE.sub("", base).strip("-_")
    return base, ext, vmaj, vmin, date


def main():
    groups = defaultdict(list)  # (dir, base, ext) -> [(fname, vmaj, vmin, date, path)]
    for root in ROOTS:
        if not os.path.isdir(root):
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in SKIP_PARTS]
            if any(p in SKIP_PARTS for p in dirpath.replace("\\", "/").split("/")):
                continue
            for fn in filenames:
                ext = os.path.splitext(fn)[1].lower()
                if ext not in EXTS or fn == "file_manifest.json":
                    continue
                base, e, vmaj, vmin, date = parse(fn)
                groups[(dirpath, base, e)].append((fn, vmaj, vmin, date, os.path.join(dirpath, fn)))

    hi, dateonly = [], []
    for (d, base, e), members in groups.items():
        if len(members) < 2:
            continue
        has_ver = any(m[1] is not None for m in members)
        # rank: date desc, then version desc
        def key(m):
            return (m[3] or "00000000", m[1] or -1, m[2] or 0)
        ranked = sorted(members, key=key, reverse=True)
        keep, superseded = ranked[0], ranked[1:]
        rec = {"dir": d, "base": base, "ext": e, "keep": keep[0], "supersede": [s[0] for s in superseded],
               "paths": [s[4] for s in superseded]}
        (hi if has_ver else dateonly).append(rec)

    L = ["# Redundant report-version sweep (read-only candidates)", "",
         f"Generated {datetime.now():%Y-%m-%d %H:%M}. Scope: {', '.join(ROOTS)} (excl. Sessions/, archive/). No changes made.", ""]
    L.append(f"## (1) HIGH-CONFIDENCE — explicit -vN version-siblings ({sum(len(r['supersede']) for r in hi)} files to archive)")
    L.append("")
    for r in sorted(hi, key=lambda r: r["dir"]):
        L.append(f"- `{r['dir']}` · **{r['base']}{r['ext']}**")
        L.append(f"    keep: {r['keep']}")
        for s in r["supersede"]:
            L.append(f"    archive -> {s}")
    L.append("")
    L.append(f"## (2) DATE-ONLY siblings — needs judgement ({sum(len(r['supersede']) for r in dateonly)} files; may be intentional history)")
    L.append("")
    for r in sorted(dateonly, key=lambda r: r["dir"]):
        L.append(f"- `{r['dir']}` · **{r['base']}{r['ext']}** — keep {r['keep']}; older: {', '.join(r['supersede'])}")

    out = os.path.join("research", "investigations", f"redundant-report-version-sweep-{datetime.now():%Y%m%d}.md")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(f"HIGH-CONFIDENCE version-siblings to archive: {sum(len(r['supersede']) for r in hi)} files across {len(hi)} docs")
    print(f"DATE-ONLY siblings (needs judgement): {sum(len(r['supersede']) for r in dateonly)} files across {len(dateonly)} docs")
    print(f"Report: {out}")


if __name__ == "__main__":
    main()
