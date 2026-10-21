"""lexical.py — the `verse_lexical` engine (Layer 1): one row per CODE within a span, holding a
mechanically resolved, never interpreted, reading. Reuses `versespanmeaningreport`'s resolution
helpers (`_base`, `sibling_variant_codes`, `gloss_supported_by_tree`, `live_step_meaning`) rather
than re-deriving them, and persists the result.

Identity-stable writes (#1520, `write_readings_for_span`): a (span_id, code_ordinal) slot keeps
the same `verse_lexical.id` while it exists -- unchanged content is not written, changed content
is an `UPDATE ... WHERE id=?`, and only a slot that disappears (the span shrank) is soft-deleted.
`verse_lexical_note` depends on the id staying stable, as `operation.phenomenon_id` does in
`handlers/operations.py:phenomenon_set`.
"""

from __future__ import annotations

import datetime
import json
import pathlib
import sqlite3

from . import reportkit
from .versespanmeaningreport import (
    _BASE_RE_FALLBACK, _base, _range_str, detect_verse_gaps, fetch_verses, gap_note,
    merge_verses_and_gaps,
)


def _fetch_spans(conn: sqlite3.Connection, verse_id: int) -> list[dict]:
    """Same shape as versespanmeaningreport.fetch_spans, plus `id` (needed as the FK this table
    keys on) — a local copy rather than modifying the retiring module."""
    return [dict(r) for r in conn.execute(
        "SELECT id, position, surface, strong_variant, morph_code, is_particle "
        "FROM span WHERE verse_id=? AND deleted=0 ORDER BY position", (verse_id,),
    ).fetchall()]

# ── role (#1706, #1607) ──────────────────────────────────────────────────────────────────────────
# `role` is a JSON array of every live `cluster_strong.cluster_code` for this strong (T- and M-codes),
# e.g. `["T5","M12"]`, keyed on the EXACT strong code, never the base (#1806: siblings carry their
# own cluster judgements). It is also the base-data readiness signal (#1606): an empty array (no
# cluster_strong allocation) fails the run before any write (`unready_codes_in_scope`).


def load_role_codes(conn: sqlite3.Connection) -> dict[str, list[str]]:
    """EXACT strong_code -> sorted list of every live `cluster_strong.cluster_code` (T- and M-codes),
    loaded once per build call. A strong with no live cluster_strong row maps to [], the readiness
    failure state. Never keyed on `_base()` (#1806)."""
    out: dict[str, list[str]] = {}
    for r in conn.execute("SELECT strong, cluster_code FROM cluster_strong WHERE deleted=0"):
        out.setdefault(r["strong"], []).append(r["cluster_code"])
    return {strong: sorted(set(codes)) for strong, codes in out.items()}


def _role_for(code: str | None, role_codes: dict[str, list[str]]) -> str:
    codes = role_codes.get(code, []) if code else []
    return json.dumps(codes)


def unready_codes_in_scope(conn: sqlite3.Connection, verse_ids: list[int]) -> list[str]:
    """The pre-run readiness validator (#1606) -- every distinct strong code in a live span across
    `verse_ids` whose role would be empty (no live cluster_strong allocation). Non-empty means the
    scope is not ready; the caller fails fast before any write. Same exact-code lookup as `_role_for`."""
    if not verse_ids:
        return []
    ph = ",".join("?" * len(verse_ids))
    codes: set[str] = set()
    for r in conn.execute(
            f"SELECT strong_variant FROM span WHERE verse_id IN ({ph}) AND deleted=0 "
            f"AND strong_variant IS NOT NULL AND strong_variant != ''", tuple(verse_ids)):
        codes.update(r["strong_variant"].split())
    role_codes = load_role_codes(conn)
    return sorted(c for c in codes if not role_codes.get(c, []))


def stale_role_strongs_for_cluster(conn: sqlite3.Connection, cluster_code: str,
                                   member_strongs: list[str]) -> list[str]:
    """The pre-verse-reading freshness check (#1719). `verse_lexical.role` is a snapshot of
    `cluster_strong` taken at the last `lexical.build` for that verse and is not re-synced when
    cluster_strong changes. Reports member strongs whose live `verse_lexical` rows never carry
    `cluster_code` in `role` although `cluster_strong` lists them, since Layer 1 would never present
    them to the LLM. A strong with no live `verse_lexical` rows at all is handled elsewhere
    (`unready_codes_in_scope`, `lexicalscope.strongs_with_no_occurrence`)."""
    stale: list[str] = []
    for strong in member_strongs:
        rows = conn.execute(
            "SELECT role FROM verse_lexical WHERE strong=? AND deleted=0", (strong,)).fetchall()
        if not rows:
            continue
        if not any(cluster_code in (json.loads(r["role"]) if r["role"] else []) for r in rows):
            stale.append(strong)
    return stale


# ── resolution, per code ─────────────────────────────────────────────────────────────────────
# Layer 1 only confirms the strong is registered; meaning readings are Layer 2 observations
# (#1706, #1711). `role` is added in `_layer1_fields`.

def resolve_code(conn: sqlite3.Connection, code: str, morph_slice: str | None) -> dict:
    """One code's full verse_lexical row content (minus span_id/verse_id/code_ordinal, and minus
    the fields `_layer1_fields` adds). `_language` is transient, carried only for the Hebrew/Greek
    gate in `_layer1_fields`/`_narrative_morph_for`; never written (language lives at
    `verse_meta.language`)."""
    row = {"strong": code, "morph_code": morph_slice, "status": "unregistered", "_language": None}
    strong_row = conn.execute(
        "SELECT strongNumber, language FROM strong WHERE strongNumber=?", (code,)).fetchone()
    if strong_row is None:
        return row
    row["_language"] = strong_row["language"]
    row["status"] = "resolved"
    return row


# ── build + version-aware write, per span ────────────────────────────────────────────────────

def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ── Layer 1 mechanical fields (#1383) ──────────────────────────────────────────────────────────
# position/surface/testament/is_negator/narrative_morph/gloss_consistent_in_verse/party_kind --
# computed for every code, no selection (cfg_method_rule mechanical-columns-run-on-every-code-no-selection).

def load_code_classes(conn: sqlite3.Connection) -> dict[str, set[str]]:
    """EXACT strong_code -> set of live code-classes, from `cluster_strong` (a special status for a
    strong is a cluster, not cfg), loaded once per build call and threaded through
    (lexical-code-class-lookup-not-hardcoded). Keyed on the exact code, never `_base()` (#1810).

    `T5`/`T7`/`T8`/`T9`/`T4` here are `cluster.cluster_code` values (Negator/Party-Divine/
    Party-Human/Party-Angelic/Adversarial), not the verse-reading technique's T1-T9 or the
    observation catalogue's T0-T7 tiers. `T6` (Connective) is not read here."""
    _CLUSTER_CODE_TO_CLASS = {
        "T5": "negator", "T4": "party_adversarial", "T7": "party_divine",
        "T8": "party_human", "T9": "party_angelic",
    }
    out: dict[str, set[str]] = {}
    placeholders = ",".join("?" * len(_CLUSTER_CODE_TO_CLASS))
    for r in conn.execute(
            f"SELECT strong, cluster_code FROM cluster_strong "
            f"WHERE deleted=0 AND cluster_code IN ({placeholders})",
            tuple(_CLUSTER_CODE_TO_CLASS)):
        out.setdefault(r["strong"], set()).add(_CLUSTER_CODE_TO_CLASS[r["cluster_code"]])
    return out


def _code_classes_for(code: str, code_classes: dict[str, set[str]]) -> set[str]:
    return code_classes.get(code, set())




_PARTY_CLASS_TO_KIND = {"party_divine": "divine", "party_human": "human",
                        "party_angelic": "non_human", "party_adversarial": "non_human"}

_party_kind_parity_checked = False


def _assert_party_kind_parity(conn: sqlite3.Connection) -> None:
    """Checks _PARTY_CLASS_TO_KIND's output values (divine/human/non_human) against the live
    party_kind cfg_enum (#1796). Cached after the first call."""
    global _party_kind_parity_checked
    if _party_kind_parity_checked:
        return
    live = {r[0] for r in conn.execute(
        "SELECT value FROM cfg_enum WHERE name='party_kind' AND inactive=0")}
    local = set(_PARTY_CLASS_TO_KIND.values())
    if not local <= live:
        raise ValueError(f"_PARTY_CLASS_TO_KIND's own values ({sorted(local)}) include some not "
                         f"in live cfg_enum party_kind ({sorted(live)})")
    _party_kind_parity_checked = True


def _testament_for(conn: sqlite3.Connection, book: str) -> str | None:
    r = conn.execute("SELECT ordinal FROM cfg_book_order WHERE book=?", (book,)).fetchone()
    if r is None or r["ordinal"] is None:
        return None
    return "OT" if r["ordinal"] <= 38 else "NT"


def _narrative_morph_for(morph_slice: str | None, language: str | None,
                         sibling_codes: list[str]) -> str | None:
    """Hebrew only (narrative-morph-hebrew-only). wayyiqtol: this code's own morph is
    'HV<stem><TAM>...' with TAM='w' at 0-based index 3. az_imperfect_opening: same shape with
    TAM='i' (imperfect) AND some OTHER code in the SAME span has a base strong of H0227
    ("az"/"then") — verified live, Exod.15.1 (H7891 HVqi3ms + H0227A HD, same span).
    `sibling_codes`: every OTHER code's own `strong` in this same span (bare, not base-stripped —
    the `H0227%` prefix check below already covers every variant suffix)."""
    if language != "Hebrew" or not morph_slice or not morph_slice.startswith("HV") or len(morph_slice) < 4:
        return None
    tam = morph_slice[3]
    if tam == "w":
        return "wayyiqtol"
    if tam == "i" and any(c.startswith("H0227") for c in sibling_codes):
        return "az_imperfect_opening"
    return None


def _layer1_fields(row: dict, span: dict, sibling_codes: list[str], language: str | None,
                   testament: str | None, code_classes: dict[str, set[str]],
                   role_codes: dict[str, list[str]], base_pattern: str) -> None:
    """Mutates `row` (a resolve_code() result) in place, adding the Layer-1 mechanical fields --
    everything except gloss_consistent_in_verse, which needs the whole verse (_apply_gloss_consistency).
    `language` is not stored; it is passed for `_narrative_morph_for`'s Hebrew/Greek gate."""
    row["position"] = span["position"]
    row["surface"] = span["surface"]
    row["testament"] = testament
    code = row["strong"]
    row["role"] = _role_for(code, role_codes)
    classes = _code_classes_for(code, code_classes) if code else set()
    row["is_negator"] = 1 if "negator" in classes else None
    # Deterministic by resulting kind, never by set iteration order (#1810): classes mapping to the
    # same kind resolve; classes mapping to different kinds (e.g. H4317Q, human and angelic) are a
    # conflict written as None, left for Layer 2 to disambiguate per occurrence.
    party_kinds = {_PARTY_CLASS_TO_KIND[c] for c in classes if c in _PARTY_CLASS_TO_KIND}
    row["party_kind"] = next(iter(party_kinds)) if len(party_kinds) == 1 else None
    row["narrative_morph"] = _narrative_morph_for(row["morph_code"], language, sibling_codes)


def _apply_gloss_consistency(verse_rows: list[dict]) -> None:
    """Mutates every row in `verse_rows` in place: gloss_consistent_in_verse=0 iff this row's own
    (strong, morph_code) pair has >1 distinct SURFACE among this verse's rows, else 1 (never NULL).
    Keyed on `surface`, which varies by occurrence (#1527). Needs the whole verse, so it runs after
    every span in the verse is resolved."""
    groups: dict[tuple, set] = {}
    for r in verse_rows:
        if r["strong"] is None or r["morph_code"] is None:
            continue
        key = (r["strong"], r["morph_code"])
        groups.setdefault(key, set()).add(r.get("surface"))
    for r in verse_rows:
        if r["strong"] is None or r["morph_code"] is None:
            r["gloss_consistent_in_verse"] = 1
            continue
        key = (r["strong"], r["morph_code"])
        r["gloss_consistent_in_verse"] = 1 if len(groups[key]) <= 1 else 0


_CONTENT_FIELDS = ("strong", "morph_code", "role", "status",
                  "position", "surface", "testament", "is_negator",
                  "narrative_morph", "gloss_consistent_in_verse", "party_kind")


def write_readings_for_span(conn: sqlite3.Connection, span_id: int, verse_id: int,
                            resolved: list[dict]) -> dict:
    """Identity-stable write (#1520). Per code_ordinal within this span:
      - no live row yet             -> INSERT.
      - live row, content identical -> untouched: same id, same created_at, same
        `verse_lexical_note` attachments.
      - live row, content differs   -> `UPDATE ... WHERE id=?`, same id; `updated_at` records when.
      - a code_ordinal live before but with no resolved code now (the span shrank) -> soft-deleted;
        notes still pointing at it are counted as `removed_with_live_notes` for the caller to surface.

    Returns counts: inserted / updated / unchanged / removed / removed_with_live_notes."""
    c = {"inserted": 0, "updated": 0, "unchanged": 0, "removed": 0, "removed_with_live_notes": 0}
    now = _now()

    existing_by_ordinal = {row["code_ordinal"]: dict(row) for row in conn.execute(
        "SELECT * FROM verse_lexical WHERE span_id=? AND deleted=0", (span_id,)).fetchall()}
    seen_ordinals: set[int] = set()

    for ordinal, r in enumerate(resolved):
        seen_ordinals.add(ordinal)
        new_content = {f: r.get(f, 1 if f == "gloss_consistent_in_verse" else None)
                       for f in _CONTENT_FIELDS}
        existing = existing_by_ordinal.get(ordinal)

        if existing is None:
            conn.execute(
                "INSERT INTO verse_lexical (span_id, verse_id, code_ordinal, strong, morph_code, "
                "role, status, created_at, deleted, position, "
                "surface, testament, is_negator, narrative_morph, "
                "gloss_consistent_in_verse, party_kind) "
                "VALUES (?,?,?,?,?,?,?,?,0,?,?,?,?,?,?,?)",
                (span_id, verse_id, ordinal, new_content["strong"], new_content["morph_code"],
                 new_content["role"], new_content["status"], now, new_content["position"],
                 new_content["surface"], new_content["testament"],
                 new_content["is_negator"], new_content["narrative_morph"],
                 new_content["gloss_consistent_in_verse"], new_content["party_kind"]))
            c["inserted"] += 1
            continue

        if {f: existing.get(f) for f in _CONTENT_FIELDS} == new_content:
            c["unchanged"] += 1
            continue

        conn.execute(
            "UPDATE verse_lexical SET strong=?, morph_code=?, role=?, status=?, "
            "position=?, surface=?, testament=?, is_negator=?, "
            "narrative_morph=?, gloss_consistent_in_verse=?, party_kind=?, updated_at=? "
            "WHERE id=?",
            (new_content["strong"], new_content["morph_code"], new_content["role"],
             new_content["status"],
             new_content["position"], new_content["surface"],
             new_content["testament"], new_content["is_negator"], new_content["narrative_morph"],
             new_content["gloss_consistent_in_verse"], new_content["party_kind"], now,
             existing["id"]))
        c["updated"] += 1

    for ordinal, existing in existing_by_ordinal.items():
        if ordinal in seen_ordinals:
            continue
        conn.execute("UPDATE verse_lexical SET deleted=1 WHERE id=?", (existing["id"],))
        c["removed"] += 1
        c["removed_with_live_notes"] += conn.execute(
            "SELECT COUNT(*) FROM verse_lexical_note WHERE verse_lexical_id=? AND deleted=0",
            (existing["id"],)).fetchone()[0]
    return c


def build_for_verse(conn: sqlite3.Connection, verse_id: int,
                    base_pattern: str = _BASE_RE_FALLBACK,
                    code_classes: dict[str, set[str]] | None = None,
                    role_codes: dict[str, list[str]] | None = None) -> dict:
    """Called only from `build_for_range`/`build_for_verse_ids`, whose entry points run the readiness
    pre-check (`unready_codes_in_scope`)."""
    _assert_party_kind_parity(conn)
    c = {"spans": 0, "codes": 0, "inserted": 0, "updated": 0, "unchanged": 0, "removed": 0,
        "removed_with_live_notes": 0}
    if code_classes is None:          # safe default for a direct/standalone caller
        code_classes = load_code_classes(conn)
    if role_codes is None:            # safe default for a direct/standalone caller
        role_codes = load_role_codes(conn)

    verse_row = conn.execute("SELECT osisId FROM verse WHERE id=?", (verse_id,)).fetchone()
    book = verse_row["osisId"].split(".", 1)[0] if verse_row else None
    testament = _testament_for(conn, book) if book else None

    spans = _fetch_spans(conn, verse_id)
    per_span_resolved: list[tuple[dict, list[dict]]] = []
    for sp in spans:
        codes = (sp["strong_variant"] or "").split()
        morphs = (sp["morph_code"] or "").split()
        if not codes:
            continue
        resolved = [
            resolve_code(conn, code, morphs[i] if i < len(morphs) else None)
            for i, code in enumerate(codes)
        ]
        for i, r in enumerate(resolved):
            sibling_codes = [c for j, c in enumerate(codes) if j != i]
            _layer1_fields(r, sp, sibling_codes, r["_language"], testament,
                          code_classes, role_codes, base_pattern)
        per_span_resolved.append((sp, resolved))

    # gloss_consistent_in_verse needs the WHOLE verse's rows — one pass after every span resolved.
    all_rows = [r for _, resolved in per_span_resolved for r in resolved]
    _apply_gloss_consistency(all_rows)

    for sp, resolved in per_span_resolved:
        counts = write_readings_for_span(conn, sp["id"], verse_id, resolved)
        c["spans"] += 1
        c["codes"] += len(resolved)
        for k in ("inserted", "updated", "unchanged", "removed", "removed_with_live_notes"):
            c[k] += counts[k]
    return c


_TOTAL_KEYS = ("spans", "codes", "inserted", "updated", "unchanged", "removed",
              "removed_with_live_notes")


class NotReady(Exception):
    """Raised by `build_for_range`/`build_for_verse_ids` when `unready_codes_in_scope` finds any code
    in scope with zero cluster_strong allocation (#1606); the run does not proceed. `.codes` carries
    the list."""
    def __init__(self, codes: list[str]):
        self.codes = codes
        super().__init__(f"{len(codes)} code(s) in scope have no cluster_strong allocation "
                         f"(role would be []): {codes[:15]}{' ...' if len(codes) > 15 else ''}")


def build_for_range(conn: sqlite3.Connection, book: str, lo: int, hi: int,
                    verse_lo: int | None, verse_hi: int | None) -> dict:
    verses = fetch_verses(conn, book, lo, hi, verse_lo, verse_hi)
    unready = unready_codes_in_scope(conn, [v["id"] for v in verses])
    if unready:
        raise NotReady(unready)
    code_classes = load_code_classes(conn)
    role_codes = load_role_codes(conn)
    totals = {"verses": 0, **{k: 0 for k in _TOTAL_KEYS}}
    for v in verses:
        counts = build_for_verse(conn, v["id"], code_classes=code_classes, role_codes=role_codes)
        totals["verses"] += 1
        for k in _TOTAL_KEYS:
            totals[k] += counts[k]
    return totals


def build_for_verse_ids(conn: sqlite3.Connection, verse_ids: list[int]) -> dict:
    """Same shape as `build_for_range`, scoped to an explicit verse_id list (e.g. a per-word rebuild,
    `raw.lexical`, the `new-word` chain's closing step). Identity-stable: unchanged verses write
    nothing, changed ones are corrected in place, and attached `verse_lexical_note` rows survive.
    Dedups the input."""
    verse_ids = list(dict.fromkeys(verse_ids))     # de-dup, preserve order
    unready = unready_codes_in_scope(conn, verse_ids)
    if unready:
        raise NotReady(unready)
    code_classes = load_code_classes(conn)
    role_codes = load_role_codes(conn)
    totals = {"verses": 0, **{k: 0 for k in _TOTAL_KEYS}}
    for vid in verse_ids:
        counts = build_for_verse(conn, vid, code_classes=code_classes, role_codes=role_codes)
        totals["verses"] += 1
        for k in _TOTAL_KEYS:
            totals[k] += counts[k]
    return totals


# ── on-demand report — DB is the source, this is a render, never an independent write ────────

def _render_component(r: sqlite3.Row) -> str:
    if r["status"] == "unregistered":
        return f"{r['strong']} [{r['role']}]: (not yet registered)"
    return f"{r['strong']} [{r['role']}]"


def _tbl(headers: list[str], rows: list[list]) -> list[str]:
    L = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for r in rows:
        L.append("| " + " | ".join(str(c) if c is not None else "" for c in r) + " |")
    return L


def write_report(cfg, book: str, lo: int, hi: int, verse_lo: int | None = None,
                 verse_hi: int | None = None, book_label: str | None = None) -> pathlib.Path:
    """Reads verse_lexical — never re-derives from span/strong/strong_meaning_parsed. If nothing
    has been built yet for this exact range, that's `no-readings` (handlers/reports.py catches
    it) — run lexical.build first (ordinal 0 of the same work package)."""
    conn = cfg.conn
    verses = fetch_verses(conn, book, lo, hi, verse_lo, verse_hi)
    range_str = _range_str(lo, hi, verse_lo, verse_hi)
    label = f"{lo}:{verse_lo}-{verse_hi}" if verse_lo is not None else f"{lo}-{hi}"

    gaps = detect_verse_gaps(verses, verse_lo)
    per_chapter_total: dict[int, int] = {}
    per_chapter_covered: dict[int, int] = {}
    verse_lines: list[str] = []
    any_readings = False

    for ch, vn, kind, v in merge_verses_and_gaps(verses, gaps):
        if kind == "gap":
            verse_lines.append(gap_note(cfg, book, book_label, ch, vn))
            verse_lines.append("")
            continue

        spans = conn.execute(
            "SELECT id, position, surface, is_particle FROM span WHERE verse_id=? AND deleted=0 "
            "ORDER BY position", (v["id"],)).fetchall()
        rows = []
        for sp in spans:
            components = conn.execute(
                "SELECT * FROM verse_lexical WHERE span_id=? AND deleted=0 ORDER BY code_ordinal",
                (sp["id"],)).fetchall()
            if components:
                any_readings = True
            if not sp["is_particle"]:
                for c in components:
                    per_chapter_total[v["chapter"]] = per_chapter_total.get(v["chapter"], 0) + 1
                    if c["status"] == "resolved":
                        per_chapter_covered[v["chapter"]] = (
                            per_chapter_covered.get(v["chapter"], 0) + 1)
            reading = (" + ".join(_render_component(c) for c in components)
                      if components else "(not yet built — run lexical.build)")
            rows.append([sp["position"], sp["surface"] or "", reading])

        verse_lines.append(f"### {v['reference']}")
        verse_lines.append("")
        verse_lines.append(v["text"] or "")
        verse_lines.append("")
        verse_lines += _tbl(["#", "surface", "reading"], rows)
        verse_lines.append("")

    intro = [
        "> On-demand extract, generated from `verse_lexical` (never an independent write) — the "
        "resolved T1-T3 reading, connected units and morph-selected sense, not a per-code dump. "
        "Verse order = osisId parsed numerically, not table-id order.",
    ]
    if not any_readings:
        intro.append("")
        intro.append("> **Nothing built yet for this range** — run `lexical.build` first.")

    coverage_rows = [[ch, per_chapter_covered.get(ch, 0), tot,
                      f"{round(100 * per_chapter_covered.get(ch, 0) / tot) if tot else 0}%"]
                     for ch, tot in sorted(per_chapter_total.items())]
    sections = {
        "coverage": _tbl(["chapter", "resolved", "total", "%"], coverage_rows),
        "verses": verse_lines,
    }

    L = reportkit.render_scaffold(conn, "report.verse_lexical", sections, intro=intro,
                                  book=book, range=label)

    output_dir = pathlib.Path(cfg.required_setting("report.verse_analysis_output_dir"))
    pattern = cfg.required_setting("report.verse_lexical_output_pattern")
    folder = book_label or book
    filename = pattern.format(book=book.lower(), range=range_str)
    path = output_dir / folder / filename

    path = reportkit.write_report(conn, "report.verse_lexical", path, L)
    return path
