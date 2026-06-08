"""_assess_relationship_probe.py — READ-ONLY. For a cluster PAIR, pull the verses where both co-occur and
show, per verse: the verse text + each side's term with its morph-derived TYPE (verb≈ACTION, noun≈STATUS/
STATE, adj≈QUALITY). Grounds the "typed thing → relationship → effect" reframe in real verses so we can read
what the relationship actually does and whether the type axis (status vs action) is visible. NO DB writes.

Usage:  python scripts/_assess_relationship_probe.py --a M01 --b M23 --sample 12 --out <file>.md
"""
import argparse, os, re, sqlite3, sys
from collections import defaultdict
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
POS = {"V": "ACTION(verb)", "N": "STATUS(noun)", "A": "QUALITY(adj)", "D": "adverb", "R": "prep",
       "C": "conj", "T": "particle", "P": "pronoun", "S": "suffix"}


def pos_of(m):
    if not m:
        return "?"
    if m[0] == "H" and len(m) > 1:
        p = m[1]
    elif m[0] == "G" and len(m) > 2 and m[1] == "-":
        p = m[2]
    else:
        p = m[0]
    return POS.get(p, p)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True); ap.add_argument("--b", required=True)
    ap.add_argument("--sample", type=int, default=12); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; c = conn.cursor()
    name = {r["cluster_code"]: (r["short_name"] or r["cluster_code"])
            for r in c.execute("SELECT cluster_code, short_name FROM cluster")}
    clA = [r[0] for r in c.execute("SELECT id FROM mti_terms WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0", (a.a,))]
    clB = [r[0] for r in c.execute("SELECT id FROM mti_terms WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0", (a.b,))]
    setA, setB = set(clA), set(clB)

    # occurrences by reference for the two clusters
    occ = defaultdict(lambda: {"A": [], "B": [], "text": ""})
    qs = ",".join("?" * (len(clA) + len(clB)))
    for r in c.execute(f"SELECT reference, verse_text, transliteration, morph_code, mti_term_id "
                       f"FROM wa_verse_records WHERE COALESCE(delete_flagged,0)=0 AND reference IS NOT NULL "
                       f"AND mti_term_id IN ({qs})", clA + clB):
        side = "A" if r["mti_term_id"] in setA else "B"
        occ[r["reference"]][side].append((r["transliteration"], r["morph_code"]))
        if r["verse_text"]:
            occ[r["reference"]]["text"] = r["verse_text"]
    both = {ref: d for ref, d in occ.items() if d["A"] and d["B"]}

    L = [f"# Relationship probe — {name.get(a.a,a.a)} × {name.get(a.b,a.b)} (typed things in real verses)", ""]
    L.append("> READ-ONLY (`scripts/_assess_relationship_probe.py`). Verses where both clusters co-occur; each "
             "side's term shown with its morph-derived TYPE (verb≈ACTION, noun≈STATUS, adj≈QUALITY). Read to "
             "see what the relationship *does*, and whether the status/action axis is visible. No DB writes.")
    L.append("")
    L.append(f"**{len(both)} verses co-occur {name.get(a.a,a.a)} + {name.get(a.b,a.b)}.**")
    L.append("")
    # type mix on each side
    def typemix(side):
        cnt = defaultdict(int)
        for d in both.values():
            for _tl, m in d[side]:
                cnt[pos_of(m).split("(")[0]] += 1
        return ", ".join(f"{k}:{v}" for k, v in sorted(cnt.items(), key=lambda x: -x[1]))
    L.append(f"- **{name.get(a.a,a.a)}** side type-mix: {typemix('A')}")
    L.append(f"- **{name.get(a.b,a.b)}** side type-mix: {typemix('B')}")
    L.append("")
    L.append(f"### Sample verses (first {a.sample})")
    L.append(""); L.append(f"| Ref | Verse | {name.get(a.a,a.a)} (type) | {name.get(a.b,a.b)} (type) |")
    L.append("|---|---|---|---|")
    for ref, d in list(both.items())[:a.sample]:
        txt = re.sub(r"\s+", " ", (d["text"] or ""))[:90].replace("|", "/")
        astr = ", ".join(f"{t} [{pos_of(m)}]" for t, m in d["A"][:3])
        bstr = ", ".join(f"{t} [{pos_of(m)}]" for t, m in d["B"][:3])
        L.append(f"| {ref} | {txt} | {astr} | {bstr} |")
    L.append("")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"{a.a}x{a.b}: {len(both)} co-occur verses; A-mix [{typemix('A')}]; B-mix [{typemix('B')}]; wrote {a.out}")


if __name__ == "__main__":
    main()
