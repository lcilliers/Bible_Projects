# Project-wide hardcoded-location-literal scan

> Project-wide scan for hardcoded folder/file-path string literals not backed by a live cfg accessor — ADVISORY, see lib/pathaudit.py's own docstring for method and honest limits. Escalation #971/#976.

## Contents

- [Summary](#summary)
- [Findings](#findings)

<a id="summary"></a>
## Summary

- **83** script(s) scanned (inactive-marked scripts excluded)
- **16** hardcoded location literal(s) found in **2** file(s)

<a id="findings"></a>
## Findings

| file | line | literal | cfg_utility registered |
| --- | --- | --- | --- |
| iba/app/lib/manifest.py | 154 | research/investigations | yes |
| iba/app/lib/manifest.py | 164 | data/imports/wa/patches | yes |
| iba/app/lib/manifest.py | 164 | archive/patches | yes |
| iba/app/lib/manifest.py | 170 | data/imports | yes |
| iba/app/lib/manifest.py | 172 | data/exports | yes |
| iba/app/lib/manifest.py | 174 | research/discovery | yes |
| iba/app/lib/manifest.py | 179 | data/schema | yes |
| iba/app/lib/manifest.py | 181 | archive/scripts | yes |
| iba/app/lib/manifest.py | 183 | archive/logs | yes |
| iba/app/lib/manifest.py | 185 | archive/docs | yes |
| iba/app/lib/manifest.py | 187 | outputs/reports | yes |
| iba/app/lib/prosestore.py | 56 | Workflow | yes |
| iba/app/lib/prosestore.py | 57 | outputs | yes |
| iba/app/lib/prosestore.py | 58 | outputs | yes |
| iba/app/lib/prosestore.py | 68 | Workflow | yes |
| iba/app/lib/prosestore.py | 93 | Workflow/Programme/prose-edits | yes |
