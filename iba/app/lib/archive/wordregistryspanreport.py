"""wordregistryspanreport.py — word_registry -> word_strong -> strong -> parse-meaning -> unique span
analysis for one registry word (`report.word_registry_span`).

Sections cluster Strong's by root family (`_cluster_by_related_strong`, from `strong_related`, STEP's
root cross-reference data). The table of contents also groups clusters by English gloss
(`_index_group_clusters`), so variations of one English word appear together even across unrelated
root families. Explicit `<a id>` anchors make the in-body ToC links work in every renderer.

Chain:
  word_registry (word)
    -> word_strong (word_id -> strong, exact code incl. suffix)
         -> strong (gloss/transliteration/language/count)
         -> strong_meaning_parsed (the exact strong_variant row; falls back to the base lemma, e.g.
              H3372 for H3372G, when the sub-entry has no row of its own)
         -> verse_lexical (strong match, deleted=0) -> span (surface = the inflected/translated text
              form tagged) -> verse (reference/text, one example per unique surface)

"Unique span" = distinct `span.surface` values tagged with that Strong's.

`strong.count` (STEP's "count") is Strong's-dictionary reference data, not a verse count in this
app's text: shown relabelled, alongside the real local `verse_lexical` occurrence/verse counts.
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
    """Checked for compliance first (#648): this module's STEP constant is flagged NON-COMPLIANT in
    cfg_utility, so cfg.assert_utility_compliant stops it until revised."""
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
                # `strong.count` is dictionary reference data, not a verse count: shown relabelled next to the
                # real local occurrence/verse counts
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

            # lemma_key is always the base: look up the exact strong_variant row first, then the base
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

    output_dir = pathlib.Path(cfg.required_setting("report.word_registry_span_output_dir"))
    output_dir.mkdir(parents=True, exist_ok=True)
    out = output_dir / f"{reg['word'].lower().replace(' ', '-')}-strong-span.md"
    out = reportkit.write_report(conn, STEP, out, L)
    return out
