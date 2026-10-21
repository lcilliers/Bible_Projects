# 2208 — Test results: PS folder read from governance.scripts_ps_dir

Escalation #2208, option (a). Test plan: `iba/app/tools/temp_2208_ps_dir_test_run.py`, run 2026-10-21 on a copy of iba.db made with `lib/dbsnapshot.copy_db`. No live DB or file written by the test. Synthetic cases: T5, T6.

6/6 pass.

| case | what | result | evidence |
|---|---|---|---|
| T1 | migration: 2 audited writes, then skips | PASS | 2 write(s) applied (run DEVMODE-2208-PS-DIR-SETTING-20261021, logged to cfg_change_detail) / already applied -- skipped |
| T2 | scripts_ps_dir no longer delivered; scripts_python_dir still delivered | PASS | 44 governance rows delivered |
| T3 | ps_dir() resolves the setting to the repo's PS folder | PASS | C:\Bible_study_projects\iba\app\ps |
| T4 | the 5 checks on real data give the counts the last live validate gave (0,0,0,0,2) | PASS | {'escalation_ps_validateset_drift': 0, 'folderpurpose_ps_validateset_drift': 0, 'ps_worksheet_drift': 0, 'escalation_worksheet_drift': 0, 'ps_scripts_bypassing_runpy': 2}; bypass: ['iba/app/ps/Behaviour.ps1 calls iba.app.(handlers/lib/tools) directly, no iba.app.run dispatch found in the same file', 'iba/app/ps/VerseMeta.ps1 calls iba.app.(handlers/lib/tools) directly, no iba.app.run dispatch found in the same file'] |
| T5 | the check follows the setting: a bypassing script in the configured folder is found | PASS | ['fakeps/Bad.ps1 calls iba.app.(handlers/lib/tools) directly, no iba.app.run dispatch found in the same file'] |
| T6 | missing setting fails loudly | PASS | KeyError: 'cfg_setting governance.scripts_ps_dir is missing or inactive' |
