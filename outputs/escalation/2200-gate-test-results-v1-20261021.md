# #2200 test results: gate_retired_script.py

Run by `iba/app/tools/temp_2200_gate_test.py` on 2026-10-21 against a backup-API copy of iba.db with three test escalations (approved by the researcher; 'approved' by Claude; approved then withdrawn), plus one case against the live DB.

| case | command | expected | actual | result |
|---|---|---|---|---|
| run retired .py (python path) | `python iba/app/tools/archive/temp_2193_test_plan_run.py` | deny | deny | pass |
| run retired .py with launcher flags | `python -I -u iba/app/tools/archive/temp_2193_test_plan_run.py` | deny | deny | pass |
| run retired module (python -m) | `python -m iba.app.tools.archive.temp_2193_test_plan_run` | deny | deny | pass |
| run retired .py, Windows path | `python iba\app\tools\archive\temp_2193_test_plan_run.py` | deny | deny | pass |
| approval written by Claude does not count | `python iba/app/tools/archive/temp_2193_test_plan_run.py` | deny | deny | pass |
| run retired .py approved by the researcher | `python iba/app/tools/archive/temp_2192_apply.py` | allow | allow | pass |
| cfg_utility inactive row | `python query_db.py` | deny | deny | pass |
| approval on a withdrawn item does not count | `python query_db.py` | deny | deny | pass |
| retired .ps1 as first word | `.\iba\app\ps\archive\Old-Thing.ps1 -X 1` | deny | deny | pass |
| retired .ps1 via & call | `& "iba/app/ps/archive/Old-Thing.ps1"` | deny | deny | pass |
| retired .ps1 inside pwsh -Command | `pwsh -NoProfile -Command ".\iba\app\ps\archive\Old-Thing.ps1"` | deny | deny | pass |
| retired .ps1 via -File | `pwsh -NoProfile -File iba/app/ps/archive/Old-Thing.ps1` | deny | deny | pass |
| retired .ps1 after another command | `cd x; .\iba\app\ps\archive\Old-Thing.ps1` | deny | deny | pass |
| read a retired file (cat) | `cat iba/app/tools/archive/temp_2193_test_plan_run.py` | allow | allow | pass |
| read a retired file (Get-Content) | `Get-Content iba\app\tools\archive\temp_2193_test_plan_run.py` | allow | allow | pass |
| grep across archive | `grep -rn foo iba/app/tools/archive` | allow | allow | pass |
| active PS script | `.\iba\app\ps\Escalation.ps1 -Action List` | allow | allow | pass |
| active module (python -m) | `python -m iba.app.run escalation-reporting --step x` | allow | allow | pass |
| python -c inline code | `python -c "print(1)"` | allow | allow | pass |
| script outside the project | `python C:/Users/someone/AppData/Local/Temp/x.py` | allow | allow | pass |
| no database: allow, logged | `python iba/app/tools/archive/temp_2193_test_plan_run.py` | allow | allow | pass |
| live DB: Start-Iba.ps1 (not yet registered) | `.\iba\app\ps\Start-Iba.ps1` | allow | allow | pass |
