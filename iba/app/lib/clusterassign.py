"""clusterassign.py — the mechanical (HIGH-confidence-only) cluster-precedent matcher.

Codes the ONE deterministic tier of the cluster-allocation session's own reusable method
(`iba/docs/cluster assignment process/wa-global-cluster-alloc-sessionlog-v1_0-20260811.md` §4) —
P1, exact gloss match to an existing labelled `cluster_strong` row (`strong.stepGloss`). Judged
safe to automate without a researcher decision in that session ("HIGH... no decision needed");
everything else (precedent-conflict, profile-suggestion, no-signal) is deliberately left
unresolved here — that judgment tier stays a researcher/LLM-reviewed batch process, not something
this module auto-decides (session log §5: TF-IDF/profile scoring was tried and rejected for
HIGH — too noisy on short glosses).

**P2 (exact match against `cluster.gloss`'s own worked-example list) REMOVED 2026-09-17** —
researcher, verbatim: *"I dont think it make sense to have gloss on cluster level. gloss is a
strong level entity. this column can be removed"* (`#1720`). `cluster.gloss` is dropped from the
schema entirely, not just unused here.

Reused pitfalls from that session, not re-derived:
- Gloss matching is exact-string (trimmed, case-insensitive), never substring — avoids the
  ill/kill, sin/hissing false-positive class the session log's LOW-review pass hit and fixed.
- A precedent that resolves to MORE THAN ONE cluster is a conflict, not a HIGH match — returns
  None, left for a later judgment-tier pass.
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
    """(cluster_code, rationale) for a HIGH-confidence match, else None. `conn` is a plain
    sqlite3 connection (read-only here) — no writes, no STEP calls, deterministic.

    P2 (exact match against `cluster.gloss`'s own worked-example list) REMOVED 2026-09-17 —
    researcher, verbatim: *"I dont think it make sense to have gloss on cluster level. gloss is a
    strong level entity. this column can be removed"* (`#1720`). P1 already covers the strong-level
    signal this rule wants; `cluster.gloss` itself is dropped, not just its use here."""
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
