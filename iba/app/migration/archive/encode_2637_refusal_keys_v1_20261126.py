"""encode_2637_refusal_keys_v1_20261126.py -- escalation #2637, plan v3 X4 (outputs/escalation/2637-build-plan-v3-20261126.md; design #2637 v10).

Researcher 2026-11-26: "the rules of the input and output packet must all be in the configs". On boast (#2620) several refusals named rules
the packet did not state (catalogue outputs/escalation/2637-known-failures-catalogue-v1-20261126.md; interventions A5, C1, C3, F2, G4, G5).
This migration:
  cfg_method_rule  PC-01..PC-07, the read contract: the rules of the answer form and of the command that no reading rule stated
  cfg_setting      layer.refusals: the registry of every refusal site of the reading package (lib/refusalrules.py), each keyed to its rule,
                   with the reads that can meet it, computed here from the source by refusalrules.scan and FUNC_READS
  cfg_setting      layer.read_types: each read's `rules` gains the keys of its refusals, so the packet prints their text
  cfg_utility      lib/refusalrules.py and this migration
Refuses (nothing written) where a site is keyed by no entry, or an entry keys no site. Written through configmaint.apply_logged. Named
snapshot before a live apply; after the live apply the file archives itself. Idempotent: a second apply writes nothing.
Usage: python iba/app/migration/encode_2637_refusal_keys_v1_20261126.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged, archive_migration  # noqa: E402
from iba.app.lib import refusalrules  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = ROOT / "iba" / "app" / "db" / "iba.db"
RUN_ID = "DEVMODE-2637-REFUSALKEYS-20261126"
MODULE = "encode_2637_refusal_keys_v1_20261126"
SRC = "escalation #2637, plan v3 X4 (outputs/escalation/2637-build-plan-v3-20261126.md)"
BY = "iba/app/lib/refusalrules.py (cfg_setting layer.refusals) with the recorders of the reading package"

RC = [  # the read contract: rules every read and record already enforced, never stated as rules
    ("PC-01 the-command-names-a-live-unit", "A read or record command names a live collection, a live subgroup of it where the read is by subgroup, and a step or item the layered reading knows. A command that names one that does not exist is refused and writes nothing."),
    ("PC-02 the-answer-is-the-packet-form", "An answer is the output form its read wrote: the `command` of that read; every entry an object, or a list, where the form has one; each field in its place with its type (a key unique in the answer, a text, a reason in words); each item answered once; and at least one entry where the form asks for entries. A file in another shape is refused whole and nothing is written."),
    ("PC-03 names-are-those-the-packet-offers", "Every ledger row, occurrence, observation, sense, node, verse and collection an answer names is one the packet offered for this unit, or a key the answer itself defines, and is live in the database. A name outside them is refused."),
    ("PC-04 values-from-the-allowed-lists", "Every coded value of an answer (kind, basis, item, part, role, route, mode, polarity, flag type, disposition, verdict, action, nature, stage, status) is one of the values the configuration allows for it (cfg_enum, cfg_setting layer.reading, reading.observation_items, validate.reading), as the packet lists them. Any other value is refused."),
    ("PC-05 the-unit-is-at-its-step", "A read or record runs only where the ledger has its unit at that step: the row open, or answered and not yet validated, and the steps before it closed (S1 before 1.1; the 2.1 rows before the sweep; the sweep before the evidence validation; its gate before 3.1; every subgroup through 3.1 before 3.2). Out of order it is refused, and the message names what comes first."),
    ("PC-06 within-the-configured-limits", "A read writes its packet within the time and size the configuration sets (cfg_setting layer.read_types: limits, package_max_chars, read_max_seconds). A read that would exceed them is refused, nothing is written, and the limit is named."),
    ("PC-07 the-config-the-code-needs-is-present", "The code of the reading runs only where the configuration it reads is in place (the settings, steps, items, natures, enums and rules it names). Where the code is ahead of the configuration, the command is refused and names what is missing."),
]

SCAN = {"modules": ["lib/layerreading", "lib/readcommands", "lib/layerinner", "lib/observationrecord", "lib/buildvalidate", "lib/validationactions",
                    "lib/recordingpass", "lib/collectionvalidate", "lib/layerloop", "lib/scanguard", "handlers/collectionbuild"],
        "only": {"lib/collectionvalidate": ["record"], "lib/layerloop": ["order_gate"],
                 "handlers/collectionbuild": ["layer_next", "read_words", "record_words", "read_senses", "record_senses", "read_enrichment",
                                              "record_enrichment", "read_structure", "record_structure", "_read_gate", "_record_gate",
                                              "sweep_superseded", "read_behaviours"]},
        "sinks": ["errors", "problems", "gaps", "missing"],
        "exceptions": ["Error", "Refused", "InvalidObservationText", "UnresolvedOccurrence", "Exceeded"],
        "calls": {"fail": 1},
        "returns": ["layerinner.check_row", "layerloop.order_gate", "buildvalidate.old_fate_ok"],
        "headings": ["the file is refused, nothing written; problems:", "the answer is refused whole, nothing written:",
                     "step {} of {} cannot be opened:"]}
EXEMPT = [
    {"site": "recordingpass.record_subgroups", "reason": "the cluster subgrouping of the older pipeline (#1690); no read of the layered reading calls it"},
    {"site": "recordingpass._window_for", "reason": "the question-catalogue window of the older recording pass; no read of the layered reading calls it"},
]

ALL = ["words", "senses", "enrichment", "structure", "sweep", "evidence", "elements", "behaviours"]
STAGE1 = ["words", "senses", "enrichment", "structure"]
INNER = ["elements", "behaviours"]
FUNC_READS = {  # module.function -> the reads whose commands reach it; a module name alone is the default for its functions
    "readcommands": ALL,
    "readcommands.read_words": ["words"], "readcommands.record_words": ["words"],
    "readcommands.read_senses": ["senses"], "readcommands.record_senses": ["senses"],
    "readcommands.read_enrichment": ["enrichment"], "readcommands.record_enrichment": ["enrichment"],
    "readcommands.read_structure": ["structure"], "readcommands.record_structure": ["structure"],
    "readcommands.read_sweep": ["sweep"], "readcommands.record_sweep": ["sweep"],
    "readcommands.read_evidence": ["evidence"], "readcommands.record_evidence": ["evidence"],
    "readcommands.read_elements": ["elements"], "readcommands.record_elements": ["elements"],
    "readcommands.read_behaviours": ["behaviours"], "readcommands.record_behaviours": ["behaviours"],
    "layerreading": ALL,
    "layerreading.record": STAGE1, "layerreading._text_rules": STAGE1, "layerreading.settle_nodes": STAGE1,
    "layerreading.sweep_superseded": ["sweep"],
    "layerinner": INNER,
    "observationrecord": ALL,
    "observationrecord.check": INNER, "observationrecord.check_item_parts": INNER,
    "buildvalidate": ALL, "buildvalidate.sweep": ["sweep"],
    "validationactions": ALL,
    "recordingpass": ALL,
    "collectionvalidate": ["evidence"], "layerloop": ALL, "scanguard": ALL,
    "collectionbuild": ALL,
    "collectionbuild.read_words": ["words"], "collectionbuild.record_words": ["words"],
    "collectionbuild.read_senses": ["senses"], "collectionbuild.record_senses": ["senses"],
    "collectionbuild.read_enrichment": ["enrichment"], "collectionbuild.record_enrichment": ["enrichment"],
    "collectionbuild.read_structure": ["structure"], "collectionbuild.record_structure": ["structure"],
    "collectionbuild.read_behaviours": ["behaviours"], "collectionbuild.sweep_superseded": ["sweep"],
}

# (key, match[, site]): the first entry whose match a refusal line holds keys it. Specific before general.
ENTRIES = [
    # PC-07 the configuration the code needs
    ("PC-07", "cfg_setting layer.reading is missing"), ("PC-07", "cfg_setting layer.scan"), ("PC-07", "layer.reading step "),
    ("PC-07", "(apply iba/app/migration/archive/"), ("PC-07", "the code is ahead of the config"), ("PC-07", "have no nature in cfg_setting layer.reading"),
    ("PC-07", "the read names rule(s) not active"), ("PC-07", "is empty: run install_nature"), ("PC-07", "are not ib_observation.tag values"),
    # PC-06 limits
    ("PC-06", " took more than "), ("PC-06", " s, more than "), ("PC-06", " characters, more than "),
    # PC-01 the command
    ("PC-01", "is not a step of the layered reading"), ("PC-01", "is not a live subgroup of"), ("PC-01", "no live collection"),
    ("PC-01", "has no live subgroup"), ("PC-01", "-Item must be one of"),
    # PC-05 the unit at its step
    ("PC-05", "only an open or an unvalidated row is recorded"), ("PC-05", " row is answered by its own command"),
    ("PC-05", "comes after its 2.1 rows"), ("PC-05", "the evidence validation of "), ("PC-05", "has no row for"),
    ("PC-05", "the sweep waits for every current subgroup"), ("PC-05", "the sweep left "),
    ("PC-05", "has no open row"), ("PC-05", "is open; other items are"), ("PC-05", "its group is retired or missing"),
    ("PC-05", "has no sweep row"), ("PC-05", "has no evidence-validation row"),
    ("LR-01", "is not closed (every row answered"),
    # RW-13 / RS-04 older and earlier observations answered
    ("RW-13", "are still open in the ledger"), ("RW-13", "have no answer in fill.older"),
    ("RS-04", "unmarked older observation(s) have no answer"), ("RS-04", "older observation(s) are still unmarked"),
    ("RS-04", "earlier reading(s) of the subg"), ("RS-04", " needs its reason ("),
    # PC-02 the answer form
    ("PC-02", "answer (its `command` must be"), ("PC-02", "a node is an object"), ("PC-02", "a finding is an object"),
    ("PC-02", "parts is an object with"), ("PC-02", "is a list of {observation, action, reason"), ("PC-02", "the answer holds no "),
    ("PC-02", "a unique key is required"), ("PC-02", "is a short name unique in the row"), ("PC-02", "text is required"),
    ("PC-02", "named twice"), ("PC-02", "answered twice"), ("PC-02", "a read_back entry is "), ("PC-02", " is {observation id: reason}"),
    ("PC-02", "`traced` is the id of an observation"), ("PC-02", "a node names the occurrence id of the word"),
    ("PC-02", "a node names the word (strong)"), ("PC-02", "an `existing` entry names a live observation and an action"),
    ("PC-02", "the row is answered by findings"), ("PC-02", "(fill.senses): at least one"), ("PC-02", "a true observation takes no action"),
    # PC-03 names the packet offers
    ("PC-03", "nothing written:\n  ledger "), ("PC-03", "not a ledger row of"), ("PC-03", "is not a word of subgroup"),
    ("PC-03", "is not a 2.1 row of subgroup"), ("PC-03", "is not an occurrence this row may name"),
    ("PC-03", "is neither a live observation nor a finding key"), ("PC-03", "are not observations this row may rest on"),
    ("PC-03", "occurrences that are not occurrences of"), ("PC-03", "is not an older live observation on the occurrences of this row"),
    ("PC-03", "not in the unmarked observations of this subgroup"), ("PC-03", "is not an open old observation of this subgroup"),
    ("PC-03", "is not an unmarked older observation of"), ("PC-03", "not an evidence observation of"), ("PC-03", "is not a 1.1 sense of subgroup"),
    ("PC-03", "which is not a B1 observation of subgroup"), ("PC-03", "adopt names a live observation"), ("PC-03", "a deferral names a live collection"),
    ("PC-03", "has no matching live verse_lexical row"), ("PC-03", "both must be different live observations"),
    ("PC-03", "is not a live occurrence of"), ("PC-03", " is not an occurrence of "), ("PC-03", "is not a live observation"),
    ("PC-03", "is not a live node"), ("PC-03", "does not exist"), ("PC-03", " is not a ", "validationactions._obs"),
    # PC-04 allowed values
    ("PC-04", "kind must be one of"), ("PC-04", "basis must be one of"), ("PC-04", "role must be one of"), ("PC-04", "route must be one of"),
    ("PC-04", "tag must be one of"), ("PC-04", "stage must be one of"), ("PC-04", "nature must be one of"), ("PC-04", "parts.item is one of"),
    ("PC-04", "are not among"), ("PC-04", "is written as a finding of the kind"), ("PC-04", "has the basis"), ("PC-04", "gives parts.polarity"),
    ("PC-04", "gives parts.mode"), ("PC-04", "gives parts.flag_type"), ("PC-04", "disposition must be observed"),
    ("PC-04", "verdict is true or repair"), ("PC-04", "the sweep answers with one of"), ("PC-04", "is not a node role"),
    ("PC-04", "cannot be modified (allowed:"), ("PC-04", "not in live cfg_enum ib_observation"), ("PC-04", ", the item takes "),
    # RW-03 one observation per finding
    ("RW-03", "is already live as observation"), ("RW-03", "the same text as"), ("RW-03", "an existing finding takes nodes only"),
    ("RW-03", "a merge is for the same description"),
    # RW-04 concise, tied to the verse, never restating it
    ("RW-04", "restates the verse"), ("RW-04", "the observation text is missing or under"), ("RW-04", "is a bare negation with no actual content"),
    # RG-06 route
    ("RG-06", "carries its route"), ("RG-06", "this item takes no route"), ("RG-06", "is held only on a party or link finding"),
    # RG-04 qualifier
    ("RG-04", "a qualification finding applies to its qualifier"),
    # DA-02 a node carries the collection of its surface
    ("DA-02", "is not a word of a collection"), ("DA-02", "is in no collection: name the occurrence it supports"),
    ("DA-02", "word node(s) carry no collection"), ("DA-02", "names collection "), ("DA-02", "belongs to collection"),
    # RW-12 node columns at creation
    ("RW-12", "morph_code is empty but"), ("RW-12", ") has no "),
    # LR-03 none
    ("LR-03", "cannot be recorded as none"), ("LR-03", "none needs its reason"), ("LR-03", "`disposition` is observed (with findings) or none"),
    # IB: stage 4
    ("IB-02", "are outside the observations the finding rests on"), ("IB-02", "a finding rests on observations"),
    ("IB-04", "names an observation this row must take up"), ("IB-08", "the collection shows at least one behaviour"),
    ("IB-07", "is not marked evidence: an inner-being observation traces to evidence"), ("IB-07", "an observation does not trace itself"),
    ("IB-03", "names its grounds in the words of the verse (parts.grounds"), ("IB-03", "at least one node (what the finding applies to)"),
    ("IB-03", "only a term finding applies to a word with no verse"),
    # LR-02 nodes from the data, coverage, grounds, tied to verses
    ("LR-02", "the text names none of them"), ("LR-02", "names its grounds in the words of the verse"), ("LR-02", "are not words of the lexicon entries"),
    ("LR-02", "are not words of the verses"), ("LR-02", "the data holds no occurrence for this aspect"), ("LR-02", "names the occurrences it is about"),
    ("LR-02", "names no occurrence (fill occurrences"), ("LR-02", "are already in another sense"), ("LR-02", "are in no sense"),
    ("LR-02", "is carried by no sense and none of its occurrences"), ("LR-02", "is already carried by sense"), ("LR-02", "has no enrichment (one enrichment"),
    ("LR-02", "is already enriched by enrichment"), ("LR-02", "no occurrence to adopt for"),
    # VA: validation actions
    ("VA-02", "why says, in words,"), ("VA-02", "a repair names the actions"),
    ("VA-03", "name the carrying observations"), ("VA-03", "the mapping is stated in words"), ("VA-03", "occurrence(s) are on no node of"),
    ("VA-03", "not carried needs its reason"),
    ("VA-04", "the reason says why it is neither evidence nor inner being"), ("VA-04", "only an observation that is neither is deleted here"),
    ("VA-04", "repair those traces first"), ("VA-04", "node(s) outside this subgroup"),
    ("VA-05", "the reason says, in words, what the observation states"), ("VA-05", "is an inner-being finding (its nodes carry an inner-being role)"),
    # RW-01 a change only by a reading, with its reason
    ("RW-01", "needs its reason, in words"), ("RW-01", "say in words what was checked"), ("RW-01", "say what it states that the existing record does not"),
    ("RW-01", "state the finding the collection is to close"), ("RW-01", "say in words which words it relies on"),
    ("RW-01", "say in words why the word supports no finding"), ("RW-01", "is the last word node of observation"),
    ("RW-01", "already holds that occurrence: drop the node instead"), ("RW-01", "its occurrence is on no live node of"),
    ("RW-09", "adopt needs its reason in words"),
    # the answers to older observations (buildvalidate._answer)
    ("PC-04", "action is one of"), ("PC-04", "names its marker, nature one of"), ("PC-03", "merge names a live observation to keep"),
    ("PC-05", "carry names a LATER step of"), ("RW-01", "carry gives its reason in words"), ("PC-03", "defer names a live collection"),
    ("VA-05", "a deferred observation is marked now"),
    # found by the historical corpus (test K11): the loop order, the stage-4 coverage and roles, the commands' own checks, the scan guard
    ("PC-05", "the loop is for one subgroup at a time"), ("IB-04", "is neither rested on by a finding nor in"),
    ("RG-03", "every node it holds bears on an act"), ("PC-02", "unknown parameter(s)"), ("RW-14", "the statement used more than"),
    ("PC-01", "cannot read "), ("PC-01", " are required"), ("PC-01", " is required"), ("PC-07", " is missing"),
    ("RW-13", "its fate is not recorded"), ("RW-13", "is not in the change log of observation"), ("RW-13", "the change log does not show it"),
    ("PC-02", "a sheet is an object"), ("PC-04", "is not an action of the validation"), ("PC-02", "missing parameter(s)"),
    ("IB-04", "is both rested on by a finding and in"), ("IB-04", "is part of this match and no finding traces it"),
    # LayerCheck of a stage 4 row (layerinner.check_row): the row re-derived from the tables
    ("LR-03", "recorded as none without a permitted reason"), ("PC-05", "the data no longer demands this aspect"),
    ("IB-06", "its observations are missing or withdrawn"), ("IB-06", "records are not readable"), ("IB-06", "which this row does not use"),
    ("IB-06", " has stage "), ("IB-06", "has no node on an occurrence"), ("IB-02", "rests on no observation (a traced node on each)"),
    ("IB-02", "which this row may not rest on"), ("PC-03", "which this row may not name"), ("RG-03", "has a node with no valid stage 4 role"),
    ("DA-02", "has a node with no collection"), ("IB-02", "outside the observations it rests on"), ("IB-02", "gives no reason in words"),
    ("IB-04", "without a reason in words"), ("IB-04", "are neither rested on by a finding nor declared"),
    ("IB-04", "declares an observation this row does not take up"), ("IB-04", "of the match are not traced"),
    ("IB-08", "no behaviour: the collection row needs a flag finding"),
    # the 3.3 gate and the quote check
    ("PC-05", "partner collection "), ("DA-02", "the nodes do not carry the collections"), ("RW-04", "is not the ESV's wording"),
]


def registry(root):
    """The registry the migration writes: every entry with the reads of the sites it keys. Raises on a site no entry keys or an entry that keys
    no site, so the config never holds a partial registry."""
    reg = {"scan": SCAN, "exempt": EXEMPT, "entries": [{"key": e[0], "match": e[1], **({"site": e[2]} if len(e) > 2 else {})} for e in ENTRIES]}
    sites = refusalrules.scan(root, reg)
    reads = {i: set() for i in range(len(ENTRIES))}
    unkeyed = []
    for s in sites:
        hit = next((i for i, e in enumerate(reg["entries"]) if (not e.get("site") or e["site"] == s["site"]) and e["match"] in s["template"]), None)
        if hit is None:
            if not s["wrapper"]:
                unkeyed.append(s)
            continue
        mod = s["site"].split(".")[0]
        reads[hit] |= set(FUNC_READS.get(s["site"], FUNC_READS[mod]))
    dead = [reg["entries"][i] for i, r in reads.items() if not r]
    if unkeyed or dead:
        raise SystemExit("refused, nothing written:\n" + "\n".join(f"  no entry keys {s['site']}:{s['line']} {s['template'][:100]!r}" for s in unkeyed)
                         + "".join(f"\n  entry keys no site: {e}" for e in dead))
    for i, e in enumerate(reg["entries"]):
        e["reads"] = [r for r in ALL if r in reads[i]]
    return reg, len(sites)


def plan(conn):
    ops = []
    have = {r[0].split(" ")[0] for r in conn.execute("SELECT rule_key FROM cfg_method_rule")}
    ordinal = conn.execute("SELECT coalesce(max(ordinal),0) FROM cfg_method_rule WHERE step='collection.layer_record'").fetchone()[0]
    for key, text in RC:
        if key.split(" ")[0] not in have:
            ordinal += 1
            ops.append(("cfg_method_rule", "insert", {}, {"step": "collection.layer_record", "rule_key": key, "rule_text": text, "source_doc": SRC,
                                                          "enforced_by": BY, "ordinal": ordinal, "active": 1}))
    reg, n_sites = registry(ROOT)
    value = json.dumps(reg, ensure_ascii=False)
    use = ("#2637 X4: every refusal of the reading package keyed to its rule (lib/refusalrules.py): scan (where the sites are read from), entries "
           "{key, match, reads, site?} (the first entry whose match a refusal line holds keys it; reads: the reads whose packets print it), exempt "
           "(functions not on the reading path, with the reason). Held to the source by iba/app/tools/temp_2637_refusal_keys_test_run.py.")
    cur = conn.execute("SELECT value FROM cfg_setting WHERE key=?", (refusalrules.SETTING,)).fetchone()
    if cur is None:     # written once: a later migration that extends the registry (encode_2637_check_answer_v1_20261126) is never undone by a re-run
        ops.append(("cfg_setting", "insert", {}, {"key": refusalrules.SETTING, "value": value, "use": use, "module": "layer", "inactive": 0}))
    rt = json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='layer.read_types'").fetchone()[0])
    changed = False
    for read in ALL:
        need = sorted({e["key"] for e in reg["entries"] if read in e["reads"]} - {k for k in rt[read]["rules"]})
        if need:
            rt[read]["rules"] = rt[read]["rules"] + need
            changed = True
    if changed:
        ops.append(("cfg_setting", "update", {"key": "layer.read_types"}, {"value": json.dumps(rt, ensure_ascii=False)}))
    for mod, path, purpose, inactive, exempt, reason in [
            ("refusalrules", "iba/app/lib/refusalrules.py", "#2637 X4: the registry of refusals keyed to rules (cfg_setting layer.refusals): key a refusal line, list a read's refusals, scan the sites", 0, 0, None),
            (MODULE, f"iba/app/migration/{MODULE}.py", "migration of #2637 X4: the read contract rules PC-01..07, cfg_setting layer.refusals, the refusal keys in each read's rules", 1, 1, "a one-off migration; its values are the config it writes")]:
        if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (mod,)).fetchone():
            ops.append(("cfg_utility", "insert", {}, {"module": mod, "file_path": path, "purpose": purpose, "inactive": inactive, "config_exempt": exempt,
                                                      "config_exempt_reason": reason, "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops, n_sites


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true")
    a = ap.parse_args()
    live = pathlib.Path(a.db).resolve() == DEFAULT_DB.resolve()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops, n_sites = plan(conn)
    if a.dry_run or not ops:
        print(("DRY RUN: " if a.dry_run else "already applied: ") + f"{len(ops)} write(s); {n_sites} refusal sites keyed")
        for t, op, where, set_ in ops:
            print(" ", t, op, where or {k: str(set_[k])[:60] for k in list(set_)[:3]})
        return 0
    if live and not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2637-refusalkeys-apply', named=True)}")
    try:
        conn.execute("SAVEPOINT rel")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE rel")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO rel")
        conn.execute("RELEASE rel")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} write(s); {n_sites} refusal sites keyed")
    if live:
        new = archive_migration(conn, RUN_ID, __file__)
        conn.commit()
        print(f"archived: {new}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
