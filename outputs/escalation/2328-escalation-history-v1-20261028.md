# Escalation deep history

## #2328 — Reading JSON filed outside the cluster folder
type=issue source=researcher

**v1** (2026-10-28T09:08:38Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **short description (set this version):** Reading JSON filed outside the cluster folder
> **comment (set this version):** Researcher, chat 2026-10-28 (verbatim): 'the code test failed.  the code does not read the correct folder for the filing of the json because the code does not read the configs.' Claude, checked in the code: iba/app/lib/reading.py line 94 builds the reading folder as the setting reading.output_dir (outputs/reading) plus the label, so it reads that one setting; nothing in iba/app reads cfg_setting governance.report.cluster_folder_naming_convention (only the prototype iba/app/tools/temp_2304_reading_cycle_prototype.py has a helper for the folder name). The filing rule says all output relating to a cluster is filed in _analytics/Clusters/{cluster_code} - {short_name}, and the control map (cfg_control_home study_output) names outputs/reading until build B7 (#2268 R7, #2279, carried by #2315). The JSON of readings m21-asking, m21-asking-redo5, m21-gen43-27 and m21-gen43-27-b is therefore in outputs/reading/ and the folder _analytics/Clusters/M21 - fasting-piety is empty. Fix for Developer Mode: the reading code resolves its folder from the home cluster per the filing rule (the setting reading.output_dir retired or turned into a pattern), the existing reading folders moved, reading_index.roots and session_close.reading_scope checked, and the change tested end to end before it is reported done.
> **context (set this version):** iba/app/lib/reading.py; iba/app/tools/temp_2304_reading_cycle_prototype.py; escalation #2320; escalation #2315
