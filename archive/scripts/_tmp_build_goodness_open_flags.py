"""Build the goodness (R067) open-flags report.

Pulls every active flag/finding-with-open-status the registry has — Session B
(SB_FINDING, DIM-67-NNN, OBS-067-NNN with status='pending'), Session D
(SP-067-NNN), data anomalies, and any other research flags. No filtering by
narrative judgement — the file aims to be a complete open-loop register for
the registry.
"""
from __future__ import annotations

import os
import sqlite3
import sys
from datetime import datetime, timezone

OUT = "research/investigations/word_deep_dive/goodness/goodness-3-open-flags.md"


def main() -> int:
    conn = sqlite3.connect(os.path.join("database", "bible_research.db"))
    conn.row_factory = sqlite3.Row

    parts: list[str] = []
    P = parts.append

    P("# Goodness — Open Flags (R067)\n")
    P(f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n")
    P("**Sources:**\n")
    P("- `wa_session_research_flags` — programme-level flags (SB_FINDING, SD_POINTER, others). `resolved=0 OR NULL` only.")
    P("- `wa_session_b_findings` — Session B findings carrying open status (DIM-67-* still `pending`, DATA_ANOMALY_* not yet resolved).")
    P("\nNarrative descriptions for these pointers are reproduced verbatim. Where a description references OBS-067-OBS-NNN observations or specific verses, those are dereferenced in [goodness-5-citations.md](goodness-5-citations.md).\n")

    # --- 1. Session-D pointers (SP-067-NNN) ---
    rows = conn.execute(
        """
        SELECT flag_label, priority, session_target, raised_date, session_raised, description
        FROM wa_session_research_flags
        WHERE registry_id = (SELECT id FROM word_registry WHERE no = 67)
        AND flag_code = 'SD_POINTER'
        AND (resolved = 0 OR resolved IS NULL)
        ORDER BY flag_label
        """,
    ).fetchall()
    P(f"## 1. Session-D pointers (`SD_POINTER`) — {len(rows)} open\n")
    P("Programme-level questions deferred to Session D synthesis. All `priority` levels included.\n")
    for r in rows:
        P(f"### {r['flag_label']}  ·  {r['priority']}  ·  {r['session_target']}")
        P(f"_Raised {r['raised_date']}.  Source: {r['session_raised']}_\n")
        P(r["description"] or "_(no description)_")
        P("")

    # --- 2. Session-B findings (SB_FINDING and other open codes in research_flags) ---
    rows = conn.execute(
        """
        SELECT flag_code, flag_label, priority, session_target, raised_date, session_raised, description, strongs_reference
        FROM wa_session_research_flags
        WHERE registry_id = (SELECT id FROM word_registry WHERE no = 67)
        AND flag_code != 'SD_POINTER'
        AND (resolved = 0 OR resolved IS NULL)
        ORDER BY flag_code, flag_label
        """,
    ).fetchall()
    P(f"\n## 2. Session-B and other research flags — {len(rows)} open\n")
    P(f"Includes `SB_FINDING`, `SB_DIMENSION`, `SD_CLUSTER`, etc. — every non-`SD_POINTER` open row in `wa_session_research_flags`.\n")
    if not rows:
        P("_None._\n")
    else:
        # group by code
        groups: dict[str, list] = {}
        for r in rows:
            groups.setdefault(r["flag_code"], []).append(r)
        for code, items in groups.items():
            P(f"### {code} — {len(items)}\n")
            for r in items:
                P(f"#### {r['flag_label']}  ·  {r['priority']}  ·  target: {r['session_target']}")
                meta = f"_Raised {r['raised_date']}._"
                if r["strongs_reference"]:
                    meta += f"  Strong's: {r['strongs_reference']}."
                if r["session_raised"]:
                    meta += f"  Source: {r['session_raised']}."
                P(meta + "\n")
                P(r["description"] or "_(no description)_")
                P("")

    # --- 3. Open Session-B findings table (status='pending') ---
    rows = conn.execute(
        """
        SELECT finding_id, finding_type, status, raised_date, session_b_instruction,
               thin_evidence, finding
        FROM wa_session_b_findings
        WHERE registry_id = 67 AND delete_flag = 0
        AND status IN ('pending','open','to-be-resolved','provisional')
        ORDER BY finding_type, finding_id
        """,
    ).fetchall()
    P(f"\n## 3. Open `wa_session_b_findings` rows (status pending) — {len(rows)}\n")
    if not rows:
        P("_None._\n")
    else:
        for r in rows:
            P(f"### {r['finding_id']}  ·  {r['finding_type']}  ·  status `{r['status']}`")
            meta = f"_Raised {r['raised_date']}.  Instr: {r['session_b_instruction']}._"
            if r["thin_evidence"]:
                meta += "  **thin_evidence=1**"
            P(meta + "\n")
            P(r["finding"] or "_(empty)_")
            P("")

    # --- 4. Data anomalies for R067 ---
    rows = conn.execute(
        """
        SELECT finding_id, finding_type, status, raised_date, finding, resolution_note
        FROM wa_session_b_findings
        WHERE registry_id = 67 AND delete_flag = 0
        AND finding_type LIKE 'DATA_ANOMALY%'
        ORDER BY finding_type, finding_id
        """,
    ).fetchall()
    P(f"\n## 4. Data anomalies (DATA_ANOMALY_*) — {len(rows)}\n")
    if not rows:
        P("_None._\n")
    else:
        for r in rows:
            P(f"### {r['finding_id']}  ·  {r['finding_type']}  ·  status `{r['status']}`")
            P(f"_Raised {r['raised_date']}._\n")
            P(r["finding"] or "_(empty)_")
            if r["resolution_note"]:
                P(f"\n**Resolution note:** {r['resolution_note']}")
            P("")

    # --- 5. Resolved-flag count for context ---
    n = conn.execute(
        """
        SELECT COUNT(*) FROM wa_session_research_flags
        WHERE registry_id = (SELECT id FROM word_registry WHERE no = 67)
        AND resolved = 1
        """,
    ).fetchone()[0]
    P(f"\n## 5. Context counts\n")
    P(f"- **Resolved `wa_session_research_flags` rows for R067:** {n}")
    n = conn.execute(
        """
        SELECT COUNT(*) FROM wa_session_b_findings
        WHERE registry_id = 67 AND delete_flag = 0
        """,
    ).fetchone()[0]
    P(f"- **Total active `wa_session_b_findings` for R067:** {n} (open + closed; full text in [goodness-5-citations.md](goodness-5-citations.md))")
    P("")

    out_path = OUT
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print(f"Wrote {out_path} ({sum(len(p) for p in parts):,} chars / {len(parts)} lines)")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
