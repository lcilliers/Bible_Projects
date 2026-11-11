"""temp_2479_phrase_members_test_run.py -- tests for escalation #2479: the phrases attached to a collection are members of it (cfg_setting collection.member_tiers),
engagement pulls only the unassessed items with -Missing, and a row is never counted twice.

Plan: outputs/escalation/2479-phrases-as-members-plan.md (cases P1 to P9). Each case is checked against a direct query written here. Read-only on iba.db, except that
case P7 works on a copy of it in the scratch dir; no working file or report is written to the project.

Usage: python iba/app/tools/temp_2479_phrase_members_test_run.py <scratch dir> [after]
  `after` runs case P8 (the engagement of the phrase rows is recorded) instead of the others.
"""
import collections
import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import collectionbuild as cb  # noqa: E402
from iba.app.lib import collectionevidence as ev  # noqa: E402
from iba.app.lib import collectionexport as ce  # noqa: E402
from iba.app.lib import engagement as eg  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402

results = []


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:340]))


S = pathlib.Path(sys.argv[1]) / "t2479"
S.mkdir(parents=True, exist_ok=True)
AFTER = len(sys.argv) > 2 and sys.argv[2] == "after"
cfg = Cfg(ROOT / "iba/app/db/iba.db")
conn = cfg.conn
q = lambda sql, *a: conn.execute(sql, a).fetchall()  # noqa: E731
WORD_TIERS = ["core", "synonym", "opposite", "gathered"]
st = eg.settings(cfg)
cid = q("SELECT id FROM collection WHERE name='search' AND deleted=0")[0][0]
phr = {r[0] for r in q("SELECT DISTINCT lower(trim(t.surface)) FROM collection_link l JOIN surface_term t ON t.id=l.term_id WHERE l.deleted=0 AND l.collection_id=? AND l.tier='phrase'", cid)}
mark = ",".join("?" * len(phr))
phrase_rows = q(f"SELECT id FROM verse_lexical WHERE deleted=0 AND lower(trim(surface)) IN ({mark})", *phr)
word_members = eg.member_terms(conn, cid, WORD_TIERS)
word_surf = {v[0] for v in word_members.values()}
wm = ",".join("?" * len(word_surf))
word_rows = q(f"SELECT id FROM verse_lexical WHERE deleted=0 AND lower(trim(surface)) IN ({wm})", *word_surf)

if not AFTER:
    case("P0", "the setting: member_tiers is the word tiers plus phrase; export_tiers is the word tiers only", st["tiers"] == WORD_TIERS + ["phrase"] and cfg.setting("collection.export_tiers") == WORD_TIERS,
         f"member_tiers {st['tiers']}; export_tiers {cfg.setting('collection.export_tiers')}")
    # P1 evidence report for search
    order = ev.Order(conn)
    vals = ev.read_settings(cfg)
    d = ev.build_collection(conn, ev.resolve(conn, ["search"])[0], vals["tiers"], order)
    ids = [o["vl_id"] for o in d["occurrences"]]
    ph_member = {t["surface"] for t in d["terms"] if "phrase" in t["tiers"].split("/")}
    case("P1", "evidence report for search: 685 word rows + 45 phrase rows, no row twice, the 21 phrases are member rows of tier phrase",
         len(ids) == len(word_rows) + len(phrase_rows) == 730 and len(ids) == len(set(ids)) and ph_member == phr and len(phr) == 21,
         f"occurrences {len(ids)} (words {len(word_rows)}, phrases {len(phrase_rows)}); distinct {len(set(ids))}; phrase members {len(ph_member)}")
    # P2 / P3 pulls
    full = eg.pull(conn, cfg, "search")
    assessed = {r[0] for r in q("SELECT DISTINCT n.verse_lexical_id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=0 AND o.stage=?", st["stage"])}
    unassessed_q = len([r for r in (word_rows + phrase_rows) if r[0] not in assessed])
    try:
        miss = eg.pull(conn, cfg, "search", missing=True)
        miss_ids = {it["vl_id"] for s_ in miss["surfaces"] for it in s_["items"]}
        refused = False
    except eg.EngagementError:
        miss, miss_ids, refused = {"missing": True}, set(), True
    n_full = sum(len(s_["items"]) for s_ in full["surfaces"])
    n_miss = len(miss_ids)
    case("P2", "Pull -Missing for search returns exactly the items with no live engagement node (direct query), none of the assessed rows; with none unassessed it refuses saying there is nothing to pull",
         n_miss == unassessed_q and not (miss_ids & assessed) and miss.get("missing") is True and (refused == (unassessed_q == 0)), f"pulled {n_miss}, query {unassessed_q}, assessed rows among them {len(miss_ids & assessed)}, refused {refused}")
    case("P3", "Pull without -Missing returns every member item: words and phrases", n_full == len(word_rows) + len(phrase_rows) and full.get("missing") is False, f"pulled {n_full}, query {len(word_rows) + len(phrase_rows)}")
    # P4 attach_phrases preview, live against the copy of the database kept before the setting was added
    scope = cfg.setting("surfaces.scope_groups")["a"]
    snaps = sorted((ROOT / "iba/app/db/snapshots/kept").glob("*pre-2479-phrase-members.db"))
    pre = copy_db(S / "pre.db", snaps[-1]) if snaps and not (S / "pre.db").exists() else S / "pre.db"
    r_now = cb.attach_phrases(conn, "TEST", scope, cfg.setting("collection.export_tiers"), "preview", dry=True)
    cfg_pre = Cfg(pre)
    r_pre = cb.attach_phrases(cfg_pre.conn, "TEST", scope, cfg_pre.setting("collection.export_tiers"), "preview", dry=True)
    moved_out = len(q("SELECT 1 FROM surface_term WHERE deleted=0 AND form='phrase' AND surface_group='other' AND group_judged_by='rule:engagement'"))
    case("P4", "attach_phrases preview (it reads collection.export_tiers) gives the same links and flags to add as on the copy kept before the setting existed; its phrase count differs only by the phrases the engagement group step moved out of the scope groups",
         r_now["links_to_add"] == r_pre["links_to_add"] and r_now["flags_to_add"] == r_pre["flags_to_add"] and r_pre["phrases"] - r_now["phrases"] <= moved_out and r_now["english"] <= r_pre["english"],
         f"before: phrases {r_pre['phrases']}, links to add {r_pre['links_to_add']}, flags {r_pre['flags_to_add']}; now: phrases {r_now['phrases']}, links {r_now['links_to_add']}, flags {r_now['flags_to_add']}; phrases moved to other by the rule {moved_out}")
    # P5 check_collection
    chk = eg.check_collection(conn, cfg, "search")
    rows = {r["surface"]: r for r in chk["surfaces"]}
    ph_un = sum(rows[p]["unassessed"] for p in phr if p in rows)
    wd_un = sum(r["unassessed"] for s, r in rows.items() if s not in phr)
    ph_direct = len([r for r in phrase_rows if r[0] not in assessed])
    case("P5", "check_collection for search reports its phrase rows unassessed as the direct count says, and its word rows complete", ph_un == ph_direct and wd_un == 0 and len(rows) == 31 and len(phrase_rows) == 45,
         f"phrase rows unassessed {ph_un} (direct {ph_direct} of {len(phrase_rows)}); word rows unassessed {wd_un}; member surfaces {len(rows)}")
    # P6 exports
    groups = cfg.setting("surfaces.export_groups")
    head, rows6 = ce.build(conn, "members-verses", st["tiers"], groups)
    ti = head.index("tier") if "tier" in head else 3
    ci = 1
    sr = head.index("surface") if "surface" in head else 5
    ph_rows = [r for r in rows6 if r[ci] == "search" and r[ti] == "phrase"]
    ph_surf = {r[sr] for r in ph_rows}
    oi, xi = head.index("osisId"), head.index("strong")
    vlc = collections.Counter((r[0], r[1], r[2]) for r in q("SELECT lower(trim(vl.surface)), v.osisId, vl.strong FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id WHERE vl.deleted=0"))
    mult = collections.Counter(tuple(r) for r in rows6)
    unexplained = [k for k, v in mult.items() if v > 1 and vlc[(k[sr], k[oi], k[xi])] < v]
    words_only = len(ce.build(conn, "members-verses", WORD_TIERS, groups)[1])
    case("P6", "the members-verses export has the phrase rows of search with tier phrase; an identical export row occurs only as often as verse_lexical has rows for that surface, verse and code (the export carries no row id), so no row is counted twice",
         phr <= ph_surf and not unexplained and len(rows6) > words_only,
         f"phrase rows of search {len(ph_rows)}, phrase surfaces {len(ph_surf)} of {len(phr)}; export rows {len(rows6)} (words only {words_only}); identical rows {sum(1 for v in mult.values() if v > 1)}, unexplained {len(unexplained)}")
    # P7 synthetic: the same row reached by two links is counted once
    cp = copy_db(S / "p7.db") if not (S / "p7.db").exists() else (S / "p7.db")
    cfg7 = Cfg(cp)
    c7 = cfg7.conn
    seek_id = c7.execute("SELECT id FROM surface_term WHERE deleted=0 AND lower(surface)='seek' AND form='word'").fetchone()[0]
    c7.execute("UPDATE surface_term SET base_id=? WHERE deleted=0 AND lower(surface)='seek out' AND form='phrase'", (seek_id,))
    c7.commit()
    d7 = ev.build_collection(c7, ev.resolve(c7, ["search"])[0], vals["tiers"], ev.Order(c7))
    ids7 = [o["vl_id"] for o in d7["occurrences"]]
    so = next(t for t in d7["terms"] if t["surface"] == "seek out")
    case("P7", "synthetic: the phrase 'seek out' made a base-of-seek is reached by two links (its own phrase link and the synonym link of seek): one member with both tiers, its rows counted once",
         len(ids7) == len(set(ids7)) == 730 and "phrase" in so["tiers"] and "synonym" in so["tiers"], f"occurrences {len(ids7)}, distinct {len(set(ids7))}, tiers of 'seek out' {so['tiers']}")
    # P9 the engaged collections
    E = {r[0] for r in q("SELECT DISTINCT lower(trim(n.surface)) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE o.stage=? AND o.deleted=0 AND n.deleted=0", st["stage"])}
    terms = {r[0]: r for r in conn.execute("SELECT id, surface, origin, surface_group, group_state, base_id FROM surface_term WHERE deleted=0")}
    memb = ce._memberships(conn, terms, WORD_TIERS, own_link=True)
    csurf = collections.defaultdict(set)
    for sid, ms in memb.items():
        for c_, cn, _, _ in ms:
            csurf[(c_, cn)].add(terms[sid][1].strip().lower())
    engaged = [k for k, v in csurf.items() if v & E]
    done_vl = {r[0] for r in q("SELECT DISTINCT n.verse_lexical_id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=0 AND o.stage=?", st["stage"])}
    cnt = collections.Counter(r[1] for r in q("SELECT id, lower(trim(surface)) FROM verse_lexical WHERE deleted=0") if r[0] not in done_vl)
    def direct_phrase_rows(k):
        return sum(cnt.get(terms[t][1].strip().lower(), 0) for t in {r[0] for r in q("SELECT term_id FROM collection_link WHERE deleted=0 AND tier='phrase' AND collection_id=?", k[0])}
                   if t in terms)
    direct = sum(direct_phrase_rows(k) for k in engaged)
    sample = sorted([k for k in engaged if direct_phrase_rows(k) > 0], key=lambda k: (len(csurf[k]), k[1]))[:3]     # the engaged collections with the fewest member surfaces that have phrase rows to assess
    agree = []
    for k in sample:
        ck = eg.check_collection(conn, cfg, k[1])
        agree.append((k[1], sum(r["unassessed"] for r in ck["surfaces"] if r["tier"] == "phrase"), direct_phrase_rows(k)))
    case("P9", "the collections already through engagement: their unassessed phrase rows by a direct count over all 38, and check_collection agrees with the direct count on the three with fewest member surfaces; nothing is written",
         len(engaged) == 38 and all(a_ == b_ for _, a_, b_ in agree) and direct > 0, f"{len(engaged)} collections; unassessed phrase rows (direct) {direct}; check_collection vs direct {agree}")
else:
    chk = eg.check_collection(conn, cfg, "search")
    rows = {r["surface"]: r for r in chk["surfaces"]}
    ph_un = sum(rows[p]["unassessed"] for p in phr if p in rows)
    nodes = q(f"SELECT count(DISTINCT n.verse_lexical_id) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=0 AND o.stage=? "
              f"AND n.verse_lexical_id IN (SELECT id FROM verse_lexical WHERE deleted=0 AND lower(trim(surface)) IN ({mark}))", st["stage"], *phr)[0][0]
    obs_surf = q(f"SELECT count(DISTINCT lower(trim(n.surface))) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=0 AND o.stage=? "
                 f"AND lower(trim(n.surface)) IN ({mark})", st["stage"], *phr)[0][0]
    case("P8", "after the engagement of the phrase rows: check_collection has none unassessed, every phrase row has a live engagement node, every phrase has observations",
         ph_un == 0 and nodes == len(phrase_rows) and obs_surf == len(phr) and chk["failing"] == 0, f"unassessed {ph_un}; rows with a node {nodes} of {len(phrase_rows)}; phrases with observations {obs_surf} of {len(phr)}; failing surfaces {chk['failing']}")

out = ["| id | case | result | evidence |", "|---|---|---|---|"] + [f"| {a} | {b} | {c} | {e} |" for a, b, c, e in results]
(S / ("results-after.md" if AFTER else "results.md")).write_text("\n".join(out) + "\n", encoding="utf-8")
print("\n".join(out))
print(f"\n{sum(r[2] == 'PASS' for r in results)} of {len(results)} passed")
shutil.rmtree(S / "p7.db", ignore_errors=True) if (S / "p7.db").is_dir() else None
sys.exit(0 if all(r[2] == "PASS" for r in results) else 1)
