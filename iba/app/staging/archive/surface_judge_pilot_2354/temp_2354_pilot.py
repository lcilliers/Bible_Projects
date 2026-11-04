"""Throwaway pilot for escalation #2354 (plan v5): judge ~100 surface strings with lib/surfacejudge.py and write one
batch file. Read-only on iba.db. The sample is seeded: the 20 words of the first timing test, plus 80 strings drawn
from three frequency bands (common, middle, rare) of the distinct lower-cased surfaces of live verse_lexical.

Usage (project venv):  python iba/app/staging/surface_judge_pilot_2354/temp_2354_pilot.py [--n-extra 80]
"""
import argparse
import pathlib
import random
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.lib import surfacejudge as sj  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

FIRST20 = ["within", "you", "written", "fear", "heart", "spirit", "angel", "wicked", "joyful", "upon", "because",
           "god", "satan", "mercy", "slowly", "therefore", "man", "destroyed", "love", "the"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-extra", type=int, default=80)
    ap.add_argument("--seed", type=int, default=20261102)
    a = ap.parse_args()
    cfg = Cfg()
    conn = cfg.conn
    freq = conn.execute("SELECT lower(surface), COUNT(*) FROM verse_lexical WHERE deleted=0 AND surface IS NOT NULL "
                        "AND surface<>'' GROUP BY 1 ORDER BY 2 DESC").fetchall()
    n = len(freq)
    rnd = random.Random(a.seed)
    bands = [freq[:500], freq[500:5000], freq[5000:]]
    each = a.n_extra // 3
    pick = []
    for band, k in zip(bands, (each, each, a.n_extra - 2 * each)):
        pick += [s for s, _ in rnd.sample(band, k) if s not in FIRST20]
    surfaces = FIRST20 + pick
    out = ROOT / pathlib.Path(cfg.setting("surface_judge.batch_dir")) / "pilot-2354-v2-words-20261102.jsonl"
    print(f"{n} distinct surface strings; pilot {len(surfaces)}; batch file {out}", flush=True)
    sj.run_words(cfg, surfaces, out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
