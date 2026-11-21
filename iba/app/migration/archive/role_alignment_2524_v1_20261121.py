"""role_alignment_2524_v1_20261121.py -- escalation #2524 (role in the programme prose and the glossary).

The researcher, 2026-11-21 (verbatim): "standalone - it is absolutely part of roles so properly define
it and fix the configs ... that is wrong" and, on rule 73, "if the config must be active to enforce the
role as per discussion, then reactivate it."

Config rows brought to one definition of role:
  - behaviour rule 73 (read-verse-by-role-of-each-mcode-word): rewritten to the current terms
    (collections, surfaces, nodes; no strand or M-code) and set active; delivered at Reading.ps1 and
    Engagement.ps1;
  - standalone defined as a role in rule 130, cfg_column ib_node.role, cfg_setting reading.node_roles,
    method rules RG-03 and RS-05, and the glossary_role pointer.
Every write through configmaint.apply_logged(). Idempotent.

Usage:
    python iba/app/migration/role_alignment_2524_v1_20261121.py [--db PATH]
"""
import argparse
import json
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2524-ROLE-ALIGNMENT-20261121"

OLD_STANDALONE = ("standalone records that the word was recognised and has no inner-being role on any "
                  "other surface of the verse")
NEW_STANDALONE = ("standalone records that the word was read in this verse and holds nothing for the "
                  "inner being: it is neither a characteristic, nor a qualifier of one, nor an object, "
                  "relational target or enactment of one, and binds to nothing (a function word, or a "
                  "word no characteristic in the verse reaches); it is a judgement of the reading and not "
                  "an absence of one")

RULE_73 = (
    "A word's role in a finding is judged by reading the verse, for each occurrence, against the main "
    "inner-being operation the verse carries. It is never taken from a cluster tag, from the collection "
    "of the surface, from the word's other occurrences or from the part it usually plays. The roles are "
    "those of cfg_setting reading.node_roles: characteristic; qualifier, with what it gives the "
    "characteristic stated; object, relational_target and enactment, which bear on the finding; "
    "standalone, the word was read in the verse and holds nothing for the inner being (it binds to "
    "nothing, and is a role, not an absence); and lexical, read lexically with its inner-being role not "
    "assessed. The same word can hold different roles in different verses: each role is its own "
    "observation, applied by its nodes to the verses where it holds, and the surface's group is not "
    "changed by the difference. A qualifier has no account of its own from that verse: it is bound to "
    "the characteristic it qualifies and carried as a face of the word and as an interrelationship; a "
    "word that only qualifies, or has no inner-being role, is not analysed by itself. A party's role "
    "is an observation, not a field. Reading goes outward from the verse and not inward from the "
    "item's question: first write down everything the verse carries (a verse often has two or three "
    "significances, and none is dropped because it was not the one asked about), then answer the "
    "item's question last. For every word that names an inner or bodily act, look at the original: the "
    "root's range, and whether the English adds or hides something. A discovery outside the verse is "
    "recorded separately and not resolved inline. Never close an item or a verse on 'not X': a role "
    "label is never a verdict, and the close records what the verse is. Glossary: role (prose_section "
    "1066); guide: Workflow/Instructions/wa-verse-reading-by-role-guide-v2-20261019.md."
)
RULE_73_ENFORCED_BY = ("Not mechanically enforced as a whole: delivered at the first use of Reading.ps1 and "
                       "Engagement.ps1 and through behaviour rules 130 and 131; Node-Check.ps1 checks that a "
                       "node has a role (N-no-role) and an observation a node of a relevant role (O-no-role-node).")

SETTING_USE = ("the roles a node may take, in sets: relevant (the characteristic, or a qualifier of it with "
               "what it gives stated), bears_on (the object, relational target or enactment of a relevant "
               "act), recognised (standalone: the word was read in the verse and holds nothing for the "
               "inner being; it binds to nothing) and lexical (a node of a stage 1 observation: read "
               "lexically, its inner-being role not assessed). The word's role in the finding, judged "
               "from the verse (behaviour rule 73).")
RG03 = ("Find the main inner-being operation, and give every word that bears on it its role in this "
        "finding (cfg_setting reading.node_roles): characteristic, qualifier and what it gives the "
        "characteristic, object or content, relational target, or enactment. A word read in the verse "
        "that holds nothing for the inner being is standalone. The role comes from this verse, never "
        "from the cluster tag. Where a standalone word proves to qualify a characteristic, it is a "
        "qualifier of it.")
RS05 = ("A surface with no inner-being role in a verse has no observation of its own. A word read in the "
        "verse that holds nothing for the inner being has the role standalone, which is a role and not "
        "an absence; where it could be a qualifier it is read as the qualifier of the characteristic "
        "it serves.")
CONCEPT = ("The role of a word in a finding, judged by reading the verse for each occurrence: "
           "characteristic, qualifier, object, relational_target, enactment, standalone, lexical "
           "(cfg_enum observation_role; cfg_setting reading.node_roles). Programme glossary entry 'role' "
           "(prose_section 1066, contentious glossary): a draft until the researcher settles it.")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    n = 0

    def put(table, where, set_):
        nonlocal n
        cols = list(set_)
        row = conn.execute(f'SELECT {",".join(cols)} FROM {table} WHERE ' + " AND ".join(f"{k}=?" for k in where),
                           list(where.values())).fetchone()
        if row is not None and list(row) == [set_[c] for c in cols]:
            return
        apply_logged(conn, RUN_ID, table, "update", where, set_)
        n += 1

    with conn:
        # rule 73: current text, active, delivered where the role is judged
        put("cfg_behaviour_rule", {"id": 73}, {"rule_text": RULE_73, "enforced_by": RULE_73_ENFORCED_BY, "active": 1})
        for tool in ("Reading.ps1", "Engagement.ps1"):
            if not conn.execute("SELECT 1 FROM cfg_rule_scope WHERE rule_ref='B:73' AND scope_kind='ps' AND scope_value=?",
                                (tool,)).fetchone():
                apply_logged(conn, RUN_ID, "cfg_rule_scope", "insert", {},
                             {"rule_ref": "B:73", "scope_kind": "ps", "scope_value": tool, "inactive": 0})
                n += 1
        # standalone, defined
        for table, where, col in (("cfg_behaviour_rule", {"id": 130}, "rule_text"),
                                  ("cfg_column", {"database": "iba", "table_name": "ib_node", "name": "role"}, "use")):
            cur = conn.execute(f'SELECT {col} FROM {table} WHERE ' + " AND ".join(f"{k}=?" for k in where),
                               list(where.values())).fetchone()[0]
            if OLD_STANDALONE in cur:
                put(table, where, {col: cur.replace(OLD_STANDALONE, NEW_STANDALONE)})
        put("cfg_setting", {"key": "reading.node_roles"}, {"use": SETTING_USE})
        put("cfg_method_rule", {"id": 145}, {"rule_text": RG03})
        put("cfg_method_rule", {"id": 223}, {"rule_text": RS05})
        put("cfg_prose_concept", {"concept_key": "glossary_role"}, {"description": CONCEPT})
    print(f"{n} audited cfg_* write(s) (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
