"""Validate Phase B B.1 constitution-debate output per v3_0 §6.1.7.

Stage gate checks:
  1. Every term has a verdict (STAYS / TRANSFERS-TO-Mxx / BOUNDARY).
  2. Every term in the cluster's mti_terms is covered by exactly one verdict.
  3. Every STAYS-with-cross_register_flag names a cluster destination + relationship.
  4. Every TRANSFERS rationale describes the verse-level relationship test.
  5. Every BOUNDARY verdict cites one of three valid §6.1.4 reasons.
  6. No verdict cites a forbidden ground (heuristic substring check).

Usage:
  python scripts/_validate_cluster_phase_b1_v1_20260528.py --cluster M38

Exit codes:
  0  PASS
  2  FAIL with delta report listing offending verdicts
"""
from __future__ import annotations
import argparse, json, sqlite3, sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

VALID_BOUNDARY_REASONS = {
    "cluster_membership_undecided",
    "homonymic_polysemic",
    "supportive_qualifying",
}

# Forbidden-ground heuristic patterns (substring match, lower-cased)
FORBIDDEN_PATTERNS = [
    "horizontal rather than vertical",
    "not god-directed",
    "lacks theological depth",
    "too circumstantial",
    "too sensory",
    "too negative",
    "morally negative",
    "analyst preference",
    "prefer not to be in scope",
]


def find_debate_json(cluster_code: str) -> Path:
    candidates = list(Path(f"Sessions/Session_Clusters/{cluster_code}").glob(
        f"WA-{cluster_code}-constitution-debate-v*.json"))
    if not candidates:
        raise FileNotFoundError(f"No constitution-debate JSON found for cluster {cluster_code}")
    return sorted(candidates)[-1]


def fetch_cluster_terms(db: str, cluster_code: str) -> set[str]:
    conn = sqlite3.connect(db)
    rows = conn.execute(
        "SELECT strongs_number FROM mti_terms WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
        (cluster_code,)
    ).fetchall()
    return {r[0] for r in rows}


def validate(debate_path: Path, cluster_terms: set[str]) -> tuple[bool, list[str]]:
    data = json.loads(debate_path.read_text(encoding="utf-8"))
    errors: list[str] = []
    verdicts = data.get("verdicts", [])

    seen_strongs: dict[str, dict] = {}

    # Check 1: every verdict has the required fields
    for i, v in enumerate(verdicts):
        strongs = v.get("strongs")
        verdict = v.get("verdict")
        rationale = v.get("rationale", "") or ""

        if not strongs:
            errors.append(f"  Verdict #{i}: missing 'strongs' field")
            continue
        if strongs in seen_strongs:
            errors.append(f"  Verdict #{i}: duplicate strongs {strongs}")
            continue
        seen_strongs[strongs] = v

        if not verdict:
            errors.append(f"  {strongs}: missing 'verdict' field")
            continue

        # Check 5: BOUNDARY requires valid reason
        if verdict == "BOUNDARY":
            reason = v.get("boundary_reason")
            if not reason:
                errors.append(f"  {strongs}: BOUNDARY missing 'boundary_reason'")
            elif reason not in VALID_BOUNDARY_REASONS:
                errors.append(f"  {strongs}: BOUNDARY reason '{reason}' not in valid set {sorted(VALID_BOUNDARY_REASONS)}")

        # Check 4: TRANSFERS requires transfer_test rationale
        if verdict.startswith("TRANSFERS"):
            test = v.get("transfer_test") or ""
            if not test or len(test) < 20:
                errors.append(f"  {strongs}: TRANSFERS missing or thin 'transfer_test' rationale (verse-level relationship test per §6.1.5)")

        # Check 3: STAYS with cross_register_flag must name destination + relationship
        if verdict == "STAYS" and v.get("cross_register_flag"):
            flag = v.get("cross_register_flag")
            # heuristic: must contain a cluster code (Mxx)
            has_cluster = any(f"M{n:02d}" in flag for n in range(1, 50)) or any(c in flag for c in ["M10b", "M10c"])
            if not has_cluster:
                errors.append(f"  {strongs}: STAYS cross_register_flag does not name a cluster destination: {flag[:80]}")

        # Check 6: forbidden-ground heuristic
        combined = (rationale + " " + str(v.get("boundary_reason", "")) + " " + str(v.get("cross_register_flag", ""))).lower()
        for pat in FORBIDDEN_PATTERNS:
            if pat in combined:
                errors.append(f"  {strongs}: verdict text contains forbidden-ground phrase '{pat}'")

    # Check 2: every cluster term covered exactly once
    debate_strongs = set(seen_strongs.keys())
    missing = cluster_terms - debate_strongs
    extra = debate_strongs - cluster_terms
    if missing:
        errors.append(f"  Cluster terms missing from debate: {sorted(missing)}")
    if extra:
        errors.append(f"  Debate contains terms not in cluster: {sorted(extra)}")

    return (len(errors) == 0), errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True, help="Cluster code, e.g. M38")
    ap.add_argument("--db", default="database/bible_research.db")
    args = ap.parse_args()

    cluster_terms = fetch_cluster_terms(args.db, args.cluster)
    debate_path = find_debate_json(args.cluster)
    print(f"Validating: {debate_path}")
    print(f"Cluster {args.cluster}: {len(cluster_terms)} active terms")

    ok, errors = validate(debate_path, cluster_terms)
    if ok:
        print(f"\nPASS — Phase B B.1 stage gate validated for cluster {args.cluster}")
        sys.exit(0)
    else:
        print(f"\nFAIL — {len(errors)} issues:")
        for e in errors:
            print(e)
        sys.exit(2)


if __name__ == "__main__":
    main()
