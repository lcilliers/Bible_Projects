"""_prototype_finding_lifecycle.py — READ-ONLY prototype of the finding correction cycle. Loads a findings
store (JSON), applies clarification-driven CORRECTION directives, records full provenance per change
(from -> to, reason, clarification, date), writes a new store version + a report. Demonstrates two cases:
(a) a FORCED finding un-induced (state-not-induce), (b) an ESCALATED finding resolved by a new clarification.
Operates on the prototype JSON store, NOT the DB.

Usage:  python scripts/_prototype_finding_lifecycle.py --store IN.json --out-store OUT.json --out REPORT.md --date YYYY-MM-DD
"""
import argparse, json, os, sys
sys.stdout.reconfigure(encoding="utf-8")

# Authored correction directives (the JUDGEMENT). Each: target id, the clarification driving it, the reason,
# and the field changes. The script applies + records provenance mechanically.
DIRECTIVES = [
    {
        "id": "M01-0007", "clarification": "REVOKE god-present->reverence (it INDUCES); apply "
        "fear-of-God-as-threat->dread where the verse shows a dread/woe posture",
        "reason": "FORCED FINDING un-induced: 1Sa 4:7 'the Philistines were afraid ... Woe to us! ... who can "
        "deliver us from these mighty gods?' is dread of God-as-threat, not reverence. god-present alone does "
        "not resolve the shade; the dread posture, read in the verse, does.",
        "set": {
            "lexical_meaning": "to fear / dread",
            "tiers.T7.1": "to fear -> dread (Qal; fear of God-as-threat, dread/woe posture read in verse)",
            "tiers.T1.4": "Qal -> dread shade",
            "triage": "ACCEPT",
            "provenance": "clarification:fear-of-God-as-threat->dread (signal read in verse) — supersedes the induced god->reverence"
        }
    },
    {
        "id": "M01-0008", "clarification": "ADD god-addressed-as-'you' counts as a god-object; "
        "covenant-obedience-life context ('fear you all the days they live') -> reverence",
        "reason": "ESCALATED then RESOLVED by a new clarification: 1Ki 8:40 'that they may fear you all the "
        "days that they live' — God is the object (as 'you'), in a covenant-obedience-life frame -> reverence. "
        "The earlier escalate was a detection gap, not genuine silence.",
        "set": {
            "lexical_meaning": "to fear = revere",
            "tiers.T7.1": "to fear -> revere (Qal; God as 'you', covenant-obedience-life context)",
            "tiers.T1.4": "Qal -> reverence shade",
            "tiers.T3": "affect + moral-evaluation (reverent obedience posture)",
            "triage": "ACCEPT",
            "provenance": "clarification:god-as-you-covenant-life->reverence (resolves prior escalate)"
        }
    }
]


def get(d, path):
    cur = d
    for k in path.split("."):
        cur = cur.get(k, {}) if isinstance(cur, dict) else None
    return cur if not isinstance(cur, dict) or cur else cur


def set_path(d, path, val):
    ks = path.split("."); cur = d
    for k in ks[:-1]:
        cur = cur.setdefault(k, {})
    old = cur.get(ks[-1])
    cur[ks[-1]] = val
    return old


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--store", required=True); ap.add_argument("--out-store", required=True)
    ap.add_argument("--out", required=True); ap.add_argument("--date", required=True)
    a = ap.parse_args()
    store = json.load(open(a.store, encoding="utf-8"))
    by_id = {f["id"]: f for f in store["findings"]}

    L = ["# Finding correction cycle — prototype run", ""]
    L.append(f"> READ-ONLY (`scripts/_prototype_finding_lifecycle.py`, {a.date}). Applies clarification-driven "
             "corrections to the findings store, recording provenance per change. Demonstrates (a) un-inducing "
             "a forced finding, (b) resolving an escalated finding by a new clarification. Not the DB.")
    L.append("")
    L.append(f"**Store: {len(store['findings'])} findings · {len(DIRECTIVES)} corrections applied.**")
    L.append("")
    for d in DIRECTIVES:
        f = by_id.get(d["id"])
        if not f:
            L.append(f"- ⚠ {d['id']} not found"); continue
        L.append(f"## {d['id']} — {f['term']} @ {f['verse']}")
        L.append(f"- **Clarification:** {d['clarification']}")
        L.append(f"- **Reason:** {d['reason']}")
        L.append("")
        L.append("| field | from | to |"); L.append("|---|---|---|")
        for path, newv in d["set"].items():
            old = set_path(f, path, newv)
            f.setdefault("corrections", []).append(
                {"date": a.date, "field": path, "from": old, "to": newv,
                 "reason": d["reason"], "clarification": d["clarification"]})
            L.append(f"| `{path}` | {old} | **{newv}** |")
        f["status"] = "corrected"
        L.append("")

    json.dump(store, open(a.out_store, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    L.append("---")
    L.append(f"Updated store written: `{os.path.basename(a.out_store)}` — each corrected finding now carries "
             "its `corrections[]` provenance (from/to/reason/clarification/date); status -> `corrected`.")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"applied {len(DIRECTIVES)} corrections; wrote {a.out_store} + {a.out}")


if __name__ == "__main__":
    main()
