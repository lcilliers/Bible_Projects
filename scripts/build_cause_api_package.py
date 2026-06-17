"""build_cause_api_package.py (2026-06-16) — Alt 2: prepare a focused, single-purpose API run that does
ONE thing — read the verse and determine the CAUSE of the inner-being state.

Emits an input package (the cause-flagged units = ve_lexical cause='pending-read') with the verse text +
term + the Alt-1 clause hint, plus the exact prompt + output schema. Read-only; writes no DB rows.
Apply the API's output back with `_apply_cause_from_api.py`.

  python scripts/build_cause_api_package.py --cluster M01
  python scripts/build_cause_api_package.py --cluster M01 --limit 50    # smaller pilot
"""
import argparse, json, os, sqlite3

DB = os.path.join("database", "bible_research.db")
PROMPT = (
    "TASK (do ONLY this): determine the CAUSE of an inner-being state, per item.\n"
    "For each item: read `verse_text`; in a SHORT phrase (<=8 words) state what AROUSES the inner state named "
    "by `term` in THIS verse. `cause_clause` is a mechanical hint (the clause after a 'because/for' marker) — "
    "it may or may not be the real cause; judge from the verse. If the verse does NOT actually state what causes "
    "the state, return \"NONE\". Do not infer beyond the text; do not add commentary.\n"
    "OUTPUT: a JSON array only — [{\"vcid\": <int>, \"cause\": \"<phrase or NONE>\"}] — one object per input item."
)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()
    if a.cluster == "T2":                                  # 01c §A3/B0: T2 is never read (reference only)
        raise SystemExit("REFUSED: T2 is a reference cluster — never sent to an API read (01c §A3).")
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    rows = cur.execute("""
        SELECT vc.id vcid, vr.reference ref, vr.verse_text vt, m.transliteration tr, m.gloss gloss,
               (SELECT value FROM ve_lexical x2 WHERE x2.verse_context_id=vc.id AND x2.ve_label='cause_clause'
                AND COALESCE(x2.delete_flagged,0)=0 LIMIT 1) clause
        FROM ve_lexical x JOIN verse_context vc ON vc.id=x.verse_context_id
        JOIN wa_verse_records vr ON vr.id=vc.verse_record_id AND COALESCE(vr.delete_flagged,0)=0
        JOIN mti_terms m ON m.id=vc.mti_term_id
        WHERE m.cluster_code=? AND x.ve_label='cause' AND x.value='pending-read'
          AND x.source_provenance='v2_engine_iter1' AND COALESCE(x.delete_flagged,0)=0
        ORDER BY vr.book_id, vr.chapter, vr.verse_num""", (a.cluster,)).fetchall()
    if a.limit:
        rows = rows[:a.limit]
    items = [{"vcid": r["vcid"], "reference": r["ref"], "verse_text": r["vt"],
              "term": r["tr"], "gloss": r["gloss"], "cause_clause": r["clause"]} for r in rows]
    payload = {"meta": {"task": "cause-resolution", "cluster": a.cluster, "items": len(items),
                        "instruction": PROMPT,
                        "output_schema": "[{vcid:int, cause:string(<=8 words) | 'NONE'}]",
                        "apply_with": "scripts/_apply_cause_from_api.py --input <api-output.json>"},
               "items": items}
    out = f"research/VE-lexical/extracts/cause-api-input-{a.cluster}-20260616.json"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    js = json.dumps(payload, ensure_ascii=False, indent=2)
    open(out, "w", encoding="utf-8").write(js)
    print(f"WROTE {out}")
    print(f"  {len(items):,} cause-flagged items · {len(js):,} chars ≈ {len(js)//4:,} tokens")
    print("  PROMPT:\n   " + PROMPT.replace("\n", "\n   "))


if __name__ == "__main__":
    main()
