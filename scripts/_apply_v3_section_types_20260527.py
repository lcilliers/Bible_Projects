"""Register v3_0 prose_section_type rows for cluster publication pipeline.

Per researcher direction 2026-05-27: extend the prose store to support v3_0
cluster publication. The existing 5-chapter `sc_v1_ch1..ch5` taxonomy from
2026-04-19 is stale (doesn't match the current 7-chapter Session C structure
or the v3_0 tier-prose model). Register the v3_0 types alongside, marking
v1 as superseded via metadata.

Three v3_0 type families:

1. **Chapter prose (per cluster, 7 chapters)** — `sc_v2_ch1`..`sc_v2_ch7`
   Scope: cluster. Authored as Session C output or assembled by the v3_0
   publication script.

2. **Tier publication prose (per characteristic, 8 tiers)** — `sc_v2_tier_T0`
   ..`sc_v2_tier_T7`. Scope: characteristic. Authored by AI DURING Phase 9
   batch (while tier context is fresh) — eliminates the Session C re-read.

3. **Cluster synthesis prose (per cluster)** — `sc_v2_synth_opening`,
   `sc_v2_synth_divine_pattern`, `sc_v2_synth_appendix`. Scope: cluster.
   Authored by AI DURING Phase 9 cluster-synthesis batch.

Idempotent: rows inserted only if the code doesn't already exist.
"""
from __future__ import annotations
import argparse, sqlite3, sys
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# v3_0 section type definitions
# (code, label, source_stage, lifecycle_tag, chapter_no, description, expected_min, expected_max, sort_order)
TYPES = [
    # === Chapter prose (per-cluster, 7 chapters) ===
    ("sc_v2_ch1", "Session C v2 — Ch1 What this study is",
     "session_c", "v2", 1,
     "Cluster opening — what this study is. Cluster-wide T0+T1 synthesis. Source tiers: T0+T1 cluster-scope.",
     300, 500, 201),
    ("sc_v2_ch2", "Session C v2 — Ch2 The characteristics in this study",
     "session_c", "v2", 2,
     "The characteristics in this study. Per-characteristic descriptions + anchor verses. Source: sub-group descriptions, characteristic table.",
     200, 400, 202),
    ("sc_v2_ch3", "Session C v2 — Ch3 The divine pattern",
     "session_c", "v2", 3,
     "The divine pattern. Cluster-wide T0 spine + per-characteristic T0 variations. Source tier: T0.",
     1500, 2500, 203),
    ("sc_v2_ch4", "Session C v2 — Ch4 Where each characteristic lives in the person",
     "session_c", "v2", 4,
     "Where each characteristic lives in the person. T2 + T3 per characteristic. Source tiers: T2, T3.",
     800, 1500, 204),
    ("sc_v2_ch5", "Session C v2 — Ch5 How each characteristic works",
     "session_c", "v2", 5,
     "How each characteristic works. T4 + T5 + T1 per characteristic. Source tiers: T4, T5, T1.",
     800, 1500, 205),
    ("sc_v2_ch6", "Session C v2 — Ch6 How each characteristic relates to the others",
     "session_c", "v2", 6,
     "How each characteristic relates to the others. T6 per characteristic. Source tier: T6.",
     400, 800, 206),
    ("sc_v2_ch7", "Session C v2 — Ch7 The view from outside Scripture",
     "session_c", "v2", 7,
     "The view from outside Scripture. T7 per characteristic plus general clinical-science knowledge. Source tier: T7.",
     400, 500, 207),

    # === Tier publication prose (per-characteristic, authored during Phase 9 batch) ===
    ("sc_v2_tier_T0", "Phase 9 tier prose — T0 Divine Image and Created Design",
     "session_b_phase9", "v2", None,
     "Per-characteristic publication prose summarising T0 findings. Authored by AI immediately after T0's 12 prompts in the Phase 9 batch (context-fresh). Consumed by Ch1+Ch3 of Session C.",
     200, 500, 211),
    ("sc_v2_tier_T1", "Phase 9 tier prose — T1 Inner Being Faculty in Operation",
     "session_b_phase9", "v2", None,
     "Per-characteristic publication prose summarising T1 findings. Authored by AI immediately after T1's 24 prompts. Consumed by Ch1+Ch5.",
     200, 500, 212),
    ("sc_v2_tier_T2", "Phase 9 tier prose — T2 Constitutional Location",
     "session_b_phase9", "v2", None,
     "Per-characteristic publication prose summarising T2 findings. Authored by AI immediately after T2's 31 prompts. Consumed by Ch4.",
     200, 500, 213),
    ("sc_v2_tier_T3", "Phase 9 tier prose — T3 Inner Being Faculties",
     "session_b_phase9", "v2", None,
     "Per-characteristic publication prose summarising T3 findings. Authored by AI immediately after T3's 33 prompts. Consumed by Ch4.",
     200, 500, 214),
    ("sc_v2_tier_T4", "Phase 9 tier prose — T4 Relational Interfaces",
     "session_b_phase9", "v2", None,
     "Per-characteristic publication prose summarising T4 findings. Authored by AI immediately after T4's 24 prompts. Consumed by Ch5.",
     200, 500, 215),
    ("sc_v2_tier_T5", "Phase 9 tier prose — T5 Transformation and Development",
     "session_b_phase9", "v2", None,
     "Per-characteristic publication prose summarising T5 findings. Authored by AI immediately after T5's 21 prompts. Consumed by Ch5.",
     200, 500, 216),
    ("sc_v2_tier_T6", "Phase 9 tier prose — T6 Inter-Characteristic Relationships",
     "session_b_phase9", "v2", None,
     "Per-characteristic publication prose summarising T6 findings. Authored by AI immediately after T6's 24 prompts. Consumed by Ch6.",
     200, 500, 217),
    ("sc_v2_tier_T7", "Phase 9 tier prose — T7 Lexical, Literary, and Scientific Analysis",
     "session_b_phase9", "v2", None,
     "Per-characteristic publication prose summarising T7 findings. Authored by AI immediately after T7's 20 prompts. Consumed by Ch7.",
     200, 500, 218),

    # === Cluster synthesis prose (per-cluster, authored during Phase 9 synthesis batch) ===
    ("sc_v2_synth_opening", "Phase 9 synthesis prose — Cluster opening (T0+T1 cluster-wide)",
     "session_b_phase9", "v2", 1,
     "Cluster-wide opening prose authored during Phase 9 synthesis (the 5th/last batch). Source: T0+T1 cluster-scope findings. Consumed directly by Ch1.",
     300, 500, 221),
    ("sc_v2_synth_divine_pattern", "Phase 9 synthesis prose — Divine pattern spine",
     "session_b_phase9", "v2", 3,
     "Cluster-wide divine-pattern spine prose authored during Phase 9 synthesis. Source: T0 cluster-scope findings. Consumed by Ch3 as the cluster-spine.",
     500, 1000, 223),
    ("sc_v2_synth_appendix", "Phase 9 synthesis prose — Cluster appendix",
     "session_b_phase9", "v2", None,
     "Free-form cluster-synthesis appendix prose (themes the 189-prompt structure does not fully capture). Authored during Phase 9 synthesis. Optional companion to chapters.",
     1000, 5000, 230),
]


def main(live: bool) -> int:
    print(f"=== v3_0 section_type registration — mode={'LIVE' if live else 'DRY-RUN'} ===")
    conn = sqlite3.connect(DB, timeout=120.0)
    conn.execute("PRAGMA busy_timeout = 120000")
    conn.row_factory = sqlite3.Row

    existing = {r["code"] for r in conn.execute(
        "SELECT code FROM prose_section_type WHERE COALESCE(delete_flagged,0)=0"
    ).fetchall()}
    print(f"Existing section_type codes: {len(existing)}")
    to_insert = [t for t in TYPES if t[0] not in existing]
    print(f"To insert: {len(to_insert)} new types (skipping {len(TYPES)-len(to_insert)} already present)")
    for t in to_insert[:5]:
        print(f"  + {t[0]}: {t[1]}")
    if len(to_insert) > 5:
        print(f"  ... and {len(to_insert)-5} more")

    if not live:
        print("\n[DRY-RUN]")
        conn.close()
        return 0

    cur = conn.cursor()
    cur.execute("BEGIN IMMEDIATE")
    try:
        for code, label, source_stage, lifecycle_tag, chapter_no, description, exp_min, exp_max, sort_order in to_insert:
            cur.execute(
                "INSERT INTO prose_section_type "
                "(code, label, source_stage, lifecycle_tag, chapter_no, description, expected_length_min, expected_length_max, sort_order, delete_flagged, created_at) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 0, ?)",
                (code, label, source_stage, lifecycle_tag, chapter_no, description, exp_min, exp_max, sort_order, NOW),
            )
        conn.commit()
        print(f"\nCOMMITTED: {len(to_insert)} new section_type rows")
    except Exception:
        conn.rollback()
        print("ROLLED BACK")
        raise
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    sys.exit(main(args.live))
