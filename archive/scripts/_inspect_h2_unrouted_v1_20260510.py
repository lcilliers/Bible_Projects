"""_inspect_h2_unrouted_v1_20260510.py — read-only inspection.

Surface the H2-class connectivity break for cluster M26: vc rows with
is_relevant=1 but group_id NULL (i.e. a verse known to be relevant to
its term but never placed into a verse_context_group / 'meaning'
group). Restricts to the sub-groups the researcher named: M26-A1 (God
Righteousness) and M26-E (Condemnation: Judicial Sentence Against).

For each (sub-group, term) bucket, show:
  - the available vcgs under that term (so the user can pick a target)
  - the full text of each unrouted verse (so the meaning fit can be
    judged from the verse itself)

NO API calls. NO DB writes. Output is a markdown file.
"""
from __future__ import annotations

import argparse
import os
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
TARGET_SUBGROUPS = ("M26-A1", "M26-E")
OUT_PATH = os.path.join(
    "outputs", "markdown",
    "m26-h2-unrouted-A1-E-v1-20260510.md",
)


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=OUT_PATH)
    args = ap.parse_args()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # H2 unrouted verses inside the two target sub-groups
    sg_filter = ",".join("?" * len(TARGET_SUBGROUPS))
    rows = list(conn.execute(f"""
        SELECT vc.id AS vc_id, vc.verse_record_id AS vr_id,
               vc.mti_term_id, vc.cluster_subgroup_id,
               vr.reference, vr.verse_text, vr.testament,
               mt.strongs_number, mt.transliteration, mt.gloss,
               cs.subgroup_code
          FROM verse_context vc
          JOIN mti_terms mt ON mt.id=vc.mti_term_id
          JOIN cluster_subgroup cs ON cs.id=vc.cluster_subgroup_id
          JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
         WHERE mt.cluster_code='M26'
           AND vc.is_relevant=1
           AND vc.group_id IS NULL
           AND COALESCE(vc.delete_flagged,0)=0
           AND (vc.set_aside_reason IS NULL OR vc.set_aside_reason='')
           AND cs.subgroup_code IN ({sg_filter})
         ORDER BY cs.sort_order, mt.strongs_number, vr.reference
    """, TARGET_SUBGROUPS).fetchall())

    print(f"H2 verses in {TARGET_SUBGROUPS}: {len(rows)}")

    # Available vcgs per term that has unrouted verses in scope
    term_ids = {r["mti_term_id"] for r in rows}
    vcgs_by_term: dict[int, list[dict]] = defaultdict(list)
    if term_ids:
        ph = ",".join("?" * len(term_ids))
        for r in conn.execute(f"""
            SELECT vcg.id AS group_id, vt.mti_term_id, vcg.group_code,
                   vcg.context_description, vcg.notes
              FROM verse_context_group vcg
              JOIN vcg_term vt ON vt.vcg_id=vcg.id
             WHERE vt.mti_term_id IN ({ph})
               AND COALESCE(vcg.delete_flagged,0)=0
               AND COALESCE(vt.delete_flagged,0)=0
             ORDER BY vcg.group_code
        """, list(term_ids)):
            vcgs_by_term[r["mti_term_id"]].append(dict(r))

    # Bucket: sub-group → mti_term_id → list of unrouted vc rows
    bucket: dict = defaultdict(lambda: defaultdict(list))
    for r in rows:
        bucket[r["subgroup_code"]][r["mti_term_id"]].append(dict(r))

    conn.close()

    # ── Render
    lines = []
    lines.append(
        f"# M26 — H2 unrouted relevant verses in {' + '.join(TARGET_SUBGROUPS)}"
    )
    lines.append("")
    lines.append(f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}")
    lines.append("")
    lines.append(
        "These verses sit in the named sub-groups with `is_relevant=1` "
        "but `group_id IS NULL` — relevant but never placed into a "
        "`verse_context_group`. To close the H2 gap, each verse must be "
        "assigned to a vcg that fits its meaning (an existing one if a "
        "fit exists, otherwise a new one)."
    )
    lines.append("")
    lines.append(f"Total in scope: **{len(rows)}** verses")
    lines.append("")

    for sg_code in TARGET_SUBGROUPS:
        sg_bucket = bucket.get(sg_code, {})
        n_in_sg = sum(len(v) for v in sg_bucket.values())
        lines.append(f"## {sg_code} ({n_in_sg} verses, "
                     f"{len(sg_bucket)} terms)")
        lines.append("")
        if not sg_bucket:
            lines.append("_(no H2 verses in this sub-group)_")
            lines.append("")
            continue

        for tid, verses in sg_bucket.items():
            sample = verses[0]
            term_label = (
                f"{sample['strongs_number']} *{sample['transliteration']}* "
                f"— {sample['gloss']}"
            )
            lines.append(f"### {term_label}  ·  {len(verses)} verses")
            lines.append("")

            # Available vcgs for this term
            vcgs = vcgs_by_term.get(tid, [])
            if vcgs:
                lines.append(f"**Existing vcgs for this term ({len(vcgs)}):**")
                lines.append("")
                lines.append("| Code | Description |")
                lines.append("|---|---|")
                for v in vcgs:
                    desc = (v["context_description"] or "").replace("|", "\\|")
                    lines.append(
                        f"| `{v['group_code']}` | {desc} |"
                    )
                lines.append("")
            else:
                lines.append(
                    "**No existing vcgs for this term — a new one (or "
                    "more) needs to be authored before these verses can "
                    "be routed (H7 alert).**"
                )
                lines.append("")

            # Unrouted verses
            lines.append("**Unrouted verses to assign:**")
            lines.append("")
            lines.append("| vc_id | Reference | Verse text |")
            lines.append("|---:|---|---|")
            for v in verses:
                vt = (v["verse_text"] or "").replace("|", "\\|")
                # Trim leading reference repeat in verse_text if present
                lines.append(
                    f"| {v['vc_id']} | {v['reference']} | {vt} |"
                )
            lines.append("")

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote: {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
