"""wordregistryspanreport.py — word_registry -> word_strong -> strong -> parse-meaning -> unique
span analysis, for one registry word. Built at the researcher's request 2026-08-09, generalising
the ad-hoc `tools/word_strong_span_report.py` prototype into a registered report
(`report.word_registry_span`) per PLAN-reports-config-governance-v1-20260722.md. Restructured
twice the same day:

1. Cluster by meaning rather than list flat by Strong's number (researcher: "the parse meaning
   must list the similar meaning together") — `_cluster_by_related_strong` below, using
   `strong_related` (STEP's own root-family cross-reference data), not a guessed similarity
   measure. Checked live against 'fear' (62 Strong's): 12 real multi-member clusters (e.g.
   G0870/G1630/G1719/G4423/G5398/G5399/G5400/G5401, the φόβος/φοβέω root family), 21 singletons.

2. Two more fixes, same day: (a) the ToC links didn't actually work — see the module docstring in
   `reportkit.py`'s `render_scaffold` for the root cause (renderer-dependent auto-slug mismatch,
   fixed there with explicit `<a id>` anchors; the same fix is applied here for this report's OWN
   in-body cluster ToC). (b) the researcher noticed the root-based clustering can legitimately
   split words an English reader would call synonyms into different sections (e.g. 'devout' shows
   up in two etymologically UNRELATED clusters — `strong_related` confirms zero edges between
   them; STEP genuinely records no shared root). Root-based clustering is correct and stays as the
   actual section structure — but the researcher also wants a second, English-gloss-based grouping
   layer purely for the table of contents, so browsing shows "several rows for the different
   variations of fear" together even though they're separate root families. See
   `_index_group_clusters` below.

Chain:
  word_registry (word)
    -> word_strong (word_id -> strong, exact code incl. suffix)
         -> strong (gloss/transliteration/language/count)
         -> strong_meaning_parsed (lemma_key = strong; falls back to the base lemma — e.g. H3372
              for H3372G — when the suffixed sub-entry has no rows of its own, since STEP's meaning
              tree lives under the base and is shared across sub-entries)
         -> verse_lexical (strong match, deleted=0) -> span (surface = the actual inflected/
              translated text form tagged) -> verse (reference/text, one example per unique surface)

"Unique span" = distinct `span.surface` values tagged with that Strong's — the different surface
realisations ("applications") a lemma took across its occurrences, not `resolved_sense` (checked:
fixed per Strong's in this data, so surface diversity carries the real signal here).

`strong.count` (STEP's `call2_getInfo` "count" field) is fixed Strong's-dictionary reference data
— NOT a verse-occurrence count in this app's Bible text, confirmed live 2026-08-10 (BUILD.md §88):
it returns byte-identical regardless of which Bible module/version is queried, including modules
that can't sensibly answer for the code at all. Shown here relabelled, alongside the real local
`verse_lexical` occurrence/verse counts — never presented alone as if it meant "how many verses."
"""

from __future__ import annotations

import pathlib
import re

from . import reportkit

STEP = "report.word_registry_span"

_STOPWORDS = {"to", "be", "a", "an", "the", "of"}


def _base_strong(strong: str) -> str | None:
    """H3372G -> H3372 (sub-entry suffix stripped); None if strong has no suffix."""
    m = re.match(r"^([HG]\d{4})([A-Z]+)$", strong)
    return m.group(1) if m else None


def _cluster_by_related_strong(strongs: list[str], edges: list[tuple[str, str]]) -> list[list[str]]:
    """The REAL clustering — union-find over `strongs`, connected by `edges` (from
    strong_related, both ends already restricted to `strongs` by the caller). This is what the
    report's body sections are actually organised by: shared Greek/Hebrew root, per STEP's own
    recorded data. Returns clusters as sorted-member lists, ordered by each cluster's lowest
    Strong's code — deterministic, matches the plain alphabetical-by-strong ordering this report
    used before clustering existed."""
    parent = {s: s for s in strongs}

    def find(x: str) -> str:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: str, b: str) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for a, b in edges:
        union(a, b)

    groups: dict[str, list[str]] = {}
    for s in strongs:
        groups.setdefault(find(s), []).append(s)
    clusters = [sorted(members) for members in groups.values()]
    clusters.sort(key=lambda members: members[0])
    return clusters


def _core_words(gloss: str) -> set[str]:
    """Lowercase word tokens from a gloss, stopwords/short words dropped — "to fear" -> {"fear"},
    "fearful thing" -> {"fearful", "thing"}. Purely mechanical (regex split + a fixed stopword
    list), no stemming library and no fabricated synonym table — every grouping this feeds is
    traceable back to an exact substring relationship between two glosses actually in the DB."""
    words = re.findall(r"[a-zA-Z']+", gloss.lower())
    return {w for w in words if w not in _STOPWORDS and len(w) >= 3}


def _shares_word(a: str, b: str) -> bool:
    """True if the shorter word is a prefix of the longer (or they're equal) — "fear"/"fearful",
    "tremble"/"trembling", "devout"/"devout". A crude but fully transparent stand-in for a real
    stemmer: every match this produces can be read directly off the two literal words."""
    shorter, longer = (a, b) if len(a) <= len(b) else (b, a)
    return longer.startswith(shorter)


def _index_group_clusters(clusters: list[list[str]], cluster_words: list[set[str]]
                          ) -> list[tuple[str | None, list[int]]]:
    """Groups CLUSTER INDICES (not Strong's) by shared English gloss word — the researcher's
    second ask: keep the root-based clusters as the real section structure, but additionally
    surface "several rows for the different variations of fear" together in the table of
    contents, even though they're separate root families.

    Deliberately a SINGLE HOP off one designated head per group, not a full transitive closure —
    a first draft used union-find (any cluster sharing a word with ANY other already-grouped
    cluster joins the group) and, checked live against 'fear', it over-merged: a cluster glossed
    "to revere" shares the word "revere" with a cluster glossed "to fear: revere" (a real,
    accurate overlap — STEP's own Hebrew gloss for that lemma covers both senses), which pulled
    the whole "reverence" family into the "fear" group; that reverence family ALSO happens to
    share "devout" with an unrelated "God/godly" family, which came along too — three genuinely
    different root families collapsed into one mislabelled "fear" bucket, two hops removed from
    fear itself. Classic single-linkage chaining. Anchoring every group to its earliest-ordered
    member and matching every OTHER cluster only against THAT head's words (never against
    already-added members) caps this at one hop by construction: everything in a group is
    guaranteed to share a word with the group's head, even if two non-head members share nothing
    with each other. Known trade-off, not silently hidden: some genuine variant spellings this
    still misses if they never co-occur with a common form (e.g. "tremble" is not literally a
    substring-prefix of "trembling" — English drops the 'e' before '-ing' — so those two only end
    up together if some cluster in between happens to gloss with the exact matching form)."""
    n = len(clusters)
    assigned = [False] * n
    result: list[tuple[str | None, list[int]]] = []
    for i in range(n):
        if assigned[i]:
            continue
        assigned[i] = True
        members = [i]
        word_votes: dict[str, int] = {}
        for j in range(i + 1, n):
            if assigned[j]:
                continue
            hit = None
            for w1 in cluster_words[i]:
                w2 = next((w for w in cluster_words[j] if _shares_word(w1, w)), None)
                if w2:
                    hit = w1 if len(w1) <= len(w2) else w2
                    break
            if hit:
                assigned[j] = True
                members.append(j)
                word_votes[hit] = word_votes.get(hit, 0) + 1
        label = (max(word_votes.items(), key=lambda kv: (kv[1], -len(kv[0])))[0]
                if len(members) > 1 else None)
        result.append((label, members))
    return result


def write_report(cfg, word: str) -> pathlib.Path | None:
    """Checked for compliance first (escalation #648, 2026-08-17) — this module's own STEP
    constant is hardcoded, flagged NON-COMPLIANT in cfg_utility; using it now signals (via
    cfg.assert_utility_compliant) that it needs revision before this is called again."""
    cfg.assert_utility_compliant("iba/app/lib/wordregistryspanreport.py")
    conn = cfg.conn
    q = lambda sql, p=(): conn.execute(sql, p).fetchall()

    reg = q("SELECT * FROM word_registry WHERE deleted=0 AND lower(word)=lower(?)", (word,))
    if not reg:
        return None
    reg = reg[0]

    strongs = [r["strong"] for r in q(
        "SELECT DISTINCT strong FROM word_strong WHERE word_id=? AND deleted=0 ORDER BY strong",
        (reg["id"],))]

    intro = [
        f"- registry id: {reg['id']}",
        f"- status: {reg['status']}",
        f"- source: {reg['source']}",
        f"- linked Strong's: {len(strongs)}",
    ]

    sections: dict[str, list[str]] = {}
    sections["overview"] = intro if strongs else intro + ["", "*No Strong's linked — nothing to analyse.*"]

    # gloss lookup, once, for cluster-label building
    gloss_of: dict[str, str | None] = {}
    for strong in strongs:
        srow = q("SELECT stepGloss FROM strong WHERE strongNumber=? AND deleted=0", (strong,))
        gloss_of[strong] = srow[0]["stepGloss"] if srow else None

    edges = [(r["strong"], r["related_strong"]) for r in q(
        "SELECT strong, related_strong FROM strong_related WHERE strong IN ({}) AND "
        "related_strong IN ({})".format(",".join("?" * len(strongs)), ",".join("?" * len(strongs))),
        (*strongs, *strongs))] if strongs else []
    clusters = _cluster_by_related_strong(strongs, edges) if strongs else []

    def cluster_label(members: list[str]) -> str:
        """Deduped glosses (case-insensitive, order preserved), joined — the meaning-first ToC/
        heading text the researcher asked for. Falls back to the Strong's code itself for any
        member with no gloss at all, rather than dropping it silently."""
        seen: list[str] = []
        seen_lower: set[str] = set()
        for m in members:
            g = gloss_of.get(m) or m
            if g.lower() not in seen_lower:
                seen.append(g)
                seen_lower.add(g.lower())
        return ", ".join(seen)

    heading_of: list[str] = []
    anchor_of: list[str] = []
    body: list[str] = []
    for members in clusters:
        label = cluster_label(members)
        heading_text = f"{label} — {', '.join(members)}"
        slug = reportkit.anchor(heading_text)
        heading_of.append(heading_text)
        anchor_of.append(slug)

        body.append(f'<a id="{slug}"></a>')
        body.append(f"### {heading_text}")
        body.append("")
        if len(members) > 1:
            body.append(f"*{len(members)} related Strong's (per `strong_related`).*")
            body.append("")

        for strong in members:
            srow = q("SELECT stepGloss, stepTransliteration, language, count FROM strong "
                     "WHERE strongNumber=? AND deleted=0", (strong,))
            srow = srow[0] if srow else None
            if len(members) > 1:
                body.append(f"#### {strong}" + (f" — {srow['stepGloss']}" if srow and srow["stepGloss"] else ""))
                body.append("")
            else:
                body.append(f"**Strong's:** {strong}")
                body.append("")
            if srow:
                # `strong.count` (STEP's call2_getInfo "count" field) is NOT a verse-occurrence
                # count — confirmed live 2026-08-10 (iba/app/reports/g2128-verse-lexical-by-
                # strong-sample-20260810.md addendum): calling getInfo for the SAME code under
                # nine different {version} values, including Hebrew-only modules that can't
                # sensibly answer for a Greek code at all, returned the IDENTICAL count every
                # time. It is fixed Strong's-dictionary reference data (global, corpus-
                # independent — plausibly NT+LXX+cited literature per the lsjDefs citations),
                # never scoped to any Bible text this app actually holds. Labelling it "STEP
                # total count" implied it meant "how many verses does this occur in" — wrong,
                # and the true figure (this DB's actual verse_lexical coverage) is usually far
                # smaller (e.g. G2128: dictionary count 52 vs 8 real verses). Replaced with the
                # real local occurrence/verse counts; the dictionary number is kept alongside,
                # relabelled so it can't be misread as a verse count again.
                occ = q("SELECT COUNT(*) n, COUNT(DISTINCT vl.verse_id) v FROM verse_lexical vl "
                       "WHERE vl.strong=? AND vl.deleted=0", (strong,))[0]
                body.append(f"transliteration: *{srow['stepTransliteration']}* &nbsp;|&nbsp; "
                           f"language: {srow['language']} &nbsp;|&nbsp; "
                           f"verse_lexical occurrences: {occ['n']} "
                           f"({occ['v']} verse{'s' if occ['v'] != 1 else ''}) &nbsp;|&nbsp; "
                           f"STEP lexicon count (dictionary-wide, NOT verse-scoped — see BUILD.md "
                           f"§88): {srow['count']}")
            else:
                body.append("*(no `strong` row for this code — not yet onboarded)*")
            body.append("")

            # Bug found + fixed 2026-08-10, building on `healing`'s meaning-table backfill
            # (BUILD.md — same session): this was querying `lemma_key=?` with the FULL
            # sub-lettered code — but `strong_meaning_tree`/`strong_meaning_parsed`.lemma_key is
            # always the BASE (added by migration/fix_strong_meaning_tree_collapse.py,
            # 2026-07-26, which gave both tables a `strong_variant` column for exactly this exact-
            # match case and updated every OTHER reader — `versespanmeaningreport.py`,
            # `build_verse_span_meaning_extract.py` — to use it; this report was never migrated).
            # `lemma_key=strong` for a sub-lettered code (e.g. 'H7965I') never matches anything
            # (no row's lemma_key is ever 'H7965I', only 'H7965'), so this ALWAYS fell through to
            # the base fallback below, silently, for every sub-lettered code — even ones that DO
            # have their own exact-variant row (confirmed live: `healing`'s H7965G-L/H2492A/H5414P
            # kept showing "no rows under X itself" immediately AFTER their own exact-variant rows
            # were backfilled, because this query was never actually capable of finding them).
            senses = q("SELECT sense_code, gloss FROM strong_meaning_parsed "
                      "WHERE strong_variant=? AND deleted=0 ORDER BY sort", (strong,))
            fallback_base = None
            if not senses:
                base = _base_strong(strong)
                if base:
                    senses = q("SELECT sense_code, gloss FROM strong_meaning_parsed "
                              "WHERE lemma_key=? AND deleted=0 ORDER BY sort", (base,))
                    if senses:
                        fallback_base = base
            body.append("**Parse meaning:**")
            body.append("")
            if fallback_base:
                body.append(f"*(no rows under {strong} itself — base lemma {fallback_base}'s "
                           f"meaning tree, shared across its sub-entries)*")
                body.append("")
            if senses:
                for s in senses:
                    body.append(f"- {(s['sense_code'] or '')} {(s['gloss'] or '')}".strip())
            else:
                body.append("*(no `strong_meaning_parsed` rows for this lemma or its base)*")
            body.append("")

            surfaces = q(
                "SELECT s.surface, COUNT(*) n FROM verse_lexical vl JOIN span s ON s.id=vl.span_id "
                "WHERE vl.strong=? AND vl.deleted=0 GROUP BY s.surface ORDER BY n DESC, "
                "s.surface ASC", (strong,))
            body.append(f"**Unique spans (distinct surface applications): {len(surfaces)}**")
            body.append("")
            if not surfaces:
                body.append("*(no `verse_lexical` occurrences for this Strong's yet — not built "
                           "in any processed book)*")
            else:
                for srf in surfaces:
                    ex = q(
                        "SELECT v.reference, v.text FROM verse_lexical vl "
                        "JOIN span s ON s.id=vl.span_id JOIN verse v ON v.id=vl.verse_id "
                        "WHERE vl.strong=? AND vl.deleted=0 AND s.surface=? ORDER BY v.id LIMIT 1",
                        (strong, srf["surface"]))[0]
                    body.append(f"- **\"{srf['surface']}\"** ({srf['n']}x) — e.g. *{ex['reference']}*: "
                              f"\"{ex['text']}\"")
            body.append("")

    if clusters:
        cluster_words = [
            {w for m in members for w in _core_words(gloss_of.get(m) or "")}
            for members in clusters
        ]
        index_groups = _index_group_clusters(clusters, cluster_words)

        toc = [
            f"**{len(clusters)}** meaning cluster(s) across **{len(strongs)}** Strong's, grouped "
            f"below by shared root (`strong_related` — same noun/verb/adjective family, e.g. "
            f"δειλία/δειλιάω/δειλός). The index that follows groups those SAME clusters a second "
            f"way, by shared English gloss word, purely so related-looking variations sit "
            f"together for browsing — a shared row here does **not** imply a shared root; see "
            f"the sections themselves (and each one's `strong_related` note) for the real "
            f"relationship.",
            "",
        ]
        for label, members in index_groups:
            if label is None:
                i = members[0]
                toc.append(f"- [{heading_of[i]}](#{anchor_of[i]})")
            else:
                toc.append(f"**{label}** ({len(members)} variant(s) — separate root families "
                          f"unless a section below says otherwise):")
                for i in members:
                    toc.append(f"  - [{heading_of[i]}](#{anchor_of[i]})")

        strongs_section = toc + [""] + body
    else:
        strongs_section = ["*No linked Strong's.*"]

    sections["strongs"] = strongs_section

    L = reportkit.render_scaffold(conn, STEP, sections, intro=None, word=reg["word"])

    output_dir = pathlib.Path(cfg.setting("report.word_registry_span_output_dir",
                                          "iba/app/verse-analysis/word_registry"))
    output_dir.mkdir(parents=True, exist_ok=True)
    out = output_dir / f"{reg['word'].lower().replace(' ', '-')}-strong-span.md"
    out = reportkit.write_report(conn, STEP, out, L)
    return out
