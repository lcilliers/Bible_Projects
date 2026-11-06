"""surfacecyclemap -- the generated sections of the config report that describe the surface cycle and the AI use (escalation #2361, stage 6).

Both sections are built from the registers at the moment the report is generated, so they cannot drift from the app:
  surface_cycle_map  the five modules of the cycle and the AI control: work package, entry script, steps with what each does, the tables each step
                     may write (cfg_write_grant), the settings modules that govern them (cfg_setting), and the state of the study tables
                     (counts by state read from the tables)
  ai_use_map         the models by role (cfg_ai_model), the prompts by key with the active version (cfg_ai_prompt), and every module and step that has
                     called the AI (ai_call): role, model, prompt version(s), outcomes, calls, seconds
`q` is the report's query function (sql, params) -> rows with named columns.
"""
from __future__ import annotations

# the cycle in the order it is run: (work package, module label, settings modules that govern it)
CYCLE = [
    ("surface-group", "1 of 5  group: the group of each surface, and its correction from the derived words", ["group"]),
    ("surface-structure", "2 of 5  structure: a surface matched to a base by the shape of the word", ["structure"]),
    ("surface-base", "3 of 5  AI base: the base of the words the structure leaves unmatched (Ask is the table route)", ["surface_judge", "ollama"]),
    ("surface-resolve", "4 of 5  resolve: the base chosen from the evidence", ["resolve"]),
    ("collection-build", "5 of 5  collections: members decided from the AI judgements; seed and ask", ["collection"]),
    ("ai-control", "AI control: models, prompts, calls, replay, compare", ["ai"]),
]
STATE_QUERIES = [
    ("surface_term by base_state", "SELECT base_state AS k, count(*) AS n FROM surface_term WHERE deleted=0 GROUP BY 1 ORDER BY 2 DESC"),
    ("surface_term by group_state", "SELECT group_state AS k, count(*) AS n FROM surface_term WHERE deleted=0 GROUP BY 1 ORDER BY 2 DESC"),
    ("collection_link by tier", "SELECT tier AS k, count(*) AS n FROM collection_link WHERE deleted=0 GROUP BY 1 ORDER BY 2 DESC"),
    ("surface_flag by kind (open)", "SELECT kind AS k, count(*) AS n FROM surface_flag WHERE status='open' AND deleted=0 GROUP BY 1 ORDER BY 2 DESC"),
]


def _tbl(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    out += ["| " + " | ".join("" if c is None else str(c).replace("|", "/").replace("\n", " ") for c in r) + " |" for r in rows]
    return out if rows else out + ["| " + " | ".join("_(none)_" for _ in headers) + " |"]


def surface_cycle_map(q) -> list[str]:
    L = ["Generated from `cfg_work_package`, `cfg_step`, `cfg_write_grant`, `cfg_setting` and the study tables. A normal pass runs the modules in this order; "
         "each is repeatable alone and reads tables only (no working file is an input). Everything the AI says is inferential until the researcher confirms it (B:4).", ""]
    for wp, label, mods in CYCLE:
        w = q("SELECT ps_script FROM cfg_work_package WHERE name=? AND inactive=0", (wp,))
        if not w:
            continue
        L += [f"**{label}** · work package `{wp}` · script `{w[0]['ps_script']}`", ""]
        steps = q("SELECT step, kind, does FROM cfg_step WHERE work_package=? AND inactive=0 ORDER BY ordinal", (wp,))
        rows = []
        for s in steps:
            grants = ", ".join(r["table_name"] for r in q("SELECT table_name FROM cfg_write_grant WHERE writer=? AND inactive=0 ORDER BY table_name", (s["step"],)))
            rows.append([s["step"], s["kind"], s["does"].split(" -- see ")[0], grants or "(reads only)"])
        L += _tbl(["step", "kind", "what it does", "may write"], rows)
        sets = []
        for m in mods:
            sets += [f"`{r['key']}`" for r in q("SELECT key FROM cfg_setting WHERE module=? AND inactive=0 ORDER BY key", (m,))]
        L += ["", "settings: " + (", ".join(sets) if sets else "(none)"), ""]
    L += ["**State of the study tables** (counts at the moment of this report)", ""]
    for title, sql in STATE_QUERIES:
        try:
            rows = q(sql)
        except Exception:     # a table not yet made
            continue
        L += [f"{title}: " + ", ".join(f"{r['k']} {r['n']}" for r in rows), ""]
    return L


def ai_use_map(q) -> list[str]:
    L = ["Generated from `cfg_ai_model`, `cfg_ai_prompt` and `ai_call`. Every call goes through `lib/aiclient.py`: the model is the active one of the role, the prompt the "
         "active version of its key, the options are within `ai.allowed_options`. Which prompt worked best is read from the calls (`Ai-Control.ps1 -Action Compare`), never stored as a claim.", ""]
    L += ["**Models by role**", ""]
    L += _tbl(["role", "model", "status", "purpose"], [[r["role"], r["name"], r["status"], r["purpose"]] for r in
                                                         q("SELECT role, name, status, purpose FROM cfg_ai_model WHERE inactive=0 ORDER BY role, name")])
    L += ["", "**Prompts by key**", ""]
    L += _tbl(["prompt key", "role", "active version", "versions", "purpose"], [
        [r["prompt_key"], r["role"], ("v" + str(r["act"])) if r["act"] else "(none)", r["n"], r["purpose"]] for r in
        q("SELECT prompt_key, role, MAX(CASE WHEN status='active' THEN version END) AS act, count(*) AS n, MAX(purpose) AS purpose FROM cfg_ai_prompt GROUP BY 1,2 ORDER BY 1")])
    L += ["", "**Where the AI has been used** (module, step; calls by outcome)", ""]
    rows = q("SELECT c.module, c.step, c.role, m.name AS model, GROUP_CONCAT(DISTINCT p.prompt_key || ' v' || p.version) AS prompts, "
             "SUM(c.outcome='answered') AS answered, SUM(c.outcome='refused') AS refused, SUM(c.outcome='failed') AS failed, SUM(c.outcome='halted') AS halted, "
             "round(avg(c.secs),1) AS secs FROM ai_call c JOIN cfg_ai_model m ON m.id=c.model_id LEFT JOIN cfg_ai_prompt p ON p.id=c.prompt_id "
             "WHERE c.deleted=0 GROUP BY c.module, c.step, c.role, m.name ORDER BY c.module, c.step")
    L += _tbl(["module", "step", "role", "model", "prompts", "answered", "refused", "failed", "halted", "avg secs"],
              [[r["module"], r["step"], r["role"], r["model"], r["prompts"], r["answered"], r["refused"], r["failed"], r["halted"], r["secs"]] for r in rows])
    steps = q("SELECT step, work_package FROM cfg_step WHERE inactive=0 AND handler IN ('iba.app.handlers.surfacebase:ask','iba.app.handlers.surfacegroup:judge',"
              "'iba.app.handlers.collectionbuild:seed','iba.app.handlers.collectionbuild:ask','iba.app.handlers.ai:replay') ORDER BY step")
    L += ["", "**Steps that call the AI** (all through the client): " + ", ".join(f"`{s['step']}`" for s in steps), ""]
    return L
