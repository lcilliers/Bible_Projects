# Programme Status Report — 2026-03-30

> Produced by Claude Code. Schema v3.8.0. Post mti\_terms deduplication and OWNER/XREF fix.

## 1\. Programme Overview

|Metric|Count|
|-|-|
|Total registries|212|
|Active (Phase 1 Complete, has terms)|179|
|Excluded|31|
|Zero-term (Complete but no terms)|0|

## 2\. Pipeline Status — Dual Track

### 2.1 session\_b\_status

|Status|Count|
|-|-|
|Verse Context Reset|181|
|NULL|31|

### 2.2 verse\_context\_status

|Status|Count|
|-|-|
|In Progress|181|
|NULL|31|

### 2.3 Combined Status Matrix

|session\_b\_status|verse\_context\_status|Count|
|-|-|-|
|Verse Context Reset|In Progress|181|
|NULL|NULL|31|

## 3\. Term Index — mti\_terms

|Metric|Count|
|-|-|
|Active terms|3807|
|Deleted (flagged)|3680|
|Total rows|7487|

### 3.1 Status Distribution (active only)

|Status|Count|%|
|-|-|-|
|extracted|2233|58.7%|
|delete|1185|31.1%|
|extracted\_thin|305|8.0%|
|candidate\_delete|62|1.6%|
|extracted\_theological\_anchor|15|0.4%|
|xref\_distress|2|0.1%|
|phase2\_enrichment|1|0.0%|
|xref\_anger|1|0.0%|
|xref\_desire|1|0.0%|
|xref\_sorrow|1|0.0%|
|xref\_wisdom|1|0.0%|

### 3.2 Language Distribution

|Language|Count|
|-|-|
|Hebrew|2529|
|Greek|1278|

### 3.3 Data Quality — Key Fields

|Field|NULL count|Status|
|-|-|-|
|strongs\_number|0|CLEAN|
|transliteration|0|CLEAN|
|gloss|0|CLEAN|
|language|0|CLEAN|
|owning\_registry\_fk|0|CLEAN|
|owning\_word|0|CLEAN|
|status|0|CLEAN|
|extraction\_date|0|CLEAN|

### 3.4 Integrity

* Duplicate Strong's (active): **0**
* 1 row per Strong's: **YES**

## 4\. Term Inventory — wa\_term\_inventory

|Metric|Count|
|-|-|
|Active records|6988|
|OWNER|3647|
|XREF|3341|

### 4.1 OWNER/XREF Integrity

* Multi-OWNER Strong's: **0**
* XREF with active verses: **0**

### 4.2 Data Quality — Key Fields

|Field|NULL count|Status|
|-|-|-|
|file\_id|0|CLEAN|
|language|0|CLEAN|
|strongs\_number|0|CLEAN|
|transliteration|0|CLEAN|
|step\_search\_gloss|0|CLEAN|
|word\_analysis\_gloss|0|CLEAN|
|occurrence\_count|0|CLEAN|
|term\_owner\_type|0|CLEAN|

## 5\. Verse Records

|Metric|Count|
|-|-|
|Active verses|85,116|
|Deleted (flagged)|139,413|
|Total|224,529|

## 6\. Verse Context — Stage 1 Progress

|Metric|Count|
|-|-|
|verse\_context\_group records|0|
|verse\_context records|0|
|Registries at VC Complete|0 / 181|
|Batches processed|0|
|**Stage 1 status**|**Not started — VCB-001 ready for submission**|

## 7\. Cluster Progress

|Cluster|Words|VC Reset|Pre-Analysis|Analysis Complete|SB Complete|
|-|-|-|-|-|-|
|C01|6|6|0|0|0|
|C02|13|13|0|0|0|
|C03|9|9|0|0|0|
|C04|7|7|0|0|0|
|C05|9|9|0|0|0|
|C06|8|7|0|0|0|
|C07|10|9|0|0|0|
|C08|11|11|0|0|0|
|C09|10|7|0|0|0|
|C10|11|10|0|0|0|
|C11|10|10|0|0|0|
|C12|10|10|0|0|0|
|C13|9|8|0|0|0|
|C14|10|7|0|0|0|
|C15|9|9|0|0|0|
|C16|10|10|0|0|0|
|C17|11|10|0|0|0|
|C18|7|5|0|0|0|
|C19|11|7|0|0|0|
|C20|7|6|0|0|0|
|C21|8|4|0|0|0|
|C22|16|7|0|0|0|

## 8\. Data Fixes Applied (2026-03-30)

|Fix|Records|Detail|
|-|-|-|
|mti\_terms deduplication|3,616 flagged|1 row per Strong's (was 1,780 duplicated)|
|mti\_terms orphans|64 flagged|No inventory reference|
|OWNER/XREF fix|1,871 flipped|Each Strong's max 1 OWNER|
|XREF verse flagging|48,237 flagged|XREF verses delete\_flagged|
|owning\_registry\_fk|1,373 set|All active mti now have FK|
|status NULL|810 set|Terms with active verses -> extracted|
|owning\_word NULL|1 fixed|Set from gloss|
|extraction\_date NULL|538 set|Set to 2026-03-28|
|word\_analysis\_gloss NULL|16 set|Set from step\_search\_gloss|
|occurrence\_count NULL|1 fixed|Set from verse count|
|delete\_flagged column|added|New column on mti\_terms|
|audit\_word.py|3 fixes|Dedup guard, FK on insert, stale field refresh|

## 9\. Next Steps

1. **VCB-001 submitted** — 1st Verse Context batch ready for Claude AI classification
2. **Estimated \~37 batches** to classify all 85,116 active verses
3. After Stage 1 complete: pool-based Session B per RMG v5.6 processing sequence

\---

*Produced 2026-03-30 by Claude Code. Schema v3.8.0.*

