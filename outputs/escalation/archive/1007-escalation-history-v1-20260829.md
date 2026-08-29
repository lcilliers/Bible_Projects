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
