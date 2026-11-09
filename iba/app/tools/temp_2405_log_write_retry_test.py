"""temp_2405: test of the ai_call write retry (aiclient._log) on a COPY of iba.db. Cases: no lock; lock released within the retries
(row written); lock held past the retries (error raised as before); an OperationalError that is not a lock (raised at once)."""
import re
import shutil
import sqlite3
import sys
import tempfile
import threading
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from iba.app.lib import cfg as cfgmod
from iba.app.lib.aiclient import AiClient

SRC = Path(__file__).resolve().parents[1] / "db" / "iba.db"
tmp = Path(tempfile.mkdtemp()) / "iba_copy.db"
s = sqlite3.connect(f"file:{SRC.as_posix()}?mode=ro", uri=True)
d = sqlite3.connect(tmp)
s.backup(d)
s.close()
d.close()


def client(retries, wait, query_only=False):
    cfg = cfgmod.Cfg(tmp)
    cfg.conn.execute("PRAGMA busy_timeout=300")
    if query_only:
        cfg.conn.execute("PRAGMA query_only=1")
    ai = AiClient(cfg, "temp_2405", "test", transport=lambda route, model, text, opts: ({"ok": 1}, "{}", {}))
    ai.vals["ai.log_write_retries"], ai.vals["ai.log_write_wait_seconds"] = retries, wait
    return ai


def call(ai):
    key, role = ai.conn.execute("SELECT prompt_key, role FROM cfg_ai_prompt WHERE status='active' LIMIT 1").fetchone()
    variables = {k: "x" for k in re.findall(r"\{(\w+)\}", ai.prompt(key)[2])}
    t = time.time()
    try:
        r = ai.call(role, key, variables, ("test", 1))
        return r["outcome"], round(time.time() - t, 1)
    except sqlite3.OperationalError as e:
        return f"OperationalError: {e}", round(time.time() - t, 1)


def hold(seconds):
    h = sqlite3.connect(tmp, timeout=1, check_same_thread=False)
    h.execute("BEGIN IMMEDIATE")
    threading.Timer(seconds, lambda: (h.rollback(), h.close())).start()


def rows():
    return sqlite3.connect(tmp).execute("SELECT count(*) FROM ai_call WHERE module='temp_2405'").fetchone()[0]


print("1 no lock                       ", call(client(3, 1)), "rows", rows())
hold(2.5)
print("2 lock freed after 2.5 s, 5x1 s ", call(client(5, 1)), "rows", rows())
hold(6)
print("3 lock held 6 s, 2 tries x 1 s  ", call(client(2, 1)), "rows", rows())
time.sleep(6)
print("4 not a lock (query_only)       ", call(client(3, 1, query_only=True)), "rows", rows())
shutil.rmtree(tmp.parent, ignore_errors=True)
