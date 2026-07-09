"""Content-mine Session B/D pointer TEXT for hooks to term / verse / cluster.

Read-only. For each pointer (wa_session_b_findings + wa_session_research_flags
pointer flags) extract from its free text + structured text fields:
  - Strong's codes      [HG]\\d+[A-Z]?         -> term -> cluster
  - verse references    Book c:v               -> wa_verse_records -> term -> cluster
  - registry mentions   'Reg NNN' / 'Reg=NNN'  -> registry
  - transliteration hit  normalised substring   -> term -> cluster   (fuzzy, lower confidence)
plus the dedicated anchor_verses / strongs_reference columns.

Classify each pointer:
  - ROUTABLE  : at least one hook resolves to a cluster (M/FLAG/T2) or a verse/term/registry
  - NO-HOOK   : no extractable hook at all -> low structural value (soft-delete candidate)

Outputs (NO db writes):
  research/investigations/session-bd-pointers-content-mining-20260601.md   (analysis + low-value list)
"""
import os
import re
import sqlite3
import unicodedata
from collections import Counter, defaultdict

DB = "database/bible_research.db"
OUT = "research/investigations/session-bd-pointers-content-mining-20260601.md"
M_RE = re.compile(r"^M\d")
STRONGS_RE = re.compile(r"\b([HG]\d{1,4}[A-Z]?)\b")
VERSE_RE = re.compile(r"\b([1-3]?\s?[A-Z][a-zA-Z]{1,4})\.?\s+(\d{1,3}):(\d{1,3})")
REG_RE = re.compile(r"\bReg(?:istry)?[\s=]*0*(\d{1,3})\b", re.I)


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

    # strongs -> cluster
    sc = defaultdict(set)
    for r in cur.execute("SELECT strongs_number sn, cluster_code cc FROM mti_terms"):
        sc[r["sn"]].add(r["cc"])
    smap = {sn: cluster_of(cl) for sn, cl in sc.items()}

    # normalised reference -> set(clusters), from active span verse records
    ref_clusters = defaultdict(set)
    for r in cur.execute("SELECT reference, term_id FROM wa_verse_records WHERE span_strong_match=1 AND COALESCE(delete_flagged,0)=0 AND reference IS NOT NULL"):
        c = smap.get(r["term_id"])
        ref_clusters[norm(r["reference"])].add(c)
    ref_set = set(ref_clusters)

    # transliteration -> cluster (len>=5 normalised, to limit noise)
    tmap = {}
    for r in cur.execute("SELECT transliteration tr, strongs_number sn FROM mti_terms WHERE transliteration IS NOT NULL"):
        n = norm(r["tr"])
        if len(n) >= 5:
            tmap.setdefault(n, smap.get(r["sn"]))
    translits = sorted(tmap, key=len, reverse=True)

    def mine(text):
        text = text or ""
        strongs = set(STRONGS_RE.findall(text))
        verses = set()
        for m in VERSE_RE.finditer(text):
            ref = norm(f"{m.group(1)}{m.group(2)}:{m.group(3)}")
            if ref in ref_set:
                verses.add(ref)
        regs = set(REG_RE.findall(text))
        ntext = norm(text)
        thits = set(t for t in translits if t in ntext)
        # clusters resolved
        cl = set()
        for s in strongs:
            if smap.get(s):
                cl.add(smap[s])
        for v in verses:
            cl |= {c for c in ref_clusters[v] if c}
        for t in thits:
            if tmap.get(t):
                cl.add(tmap[t])
        return strongs, verses, regs, thits, cl

    def analyse(label, rows, textfn, extra_verse_fn=None):
        out = {"n": len(rows), "strongs": 0, "verse": 0, "reg": 0, "translit": 0,
               "cluster": 0, "any_hook": 0, "nohook": []}
        for r in rows:
            s, v, g, t, cl = mine(textfn(r))
            if extra_verse_fn:  # anchor_verses column adds verse hooks
                for m in VERSE_RE.finditer(extra_verse_fn(r) or ""):
                    ref = norm(f"{m.group(1)}{m.group(2)}:{m.group(3)}")
                    if ref in ref_set:
                        v.add(ref); cl |= {c for c in ref_clusters[ref] if c}
            if s:
                out["strongs"] += 1
            if v:
                out["verse"] += 1
            if g:
                out["reg"] += 1
            if t:
                out["translit"] += 1
            if cl:
                out["cluster"] += 1
            if s or v or g or t:
                out["any_hook"] += 1
            else:
                out["nohook"].append(r)
        return out, label

    # populations
    findings = cur.execute("SELECT id, finding_type ft, status, registry_id reg, anchor_verses av, finding FROM wa_session_b_findings WHERE COALESCE(delete_flag,0)=0").fetchall()
    fa, _ = analyse("wa_session_b_findings", findings, lambda r: r["finding"], lambda r: r["av"])

    flag_results = {}
    for code in ("SD_POINTER", "SB_FINDING", "SB_INNER_BEING", "SD_CLUSTER"):
        rows = cur.execute("SELECT id, registry_id reg, flag_label fl, description d, strongs_reference sr FROM wa_session_research_flags WHERE flag_code=?", (code,)).fetchall()
        res, _ = analyse(code, rows, lambda r: (r["fl"] or "") + " " + (r["d"] or ""))
        flag_results[code] = res

    def pct(a, b):
        return f"{a} ({round(100*a/b) if b else 0}%)"

    L = ["# Session B/D pointers — content mining for term/verse/cluster hooks", "",
         "**Generated:** 2026-06-01 (read-only, NO writes). Mines the free text + anchor/strongs columns for Strong's codes, verse references, `Reg NNN` mentions, and transliteration/gloss matches; resolves each to a cluster where possible. Flags no-hook pointers as low-value (soft-delete) candidates for study.", "",
         f"Reference data: {len(smap)} strongs→cluster; {len(ref_set)} distinct verse refs; {len(tmap)} transliterations (≥5 chars).", "",
         "## Routability by content (vs the dedicated columns)", "",
         "| population | n | has Strong's | has verse ref | has Reg | has translit | **resolves to cluster** | no hook at all |",
         "|---|--:|--:|--:|--:|--:|--:|--:|"]
    for res, lab in [(fa, "wa_session_b_findings")] + [(flag_results[c], c) for c in ("SD_POINTER", "SB_FINDING", "SB_INNER_BEING", "SD_CLUSTER")]:
        n = res["n"]
        L.append(f"| {lab} | {n} | {pct(res['strongs'],n)} | {pct(res['verse'],n)} | {pct(res['reg'],n)} | {pct(res['translit'],n)} | **{pct(res['cluster'],n)}** | {len(res['nohook'])} |")

    # low-value candidates (no hook), shortest first
    L += ["", "## Low-value / soft-delete candidates (no extractable hook)", "",
          "These carry no Strong's, verse, registry, or transliteration hook. Sorted shortest-text first (most likely nonsense). **For your study — nothing is deleted.**", ""]
    for res, lab in [(fa, "wa_session_b_findings")] + [(flag_results[c], c) for c in ("SD_POINTER", "SB_FINDING", "SB_INNER_BEING", "SD_CLUSTER")]:
        nh = res["nohook"]
        if not nh:
            continue
        L += [f"### {lab} — {len(nh)} no-hook", "", "| id | type/label | text |", "|---|---|---|"]
        def keytext(r):
            return r["finding"] if "finding" in r.keys() else ((r["fl"] or "") + " " + (r["d"] or ""))
        for r in sorted(nh, key=lambda r: len(keytext(r) or "")):
            txt = (keytext(r) or "").replace("|", "/").replace("\n", " ")
            txt = (txt[:140] + "…") if len(txt) > 141 else txt
            lab2 = (r["ft"] if "ft" in r.keys() else r["fl"]) or ""
            L.append(f"| {r['id']} | {str(lab2)[:28]} | {txt} |")
        L.append("")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("findings:", {k: fa[k] for k in ("n", "strongs", "verse", "reg", "translit", "cluster")}, "nohook", len(fa["nohook"]))
    for c in ("SD_POINTER", "SB_FINDING", "SB_INNER_BEING", "SD_CLUSTER"):
        r = flag_results[c]
        print(c, {k: r[k] for k in ("n", "strongs", "verse", "reg", "translit", "cluster")}, "nohook", len(r["nohook"]))
    print("wrote:", OUT)
    conn.close()


if __name__ == "__main__":
    main()
