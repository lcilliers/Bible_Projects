"""surface_collection_fix_2361_v1_20261106.py -- escalation #2361, stage 5: corrects the `does` text of step collection.links, which still named
the -Associate switch that the final design (a removal is respected) does not have. Through configmaint.apply_logged(). Idempotent."""
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

RUN_ID = "DEVMODE-2361-SURFACE-COLLECTION-FIX-20261106"
DOES = ("decide the members of each collection from the AI judgements and write the difference: new links, tier changes (old row deleted, superseded_by), "
        "shared flags, word states; -Check previews; a pair whose link was removed (deleted, no successor) is not linked again -- see lib/collectionbuild.py "
        "(escalation #2361)")
conn = Cfg(pathlib.Path(sys.argv[sys.argv.index("--db") + 1] if "--db" in sys.argv else r"C:\Bible_study_projects\iba\app\db\iba.db")).conn
cur = conn.execute("SELECT does FROM cfg_step WHERE step='collection.links'").fetchone()[0]
if cur == DOES:
    print("already applied: nothing changed")
else:
    apply_logged(conn, RUN_ID, "cfg_step", "update", {"step": "collection.links"}, {"does": DOES})
    conn.commit()
    print(f"applied (run {RUN_ID}): collection.links text corrected")
