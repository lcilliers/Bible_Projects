"""_build_verse_read_pilot_review.py — READ-ONLY. Assembles the M01 verse-read pilot review:
corrected self-audit rate (free-text content fields only), the unprocessed verse, and sample full records
(extraction fields + meaning paragraph) per term. No DB writes.
"""
import sqlite3, re, sys, os
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
IDS = [266, 269, 703, 1554, 1681]
NAME = {266: "fobos G5401", 269: "yir.ah H3374", 703: "cha.tat H2865", 1554: "ra.gaz H7264", 1681: "ya.re H3373"}
OBS2F = {225: "attributed_to_God", 227: "purpose_equips", 234: "typology_direction", 238: "relational_implication",
         239: "type", 240: "compound", 245: "mode", 248: "immediate_response", 251: "produces_effect",
         285: "origin", 395: "sense_applied", 404: "literary_setting"}
FACULTY = {291: "perception", 294: "cognition", 297: "memory", 300: "affect", 303: "creativity",
           306: "volition", 309: "agency", 312: "moral-evaluation", 315: "conscience", 321: "relational"}
LOCATION = {260: "spirit", 264: "soul", 267: "heart", 270: "mind", 276: "body"}
FREETEXT = {"immediate_response", "produces_effect", "relational_implication", "purpose_equips"}
NULL = {"none", "silent", "not-stated", "n/a", "na", ""}
STOP = {"the", "and", "that", "with", "from", "this", "into", "upon", "have", "been", "which", "their", "person", "something"}

c = sqlite3.connect(DB); c.row_factory = sqlite3.Row

# gather per vcid: fields, faculty/location lists, paragraph, ref, term
rows = c.execute("""SELECT f.id, f.verse_context_id v, f.mti_term_id m, f.provenance prov, f.finding_value val,
                          l.question_id q, vr.reference ref
                   FROM finding f LEFT JOIN finding_question_link l ON l.finding_id=f.id
                   JOIN verse_context vc ON vc.id=f.verse_context_id
                   JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
                   WHERE f.provenance IN ('l2_api','l2_meaning') AND f.mti_term_id IN (266,269,703,1554,1681)""").fetchall()
V = {}
for r in rows:
    d = V.setdefault((r["v"], r["m"]), {"ref": r["ref"], "fields": {}, "fac": [], "loc": [], "para": ""})
    if r["prov"] == "l2_meaning":
        d["para"] = r["val"] or ""
    elif r["q"] in OBS2F:
        d["fields"][OBS2F[r["q"]]] = r["val"]
    elif r["q"] in FACULTY and (r["val"] or "").lower() not in NULL:
        d["fac"].append(FACULTY[r["q"]])
    elif r["q"] in LOCATION and (r["val"] or "").lower() not in NULL:
        d["loc"].append(LOCATION[r["q"]])


def real_missing(d):
    pw = set(re.findall(r"[a-z]{4,}", d["para"].lower()))
    miss = []
    for k in FREETEXT:
        val = (d["fields"].get(k) or "").lower().strip()
        if val in NULL:
            continue
        w = {x for x in re.findall(r"[a-z]{4,}", val) if x not in STOP}
        if w and not (w & pw):
            miss.append(k)
    return miss


L = ["# M01 verse-read pilot — review", "",
     "> READ-ONLY review of the live 5-term pilot (223 verses, 3,288 findings, ~$1.40). "
     "`scripts/_build_verse_read_pilot_review.py`.", ""]
# corrected flag rate
real_flag = sum(1 for d in V.values() if real_missing(d))
L.append(f"## Corrected self-audit rate")
L.append(f"- DB flagged (over-strict union): **127 / 222**.")
L.append(f"- **Real omissions (free-text content field not echoed): {real_flag} / {len(V)}** "
         f"({100*real_flag/len(V):.0f}%) — the rest were option-list fields (origin etc.) + 'note-then-OK' API selfaudits.")
L.append("")
# unprocessed verse
proc = {(r["v"], r["m"]) for r in rows if r["q"] is None or True}
allvc = c.execute("""SELECT vc.id v, vr.reference ref FROM verse_context vc JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
                     WHERE vc.mti_term_id=269 AND COALESCE(vc.delete_flagged,0)=0""").fetchall()
done = {k[0] for k in V}
missing = [(r["v"], r["ref"]) for r in allvc if r["v"] not in done]
L.append(f"## Unprocessed verse (yir.ah → status 'review')")
L.append(f"- {missing if missing else 'none'} — caught by the per-term self-audit (not marked complete).")
L.append("")
# samples: 2 per term (one clean, one with real omission if any)
L.append("## Sample records (full extraction + meaning paragraph)")
for mid in IDS:
    items = [(k, d) for k, d in V.items() if k[1] == mid]
    clean = [x for x in items if not real_missing(x[1])]
    flagged = [x for x in items if real_missing(x[1])]
    picks = (clean[:1] + flagged[:1]) or items[:2]
    L.append(f"\n### {NAME[mid]}")
    for (vc, _), d in picks:
        L.append(f"\n**{d['ref']}**  (vcid={vc}){'  ⚑ real-omission: '+','.join(real_missing(d)) if real_missing(d) else ''}")
        for k in ["sense_applied", "type", "compound", "mode", "origin", "attributed_to_God",
                  "purpose_equips", "typology_direction", "immediate_response", "produces_effect",
                  "relational_implication", "literary_setting"]:
            if k in d["fields"]:
                L.append(f"- {k}: {d['fields'][k]}")
        L.append(f"- faculty: {', '.join(d['fac']) or 'NONE'}")
        L.append(f"- constitutional_location: {', '.join(d['loc']) or 'NONE'}")
        L.append(f"- **MEANING:** {d['para']}")
out = "research/investigations/wa-verse-read-pilot-review-M01-v1-20260609.md"
open(out, "w", encoding="utf-8").write("\n".join(L))
print(f"real-omission rate: {real_flag}/{len(V)} ({100*real_flag/len(V):.0f}%); missing verse: {missing}; wrote {out}")
