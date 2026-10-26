"""#2305 step 1: index of the documents to capture, from the cluster reading index (#2228).

Read-only on iba.db. Writes outputs/escalation/2305-prior-work-document-index-v1-20261026.json.
"""
import collections, datetime, hashlib, json, pathlib, re, sqlite3, sys

ROOT = pathlib.Path(r"C:\Bible_study_projects")
sys.path.insert(0, str(ROOT / "iba" / "app"))
from lib.readingindex import files_in_roots  # noqa: E402

OUT = ROOT / "outputs/escalation/2305-prior-work-document-index-v1-20261026.json"
c = sqlite3.connect(ROOT / "iba/app/db/iba.db")
roots = json.loads(c.execute("select value from cfg_setting where key='reading_index.roots'").fetchone()[0])
names = dict(c.execute("select cluster_code, short_name from cluster"))

# Kind from the file name only: a hint for ordering the capture, not a reading of the file.
KINDS = [
    ("admin", r"^(cluster_readme\.md|cluster-assign(-v\d+-\d{8})?\.md|cluster(-v\d+-\d{8})?\.md)$"),
    ("process", r"proposal|handoff|plan-|method|process|rulings?|scope|test|check|filter|split|"
                r"change-record|redraft|question|stocktake|status|coverage|fanout|reallocation|iteration|grouping"),
    ("data", r"worksheet|list|-verses|passages|full-text|register|index|-data|surface-forms|rows|remaining|crossref|pull"),
    ("ledger", r"ledger"),
    ("synthesis", r"overview|synthesis|summary|account|digest|depiction|phenomena|findings|observations|"
                  r"consolidation|reconcile|synergy|distinction|assessment|linkage|narrative|framework|"
                  r"consideration|decisions|weave|anchor|cuts|mcode|qualifier|discussion|candidate|map"),
    ("reading", r"reading|batch|scan|trace|r0|-x-"),
]


def kind_of(name: str) -> str:
    n = name.lower()
    if re.search(r"reading|reread|validation", n) and not re.search(r"proposal|handoff|test", n):
        return "reading"
    for k, pat in KINDS:
        if re.search(pat, n):
            return k
    return "other"


def cluster_of(path: str, indexed: str | None) -> str | None:
    if indexed:
        return indexed
    n = path.rsplit("/", 1)[-1].lower()
    if "origin-of-thought" in path:
        return None
    m = re.search(r"\bm(\d{2})\b|-m(\d{2})-|^m(\d{2})-", n)
    return f"M{next(g for g in m.groups() if g)}" if m else None


def version_date(name: str):
    m = re.search(r"-v(\d+)-(\d{8})\.md$", name) or re.search(r"()-(\d{8})\.md$", name)
    if not m:
        return None, None
    v = int(m.group(1)) if m.group(1) else None
    d = m.group(2)
    return v, f"{d[:4]}-{d[4:6]}-{d[6:]}"


disk = set(files_in_roots(ROOT, roots))
idx = {r[1]: r for r in c.execute(
    "select id, path, cluster, size_bytes, sha256, indexed_at, sections, refs, imported_observations "
    "from reading_file where removed=0")}
verses = dict(c.execute(
    "select file_id, count(distinct verse_id) from reading_ref where deleted=0 and verse_id is not null group by 1"))
ref_secs = dict(c.execute(
    "select file_id, count(distinct section_id) from reading_ref where deleted=0 group by 1"))

docs = []
gone = sorted(set(idx) - disk)
for path in sorted(disk):
    r = idx.get(path)
    p = ROOT / path
    on_disk = path in disk
    sha = hashlib.sha256(p.read_bytes()).hexdigest() if on_disk else None
    name = path.rsplit("/", 1)[-1]
    v, d = version_date(name)
    cl = cluster_of(path, r[2] if r else None)
    imported = c.execute("select count(*) from ib_observation where revisit_note like ? and status <> 'withdrawn'",
                         (f"%{path}%",)).fetchone()[0]
    index_state = ("not in index (new since build)" if not r else
                   "gone from disk" if not on_disk else
                   "changed since build" if sha != r[4] else "current")
    docs.append({
        "path": path,
        "folder": path.rsplit("/", 1)[0],
        "cluster": cl,
        "cluster_name": names.get(cl) if cl else ("origin-of-thought strand" if "origin-of-thought" in path else None),
        "kind_by_name": kind_of(name),
        "version": v,
        "date": d,
        "size_bytes": p.stat().st_size if on_disk else (r[3] if r else None),
        "reading_file_id": r[0] if r else None,
        "index_state": index_state,
        "sections": r[6] if r else None,
        "sections_with_refs": ref_secs.get(r[0], 0) if r else None,
        "refs": r[7] if r else None,
        "distinct_verses": verses.get(r[0], 0) if r else None,
        "already_imported_observations": imported,
        "imported_at_index_build": r[8] if r else None,
        "capture_status": "not started",
        "note": ("admin file by name; expected to hold no findings (researcher to confirm)" if kind_of(name) == "admin" else
                 "has observations from the October catch-up, imported outside the observation rules (#2266)"
                 if imported else None),
    })

# Earlier versions of the same document (same name stem, lower version).
stems = collections.defaultdict(list)
for dd in docs:
    stem = re.sub(r"-v\d+-\d{8}\.md$|-\d{8}\.md$|\.md$", "", dd["path"])
    stems[stem].append(dd)
for group in stems.values():
    group = [x for x in group if x["version"] is not None]
    if len(group) > 1:
        latest = max(group, key=lambda x: (x["version"] or 0, x["date"] or ""))
        for dd in group:
            if dd is not latest:
                dd["later_version"] = latest["path"]

by = lambda key: dict(sorted(collections.Counter(str(dd[key]) for dd in docs).items()))
index = {
    "escalation": 2305,
    "title": "Capture prior reading work into ib_observation and ib_node: document index",
    "version": 1,
    "generated_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "source": {
        "set": "the cluster reading index (#2228): every .md file under cfg_setting reading_index.roots, archive/ folders left out",
        "roots": roots,
        "tables": ["reading_file", "reading_section", "reading_ref"],
        "already_imported": "live ib_observation rows (not withdrawn) whose revisit_note names the file, counted now; imported_at_index_build is reading_file.imported_observations from 2026-10-23",
        "excluded_by_researcher_2026-10-22": "outputs/escalation/2228-discovery-scope-and-known-v3-20261022.md (Bible_Books, registry, essay, characteristics, dimensions, outputs/, research/; cross-cluster-web except origin-of-thought)",
        "not_included": "the .csv files in origin-of-thought (not .md, so not in the reading index)",
    },
    "field_notes": {
        "kind_by_name": "a hint from the file name only (reading, ledger, synthesis, data, process, admin, other); not a reading of the file",
        "index_state": "the file against its reading_file row: current, changed since build, not in index, gone from disk",
        "distinct_verses": "resolved verse references in the file (reading_ref, verse_id not null)",
        "capture_status": "not started | in progress | captured | nothing to capture; set as the capture runs",
        "later_version": "set when a later version of the same document is also in the set",
    },
    "totals": {
        "documents": len(docs),
        "size_bytes": sum(dd["size_bytes"] or 0 for dd in docs),
        "refs": sum(dd["refs"] or 0 for dd in docs),
        "already_imported_observations": sum(dd["already_imported_observations"] for dd in docs),
        "documents_with_imports": sum(1 for dd in docs if dd["already_imported_observations"]),
        "by_cluster": by("cluster"),
        "by_kind_by_name": by("kind_by_name"),
        "by_index_state": by("index_state"),
        "gone_from_disk_since_build": gone,
        "with_later_version": sum(1 for dd in docs if "later_version" in dd),
    },
    "documents": [dict(seq=i, **dd) for i, dd in enumerate(docs, start=1)],
}
OUT.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps(index["totals"], indent=2))
