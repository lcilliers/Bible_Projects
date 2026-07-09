"""Load M10 thematic observations into cluster_observation.

Source file: Sessions/Session_Clusters/M10/wa-m10-thematic-observations-v1-20260524.md
67 KB, 8 H2 sections of analytical content authored on 2026-05-24 — "windows/
themes for Session C architecture" per the file header. Compiled from T1/T2/T3
tier interrogation across the 22 M10 characteristics.

The 8 sections are:
  §1 The Heart is the Cluster's Constitutional Centre
  §2 The Conscience is the Cluster's Primary Diagnostic Instrument
  §3 The Will is the Cluster's Primary Faculty — But Its Role Changes
  §4 Constitutional Deposit: The Progressive Entrenchment of Sin
  §5 Three Structural Tiers Emerge from the Data
  §6 Two Characteristics Are Resolution-Facing (Not Sin-Describing)
  §7 The Relational Damage Pattern
  §8 Spirit-Level Pattern (59 KB — the substantive bulk)

Loads each as a cluster_observation row with:
  cluster_code      = 'M10'
  observation_type  = 'CLUSTER_SYNTHESIS'  (same type as the OBS-NN rows)
  target_phase      = 'session_c'   (per the file's stated purpose)
  source_phase      = 'phase_9_thematic_exploration'
  source_file       = the .md path
  title             = 'M10 thematic observation §N — {section title}'
  description       = the section body
  status            = 'open'

Why CLUSTER_SYNTHESIS: these are cross-characteristic synthesis observations
at cluster scope, indistinguishable in kind from the 15 OBS-NN rows already
loaded.

Idempotent: aborts if rows from this source_file already exist.
"""
from __future__ import annotations
import argparse, io, re, sqlite3, sys
from datetime import datetime, timezone
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

SRC = REPO / "Sessions" / "Session_Clusters" / "M10" / "wa-m10-thematic-observations-v1-20260524.md"
SOURCE_REL = "Sessions/Session_Clusters/M10/wa-m10-thematic-observations-v1-20260524.md"
CLUSTER = "M10"

H2_RE = re.compile(r"^## (\d+)\.\s+(.+?)$", re.MULTILINE)


def parse_sections(text: str) -> list[dict]:
    """Walk H2 sections (## N. Title) and capture body up to next H2 or EOF."""
    matches = list(H2_RE.finditer(text))
    out = []
    for i, m in enumerate(matches):
        num = int(m.group(1))
        title = m.group(2).strip()
        body_start = m.end()
        body_end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[body_start:body_end].strip()
        out.append({"num": num, "title": title, "body": body})
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    dry = not args.live

    print(f"=== M10 thematic observations load — mode={'LIVE' if not dry else 'DRY-RUN'} ===")

    if not SRC.exists():
        raise SystemExit(f"Source not found: {SRC}")
    text = SRC.read_text(encoding="utf-8")
    sections = parse_sections(text)
    print(f"Parsed {len(sections)} sections from {SRC.name}")
    for s in sections:
        print(f"  §{s['num']} ({len(s['body']):,}c): {s['title'][:80]}")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    existing = conn.execute(
        "SELECT COUNT(*) FROM cluster_observation "
        "WHERE source_file=? AND COALESCE(delete_flagged,0)=0",
        (SOURCE_REL,),
    ).fetchone()[0]
    if existing:
        print(f"\nAbort: {existing} cluster_observation rows already exist from this source_file.")
        conn.close()
        return 1
    print("\nPre-check: 0 existing rows from this source_file — clean to load.")

    if dry:
        print("\n[DRY-RUN — no writes]")
        conn.close()
        return 0

    cur = conn.cursor()
    cur.execute("BEGIN")
    try:
        n = 0
        for s in sections:
            title = f"M10 thematic observation §{s['num']} — {s['title']}"
            cur.execute(
                "INSERT INTO cluster_observation "
                "(cluster_code, characteristic_id, cluster_subgroup_id, source_phase, "
                " observation_type, target_phase, title, description, status, "
                " raised_date, source_file, delete_flagged, created_at, last_updated_date) "
                "VALUES (?, NULL, NULL, ?, ?, ?, ?, ?, 'open', ?, ?, 0, ?, ?)",
                (CLUSTER, "phase_9_thematic_exploration", "CLUSTER_SYNTHESIS", "session_c",
                 title, s["body"], NOW, SOURCE_REL, NOW, NOW),
            )
            n += 1
        conn.commit()
        print(f"\nCOMMITTED — {n} cluster_observation rows inserted")
    except Exception:
        conn.rollback()
        print("ROLLED BACK")
        raise
    finally:
        # Post-state
        total = conn.execute(
            "SELECT COUNT(*) FROM cluster_observation "
            "WHERE cluster_code=? AND observation_type='CLUSTER_SYNTHESIS' "
            "AND COALESCE(delete_flagged,0)=0",
            (CLUSTER,),
        ).fetchone()[0]
        print(f"M10 CLUSTER_SYNTHESIS rows post-load: {total}")
        conn.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
