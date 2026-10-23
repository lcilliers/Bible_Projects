# #2212 — prose.apply_patch: test results

Run 2026-10-23, `python -m iba.app.tools.temp_2212_apply_patch_test <scratch>`. Each case runs on its
own copy of `bible_research.db` (`lib/dbsnapshot.copy_db`). Cases are test 8 of
`iba/app/reports/prose-functionality-test-plan-20260826.md`. The SetStatus patch came from the live
generator (`prosestore.run_set_status`, which only reads), for section 2 (author `claude_ai`).

```
PASS  8c dry run: counts {'prose_section_status_set': 1}; tables unchanged: True
PASS  8d live set_status: status draft -> in_review; log rows 1; version 1288 = log id 1288; payload prior status 'draft'
PASS  8e re-apply: PATCH-20261023T125744Z-PROSE-SET-STATUS: already applied (record_change_log.change_source)
PASS  8f supersede: body changed, heading kept: True, word_count 224, payload holds old body: True
PASS  8g ungranted table: P-8g: writer 'apply_session_patch' has no cfg_write_grant for ['prose_section_dimension_link']; nothing written: True
PASS  8h good then bad: T2: supersede target 999999999 not found; nothing written: True
PASS  8i unknown operation: T: operation 'explode' on 'prose_section' is not supported; nothing written: True
PASS  8j immutable type field: T: prose_section_type update sets immutable or unknown fields ['code']; nothing written: True
PASS  8k session_a_replace author gate: T: session_a_replace target 2 is not a claude_code row; nothing written: True
PASS  8l no patch id: the patch has no _patch_meta.patch_id; nothing written: True
PASS  8l no operations: P-8l: the patch has no operations; nothing written: True
11/11 passed
```

**8a** (front door, no `-PatchFile`): `iba\app\ps\Prose.ps1 -Step ApplyPatch` printed "ApplyPatch
needs -PatchFile." and exited 1. Pass.

**8b** (through `run.py`, file not found), after #2241 was applied:
`iba\app\ps\Prose.ps1 -Step ApplyPatch -PatchFile nothere.json -DryRun` gave run
RUN-20261023_141514_208-PROSE, `prose.apply_patch report-stop no patch file at nothere.json`, exit 3.
Pass. The dispatcher raised #2244 for the stop, as it does for any bad-params stop; it was resolved
as a test artefact.

**Live database after the run:** `record_change_log` 1,287 rows, newest 2026-09-18T05:36:39Z
(as before); section 2 status `draft` (as before). Nothing live was written.
