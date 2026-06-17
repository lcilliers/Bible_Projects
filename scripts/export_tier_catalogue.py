"""export_tier_catalogue.py (2026-06-17) — read-only export of the Tier Catalogue
(`wa_obs_question_catalogue`) to JSON, grouped tier -> component -> question.

  python scripts/export_tier_catalogue.py                 # all rows (active flagged)
  python scripts/export_tier_catalogue.py --active-only    # deleted=0 only
"""
import argparse, json, os, sqlite3
DB = os.path.join("database", "bible_research.db")

# tier-level titles (stable; the DB stores component titles, not tier titles) — per the 2026-06-11 restructure
TIER_TITLES = {
    "T0": "Divine Image and Created Design", "T1": "Definition",
    "T2": "Constitutional Location and Boundaries", "T3": "The Inner Faculties",
    "T4": "Relational Interfaces", "T5": "Formative and Developmental Dimension",
    "T6": "Structural Relationships with Other Characteristics", "T7": "Evidential and Methodological Foundation",
}


def to_markdown(tier_list, total):
    L = []
    L.append("# WA Tier Catalogue — CURRENT STATE (as held in the database) — v1 — 2026-06-17")
    L.append("")
    L.append("> **THIS IS THE AUTHORITATIVE, CURRENT REPRESENTATION OF THE TIER SYSTEM.** Generated directly from "
             "`wa_obs_question_catalogue` (`deleted=0 AND tier IS NOT NULL`). It cannot drift from the DB — "
             "regenerate with `python scripts/export_tier_catalogue.py --md`. Other docs in this folder are "
             "*design/refit history*, not the current state (see Provenance).")
    L.append("")
    L.append(f"**Scheme:** T0–T7 · **Active tiered questions:** {total} · **Source:** `wa_obs_question_catalogue` · "
             "**As of:** 2026-06-17")
    L.append("")
    L.append("## Scheme overview (T0–T7)")
    L.append("")
    L.append("| Tier | Title | Active questions |")
    L.append("|---|---|---|")
    for t in tier_list:
        L.append(f"| {t['tier']} | {TIER_TITLES.get(t['tier'],'')} | {t['question_count']} |")
    L.append("")
    L.append("## Crosswalk from the superseded T1–T8 framework")
    L.append("")
    L.append("The old `WA-tier-framework-definitions-v1_2-2026-04-29.md` (T1–T8, **archived/superseded**) maps to the "
             "current T0–T7 as: T1→T1 · T2→T2 · T3→T3 · **T5→T4 · T6→T5 · T7→T6 · T8→T7**; the current scheme **adds "
             "T0 (Divine Image)**, which v1.2 had dropped. Analyses written in T1–T8 (e.g. M01-c1) must be remapped.")
    L.append("")
    L.append("## Pending refit (not yet in the DB)")
    L.append("")
    L.append("A two-layer **VE / SYNTH** refit (verse-extraction fields VE-01..VE-17 + synthesis roll-ups) is proposed "
             "in `wa-tier-catalogue-restructured-v2-20260611.md` — **approved-in-principle, DB unchanged.** Until applied, "
             "the catalogue below (the T0–T7 question form) remains current.")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## The catalogue")
    for t in tier_list:
        L.append("")
        L.append(f"### {t['tier']} — {TIER_TITLES.get(t['tier'],'')}")
        for c in t["components"]:
            L.append("")
            L.append(f"**{c['component_code']} · {c['component_title']}**")
            L.append("")
            for q in sorted(c["questions"], key=lambda x: (x["prompt_seq"] or 0, x["question_code"] or "")):
                L.append(f"- **{q['question_code']}** — {q['question_text']}")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## Provenance")
    L.append(f"- **Current state (this doc):** the {total} active T0–T7 questions, generated from the DB.")
    L.append("- **Pending design:** `wa-tier-catalogue-restructured-v2-20260611.md` (VE/SYNTH two-layer refit — not yet applied).")
    L.append("- **Superseded (archived):** `WA-tier-framework-definitions-v1_2-2026-04-29.md` (T1–T8 prose framework), "
             "`wa-tier-questions-extract-v1-20260604.md` (flat extract), and the prior debate/draft logs in `archive/`.")
    L.append("- **16 questions soft-deleted** from the documented 189 = the agreed DROP list (T1.8, T1.2.3, T2.8, T5.7, "
             "T6.6, T6.7); 189 − 16 = " + str(total) + " active.")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--active-only", action="store_true", help="restrict to deleted=0")
    ap.add_argument("--canonical", action="store_true",
                    help="the canonical tier catalogue only: deleted=0 AND tier set (T0-T7); excludes legacy untiered flag questions")
    ap.add_argument("--md", action="store_true", help="emit the current-state markdown doc (forces --canonical scope)")
    ap.add_argument("--out", default="outputs/tier-catalogue-extract-20260617.json")
    a = ap.parse_args()
    if a.md:
        a.canonical = True
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    if a.canonical:
        where = "WHERE COALESCE(deleted,0)=0 AND tier IS NOT NULL"
    elif a.active_only:
        where = "WHERE COALESCE(deleted,0)=0"
    else:
        where = ""
    rows = cur.execute(f"""
        SELECT obs_id, question_code, tier, component_code, component_title, prompt_seq,
               section, source_word, source_registry_no, question_text, pattern_type,
               scope, status, deleted, catalogue_version, date_added, review_note
        FROM wa_obs_question_catalogue {where}
        ORDER BY (tier IS NULL), tier, (component_code IS NULL), component_code, prompt_seq, question_code
    """).fetchall()

    # distributions for meta
    def dist(col):
        return {str(r[0]): r[1] for r in cur.execute(
            f"SELECT {col}, COUNT(*) FROM wa_obs_question_catalogue GROUP BY {col} ORDER BY COUNT(*) DESC")}

    # group tier -> component -> questions
    tiers = {}
    for r in rows:
        t = r["tier"] or "UNTIERED"
        comp_key = r["component_code"] or "(none)"
        tier = tiers.setdefault(t, {"tier": t, "components": {}})
        comp = tier["components"].setdefault(comp_key, {
            "component_code": r["component_code"], "component_title": r["component_title"], "questions": []})
        comp["questions"].append({
            "obs_id": r["obs_id"], "question_code": r["question_code"], "prompt_seq": r["prompt_seq"],
            "question_text": r["question_text"], "pattern_type": r["pattern_type"], "scope": r["scope"],
            "status": r["status"], "active": (r["deleted"] or 0) == 0, "catalogue_version": r["catalogue_version"],
            "section": r["section"], "source_word": r["source_word"], "source_registry_no": r["source_registry_no"],
            "review_note": r["review_note"],
        })
    # flatten component dicts to lists, ordered
    tier_list = []
    for t in sorted(tiers, key=lambda x: (x == "UNTIERED", x)):
        comps = list(tiers[t]["components"].values())
        tier_list.append({"tier": t, "question_count": sum(len(c["questions"]) for c in comps), "components": comps})

    payload = {
        "meta": {
            "what_this_is": "The Tier Catalogue (observation question catalogue) from `wa_obs_question_catalogue`, "
                            "grouped tier -> component -> question. Companion to WA-tier-framework-definitions.",
            "source_table": "wa_obs_question_catalogue",
            "extracted": "2026-06-17",
            "filter": "deleted=0 (active only)" if a.active_only else "ALL rows (per-row `active` flag = deleted=0)",
            "row_count": len(rows),
            "distributions": {"by_tier": dist("tier"), "by_status": dist("status"),
                              "by_catalogue_version": dist("catalogue_version"), "deleted": dist("deleted")},
            "field_glossary": {
                "tier": "T0-T7 tier (UNTIERED = F-xxx flag-type questions, no tier)",
                "component_code/title": "the tier sub-component the question sits under",
                "question_code": "stable code (e.g. F-001)", "prompt_seq": "order within the component",
                "status": "active | redundant_v1 | dropped | superseded", "active": "deleted=0",
            },
        },
        "tiers": tier_list,
    }
    if a.md:
        out = a.out if a.out.endswith(".md") else "Workflow/Tiers/WA-tier-catalogue-current-state-v1-20260617.md"
        os.makedirs(os.path.dirname(out), exist_ok=True)
        md = to_markdown(tier_list, len(rows))
        open(out, "w", encoding="utf-8").write(md)
        print(f"WROTE {out} · {len(rows)} questions · {len(tier_list)} tiers · {len(md):,} chars")
        return
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    js = json.dumps(payload, ensure_ascii=False, indent=2)
    open(a.out, "w", encoding="utf-8").write(js)
    print(f"WROTE {a.out} · {len(rows)} questions · {len(tier_list)} tier groups · {len(js):,} chars")
    print("tiers:", ", ".join(f"{t['tier']}({t['question_count']})" for t in tier_list))


if __name__ == "__main__":
    main()
