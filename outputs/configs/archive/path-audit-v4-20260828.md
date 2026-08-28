# Project-wide hardcoded-location-literal scan

> Project-wide scan for hardcoded folder/file-path string literals not backed by a live cfg accessor — ADVISORY, see lib/pathaudit.py's own docstring for method and honest limits. Escalation #971/#976.

## Contents

- [Summary](#summary)
- [Findings](#findings)

<a id="summary"></a>
## Summary

- **84** script(s) scanned (inactive-marked scripts excluded)
- **17** hardcoded location literal(s) found in **3** file(s)

<a id="findings"></a>
## Findings

| file | line | literal | cfg_utility registered |
| --- | --- | --- | --- |
| iba/app/lib/manifest.py | 139 | research/investigations | yes |
| iba/app/lib/manifest.py | 149 | data/imports/wa/patches | yes |
| iba/app/lib/manifest.py | 149 | archive/patches | yes |
| iba/app/lib/manifest.py | 155 | data/imports | yes |
| iba/app/lib/manifest.py | 157 | data/exports | yes |
| iba/app/lib/manifest.py | 159 | research/discovery | yes |
| iba/app/lib/manifest.py | 161 | data/schema | yes |
| iba/app/lib/manifest.py | 163 | archive/scripts | yes |
| iba/app/lib/manifest.py | 165 | archive/logs | yes |
| iba/app/lib/manifest.py | 167 | archive/docs | yes |
| iba/app/lib/manifest.py | 169 | outputs/reports | yes |
| iba/app/lib/prosestore.py | 54 | Workflow | yes |
| iba/app/lib/prosestore.py | 55 | outputs | yes |
| iba/app/lib/prosestore.py | 56 | outputs | yes |
| iba/app/lib/prosestore.py | 62 | outputs | yes |
| iba/app/lib/prosestore.py | 84 | outputs/markdown/prose-edits | yes |
| iba/app/tools/word_strong_span_report.py | 181 | iba/app/db/iba.db | NO |
