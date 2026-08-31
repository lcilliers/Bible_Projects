# Schema overview

> Generated 2026-08-31T13:14:19Z by `report.schema_overview`. Introspects the live DB directly and merges it against `cfg_table`/`cfg_column` (database='iba') — always current, never hand-maintained.

- data tables: **41** live

## Contents

- [Table inventory](#table-inventory)
- [Every data table, in full](#every-data-table-in-full)

<a id="table-inventory"></a>
## Table inventory

| table | rows (live) | cfg use | category | discrepancy |
| --- | --- | --- | --- | --- |
| candidate_seed | 1806 | L4b seed decision (potential, not definite); the lexical stage is the real test. | data |  |
| cluster | 51 | Migrated from the old project's bible_research.db `cluster` table, 2026-08-11. c | data |  |
| cluster_strong | 7391 | The strong<->cluster link. Cluster membership is a property of the Strong's code | data |  |
| content_index | 0 | Content-index search: one row per indexed hit -- a key (e.g. an escalation id, a | data |  |
| content_index_scan | 0 | Content-index incremental-scan state: last-scanned mtime per file, so a rebuild  | data |  |
| debate_change_detail | 242 | one row per hib/hib_referent_option/verse_hib/passage/verse_passage/phenomenon/o | data |  |
| escalation | 638 | One row per item, CURRENT STATE ONLY. NOT redundant with escalation_history -- h | data |  |
| escalation_history | 2316 | One row per update to an item, ever -- append-only, a TRUE DELTA per version (mo | data |  |
| escalations_old | 723 | Historical escalation data, frozen at the 2026-08-20 redesign cutover (v2, corre | data | **inactive in cfg_table but has live rows** |
| file_manifest | 16197 | Filename/path metadata for every file in the project tree (18,653 rows at regist | data |  |
| folder_purpose | 959 | Reference/data table (like bible_research.db's books, NOT a cfg_* rule table) -- | data |  |
| hib | 21 | one row per Human Inner Being identified in a scope (debate digest Step 1) -- sc | data |  |
| hib_referent_option | 0 | one row per grammatically-live referent-crux reading (T4), child of hib. | data |  |
| lemma_inventory | 11781 | L4b seed substrate; imported from the old study, NOT derived from the registry,  | data |  |
| operation | 121 | the operation for a registered phenomenon (Step 4-5 output) -- phenomenon_id NOT | data |  |
| operation_party | 136 | one row per source/target of an operation (plural-capable, v1.5 step1 note a), c | data |  |
| passage | 42 | extends a characteristic's context to adjacent verses for assessing movement/pro | data | **RETIRED** |
| passage_emergent_question | 3 | Part C section 6 (Q10/B.9/B.12) -- interpretive forks and genuine literary/struc | data |  |
| passage_insufficiency | 1 | Part C section 5 (Q9/B.7) -- data the base extract does not carry, named not fil | data |  |
| passage_linkage | 3 | Part C section 4 (Q7) -- linkages between two specific, already-registered opera | data |  |
| passage_validation_note | 4 | Part C section 7 (Phase 3) -- the closing re-examination of the passage's own ph | data |  |
| phenomenon | 121 | the phenomena register (Step 3 output) -- one row per HIB per verse per passage. | data |  |
| run | 2361 | what ran, pinned to a config version, and RESUMABLE (O7): state + resume_point p | data |  |
| span | 378149 | L4a - SOURCE, immutable. A parse of verse.preview. position is the running TAG i | data |  |
| span_candidate | 83914 | over-inclusive candidate stamp; the lexical stage later tests each in context | data |  |
| strong | 15293 | L2 — the strong's identity. The meaning is normalised out (O4): it lives in stro | data |  |
| strong_lexicon | 5639 | the large lexicon text — separate because rarely scanned | data |  |
| strong_lsj_parsed | 36199 | L2b — the parsed classical-Greek lexicon layer over strong_lexicon.lsj (raw). Se | data |  |
| strong_meaning_parsed | 47113 | L2b — the parsed meaning layer over strong_meaning_tree (raw). Segment-scoped: r | data |  |
| strong_meaning_tree | 40315 | the lemma's full range — read rarely, only when the broader context is needed. K | data |  |
| strong_mounce_parsed | 5742 | L2b — the parsed Greek lexicon layer over strong_lexicon.mounce (raw). Split ONL | data |  |
| strong_related | 87535 | L2b — NOT derived from any raw table; fetched live from STEP per full strong cod | data |  |
| strong_sense | 15293 | the span's meaning, read constantly. The head is the first line of mediumDef (th | data |  |
| strong_verse | 132718 | the source's assertion 'this strong is in this verse'. The check side against sp | data |  |
| validation_result | 39457 | util.validation — the outcome of a check, persisted so it can be inspected and r | data |  |
| verse | 29759 | L3 — the addressable verse. preview is the full interlinear, kept verbatim so sp | data |  |
| verse_hib | 235 | one row per HIB present/a presumptive candidate in a given verse (Step 1's per-v | data |  |
| verse_lexical | 552353 | L4b — DERIVED, version-aware. The mechanical T1-T3 reading: role classification  | data |  |
| verse_passage | 777 | which passage a verse belongs to; a verse is in at most one passage | data | **RETIRED** |
| word_registry | 180 | the study's entry point; scope of a new-word run | data |  |
| word_strong | 4874 | L1 — the discovery record: which strongs a word maps to. These strongs are the b | data |  |

- 41 live table(s), 41 registered in `cfg_table` (database='iba'), **1 discrepancy**.

**Retired** (2) — soft-deleted at the data level, kept for the historical record, not part of the live system: `passage` (see `reports/archive/passage-system-retirement-record-20260726.md`); `verse_passage` (see `reports/archive/passage-system-retirement-record-20260726.md`)

<a id="every-data-table-in-full"></a>
## Every data table, in full

### candidate_seed (1806 row(s))

cfg_table.use: L4b seed decision (potential, not definite); the lexical stage is the real test. registry_match NULL on a candidate = a candidate MISSING registry word (the double control)

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  | surrogate key |  |
| lemma_key | TEXT |  | ✓ | lemma_inventory.lemma_key | the assessed lemma |  |
| decision | TEXT |  |  |  | DORMANT - candidate.seed retired 2026-07-23; no active mecha |  |
| layer | TEXT |  |  |  | DORMANT - candidate.seed retired 2026-07-23; no active mecha |  |
| registry_match | TEXT |  |  |  | DORMANT - candidate.seed retired 2026-07-23; no active mecha |  |
| tag | TEXT |  |  |  | DORMANT - candidate.seed retired 2026-07-23; no active mecha |  |
| strong_variant | TEXT |  | ✓ |  | the specific sub-lettered Strongs variant this row's tag ref |  |
| sense_seq | INTEGER |  | ✓ |  | DORMANT - candidate.load retired 2026-07-23; no active mecha |  |
| step_status | TEXT |  |  |  | DORMANT - candidate.load retired 2026-07-23; no active mecha |  |
| ib_referent_type | TEXT |  |  |  | DORMANT - candidate.load retired 2026-07-23; no active mecha |  |
| assessed_at | TEXT |  |  |  | DORMANT - candidate.seed retired 2026-07-23; no active mecha |  |
| deleted | INTEGER |  |  |  | soft delete |  |
indexes: idx_candidate_seed_live_unique, idx_candidate_seed_strong_variant, idx_candidate_seed_lemma_key, sqlite_autoindex_candidate_seed_1

### cluster (51 row(s))

cfg_table.use: Migrated from the old project's bible_research.db `cluster` table, 2026-08-11. cluster_code is the canonical key referenced everywhere else (cluster_strong, and any future dimension work). T2 is the landing zone for codes not included in analysis; FLAG is unresolved/needs-review; M01-M46 are the named inner-being characteristics.

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| cluster_code | TEXT | ✓ |  |  | canonical key, e.g. M01, FLAG, T2 |  |
| short_name | TEXT |  |  |  | short display name, e.g. 'Fear' |  |
| description | TEXT |  |  |  | one-line description, e.g. 'Fear, Dread and Terror' |  |
| gloss | TEXT |  |  |  | worked-example term list for this cluster (comma-joined glos |  |
| deleted | INTEGER |  |  |  | soft delete |  |
indexes: sqlite_autoindex_cluster_1

### cluster_strong (7391 row(s))

cfg_table.use: The strong<->cluster link. Cluster membership is a property of the Strong's code itself, independent of word_strong/word_registry — deliberately has no FK/dependency on either. `source` tracks provenance (old-system-migration now; future allocation passes get their own source value, never overwriting a prior row in place).

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  | surrogate key |  |
| strong | TEXT |  | ✓ | strong.strongNumber | the full Strong's code this assignment is for |  |
| cluster_code | TEXT |  | ✓ | cluster.cluster_code | the assigned cluster |  |
| source | TEXT |  | ✓ |  | provenance: 'old-system-migration' | (future) an LLM-allocat |  |
| created_at | TEXT |  |  |  | ISO-8601 UTC |  |
| deleted | INTEGER |  |  |  | soft delete |  |
| confidence | TEXT |  |  |  | 'high' | 'medium' | 'low' -- an allocation pass's own confid |  |
| operation | INTEGER |  |  |  | 1 if the code denotes a human operation/movement (a T3 'Oper |  |
| alt_clusters | TEXT |  |  |  | JSON list of alternate cluster_code candidates an allocation |  |
| review_flag | INTEGER |  |  |  | 1 if this specific assignment needs researcher review before |  |
| rationale | TEXT |  |  |  | free-text reasoning for the assignment, as given by whatever |  |

### content_index (0 row(s))

cfg_table.use: Content-index search: one row per indexed hit -- a key (e.g. an escalation id, a Strong number) found at a specific file/line, with a text snippet. Currently 0 rows -- report.content_index_search/rebuild exist but escalation #770 (on-hold) judged the current design unsupportable at scale; not yet populated.

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| key_type | TEXT | ✓ | ✓ |  | Kind of key indexed (e.g. escalation id, Strong number) -- p |  |
| key_value | TEXT | ✓ | ✓ |  | The actual key value indexed -- part of the composite PK. |  |
| file_path | TEXT | ✓ | ✓ |  | File the key was found in -- part of the composite PK. |  |
| line_number | INTEGER | ✓ | ✓ |  | Line the key was found at -- part of the composite PK. |  |
| snippet | TEXT |  | ✓ |  | Text snippet around the match, for display. |  |
| indexed_at | TEXT |  | ✓ |  | When this hit was indexed. |  |
indexes: ix_content_index_file, ix_content_index_key, sqlite_autoindex_content_index_1

### content_index_scan (0 row(s))

cfg_table.use: Content-index incremental-scan state: last-scanned mtime per file, so a rebuild only re-indexes changed files. Currently 0 rows, same status as content_index (escalation #770, on-hold).

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| file_path | TEXT | ✓ |  |  | File path, primary key -- one row per scanned file. |  |
| mtime | TEXT |  | ✓ |  | File modification time at last scan, so a rebuild only re-in |  |
| scanned_at | TEXT |  | ✓ |  | When this file was last scanned. |  |
indexes: sqlite_autoindex_content_index_scan_1

### debate_change_detail (242 row(s))

cfg_table.use: one row per hib/hib_referent_option/verse_hib/passage/verse_passage/phenomenon/operation/operation_party/passage_linkage/passage_insufficiency/passage_emergent_question/passage_validation_note row inserted, updated, or soft-deleted by hib.set/passage.build/phenomenon.set/operation.set/closing.set -- the per-run CRUD audit trail shared by every debate writer (researcher direction 2026-08-08).

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  | surrogate PK |  |
| run_id | TEXT |  | ✓ | run.run_id | which run made this change -- same fk convention as escalati |  |
| table_name | TEXT |  | ✓ |  | 'hib' | 'hib_referent_option' | 'verse_hib' -- which table t |  |
| op | TEXT |  | ✓ |  | 'insert' | 'update' | 'delete' -- free text, matching cfg_ch |  |
| where_json | TEXT |  |  |  | identifies the row touched, e.g. {"id": 47} |  |
| set_json | TEXT |  |  |  | the new values written (insert/update only) |  |
| before_json | TEXT |  |  |  | prior row state (update/delete only), NULL on insert |  |
| applied_at | TEXT |  | ✓ |  | ISO-8601 UTC |  |
| writer | TEXT |  | ✓ |  | which step made this change -- 'hib.set' | 'passage.build' | |  |
indexes: idx_hib_change_detail_run_id

### escalation (638 row(s))

cfg_table.use: One row per item, CURRENT STATE ONLY. NOT redundant with escalation_history -- history stores true per-version deltas (most fields NULL per row); escalation is the only place the full current state is materialised. Ids continue from escalations_old's max (735) once D1's rebuild lands (register v9, escalation-design-decision-register-v9-20260821).

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  | serial PK, 4-digit display; continues from escalations_old's |  |
| version | INTEGER |  | ✓ |  | current version number for this id -- count of its escalatio |  |
| run_id | TEXT |  |  |  | restored 2026-08-20 (v1 dropped it, broke dispatch, rolled b |  |
| source | TEXT |  | ✓ |  | what triggered the item: script name | module | issue area.  |  |
| at_step | TEXT |  |  |  | pipeline reference, only set if code-generated/run-error. Im |  |
| type | TEXT |  | ✓ |  | differentiates the kind of item |  |
| short_description | TEXT |  | ✓ |  | label/title -- what this item is about. IMMUTABLE after Rais |  |
| context | TEXT |  |  |  | what must be done or the error message, plus links to extern |  |
| comment | TEXT |  |  |  | additional information for the assigned party. Cumulative, s |  |
| tried | TEXT |  |  |  | the corrective action taken -- REQUIRED when next_action_ass |  |
| state | TEXT |  | ✓ |  | current status -- raised at Raise; mostly logic-derived on U |  |
| next_action | TEXT |  |  |  | what's expected of the current reader (incoming) / what the  |  |
| next_action_assigned_to | TEXT |  |  |  | Claude | Researcher |  |
| originator | TEXT |  |  |  | who created the latest escalation_history row -- auto-popula |  |
| resolution | TEXT |  |  |  | what was actually done -- REQUIRED when next_action=approved |  |
| raised_at | TEXT |  | ✓ |  | first creation datetime -- set once, immutable |  |
| answered_at | TEXT |  |  |  | mirrors the latest escalation_history row's timestamp |  |
| resolution_kind | TEXT |  |  |  | decision_required or self_correctable (cfg_enum resolution_k |  |
| needs_claude_followup | INTEGER |  | ✓ |  | Set by Claude at Raise or at the ready_for_approval Update:  |  |

### escalation_history (2316 row(s))

cfg_table.use: One row per update to an item, ever -- append-only, a TRUE DELTA per version (most fields NULL per row unless that version's own transaction set them), not a full snapshot. Envelope fields (state/next_action/next_action_assigned_to/originator/answered_at) always populated; content fields (comment/context/resolution/tried/short_description/related_activity) NULL unless touched this version. escalation is the current-state materialisation of the latest row here, not the reverse.

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  | surrogate PK, row order = write order |  |
| escalation_id | INTEGER |  | ✓ | escalation.id | which item this snapshot belongs to |  |
| version | INTEGER |  | ✓ |  | this item's version number at the time of this snapshot -- m |  |
| run_id | TEXT |  |  |  | snapshot of escalation.run_id (constant per item) |  |
| source | TEXT |  |  |  | delta: NULL after v1 unless source is corrected (it normally |  |
| at_step | TEXT |  |  |  | snapshot of escalation.at_step at this version |  |
| type | TEXT |  |  |  | delta: NULL after v1 unless type is corrected -- was wrongly |  |
| short_description | TEXT |  |  |  | delta: NULL after v1 unless the title is explicitly correcte |  |
| context | TEXT |  |  |  | delta: the raw increment THIS version added, NULL if this ve |  |
| comment | TEXT |  |  |  | delta: the raw increment THIS version added, NULL if this ve |  |
| tried | TEXT |  |  |  | snapshot of escalation.tried at this version |  |
| state | TEXT |  | ✓ |  | snapshot of escalation.state at this version |  |
| next_action | TEXT |  |  |  | snapshot of escalation.next_action at this version |  |
| next_action_assigned_to | TEXT |  |  |  | snapshot of escalation.next_action_assigned_to at this versi |  |
| originator | TEXT |  |  |  | who created THIS specific snapshot -- the real per-update au |  |
| resolution | TEXT |  |  |  | snapshot of escalation.resolution at this version |  |
| raised_at | TEXT |  |  |  | delta, structural: only ever set at v1 (the item's true crea |  |
| answered_at | TEXT |  | ✓ |  | THIS row's own write timestamp -- the real per-update dateti |  |
| resolution_kind | TEXT |  |  |  | per-version snapshot of escalation.resolution_kind at that v |  |
| needs_claude_followup | INTEGER |  | ✓ |  | Mirrors escalation.needs_claude_followup -- envelope column, |  |
indexes: idx_escalation_history_escalation_id, sqlite_autoindex_escalation_history_1

### escalations_old (723 row(s))

cfg_table.use: Historical escalation data, frozen at the 2026-08-20 redesign cutover (v2, corrected retry of the rolled-back 2026-08-19 v1) -- 723 rows, pre-dates escalation_history entirely. Read-only reference only, excluded from all new validation/correction (researcher instruction, 2026-08-19). Superseded by escalation + escalation_history.

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  | surrogate key |  |
| run_id | TEXT |  | ✓ | run.run_id | the paused run |  |
| source | TEXT |  | ✓ |  | the source of the escalation -- 'new-word: <word>' for a wor |  |
| at_step | TEXT |  |  |  | where to resume — makes it a pause not a fork |  |
| type | TEXT |  |  |  | task | run_error | issue | notice | config |  |
| short_description | TEXT |  |  |  | the short description of what's being escalated |  |
| context | TEXT |  |  |  | the context that lets it be answered (JSON) |  |
| tried | TEXT |  |  |  | what the app attempted before asking |  |
| state | TEXT |  |  |  | raised | re-assign | on-hold | closed | withdraw | completed |  |
| next_action | TEXT |  |  |  | the decision/next action taken: approve | reject | revise |  |  |
| answered_at | TEXT |  |  |  | when |  |
| raised_at | TEXT |  |  |  | when raised |  |
| comment | TEXT |  |  |  | researcher feedback on a 'revise' answer (or any answer) |  |
| resolution | TEXT |  |  |  | what was actually done to resolve the item -- a short descri |  |
| related_activity | TEXT |  |  |  | the process, module, or activity this row relates to -- defa |  |
| next_action_assigned_to | TEXT |  |  |  | who should act on this next -- Claude or Researcher |  |
| answered_by | TEXT |  |  |  | who recorded the decision/resolution -- Claude or Researcher |  |
indexes: idx_escalation_run_id

### file_manifest (16197 row(s))

cfg_table.use: Filename/path metadata for every file in the project tree (18,653 rows at registration time, 2026-08-28) -- built by lib/manifest.py:rebuild(), a full-tree walk. Content is never read, only path/name/size/mtime facts. Was live and populated for 13 days before being registered here (escalation #972's own orphan check caught the gap while grounding escalation #971).

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| path | TEXT | ✓ |  |  | Project-root-relative path (POSIX slashes) of the file. Prim |  |
| category | TEXT |  | ✓ |  | Coarse classification (iba/session/script/cluster/discovery/ |  |
| file_type | TEXT |  | ✓ |  | Finer-grained type within category, e.g. 'iba-lib', 'analysi |  |
| currency | TEXT |  | ✓ |  | current/archived/cross-reference/historical/backup/other --  |  |
| archived | INTEGER |  | ✓ |  | 1 iff currency='archived' (path contains an archive/ segment |  |
| registry | INTEGER |  |  |  | word_registry id extracted from the filename, when the namin |  |
| word | TEXT |  |  |  | English word extracted from the filename, when present. |  |
| cluster | TEXT |  |  |  | M-code cluster extracted from the filename, when present. |  |
| vcb_batch | INTEGER |  |  |  | Verse-context-batch number extracted from the filename, when |  |
| version | TEXT |  |  |  | The -v{n} version suffix extracted from the filename, when p |  |
| date | TEXT |  |  |  | Date extracted from the filename (compact or hyphenated), wh |  |
| ext | TEXT |  |  |  | File extension, lowercase, including the leading dot. |  |
| size_bytes | INTEGER |  | ✓ |  | File size in bytes at scan time. |  |
| modified_at | TEXT |  | ✓ |  | The file's own filesystem mtime, UTC ISO-8601. |  |
| scanned_at | TEXT |  | ✓ |  | When this row was written by manifest.rebuild() -- identical |  |
indexes: ix_file_manifest_registry, ix_file_manifest_currency, ix_file_manifest_category, sqlite_autoindex_file_manifest_1

### folder_purpose (959 row(s))

cfg_table.use: Reference/data table (like bible_research.db's books, NOT a cfg_* rule table) -- one row per folder in the project tree, seeded from a full census (outputs/folder-census-20260828.csv, 793 folders). Gives the researcher visibility into every live folder's purpose/status and lets folder-classifying code (lib/manifest.py) read a governed source instead of hardcoded prefix rules. Escalation #971, iba/docs/folder-purpose-governance-plan-v5-20260828.md.

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| folder_path | TEXT | ✓ |  |  | Project-root-relative folder prefix, POSIX slashes, no trail |  |
| top_level_root | TEXT |  | ✓ |  | First path segment (or '(repo root)' for the root itself) -- |  |
| depth | INTEGER |  | ✓ |  | Path segment count; 0 = repo root. |  |
| parent_path | TEXT |  | ✓ |  | This folder's immediate parent's folder_path. |  |
| direct_file_count | INTEGER |  | ✓ |  | Files directly in this folder, not counting subfolders -- re |  |
| recursive_file_count | INTEGER |  | ✓ |  | Files in this folder and everything under it -- Method A-ref |  |
| direct_subfolder_count | INTEGER |  | ✓ |  | Immediate child folders -- Method A-refreshed. |  |
| top_ext_direct | TEXT |  |  |  | Up to 5 file extensions by count among this folder's direct  |  |
| last_modified_direct | TEXT |  |  |  | Latest mtime among this folder's direct files, UTC ISO-8601  |  |
| governed_by_setting | TEXT |  |  |  | Which cfg_setting key(s) already point at this exact folder  |  |
| manifest_category | TEXT |  |  |  | What file_manifest.category a file in this folder should get |  |
| manifest_currency | TEXT |  |  |  | Same, for file_manifest.currency -- NULL until set. |  |
| type | TEXT |  |  |  | archive|operations|results (cfg_enum folder_purpose_type) -- |  |
| status | TEXT |  |  |  | authoritative|mixed|reallocate|stale|deleted (cfg_enum folde |  |
| usage_description | TEXT |  |  |  | Free-text description of what this folder is actually for, i |  |
| added_at | TEXT |  | ✓ |  | When this row was first created. |  |
| last_reviewed_at | TEXT |  |  |  | When type/status/usage_description were last confirmed accur |  |
indexes: ix_folder_purpose_type, ix_folder_purpose_status, ix_folder_purpose_top_level_root, sqlite_autoindex_folder_purpose_1

### hib (21 row(s))

cfg_table.use: one row per Human Inner Being identified in a scope (debate digest Step 1) -- scope-wide, not passage-scoped: the same HIB recurs across many passages of a book.

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  | surrogate PK |  |
| book | TEXT |  | ✓ |  | OSIS book code, same convention as verse.osisId's book segme |  |
| label | TEXT |  | ✓ |  | e.g. 'Daniel', 'the four youths', 'King Belshazzar' |  |
| kind | TEXT |  | ✓ |  | named_individual | unnamed_individual | named_collection | u |  |
| first_verse_id | INTEGER |  |  | verse.id | anchor -- where this HIB was first identified |  |
| created_at | TEXT |  | ✓ |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  | version-aware soft-delete, standard convention |  |
indexes: idx_hib_first_verse_id

### hib_referent_option (0 row(s))

cfg_table.use: one row per grammatically-live referent-crux reading (T4), child of hib.

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  | surrogate PK |  |
| hib_id | INTEGER |  | ✓ | hib.id | the HIB this referent-crux reading belongs to |  |
| reading_text | TEXT |  | ✓ |  | one grammatically-live candidate reading (T4) -- e.g. one op |  |
| textual_grounds | TEXT |  |  |  | why this reading is live |  |
| adopted | INTEGER |  | ✓ |  | exactly one row per hib_id should be 1 -- the explicit choic |  |
| ordinal | INTEGER |  | ✓ |  |  | no use text |
| created_at | TEXT |  | ✓ |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  | version-aware soft-delete |  |
indexes: idx_hib_referent_option_hib_id

### lemma_inventory (11781 row(s))

cfg_table.use: L4b seed substrate; imported from the old study, NOT derived from the registry, so the seed is a real completeness control

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  | surrogate key |  |
| lemma_key | TEXT |  | ✓ |  | base Strong's, sub-letters stripped |  |
| gloss | TEXT |  |  |  | the lemma's English gloss — the meaning the net matches on |  |
| language | TEXT |  |  |  | Hebrew/Greek |  |
| source | TEXT |  |  |  | import provenance |  |
| created_at | TEXT |  |  |  | when imported |  |
| deleted | INTEGER |  |  |  | soft delete |  |
indexes: idx_lemma_inventory_live_unique, sqlite_autoindex_lemma_inventory_1

### operation (121 row(s))

cfg_table.use: the operation for a registered phenomenon (Step 4-5 output) -- phenomenon_id NOT NULL enforces Part B.12 at the DB level.

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  | surrogate PK |  |
| phenomenon_id | INTEGER |  | ✓ | phenomenon.id | NOT NULL by design -- the DB-level enforcement of WA-interpr |  |
| process | TEXT |  |  |  | state/status, or a movement (come from/go to/impact on/emerg |  |
| action_type | TEXT |  |  |  | short verb-based label (Q11) -- a label, not a controlled vo |  |
| decision | TEXT |  |  |  | 'retain' | 'set_aside' | 'retain_referential' | 'recorded_si |  |
| observation_text | TEXT |  |  |  | what the text/span-data states, Strong's codes cited |  |
| description_text | TEXT |  |  |  | debate digest Step 5's descriptive write-up |  |
| created_at | TEXT |  | ✓ |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  | version-aware soft-delete |  |
indexes: idx_operation_phenomenon_id

### operation_party (136 row(s))

cfg_table.use: one row per source/target of an operation (plural-capable, v1.5 step1 note a), child of operation.

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  | surrogate PK |  |
| operation_id | INTEGER |  | ✓ | operation.id |  | no use text |
| role | TEXT |  | ✓ |  | 'source' | 'target' |  |
| kind | TEXT |  | ✓ |  | 'self' | 'human' | 'non_human' | 'object_situation' | 'none' |  |
| detail | TEXT |  |  |  | which human/object, if named |  |
| enablement_only | INTEGER |  | ✓ |  | role='source' rows only -- Part B.5's source-of-state vs sou |  |
| ordinal | INTEGER |  | ✓ |  | a phenomenon's operation can have multiple sources/targets ( |  |
| created_at | TEXT |  | ✓ |  | ISO-8601 UTC |  |
| hib_id | INTEGER |  |  | hib.id | which registered HIB this source/target party IS, when it is |  |
| deleted | INTEGER |  | ✓ |  | version-aware soft-delete |  |
indexes: idx_operation_party_operation_id, idx_operation_party_hib_id

### passage (42 row(s) — RETIRED, see note above)

cfg_table.use: extends a characteristic's context to adjacent verses for assessing movement/process/qualifying spans; NOT a thematic unit

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  | surrogate key |  |
| book | TEXT |  | ✓ |  | OSIS book code |  |
| anchor_verse_id | INTEGER |  | ✓ | verse.id | first verse of the run — the anchor |  |
| start_chapter | INTEGER |  |  |  | range start chapter - now populated by the verse-fanout trac |  |
| start_verse | INTEGER |  |  |  | range start verse - now populated by the verse-fanout tracki |  |
| end_chapter | INTEGER |  |  |  | range end chapter - now populated by the verse-fanout tracki |  |
| end_verse | INTEGER |  |  |  | range end verse - now populated by the verse-fanout tracking |  |
| ref | TEXT |  |  |  | human range - now populated by the verse-fanout tracking mec |  |
| verse_count | INTEGER |  |  |  | count of verses in the range - now populated by the verse-fa |  |
| rule | TEXT |  |  |  | char-continuity | maximal - DORMANT since passage.build reti |  |
| source | TEXT |  |  |  | passage-build | single-verse-emergent - DORMANT since passag |  |
| needs_review | INTEGER |  |  |  | 1 when verse_count > passage.review_over (passage.build only |  |
| created_at | TEXT |  |  |  | when this passage row was created - now populated by the ver |  |
| deleted | INTEGER |  |  |  | soft delete |  |
| book_label | TEXT |  |  |  | human-facing subfolder name (e.g. 'Daniel') used by the vers |  |
| verse_span_meaning_path | TEXT |  |  |  | path to this range's report.verse_span_meaning output, writt |  |
| verse_span_meaning_written_at | TEXT |  |  |  | UTC timestamp of the last report.verse_span_meaning write fo |  |
| debate_path | TEXT |  |  |  | path to this range's report.passage_debate output (scaffold  |  |
| debate_written_at | TEXT |  |  |  | UTC timestamp of the last report.passage_debate write for th |  |
| debate_status | TEXT |  |  |  | 'scaffold' (auto-generated, still has unreplaced <!-- fill i |  |
| phenomena_complete_at | TEXT |  |  |  | NULL until the debate digest Step 3 phase gate is confirmed  |  |
| open_decisions_note | TEXT |  |  |  | Part C section 8 -- short free-text summary of open decision |  |
| story_summary | TEXT |  |  |  | Step 2's high-level story synthesis for this passage's scope |  |
| feasibility_note | TEXT |  |  |  | Step 2's own self-assessment record: why this scope was judg |  |
indexes: idx_passage_live_unique, idx_passage_anchor_verse_id, idx_passage_range_live

### passage_emergent_question (3 row(s))

cfg_table.use: Part C section 6 (Q10/B.9/B.12) -- interpretive forks and genuine literary/structural observations, tracked per passage, never merged across passages.

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  | surrogate PK |  |
| passage_id | INTEGER |  | ✓ | passage.id |  | no use text |
| verse_id | INTEGER |  |  | verse.id | nullable -- an emergent question can span the whole passage |  |
| question_text | TEXT |  | ✓ |  | Part C section 6 / Q10 -- interpretive forks (Part B.9) and  |  |
| kind | TEXT |  | ✓ |  | 'interpretive_fork' | 'literary_structural' | 'other' |  |
| ordinal | INTEGER |  | ✓ |  | natural key within passage_id for the reconciliation writer |  |
| created_at | TEXT |  | ✓ |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  | version-aware soft-delete |  |
indexes: idx_passage_emergent_question_verse_id, idx_passage_emergent_question_passage_id, idx_passage_emergent_question_live_unique

### passage_insufficiency (1 row(s))

cfg_table.use: Part C section 5 (Q9/B.7) -- data the base extract does not carry, named not filled.

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  | surrogate PK |  |
| passage_id | INTEGER |  | ✓ | passage.id |  | no use text |
| verse_id | INTEGER |  |  | verse.id | nullable -- an insufficiency can be passage-wide, not always |  |
| note | TEXT |  | ✓ |  | Part C section 5 / Q9 / Part B.7 -- data the base extract do |  |
| ordinal | INTEGER |  | ✓ |  | natural key within passage_id for the reconciliation writer |  |
| created_at | TEXT |  | ✓ |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  | version-aware soft-delete |  |
indexes: idx_passage_insufficiency_verse_id, idx_passage_insufficiency_passage_id, idx_passage_insufficiency_live_unique

### passage_linkage (3 row(s))

cfg_table.use: Part C section 4 (Q7) -- linkages between two specific, already-registered operations in the same passage, and surfaced non-linkages.

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  | surrogate PK |  |
| passage_id | INTEGER |  | ✓ | passage.id |  | no use text |
| from_operation_id | INTEGER |  | ✓ | operation.id | Part C section 4 / Q7 -- a linkage connects two SPECIFIC, al |  |
| to_operation_id | INTEGER |  | ✓ | operation.id |  | no use text |
| note | TEXT |  | ✓ |  | what the linkage is -- also where a Q7 SURFACED ABSENCE gets |  |
| ordinal | INTEGER |  | ✓ |  | natural key within passage_id for the reconciliation writer |  |
| created_at | TEXT |  | ✓ |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  | version-aware soft-delete |  |
indexes: idx_passage_linkage_to_operation_id, idx_passage_linkage_passage_id, idx_passage_linkage_from_operation_id, idx_passage_linkage_live_unique

### passage_validation_note (4 row(s))

cfg_table.use: Part C section 7 (Phase 3) -- the closing re-examination of the passage's own phenomena/operations, corrected before the debate is considered filled.

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  | surrogate PK |  |
| passage_id | INTEGER |  | ✓ | passage.id |  | no use text |
| phenomenon_id | INTEGER |  |  | phenomenon.id | nullable -- a validation finding can be about the passage's  |  |
| finding_text | TEXT |  | ✓ |  | Part C section 7 / Phase 3 step 6 -- is this genuinely an in |  |
| corrected | INTEGER |  | ✓ |  | WA-passage-read-guidance v1.5 step 6: a failure found here i |  |
| ordinal | INTEGER |  | ✓ |  | natural key within passage_id for the reconciliation writer |  |
| created_at | TEXT |  | ✓ |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  | version-aware soft-delete |  |
indexes: idx_passage_validation_note_phenomenon_id, idx_passage_validation_note_passage_id, idx_passage_validation_note_live_unique

### phenomenon (121 row(s))

cfg_table.use: the phenomena register (Step 3 output) -- one row per HIB per verse per passage.

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  | surrogate PK |  |
| passage_id | INTEGER |  | ✓ | passage.id |  | no use text |
| verse_id | INTEGER |  | ✓ | verse.id |  | no use text |
| hib_id | INTEGER |  | ✓ | hib.id |  | no use text |
| description | TEXT |  | ✓ |  | the phenomenon: a state, disposition, or characteristic of t |  |
| textual_warrant | TEXT |  |  |  | the verb/clause/stated-silence that grounds it (WA-passage-r |  |
| status | TEXT |  | ✓ |  | 'stated' | 'inferred' | 'silent' -- 'no phenomenon found, si |  |
| ordinal | INTEGER |  | ✓ |  | allows more than one phenomenon for the same HIB in the same |  |
| created_at | TEXT |  | ✓ |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  | version-aware soft-delete |  |
indexes: idx_phenomenon_verse_id, idx_phenomenon_passage_id, idx_phenomenon_hib_id, idx_phenomenon_live_unique

### run (2361 row(s))

cfg_table.use: what ran, pinned to a config version, and RESUMABLE (O7): state + resume_point persisted so a pause survives the process.

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  | surrogate key |  |
| run_id | TEXT |  | ✓ |  | the run identifier |  |
| work_package | TEXT |  |  |  | which package |  |
| params | TEXT |  |  |  | JSON of the run params |  |
| runs_over | TEXT |  |  |  | the scope value, e.g. the word |  |
| config_version | TEXT |  |  |  | the config that ran — pinned before any work |  |
| state | TEXT |  |  |  | running | paused | done | failed |  |
| resume_point | TEXT |  |  |  | the step to resume at on continue |  |
| started_at | TEXT |  |  |  | start |  |
| ended_at | TEXT |  |  |  | end |  |
| outcome | TEXT |  |  |  | the final result |  |
indexes: sqlite_autoindex_run_1

### span (378149 row(s))

cfg_table.use: L4a - SOURCE, immutable. A parse of verse.preview. position is the running TAG index; (verse, position) is the key. strong_variant/morph_code may hold more than one space-separated code when STEP's own HTML combines them on one tag (corrected 2026-07-25 - see migration/rebuild_span_combined_units.py; the old one-row-per-code model split a combined unit and misattributed surface text).

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  | surrogate key |  |
| verse_id | INTEGER |  | ✓ | verse.id | the verse |  |
| position | INTEGER |  | ✓ |  | running code index in the verse — the key with verse_id |  |
| surface | TEXT |  |  |  | the English word this code belongs to; repeats across a word |  |
| strong_variant | TEXT |  |  | strong.strongNumber | one or more strong codes, space-separated - STEP's HTML <spa |  |
| morph_code | TEXT |  |  |  | the grammatical layer — one, aligned with the code |  |
| is_particle | INTEGER |  |  |  | 1 only if EVERY code on the tag is a grammar-particle code ( |  |
| built_at | TEXT |  |  |  | raw time |  |
| deleted | INTEGER |  |  |  | soft delete |  |
indexes: idx_span_live_unique, idx_span_verse_id, sqlite_autoindex_span_1

### span_candidate (83914 row(s))

cfg_table.use: over-inclusive candidate stamp; the lexical stage later tests each in context

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  | surrogate key |  |
| span_id | INTEGER |  | ✓ | span.id | the L4a span stamped |  |
| lemma_key | TEXT |  |  |  | base Strong's of the span (denormalised for continuity/join) |  |
| candidate_tag | TEXT |  |  |  | the IB label from the seed |  |
| seed_source | TEXT |  |  |  | DORMANT - candidate.set retired 2026-07-23; no active mechan |  |
| set_at | TEXT |  |  |  | DORMANT - candidate.set retired 2026-07-23; no active mechan |  |
| deleted | INTEGER |  |  |  | soft delete |  |
indexes: idx_span_candidate_live_unique, idx_span_candidate_span_id, sqlite_autoindex_span_candidate_1

### strong (15293 row(s))

cfg_table.use: L2 — the strong's identity. The meaning is normalised out (O4): it lives in strong_sense / strong_meaning_tree / strong_lexicon.

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| strongNumber | TEXT | ✓ |  |  | the resolved Strong's code — the key |  |
| accentedUnicode | TEXT |  |  |  | the actual Hebrew/Greek word |  |
| stepGloss | TEXT |  |  |  | short English sense |  |
| stepTransliteration | TEXT |  |  |  | romanised form; never shown without the gloss |  |
| language | TEXT |  |  |  | Hebrew/Greek from the code prefix |  |
| count | INTEGER |  |  |  | STEP token frequency — NOT a verse count, may be capped |  |
| freqList | TEXT |  |  |  | raw frequency distribution |  |
| created_at | TEXT |  |  |  | when first fetched |  |
| deleted | INTEGER |  |  |  | soft delete |  |
| origin | TEXT |  | ✓ |  | 'word' = deliberately onboarded for a registry word (raw.dis |  |
indexes: sqlite_autoindex_strong_1

### strong_lexicon (5639 row(s))

cfg_table.use: the large lexicon text — separate because rarely scanned

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| strong | TEXT | ✓ |  | strong.strongNumber | the strong |  |
| lsj | TEXT |  |  |  | LSJ entry (Greek) |  |
| mounce | TEXT |  |  |  | Mounce short def (Greek) |  |
| deleted | INTEGER |  |  |  | soft delete |  |
indexes: idx_strong_lexicon_strong, sqlite_autoindex_strong_lexicon_1

### strong_lsj_parsed (36199 row(s))

cfg_table.use: L2b — the parsed classical-Greek lexicon layer over strong_lexicon.lsj (raw). Sense blocks split on LSJ's own <LevelN>/<br> structure; gloss kept whole within a block, not exploded on internal commas.

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  | surrogate key |  |
| strong | TEXT |  | ✓ | strong.strongNumber | the full strong code this LSJ sense belongs to |  |
| sense_label | TEXT |  |  |  | LSJ sense position, e.g. I / I.2 / II.2.b, or 'headword' |  |
| gloss | TEXT |  |  |  | the sense's bold-span gloss text, kept whole (no comma split |  |
| note | TEXT |  |  |  | dialect/grammar labels, connective prose — everything in the |  |
| row_type | TEXT |  |  |  | headword for the entry's own headword row(s), lookup for eve |  |
| deleted | INTEGER |  |  |  | soft delete |  |
indexes: idx_strong_lsj_parsed_strong

### strong_meaning_parsed (47113 row(s))

cfg_table.use: L2b — the parsed meaning layer over strong_meaning_tree (raw). Segment-scoped: refs/note belong to the exact <b> span they followed, not pooled across the whole source row (the original extract's bug, fixed before this table existed). Comma/semicolon are NOT sense separators here — only a literal line break splits a gloss further.

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  | surrogate key |  |
| lemma_key | TEXT |  | ✓ |  | the base code this parsed sense belongs to (never a sub-entr |  |
| sort | INTEGER |  |  |  | order within the source sense tree |  |
| sense_code | TEXT |  |  |  | the tree position, e.g. 1a1a) — or the sense_code column val |  |
| gloss | TEXT |  |  |  | one exploded gloss term, kept whole (no comma/semicolon spli |  |
| verse_refs | TEXT |  |  |  | verse citations scoped to this gloss's own <b> span, semicol |  |
| note | TEXT |  |  |  | commentary scoped to this gloss's own segment, not pooled ac |  |
| row_type | TEXT |  |  |  | lookup / description / not applicable — lexicon_split_common |  |
| deleted | INTEGER |  |  |  | soft delete |  |
| strong_variant | TEXT |  |  | strong.strongNumber |  | no use text |
indexes: idx_strong_meaning_parsed_strong_variant

### strong_meaning_tree (40315 row(s))

cfg_table.use: the lemma's full range — read rarely, only when the broader context is needed. Keyed on the lemma (shared across its senses, which the prototype proved).

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  | surrogate key |  |
| lemma_key | TEXT |  | ✓ |  | the base code the tree belongs to |  |
| sense_code | TEXT |  |  |  | the tree position: 1), 1a), 1b1) |  |
| sense_text | TEXT |  |  |  | the sense line |  |
| sort | INTEGER |  |  |  | order within the tree |  |
| deleted | INTEGER |  |  |  | soft delete |  |
| strong_variant | TEXT |  |  | strong.strongNumber |  | no use text |
indexes: idx_strong_meaning_tree_strong_variant

### strong_mounce_parsed (5742 row(s))

cfg_table.use: L2b — the parsed Greek lexicon layer over strong_lexicon.mounce (raw). Split ONLY on <br> (the source's real line breaks); comma/semicolon within one line are punctuation inside a sense, not sense separators.

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  | surrogate key |  |
| strong | TEXT |  | ✓ | strong.strongNumber | the full strong code this Mounce line belongs to |  |
| mounce_parsed | TEXT |  |  |  | one <br>-delimited line of Mounce's entry, kept whole (no co |  |
| row_type | TEXT |  |  |  | lookup / description — lexicon_split_common.classify_row() |  |
| deleted | INTEGER |  |  |  | soft delete |  |
indexes: idx_strong_mounce_parsed_strong

### strong_related (87535 row(s))

cfg_table.use: L2b — NOT derived from any raw table; fetched live from STEP per full strong code (lib.stepapi.Step.call2_getInfo, vocabInfos[0].relatedNos) since no raw table captures this. related_strong is unconstrained — STEP can name a code this app has never onboarded via raw.detail.

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  | surrogate key |  |
| strong | TEXT |  | ✓ | strong.strongNumber | the full code of the SOURCE term STEP was asked about |  |
| related_strong | TEXT |  | ✓ |  | the full code of the RELATED term — may have no strong row o |  |
| related_form | TEXT |  |  |  | the related term's native-script form |  |
| related_transliteration | TEXT |  |  |  | the related term's transliteration |  |
| related_gloss | TEXT |  |  |  | the related term's own short gloss |  |
| deleted | INTEGER |  |  |  | soft delete |  |
indexes: idx_strong_related_strong

### strong_sense (15293 row(s))

cfg_table.use: the span's meaning, read constantly. The head is the first line of mediumDef (the sense); is_own_lemma marks a code that is its own lemma, where the gloss carries the sense.

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| strong | TEXT | ✓ |  | strong.strongNumber | the strong |  |
| head | TEXT |  |  |  | the sense — THE SPAN'S MEANING |  |
| is_own_lemma | INTEGER |  |  |  | 1 = no ': ' head; the code is its own lemma and the gloss is |  |
| deleted | INTEGER |  |  |  | soft delete |  |
indexes: idx_strong_sense_strong, sqlite_autoindex_strong_sense_1

### strong_verse (132718 row(s))

cfg_table.use: the source's assertion 'this strong is in this verse'. The check side against span (what the parse found).

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  | surrogate key |  |
| strong | TEXT |  | ✓ | strong.strongNumber | the strong searched |  |
| verse_id | INTEGER |  | ✓ | verse.id | the verse returned |  |
| deleted | INTEGER |  |  |  | soft delete |  |
indexes: idx_strong_verse_live_unique, idx_strong_verse_verse_id, idx_strong_verse_strong, sqlite_autoindex_strong_verse_1

### validation_result (39457 row(s))

cfg_table.use: util.validation — the outcome of a check, persisted so it can be inspected and reported. A passed check is a recorded fact, not just an advancing run.

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  | surrogate key |  |
| run_id | TEXT |  | ✓ | run.run_id | the run that ran the check |  |
| word | TEXT |  |  |  | the word the check was over |  |
| step | TEXT |  |  |  | the step that ran it |  |
| check_name | TEXT |  |  |  | which check |  |
| result | TEXT |  |  |  | pass | fail |  |
| detail | TEXT |  |  |  | the specifics — counts, what failed |  |
| ran_at | TEXT |  |  |  | when |  |
| deleted | INTEGER |  |  |  | soft delete |  |
indexes: idx_validation_result_run_id

### verse (29759 row(s))

cfg_table.use: L3 — the addressable verse. preview is the full interlinear, kept verbatim so span is re-derivable.

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  | surrogate key |  |
| osisId | TEXT |  | ✓ |  | the machine key, e.g. Matt.23.28 |  |
| reference | TEXT |  |  |  | human reference, e.g. Mat 23:28 |  |
| preview | TEXT |  |  |  | the full interlinear HTML — the source of span |  |
| step_version | TEXT |  |  |  | provenance — which STEP module |  |
| created_at | TEXT |  |  |  | when first built |  |
| deleted | INTEGER |  |  |  | soft delete |  |
| text | TEXT |  |  |  | The verse full text (ESV_th per Start-Iba.ps1 STEP tag) -- t |  |
indexes: idx_verse_live_unique, sqlite_autoindex_verse_1

### verse_hib (235 row(s))

cfg_table.use: one row per HIB present/a presumptive candidate in a given verse (Step 1's per-verse sweep) -- the input B4's future HIB-continuity passage-boundary rule reads from.

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  | surrogate PK |  |
| verse_id | INTEGER |  | ✓ | verse.id |  | no use text |
| hib_id | INTEGER |  | ✓ | hib.id | this HIB is present/a presumptive candidate in this verse (d |  |
| created_at | TEXT |  | ✓ |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  | version-aware soft-delete |  |
indexes: idx_verse_hib_verse_id, idx_verse_hib_hib_id, idx_verse_hib_live_unique

### verse_lexical (552353 row(s))

cfg_table.use: L4b — DERIVED, version-aware. The mechanical T1-T3 reading: role classification + stem/voice-selected sense + named-not-resolved ambiguity, per code. Read by report.verse_lexical and, downstream, by T4-T9 — never by re-deriving from span/strong/strong_meaning_parsed directly.

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  | surrogate PK |  |
| span_id | INTEGER |  | ✓ | span.id | which span this reading is for — a span may carry several co |  |
| verse_id | INTEGER |  | ✓ | verse.id | denormalized from span, matches verse_passage's own preceden |  |
| code_ordinal | INTEGER |  | ✓ |  | position of this code within the span's space-joined strong_ |  |
| strong | TEXT |  |  | strong.strongNumber | the single code this row resolves — may be NULL only if stro |  |
| morph_code | TEXT |  |  |  | this code's own morph slice (space-split from span.morph_cod |  |
| role | TEXT |  | ✓ |  | 'content' (independent lexical item) or 'function' (grammati |  |
| status | TEXT |  | ✓ |  | 'resolved' (strong row found, sense pulled -- content or fun |  |
| resolved_sense | TEXT |  |  |  | stem/voice-selected sense text for 'resolved' rows (content  |  |
| ambiguity_note | TEXT |  |  |  | set only when the sibling/base-fallback ambiguity check fire |  |
| created_at | TEXT |  | ✓ |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  | version-aware soft-delete — rewriting a (span_id, code_ordin |  |
indexes: idx_verse_lexical_verse_id, idx_verse_lexical_strong, idx_verse_lexical_span_id, idx_verse_lexical_live_unique

### verse_passage (777 row(s) — RETIRED, see note above)

cfg_table.use: which passage a verse belongs to; a verse is in at most one passage

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  | surrogate key |  |
| passage_id | INTEGER |  | ✓ | passage.id | the passage |  |
| verse_id | INTEGER |  | ✓ | verse.id | the verse (unique — one passage per verse) |  |
| is_anchor | INTEGER |  |  |  | 1 on the anchor verse - now populated by the verse-fanout tr |  |
| created_at | TEXT |  |  |  | when this link was created - now populated by the verse-fano |  |
| deleted | INTEGER |  |  |  | soft delete |  |
indexes: idx_verse_passage_live_unique, idx_verse_passage_verse_id, idx_verse_passage_passage_id, idx_verse_passage_verse_id_live

### word_registry (180 row(s))

cfg_table.use: the study's entry point; scope of a new-word run

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  | surrogate key |  |
| word | TEXT |  | ✓ |  | the English word |  |
| source | TEXT |  |  |  | why it was registered — the growth trigger |  |
| status | TEXT |  |  |  | registry processing stage |  |
| created_at | TEXT |  |  |  | when registered |  |
| deleted | INTEGER |  |  |  | soft delete |  |
indexes: idx_word_registry_live_unique, sqlite_autoindex_word_registry_1

### word_strong (4874 row(s))

cfg_table.use: L1 — the discovery record: which strongs a word maps to. These strongs are the basis for L2. Carries the link only, no strong detail.

| column | type | pk | notnull | fk | cfg use | discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  | surrogate key |  |
| word_id | INTEGER |  | ✓ | word_registry.id | the word |  |
| strong | TEXT |  | ✓ | strong.strongNumber | a strong the word returned |  |
| deleted | INTEGER |  |  |  | soft delete |  |
indexes: idx_word_strong_live_unique, idx_word_strong_word_id, idx_word_strong_strong, sqlite_autoindex_word_strong_1
