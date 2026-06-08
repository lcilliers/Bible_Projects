"""_assess_verse_assembly.py — READ-ONLY. L1 establishment per verse for a cluster: assembles each verse's
full TYPED ARRAY — the in-scope thing(s) with type (ACTION/STATUS/QUALITY) + morph stem + the BDB sense-branch
that stem selects + keywords; the co-occurring OTHER-cluster things (faculty + type); and any T2 qualifiers.
This is the raw material the verse-read turns into a typed-relationship finding. NO DB writes.

Usage:  python scripts/_assess_verse_assembly.py --cluster M01 [--strongs H..,H..] [--limit N] --out <file>.md
"""
import argparse, os, re, sqlite3, sys
from collections import defaultdict
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
POSm = {"V": "ACTION", "N": "STATUS", "A": "QUALITY"}
STEM_MARK = re.compile(r"\((Qal|Niphal|Piel|Pual|Hiphil|Hophal|Hithpael|Polel|Pilpel|Poel|Tiphil|Polpal)\)", re.I)


def pos_of(m):
    if not m: return "?"
    if m[0] == "H" and len(m) > 1: p = m[1]
    elif m[0] == "G" and len(m) > 2 and m[1] == "-": p = m[2]
    else: p = m[0]
    return POSm.get(p, "·")


def branches(sense_text):
    t = sense_text or ""; out = {}
    marks = list(STEM_MARK.finditer(t))
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(t)
        seg = re.sub(r"\s+", " ", t[m.end():end]).strip().strip(":").strip()
        seg = re.split(r"\s\d+\)\s", seg)[0][:70]
        out[m.group(1).capitalize()] = seg
    if not out:  # no stem branches: take the head sense
        head = re.sub(r"\s+", " ", t).strip()[:70]
        out["_"] = head
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True); ap.add_argument("--strongs"); ap.add_argument("--limit", type=int)
    ap.add_argument("--out", required=True); a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; c = conn.cursor()
    name = {r["cluster_code"]: (r["short_name"] or r["cluster_code"])
            for r in c.execute("SELECT cluster_code, short_name FROM cluster")}
    # term meta
    meta = {}  # mti_id -> dict
    for r in c.execute("SELECT m.id mid, m.cluster_code cc, m.strongs_number sn, m.transliteration tl, "
                       "ti.parsed_meaning_id pmid FROM mti_terms m "
                       "LEFT JOIN wa_term_inventory ti ON ti.strongs_number=m.strongs_number AND COALESCE(ti.delete_flagged,0)=0 "
                       "WHERE m.cluster_code IS NOT NULL AND m.cluster_code NOT IN ('FLAG') "
                       "AND COALESCE(m.delete_flagged,0)=0 GROUP BY m.id"):
        meta[r["mid"]] = {"cc": r["cc"], "sn": r["sn"], "tl": r["tl"], "pmid": r["pmid"], "br": None}
    # branch parse for in-cluster terms (lazy: only the cluster's terms)
    for mid, d in meta.items():
        if d["cc"] == a.cluster and d["pmid"]:
            row = c.execute("SELECT group_concat(sense_text, '\n') st FROM wa_meaning_sense WHERE parsed_meaning_id=?",
                            (d["pmid"],)).fetchone()
            d["br"] = branches(row["st"] or "")
    # per-term dominant type (from morph)
    typ = defaultdict(lambda: defaultdict(int))
    for r in c.execute("SELECT mti_term_id, morph_code FROM wa_verse_records WHERE COALESCE(delete_flagged,0)=0 "
                       "AND mti_term_id IS NOT NULL AND morph_code IS NOT NULL"):
        if r["mti_term_id"] in meta:
            typ[r["mti_term_id"]][pos_of(r["morph_code"])] += 1
    def term_type(mid):
        d = typ.get(mid)
        return max(d, key=d.get) if d else "?"

    # target terms
    tgt = [mid for mid, d in meta.items() if d["cc"] == a.cluster]
    if a.strongs:
        want = set(a.strongs.split(","))
        tgt = [mid for mid in tgt if meta[mid]["sn"] in want]
    tgtset = set(tgt)

    # refs that contain a target term, and all occurrences at those refs
    qs = ",".join("?" * len(tgt))
    refs = [r[0] for r in c.execute(f"SELECT DISTINCT reference FROM wa_verse_records WHERE COALESCE(delete_flagged,0)=0 "
                                    f"AND reference IS NOT NULL AND mti_term_id IN ({qs})", tgt)]
    refs = sorted(refs)
    if a.limit: refs = refs[:a.limit]
    occ = defaultdict(list); text = {}
    qr = ",".join("?" * len(refs))
    for r in c.execute(f"SELECT reference, verse_text, transliteration, morph_code, stem, mti_term_id FROM wa_verse_records "
                       f"WHERE COALESCE(delete_flagged,0)=0 AND reference IN ({qr})", refs):
        occ[r["reference"]].append(r)
        if r["verse_text"]: text[r["reference"]] = r["verse_text"]

    L = [f"# Verse assembly — L1 establishment: {a.cluster} ({name.get(a.cluster,a.cluster)})", ""]
    L.append("> READ-ONLY (`scripts/_assess_verse_assembly.py`). Per verse: the in-cluster thing(s) "
             "[TYPE · stem→sense] · co-occurring other-faculty things [cluster·TYPE] · qualifiers. Input to "
             "the verse-read. No DB writes.")
    L.append("")
    L.append(f"**{len(refs)} verses assembled.**")
    L.append("")
    for ref in refs:
        rows = occ[ref]
        infac = [r for r in rows if r["mti_term_id"] in tgtset]
        other = [r for r in rows if meta.get(r["mti_term_id"], {}).get("cc") not in (a.cluster, "T2", None)
                 and r["mti_term_id"] in meta]
        qual = [r for r in rows if meta.get(r["mti_term_id"], {}).get("cc") == "T2"]
        L.append(f"### {ref}")
        L.append(f"> {re.sub(r'\\s+', ' ', (text.get(ref) or ''))[:200]}")
        for r in infac:
            d = meta[r["mti_term_id"]]; st = r["stem"] or "_"
            br = (d["br"] or {}).get(st) or (d["br"] or {}).get("_") or ""
            L.append(f"- **{r['transliteration']}** [{term_type(r['mti_term_id'])}"
                     f"{('·'+st) if r['stem'] else ''}] → {br}")
        if other:
            os_ = ", ".join(f"{r['transliteration']}({name.get(meta[r['mti_term_id']]['cc'])}·{term_type(r['mti_term_id'])})"
                            for r in other)
            L.append(f"- _other faculties:_ {os_}")
        if qual:
            L.append(f"- _qualifiers:_ {', '.join(r['transliteration'] for r in qual)}")
        L.append("")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"{a.cluster}: assembled {len(refs)} verses ({len(tgt)} target terms); wrote {a.out}")


if __name__ == "__main__":
    main()
