"""temp_2381_units_test_run.py -- escalation #2381 test plan (design outputs/escalation/2381-verse-lexical-surface-fix-design-v2-20261107.md).
Read-only on the live iba.db, except case E which rebuilds four verses on a COPY (never the live DB).
Cases: S synthetic units (apply_unit_fields), R real verses, I invariants over every live row, H the held rows, N nodes,
U the unit reader, W the reading sheet, E idempotence. Usage: python iba/app/tools/temp_2381_units_test_run.py <scratch dir>.
Prints PASS/FAIL per case."""
import collections
import pathlib
import re
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib import lexical, reading  # noqa: E402

LIVE = ROOT / "iba/app/db/iba.db"
cfg = Cfg(LIVE)
conn = cfg.conn
conn.row_factory = sqlite3.Row
rule = cfg.required_setting("lexical.span_surface")
particle = re.compile(cfg.required_setting("discovery.particle_pattern"))
res = []


def case(name, what, ok, detail=""):
    res.append(bool(ok))
    print(f"{name} {'PASS' if ok else 'FAIL'} {what}" + ("" if ok else f"  -- {detail}"), flush=True)


def q(sql, *a):
    return conn.execute(sql, a).fetchall()


def run(word, codes, hits=None):
    rows = [{"strong": c, "morph_code": m, "surface": word} for c, m in codes]
    lexical.apply_unit_fields(conn, {"id": 1, "surface": word}, rows, {(1, i): w for i, w in (hits or {}).items()}, rule, particle)
    return [(r["strong"], r["surface"], r["surface_kind"], r["unit_role"], r["unit_size"]) for r in rows]


# ── S synthetic ───────────────────────────────────────────────────────────────────────────────────
case("S1", "a one-code unit is sole and own", run("love", [("G0026", "N-ASF")]) == [("G0026", "love", "own", "sole", 1)])
s = run("heart", [("H3820A", "HNcms"), ("H9002", "HC"), ("H9023", "HSp3m")])
case("S2", "one content code with a prefix and a suffix: head keeps the unit's word (own); prefix and suffix take their own gloss (gloss)",
     s == [("H3820A", "heart", "own", "head", 3), ("H9002", "and", "gloss", "prefix", 3), ("H9023", "his", "gloss", "suffix", 3)], s)
s = run("gave", [("H5414G", "HVqp3"), ("H3588A", "HTc"), ("H9005", "HR")])
case("S3", "two content codes, no exact word: both content_part and shared (the word is not guessed); the affix is gloss",
     s == [("H5414G", "gave", "shared", "content_part", 3), ("H3588A", "gave", "shared", "content_part", 3), ("H9005", "to/for", "gloss", "prefix", 3)], s)
s = run("alive", [("H2416A", "HAams"), ("H5750", "HAcms")], {1: "still"})
case("S4", "two content codes: the look-back word is own; a unit word that is a whole alternative of the code's gloss is own too",
     s == [("H2416A", "alive", "own", "content_part", 2), ("H5750", "still", "own", "content_part", 2)], s)
s = run("from", [("H9006", "HR"), ("H9013", "HSh")])
case("S5", "an affix-only unit has no head: each code is gloss, roles from the morph class",
     [x[2:] for x in s] == [("gloss", "prefix", 2), ("gloss", "suffix", 2)] and s[0][1] == "from" and s[1][1] == "[emph.?]", s)
s = run("attack", [("G9315", "V-2AMI-3P"), ("H9005", "HR")])
case("S6", "G9315 matches the affix pattern but is a content code (not_affix_codes): head and own", s[0][1:] == ("attack", "own", "head", 2), s)
s = run("x", [("H3068G", "HNp"), ("H9008", "XYZ")])
case("S7", "an affix whose morph class is in neither list is role affix (still gloss)", s[1][2:4] == ("gloss", "affix"), s)
s = run("x", [("H3068G", "HNp"), ("H9008", None)])
case("S8", "an affix with no morph code is role affix, not a crash", s[1][2:4] == ("gloss", "affix"), s)

# ── R real verses ─────────────────────────────────────────────────────────────────────────────────
def rows_of(osis, pos):
    return [(r["strong"], r["surface"], r["surface_kind"], r["unit_role"]) for r in q(
        "SELECT vl.strong, vl.surface, vl.surface_kind, vl.unit_role FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id "
        "WHERE v.osisId=? AND vl.position=? AND vl.deleted=0 ORDER BY vl.code_ordinal", osis, pos)]


case("R1", "Jer 23:12 position 3: H2519 'slippery paths' head; H9028 their, H9005 to/for, H9038 them are the affix glosses",
     rows_of("Jer.23.12", 3) == [("H2519", "slippery paths", "own", "head"), ("H9028", "their", "gloss", "suffix"),
                                 ("H9005", "to/for", "gloss", "prefix"), ("H9038", "them", "gloss", "suffix")], rows_of("Jer.23.12", 3))
case("R2", "Isa 32:6 position 3: heart (H3820A) own head, H9002 'and' a prefix",
     rows_of("Isa.32.6", 3) == [("H3820A", "heart", "own", "head"), ("H9002", "and", "gloss", "prefix")], rows_of("Isa.32.6", 3))
case("R3", "Gen 43:27 position 7: alive and still own (the October look-back), he and [?] glosses",
     [x[:3] for x in rows_of("Gen.43.27", 7)] == [("H2416A", "alive", "own"), ("H5750", "still", "own"), ("H9043", "he", "gloss"), ("H9008", "[¿]", "gloss")],
     rows_of("Gen.43.27", 7))
case("R4", "Job 21:19 position 3: children (H1121A) own head with the prefix to/for",
     rows_of("Job.21.19", 3) == [("H1121A", "children", "own", "head"), ("H9005", "to/for", "gloss", "prefix")], rows_of("Job.21.19", 3))

# ── I invariants over every live row ──────────────────────────────────────────────────────────────
tot = q("SELECT count(*) FROM verse_lexical WHERE deleted=0")[0][0]
case("I1", "no live row has an empty unit column", q("SELECT count(*) FROM verse_lexical WHERE deleted=0 AND (unit_surface IS NULL OR surface_kind IS NULL OR unit_size IS NULL OR unit_role IS NULL)")[0][0] == 0)
case("I2", "every kind and role is an enum value", q("SELECT count(*) FROM verse_lexical WHERE deleted=0 AND (surface_kind NOT IN (SELECT value FROM cfg_enum WHERE name='verse_lexical.surface_kind') OR unit_role NOT IN (SELECT value FROM cfg_enum WHERE name='verse_lexical.unit_role'))")[0][0] == 0)
bad = q("SELECT count(*) FROM (SELECT span_id, count(*) n, min(unit_size) a, max(unit_size) b, count(DISTINCT unit_surface) d FROM verse_lexical WHERE deleted=0 GROUP BY span_id) WHERE n<>a OR a<>b OR d<>1")[0][0]
case("I3", "each unit: unit_size equals its live row count and unit_surface is one value", bad == 0, bad)
case("I4", "unit_size 1 is exactly role sole and kind own", q("SELECT count(*) FROM verse_lexical WHERE deleted=0 AND ((unit_size=1) <> (unit_role='sole') OR (unit_size=1 AND surface_kind<>'own'))")[0][0] == 0)
aff = [r["id"] for r in q("SELECT id, strong, unit_size, surface_kind FROM verse_lexical WHERE deleted=0 AND unit_size>1") if lexical.is_affix(r["strong"], particle, rule) and r["surface_kind"] != "gloss"]
case("I5", "every affix code in a multi-code unit is gloss (131,024 rows)", not aff and q("SELECT count(*) FROM verse_lexical WHERE deleted=0 AND surface_kind='gloss'")[0][0] == 131024, len(aff))
case("I6", "a gloss row's surface is its code's own STEP gloss, never empty",
     q("SELECT count(*) FROM verse_lexical vl JOIN strong s ON s.strongNumber=vl.strong WHERE vl.deleted=0 AND vl.surface_kind='gloss' AND vl.surface IS NOT s.stepGloss")[0][0] == 0)
case("I7", "a head exists exactly where a unit has one content code and at least one affix (83,419 units)",
     q("SELECT count(*) FROM verse_lexical WHERE deleted=0 AND unit_role='head'")[0][0] == 83419
     and q("SELECT count(*) FROM (SELECT span_id FROM verse_lexical WHERE deleted=0 AND unit_role='head' GROUP BY span_id HAVING count(*)>1)")[0][0] == 0)
case("I8", "a shared row exists only in a unit with two or more content codes",
     q("SELECT count(*) FROM verse_lexical a WHERE a.deleted=0 AND a.surface_kind='shared' AND (SELECT count(*) FROM verse_lexical b WHERE b.span_id=a.span_id AND b.deleted=0 AND b.unit_role IN ('content_part','head'))<2")[0][0] == 0)
case("I9", "every live row is accounted: kinds sum to the live rows", sum(r[0] for r in q("SELECT count(*) FROM verse_lexical WHERE deleted=0 GROUP BY surface_kind")) == tot, tot)
pm = collections.Counter()
for r in q("SELECT unit_role, substr(morph_code,1,2) m FROM verse_lexical WHERE deleted=0 AND unit_role IN ('prefix','suffix')"):
    pm[(r["unit_role"], r["m"][:2] if r["m"] else "")] += 1
wrong = [k for k in pm if (k[0] == "prefix" and any(k[1].startswith(p) for p in rule["suffix_morph_classes"]))
         or (k[0] == "suffix" and any(k[1].startswith(p) for p in rule["prefix_morph_classes"]))]
case("I10", "no prefix carries a suffix morph class and no suffix a prefix class", not wrong, wrong)

# ── H the held rows ───────────────────────────────────────────────────────────────────────────────
held = q("SELECT id, strong, surface, unit_role, surface_kind FROM verse_lexical WHERE id IN (1377514, 1467529, 1242509)")
case("H1", "the three rows #2326 held keep their old surface and have their unit columns",
     sorted((r["strong"], r["surface"]) for r in held) == [("G1790", "fear"), ("H3321", "truth"), ("H7769", "help")] and all(r["unit_role"] and r["surface_kind"] for r in held),
     [tuple(r) for r in held])

# ── N nodes ───────────────────────────────────────────────────────────────────────────────────────
case("N1", "no node's surface differs from its occurrence's surface", q("SELECT count(*) FROM ib_node n JOIN verse_lexical v ON v.id=n.verse_lexical_id WHERE n.surface IS NOT v.surface")[0][0] == 0)
case("N2", "the node changes of the back-fill are in ib_observation_change with a reason (63)",
     q("SELECT count(*) FROM ib_observation_change WHERE run_id='DEVMODE-2381-VERSE-LEXICAL-UNITS-BACKFILL-20261107' AND reason LIKE '%#2381%'")[0][0] == 63)

# ── U the unit reader ─────────────────────────────────────────────────────────────────────────────
vid = q("SELECT id FROM verse WHERE osisId='Jer.23.12'")[0][0]
u = next(x for x in lexical.unit_view(conn, [vid]).values() if x["position"] == 3)
case("U1", "unit_view: Jer 23:12 position 3 reads 'to/for + smoothness + their + them', rendering 'slippery paths', head H2519",
     u["construct"] == "to/for + smoothness + their + them" and u["rendering"] == "slippery paths" and q("SELECT strong FROM verse_lexical WHERE id=?", u["head"])[0][0] == "H2519", u)
case("U2", "unit_view of no verse and of a verse with no unit is empty", lexical.unit_view(conn, []) == {} and lexical.unit_view(conn, [q("SELECT vl.verse_id FROM verse_lexical vl GROUP BY vl.verse_id HAVING max(vl.unit_size)=1 LIMIT 1")[0][0]]) == {})
allu = lexical.unit_view(conn, [r[0] for r in q("SELECT DISTINCT verse_id FROM verse_lexical WHERE deleted=0 AND verse_id%50=0")])
ordok = all([p["role"] for p in x["parts"]] == sorted([p["role"] for p in x["parts"]], key=lambda r: {"prefix": 0, "suffix": 2}.get(r, 1)) for x in allu.values())
case("U3", f"over {len(allu)} units of every 50th verse the parts are in word order (prefix, content, suffix)", ordok)

# ── W the reading sheet ───────────────────────────────────────────────────────────────────────────
sample = [r[0] for r in q("SELECT DISTINCT v.id FROM verse v JOIN verse_lexical vl ON vl.verse_id=v.id WHERE vl.deleted=0 AND v.id%97=0")]
items = [{"verse_id": i, "osis": q("SELECT osisId FROM verse WHERE id=?", i)[0][0], "verse": ""} for i in sample]
sheets = {}
for k in range(0, len(items), 200):
    sheets.update(reading._sheets(cfg, conn, items[k:k + 200]))
cov_ok = dup_ok = unit_ok = True
lines_before = groups_now = 0
for i in sample:
    ids_live = [r[0] for r in q("SELECT id FROM verse_lexical WHERE verse_id=? AND deleted=0", i)]
    occ = [o for g in sheets[i]["surfaces"] for o in g["occurrences"]]
    cov_ok &= sorted(occ) == sorted(ids_live)
    keys = [(g["strong"], g["surface"]) for g in sheets[i]["surfaces"]]
    dup_ok &= len(keys) == len(set(keys))
    unit_ok &= all(g["units"] for g in sheets[i]["surfaces"] for o in g["occurrences"][:1]
                   if q("SELECT unit_size FROM verse_lexical WHERE id=?", o)[0][0] > 1)
    lines_before += len(ids_live)
    groups_now += len(sheets[i]["surfaces"])
case("W1", f"{len(sample)} verses: every live occurrence id is in exactly one sheet group", cov_ok)
case("W2", "no two groups of a verse share (strong, surface)", dup_ok)
case("W3", "a group whose occurrence stands in a multi-code unit carries the unit (rendering, construct, parts)", unit_ok)
print(f"   sheet lines: {lines_before} code rows became {groups_now} groups in the sample ({round(100 * (1 - groups_now / lines_before), 1)}% fewer)")
head_groups = [g for i in sample for g in sheets[i]["surfaces"]
               if len(g["units"]) == 1 and q("SELECT unit_role FROM verse_lexical WHERE id=?", g["occurrences"][0])[0][0] == "head"]
case("W4", f"{len(head_groups)} single-unit head groups: the group holds every part's occurrence id (affix ids joined; same-key occurrences of other units may share the group)",
     head_groups and all({p["id"] for p in g["units"][0]["parts"]} <= set(g["occurrences"]) and g["surface_kind"] == "own" for g in head_groups),
     [(g["word"], g["occurrences"]) for g in head_groups if not {p["id"] for p in g["units"][0]["parts"]} <= set(g["occurrences"])][:3])
affix_lines = [g for i in sample for g in sheets[i]["surfaces"] if g["surface_kind"] == "gloss"]
case("W5", "an affix part that stays its own group (multi-content or affix-only unit) says it is part of the unit",
     all(any("part of the unit" in h for h in g["hint"]) for g in affix_lines), len(affix_lines))

# ── C the scope resolver's word selector ──────────────────────────────────────────────────────────
from iba.app.lib import versescope as vs  # noqa: E402

rs = vs.Resolver(cfg)
n_children = rs.word("children")
case("C1", "word 'children' no longer reaches the verses where the host's word sat on an affix row (Job 21:19 H9005 was one)",
     n_children == q("SELECT count(DISTINCT verse_id) FROM verse_lexical WHERE deleted=0 AND surface_kind<>'gloss' AND lower(trim(surface))='children'")[0][0], n_children)
rs2 = vs.Resolver(cfg)
n_and = rs2.word("and")
own_and = q("SELECT count(DISTINCT verse_id) FROM verse_lexical WHERE deleted=0 AND surface_kind<>'gloss' AND lower(trim(surface))='and'")[0][0]
all_and = q("SELECT count(DISTINCT verse_id) FROM verse_lexical WHERE deleted=0 AND lower(trim(surface))='and'")[0][0]
case("C2", "word 'and' enters through the ESV word only, not through 24,033 affix glosses", n_and == own_and and own_and < all_and, (n_and, own_and, all_and))
try:
    vs.Resolver(cfg).word("to/for")
    case("C3", "an affix gloss text that is no ESV word ('to/for') is refused as no surface", False, "not refused")
except vs.ScopeError:
    case("C3", "an affix gloss text that is no ESV word ('to/for') is refused as no surface", True)
terms = {r["s"] for r in q("SELECT lower(trim(surface)) s FROM surface_term WHERE deleted=0 AND origin='surface'")}
own_set = {r[0] for r in q("SELECT DISTINCT lower(trim(surface)) FROM verse_lexical WHERE deleted=0 AND surface_kind IN ('own','shared')")}
gloss_set = {r[0] for r in q("SELECT DISTINCT lower(trim(surface)) FROM verse_lexical WHERE deleted=0 AND surface_kind='gloss'")}
linked = {r[0] for r in q("SELECT DISTINCT lower(trim(t.surface)) FROM collection_link cl JOIN surface_term t ON t.id=cl.term_id WHERE cl.deleted=0")}
case("C4", "all 6,066 surface terms still have an own or shared row (none disappears); no collection holds an affix-gloss word",
     len(terms) == 6066 and not (terms - own_set) and not (linked & gloss_set), (len(terms), len(terms - own_set), sorted(linked & gloss_set)))

# ── E idempotence on a copy ───────────────────────────────────────────────────────────────────────
S = pathlib.Path(sys.argv[1]) / "t2381"
S.mkdir(parents=True, exist_ok=True)
copy = S / "iba-copy.db"
if copy.exists():
    copy.unlink()
dst = sqlite3.connect(copy)
sqlite3.connect(f"file:{LIVE}?mode=ro", uri=True).backup(dst)
dst.close()
cc = Cfg(copy)
v4 = [cc.conn.execute("SELECT id FROM verse WHERE osisId=?", (o,)).fetchone()[0] for o in ("Jer.23.12", "Isa.32.6", "Gen.43.27", "Job.21.19")]
c1 = lexical.build_for_verse_ids(cc.conn, v4)
case("E1", "rebuilding four verses on a copy writes nothing: 0 inserted, 0 updated, 0 removed", c1["inserted"] == 0 and c1["updated"] == 0 and c1["removed"] == 0, c1)
cc.conn.execute("UPDATE verse_lexical SET surface='children' WHERE verse_id=? AND strong='H9005'", (v4[3],))
c2 = lexical.build_for_verse_ids(cc.conn, v4)
case("E2", "an affix row carrying the host's word (the old fault) is corrected by the build itself", c2["updated"] == 1 and cc.conn.execute("SELECT surface FROM verse_lexical WHERE verse_id=? AND strong='H9005'", (v4[3],)).fetchone()[0] == "to/for", c2)
before_u = cc.conn.execute("SELECT updated_at FROM verse_lexical WHERE verse_id=? AND strong='H1121A'", (v4[3],)).fetchone()[0]
cc.conn.execute("UPDATE verse_lexical SET unit_role=NULL, surface_kind=NULL, unit_surface=NULL, unit_size=NULL WHERE verse_id=? AND strong='H1121A'", (v4[3],))
lexical.build_for_verse_ids(cc.conn, v4)
after_u = cc.conn.execute("SELECT updated_at, unit_role FROM verse_lexical WHERE verse_id=? AND strong='H1121A'", (v4[3],)).fetchone()
case("E3", "filling only the unit columns is not a correction: updated_at stays as it was", after_u[0] == before_u and after_u[1] == "head", (before_u, tuple(after_u)))
print(f"\n{sum(res)} of {len(res)} cases pass")
sys.exit(0 if all(res) else 1)
