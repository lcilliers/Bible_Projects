# mti_terms diff — live vs 2026-05-28 backup (pre-today)

**Backup:** `bible_research_backup_20260528_065554_wa-cluster-M38-patch-borderline-resolution-v1-20260528.db`

- rows with `delete_flagged` flipped 0→1 today: **1233**
- rows with `delete_flagged` flipped 1→0 today: 0
- rows where `exclusion_reason` set to backfill signature ('Bulk deleted, decision not recorded'): **2131**
   - of those, were df=0 (NOT deleted) in backup → newly deleted by the backfill: **562**
- rows with some other `exclusion_reason` change: 0
- rows with `cluster_code` change (e.g. F→FLAG): 206
- rows present in live but not backup: 0

A surgical restore = copy (delete_flagged, exclusion_reason) from backup back into live for the affected rows, re-validate the evidence guard on the term_id link, then redo correctly.
F→FLAG (cluster_code) can be preserved (non-destructive, wanted).
