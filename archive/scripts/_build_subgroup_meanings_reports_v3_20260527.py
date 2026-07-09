"""Build per-sub-group meanings reports for Phase B.3 (v3_0).

For each sub-group in a cluster's mapping JSON, write one report file
containing every verse_context row in that sub-group with Pass A meaning
and keywords. This is the analytical input for B.3 VCG design.

Per `wa-sessionb-cluster-instruction-v3_0-20260527.md` §6.3.1:
the per-sub-group meanings report is the only B.3 input.

Usage:
    python scripts/_build_subgroup_meanings_reports_v3_20260527.py \
        --cluster M11 \
        --mapping Sessions/Session_Clusters/M11/WA-M11-subgroup-mapping-v1-20260527.json \
        --design Sessions/Session_Clusters/M11/WA-M11-subgroup-design-v1-20260527.md \
        --out-dir Sessions/Session_Clusters/M11/

Outputs one file per sub-group:
    WA-{code}-{subgroup_code}-meanings-v1-{date}.md
"""
from __future__ import annotations
import argparse, json, re, sqlite3, sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
TODAY = datetime.now(timezone.utc).strftime("%Y%m%d")


def parse_subgroup_labels(design_path: Path) -> dict[str, str]:
    """Extract sub-group label from the design markdown (§2.x sections)."""
    labels: dict[str, str] = {}
    if not design_path.exists():
        return labels
    text = design_path.read_text(encoding="utf-8")
    # Match patterns like: "### §2.1 M11-A — Atonement"
    for m in re.finditer(r"###\s+§\d+\.\d+\s+([A-Z][\w\-]+)\s+[—-]\s+(.+?)$", text, re.MULTILINE):
        sg_code, label = m.group(1), m.group(2).strip()
        labels[sg_code] = label
    return labels


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--mapping", required=True)
    ap.add_argument("--design", required=False, default=None,
                    help="path to design markdown (for sub-group labels)")
    ap.add_argument("--out-dir", required=True)
    args = ap.parse_args()

    mapping = json.loads(Path(args.mapping).read_text(encoding="utf-8"))
    mapping = {int(k): v for k, v in mapping.items()}

    labels = parse_subgroup_labels(Path(args.design)) if args.design else {}

    by_sg: dict[str, list[int]] = defaultdict(list)
    for vc_id, sg in mapping.items():
        by_sg[sg].append(vc_id)

    conn = sqlite3.connect(DB, timeout=60.0)
    conn.row_factory = sqlite3.Row

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"=== Building {len(by_sg)} per-sub-group meanings reports for {args.cluster} ===")

    for sg_code in sorted(by_sg):
        vc_ids = by_sg[sg_code]
        rows = conn.execute(
            f"""
            SELECT vc.id AS vc_id, vc.mti_term_id, vc.analysis_note, vc.keywords,
                   vr.reference, m.strongs_number, m.transliteration, m.gloss, m.language
            FROM verse_context vc
            JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
            JOIN mti_terms m ON m.id = vc.mti_term_id
            WHERE vc.id IN ({','.join('?' * len(vc_ids))})
            ORDER BY m.language, m.strongs_number, vr.reference
            """,
            vc_ids,
        ).fetchall()

        label = labels.get(sg_code, "")
        out_path = out_dir / f"WA-{args.cluster}-{sg_code}-meanings-v1-{TODAY}.md"

        # Group by term for readability
        by_term: dict[tuple, list] = defaultdict(list)
        for r in rows:
            term_key = (r["strongs_number"], r["transliteration"], r["gloss"], r["language"])
            by_term[term_key].append(r)

        with out_path.open("w", encoding="utf-8") as f:
            f.write(f"# {args.cluster} {sg_code} — meanings report (Phase B.3 input)\n\n")
            f.write(f"**Sub-group:** {sg_code}  \n")
            if label:
                f.write(f"**Label:** {label}  \n")
            f.write(f"**Verses:** {len(rows)}  \n")
            f.write(f"**Built:** {TODAY}  \n")
            f.write(f"**Source mapping:** `{Path(args.mapping).name}`\n\n")
            f.write("---\n\n")
            f.write("## Per-term verse-meaning corpus\n\n")
            f.write("Each verse line: `vc_id | reference | Pass A meaning | [keywords]`\n\n")

            for term_key in sorted(by_term, key=lambda k: (k[3], k[0])):  # lang, strongs
                strongs, translit, gloss, lang = term_key
                term_rows = by_term[term_key]
                f.write(f"### {strongs} `{translit}` ({lang[:2]}) — {gloss}  ({len(term_rows)}V)\n\n")
                for r in term_rows:
                    note = (r["analysis_note"] or "").replace("\n", " ").strip()
                    kw = r["keywords"] or ""
                    try:
                        kw_list = json.loads(kw) if kw else []
                        kw_disp = " · ".join(kw_list) if isinstance(kw_list, list) else kw
                    except Exception:
                        kw_disp = kw
                    f.write(f"- **vc={r['vc_id']}** `{r['reference']}` — {note}  \n")
                    if kw_disp:
                        f.write(f"  *keywords:* {kw_disp}\n")
                f.write("\n")
            f.write("---\n\n")
            f.write(f"*Built by `_build_subgroup_meanings_reports_v3_20260527.py` — {TODAY}*\n")

        print(f"  wrote {out_path.name} ({len(rows)} verses)")

    conn.close()
    print("=== Done ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
