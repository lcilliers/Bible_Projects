"""Load M10 Phase 9 synthesis findings into cluster_observation.

Source file: Sessions/Session_Clusters/M10/wa-cluster-M10-phase9-synthesis-findings-v1-20260524.md

Two parts in the source:
  PART A — per-tier reading guides (27 findings; markers `[M10-SYNTH] T{N}-GUIDE-{seq}`)
  PART B — cluster-scope observations (15 findings; markers `[M10-SYNTH] OBS-{NN} — {title}`)

Both load into `cluster_observation`:
  - PART A → observation_type='TIER_READING_GUIDE',
            target_phase='session_c',
            title='Tier T{N} guide #{seq}',
            description=body text (with no leading marker)
  - PART B → observation_type='CLUSTER_SYNTHESIS',
            target_phase='session_c',
            title=the OBS title from the marker,
            description=body text

Shared metadata:
  cluster_code = 'M10'
  characteristic_id = NULL (cluster-scope)
  cluster_subgroup_id = NULL
  source_phase = 'phase_9_synthesis'
  source_file = the .md path
  status = 'open'
  raised_date = NOW
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

SRC = REPO / "Sessions" / "Session_Clusters" / "M10" / "wa-cluster-M10-phase9-synthesis-findings-v1-20260524.md"
CLUSTER = "M10"
SOURCE_FILE_REL = "Sessions/Session_Clusters/M10/wa-cluster-M10-phase9-synthesis-findings-v1-20260524.md"

# Tier section header — used to track which tier we're inside for PART A
TIER_HEADER_RE = re.compile(r"^###\s+Tier\s+(T\d+)\b", re.MULTILINE)
# Tier guide marker
GUIDE_RE = re.compile(r"^\*\*\[M10-SYNTH\]\s+(T\d+)-GUIDE-(\d+)\*\*\s*$", re.MULTILINE)
# OBS marker (with title)
OBS_RE = re.compile(r"^\*\*\[M10-SYNTH\]\s+OBS-(\d+)\s+—\s+(.+?)\*\*\s*$", re.MULTILINE)
# PART boundaries
PART_A_RE = re.compile(r"^## PART A\b", re.MULTILINE)
PART_B_RE = re.compile(r"^## PART B\b", re.MULTILINE)


def parse_findings(text: str) -> tuple[list[dict], list[dict]]:
    """Return (tier_guides, obs_findings)."""
    part_a_match = PART_A_RE.search(text)
    part_b_match = PART_B_RE.search(text)
    if not part_a_match or not part_b_match:
        raise SystemExit("Could not locate PART A and PART B sections")

    part_a_text = text[part_a_match.end():part_b_match.start()]
    part_b_text = text[part_b_match.end():]

    # --- PART A: walk the part-A text; for each tier header, then each GUIDE marker ---
    tier_guides: list[dict] = []
    # Find all guide markers with positions
    guide_matches = list(GUIDE_RE.finditer(part_a_text))
    for i, m in enumerate(guide_matches):
        tier = m.group(1)
        seq = int(m.group(2))
        body_start = m.end()
        body_end = guide_matches[i + 1].start() if i + 1 < len(guide_matches) else len(part_a_text)
        body = part_a_text[body_start:body_end].strip()
        # Strip trailing horizontal rules / next tier header bleed
        # Cut at first "---" or "### " on its own line
        cut = re.search(r"\n---\s*$|\n### ", body, re.MULTILINE)
        if cut:
            body = body[:cut.start()].strip()
        tier_guides.append({
            "tier": tier,
            "seq": seq,
            "body": body,
        })

    # --- PART B: walk OBS markers ---
    obs_findings: list[dict] = []
    obs_matches = list(OBS_RE.finditer(part_b_text))
    for i, m in enumerate(obs_matches):
        seq = int(m.group(1))
        title = m.group(2).strip()
        body_start = m.end()
        body_end = obs_matches[i + 1].start() if i + 1 < len(obs_matches) else len(part_b_text)
        body = part_b_text[body_start:body_end].strip()
        cut = re.search(r"\n---\s*$|\n\*End of synthesis", body, re.MULTILINE)
        if cut:
            body = body[:cut.start()].strip()
        obs_findings.append({
            "seq": seq,
            "title": title,
            "body": body,
        })

    return tier_guides, obs_findings


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true", help="Apply (default: dry-run)")
    args = ap.parse_args()
    dry = not args.live

    if not SRC.exists():
        raise SystemExit(f"Source not found: {SRC}")

    text = SRC.read_text(encoding="utf-8")
    tier_guides, obs_findings = parse_findings(text)

    print(f"Parsed PART A (tier guides): {len(tier_guides)}")
    by_tier: dict[str, int] = {}
    for g in tier_guides:
        by_tier[g["tier"]] = by_tier.get(g["tier"], 0) + 1
    for tier in sorted(by_tier.keys()):
        print(f"  {tier}: {by_tier[tier]} guides")
    print(f"Parsed PART B (cluster observations): {len(obs_findings)}")
    print()

    # Sample preview
    print("Sample tier guide:")
    g0 = tier_guides[0]
    print(f"  [{g0['tier']}-GUIDE-{g0['seq']:02d}] body[:120]:")
    print(f"  {g0['body'][:200]}…")
    print()
    print("Sample OBS finding:")
    o0 = obs_findings[0]
    print(f"  OBS-{o0['seq']:02d} — {o0['title']}")
    print(f"  body[:120]: {o0['body'][:200]}…")
    print()

    # Body-length sanity
    short_guides = [g for g in tier_guides if len(g["body"]) < 100]
    short_obs = [o for o in obs_findings if len(o["body"]) < 100]
    if short_guides:
        print(f"WARN: {len(short_guides)} guide findings with body < 100 chars (suspicious parse)")
        for g in short_guides[:3]:
            print(f"  [{g['tier']}-GUIDE-{g['seq']}] '{g['body'][:80]}'")
    if short_obs:
        print(f"WARN: {len(short_obs)} OBS findings with body < 100 chars (suspicious parse)")

    if dry:
        print("\n[DRY-RUN — no DB writes]")
        return 0

    # --- LIVE ---
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("BEGIN")
    try:
        # Check for existing rows with the same source_file (idempotency guard)
        existing = cur.execute(
            "SELECT COUNT(*) FROM cluster_observation "
            "WHERE source_file=? AND COALESCE(delete_flagged,0)=0",
            (SOURCE_FILE_REL,),
        ).fetchone()[0]
        if existing:
            raise SystemExit(
                f"{existing} cluster_observation rows already loaded from this source file. "
                "Aborting to avoid duplicate ingestion. Use a fresh source file or soft-delete "
                "the existing rows first."
            )

        n_a = 0
        for g in tier_guides:
            title = f"M10 Phase 9 — Tier {g['tier']} reading guide #{g['seq']}"
            cur.execute(
                "INSERT INTO cluster_observation "
                "(cluster_code, characteristic_id, cluster_subgroup_id, source_phase, "
                "observation_type, target_phase, title, description, status, raised_date, "
                "source_file, delete_flagged, created_at, last_updated_date) "
                "VALUES (?, NULL, NULL, ?, ?, ?, ?, ?, 'open', ?, ?, 0, ?, ?)",
                (CLUSTER, "phase_9_synthesis", "TIER_READING_GUIDE", "session_c",
                 title, g["body"], NOW, SOURCE_FILE_REL, NOW, NOW),
            )
            n_a += 1

        n_b = 0
        for o in obs_findings:
            title = f"M10 cluster synthesis OBS-{o['seq']:02d} — {o['title']}"
            cur.execute(
                "INSERT INTO cluster_observation "
                "(cluster_code, characteristic_id, cluster_subgroup_id, source_phase, "
                "observation_type, target_phase, title, description, status, raised_date, "
                "source_file, delete_flagged, created_at, last_updated_date) "
                "VALUES (?, NULL, NULL, ?, ?, ?, ?, ?, 'open', ?, ?, 0, ?, ?)",
                (CLUSTER, "phase_9_synthesis", "CLUSTER_SYNTHESIS", "session_c",
                 title, o["body"], NOW, SOURCE_FILE_REL, NOW, NOW),
            )
            n_b += 1

        conn.commit()
        print(f"COMMITTED: {n_a} tier guides + {n_b} cluster observations = {n_a + n_b} rows.")
    except Exception:
        conn.rollback()
        print("ROLLED BACK")
        raise
    finally:
        conn.close()

    # Post-state
    conn = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    n_total_tier = conn.execute(
        "SELECT COUNT(*) FROM cluster_observation "
        "WHERE cluster_code=? AND observation_type='TIER_READING_GUIDE' "
        "AND COALESCE(delete_flagged,0)=0",
        (CLUSTER,)
    ).fetchone()[0]
    n_total_synth = conn.execute(
        "SELECT COUNT(*) FROM cluster_observation "
        "WHERE cluster_code=? AND observation_type='CLUSTER_SYNTHESIS' "
        "AND COALESCE(delete_flagged,0)=0",
        (CLUSTER,)
    ).fetchone()[0]
    conn.close()
    print(f"Post: M10 TIER_READING_GUIDE rows = {n_total_tier}")
    print(f"Post: M10 CLUSTER_SYNTHESIS rows = {n_total_synth}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
