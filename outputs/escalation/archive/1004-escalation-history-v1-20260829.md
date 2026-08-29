# Escalation deep history

## #1004 —  User PS Tool in excel 
type=task source=researcher

**v1** (2026-08-28T15:18:59Z, Researcher) state=raised next_action=review assigned_to=Claude
> **short description (set this version):**  User PS Tool in excel 
> **comment (set this version):**  Create a user interface tool, based on the example iba\docs\escalation actions worksheet.xlsx for all methods and other PS utilities. each row represent to compulation of an instruction 

**v2** (2026-08-28T15:24:18Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **resolution (set this version):** Built: iba\docs\ps tools worksheet.xlsx -- one sheet per script in iba\app\ps (47 scripts + an Index tab). Each sheet: row 4 = flag headers (-ParamName, one per column), row 5 = hints where a param has an enum/format, row 6 = fill-in-and-compile row -- column B compiles the full command for copy/paste, column A the script path, columns C+ the params. Design difference from your model sheet: your Escalations sheet hard-codes exactly which flags belong to each fixed action-shape (Raise/Update/etc); most of the other 46 scripts don't have that few-fixed-shapes structure, so every flag here is wrapped in IF(cell='','','-Flag value') -- a blank cell just drops out of the compiled command, so one row per script covers every combination rather than needing a row per mode. Escalation.ps1 itself is NOT duplicated -- its tab just points back to your existing model sheet.
