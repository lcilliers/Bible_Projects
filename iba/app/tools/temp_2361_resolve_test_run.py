"""temp_2361_resolve_test_run.py -- tests for escalation #2361 stage 3: the resolve module (lib/surfaceresolve.py, handlers/surfaceresolve.py,
Surface-Resolve.ps1). The loaded combined base of 2026-11-04 is the expected value: on a copy of iba.db the rule must decide it unchanged; the
copy is then scrambled (every base removed, every accepted flag cleared, the own evidence rows deleted) and Run must restore it exactly.
Then the behaviour with changed evidence: a protected state, a missing AI answer, a new AI base, a failed call, an ambiguous word.

Usage: python iba/app/tools/temp_2361_resolve_test_run.py <scratch dir>
"""
import builtins
import json
import pathlib
import shutil
import subprocess
import sys
import types

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers import surfaceresolve as H  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402

results = []


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:300]))


S = pathlib.Path(sys.argv[1]) / "t2361r"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db")
mig = ROOT / "iba/app/migration/surface_resolve_2361_v1_20261106.py"
mig = mig if mig.exists() else ROOT / "iba/app/migration/archive" / mig.name
o = [subprocess.run([sys.executable, str(mig), "--db", str(DB), "--no-snapshot"], capture_output=True, text=True).stdout.strip() for _ in range(2)]
case("B0", "migration: applied (or already), then nothing to do", ("applied" in o[0] or "already" in o[0]) and "already" in o[1], o)
cfg = Cfg(DB)
conn = cfg.conn
ctx = lambda **p: types.SimpleNamespace(cfg=cfg, params=p, run_id="TEST-RUN")  # noqa: E731
count = lambda sql, *a: conn.execute(sql, a).fetchone()[0]  # noqa: E731


def state():
    terms = conn.execute("SELECT t.surface, b.surface, t.base_source, t.base_state FROM surface_term t LEFT JOIN surface_term b ON b.id=t.base_id "
                         "WHERE t.deleted=0 ORDER BY t.surface, t.id").fetchall()
    acc = conn.execute("SELECT t.surface, d.method, d.kind, d.base_word, d.accepted FROM surface_derivation d JOIN surface_term t ON t.id=d.term_id "
                       "WHERE d.deleted=0 AND d.accepted=1 ORDER BY 1,2,3,4").fetchall()
    return terms, acc


_real_open = builtins.open


def _no_files(path, *a, **k):
    if any(x in str(path).replace("\\", "/") for x in ("_analytics/", "outputs/")):
        raise AssertionError(f"a file was read: {path}")
    return _real_open(path, *a, **k)


builtins.open = _no_files
try:
    st0 = state()
    o = H.status(_ctx := ctx())
    case("B1", "the rule decides the loaded combined base unchanged: 6,066 terms as decided, none to change", o.condition == "ok" and o.counts["to_change"] == 0
         and o.counts["unchanged"] == 6066, o.counts)
    for k, v in (("matched_structure", 1232), ("base_ambiguous", 14), ("matched_sibling", 89), ("ai_answered", 387), ("ai_none", 289), ("ai_failed", 31),
                 ("resolved_own", 642), ("phrase_not_tested", 1166), ("out_of_scope", 2216)):
        assert count("SELECT count(*) FROM surface_term WHERE deleted=0 AND origin='surface' AND base_state=?", k) == v
    case("B2", "the nine states hold the recorded counts (1,232 / 14 / 89 / 387 / 289 / 31 / 642 / 1,166 / 2,216)", True, "asserted")
    # scramble
    conn.execute("UPDATE surface_term SET base_id=NULL, base_source=NULL, base_state='unmatched' WHERE deleted=0 AND origin='surface'")
    conn.execute("UPDATE surface_derivation SET accepted=0 WHERE deleted=0")
    conn.execute("DELETE FROM surface_derivation WHERE method='own'")
    conn.commit()
    o = H.run(ctx(Check="true"))
    case("B3", "scrambled copy: Run -Check previews the repair and writes nothing", o.condition == "ok" and "PREVIEW" in o.message
         and count("SELECT count(*) FROM surface_term WHERE base_state='unmatched'") > 6000, o.counts)
    o = H.run(ctx())
    st1 = state()
    case("B4", "Run restores every base, source and state", st1[0] == st0[0], o.counts)
    case("B5", "and every accepted evidence row (the own rows are written again)", st1[1] == st0[1], (len(st0[1]), len(st1[1])))
    o = H.run(ctx())
    case("B6", "a second Run changes nothing", o.counts["terms"] == 0 and state() == st1, o.counts)
    ev = count("SELECT count(*) FROM surface_event WHERE action='set_base' AND by='surface-resolve'")
    case("B7", "every changed term has a surface_event with its before and after", ev > 6000 and count("SELECT count(*) FROM surface_event WHERE by='surface-resolve' AND value_before IS NULL") == 0, ev)
    # protected
    conn.execute("UPDATE surface_term SET base_state='confirmed', base_id=(SELECT id FROM surface_term WHERE surface='hide' AND deleted=0) WHERE surface='hides' AND deleted=0")
    conn.commit()
    H.run(ctx())
    case("B8", "a base the researcher confirmed is never touched", count("SELECT count(*) FROM surface_term WHERE surface='hides' AND base_state='confirmed' AND base_id=(SELECT id FROM surface_term WHERE surface='hide' AND deleted=0)") == 1, "hides -> hide")
    # a missing AI answer: soft delete one answered call
    sid, call = conn.execute("SELECT t.id, d.ai_call_id FROM surface_term t JOIN surface_derivation d ON d.term_id=t.id WHERE t.base_state='ai_answered' AND d.method='ollama' AND d.accepted=1 LIMIT 1").fetchone()
    conn.execute("UPDATE ai_call SET deleted=1 WHERE id=?", (call,))
    conn.commit()
    H.run(ctx())
    row = conn.execute("SELECT base_state, base_id, base_source FROM surface_term WHERE id=?", (sid,)).fetchone()
    case("B9", "no AI call for a word the structure leaves unmatched: state unmatched, no base, the Ollama row no longer accepted",
         tuple(row) == ("unmatched", None, None) and count("SELECT count(*) FROM surface_derivation WHERE term_id=? AND method='ollama' AND accepted=1 AND deleted=0", sid) == 0, tuple(row))
    # a new AI answer with a base that is not a surface: computed term
    mod, step, role, mid = conn.execute("SELECT module, step, role, model_id FROM ai_call WHERE id=?", (call,)).fetchone()
    cur = conn.execute("INSERT INTO ai_call (module, step, role, model_id, subject_kind, subject_id, answer, result, outcome, created_by) VALUES (?,?,?,?, 'surface_term', ?, ?, ?, 'answered', 'test')",
                       (mod, step, role, mid, sid, json.dumps({"relation": "derivation", "base": "zzbase"}), "zzbase"))
    conn.commit()
    H.run(ctx())
    row = conn.execute("SELECT t.base_state, b.surface, b.origin, t.base_source FROM surface_term t JOIN surface_term b ON b.id=t.base_id WHERE t.id=?", (sid,)).fetchone()
    case("B10", "a new AI answer with a base outside the list: ai_answered, a computed term is made for the base", tuple(row) == ("ai_answered", "zzbase", "computed", "ollama"), tuple(row))
    # failed call
    conn.execute("UPDATE ai_call SET outcome='refused', result=NULL, answer=NULL WHERE id=?", (cur.lastrowid,))
    conn.commit()
    H.run(ctx())
    row = conn.execute("SELECT t.base_state, t.base_id=t.id, t.base_source FROM surface_term t WHERE t.id=?", (sid,)).fetchone()
    case("B11", "a refused call: ai_failed, the word is its own base, no Ollama row accepted", tuple(row) == ("ai_failed", 1, "own"), tuple(row))
    # ambiguity
    amb = conn.execute("SELECT id FROM surface_term WHERE surface='hiding' AND deleted=0").fetchone()[0]
    case("B12", "a word with two structure bases is base_ambiguous: no base, nothing accepted",
         tuple(conn.execute("SELECT base_state, base_id FROM surface_term WHERE id=?", (amb,)).fetchone()) == ("base_ambiguous", None)
         and count("SELECT count(*) FROM surface_derivation WHERE term_id=? AND accepted=1 AND deleted=0", amb) == 0, "hiding")
    o = H.show(ctx(Surface="hiding"))
    case("B13", "Show names the stored state, the decision and the evidence rows", o.condition == "ok" and "base_ambiguous" in o.message, o.message[:80])
    o = H.show(ctx(Surface="not a surface"))
    case("B14", "Show: a word that is not a live surface is refused", o.condition == "refused", o.message[:60])
    conn.execute("DELETE FROM cfg_setting WHERE key='resolve.order'")
    conn.commit()
    before = count("SELECT count(*) FROM surface_event")
    o1, o2 = H.status(ctx()), H.run(ctx())
    case("B15", "a missing setting is refused by Status and Run and writes nothing", o1.condition == "refused" and o2.condition == "refused"
         and count("SELECT count(*) FROM surface_event") == before, o2.message[:80])
finally:
    builtins.open = _real_open
case("B16", "no file under _analytics or outputs was read by any handler call above", True, "open() was patched to raise, and none did")

width = max(len(r[0]) for r in results)
fails = [r for r in results if r[2] == "FAIL"]
for cid, desc, res_, evd in results:
    print(f"{cid:<{width}}  {res_}  {desc}  [{evd}]")
print(f"\n{len(results) - len(fails)} of {len(results)} pass")
sys.exit(1 if fails else 0)
