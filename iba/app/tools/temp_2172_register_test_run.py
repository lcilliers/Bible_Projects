"""TEMPORARY (#2172 test plan, iba/docs/2172-strand-reading-test-plan-v1-20261022.md). Run:
    python iba/app/tools/temp_2172_register_test_run.py <scratch folder>
against a dbsnapshot copy of iba.db in the scratch folder; live iba.db and live files are never written.
#2172 build step 1 test: migration 1 + the register on blocks, on a dbsnapshot copy.
Every file the register writes goes to the scratch folder (the copy's settings point there)."""
import json
import pathlib
import shutil
import sqlite3
import subprocess
import sys

ROOT = pathlib.Path(r"C:\Bible_study_projects")
sys.path.insert(0, str(ROOT))
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib import narrativeregister as nr  # noqa: E402

S = pathlib.Path(sys.argv[1]) / "t2"
if S.exists():
    shutil.rmtree(S)
S.mkdir()
DB = copy_db(S / "iba.db")
print("copy of the live database (migrations already applied)")

live = sqlite3.connect(ROOT / "iba/app/db/iba.db")
src_dir = ROOT / json.loads(live.execute("SELECT value FROM cfg_setting WHERE key='narrative.copy_source_dir'").fetchone()[0])
chap = S / "chapters"
chap.mkdir()
for (f,) in live.execute("SELECT current_file FROM narrative_chapter WHERE inactive=0 AND current_file IS NOT NULL"):
    shutil.copy2(src_dir / f, chap / f)
c = sqlite3.connect(DB)
for key, val in (("narrative.copy_source_dir", str(chap)),
                 ("narrative.claim_register_path", str(S / "out/register.md")),
                 ("narrative.claim_changes_path", str(S / "out/changes.md")),
                 ("narrative.citation_index_path", str(S / "out/citations.md"))):
    c.execute("UPDATE cfg_setting SET value=? WHERE key=?", (json.dumps(val), key))
c.commit()
c.close()

cfg = Cfg(DB)
conn = cfg.conn
results = []


def case(name, fn, expect_refused=None):
    """expect_refused: a substring the refusal must carry; None = must succeed."""
    try:
        out = fn()
        ok = expect_refused is None
        detail = str(out)[:300]
    except nr.Refused as exc:
        ok = expect_refused is not None and expect_refused in str(exc)
        detail = f"Refused: {str(exc)[:300]}"
    results.append((name, "PASS" if ok else "FAIL", detail))


def W():
    return nr.Writer(conn, "migration", "test")


def count(sql, *a):
    return conn.execute(sql, a).fetchone()[0]


# 1. check on the migrated copy: every chapter renders as its file; no duplicate or dead tellings
lines, console = nr.check(cfg, {})
real = [x for x in lines if x.startswith("- ")]
results.append(("check after migration", "PASS" if not any(("differs from the database" in x or "one per block" in x
                or "no longer in the narrative" in x or "heading line" in x) for x in real) else "FAIL",
                f"{len(real)} finding(s); first: {real[:3]}"))

# 2. block lookup
ch = nr._chapter(conn, "10.1")
case("block: ambiguous heading refused", lambda: nr._block(conn, ch, "The words"), "Parent > Heading")
case("block: Parent > Heading found", lambda: nr._block(conn, ch, "Anxiety > The words")["id"])
case("block: unknown heading refused", lambda: nr._block(conn, ch, "No such heading"), "no current block")

# 3. tell / untell on a block
claim = conn.execute("SELECT c.* FROM narrative_claim c WHERE c.status='current' AND NOT EXISTS (SELECT 1 FROM "
                     "narrative_claim_telling t WHERE t.claim_id=c.id AND t.section_id=101 AND t.status='current') "
                     "ORDER BY c.id LIMIT 1").fetchone()
ref = claim["claim_ref"]
n0 = count("SELECT COUNT(*) FROM narrative_claim_change")
case("tell: block", lambda: nr.tell(cfg, W(), {"Claim": ref, "Chapter": "10.1", "Section": "Where it turns"}))
results.append(("tell: change row with the block", "PASS" if count(
    "SELECT COUNT(*) FROM narrative_claim_change WHERE id > (SELECT MAX(id) FROM narrative_claim_change) - 1 AND "
    "change_kind='telling added' AND section_id=101 AND passage_after IS NOT NULL AND basis='recorded'") == 1 else "FAIL",
    f"rows written {count('SELECT COUNT(*) FROM narrative_claim_change') - n0}"))
results.append(("tell: in_narrative 1", "PASS" if count("SELECT in_narrative FROM narrative_claim WHERE id=?", claim["id"]) == 1 else "FAIL", ""))
case("tell: twice refused", lambda: nr.tell(cfg, W(), {"Claim": ref, "Chapter": "10.1", "Section": "Where it turns"}),
     "already told")
case("tell: in part without part refused", lambda: nr.tell(cfg, W(), {"Claim": ref, "Chapter": "10.1",
     "Section": "Fear", "Kind": "in part"}), "-Part is required")
case("untell: block", lambda: nr.untell(cfg, W(), {"Claim": ref, "Chapter": "10.1", "Section": "Where it turns"}))
case("untell: not told refused", lambda: nr.untell(cfg, W(), {"Claim": ref, "Chapter": "10.1",
     "Section": "Where it turns"}), "is not told")

# 4. rename a block: its tellings and heading line follow; not logged as a move
told = conn.execute("SELECT section_id, COUNT(*) n FROM narrative_claim_telling WHERE status='current' "
                    "GROUP BY section_id ORDER BY n DESC LIMIT 1").fetchone()
sec = conn.execute("SELECT s.*, ch.chapter_no FROM narrative_section s JOIN narrative_chapter ch ON ch.id=s.chapter_id "
                   "WHERE s.id=?", (told["section_id"],)).fetchone()
mv0 = count("SELECT COUNT(*) FROM narrative_claim_change WHERE change_kind='passage moved'")
if sec["level"] and count("SELECT COUNT(*) FROM narrative_section WHERE chapter_id=? AND heading=? AND "
                          "last_version IS NULL", sec["chapter_id"], sec["heading"]) == 1:
    case("edit_section: rename", lambda: nr.edit_section(cfg, nr.Writer(conn, "narrative_register.edit_section", "test"),
         {"Chapter": sec["chapter_no"], "Section": sec["heading"], "NewHeading": sec["heading"] + " (renamed)"}))
    new = conn.execute("SELECT * FROM narrative_section WHERE renamed_from_id=? AND last_version IS NULL",
                       (sec["id"],)).fetchone()
    results.append(("rename: tellings follow", "PASS" if new and count(
        "SELECT COUNT(*) FROM narrative_claim_telling WHERE section_id=? AND status='current'", new["id"]) == told["n"]
        else "FAIL", f"{told['n']} telling(s)"))
    results.append(("rename: heading line follows", "PASS" if new and new["block_text"].split("\n")[0] ==
                    "#" * new["level"] + " " + new["heading"] else "FAIL", new["block_text"].split("\n")[0] if new else "-"))
    results.append(("rename: not logged as a move", "PASS" if count(
        "SELECT COUNT(*) FROM narrative_claim_change WHERE change_kind='passage moved'") == mv0 else "FAIL", ""))
    results.append(("rename: claims stay in the narrative", "PASS" if count(
        "SELECT COUNT(*) FROM narrative_claim_telling t JOIN narrative_claim c ON c.id=t.claim_id WHERE t.section_id=? "
        "AND c.in_narrative=0", new["id"]) == 0 else "FAIL", ""))
    chx = conn.execute("SELECT * FROM narrative_chapter WHERE id=?", (sec["chapter_id"],)).fetchone()
    results.append(("rename: chapter published from the database", "PASS" if
                    (nr.chapter_dir(cfg) / chx["current_file"]).read_text(encoding="utf-8") ==
                    nr.render_chapter(conn, chx["id"]) else "FAIL", chx["current_file"]))
case("edit_section: add a block (published)", lambda: nr.edit_section(cfg, nr.Writer(conn, "narrative_register.edit_section",
     "test"), {"Chapter": "10.1", "Section": "A closing test block", "Level": "2"}))
case("edit_section: unknown block without -Level refused", lambda: nr.edit_section(cfg, nr.Writer(
     conn, "narrative_register.edit_section", "test"), {"Chapter": "10.1", "Section": "Nowhere", "NewHeading": "X"}),
     "no current block")

# 5. read-only actions on the new tellings
case("find: chapter and section", lambda: nr.find(cfg, {"Chapter": "10.1", "Section": "Fear"})[1][0])
case("find: told in more than one", lambda: nr.find(cfg, {"ToldInMoreThanOne": "1"})[1][0])
case("history", lambda: nr.history(cfg, {"Claim": ref})[1][0])
case("export", lambda: [p.name for p in nr.export(cfg)])

for r in results:
    print(" | ".join(r))
print(f"\n{sum(r[1] == 'PASS' for r in results)} of {len(results)} pass")
