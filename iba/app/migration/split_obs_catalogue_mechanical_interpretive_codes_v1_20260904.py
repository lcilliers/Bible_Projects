"""split_obs_catalogue_mechanical_interpretive_codes_v1_20260904.py — ONE-OFF, idempotent.
Escalation #1444 v9 (resolution) / #1383 (field-mapping + finishing-doc + catalogue-scope-and-
wording-update docs). Researcher instruction (verbatim, this chat turn, Developer Mode session):
"you will now complete the outstanding build work in escalation 1383 and 1444" — this migration is
#1444's own named outstanding item: "Full spec for the 5 remaining splits (T0.1.2/T4.6.2/T4.6.3/
T7.2.2/T1.4.1 a/b pairs, wording+scope for each) written and ready to build once Developer Mode is
entered — obs_catalogue.update has no INSERT path, new question_codes need a migration."

Full spec: iba/docs/1444-catalogue-scope-and-wording-update-v1-20260904.md §6. Content-only change
(no DDL) to `wa_obs_question_catalogue` (bible_research.db, ordinary content table, not `cfg_*` —
same "not a configmaint.propose matter" reasoning cataloguewrite.py's own header already states)
— run directly here rather than through `obs_catalogue.update` (UPDATE-by-obs_id only, no INSERT)
per that doc's own stated build-mechanics gap.

Each of the 5 bundled questions conflates a Window-1-mechanical fact with a Window-2-interpretive
judgement (same bundling pattern #1383's finishing doc caught 4 times already, this doc's §3b found
a 5th and 6th). Split mechanics (the doc's own §6 "open build-mechanics question," resolved here,
not improvised mid-build): soft-delete (deleted=1) the old unified code, insert two new child rows
— the same soft-delete pattern already used earlier this session for the 55-row catalogue_version
cleanup (escalation #1444 v9's own applied resolution), not a new parent/rollup column this table
has no precedent or schema for. Sibling rows in the same `component_code` that sat after the split
row are renumbered by +1 in `prompt_seq` so display order stays contiguous (T7.2.3-6, T1.4.2-3) —
mechanical renumbering, not a content change.

T4.6.3a/b wording: the source doc named the split shape but left the exact text "to be drafted at
build time" (T4.6.2's own already-specified split is the template). Drafted here, same shape as
T4.6.2: mechanical half asks whether an angelic-being code appears as an acting party; interpretive
half asks what that pattern shows about the characteristic's relation to angelic ministry (mirrors
the original T4.6.3 question_text this row replaces).

`review_note` set on every new row recording its provenance (old code + escalation), since this
table carries no separate history/audit table (researcher ruling, escalation #1007, restated in
cataloguewrite.py's own header) — the one place this migration's own trace survives on the row
itself.

    python -m iba.app.migration.split_obs_catalogue_mechanical_interpretive_codes_v1_20260904
"""

from __future__ import annotations

import datetime
import json
import sqlite3
import sys

from ..lib.cfg import DB_PATH

_TABLE = "wa_obs_question_catalogue"
_CATALOGUE_VERSION = "v2-2026-09-04"
_PROVENANCE = ("Split from {old} (obs_id {obs_id}) per escalation #1444 v9 / #1383 field-mapping "
               "+ catalogue-scope-and-wording-update docs, 2026-09-04 (Developer Mode build).")

# (old_question_code, [ (new_code, question_text, scope, prompt_seq) x2 ])
_SPLITS = [
    ("T0.1.2", [
        ("T0.1.2a",
         "Across the characteristic's verses, is the characteristic ever predicated of God "
         "himself (not just present in a verse where God is also mentioned)?",
         "Word/term (lexical)", 2),
        ("T0.1.2b",
         "What does the pattern of presence/absence found in T0.1.2a indicate for the "
         "characteristic's place in the human person and in the divine image?",
         "Other non-human beings", 3),
    ]),
    ("T4.6.2", [
        ("T4.6.2a",
         "Does an adversarial-being code ever appear as an acting party in a verse carrying "
         "this characteristic?",
         "Word/term (lexical)", 2),
        ("T4.6.2b",
         "What does that pattern show about the characteristic being a site of adversarial "
         "activity?",
         "Other non-human beings", 3),
    ]),
    ("T4.6.3", [
        ("T4.6.3a",
         "Does an angelic-being code ever appear as an acting party in a verse carrying this "
         "characteristic?",
         "Word/term (lexical)", 4),
        ("T4.6.3b",
         "What does that pattern show about the characteristic being communicated, "
         "strengthened, or mediated through angelic ministry?",
         "Other non-human beings", 5),
    ]),
    ("T7.2.2", [
        ("T7.2.2a",
         "What literary form carries the primary verse evidence (narrative, psalm, wisdom, "
         "prophecy, epistle, apocalyptic)?",
         "Word/term (lexical)", 2),
        ("T7.2.2b",
         "What does that literary form require for responsible interpretation?",
         "The verse", 3),
    ]),
    ("T1.4.1", [
        ("T1.4.1a",
         "What is the grammatical/stem form of the characteristic's primary term in this verse?",
         "Word/term (lexical)", 1),
        ("T1.4.1b",
         "In what distinct mode(s) does the characteristic operate within the inner person in "
         "this verse — the manner of its functioning?",
         "Verse-context", 2),
    ]),
]

# Sibling rows (same component_code, unaffected question_code) whose prompt_seq shifts by +1
# because a split inserted a second row ahead of them. (component_code, question_code, new_seq).
_SIBLING_RENUMBER = [
    ("T7.2", "T7.2.3", 4),
    ("T7.2", "T7.2.4", 5),
    ("T7.2", "T7.2.5", 6),
    ("T7.2", "T7.2.6", 7),
    ("T1.4", "T1.4.2", 3),
    ("T1.4", "T1.4.3", 4),
]

_SELF_PATH = ("iba/app/migration/"
              "split_obs_catalogue_mechanical_interpretive_codes_v1_20260904.py")


def _now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _research_db_path(iba_conn: sqlite3.Connection) -> str:
    """Same resolution `Cfg.database_path('bible_research')` performs at runtime — done here with
    raw SQL because a standalone migration script has no live `Cfg` instance (same pattern as
    add_obs_catalogue_source_last_modified_and_update_tool_v1_20260831.py)."""
    row = iba_conn.execute(
        "SELECT value FROM cfg_setting WHERE key='database.bible_research.path'").fetchone()
    if not row:
        raise RuntimeError("no database.bible_research.path setting -- run Start-Iba.ps1 first")
    rel = json.loads(row[0])
    repo_root = DB_PATH.resolve().parent.parent.parent.parent
    return str(repo_root / rel)


def main() -> int:
    iba_conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    research_path = _research_db_path(iba_conn)
    rconn = sqlite3.connect(research_path)
    rconn.row_factory = sqlite3.Row
    try:
        now = _now_iso()
        for old_code, children in _SPLITS:
            old = rconn.execute(
                f'SELECT * FROM "{_TABLE}" WHERE question_code=? AND deleted=0',
                (old_code,)).fetchone()
            if old is None:
                # Already split (idempotent re-run) if children already present and active.
                existing_children = rconn.execute(
                    f'SELECT question_code FROM "{_TABLE}" WHERE question_code IN (?,?) '
                    f'AND deleted=0', tuple(c[0] for c in children)).fetchall()
                if len(existing_children) == 2:
                    report.append(f"{old_code} already split — skipped")
                    continue
                raise RuntimeError(
                    f"{old_code} not found active and children not both present — "
                    "inconsistent state, needs manual review")
            old = dict(old)

            # Soft-delete the old unified row (preserve its own catalogue_version, per the
            # 55-row cleanup precedent earlier this session).
            rconn.execute(
                f'UPDATE "{_TABLE}" SET deleted=1, last_modified=? WHERE obs_id=?',
                (now, old["obs_id"]))
            report.append(f"{old_code} (obs_id {old['obs_id']}) soft-deleted (deleted=1)")

            for new_code, text, scope, seq in children:
                exists = rconn.execute(
                    f'SELECT 1 FROM "{_TABLE}" WHERE question_code=? AND deleted=0',
                    (new_code,)).fetchone()
                if exists:
                    report.append(f"{new_code} already present — skipped insert")
                    continue
                rconn.execute(
                    f'INSERT INTO "{_TABLE}" '
                    '(question_code, section, source_word, source_registry_no, question_text, '
                    'pattern_type, scope, status, deleted, date_added, catalogue_version, '
                    'review_note, tier, component_code, component_title, prompt_seq, source, '
                    'last_modified) '
                    'VALUES (?,?,?,?,?,?,?,\'active\',0,?,?,?,?,?,?,?,?,?)',
                    (new_code, old["section"], old["source_word"], old["source_registry_no"],
                     text, old["pattern_type"], scope, now, _CATALOGUE_VERSION,
                     _PROVENANCE.format(old=old_code, obs_id=old["obs_id"]),
                     old["tier"], old["component_code"], old["component_title"], seq,
                     old["source"], now))
                report.append(f"{new_code} inserted (scope={scope!r}, prompt_seq={seq})")

        for component_code, question_code, new_seq in _SIBLING_RENUMBER:
            row = rconn.execute(
                f'SELECT obs_id, prompt_seq FROM "{_TABLE}" WHERE component_code=? '
                f'AND question_code=? AND deleted=0', (component_code, question_code)).fetchone()
            if row is None:
                report.append(f"sibling {question_code} not found active — skipped renumber")
                continue
            if row["prompt_seq"] == new_seq:
                report.append(f"sibling {question_code} prompt_seq already {new_seq} — skipped")
                continue
            rconn.execute(
                f'UPDATE "{_TABLE}" SET prompt_seq=?, last_modified=? WHERE obs_id=?',
                (new_seq, now, row["obs_id"]))
            report.append(f"sibling {question_code} prompt_seq -> {new_seq}")

        rconn.commit()
    finally:
        rconn.close()

    # Self-register in cfg_utility, inactive=1 once applied — same one-off-migration pattern
    # every other script in this directory follows.
    if not iba_conn.execute("SELECT 1 FROM cfg_utility WHERE file_path=?", (_SELF_PATH,)).fetchone():
        iba_conn.execute(
            "INSERT INTO cfg_utility (module, file_path, purpose, inactive, config_exempt) "
            "VALUES (?,?,?,1,0)",
            ("split_obs_catalogue_mechanical_interpretive_codes_v1_20260904", _SELF_PATH,
             "ONE-OFF migration, escalation #1444/#1383 -- splits 5 bundled wa_obs_question_"
             "catalogue codes (T0.1.2, T4.6.2, T4.6.3, T7.2.2, T1.4.1) each into a mechanical "
             "(Word/term lexical) + interpretive child pair, soft-deleting the old unified code. "
             "inactive=1 once applied -- a one-off, not a reusable routine."))
        report.append(f"cfg_utility (self) {_SELF_PATH!r} added")
    else:
        report.append(f"cfg_utility (self) {_SELF_PATH!r} already present")

    iba_conn.commit()
    iba_conn.close()

    print("obs_catalogue mechanical/interpretive code split:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
