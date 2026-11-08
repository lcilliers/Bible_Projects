"""collection_batch_run.py -- build collections from the sub-groups of the bases not yet in any collection (escalation #2388), unattended, with the progress
control of lib/longrun.py.

    python -m iba.app.tools.collection_batch_run --job NAME --plan            # write the plan (one seed word per sub-group) and stop
    python -m iba.app.tools.collection_batch_run --job NAME --run [--limit n] # work through the plan: Seed then Ask per sub-group, Links every 10 and at the end
    Progress and Stop are Long-Run.ps1 (iba/app/ps/Long-Run.ps1); starting it detached is Long-Run.ps1 -Action Start.

The seed rule is the one used for the ten pilot collections: the words of a sub-group (kind group or qualifier) that are single words of behaviour or
inner_being_state; the seed is the word with the most occurrences among those whose dominant sub-group share is at least 0.5, else the most frequent. A
computed base cannot be a seed (only a surface word can be a collection's core). Every step is the ordinary Collection-Build.ps1 action, so every call is an
ai_call row. A re-run resumes: sub-groups already done are skipped, an existing collection of the seed is not seeded again, and Ask never re-asks a judged word."""
from __future__ import annotations

import argparse
import collections
import json
import pathlib
import shutil
import sqlite3
import subprocess
import sys
import time

from ..lib import longrun as lr

ROOT = lr.ROOT
DB = ROOT / "iba" / "app" / "db" / "iba.db"
PS = ROOT / "iba" / "app" / "ps" / "Collection-Build.ps1"
PWSH = shutil.which("pwsh") or r"C:\Program Files (x86)\PowerShell\7\pwsh.exe"
STEP_TIMEOUT = 90 * 60
MAX_FAILS_IN_A_ROW = 3
LINKS_EVERY = 10


def build_plan() -> list[dict]:
    c = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    q = lambda s, *a: c.execute(s, a).fetchall()
    bases = q("SELECT id, surface, origin, surface_group, form FROM surface_term WHERE deleted=0 AND collection_state='untouched'")
    members = collections.defaultdict(list)
    for i, s in q("SELECT base_id, surface FROM surface_term WHERE deleted=0 AND base_id IS NOT NULL"):
        members[i].append(s)
    occ = dict(q("SELECT surface, count(*) FROM verse_lexical WHERE deleted=0 AND surface IS NOT NULL GROUP BY surface"))
    subs = collections.defaultdict(collections.Counter)
    for surf, cl, sc, lab, kind in q("SELECT s.surface, s.cluster_code, g.subgroup_code, g.label, g.kind FROM surface_subgroup s "
                                     "LEFT JOIN cluster_subgroup g ON g.id=s.cluster_subgroup_id WHERE s.deleted=0"):
        subs[surf][(cl, sc, lab, kind)] += 1
    by_sub = collections.defaultdict(list)
    for i, surf, origin, grp, form in bases:
        if grp not in ("behaviour", "inner_being_state") or form != "word":
            continue
        sc = collections.Counter()
        for m in set(members.get(i, [])) | {surf}:
            sc.update(subs.get(m, {}))
        if not sc:
            continue
        top, n = sc.most_common(1)[0]
        if top[3] not in ("group", "qualifier"):
            continue
        by_sub[top].append(dict(base=surf, origin=origin, occ=sum(occ.get(m, 0) for m in set(members.get(i, [])) | {surf}), share=n / sum(sc.values())))
    plan = []
    for k, xs in by_sub.items():
        seedable = [x for x in xs if x["origin"] == "surface"]
        cand = sorted([x for x in seedable if x["share"] >= 0.5], key=lambda x: -x["occ"]) or sorted(seedable, key=lambda x: -x["occ"])
        plan.append(dict(cluster=k[0], subgroup=k[1], label=k[2], n=len(xs), seed=cand[0]["base"] if cand else None,
                         others=[x["base"] for x in sorted(xs, key=lambda x: -x["occ"]) if not cand or x is not cand[0]][:6]))
    plan.sort(key=lambda p: (-p["n"], p["subgroup"]))
    return plan


def ps(action: str, log, **params) -> tuple[int, str]:
    """One Collection-Build.ps1 action; its output is appended to the job log. Returns (exit code, last line of output)."""
    args = [PWSH, "-NoProfile", "-File", str(PS), "-Action", action] + [x for k, v in params.items() for x in (f"-{k}", str(v))]
    log.write(f"\n--- {lr.iso(time.time())} {action} {params}\n")
    log.flush()
    try:
        r = subprocess.run(args, cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=STEP_TIMEOUT)
    except subprocess.TimeoutExpired:
        log.write(f"timed out after {STEP_TIMEOUT} s\n")
        return 124, "timed out"
    out = (r.stdout or "") + (r.stderr or "")
    log.write(out)
    log.flush()
    lines = [x.strip() for x in out.splitlines() if x.strip()]
    # a refusal or a halt exits 0 (a usage outcome), so the output is read too
    bad = r.returncode != 0 or any(w in out for w in ("refused, nothing written", "halted", "Traceback"))
    step_line = next((x for x in reversed(lines) if x.startswith("collection.")), lines[-1] if lines else "")
    return (r.returncode or 1) if bad else 0, step_line


def has_collection(word: str) -> bool:
    c = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    return bool(c.execute("SELECT 1 FROM collection c JOIN surface_term t ON t.id=c.core_term_id WHERE t.surface=? AND c.deleted=0 AND c.status!='retired'", (word,)).fetchone())


def run(job: str, plan: list[dict], limit: int | None) -> int:
    prev = lr.read(job) or {}
    done_codes = set(prev.get("done_subgroups", []))
    todo = [p for p in plan if p["subgroup"] not in done_codes]
    if limit:
        todo = todo[:limit]
    p = lr.paths(job)
    fails = 0
    with p["log"].open("a", encoding="utf-8") as log, lr.Job(job, len(todo), extra={"done_subgroups": sorted(done_codes), "plan_total": len(plan),
                                                                                       "since_links": 0}) as j:
        for item in todo:
            if j.stop_asked():
                j.prog["state"] = "stopped"
                return 0
            t0 = time.time()
            j.write(current=f"{item['subgroup']} (seed {item['seed']}, {item['n']} words)", current_since=lr.iso(t0))
            if not item["seed"]:
                j.step_done(0, skipped=True)
                log.write(f"skipped {item['subgroup']}: no seedable word (all computed bases)\n")
                continue
            err = None
            if not has_collection(item["seed"]):
                rc, last = ps("Seed", log, Word=item["seed"])
                if rc != 0:
                    err = f"Seed {item['seed']}: {last}"
            if err is None:
                rc, last = ps("Ask", log, Collection=item["seed"])
                if rc != 0:
                    err = f"Ask {item['seed']}: {last}"
            if err:
                fails += 1
                j.step_done(time.time() - t0, ok_=False, error=err)
                if fails >= MAX_FAILS_IN_A_ROW:
                    j.prog["state"] = "halted"
                    return 3
                continue
            fails = 0
            done_codes.add(item["subgroup"])
            j.prog["done_subgroups"] = sorted(done_codes)
            j.prog["since_links"] += 1
            j.step_done(time.time() - t0)
            if j.prog["since_links"] >= LINKS_EVERY:
                ps("Links", log)
                j.prog["since_links"] = 0
        ps("Links", log)
        j.prog["state"] = "finished"
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--job", required=True)
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--limit", type=int)
    a = ap.parse_args()
    pf = lr.DIR / f"{a.job}.plan.json"
    lr.DIR.mkdir(parents=True, exist_ok=True)
    if a.plan or not pf.exists():
        plan = build_plan()
        pf.write_text(json.dumps(plan, indent=1), encoding="utf-8")
        print(f"plan: {len(plan)} sub-groups, {sum(1 for x in plan if not x['seed'])} without a seedable word -> {pf}")
        if a.plan:
            return 0
    if a.run:
        return run(a.job, json.loads(pf.read_text(encoding="utf-8")), a.limit)
    return 0


if __name__ == "__main__":
    sys.exit(main())
