---
name: filing-is-first-class-governance
description: File-organisation/naming/versioning is a first-class governance concern the researcher cares about and I keep dropping; governed by docs/file-organisation-rules.md + GR-FILE + the manifest; the guidance itself has drifted from the restructured layout
metadata:
  type: feedback
---

FEEDBACK (2026-06-14): treat **filing / file-organisation as a first-class governance concern**, not an afterthought. I omitted it entirely from the project reconstruction (orientation map + failures log) and was corrected — a repeat pattern. The researcher cares about it: "filing is not consistent, so there is no real reliability to try and use the folders."

**Governing artefacts:** `docs/file-organisation-rules.md` (naming §2; **snapshot vs living-document versioning** §2.3/§2.3a — living docs carry NO `-vN`, version lives in metadata + git; folder rules §3 incl. §3.0 `Sessions-v2/` = home for all new cluster output; archiving §4; CC obligations §5; manifest §6) · **GR-FILE-*** in `Workflow/Global_rules/wa-global-rules-all-v2` · file-naming in `wa-reference [current]` · the DB pattern registries `wa_file_name_pattern`/`wa_label_pattern`/`wa_patch_type_registry` (M34) · the index `database/file_manifest.json` (`scripts/build_file_manifest.py`).

**How to apply:** before writing any file, set its location/name from the rules; archive superseded versions (silent supersession = a filing-rule breach); rebuild the manifest after moves; **locate files via the manifest, not the folders** (folders are unreliable). **The guidance itself is partly drifted** (verified 2026-06-14: §3.9 `data/schema` missing → schema now `Workflow/schema`; top-level `data/` exists but absent from CLAUDE.md §2; exports have two homes — `Sessions/Session_A/STEP Extracts` and `data/exports`). A **filing audit** (reconcile rules + registries ↔ actual tree) is an open item. See [[reference-core-memory-orientation-map]] · [[project_reconstruction_baseline_20260614]] · [[source-of-truth-is-written-record]].
