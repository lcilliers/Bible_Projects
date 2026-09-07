"""lexicalscope.py — selector-to-verse-id resolution for `lexical.run` (escalation #1549 rework,
2026-09-07). The old `-Book`+one-contiguous-`-Range`/`-Chapters` entry point `lexical.build`/
`lexical.enrich` shared is stale, researcher's own words: "it is fundamentally built on books and
passages which contradicts the analytic operation for clusters and groups of strongs." The real
input is a scattered, cross-book verse list generated as a subset via a cluster or group of
strongs — cluster/word are both converted to a strong-list first, which converts to a verse-list,
the actual lexical unit ("Implicitly a cluster request is in effect a request for a series of
strongs that is implicitly a series of verses").

**Why `span.strong_variant`, not `strong_verse`** — found and rejected live, same session:
`strong_verse` (used by `handlers/raw.py:lexical`, the per-WORD rebuild step) looked like the
obvious strong→verse lookup, but it undercounts — it's only populated for strongs belonging to an
individually-onboarded `word_registry` word. Verified: cluster M01's 100 strongs resolve to 892
verses via `strong_verse` vs **933** via `span.strong_variant` (the raw per-token STEP parse,
populated corpus-wide regardless of onboarding status) — a real 41-verse gap. `span.strong_variant`
is the complete source; matched as a whole space-separated token (a span can carry a compound code,
e.g. "H1234 H5678" — confirmed live, 118,922 of 378,149 live spans are compound), never a substring
match and never base-stripped (`reference_strong_related_keyed_on_exact_code_not_base`).
"""

from __future__ import annotations

import sqlite3


def _span_token_set(conn: sqlite3.Connection) -> set[str]:
    """Every exact code actually attested in a live span, corpus-wide — the real ground truth for
    "does this strong code have any occurrences at all," independent of whether `strong`'s own
    lexicon-catalogue row for it happens to exist yet (`lexicon.parse` backlog, see module
    docstring's #1553 addendum) or of `cluster_strong`/`word_strong` tagging (which can itself carry
    a stale/bare code — also see that addendum). Single query, reused by both the -StrongList guard
    and the cluster/word zero-occurrence check below, rather than trusting either lookup table on
    its own."""
    tokens: set[str] = set()
    for r in conn.execute("SELECT DISTINCT strong_variant FROM span WHERE deleted=0"):
        tokens.update((r["strong_variant"] or "").split())
    return tokens


def strongs_with_no_occurrence(conn: sqlite3.Connection, strongs: list[str],
                               span_tokens: set[str] | None = None) -> list[str]:
    """Of a resolved strong-list (from -ClusterCode/-Word/-StrongList), which have ZERO live span
    occurrences — a real, found-live data-sync gap: 3 `cluster_strong` rows (T7/T8, source=
    'migration-20260905-decfgification') carry the BARE form of a code (G1135/G2424/H0802) instead
    of the suffixed sub-entry `span.strong_variant` actually uses (G1135G/H, G2424G/I/J, H0802G/H/I)
    — those 3 rows can never match a real verse as currently stored. Not raised as an error here
    (a genuinely rare/unattested lemma legitimately belonging to a cluster is not itself a bug) —
    the caller surfaces this as a named warning, never silently drops it."""
    tokens = span_tokens if span_tokens is not None else _span_token_set(conn)
    return [s for s in strongs if s not in tokens]


def resolve_strongs(conn: sqlite3.Connection, cluster_code: str | None = None,
                    strong_list: list[str] | None = None, word: str | None = None) -> list[str]:
    """Exactly one of the three selectors. Returns the exact strong codes (deduped, order not
    meaningful) — never base-stripped, callers must not strip suffixes before or after this call."""
    given = [x for x in (cluster_code, strong_list, word) if x]
    if len(given) != 1:
        raise ValueError("resolve_strongs needs exactly one of cluster_code/strong_list/word")

    if cluster_code:
        rows = conn.execute(
            "SELECT DISTINCT strong FROM cluster_strong WHERE cluster_code=? AND deleted=0",
            (cluster_code,)).fetchall()
        if not rows:
            raise ValueError(f"cluster_code {cluster_code!r} has no live cluster_strong rows")
        return [r["strong"] for r in rows]

    if word:
        wrow = conn.execute(
            "SELECT id FROM word_registry WHERE word=? AND deleted=0", (word,)).fetchone()
        if wrow is None:
            raise ValueError(f"word {word!r} is not in word_registry")
        rows = conn.execute(
            "SELECT strong FROM word_strong WHERE word_id=? AND deleted=0", (wrow["id"],)).fetchall()
        if not rows:
            raise ValueError(f"word {word!r} has no live word_strong rows")
        return [r["strong"] for r in rows]

    deduped = list(dict.fromkeys(strong_list))   # preserve order
    # Guard against the known exact-suffix trap (reference_strong_related_keyed_on_exact_code_not_
    # base): a bare code like "H0430" matches NOTHING in `span.strong_variant`, which is always
    # suffixed ("H0430G") -- confirmed live, this exact case, while building this module. Validated
    # against ACTUAL SPAN PRESENCE, not the `strong` catalogue table -- found live, same session,
    # that `strong` undercounts too: 409 distinct span tokens (each with 1-2 real occurrences) have
    # no `strong` row at all yet (a `lexicon.parse` coverage lag, not a corruption), and validating
    # a -StrongList entry against `strong` would wrongly reject every one of those as "not found"
    # even though it resolves real verses. `strong` is still used, separately, to build the "did you
    # mean" suggestion when a code genuinely isn't attested anywhere.
    span_tokens = _span_token_set(conn)
    bad = [s for s in deduped if s not in span_tokens]
    if bad:
        known = {r["strongNumber"] for r in conn.execute(
            "SELECT strongNumber FROM strong WHERE deleted=0")}
        hints = {}
        for s in bad:
            variants = sorted(v for v in (known | span_tokens) if v.startswith(s))
            if variants:
                hints[s] = variants
        detail = "; ".join(
            f"{s!r} has no live span occurrence" +
            (f" -- did you mean {hints[s]}?" if s in hints else "")
            for s in bad)
        raise ValueError(f"{len(bad)} strong code(s) not attested in the corpus: {detail}")
    return deduped


def resolve_verse_ids_for_strongs(conn: sqlite3.Connection, strongs: list[str]) -> list[int]:
    """`span.strong_variant` is space-separated, possibly compound (see module docstring) — pulled
    once and token-matched in Python (same tokenization `lib/lexical.py`'s own build step uses:
    `(sp["strong_variant"] or "").split()`), not a per-strong SQL LIKE loop. 378k live spans is
    small enough this is a single cheap pass, and it sidesteps any LIKE-boundary edge case
    entirely — exact token-set membership, nothing else."""
    target = set(strongs)
    if not target:
        return []
    ids: set[int] = set()
    for r in conn.execute("SELECT verse_id, strong_variant FROM span WHERE deleted=0"):
        codes = (r["strong_variant"] or "").split()
        if target.intersection(codes):
            ids.add(r["verse_id"])
    return sorted(ids)


def resolve_verse_ids_for_refs(conn: sqlite3.Connection, verse_refs: list[str]) -> list[int]:
    """Direct OSIS-reference list (e.g. from a prior session's own finding) — no strong/cluster
    involved. Each ref must resolve to a live `verse` row; an unresolvable ref is a hard error
    naming it, never silently dropped."""
    ids: list[int] = []
    missing: list[str] = []
    for ref in dict.fromkeys(verse_refs):
        row = conn.execute("SELECT id FROM verse WHERE osisId=? AND deleted=0", (ref,)).fetchone()
        if row is None:
            missing.append(ref)
        else:
            ids.append(row["id"])
    if missing:
        raise ValueError(f"{len(missing)} verse ref(s) not found: {missing[:10]}"
                         f"{' ...' if len(missing) > 10 else ''}")
    return ids


def verse_id_by_osis_for(conn: sqlite3.Connection, verse_ids: list[int]) -> dict[str, int]:
    """The `{osisId: verse_id}` shape `lexicalenrich.enrich_passage`/`resolve_verse_lexical_id`
    need — built from an arbitrary verse_id list rather than `fetch_verses`'s book/range scan."""
    if not verse_ids:
        return {}
    ph = ",".join("?" * len(verse_ids))
    return {r["osisId"]: r["id"] for r in conn.execute(
        f"SELECT id, osisId FROM verse WHERE id IN ({ph}) AND deleted=0", tuple(verse_ids))}
