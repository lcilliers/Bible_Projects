"""lexical.py — the `verse_lexical` engine: T1-T3 of the verse-lexical technique
(`iba/docs/WA-verse-reading-technique-v4-2026-08-05.md`), mechanised. Replaces
`report.verse_span_meaning`'s per-span dump with one row per CODE within a span, holding a
mechanically resolved — never interpreted — reading. Full design record:
`iba/app/reports/t1-t3-design-decisions-20260805.md`.

Reuses `versespanmeaningreport`'s exact-variant/base-fallback resolution and its sibling/base
ambiguity check (`_base`, `sibling_variant_codes`, `gloss_supported_by_tree`, `live_step_meaning`)
rather than re-deriving them — same underlying facts, this module adds role classification and
stem/voice selection on top, then persists the result instead of only rendering it.

Runs independent of T4-T9 and `report.passage_debate` — no awareness of either. Identity-stable
writes (redesigned 2026-09-05, escalation #1520 — see `write_readings_for_span`'s own docstring
for the full rationale): a (span_id, code_ordinal) slot keeps the same `verse_lexical.id` for as
long as it exists, whether its content is confirmed unchanged (no write at all) or genuinely
corrected (real `UPDATE ... WHERE id=?`) — never soft-delete-and-reinsert for a slot that still
exists. Matches `handlers/operations.py:phenomenon_set`'s own in-place-UPDATE convention, used
there for the same reason: a downstream FK (`verse_lexical_note`, like `operation.phenomenon_id`)
depends on the id staying stable. Only a slot that genuinely disappears (the span shrank) is
soft-deleted for real — `verse`/`span`/`strong`'s own supersede-on-every-write convention remains
correct for those tables (nothing external held a durable pointer into their old ids the way
`verse_lexical_note` does into this one) and is deliberately NOT changed here.
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

# ── role — REDESIGNED 2026-09-16 (escalation #1706 Phase B item 3, #1607 D1/D4) ─────────────────
# Full rebuild, not a patch: the OLD role (a 'content'/'function' morph-tag classifier, below in
# git history) is DELETED, not fixed — it's the exact mechanism escalation #1590 diagnosed as
# buggy (the Greek article tag 'T' misclassified content instead of function), and per #1592/#1607
# it's being replaced wholesale, not repaired. `role` is now a bare JSON array of every live
# `cluster_strong.cluster_code` for this strong (T-codes AND M-codes both, not just the T4/T5/T7/
# T8/T9 subset `load_code_classes` below restricts to) — e.g. `["T5","M12"]`, not an array of
# objects (researcher, verbatim, 2026-09-16: "the column value should include the role(s) of the
# word in the row" — a plain list, D1's own volume note: "not more than 3-4 cluster codes").
# `role` is ALSO now the base-data readiness signal itself (#1606 D1, researcher verbatim,
# 2026-09-09/10): "role is almost the validator that the base data is ready for lexical
# analysis... if role is null for any word in the span for the scope, the validation fails and the
# run does not proceed" — an empty array (no cluster_strong allocation at all) is that failure
# state; see `unready_codes_in_scope` below, called by every build entry point BEFORE any write.
#
# CORRECTED 2026-09-20 (escalation #1806) — `load_role_codes`/`_role_for`/`unready_codes_in_scope`
# used to key on `_base(strong)` (the suffix-letter-stripped code), unioning cluster_strong across
# every sub-lettered sibling sharing a base number. Found live: verse_id 7478 span 637365 (strong
# H7725O, cluster_strong live-allocated to M11 only) carried role `["M11","M81","T3"]` — M81 and T3
# belong to siblings H7725N and H7725G/H/I/J/K/L/M respectively, never to H7725O itself.
# `cluster_strong` treats each suffixed code as an independently-assigned entry (confirmed: those
# siblings carry different, separately-made cluster judgements) — unioning them back together in
# `role` tagged verses for clusters unrelated to the word actually occurring there. Researcher
# ruling, verbatim, this chat: the span's `strong_variant` is "the strong that need to be carried in
# the strong table, need to be associated with a cluster, and need to be the role" — a direct
# lookup, not a computed aggregation. Matches the project's own established rule elsewhere
# (`reference_strong_related_keyed_on_exact_code_not_base`: exact code, never base). All three
# functions below now key on the EXACT strong code. `handlers/lexical.py:readiness()` Leg 3 was
# already exact-match (never needed this fix); this brings `role` in line with it. Affected
# 69,563 of 544,667 live `verse_lexical` rows at time of fix — rebuilt via `build_for_verse_ids`
# over every affected verse_id (see BUILD.md for the rebuild record), not left for the next
# incidental `lexical.build` call to silently correct.


def load_role_codes(conn: sqlite3.Connection) -> dict[str, list[str]]:
    """EXACT strong_code -> sorted list of every live `cluster_strong.cluster_code` (T-codes and
    M-codes both) — the full set, unlike `load_code_classes` below (which stays, unchanged, for
    is_negator/party_kind's own narrower T4/T5/T7/T8/T9 need — a deliberately different, base-keyed
    lookup for a different field, see its own docstring). Loaded once per build call, same pattern
    as load_code_classes/live_cache. A strong with no live cluster_strong row of any kind maps to
    [] — the empty-array readiness-failure state `unready_codes_in_scope` checks for.

    Keyed on the EXACT code, never `_base()` — see the module banner above (escalation #1806,
    2026-09-20): base-keying pulled in unrelated siblings' cluster allocations."""
    out: dict[str, list[str]] = {}
    for r in conn.execute("SELECT strong, cluster_code FROM cluster_strong WHERE deleted=0"):
        out.setdefault(r["strong"], []).append(r["cluster_code"])
    return {strong: sorted(set(codes)) for strong, codes in out.items()}


def _role_for(code: str | None, role_codes: dict[str, list[str]]) -> str:
    codes = role_codes.get(code, []) if code else []
    return json.dumps(codes)


def unready_codes_in_scope(conn: sqlite3.Connection, verse_ids: list[int]) -> list[str]:
    """The pre-run readiness validator (#1606 D1) — every DISTINCT strong code occurring in a live
    span across `verse_ids` that would resolve to an EMPTY role array (no live cluster_strong
    allocation at all). Non-empty return means the scope is not ready; the caller fails fast,
    before any resolve/write happens — same EXACT-code lookup `_role_for` itself uses (escalation
    #1806, 2026-09-20 — no longer base-stripped), so a code this reports as unready is exactly one
    whose `role` would otherwise be written as `[]`."""
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
    """The pre-`verse-reading` freshness check (`#1719`, found and required live 2026-09-17 running
    `M67`/`M60`, researcher instruction same day: *"before starting verse-reading, a validation
    check must be performed to ensure that the lexical for the cluster in focus is up to date"*).

    `verse_lexical.role` is a point-in-time snapshot of `cluster_strong` taken at the last
    `lexical.build` run for that verse -- nothing re-syncs it automatically when `cluster_strong`
    changes afterward (a curation fix, a reassignment) for a cluster still short of
    `ready_for_subgroup_allocation`. A member strong whose OWN live `verse_lexical` rows never
    carry `cluster_code` in `role`, despite `cluster_strong` currently listing it as a member, is
    exactly the failure mode found live: Layer 1 silently never presents that strong to the LLM at
    all, so a "complete" verse-reading pass can be complete against a stale, undercounted
    membership list without anyone noticing. A strong with ZERO live `verse_lexical` rows at all is
    a different, already-handled case (`unready_codes_in_scope`/`lexicalscope.
    strongs_with_no_occurrence`) -- not reported here, since there is nothing to be stale."""
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
# SIMPLIFIED 2026-09-16 (#1706 Phase B) -- resolved_sense/ambiguity_note are both dropped from
# Layer 1 entirely (researcher, verbatim, 2026-09-15: the multi-source meaning reading "should be
# part of layer 2... an observation linked to a question," not a Layer 1 column at all -- see the
# new `verse_meaning` stage, #1711). This function no longer touches `strong_meaning_parsed` or
# STEP live lookups at all -- it just confirms the strong is registered. `role` moved to
# `_layer1_fields` below (it's a code_classes-style lookup, same shape as is_negator/party_kind,
# not something that belongs in the per-strong_meaning_parsed resolution path).

def resolve_code(conn: sqlite3.Connection, code: str, morph_slice: str | None) -> dict:
    """One code's full verse_lexical row content (minus span_id/verse_id/code_ordinal, and minus
    the Layer-1-mechanical fields `_layer1_fields` adds afterward). `_language` is transient —
    carried only so `_layer1_fields`/`_narrative_morph_for` can gate on Hebrew-vs-Greek; never
    written to the DB (verse_lexical.language is dropped, #1706 Phase B item 8; the verse-grain
    equivalent is `verse_meta.language`, auto-computed by trigger, not by this module)."""
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


# ── Layer 1 mechanical fields (escalation #1383, build spec §B.5/§C.1) ────────────────────────
# position/surface/language/testament/is_negator/narrative_morph/gloss_consistent_in_verse/
# party_kind — computed unconditionally for every code, no selection (method-and-drift-
# mitigation doc §1-2, cfg_method_rule `mechanical-columns-run-on-every-code-no-selection`).

def load_code_classes(conn: sqlite3.Connection) -> dict[str, set[str]]:
    """EXACT strong_code -> set of live code-classes. Loaded once per build call (see
    build_for_range/build_for_verse_ids) and threaded through, same pattern as `live_cache` —
    this lookup is small (~40 rows) but every-code-every-verse re-querying it would still be
    wasteful at corpus scale. `lexical-code-class-lookup-not-hardcoded`: this IS the queried
    lookup that rule requires, never a hardcoded dict in this module.

    Sourced from `cluster_strong`, NOT `cfg_lexical_code_class` (architecture correction,
    researcher verdict 2026-09-05: "assigning a special status to a strong is to use a cluster
    for it... this is not cfg territory" — full record BUILD.md #228/#229).

    CORRECTED 2026-09-21 (escalation #1810, same defect class as `role` — BUILD.md #305/#1806):
    this used to base-strip `cluster_strong.strong` via `_base()` before keying the dict, on the
    reasoning "the old table was one-row-per-BASE-code, so base-keying needs no change to
    `_code_classes_for()`" — inertia from a data-source migration, not a considered decision that
    party/negator classification should be shared across sub-lettered siblings. Found live, same
    session as the `role` fix: 9,100 live `verse_lexical` rows had a `party_kind`/`is_negator`
    borrowed from an unrelated sibling's cluster_strong allocation (e.g. H4428G showed
    `party_kind='divine'` with zero live T7/divine-party allocation of its own — the tag belonged
    to a different H4428 suffix code entirely). Same root cause, same fix: keyed on the EXACT
    strong code now, never `_base()`. Unlike `role`, this one was never read by any live LLM
    generator (`versereadinggenerate.py`/`subgroupgenerate.py`/`charreadinggenerate.py`/
    `charanswergenerate.py` — checked, none reference `is_negator`/`party_kind`); its only live
    consumers were `report.lexical_exceptions` (a read-only diagnostic count) and the inactive
    `lexical.run`/`lexical.enrich` notes payload — so no downstream `ib_observation` re-examination
    question here, unlike `role`'s.

    `T5`/`T7`/`T8`/`T9`/`T4` here are `cluster.cluster_code` values (Negator/Party-Divine/
    Party-Human/Party-Angelic/Adversarial) — NOT this module's own unrelated "T1-T9" (the Verse
    Reading Technique steps named in this file's own docstring) or the observation-catalogue's
    T0-T7 tier scheme. Three different T-numbering schemes coexist project-wide; see the
    programme glossary's own T1 disambiguation entry. `T6` (Connective) is deliberately excluded
    — nothing in this module reads a connective classification (that lives in `verse_lexical_note`
    instead, a different mechanism entirely, `lexicalenrich.py`)."""
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


# `load_mcode_strongs` — DELETED 2026-09-16 (#1706 Phase B). Its sole purpose (gating
# `resolved_sense` to M-code strongs only, escalation #1527) went dead the moment #1575/#1527-cont.
# stopped writing resolved_sense from Layer 1 at all (2026-09-07); it had already been reduced to
# "loaded, threaded through, unused" by that point (see `build_for_verse`'s own prior comment) and
# resolved_sense's full removal from Layer 1 (this rebuild) removes its last reason to exist.
# `role` now needs the FULL cluster_strong set regardless of M/T-code (see `load_role_codes`
# above) — a different, wider lookup, not a revival of this one.


_PARTY_CLASS_TO_KIND = {"party_divine": "divine", "party_human": "human",
                        "party_angelic": "non_human", "party_adversarial": "non_human"}

_party_kind_parity_checked = False


def _assert_party_kind_parity(conn: sqlite3.Connection) -> None:
    """Live cfg_enum cross-check for _PARTY_CLASS_TO_KIND's own value set, added 2026-09-20
    (escalation #1796): party_kind was a registered cfg_enum group nothing ever looked up by name
    at runtime -- this hardcoded dict is the sole source of every party_kind ever written, with
    nothing confirming its 3 output values (divine/human/non_human) stay inside the registered
    enum. Cached after the first call (module-level flag, not re-queried per verse) -- build_for_verse
    runs once per verse in bulk builds, and this only needs to catch a genuine future edit drifting
    the two apart, not run thousands of times per call."""
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
    """Mutates `row` (a resolve_code() result) in place, adding the Layer-1 mechanical fields —
    everything except gloss_consistent_in_verse, which needs the whole verse's rows (computed
    separately, see _apply_gloss_consistency below). `language` is NOT stored (2026-09-16, #1706
    Phase B item 8 — dropped from verse_lexical, lives at verse_meta grain instead); still threaded
    through as a parameter because `_narrative_morph_for` needs the per-code Hebrew/Greek gate."""
    row["position"] = span["position"]
    row["surface"] = span["surface"]
    row["testament"] = testament
    code = row["strong"]
    row["role"] = _role_for(code, role_codes)
    classes = _code_classes_for(code, code_classes) if code else set()
    row["is_negator"] = 1 if "negator" in classes else None
    # Deterministic by RESULTING KIND, not by picking an arbitrary class out of an unordered set
    # (fixed 2026-09-21, escalation #1810 re-verification -- found live on H4317Q/Michael, which
    # deliberately carries BOTH party_human and party_angelic live at once per the researcher's own
    # 2026-09-09 instruction: "both stay live so Layer 2 checks which referent applies per
    # occurrence." The old `next((c for c in classes if c in _PARTY_CLASS_TO_KIND), None)` drew
    # from Python's unordered set iteration -- reproducible only by accident of a single process's
    # hash seed, not by anything in the data, contradicting this module's own "mechanically
    # resolved, never interpreted" principle. Two classes mapping to the SAME kind (e.g.
    # party_angelic + party_adversarial, both "non_human") are not a real conflict and still
    # resolve; two classes mapping to DIFFERENT kinds (human vs non_human, Michael's actual case)
    # is a genuine, then-unresolved conflict -- written as None, matching the researcher's own
    # stated design that Layer 2 (not Layer 1) is what disambiguates a specific occurrence, not
    # silently asserted as whichever kind happened to iterate first.
    party_kinds = {_PARTY_CLASS_TO_KIND[c] for c in classes if c in _PARTY_CLASS_TO_KIND}
    row["party_kind"] = next(iter(party_kinds)) if len(party_kinds) == 1 else None
    row["narrative_morph"] = _narrative_morph_for(row["morph_code"], language, sibling_codes)


def _apply_gloss_consistency(verse_rows: list[dict]) -> None:
    """Mutates every row in `verse_rows` in place — gloss_consistent_in_verse=0 iff this row's
    own (strong, morph_code) pair has >1 distinct SURFACE (the translation's own rendering, not
    resolved_sense) among this verse's own rows, else 1 (never NULL — per §D.1). Needs the WHOLE
    verse's resolved rows, not just one span's, hence a separate pass after every span in the
    verse has been resolved.

    Escalation #1527 (2026-09-06), researcher decision, previously made and confirmed here:
    keyed on `surface`, not `resolved_sense`. `resolved_sense` is a pure function of
    (strong, morph_code) with no per-occurrence signal at all (see #1527's own root-cause
    finding), so a same-code-different-sense check against it can never fire, for any corpus —
    it isn't a rare miss, it's structurally impossible. `surface` (the aligned translation word
    for this span) genuinely does vary by occurrence — confirmed live, Dan 1:8's own H0834A
    ('that' at one occurrence, 'allow' at the other) — so this is the field the check was always
    meant to be run against."""
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


# resolved_sense/ambiguity_note/language DROPPED 2026-09-16 (#1706 Phase B items 3-4/8) — see
# module banner. `role`'s CONTENT changed (cluster-code JSON array, not content/function) but it
# stays a plain identity-write column like every other field here — no special-casing needed.
_CONTENT_FIELDS = ("strong", "morph_code", "role", "status",
                  "position", "surface", "testament", "is_negator",
                  "narrative_morph", "gloss_consistent_in_verse", "party_kind")


def write_readings_for_span(conn: sqlite3.Connection, span_id: int, verse_id: int,
                            resolved: list[dict]) -> dict:
    """Identity-stable write, redesigned 2026-09-05 (escalation #1520 root-cause fix,
    `iba/docs/1520-verse-lexical-crud-safety-review-v1-20260905.md`) — replaces the old
    "soft-delete + insert a fresh row on every run, even for identical content" convention, which
    minted a new `verse_lexical.id` on every rebuild and silently orphaned any `verse_lexical_note`
    row that had come to depend on the old one. Matches this codebase's own already-correct
    precedent for a table WITH downstream FK dependents (`handlers/operations.py:phenomenon_set`,
    in-place UPDATE, not supersede) rather than the pattern that's only safe for a leaf table with
    none (`verse`/`span`/`strong`'s own convention, which `verse_lexical` used to copy blindly).

    Per code_ordinal within this span:
      - no live row yet             -> INSERT (genuinely new — a fresh id is correct here).
      - live row, content identical -> untouched. No write at all: same id, same created_at,
        same `verse_lexical_note` attachments. This is the common case (most rebuilds re-confirm
        already-correct data) and it is what actually eliminates the orphan risk, not a workaround
        bolted on beside it.
      - live row, content differs   -> real `UPDATE ... WHERE id=?`. Same id preserved forever;
        `updated_at` set to record when the correction was confirmed (replaces the old
        "created_at reflects the last run" signal without requiring the id to churn to get it).
      - a code_ordinal that WAS live before this call but has no resolved code now (the span
        genuinely shrank) -> soft-deleted for real. This is the one case where the row's id
        legitimately goes away, so any `verse_lexical_note` still pointing at it is now genuinely
        stale, not a rebuild artefact — counted and returned as `removed_with_live_notes` rather
        than silently left to dangle; the caller surfaces a nonzero count, never swallows it.

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
    """Internal to this module — only ever called from `build_for_range`/`build_for_verse_ids`
    below (checked live 2026-09-16, no external caller), which is why the readiness pre-check
    (`unready_codes_in_scope`) lives at THEIR entry points, not here: this function has no
    standalone `verse_ids` scope of its own to check against."""
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
    """Raised by `build_for_range`/`build_for_verse_ids` when `unready_codes_in_scope` finds any
    code in the requested scope with zero cluster_strong allocation (#1606 D1) — the run does not
    proceed, per the researcher's own ruling, 2026-09-09/10. `.codes` carries the exact list."""
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
    """Same shape as `build_for_range`, but scoped to an explicit verse_id list rather than a
    book/chapter range — for a per-WORD rebuild (2026-08-10, `raw.lexical`, the `new-word` chain's
    closing step: "checking that the lexicals for the verses are correct with the parse values").
    `build_for_verse` is identity-stable (`write_readings_for_span`, redesigned 2026-09-05,
    escalation #1520): re-running this for a verse whose parse values haven't changed is a true
    no-op (`unchanged`, same ids, nothing written); a verse whose span content HAS changed gets its
    `verse_lexical` rows corrected in place (`updated`, same ids) — either way, any
    `verse_lexical_note` already attached survives untouched. Dedups the input (a word's strongs
    can share a verse many times over)."""
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
