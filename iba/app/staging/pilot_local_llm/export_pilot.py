"""Read-only export for the local-LLM pilot: the 39 verses of the 2026-10-30 Analysis_phase_1 redo
(run ids RUN-20261030*), with the ESV text and the researcher's reference observations.
Usage: python -I export_pilot.py <db_path> <out_json>"""
import json, sqlite3, sys

db, out = sys.argv[1], sys.argv[2]
c = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
rows = c.execute("""
    select n.verse_reference, o.id, o.tag, o.basis, o.parts, o.obs_text
    from ib_observation o join ib_node n on n.observation_id = o.id
    where o.stage = 'Analysis_phase_1' and o.deleted = 0 and n.deleted = 0
      and o.run_id like 'RUN-20261030%'
    group by n.verse_reference, o.id order by n.verse_reference, o.id""").fetchall()
verses = {}
for ref, oid, tag, basis, parts, text in rows:
    v = verses.setdefault(ref, {"osisId": ref, "reference": None, "text": None, "reference_observations": []})
    p = json.loads(parts) if parts else {}
    v["reference_observations"].append({"id": oid, "kind": tag, "basis": basis,
                                        "item": p.get("item"), "mode": p.get("mode"), "obs_text": text})
for ref, v in verses.items():
    r = c.execute("select reference, text from verse where osisId = ?", (ref,)).fetchone()
    v["reference"], v["text"] = r
items = json.loads(c.execute("select value from cfg_setting where key like '%observation_items%'").fetchone()[0])
json.dump({"items": items, "verses": list(verses.values())}, open(out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(f"{len(verses)} verses, {len(rows)} reference observations -> {out}")
