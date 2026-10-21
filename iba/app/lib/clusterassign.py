"""clusterassign.py — the mechanical (HIGH-confidence-only) cluster-precedent matcher: P1, an exact
gloss match to an existing labelled `cluster_strong` row (`strong.stepGloss`), judged safe to
automate without a researcher decision. Everything else (precedent conflict, profile suggestion, no
signal) is left for a researcher/LLM-reviewed batch.

- Gloss matching is exact-string (trimmed, case-insensitive), never substring (avoids ill/kill,
  sin/hissing).
- A precedent resolving to more than one cluster is a conflict, not a HIGH match: returns None.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Rules:
    exclude_flag_from_voting: bool


_DEFAULTS = {
    "cluster.assign.exclude_flag_gloss_from_voting": True,
}


def load_rules(cfg) -> Rules:
    return Rules(
        exclude_flag_from_voting=bool(cfg.setting(
            "cluster.assign.exclude_flag_gloss_from_voting",
            _DEFAULTS["cluster.assign.exclude_flag_gloss_from_voting"])),
    )


def _norm(s: str | None) -> str:
    return (s or "").strip().casefold()


def match_precedent(conn, rules: Rules, step_gloss: str) -> tuple[str, str] | None:
    """(cluster_code, rationale) for a HIGH-confidence match, else None. `conn` is a plain sqlite3
    connection (read-only here): no writes, no STEP calls, deterministic."""
    target = _norm(step_gloss)
    if not target:
        return None

    # P1 — exact gloss match against existing cluster_strong-linked strong.stepGloss values.
    p1_clusters: set[str] = set()
    for row in conn.execute(
            "SELECT DISTINCT cs.cluster_code FROM cluster_strong cs "
            "JOIN strong s ON s.strongNumber = cs.strong AND s.deleted = 0 "
            "WHERE cs.deleted = 0 AND LOWER(TRIM(s.stepGloss)) = ?", (target,)):
        if rules.exclude_flag_from_voting and row[0] == "FLAG":
            continue
        p1_clusters.add(row[0])

    if len(p1_clusters) != 1:
        return None  # none, or a conflict — either way, not a HIGH match; defer

    code = next(iter(p1_clusters))
    return code, "P1 (prior-allocation gloss precedent)"
