"""import_seed.py — ONE-OFF migration: bring the candidate seed into the IBA app.

Migrates the old study's INDEPENDENT candidate assessment (not the registry) into the app:
  - lemma_inventory  <- the ~11,804-lemma inventory (the independent substrate).
  - candidate_seed   <- each lemma's decision, read from the inventory's own flags
                        (char_matched -> registry-direct; ib_candidate -> ib-judgement),
                        plus the IB-judgement REJECTED list, plus read-emergent extensions.
Then it performs the once-off MAPPING against the strongs already in the IBA DB: for every
seed lemma, registry_match = a current IBA registry word that carries it (via word_strong).
A candidate with registry_match NULL is a candidate MISSING registry word — the double control.

Read-only on the old study files; writes only lemma_inventory + candidate_seed in the app DB.

    python -m iba.app.migration.import_seed            # run the migration (idempotent)
"""

from __future__ import annotations

import datetime
import glob
import json
import pathlib
import re
import sys

from ..lib.cfg import Cfg
from ..lib.db import Db

REPO = pathlib.Path(__file__).resolve().parents[3]
INVENTORY = REPO / "research/discovery/lemma-inventory-master-no-particles-20260707.json"
REJECTED = REPO / "research/investigations/ib-judgement-rejected-20260707.md"
EMERGENT_GLOB = str(REPO / "verse-analysis/**/char-seed-extension-read-emergent-*.json")


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _base(code: str, pat: str) -> str:
    m = re.match(pat, code or "")
    return m.group(1) if m else (code or "")


def _md_strongs(path: pathlib.Path) -> list[str]:
    if not path.exists():
        return []
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*([HG]\d+)", line.strip())
        if m:
            out.append(m.group(1))
    return out


def main() -> int:
    cfg = Cfg()
    db = Db(cfg)
    if "candidate_seed" not in cfg.may_write("migration"):
        print("write-grant violation: 'migration' may not write candidate_seed", file=sys.stderr)
        return 1
    if not INVENTORY.exists():
        print(f"lemma inventory not found: {INVENTORY}", file=sys.stderr)
        return 1

    pat = cfg.setting("candidate.lemma_base_pattern", r"^([HG]\d+)([A-Z]?)$")
    now = _now()
    inv = json.loads(INVENTORY.read_text(encoding="utf-8"))["lemmas"]

    # clean re-run
    db.conn.execute("DELETE FROM candidate_seed")
    db.conn.execute("DELETE FROM lemma_inventory")

    # 1. lemma_inventory (dedup on base) + 2. candidate_seed from the inventory's own flags
    inv_keys: set[str] = set()
    written: set[str] = set()
    c = {"inventory": 0, "registry_direct": 0, "ib_judgement": 0, "rejected": 0, "read_emergent": 0}
    for L in inv:
        lk = _base(L.get("strong", ""), pat)
        if not lk or lk in inv_keys:
            continue
        inv_keys.add(lk)
        db.write("lemma_inventory", {
            "lemma_key": lk, "gloss": L.get("gloss"), "language": L.get("language"),
            "source": "lemma-inventory-master-2026", "created_at": now, "deleted": 0})
        c["inventory"] += 1
        matched, ibc = L.get("char_matched"), L.get("ib_candidate")
        if matched or ibc:
            layer = "registry-direct" if matched else "ib-judgement"
            db.write("candidate_seed", {
                "lemma_key": lk, "decision": "candidate", "layer": layer,
                "registry_match": None, "tag": L.get("gloss"), "assessed_at": now, "deleted": 0})
            written.add(lk)
            c["registry_direct" if matched else "ib_judgement"] += 1

    # 3. explicit IB-judgement rejects
    for s in _md_strongs(REJECTED):
        lk = _base(s, pat)
        if lk in inv_keys and lk not in written:
            db.write("candidate_seed", {
                "lemma_key": lk, "decision": "rejected", "layer": "ib-judgement",
                "registry_match": None, "tag": None, "assessed_at": now, "deleted": 0})
            written.add(lk)
            c["rejected"] += 1

    # 4. read-emergent extensions (self-learning) — candidates surfaced by past reads
    for f in glob.glob(EMERGENT_GLOB, recursive=True):
        for e in json.loads(pathlib.Path(f).read_text(encoding="utf-8")).get("lemmas", []):
            lk = _base(e.get("strong", ""), pat)
            if lk in inv_keys and lk not in written:
                db.write("candidate_seed", {
                    "lemma_key": lk, "decision": "candidate", "layer": "read-emergent",
                    "registry_match": None, "tag": e.get("seed_word"), "assessed_at": now, "deleted": 0})
                written.add(lk)
                c["read_emergent"] += 1

    # 5. once-off MAPPING against the strongs already in the IBA DB
    cover: dict[str, str] = {}
    for r in db.rows("SELECT wr.word AS word, ws.strong AS strong FROM word_strong ws "
                     "JOIN word_registry wr ON wr.id = ws.word_id "
                     "WHERE ws.deleted=0 AND wr.deleted=0"):
        cover.setdefault(_base(r["strong"], pat), r["word"])
    mapped = 0
    for lk, word in cover.items():
        if lk in written:
            db.conn.execute("UPDATE candidate_seed SET registry_match=? WHERE lemma_key=?", (word, lk))
            mapped += 1

    db.close()
    cfg.close()
    total = c["registry_direct"] + c["ib_judgement"] + c["read_emergent"]
    print(f"seed migrated: {c['inventory']} inventory lemma(s); "
          f"{total} candidate(s) (registry-direct {c['registry_direct']}, "
          f"ib-judgement {c['ib_judgement']}, read-emergent {c['read_emergent']}), "
          f"{c['rejected']} rejected. Mapped {mapped} to existing IBA registry words.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
