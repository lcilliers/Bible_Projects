---
description: Open the two Excel tool-interface worksheets (ps tools, escalation actions) in Excel
---

Open both Excel tool-interface worksheets in Excel itself (their default file association), via
PowerShell `Start-Process` — not via any editor/extension:

```powershell
Start-Process "c:\Bible_study_projects\iba\docs\ps tools worksheet.xlsx"
Start-Process "c:\Bible_study_projects\iba\docs\escalation actions worksheet.xlsx"
```

Run both commands, then confirm briefly that both were launched. Nothing else — no status report,
no other checks.
