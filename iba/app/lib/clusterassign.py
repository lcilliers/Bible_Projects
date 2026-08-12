"""clusterassign.py — the mechanical (HIGH-confidence-only) cluster-precedent matcher.

Codes the ONE deterministic tier of the cluster-allocation session's own reusable method
(`iba/docs/cluster assignment process/wa-global-cluster-alloc-sessionlog-v1_0-20260811.md` §4) —
P1 (exact gloss match to an existing labelled `cluster_strong` row) and P2 (exact gloss match to
`cluster.gloss`'s own worked-example list). Both were judged safe to automate without a researcher
decision in that session ("HIGH... no decision needed"); everything else (precedent-conflict,
profile-suggestion, no-signal) is deliberately left unresolved here — that judgment tier stays a
researcher/LLM-reviewed batch process, not something this module auto-decides (session log §5:
TF-IDF/profile scoring was tried and rejected for HIGH — too noisy on short glosses).

Reused pitfalls from that session, not re-derived:
- `FLAG`'s own gloss list is an uncertainty bag, not a positive signal — excluded from P2 voting
  (config-driven: `cluster.assign.exclude_flag_gloss_from_voting`).
- Gloss matching is exact-string (trimmed, case-insensitive), never substring — avoids the
  ill/kill, sin/hissing false-positive class the session log's LOW-review pass hit and fixed.
- A precedent that resolves to MORE THAN ONE cluster is a conflict, not a HIGH match — returns
  None, left for a later judgment-tier pass.
"""

from __future__ import annotations

import re
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


# cluster.csv's own gloss field shape: "term (translit), term (translit), ..." — split on the
# top-level comma (not commas inside a parenthetical) and pull just the term, not the transliteration.
_GLOSS_ENTRY_RE = re.compile(r"([^,(]+?)\s*\([^)]*\)")


def _cluster_gloss_terms(gloss: str | None) -> set[str]:
    if not gloss:
        return set()
    return {_norm(m.group(1)) for m in _GLOSS_ENTRY_RE.finditer(gloss)}


def match_precedent(conn, rules: Rules, step_gloss: str) -> tuple[str, str] | None:
    """(cluster_code, rationale) for a HIGH-confidence match, else None. `conn` is a plain
    sqlite3 connection (read-only here) — no writes, no STEP calls, deterministic."""
    target = _norm(step_gloss)
    if not target:
        return None

    # P1 — exact gloss match against existing cluster_strong-linked strong.stepGloss values.
    p1_clusters: set[str] = set()
    for row in conn.execute(
            "SELECT DISTINCT cs.cluster_code FROM cluster_strong cs "
            "JOIN strong s ON s.strongNumber = cs.strong AND s.deleted = 0 "
            "WHERE cs.deleted = 0 AND LOWER(TRIM(s.stepGloss)) = ?", (target,)):
        p1_clusters.add(row[0])

    # P2 — exact gloss match against cluster.gloss's own worked-example term list.
    p2_clusters: set[str] = set()
    for code, gloss in conn.execute(
            "SELECT cluster_code, gloss FROM cluster WHERE deleted = 0"):
        if rules.exclude_flag_from_voting and code == "FLAG":
            continue
        if target in _cluster_gloss_terms(gloss):
            p2_clusters.add(code)

    clusters = p1_clusters | p2_clusters
    if len(clusters) != 1:
        return None  # none, or a conflict — either way, not a HIGH match; defer

    code = next(iter(clusters))
    sources = []
    if code in p1_clusters:
        sources.append("P1 (prior-allocation gloss precedent)")
    if code in p2_clusters:
        sources.append("P2 (cluster.csv gloss-list precedent)")
    return code, " + ".join(sources)
