"""Linking design input + no-link retention set for Session B/D pointers.

Read-only. Resolves each pointer to its cluster SET using term/verse/gloss ONLY
(registry is NOT a cluster route — clusters are agnostic to registries). Reports:
  - resolution by confidence: HIGH (Strong's + verse) vs +gloss(translit)
  - how many clusters each resolving pointer maps to (1 / 2 / 3+)  [the many-to-many reality]
  - the NO-LINK set (resolves to zero clusters even with gloss) -> retention study

Output: research/investigations/session-bd-pointers-linking-20260601.md   (NO db writes)
"""
import os
import re
import sqlite3
import unicodedata
from collections import Counter, defaultdict

DB = "database/bible_research.db"
OUT = "research/investigations/session-bd-pointers-linking-20260601.md"
M_RE = re.compile(r"^M\d")
STRONGS_RE = re.compile(r"\b([HG]\d{1,4}[A-Z]?)\b")
VERSE_RE = re.compile(r"\b([1-3]?\s?[A-Z][a-zA-Z]{1,4})\.?\s+(\d{1,3}):(\d{1,3})")


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s.\-]", "", s.lower())


def cluster_of(clusters):
    real = [c for c in clusters if c and M_RE.match(c)]
    if real:
        return real[0] if len(set(real)) == 1 else "Mxx"
    if "FLAG" in clusters:
        return "FLAG"
    if "T2" in clusters:
        return "T2"
    return None


def main():
    conn = sqlite3.connect(DB, timeout=10)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    sc = defaultdict(set)
    for r in cur.execute("SELECT strongs_number sn, cluster_code cc FROM mti_terms"):
        sc[r["sn"]].add(r["cc"])
    smap = {sn: cluster_of(cl) for sn, cl in sc.items()}

    ref_clusters = defaultdict(set)
    for r in cur.execute("SELECT reference, term_id FROM wa_verse_records WHERE span_strong_match=1 AND COALESCE(delete_flagged,0)=0 AND reference IS NOT NULL"):
        c = smap.get(r["term_id"])
        if c:
            ref_clusters[norm(r["reference"])].add(c)
    ref_set = set(ref_clusters) | {norm(r["reference"]) for r in cur.execute("SELECT DISTINCT reference FROM wa_verse_records WHERE reference IS NOT NULL")}

    tmap = {}
    for r in cur.execute("SELECT transliteration tr, strongs_number sn FROM mti_terms WHERE transliteration IS NOT NULL"):
        n = norm(r["tr"])
        if len(n) >= 5 and smap.get(r["sn"]):
            tmap.setdefault(n, smap[r["sn"]])
    translits = sorted(tmap, key=len, reverse=True)

    def resolve(text, anchor=""):
        text = (text or "") + " " + (anchor or "")
        hi = set()                      # high-confidence clusters (strongs + verse)
        for s in set(STRONGS_RE.findall(text)):
            if smap.get(s):
                hi.add(smap[s])
        for m in VERSE_RE.finditer(text):
            ref = norm(f"{m.group(1)}{m.group(2)}:{m.group(3)}")
            if ref in ref_clusters:
                hi |= ref_clusters[ref]
        ntext = norm(text)
        lo = set(tmap[t] for t in translits if t in ntext)   # gloss/translit clusters
        return hi, lo

    def analyse(rows, textfn, anchorfn=None):
        hi_res = 0; any_res = 0; nolink = []; ccount = Counter()
        for r in rows:
            hi, lo = resolve(textfn(r), anchorfn(r) if anchorfn else "")
            allc = hi | lo
            if hi:
                hi_res += 1
            if allc:
                any_res += 1
                ccount[min(len(allc), 3)] += 1   # 1,2,3(=3+)
            else:
                nolink.append(r)
        return {"n": len(rows), "hi": hi_res, "any": any_res, "ccount": ccount, "nolink": nolink}

    findings = cur.execute("SELECT id, finding_type ft, status, anchor_verses av, finding FROM wa_session_b_findings WHERE COALESCE(delete_flag,0)=0").fetchall()
    fa = analyse(findings, lambda r: r["finding"], lambda r: r["av"])

    flagres = {}
    for code in ("SD_POINTER", "SB_FINDING", "SB_INNER_BEING", "SD_CLUSTER"):
        rows = cur.execute("SELECT id, flag_label fl, description d FROM wa_session_research_flags WHERE flag_code=?", (code,)).fetchall()
        flagres[code] = analyse(rows, lambda r: (r["fl"] or "") + " " + (r["d"] or ""))

    def cc(d):
        return f"1→{d.get(1,0)}, 2→{d.get(2,0)}, 3+→{d.get(3,0)}"

    L = ["# Session B/D pointers — cluster-link design input & no-link retention set", "",
         "**Generated:** 2026-06-01 (read-only). Cluster link via **term/verse/gloss only** — registry is NOT a cluster route (clusters are agnostic to registries).", "",
         "## Resolution (registry excluded)", "",
         "| population | n | HIGH-conf link (Strong's+verse) | any link (incl gloss) | NO link | clusters-per-pointer (any) |",
         "|---|--:|--:|--:|--:|---|"]
    for lab, res in [("wa_session_b_findings", fa)] + [(c, flagres[c]) for c in ("SD_POINTER", "SB_FINDING", "SB_INNER_BEING", "SD_CLUSTER")]:
        n = res["n"]
        L.append(f"| {lab} | {n} | {res['hi']} | {res['any']} | {len(res['nolink'])} | {cc(res['ccount'])} |")

    L += ["", "**Many-to-one reality:** the *clusters-per-pointer* column shows how many distinct clusters each resolving pointer touches — most findings span **multiple** clusters (via their anchor verses), so a single-value link field would be lossy.", ""]

    # no-link lists (retention study)
    L += ["## No-link items (term/verse/gloss all empty) — retention study", "",
          "Nothing resolves these to a cluster. **For your retain/soft-delete judgement — nothing written.**", ""]
    for lab, res, fields in [("wa_session_b_findings", fa, ("ft", "finding")),
                             ("SD_POINTER", flagres["SD_POINTER"], ("fl", "d")),
                             ("SB_FINDING", flagres["SB_FINDING"], ("fl", "d"))]:
        nl = res["nolink"]
        if not nl:
            continue
        L += [f"### {lab} — {len(nl)} no-link", "", "| id | label/type | text |", "|---|---|---|"]
        for r in sorted(nl, key=lambda r: len((r[fields[1]] or ""))):
            lab2 = str(r[fields[0]] or "")[:26]
            txt = (r[fields[1]] or "").replace("|", "/").replace("\n", " ")
            txt = (txt[:150] + "…") if len(txt) > 151 else txt
            L.append(f"| {r['id']} | {lab2} | {txt} |")
        L.append("")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("findings:", {k: fa[k] for k in ("n", "hi", "any")}, "nolink", len(fa["nolink"]), "clusters/ptr", dict(fa["ccount"]))
    for c in ("SD_POINTER", "SB_FINDING", "SB_INNER_BEING", "SD_CLUSTER"):
        r = flagres[c]
        print(c, {k: r[k] for k in ("n", "hi", "any")}, "nolink", len(r["nolink"]), "clusters/ptr", dict(r["ccount"]))
    print("wrote:", OUT)
    conn.close()


if __name__ == "__main__":
    main()
