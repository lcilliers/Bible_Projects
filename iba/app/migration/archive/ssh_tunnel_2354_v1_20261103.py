"""ssh tunnel to the Ollama server (escalation #2354, researcher 2026-11-03).

The server's own port (ollama.host) does not connect from this machine while ssh does, so the run opens an ssh
tunnel with the batch key (ollama.ssh_key, no passphrase) and calls the server through its local end.
One setting: ollama.tunnel_local_port. Idempotent. Usage: python this_file.py [path of an iba.db copy]
(default: the live iba.db)."""
import sqlite3
import sys

from iba.app.handlers.configmaint import apply_logged

DB = sys.argv[1] if len(sys.argv) > 1 else "iba/app/db/iba.db"
RUN_ID = "DEVMODE-2354-SSH-TUNNEL-20261103"
KEY = "ollama.tunnel_local_port"
USE = ("the local port of the ssh tunnel a judging run opens to the Ollama server, with ollama.ssh_key as "
       "ollama.ssh_target, and calls the server through (127.0.0.1:this port to the server's own port of "
       "ollama.host); the tunnel is closed when the run ends. Used because the server's port does not connect "
       "directly from this machine while ssh does (#2354, researcher 2026-11-03). Not set: the server is called "
       "at ollama.host directly. Must differ from 11434, the port of a local Ollama")

conn = sqlite3.connect(DB)
if conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (KEY,)).fetchone():
    print("already present:", KEY)
else:
    apply_logged(conn, RUN_ID, "cfg_setting", "insert", {},
                 {"key": KEY, "value": "11435", "use": USE, "module": "ollama", "inactive": 0})
    conn.commit()
    print("inserted:", KEY)
