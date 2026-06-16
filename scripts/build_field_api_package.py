"""build_field_api_package.py (2026-06-16) — Alt 3: prepare a focused, single-instruction API read for ANY
enhanceable field (one field per run). Generalises the cause pipeline.

  python scripts/build_field_api_package.py --cluster M01 --field location
  fields: location · divine-involvement · valence · object-type   (extend FIELD_SPECS for more)

Run the package with scripts/_run_cause_api.py (generic runner); apply with scripts/_apply_field_from_api.py.
"""
import argparse, json, os, sqlite3

DB = os.path.join("database", "bible_research.db")

FIELD_SPECS = {
    # field: {where (ve_lexical filter; None = ALL units), prompt}
    "location": {
        "where": "x.ve_label='location' AND x.value='UNRESOLVED'",
        "prompt": ("TASK (only this): each verse contains a 'spirit/breath' word (ruach/pneuma). Decide, for the "
                   "named `term`, whether that word is the human inner-being SEAT (the spirit as a constitutional "
                   "seat). If yes -> \"spirit\". If it is the divine Spirit, a disposition, wind, or breath (NOT "
                   "the seat) -> \"NONE\". OUTPUT JSON only: [{\"vcid\":int,\"value\":\"spirit\"|\"NONE\"}]."),
    },
    "divine-involvement": {
        "where": "x.ve_label='divine-involvement'",
        "prompt": ("TASK (only this): state GOD's role toward the inner-being `term` in this verse — EXACTLY one "
                   "of: agent | possessor | giver | object | addressee | none. OUTPUT JSON only: "
                   "[{\"vcid\":int,\"value\":\"<role>\"}]."),
    },
    "object-type": {
        "where": "x.ve_label='object-type' AND x.value='thing/abstract'",
        "prompt": ("TASK (only this): the inner-being `term` is directed at an object. Classify that object in "
                   "THIS verse — EXACTLY one of: threat | person | God | spiritual-being | situation | abstract "
                   "| thing. OUTPUT JSON only: [{\"vcid\":int,\"value\":\"<type>\"}]."),
    },
    "valence": {
        "where": None,   # all cluster units
        "prompt": ("TASK (only this): does the inner-being state named by `term` carry a MORAL valence in THIS "
                   "verse — EXACTLY one of: righteous | sinful | commanded | forbidden | neutral | NONE. Use NONE "
                   "if the verse gives no moral framing. OUTPUT JSON only: [{\"vcid\":int,\"value\":\"<valence>\"}]."),
    },
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--field", required=True, choices=list(FIELD_SPECS))
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()
    spec = FIELD_SPECS[a.field]
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    if spec["where"]:
        rows = cur.execute(f"""SELECT vc.id vcid, vr.reference ref, vr.verse_text vt, m.transliteration tr, m.gloss gloss
            FROM ve_lexical x JOIN verse_context vc ON vc.id=x.verse_context_id
            JOIN wa_verse_records vr ON vr.id=vc.verse_record_id AND COALESCE(vr.delete_flagged,0)=0
            JOIN mti_terms m ON m.id=vc.mti_term_id
            WHERE m.cluster_code=? AND {spec['where']} AND x.source_provenance='v2_engine_iter1' AND COALESCE(x.delete_flagged,0)=0
            ORDER BY vr.book_id, vr.chapter, vr.verse_num""", (a.cluster,)).fetchall()
    else:
        rows = cur.execute("""SELECT vc.id vcid, vr.reference ref, vr.verse_text vt, m.transliteration tr, m.gloss gloss
            FROM verse_context vc JOIN wa_verse_records vr ON vr.id=vc.verse_record_id AND COALESCE(vr.delete_flagged,0)=0
            JOIN mti_terms m ON m.id=vc.mti_term_id
            WHERE m.cluster_code=? AND COALESCE(vc.delete_flagged,0)=0
            ORDER BY vr.book_id, vr.chapter, vr.verse_num""", (a.cluster,)).fetchall()
    if a.limit:
        rows = rows[:a.limit]
    items = [{"vcid": r["vcid"], "reference": r["ref"], "verse_text": r["vt"], "term": r["tr"], "gloss": r["gloss"]} for r in rows]
    payload = {"meta": {"task": f"{a.field}-read", "field": a.field, "cluster": a.cluster, "items": len(items),
                        "instruction": spec["prompt"],
                        "apply_with": f"scripts/_apply_field_from_api.py --field {a.field} --input <out.json>"},
               "items": items}
    out = f"research/VE-lexical/extracts/field-api-input-{a.cluster}-{a.field}-20260616.json"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    js = json.dumps(payload, ensure_ascii=False, indent=2)
    open(out, "w", encoding="utf-8").write(js)
    print(f"WROTE {out}  ·  {len(items):,} items · {len(js):,} chars ≈ {len(js)//4:,} tokens")


if __name__ == "__main__":
    main()
