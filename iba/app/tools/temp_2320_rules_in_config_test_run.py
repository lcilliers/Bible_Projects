"""temp_2320_rules_in_config_test_run.py -- test plan for governance.rules_must_be_config_driven (escalation #2320, researcher 2026-10-28:
"rules are configs, not hard recorded in the code"). On a COPY of the live iba.db: every rule of Analysis_phase_1 that Record, the
build of verse_lexical and the filing enforce is a cfg_setting row (reading.observation_rules, lexical.span_surface,
report.cluster_folder_name_rule), and changing the row changes the behaviour, which a rule hard-coded in the code could not do. Each case
runs the behaviour with the shipped row and again with the row changed. Usage:
python iba/app/tools/temp_2320_rules_in_config_test_run.py <scratch dir>. Prints PASS/FAIL per case."""
import json
import os
import subprocess
import pathlib
import shutil
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib import observationrecord as orec  # noqa: E402
from iba.app.lib import reading as rd  # noqa: E402
from iba.app.lib import lexical, filingkit  # noqa: E402

S = pathlib.Path(sys.argv[1]) / "t2320cfgrun"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db", ROOT / "iba/app/db/iba.db")
_mig = ROOT / "iba/app/migration/analysis_phase_1_2329_v3_20261030.py"          # the nine observation items (#2329), when the copy lacks them
_mig = _mig if _mig.exists() else ROOT / "iba/app/migration/archive" / _mig.name
subprocess.run([sys.executable, str(_mig), "--db", str(DB)], capture_output=True, text=True,
               env={**os.environ, "PYTHONPATH": str(ROOT), "PYTHONUTF8": "1"})
cfg = Cfg(DB)
conn = cfg.conn
res = []


def case(cid, desc, ok, ev=""):
    ok = bool(ok)
    res.append(ok)
    print(f"{cid} {'PASS' if ok else 'FAIL'} {desc}" + ("" if ok else f"  -- {str(ev)[:700]}"), flush=True)


def setting(key):
    return json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key=?", (key,)).fetchone()[0])


def put(key, value):
    conn.execute("UPDATE cfg_setting SET value=? WHERE key=?", (json.dumps(value), key))
    conn.commit()


def with_rule(key, change):
    """Run `change(value)` on a copy of the setting, write it, return a function that restores the shipped row."""
    old = setting(key)
    new = json.loads(json.dumps(old))
    change(new)
    put(key, new)
    return lambda: put(key, old)


FULL = {"item": "circumstance"}


def sheet(kind="statement", parts=None, nodes=None, tag=None):
    node = {"node": 1, "word": "w (H1)", "role": "characteristic", "occurrence": 1, "counts_for": None, "cluster": "T1", "subgroup": None,
            "reading_id": None, "suggest": None, "flags": [], "action": None}
    e = {"observation": 99999, "stage": "x", "kind": tag or kind, "text": "t", "flags": [], "meaning": None, "implication": None, "basis": "stated",
         "route": None, "parts": parts, "nodes_on_other_verses": 0, "nodes": nodes if nodes is not None else [node],
         "action": {"action": "accept"}}
    return {"verse": "Gen 1:1", "sheet": {"surfaces": [], "existing": [e], "findings": [], "ledger_faces": []}}


def errors_of(v):
    errs = []
    rd._validate_sheet(cfg, conn, v, errs)
    return errs


# ── S: the settings exist, and the code fails loudly when one is missing ───────────────────────────
for key in ("reading.observation_rules", "lexical.span_surface", "report.cluster_folder_name_rule"):
    case("S-" + key, f"{key} is a live cfg_setting with a use text",
         conn.execute("SELECT count(*) FROM cfg_setting WHERE key=? AND inactive=0 AND coalesce(use,'')<>''", (key,)).fetchone()[0] == 1)
conn.execute("UPDATE cfg_setting SET inactive=1 WHERE key='reading.observation_rules'")
conn.commit()
try:
    orec.rules(Cfg(DB))
    case("S4", "a missing rule is an error, never a fallback in the code", False, "it returned")
except KeyError as exc:
    case("S4", "a missing rule is an error, never a fallback in the code", "rules_must_be_config_driven" in str(exc))
conn.execute("UPDATE cfg_setting SET inactive=0 WHERE key='reading.observation_rules'")
conn.commit()
# ── R: reading.observation_rules ─────────────────────────────────────────────────────────────────
p = {"item": "operation", "mode": "done"}
e1 = []
orec.check_item_parts(cfg, p, "statement", "read", None, "w", e1)
undo = with_rule("reading.observation_items", lambda v: v.update(grounds_required_for_basis=[]))
e2 = []
orec.check_item_parts(cfg, p, "statement", "read", None, "w", e2)
undo()
case("R1", "grounds_required_for_basis: a read observation without grounds is refused; with the row emptied it is accepted",
     any("grounds" in x for x in e1) and not any("grounds" in x for x in e2), (e1, e2))
v = sheet(tag="silence", parts=FULL)
a = [x for x in errors_of(v) if "not a kind of observation" in x]
undo = with_rule("reading.observation_rules", lambda x: x.update(unused_kinds=[]))
b = [x for x in errors_of(sheet(tag="silence", parts=FULL)) if "not a kind of observation" in x]
undo()
case("R2", "unused_kinds: an accepted silence observation is refused; with the row emptied it is not", a and not b, (a, b))
objnode = [{"node": 1, "word": "w (H1)", "role": "object", "occurrence": 1, "counts_for": None, "cluster": "T1", "subgroup": None,
            "reading_id": None, "suggest": None, "flags": [], "action": None}]
a = [x for x in errors_of(sheet(parts=FULL, nodes=objnode)) if "bear on an act" in x or "bears on an act" in x]
undo = with_rule("reading.observation_rules", lambda x: x.update(bears_on_only_refused=False))
b = [x for x in errors_of(sheet(parts=FULL, nodes=objnode)) if "bear on an act" in x or "bears on an act" in x]
undo()
case("R3", "bears_on_only_refused: an observation of bears-on nodes only is refused; with the row false it is not", a and not b, (a, b))
a = [x for x in errors_of(sheet(parts=FULL)) if "the item 'operation'" in x]
undo = with_rule("reading.observation_items", lambda x: x.update(verse_always=[]))
b = [x for x in errors_of(sheet(parts=FULL)) if "the item 'operation'" in x]
undo()
case("R4", "verse_always: the verse without an operation observation is refused; with the row emptied it is not", a and not b, (a, b))
run8 = "one two three four five six seven eight nine"
a = orec.copies_verse(cfg, [run8], run8)
undo = with_rule("reading.observation_items", lambda x: x.update(max_verse_words_copied=20))
b = orec.copies_verse(cfg, [run8], run8)
undo()
case("R5", "max_verse_words_copied: a run of nine words is a restatement; with the row at 20 it is not", a and b is None, (a, b))
spec = {"key": "p", "kind": "party", "text": "a party finding with no route at all", "basis": "stated",
        "nodes": [{"strong": "H5750", "occurrence": conn.execute("SELECT id FROM verse_lexical WHERE strong='H5750' AND deleted=0 LIMIT 1").fetchone()[0],
                   "role": "qualifier", "cluster": "T2"}]}
e1 = []
orec.check(cfg, [("t", dict(spec))], e1, [])
undo = with_rule("reading.observation_rules", lambda x: x.update(route_required_kinds=[]))
e2 = []
orec.check(cfg, [("t", dict(spec))], e2, [])
undo()
case("R6", "route_required_kinds: a party finding without a route is refused; with the row emptied it is not",
     any("carries its route" in x for x in e1) and not any("carries its route" in x for x in e2), (e1, e2))
undo = with_rule("reading.observation_rules", lambda x: x.update(stage="StageX"))
e3, qt = [], []
pl = orec.check(cfg, [("t", dict(spec, route="B", text="a party finding to see the stage written"))], e3, qt)
w = orec.write(conn, pl, None, "RUN-TEST")
oid = w["p"]["observation"]
stg = (conn.execute("SELECT stage FROM ib_observation WHERE id=?", (oid,)).fetchone()[0],
       conn.execute("SELECT source_stage FROM ib_node WHERE observation_id=?", (oid,)).fetchone()[0])
undo()
case("R7", "stage: what is written carries the stage of the row (StageX), observation and node", stg == ("StageX", "StageX"), (e3, stg))
a = conn.execute("SELECT id FROM ib_observation WHERE deleted=0 AND tag='statement' ORDER BY id LIMIT 2").fetchall()
try:
    orec.merge_observation(conn, a[0][0], a[1][0], "test: two different descriptions merged", None, "T", "Claude")
    r1 = "merged"
except orec.Refused as exc:
    r1 = str(exc)
undo = with_rule("reading.observation_rules", lambda x: x.update(merge_same_text_only=False))
try:
    orec.merge_observation(conn, a[0][0], a[1][0], "test: two different descriptions merged", None, "T", "Claude")
    r2 = "merged"
except orec.Refused as exc:
    r2 = str(exc)
undo()
case("R8", "merge_same_text_only: two different descriptions are refused; with the row false the merge is allowed",
     "texts differ" in r1 and r2 == "merged", (r1, r2))
# ── L: lexical.span_surface ──────────────────────────────────────────────────────────────────────
vid = conn.execute("SELECT id FROM verse WHERE osisId='Gen.43.27'").fetchone()[0]
spans = [dict(r) for r in conn.execute("SELECT id, position, surface, strong_variant FROM span WHERE verse_id=? AND deleted=0 ORDER BY position", (vid,))]
base = lexical.span_code_surfaces(conn, vid, spans)
undo = with_rule("lexical.span_surface", lambda x: x.update(look_back_words=0))
none_ = lexical.span_code_surfaces(conn, vid, spans)
undo()
case("L1", "look_back_words: 5 finds 'still' before 'alive'; 0 looks at nothing", sorted(base.values()) == ["still"] and none_ == {}, (base, none_))
case("L2", "single_word_gloss_only: 'to be ashamed' gives nothing, and with the row false gives its words",
     lexical.gloss_alternatives("to be ashamed", setting("lexical.span_surface")) == set()
     and lexical.gloss_alternatives("to be ashamed", dict(setting("lexical.span_surface"), single_word_gloss_only=False)) == {"be", "ashamed"})
case("L3", "gloss_alternative_separators: '/' splits 'about/through', and with only ';' it does not",
     lexical.gloss_alternatives("about/through", setting("lexical.span_surface")) == {"about", "through"}
     and lexical.gloss_alternatives("about/through", dict(setting("lexical.span_surface"), gloss_alternative_separators=";")) == set())
conn.execute("UPDATE cfg_setting SET value=? WHERE key='discovery.particle_pattern'", (json.dumps("^NOPE$"),))
conn.commit()
pp = lexical.span_code_surfaces(conn, vid, spans)
conn.execute("UPDATE cfg_setting SET value=? WHERE key='discovery.particle_pattern'", (json.dumps(r"^[HG]9\d{3}$"),))
conn.commit()
case("L4", "the particle pattern is discovery.particle_pattern (one home): with another pattern the particles H9043, H9008 are not skipped",
     len(pp) >= len(base), (base, pp))
# ── F: report.cluster_folder_name_rule ───────────────────────────────────────────────────────────
case("F1", "the shipped rule gives 'M21 - fasting-piety'", filingkit.cluster_folder_name(conn, "M21") == "M21 - fasting-piety")
undo = with_rule("report.cluster_folder_name_rule", lambda x: x.update(pattern="{slug} ({cluster_code})", word_separator="_"))
alt = filingkit.cluster_folder_name(conn, "M21")
undo()
case("F2", "pattern and word_separator are the row's: 'fasting_piety (M21)'", alt == "fasting_piety (M21)", alt)
case("F3", "the prose convention points at the rule instead of repeating it (one home)",
     "report.cluster_folder_name_rule" in setting("report.cluster_folder_naming_convention")
     and "lowercased, & and all other punctuation dropped" not in setting("report.cluster_folder_naming_convention"))
print(f"\n{sum(res)} of {len(res)} cases pass")
