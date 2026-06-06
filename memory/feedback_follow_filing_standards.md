---
name: feedback_follow_filing_standards
description: "Every file must comply with docs/file-organisation-rules.md (naming, filing, archiving). Don't improvise names/locations; follow the documented guide."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: eae3184c-630b-48c2-9ac1-b0b494ccf689
---

Every file CC creates must comply with `docs/file-organisation-rules.md` — naming (§2), folder/filing (§3), and archiving (§4). Do not improvise file names, locations, or process; the standards are documented and were developed deliberately over days. When unsure where something goes or what a thing means, **read the guide / the documented design — do not invent it from the records.**

**Why (2026-06-01, serious correction):** "Your file naming conventions does not meet the standards … your filing of documents does not meet the standard … the archiving and maintenance of all the old redundant files do not meet the standard … you have gone off the rails." During the off-the-rails stretch I created ad-hoc names (`cluster_ac_validation_v1_…`, `_validate_/_dump_` scripts), dumped reports in `outputs/markdown/` (not a sanctioned location), left "lists" in temp tool-results paths, and left `_tmp_*` dumps lying around.

**How to apply (the rules I broke):**
- **Naming (§2):** lowercase, hyphens (not underscores), `YYYYMMDD`, `-v{n}` where versioned; `wa-…` for programme files; identifiers keep case (M38, G2285).
- **Investigations / ad-hoc audits / assessments → `research/investigations/`** as `{topic}-{YYYYMMDD}.{ext}`. **NOT `outputs/markdown/`** — nothing goes in `outputs/` root (§3.10).
- **Scripts (§3.13):** sanctioned prefixes only — read-only `_assess_`/`_check_`/`_probe_`/`_discover_`/`_explore_`/`verify_`/`inspect_`; DB-modifying `_apply_`/`_repair_`/`_realign_`/`_reset_`/`_extract_`/`_delete_`. No `_validate_`/`_dump_`.
- **Archiving (§4):** `_tmp_*` deleted or → `archive/scripts/` at session end; one-off `_check_`/`_probe_` that served their purpose → `archive/scripts/`; superseded report versions → the folder's `archive/`. Don't let redundant files accumulate.
- **After any moves/renames:** run `python scripts/build_file_manifest.py` (§6).
- Living-document versioning (registers/working docs) uses metadata + git, not filename `-vN` — see [[feedback_version_discipline]] §2.3a.

Relates to [[feedback_integrity_and_intent_first]] (follow the documented design, don't improvise) and [[feedback_review_via_files_not_chat]].
