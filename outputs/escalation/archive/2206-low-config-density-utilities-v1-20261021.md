# 2206 — Low-config-density utilities: one decision each (option 2b)

Escalation: #2206, option 2b, approved by the researcher on 2026-10-21. The check
`cfgquality.find_utility_config_density` (`iba/app/lib/cfgquality.py`) lists every active,
non-exempt `cfg_utility` module whose file has no `Cfg` method call (`.setting()`, `.enum()`, ...).
It enforces `governance.utility.config`. Today it lists **12**, not the 10 stated in the v2 options
file: that figure came from the stale #2197.

Once you have decided each row:

- an exempt is written with `cfg_utility.config_exempt=1` and the reason;
- "make it read config" becomes its own task;
- the check then lists only new cases.

## Facts per utility

Measured 2026-10-21 from the files and `cfg_utility`:

- **raw cfg refs:** occurrences of `cfg_setting`/`cfg_enum` in the file. These are reads by SQL,
  which the check does not see.
- **file literals:** quoted file names in the file.

| # | Utility | File | Lines | Raw cfg refs | File literals | What it is (cfg_utility.purpose, shortened) | Claude's reading | Decision |
|---|---|---|---|---|---|---|---|---|
| 1 | scripts_apply_session_patch | scripts/apply_session_patch.py | 2348 | 0 | 1 | Its purpose text says INACTIVE since 2026-08-18 (#729), yet `cfg_utility.inactive` = 0 | Incoherent row: set inactive (the 2026-08-18 ruling) rather than exempt |  |
| 2 | scripts_backup_db_to_nas | scripts/backup_db_to_nas.py | 308 | 0 | 2 | Marked NON-COMPLIANT (#648): hardcoded constants | A real gap, already known: move the constants to cfg_setting |  |
| 3 | handlers_catalogue | iba/app/handlers/catalogue.py | 38 | 0 | 0 | Thin dispatcher adapter over cataloguewrite.py | Exempt: it passes through, and its callee holds the rules |  |
| 4 | lexicalenrich | iba/app/lib/lexicalenrich.py | 294 | 0 | 0 | Stage 1 layer 2 engine, JSON-payload driven (#1383) | Exempt: driven by its payload (inferential: not checked line by line) |  |
| 5 | lexicalscope | iba/app/lib/lexicalscope.py | 130 | 0 | 0 | Selector-to-verse-id resolution for lexical.run (#1549) | Exempt: a pure resolver over data tables |  |
| 6 | clusterfamilyscan | iba/app/lib/clusterfamilyscan.py | 134 | 0 | 0 | Candidate generation from strong_related (#1598) | Check for literal thresholds before exempting |  |
| 7 | clusterstatus | iba/app/lib/clusterstatus.py | 293 | 4 | 0 | cluster.status lifecycle transitions (#1697) | Reads config by SQL: a false finding of the check |  |
| 8 | recordingpass | iba/app/lib/recordingpass.py | 636 | 12 | 0 | Single writer for ib_observation/ib_node (#1693) | Reads config by SQL: a false finding |  |
| 9 | batchcontrol | iba/app/lib/batchcontrol.py | 99 | 3 | 0 | Single writer for run_batch (#1756) | Reads config by SQL: a false finding |  |
| 10 | batchprogressreport | iba/app/lib/batchprogressreport.py | 91 | 0 | 0 | Read-only progress report over run_batch (#1756) | Exempt: a read-only report |  |
| 11 | observationenhancer | iba/app/handlers/observationenhancer.py | 198 | 4 | 0 | Applies a confirmed cfg_observation change (#1778) | Reads config by SQL: a false finding |  |
| 12 | taggingguidance | iba/app/lib/taggingguidance.py | 142 | 2 | 0 | Shared tag definitions for the generator stages (#1836) | Reads config by SQL: a false finding |  |

## A defect in the check itself

For rows 7, 8, 9, 11 and 12 the module reads `cfg_*` tables by SQL, which the check does not count.
That is a defect in the check, not in those modules. The root fix (rule 38) is for the check to
count a `cfg_` table read as config use. It changes what a check enforces, so it is a new
decision.

**Question A:** count SQL reads of `cfg_*` tables as config use in
`find_utility_config_density`? (yes / no)

## Your decision

Fill the Decision column per row (exempt / inactive / make it read config / other), and answer
Question A.
