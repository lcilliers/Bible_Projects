# Escalation deep history

## #1007 —  create ps tool to work with catelogue 
type=task source=researcher

**v1** (2026-08-29T03:29:24Z, Researcher) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):**  create ps tool to work with catelogue 
> **comment (set this version):**  The catelogue is the framework used for cluster analysis.  This ps method aim at allowing full CRUD for the tables associated with the catelogue, and also reporting from various angles 
> **context (set this version):**  Previously catelogue work was done with scripts created and modified on demand. 
The catelogue tables are in the bible_research_db
The operation functionality around the catelogue must be in IBA_db, fully compliant with governance. 

**v2** (2026-08-29T03:36:12Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):**  proceed with building this tool. first extract the full content of all the associated table into csv so I can inspect the table. there may be two handles a) CRUD for changes to the tables, this include switches to produce views to csv. then analysis reports, that can pull out results. the reports must all use the governance report infrastructure, but each report will be produced on demand, and provide a different angle. it must be possible to request modifications for individual components of a report.  I will provide more build instructions once I had a chance to explore the csv and other elements 
> **context (set this version):**   

**v3** (2026-08-29T03:44:21Z, Claude) state=re-assigned next_action=review assigned_to=Researcher
> **comment (set this version):** Phase 1 done: identified the catalogue as wa_obs_question_catalogue + its 4 linked tables (cluster_finding, finding_question_link, wa_finding_catalogue_links, wa_flag_type_question_link), all in bible_research.db, traced via cfg_column FK to obs_id. Extended the already-registered table-export step (Export-Tables.ps1) with a -Database param (cfg-driven database_path(), same mechanism prosestore.py uses for bible_research.db) rather than a one-off script, so it's reusable governance infra, not throwaway. Ran it for the 5 catalogue tables -- CSVs written for your review. Config-Maintenance -Step Validate re-run clean (same 3 pre-existing unrelated advisory findings, nothing new). CRUD + reporting design awaits your review of the CSVs, per your v2 instruction.
> **resolution (set this version):** iba/docs/catalogue-1007-csv-extract-20260829/ (5 CSVs: wa_obs_question_catalogue.csv 424 rows, finding_question_link.csv 332205 rows, wa_finding_catalogue_links.csv 6199 rows, wa_flag_type_question_link.csv 12 rows, cluster_finding.csv 19318 rows). Code: iba/app/tools/export_tables_csv.py, iba/app/handlers/reports.py, iba/app/ps/Export-Tables.ps1 (-Database param). Build record: iba/app/BUILD.md section 200.

**v4** (2026-08-29T03:44:44Z, Claude) state=re-assigned next_action=review assigned_to=Researcher
> **comment (set this version):** Correction to my own last comment's row counts (checked against COUNT(*), not restated from a description): finding_question_link is 332204 (not 332205), cluster_finding is 19997 (not 19318) -- everything else in that comment stands.
> **resolution (set this version):** Verified counts for iba/docs/catalogue-1007-csv-extract-20260829/: wa_obs_question_catalogue.csv 424 rows, finding_question_link.csv 332204 rows, wa_finding_catalogue_links.csv 6199 rows, wa_flag_type_question_link.csv 12 rows, cluster_finding.csv 19997 rows. Code/build record unchanged: iba/app/tools/export_tables_csv.py, iba/app/handlers/reports.py, iba/app/ps/Export-Tables.ps1, iba/app/BUILD.md section 200.

**v5** (2026-08-29T03:57:21Z, Claude) state=re-assigned next_action=review assigned_to=Researcher
> **comment (set this version):** Filing correction: I'd put the CSVs at iba/docs/catalogue-1007-csv-extract-20260829/ -- wrong per cfg_behaviour_rule 'filing'/tool-report-path-vs-deliverable-document (id 60): a tool's own auto-generated output stays where its *.output_dir setting points, and iba/docs is for authored planning/engineering docs, not raw table dumps (governance.engineering_documentation_folder). table_export.output_dir is already governed to Workflow/schema (folder_purpose confirms it), so re-ran without -Out to land there instead, and deleted the misfiled iba/docs copy.
> **resolution (set this version):** Corrected location: Workflow/schema/wa_obs_question_catalogue.csv, finding_question_link.csv, wa_finding_catalogue_links.csv, wa_flag_type_question_link.csv, cluster_finding.csv (same 5 tables, same row counts as before). Code/build record unchanged otherwise: iba/app/tools/export_tables_csv.py, iba/app/handlers/reports.py, iba/app/ps/Export-Tables.ps1, iba/app/BUILD.md section 200 (path corrected there too).

**v6** (2026-08-29T10:15:27Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Foundational work for the catalogue tool is complete and ready for your sign-off; the report itself (design/build) continues as an open thread, not covered by this sign-off.
> **resolution (set this version):** Completed under #1007: catalogue identified (wa_obs_question_catalogue + 4 link tables) and CSV-extracted; wa_flag_type_question_link retired (dead: 12 orphaned/coincidental rows, questions all redundant_v1); cluster_finding + wa_finding_catalogue_links folded into a single finding/finding_question_link pair (BUILD.md sec203), both source tables retained inactive; finding_verse_index built (578,816 rows, 3 passes, direct to iba.verse.id) + finding.strong_number (99.99% resolved) replacing verse_context_id/mti_term_id as the live link mechanism (BUILD.md sec205); the verse-lexical concept clarified and a real UI gap fixed (VerseLexical.ps1 -Step, escalation #1041/BUILD.md sec206); a real escalation-dedup bug found and fixed along the way (BUILD.md sec204). Not yet built: the actual CRUD + standard-report tool -- report layout/density now being prototyped per your instruction, continuing as its own thread.
