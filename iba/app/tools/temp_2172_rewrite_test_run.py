"""TEMPORARY (#2172 test plan, iba/docs/2172-strand-reading-test-plan-v1-20261022.md). Run:
    python iba/app/tools/temp_2172_rewrite_test_run.py <scratch folder>
against a dbsnapshot copy of iba.db in the scratch folder; live iba.db and live files are never written.
#2172 build: narrativeregister.rewrite on the t2 copy (run after test_register.py)."""
import pathlib
import sys

ROOT = pathlib.Path(r"C:\Bible_study_projects")
sys.path.insert(0, str(ROOT))
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib import narrativeregister as nr  # noqa: E402
from iba.app.lib import quotecheck  # noqa: E402

S = pathlib.Path(sys.argv[1]) / "t2"
cfg = Cfg(S / "iba.db")
conn = cfg.conn
results = []
n = [0]


def W():
    return nr.Writer(conn, "migration", "test")


def count(sql, *a):
    return conn.execute(sql, a).fetchone()[0]


def data(blocks, title=None):
    n[0] += 1
    return {"update": {"update_date": "2026-10-22", "title": title or f"test rewrite {n[0]}"},
            "refs": [{"kind": "escalation", "value": "2172"}], "blocks": blocks}


def case(name, fn, expect_refused=None, check=None):
    before = (count("SELECT COUNT(*) FROM narrative_update"), count("SELECT COUNT(*) FROM narrative_claim_change"))
    try:
        out = fn()
        ok = expect_refused is None and (check is None or check(out))
        detail = str(out)[:300]
    except nr.Refused as exc:
        after = (count("SELECT COUNT(*) FROM narrative_update"), count("SELECT COUNT(*) FROM narrative_claim_change"))
        ok = expect_refused is not None and expect_refused in str(exc) and after == before
        detail = f"Refused{' (nothing written)' if after == before else ' BUT ROWS WRITTEN'}: {str(exc)[:260]}"
    results.append((name, "PASS" if ok else "FAIL", detail))


# a block that tells at least two claims and whose quotations all pass the check
corpus = quotecheck.Corpus(conn)
mw = int(cfg.required_setting("narrative.quote_min_words"))
skip = quotecheck.titles(conn)
target = None
for r in conn.execute("SELECT s.*, ch.chapter_no, COUNT(*) n FROM narrative_claim_telling t JOIN narrative_section s ON "
                      "s.id=t.section_id JOIN narrative_chapter ch ON ch.id=s.chapter_id WHERE t.status='current' AND "
                      "s.level >= 2 AND s.last_version IS NULL GROUP BY s.id HAVING n >= 2 ORDER BY s.id"):
    if not quotecheck.check_lines(corpus, r["block_text"].split("\n"), mw, skip)[1] and count(
            "SELECT COUNT(*) FROM narrative_section WHERE chapter_id=? AND heading=? AND last_version IS NULL",
            r["chapter_id"], r["heading"]) == 1:
        target = r
        break
assert target, "no clean target block"
ch = conn.execute("SELECT * FROM narrative_chapter WHERE id=?", (target["chapter_id"],)).fetchone()
told = conn.execute("SELECT c.claim_ref, t.kind, t.part_told FROM narrative_claim_telling t JOIN narrative_claim c ON "
                    "c.id=t.claim_id WHERE t.section_id=? AND t.status='current' ORDER BY c.id", (target["id"],)).fetchall()
# a part left unrecorded in the register (an existing gap) is filled here, as a rewrite must
tells = [{"claim": t["claim_ref"], "kind": t["kind"],
          "part": t["part_told"] or ("test part" if t["kind"] == "in part" else None)} for t in told]
CH, SEC = ch["chapter_no"], target["heading"]
text0 = target["block_text"]
print(f"target: Ch {CH} *{SEC}* (block {target['id']}), {len(told)} claims, file {ch['current_file']}")

# R1 a clean rewrite: the same claims, the text changed, a reference added
new_text = text0.rstrip("\n") + "\n\nThe same is said of the inner person in Rom 7:22.\n"
old_file = ch["current_file"]
case("R1 rewrite keeping its claims", lambda: nr.rewrite(cfg, W(), data([{"chapter": CH, "section": SEC, "text": new_text,
     "tells": tells}]), "test"), check=lambda o: CH in o["chapters"])
ch1 = conn.execute("SELECT * FROM narrative_chapter WHERE id=?", (ch["id"],)).fetchone()
chap = nr.chapter_dir(cfg)
results.append(("R1 chapter published v+1, old file archived",
                "PASS" if ch1["current_version"] == (ch["current_version"] or 0) + 1 and (chap / ch1["current_file"]).is_file()
                and (chap / "archive" / old_file).is_file() and not (chap / old_file).exists() else "FAIL",
                f"{old_file} -> {ch1['current_file']}"))
results.append(("R1 file reads as the database renders it",
                "PASS" if (chap / ch1["current_file"]).read_text(encoding="utf-8") == nr.render_chapter(conn, ch["id"]) else "FAIL", ""))
results.append(("R1 one 'telling changed' row per claim, with before and after",
                "PASS" if count("SELECT COUNT(*) FROM narrative_claim_change WHERE section_id=? AND change_kind='telling changed' "
                                "AND passage_before=? AND passage_after=?", target["id"], text0, new_text) == len(told) else "FAIL",
                f"{len(told)} claims"))
results.append(("R1 citation added for Rom 7:22", "PASS" if count(
    "SELECT COUNT(*) FROM narrative_citation WHERE section_id=? AND ref_normalised='Rom 7:22' AND last_version IS NULL",
    target["id"]) == 1 else "FAIL", ""))
lines, _ = nr.check(cfg, {})
results.append(("R1 check: no file/database difference", "PASS" if not any("differs from the database" in x for x in lines)
                else "FAIL", ""))

# R2 safeguard 3: a claim dropped without an account
case("R2 claim dropped, not accounted -> refused", lambda: nr.rewrite(cfg, W(), data([{"chapter": CH, "section": SEC,
     "text": new_text, "tells": tells[1:]}]), "test"), "not accounted for")
# R3 'withdrawn' for a claim that is not withdrawn
case("R3 accounted withdrawn, claim not withdrawn -> refused", lambda: nr.rewrite(cfg, W(), data([{"chapter": CH,
     "section": SEC, "text": new_text, "tells": tells[1:], "accounts": [{"claim": tells[0]["claim"], "as": "withdrawn"}]}]),
     "test"), "is not withdrawn")
# R4 'moved' to a block that does not tell it
case("R4 accounted moved, target does not tell it -> refused", lambda: nr.rewrite(cfg, W(), data([{"chapter": CH,
     "section": SEC, "text": new_text, "tells": tells[1:], "accounts": [{"claim": tells[0]["claim"], "as": "moved",
     "to": {"chapter": "10.1", "section": "Losing heart"}}]}]), "test"), "does not tell it")
# R5 'moved' to a block rewritten in the same JSON that tells it
lh = nr._block(conn, nr._chapter(conn, "10.1"), "Losing heart")
lh_tells = [{"claim": r[0], "kind": r[1], "part": r[2] or ("test part" if r[1] == "in part" else None)} for r in conn.execute(
    "SELECT c.claim_ref, t.kind, t.part_told FROM narrative_claim_telling t JOIN narrative_claim c ON c.id=t.claim_id "
    "WHERE t.section_id=? AND t.status='current'", (lh["id"],))]
lh_ok = not quotecheck.check_lines(corpus, lh["block_text"].split("\n"), mw, skip)[1]
if lh_ok:
    case("R5 accounted moved, and told there in the same rewrite", lambda: nr.rewrite(cfg, W(), data([
        {"chapter": CH, "section": SEC, "text": new_text, "tells": tells[1:],
         "accounts": [{"claim": tells[0]["claim"], "as": "moved", "to": {"chapter": "10.1", "section": "Losing heart"}}]},
        {"chapter": "10.1", "section": "Losing heart", "text": lh["block_text"],
         "tells": lh_tells + [{"claim": tells[0]["claim"], "kind": "in full"}]}]), "test"),
        check=lambda o: len(o["chapters"]) == 2)
else:
    results.append(("R5 accounted moved", "SKIP", "Losing heart has a failing quotation"))
# R6 a quotation not in the ESV text
case("R6 quotation not in the text -> refused", lambda: nr.rewrite(cfg, W(), data([{"chapter": CH, "section": SEC,
     "text": new_text + '\nAs it is written, "the heart is a lantern of brass and wool".\n', "tells": tells}]), "test"),
     "not found in the ESV text")
# R7 heading line wrong; R8 a second heading inside a block
case("R7 block not opening with its heading -> refused", lambda: nr.rewrite(cfg, W(), data([{"chapter": CH,
     "section": SEC, "text": "## Another heading\n\nText.", "tells": tells}]), "test"), "must open with its heading line")
case("R8 another heading inside the block -> refused", lambda: nr.rewrite(cfg, W(), data([{"chapter": CH,
     "section": SEC, "text": new_text + "\n### Inside\n\nMore.", "tells": tells}]), "test"), "holds another heading")
# R9 the same update twice
case("R9 same update title twice -> refused", lambda: nr.rewrite(cfg, W(), data([{"chapter": CH, "section": SEC,
     "text": new_text, "tells": tells}], title="test rewrite 1"), "test"), "already recorded")
# R10 a new block, then retired with its claim moved back
cur = nr._block(conn, nr._chapter(conn, CH), SEC)
lvl = cur["level"]
claim0 = tells[1]["claim"]
case("R10 new block after the target, telling a claim", lambda: nr.rewrite(cfg, W(), data([{"chapter": CH,
     "new": {"heading": "A test block", "level": lvl, "after": SEC}, "text": f"{'#' * lvl} A test block\n\nA new block.\n",
     "tells": [{"claim": claim0, "kind": "pointer"}]}]), "test"))
nb = conn.execute("SELECT * FROM narrative_section WHERE chapter_id=? AND heading='A test block' AND last_version IS NULL",
                  (ch["id"],)).fetchone()
rendered = nr.render_chapter(conn, ch["id"])
results.append(("R10 new block placed after the target and its sub-blocks", "PASS" if nb and
                rendered.index(f"{'#' * lvl} A test block") > rendered.index(f"{'#' * lvl} {SEC}") else "FAIL",
                f"ordinal {nb['ordinal'] if nb else '-'}"))
case("R11 retire a block whose claim is not accounted -> refused", lambda: nr.rewrite(cfg, W(), data([{"chapter": CH,
     "section": "A test block", "retire": True}]), "test"), "not accounted for")
case("R12 retire a block, its claim kept elsewhere", lambda: nr.rewrite(cfg, W(), data([{"chapter": CH,
     "section": "A test block", "retire": True, "accounts": [{"claim": claim0, "as": "moved",
     "to": {"chapter": CH, "section": SEC}}]}]), "test"))
results.append(("R12 retired block out of the narrative, no current telling", "PASS" if count(
    "SELECT COUNT(*) FROM narrative_section WHERE id=? AND last_version IS NOT NULL", nb["id"]) == 1 and count(
    "SELECT COUNT(*) FROM narrative_claim_telling WHERE section_id=? AND status='current'", nb["id"]) == 0 else "FAIL", ""))
lines, _ = nr.check(cfg, {})
results.append(("final check: files match the database, no dead or double tellings",
                "PASS" if not any(k in x for x in lines for k in ("differs from the database", "one per block",
                                                                   "no longer in the narrative", "heading line",
                                                                   "newer file")) else "FAIL",
                "; ".join(x for x in lines if "differs" in x or "per block" in x or "no longer" in x)[:300]))

for r in results:
    print(" | ".join(r))
print(f"\n{sum(r[1] == 'PASS' for r in results)} of {len(results)} pass")
