"""Build per-tier interrogation packages for M10 Phase 9.

One markdown file per tier (T0..T7). Each file contains, in catalogue order:
  - the tier's prompts (T#.#.#) with the question text
  - all 22 characteristics' findings stacked verbatim under each prompt

No distribution stats, no primary-grouping suggestions, no synthesis brief —
just the raw data organised tier-by-tier and prompt-by-prompt for an open
exploratory AI session.

Output (8 files):
  Sessions/Session_Clusters/M10/wa-cluster-M10-phase9-tier-T{N}-by-char-v1-{date}.md
"""
from __future__ import annotations
import argparse, io, sqlite3, sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"

STATUS_LABEL = {"finding": "E", "silent": "S", "gap": "G"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", default="M10")
    ap.add_argument("--tier", default=None,
                    help="Optional single tier (e.g. T3) — default writes all 8")
    args = ap.parse_args()

    cluster = args.cluster.strip()
    conn = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row

    cluster_row = conn.execute(
        "SELECT description FROM cluster WHERE cluster_code=?", (cluster,)
    ).fetchone()
    if not cluster_row:
        raise SystemExit(f"cluster {cluster} not found")
    description = cluster_row["description"]

    chars = conn.execute(
        "SELECT id, char_seq, short_name FROM characteristic "
        "WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 ORDER BY char_seq",
        (cluster,)
    ).fetchall()
    char_seq_by_id = {c["id"]: c["char_seq"] for c in chars}
    char_name_by_seq = {c["char_seq"]: c["short_name"] for c in chars}
    n_chars = len(chars)

    rows = conn.execute(
        """
        SELECT q.question_code, q.tier, q.component_code, q.component_title,
               q.prompt_seq, q.question_text,
               cf.characteristic_id, cf.finding_status, cf.finding_text
        FROM cluster_finding cf
        JOIN wa_obs_question_catalogue q ON q.obs_id = cf.obs_id
        WHERE cf.cluster_code = ?
          AND cf.characteristic_id IS NOT NULL
          AND COALESCE(cf.delete_flagged, 0) = 0
        ORDER BY q.tier, q.component_code, q.prompt_seq, cf.characteristic_id
        """,
        (cluster,)
    ).fetchall()

    # Group rows by tier, then by question_code preserving catalogue order
    tier_prompts: dict[str, dict[str, dict]] = defaultdict(dict)
    for r in rows:
        tier = r["tier"]
        qc = r["question_code"]
        if qc not in tier_prompts[tier]:
            tier_prompts[tier][qc] = {
                "tier": tier,
                "component_code": r["component_code"],
                "component_title": r["component_title"],
                "prompt_seq": r["prompt_seq"],
                "question_text": r["question_text"],
                "findings": [],  # list of (char_seq, status, finding_text)
            }
        cseq = char_seq_by_id[r["characteristic_id"]]
        tier_prompts[tier][qc]["findings"].append(
            (cseq, r["finding_status"], r["finding_text"])
        )

    out_dir = REPO / "Sessions" / "Session_Clusters" / cluster
    out_dir.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now(timezone.utc).strftime("%Y%m%d")

    tiers_to_write = ([args.tier] if args.tier else
                      sorted(tier_prompts.keys()))

    for tier in tiers_to_write:
        if tier not in tier_prompts:
            print(f"WARN: tier {tier} not found in data")
            continue
        # Sort prompts by (component_code, prompt_seq)
        prompts_sorted = sorted(
            tier_prompts[tier].values(),
            key=lambda p: (p["component_code"], p["prompt_seq"]),
        )
        n_prompts = len(prompts_sorted)
        component_title = prompts_sorted[0]["component_title"] if prompts_sorted else ""

        L: list[str] = []
        L.append(f"# {cluster} Phase 9 — Tier {tier} findings — interrogation view")
        L.append("")
        L.append(f"**Cluster:** {cluster} — {description}")
        L.append(f"**Tier:** {tier}")
        L.append(f"**Prompts in tier:** {n_prompts}")
        L.append(f"**Characteristics:** {n_chars}")
        L.append(f"**Finding blocks below:** {n_prompts * n_chars}")
        L.append("")
        L.append("Each prompt in this tier is shown in catalogue order. Under each prompt, all "
                 f"{n_chars} characteristics' findings are stacked verbatim. No analytics, no "
                 "grouping, no synthesis suggestions — just the raw data organised tier-by-tier "
                 "for open exploration.")
        L.append("")
        L.append("Status codes: **E** = evidenced; **S** = silent; **G** = gap.")
        L.append("")
        L.append("---")
        L.append("")

        # Group by component for nicer headings
        current_component = None
        for p in prompts_sorted:
            comp = (p["component_code"], p["component_title"])
            if comp != current_component:
                current_component = comp
                L.append(f"## {comp[0]} — {comp[1]}")
                L.append("")

            qc = (f"{p['tier']}.{p['component_code'].replace(p['tier'] + '.', '')}.{p['prompt_seq']}"
                  if p['component_code'].startswith(p['tier'] + '.')
                  else f"{p['tier']}.?.{p['prompt_seq']}")
            # Reconstruct question_code from row directly
            # actually use the original question_code from data — let me use the prompts dict key
            # Find the question_code that maps to this prompt
            # Easier: pull qc back from the parent loop
            # Already have it in p, but we didn't save it — patch:
            # (will fix by saving qc on the dict when grouping)
            qc = next(qc for qc, info in tier_prompts[tier].items() if info is p)

            L.append(f"### {qc}")
            L.append("")
            L.append(f"**Question:** {p['question_text']}")
            L.append("")

            # Sort findings by char_seq for stable order
            for cseq, status, finding_text in sorted(p["findings"], key=lambda f: f[0]):
                name = char_name_by_seq.get(cseq, "?")
                status_marker = STATUS_LABEL.get(status, "?")
                L.append(f"**[CHAR-{cseq}] {name}** *({status_marker})*")
                L.append("")
                # Insert the finding body
                body = (finding_text or "").strip()
                # Indent paragraphs slightly? Keep it flat — easier to read.
                L.append(body)
                L.append("")

            L.append("---")
            L.append("")

        out_path = out_dir / f"wa-cluster-{cluster}-phase9-tier-{tier}-by-char-v1-{date_str}.md"
        out_path.write_text("\n".join(L), encoding="utf-8")
        size_kb = out_path.stat().st_size / 1024
        print(f"  {tier}: {n_prompts} prompts × {n_chars} chars = "
              f"{n_prompts * n_chars} finding blocks → {out_path.name} ({size_kb:.1f} KB)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
