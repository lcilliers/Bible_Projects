-- ═══════════════════════════════════════════════════════════════════════════
-- Bible Research SQLite schema — post-DBR migrations M19-M28 (2026-04-19)
-- ═══════════════════════════════════════════════════════════════════════════
-- Schema version: 3.10.0
-- Regenerated from the post-migration DB copy for the canonical target state.
-- Prior file preserved as create_tables.sql.pre_DBR_bak

-- ── book_code_variants ──
CREATE TABLE book_code_variants (
        code    TEXT    PRIMARY KEY,
        book_id INTEGER NOT NULL REFERENCES books(id)
    );

-- ── books ──
CREATE TABLE books (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT    NOT NULL UNIQUE,           -- e.g. "John"
    abbreviation TEXT   NOT NULL UNIQUE,           -- e.g. "Jn"
    testament   TEXT    NOT NULL                   -- "OT" or "NT"
                CHECK (testament IN ('OT', 'NT')),
    book_order  INTEGER NOT NULL UNIQUE            -- canonical order 1–66
, full_name TEXT, short_code TEXT, verse_count INTEGER NOT NULL DEFAULT 0, last_updated TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%S','now')));

-- ── engine_run_log ──
CREATE TABLE engine_run_log (
            id                   INTEGER PRIMARY KEY AUTOINCREMENT,
            run_id               TEXT    NOT NULL UNIQUE,
            mode                 TEXT    NOT NULL,
            target_registry_ids  TEXT,
            started_at           TEXT    NOT NULL,
            completed_at         TEXT,
            outcome              TEXT,
            words_attempted      INTEGER DEFAULT 0,
            words_complete       INTEGER DEFAULT 0,
            words_stopped        INTEGER DEFAULT 0,
            total_terms_new      INTEGER DEFAULT 0,
            total_terms_xref     INTEGER DEFAULT 0,
            total_verses_inserted INTEGER DEFAULT 0,
            total_verses_filtered INTEGER DEFAULT 0,
            total_meanings_parsed INTEGER DEFAULT 0,
            error_detail         TEXT,
            resume_from          TEXT
        );

-- ── engine_stream_checkpoint ──
CREATE TABLE engine_stream_checkpoint (
            id               INTEGER PRIMARY KEY AUTOINCREMENT,
            run_id           TEXT    NOT NULL REFERENCES engine_run_log(run_id),
            stream_name      TEXT    NOT NULL,
            status           TEXT    NOT NULL DEFAULT 'pending',
            last_registry_id TEXT,
            last_strong      TEXT,
            rows_written     INTEGER DEFAULT 0,
            rows_filtered    INTEGER DEFAULT 0,
            error_detail     TEXT,
            started_at       TEXT,
            completed_at     TEXT
        );

-- ── mti_term_cross_refs ──
CREATE TABLE "mti_term_cross_refs" (
    id                  INTEGER PRIMARY KEY,
    mti_term_id         INTEGER NOT NULL REFERENCES mti_terms(id) ON DELETE CASCADE,
    registry            TEXT NOT NULL,
    registry_fk         INTEGER REFERENCES word_registry(id),
    word                TEXT,
    part                TEXT,
    word_data_reference TEXT,
    UNIQUE (mti_term_id, registry, word, part)
);

-- ── mti_term_flags ──
CREATE TABLE mti_term_flags (
            mti_term_id INTEGER NOT NULL REFERENCES mti_terms(id),
            flag_id     INTEGER NOT NULL REFERENCES phase2_flag_types(id),
            PRIMARY KEY (mti_term_id, flag_id)
        );

-- ── mti_terms ──
CREATE TABLE "mti_terms" (
    id                  INTEGER PRIMARY KEY,
    strongs_number      TEXT,
    transliteration     TEXT NOT NULL,
    gloss               TEXT NOT NULL,
    language            TEXT,
    owning_registry     TEXT,
    owning_registry_fk  INTEGER REFERENCES word_registry(id) ON DELETE RESTRICT,
    owning_word         TEXT,
    owning_part         TEXT,
    word_data_reference TEXT,
    word_data_ref_fk    INTEGER REFERENCES wa_file_index(id),
    status              TEXT,
    exclusion_reason    TEXT,
    extraction_date     TEXT,
    strongs_reconciled  INTEGER DEFAULT 0,
    anchor_note         TEXT,
    last_changed        TEXT DEFAULT (datetime('now'))
, delete_flagged INTEGER DEFAULT 0);

-- ── phase2_flag_types ──
CREATE TABLE phase2_flag_types (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            flag_code   TEXT NOT NULL UNIQUE,
            description TEXT
        );

-- ── prose_section ──
CREATE TABLE prose_section (
            id                INTEGER PRIMARY KEY,
            registry_id       INTEGER NOT NULL REFERENCES word_registry(id),
            section_type_id   INTEGER NOT NULL REFERENCES prose_section_type(id),
            heading           TEXT,
            body              TEXT    NOT NULL,
            word_count        INTEGER NOT NULL DEFAULT 0,
            status            TEXT    NOT NULL,
            version           INTEGER NOT NULL DEFAULT 1,
            supersedes_id     INTEGER REFERENCES prose_section(id),
            superseded_by_id  INTEGER REFERENCES prose_section(id),
            author            TEXT    NOT NULL,
            created_at        TEXT    NOT NULL,
            approved_at       TEXT,
            approved_by       TEXT,
            metadata_json     TEXT,
            source_file       TEXT,
            delete_flagged    INTEGER NOT NULL DEFAULT 0,
            CHECK (status IN ('draft','in_review','approved','archived')),
            CHECK (author IN ('claude_ai','claude_code','researcher'))
        );

-- ── prose_section_dimension_link ──
CREATE TABLE prose_section_dimension_link (
            prose_section_id  INTEGER NOT NULL REFERENCES prose_section(id),
            dimension_id      INTEGER NOT NULL,
            link_type         TEXT    NOT NULL DEFAULT 'discusses',
            created_at        TEXT    NOT NULL DEFAULT (datetime('now')),
            PRIMARY KEY (prose_section_id, dimension_id, link_type)
        );

-- ── prose_section_finding_link ──
CREATE TABLE prose_section_finding_link (
            prose_section_id  INTEGER NOT NULL REFERENCES prose_section(id),
            finding_id        INTEGER NOT NULL REFERENCES wa_session_b_findings(id),
            link_type         TEXT    NOT NULL DEFAULT 'discusses',
            created_at        TEXT    NOT NULL DEFAULT (datetime('now')),
            PRIMARY KEY (prose_section_id, finding_id, link_type)
        );

-- ── prose_section_fts ──
CREATE VIRTUAL TABLE prose_section_fts USING fts5(
            body,
            heading,
            section_type_code UNINDEXED,
            registry_id UNINDEXED,
            status UNINDEXED,
            tokenize='porter unicode61 remove_diacritics 2'
        );

-- ── prose_section_fts_config ──
CREATE TABLE 'prose_section_fts_config'(k PRIMARY KEY, v) WITHOUT ROWID;

-- ── prose_section_fts_content ──
CREATE TABLE 'prose_section_fts_content'(id INTEGER PRIMARY KEY, c0, c1, c2, c3, c4);

-- ── prose_section_fts_data ──
CREATE TABLE 'prose_section_fts_data'(id INTEGER PRIMARY KEY, block BLOB);

-- ── prose_section_fts_docsize ──
CREATE TABLE 'prose_section_fts_docsize'(id INTEGER PRIMARY KEY, sz BLOB);

-- ── prose_section_fts_idx ──
CREATE TABLE 'prose_section_fts_idx'(segid, term, pgno, PRIMARY KEY(segid, term)) WITHOUT ROWID;

-- ── prose_section_type ──
CREATE TABLE prose_section_type (
            id                   INTEGER PRIMARY KEY,
            code                 TEXT    NOT NULL UNIQUE,
            label                TEXT    NOT NULL,
            source_stage         TEXT    NOT NULL,
            lifecycle_tag        TEXT,
            chapter_no           INTEGER,
            description          TEXT,
            expected_length_min  INTEGER,
            expected_length_max  INTEGER,
            sort_order           INTEGER NOT NULL DEFAULT 0,
            delete_flagged       INTEGER NOT NULL DEFAULT 0,
            created_at           TEXT    NOT NULL DEFAULT (datetime('now'))
        );

-- ── schema_version ──
CREATE TABLE "schema_version" (
            id                 INTEGER PRIMARY KEY,
            version_code       TEXT    NOT NULL,
            applied_at         TEXT    NOT NULL,
            migration_history  TEXT,
            engine_min_version TEXT
        );

-- ── session_d_observations ──
CREATE TABLE session_d_observations (
  id INTEGER PRIMARY KEY,
  run_id TEXT NOT NULL,
  observation_id TEXT NOT NULL UNIQUE,
  observation_type TEXT NOT NULL,
  registries_implicated TEXT NOT NULL,
  terms_implicated TEXT,
  structural_note TEXT,
  source_refs TEXT,
  gate TEXT NOT NULL,
  researcher_flag INTEGER DEFAULT 0,
  raised_date TEXT NOT NULL
);

-- ── session_d_runs ──
CREATE TABLE session_d_runs (
  id INTEGER PRIMARY KEY,
  run_id TEXT NOT NULL UNIQUE,
  run_date TEXT NOT NULL,
  cluster_ref TEXT,
  registries_in_scope TEXT NOT NULL,
  registries_completed_at_run INTEGER,
  session_b_sources TEXT,
  run_summary TEXT,
  json_filename TEXT
);

-- ── session_d_term_links ──
CREATE TABLE session_d_term_links (
  id INTEGER PRIMARY KEY,
  run_id TEXT NOT NULL,
  strongs_id TEXT NOT NULL,
  transliteration TEXT,
  registry_data TEXT NOT NULL,
  status_divergence INTEGER DEFAULT 0,
  gate TEXT NOT NULL,
  raised_date TEXT NOT NULL
);

-- ── session_d_verse_links ──
CREATE TABLE session_d_verse_links (
  id INTEGER PRIMARY KEY,
  run_id TEXT NOT NULL,
  verse_ref TEXT NOT NULL,
  registry_ids TEXT NOT NULL,
  terms_involved TEXT,
  overlap_count INTEGER,
  threshold_met INTEGER DEFAULT 0,
  gate TEXT NOT NULL,
  raised_date TEXT NOT NULL
);

-- ── sources ──
CREATE TABLE sources (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    zotero_key  TEXT    UNIQUE,                    -- Zotero item key (nullable)
    title       TEXT    NOT NULL,
    author      TEXT,
    year        INTEGER,
    source_type TEXT                               -- "commentary", "lexicon", "paper", etc.
);

-- ── term_fetch_log ──
CREATE TABLE term_fetch_log (
            id                   INTEGER PRIMARY KEY AUTOINCREMENT,
            run_id               TEXT    NOT NULL REFERENCES engine_run_log(run_id),
            registry_id          TEXT    NOT NULL,
            strongs_input        TEXT    NOT NULL,
            strongs_resolved     TEXT,
            suffix_resolution    INTEGER DEFAULT 0,
            vocab_status         TEXT,
            verse_status         TEXT,
            verse_count_fetched  INTEGER DEFAULT 0,
            verse_count_stored   INTEGER DEFAULT 0,
            verse_count_filtered INTEGER DEFAULT 0,
            span_conflict        INTEGER DEFAULT 0,
            api_warnings         TEXT,
            fetched_at           TEXT
        );

-- ── themes ──
CREATE TABLE themes (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT    NOT NULL UNIQUE,           -- e.g. "salvation"
    description TEXT
);

-- ── verse_context ──
CREATE TABLE verse_context (
  id              INTEGER PRIMARY KEY,
  verse_record_id INTEGER NOT NULL REFERENCES wa_verse_records(id),
  mti_term_id     INTEGER NOT NULL REFERENCES mti_terms(id),
  group_id        INTEGER REFERENCES verse_context_group(id),
  is_anchor       INTEGER NOT NULL DEFAULT 0,
  is_relevant     INTEGER NOT NULL DEFAULT 0,
  is_related      INTEGER NOT NULL DEFAULT 0,
  notes           TEXT DEFAULT NULL,
  delete_flagged  INTEGER DEFAULT 0, vertical_pass_flag INTEGER DEFAULT 0, set_aside_reason TEXT DEFAULT NULL,
  UNIQUE (verse_record_id, mti_term_id, group_id)
);

-- ── verse_context_group ──
CREATE TABLE verse_context_group (
  id                  INTEGER PRIMARY KEY,
  mti_term_id         INTEGER NOT NULL REFERENCES mti_terms(id),
  group_code          TEXT NOT NULL UNIQUE,
  context_description TEXT NOT NULL,
  notes               TEXT DEFAULT NULL,
  delete_flagged      INTEGER DEFAULT 0
, vertical_pass_flag INTEGER DEFAULT 0);

-- ── wa_cross_registry_links ──
CREATE TABLE wa_cross_registry_links (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            file_id             INTEGER NOT NULL REFERENCES wa_file_index(id),
            linked_word         TEXT,
            linked_registry_id  INTEGER REFERENCES word_registry(id),
            connection_type_id  INTEGER NOT NULL REFERENCES wa_crosslink_type(id),
            connecting_term     TEXT,
            note                TEXT,
            last_changed        TEXT
        );

-- ── wa_crosslink_type ──
CREATE TABLE wa_crosslink_type (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            type_code   TEXT NOT NULL UNIQUE,
            description TEXT
        );

-- ── wa_data_quality_flags ──
CREATE TABLE wa_data_quality_flags (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            file_id      INTEGER NOT NULL REFERENCES wa_file_index(id),
            term_id      TEXT,
            flag_id      INTEGER NOT NULL REFERENCES wa_quality_flag_types(id),
            description  TEXT,
            last_changed TEXT
        );

-- ── wa_dim_review_cluster_log ──
CREATE TABLE wa_dim_review_cluster_log (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  cluster TEXT NOT NULL UNIQUE,
  completed_date TEXT NOT NULL,
  instruction_version TEXT NOT NULL,
  registry_count INTEGER NOT NULL DEFAULT 0,
  group_count INTEGER NOT NULL DEFAULT 0,
  anchored_count INTEGER NOT NULL DEFAULT 0,
  notes TEXT,
  last_modified TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%S','now'))
);

-- ── wa_dimension_index ──
CREATE TABLE wa_dimension_index (
        id                    INTEGER PRIMARY KEY,
        verse_context_group_id INTEGER NOT NULL REFERENCES verse_context_group(id),
        owning_registry_no    INTEGER NOT NULL,
        cluster_assignment    TEXT,
        dimension             TEXT,
        anchor_count          INTEGER DEFAULT 0,
        related_count         INTEGER DEFAULT 0,
        set_aside_count       INTEGER DEFAULT 0,
        total_verse_count     INTEGER DEFAULT 0,
        delete_flagged        INTEGER DEFAULT 0
    , dimension_confidence TEXT DEFAULT NULL, manual_override INTEGER DEFAULT 0, notes TEXT DEFAULT NULL, last_modified TEXT DEFAULT NULL, dominant_subject TEXT DEFAULT NULL);

-- ── wa_file_index ──
CREATE TABLE "wa_file_index" (
    id                           INTEGER PRIMARY KEY,
    filename                     TEXT NOT NULL,
    registry_id                  TEXT NOT NULL,
    word_registry_fk             INTEGER REFERENCES word_registry(id) ON DELETE RESTRICT,
    word                         TEXT NOT NULL,
    part_number                  INTEGER,
    total_parts                  INTEGER,
    is_split                     INTEGER,
    schema_version               TEXT,
    phase                        TEXT,
    produced_date                TEXT,
    source_file                  TEXT,
    translation_used             TEXT,
    specification                TEXT,
    revision_note                TEXT,
    source_list                  TEXT,
    category                     TEXT,
    testament_coverage           TEXT,
    root_families_in_prior_parts TEXT,
    last_changed                 TEXT DEFAULT (datetime('now'))
);

-- ── wa_finding_catalogue_links ──
CREATE TABLE wa_finding_catalogue_links (
    id              INTEGER  PRIMARY KEY AUTOINCREMENT,
    finding_id      INTEGER  NOT NULL REFERENCES wa_session_b_findings(id),
    question_id     INTEGER  NOT NULL REFERENCES wa_obs_question_catalogue(obs_id),
    coverage        TEXT,
    status          TEXT     NOT NULL DEFAULT 'suggested',
    pattern_type    TEXT,
    mapped_date     TEXT,
    validated_date  TEXT,
    validated_by    TEXT,
    session_b_note  TEXT,
    delete_flagged  INTEGER  NOT NULL DEFAULT 0,
    UNIQUE (finding_id, question_id)
);

-- ── wa_finding_entity_links ──
CREATE TABLE wa_finding_entity_links (
    id              INTEGER PRIMARY KEY,
    finding_id      INTEGER NOT NULL,
    entity_type     TEXT NOT NULL,
    entity_id       INTEGER,
    entity_strongs  TEXT,
    raised_date     TEXT NOT NULL, delete_flagged INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (finding_id) REFERENCES wa_session_b_findings(id)
);

-- ── wa_lsj_parsed ──
CREATE TABLE wa_lsj_parsed (
            id                    INTEGER PRIMARY KEY AUTOINCREMENT,
            term_inv_id           INTEGER NOT NULL UNIQUE REFERENCES wa_term_inventory(id),
            raw_lsj               TEXT,
            lsj_gloss             TEXT,
            lsj_domains           TEXT,
            lsj_philosophical_note TEXT,
            lsj_etymology_note    TEXT,
            lsj_cognate_forms     TEXT,
            parsed_at             TEXT    NOT NULL,
            parse_version         TEXT    NOT NULL
        );

-- ── wa_meaning_parsed ──
CREATE TABLE wa_meaning_parsed (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            term_inv_id         INTEGER NOT NULL UNIQUE REFERENCES wa_term_inventory(id),
            strongs_number      TEXT    NOT NULL,
            language            TEXT    NOT NULL,
            top_sense_count     INTEGER DEFAULT 0,
            stem_count          INTEGER DEFAULT 0,
            has_causative_stem  INTEGER DEFAULT 0,
            has_domain_tags     INTEGER DEFAULT 0,
            parsed_at           TEXT    NOT NULL,
            parse_version       TEXT    NOT NULL,
            parse_warnings      TEXT
        );

-- ── wa_meaning_sense ──
CREATE TABLE wa_meaning_sense (
            id                 INTEGER PRIMARY KEY AUTOINCREMENT,
            parsed_meaning_id  INTEGER NOT NULL REFERENCES wa_meaning_parsed(id),
            level_code         TEXT    NOT NULL,
            level_depth        INTEGER NOT NULL,
            parent_level_code  TEXT,
            sense_text         TEXT,
            is_stem_label      INTEGER DEFAULT 0,
            stem_label         TEXT,
            domain_tag         TEXT,
            sort_order         INTEGER NOT NULL
        );

-- ── wa_meaning_stem ──
CREATE TABLE wa_meaning_stem (
            id                INTEGER PRIMARY KEY AUTOINCREMENT,
            parsed_meaning_id INTEGER NOT NULL REFERENCES wa_meaning_parsed(id),
            stem_name         TEXT    NOT NULL,
            stem_type         TEXT,
            sense_count       INTEGER DEFAULT 0,
            top_sense_text    TEXT
        );

-- ── wa_obs_question_catalogue ──
CREATE TABLE wa_obs_question_catalogue (
    obs_id            INTEGER  PRIMARY KEY AUTOINCREMENT,
    question_code     TEXT     NOT NULL UNIQUE,
    section           TEXT     NOT NULL,
    source_word       TEXT,
    source_registry_no INTEGER  REFERENCES word_registry(id),
    question_text     TEXT     NOT NULL,
    pattern_type      TEXT,
    scope             TEXT     NOT NULL DEFAULT 'universal',
    status            TEXT     NOT NULL DEFAULT 'active',
    deleted           INTEGER  NOT NULL DEFAULT 0,
    date_added        TEXT     NOT NULL,
    catalogue_version TEXT     NOT NULL
);

-- ── wa_quality_flag_types ──
CREATE TABLE wa_quality_flag_types (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            flag_group  TEXT NOT NULL,
            flag_code   TEXT NOT NULL UNIQUE,
            description TEXT
        , deprecated INTEGER DEFAULT 0, deprecation_note TEXT, category TEXT);

-- ── wa_session_b_dimensions ──
CREATE TABLE wa_session_b_dimensions (
  id INTEGER PRIMARY KEY,
  registry_id INTEGER NOT NULL,
  file_id INTEGER,
  relational_environment INTEGER DEFAULT 0,
  relational_environment_note TEXT,
  spirit_soul_body INTEGER DEFAULT 0,
  spirit_soul_body_note TEXT,
  inner_operations INTEGER DEFAULT 0,
  inner_operations_note TEXT,
  being INTEGER DEFAULT 0,
  being_note TEXT,
  raised_date TEXT NOT NULL,
  session_b_instruction TEXT NOT NULL
);

-- ── wa_session_b_findings ──
CREATE TABLE wa_session_b_findings (
  id INTEGER PRIMARY KEY,
  finding_id TEXT NOT NULL UNIQUE,
  registry_id INTEGER NOT NULL,
  file_id INTEGER,
  finding_type TEXT NOT NULL,
  finding TEXT NOT NULL,
  anchor_verses TEXT,
  raised_date TEXT NOT NULL,
  session_b_instruction TEXT NOT NULL
, pass_ref TEXT, study_segment TEXT, delete_flag INTEGER DEFAULT 0, obsolete_reason TEXT, obsolete_date TEXT, superseded_by_id INTEGER, related_finding_id INTEGER, resolution_note TEXT, thin_evidence INTEGER DEFAULT 0, status TEXT DEFAULT 'pending', term_id INTEGER REFERENCES mti_terms(id) ON DELETE SET NULL);

-- ── wa_session_research_flags ──
CREATE TABLE wa_session_research_flags (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            registry_id         INTEGER NOT NULL,
            file_id             INTEGER,
            flag_code           TEXT    NOT NULL,
            flag_label          TEXT    NOT NULL UNIQUE,
            strongs_reference   TEXT,
            cross_registry_id   INTEGER,
            priority            TEXT    DEFAULT 'MEDIUM',
            session_target      TEXT    DEFAULT 'D',
            description         TEXT    NOT NULL,
            session_raised      TEXT    NOT NULL,
            raised_date         TEXT    NOT NULL,
            resolved            INTEGER NOT NULL DEFAULT 0,
            resolved_date       TEXT,
            resolved_note       TEXT,
            FOREIGN KEY (registry_id) REFERENCES word_registry(id),
            FOREIGN KEY (file_id) REFERENCES wa_file_index(id),
            FOREIGN KEY (cross_registry_id) REFERENCES word_registry(id)
        );

-- ── wa_term_inventory ──
CREATE TABLE "wa_term_inventory" (
    id                          INTEGER PRIMARY KEY,
    file_id                     INTEGER NOT NULL REFERENCES wa_file_index(id) ON DELETE RESTRICT,
    language                    TEXT NOT NULL,
    term_id                     TEXT NOT NULL,
    strongs_number              TEXT,
    transliteration             TEXT NOT NULL,
    step_search_gloss           TEXT,
    word_analysis_gloss         TEXT,
    occurrence_count            INTEGER,
    occurrence_count_qualifier  TEXT,
    meaning                     TEXT,
    meaning_numbered            TEXT,
    also_spelled                TEXT,
    lsj_entry                   TEXT,
    testament                   TEXT,
    causative_form_present      INTEGER DEFAULT 0,
    last_changed                TEXT DEFAULT (datetime('now')),
    short_def_mounce            TEXT,
    parsed_meaning_id           INTEGER
, delete_flagged INTEGER DEFAULT 0, evidential_status TEXT DEFAULT NULL, retention_note TEXT DEFAULT NULL, term_owner_type TEXT DEFAULT NULL);

-- ── wa_term_phase2_flags ──
CREATE TABLE wa_term_phase2_flags (
            term_inv_id INTEGER NOT NULL REFERENCES wa_term_inventory(id),
            flag_id     INTEGER NOT NULL REFERENCES phase2_flag_types(id), description TEXT, source TEXT, raised_date TEXT, delete_flagged INTEGER DEFAULT 0, obsolete_reason TEXT,
            PRIMARY KEY (term_inv_id, flag_id)
        );

-- ── wa_term_related_words ──
CREATE TABLE "wa_term_related_words" (
    id                  INTEGER PRIMARY KEY,
    term_inv_id         INTEGER NOT NULL REFERENCES wa_term_inventory(id) ON DELETE CASCADE,
    gloss               TEXT,
    transliteration     TEXT,
    strongs_number      TEXT,
    relationship_note   TEXT
, delete_flagged INTEGER DEFAULT 0);

-- ── wa_term_root_family ──
CREATE TABLE "wa_term_root_family" (
    id              INTEGER PRIMARY KEY,
    term_inv_id     INTEGER NOT NULL REFERENCES wa_term_inventory(id) ON DELETE CASCADE,
    root_code       TEXT NOT NULL,
    root_language   TEXT,
    root_gloss      TEXT,
    note            TEXT
, delete_flagged INTEGER DEFAULT 0);

-- ── wa_verse_records ──
CREATE TABLE "wa_verse_records" (
    id                  INTEGER PRIMARY KEY,
    file_id             INTEGER NOT NULL REFERENCES wa_file_index(id) ON DELETE RESTRICT,
    term_inv_id         INTEGER REFERENCES wa_term_inventory(id) ON DELETE RESTRICT,
    term_id             TEXT,
    transliteration     TEXT,
    testament           TEXT,
    reference           TEXT,
    verse_text          TEXT,
    last_changed        TEXT DEFAULT (datetime('now')),
    book_id             INTEGER REFERENCES books(id),
    chapter             INTEGER,
    verse_num           INTEGER,
    translation         TEXT NOT NULL DEFAULT 'ESV',
    note                TEXT,
    claude_output       TEXT,
    created_at          TEXT,
    updated_at          TEXT,
    target_word         TEXT,
    span_strong_match   INTEGER,
    context_before      TEXT,
    context_after       TEXT
, delete_flagged INTEGER DEFAULT 0, mti_term_id INTEGER DEFAULT NULL);

-- ── wa_verse_term_links ──
CREATE TABLE wa_verse_term_links (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    verse_id            INTEGER NOT NULL REFERENCES wa_verse_records(id) ON DELETE CASCADE,
    term_inv_id         INTEGER NOT NULL REFERENCES wa_term_inventory(id) ON DELETE CASCADE,
    step_subgloss_code  TEXT,
    step_subgloss_label TEXT,
    span_strong_match   INTEGER,
    target_word         TEXT,
    created_at          TEXT DEFAULT (strftime('%Y-%m-%dT%H:%M:%S','now')),
    UNIQUE (verse_id, term_inv_id)
);

-- ── word_registry ──
CREATE TABLE word_registry (
    id              INTEGER PRIMARY KEY,
    no              INTEGER,
    word            TEXT NOT NULL,
    source_list     TEXT,
    category_hint   TEXT,
    phase1_input_file  TEXT,
    phase1_status      TEXT,
    phase1_output_file TEXT,
    phase2_datasets    REAL,
    notes           TEXT
, automation_eligible INTEGER DEFAULT 1, last_automation_run TEXT, automation_run_id TEXT, phase1_term_count INTEGER, phase1_verse_count INTEGER, strongs_list TEXT, description TEXT, origin TEXT, dimensions TEXT, inference_note TEXT, session_b_status TEXT, cluster_assignment TEXT DEFAULT "unassigned", sb_classification TEXT DEFAULT NULL, sb_classification_reasoning TEXT DEFAULT NULL, carry_forward INTEGER DEFAULT 1, unique_term_count INTEGER DEFAULT 0, shared_term_count INTEGER DEFAULT 0, term_sharing_ratio REAL DEFAULT 0.0, verse_context_status TEXT DEFAULT NULL, dim_review_status TEXT DEFAULT NULL, dim_review_version TEXT DEFAULT NULL, word_synopsis TEXT);

-- ── word_run_state ──
CREATE TABLE word_run_state (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            run_id              TEXT    NOT NULL REFERENCES engine_run_log(run_id),
            registry_id         TEXT    NOT NULL,
            word                TEXT    NOT NULL,
            phase_reached       TEXT,
            audit_result        TEXT,
            audit_detail        TEXT,
            stop_reason         TEXT,
            researcher_approved INTEGER DEFAULT 0,
            approved_by         TEXT,
            approved_at         TEXT
        );

-- ═══════════════ Indexes ═══════════════

CREATE UNIQUE INDEX uq_books_short_code ON books (short_code);
CREATE INDEX idx_cross_refs_registry ON mti_term_cross_refs(registry, word);
CREATE INDEX idx_cross_refs_term_id  ON mti_term_cross_refs(mti_term_id);
CREATE INDEX idx_mti_del ON mti_terms (delete_flagged);
CREATE INDEX idx_mti_status_del ON mti_terms (status, delete_flagged);
CREATE INDEX idx_mti_strongs_status ON mti_terms (strongs_number, status);
CREATE INDEX idx_mti_terms_reg_fk   ON mti_terms(owning_registry_fk);
CREATE INDEX idx_mti_terms_registry ON mti_terms(owning_registry);
CREATE INDEX idx_mti_terms_status   ON mti_terms(status);
CREATE INDEX idx_mti_terms_strongs  ON mti_terms(strongs_number);
CREATE INDEX idx_mti_terms_word     ON mti_terms(owning_word);
CREATE INDEX idx_ps_registry_type_current
            ON prose_section(registry_id, section_type_id)
            WHERE delete_flagged = 0 AND superseded_by_id IS NULL;
CREATE INDEX idx_ps_status
            ON prose_section(status)
            WHERE delete_flagged = 0 AND superseded_by_id IS NULL;
CREATE INDEX idx_ps_supersedes
            ON prose_section(supersedes_id)
            WHERE supersedes_id IS NOT NULL;
CREATE INDEX idx_pst_stage_lifecycle
            ON prose_section_type(source_stage, lifecycle_tag)
            WHERE delete_flagged = 0;
CREATE INDEX idx_vc_grp ON verse_context (group_id);
CREATE INDEX idx_vc_grp_anchor ON verse_context (group_id, is_anchor, delete_flagged);
CREATE INDEX idx_vc_grp_anchor_live
        ON verse_context(group_id, is_anchor)
        WHERE delete_flagged = 0 AND is_anchor = 1
    ;
CREATE INDEX idx_vc_mti ON verse_context (mti_term_id);
CREATE INDEX idx_vc_mti_del ON verse_context (mti_term_id, delete_flagged);
CREATE INDEX idx_vc_vr ON verse_context (verse_record_id);
CREATE INDEX idx_vcg_mti ON verse_context_group (mti_term_id);
CREATE INDEX idx_wa_xrl_file ON wa_cross_registry_links (file_id);
CREATE INDEX idx_wa_xrl_linked ON wa_cross_registry_links (linked_registry_id);
CREATE INDEX idx_wdqf_file ON wa_data_quality_flags (file_id);
CREATE INDEX idx_wdqf_flag ON wa_data_quality_flags (flag_id);
CREATE INDEX idx_dim_index_dimension ON wa_dimension_index(dimension);
CREATE INDEX idx_dim_index_group ON wa_dimension_index(verse_context_group_id);
CREATE INDEX idx_dim_index_registry ON wa_dimension_index(owning_registry_no);
CREATE INDEX idx_wdi_conf ON wa_dimension_index (dimension_confidence);
CREATE INDEX idx_wdi_del ON wa_dimension_index (delete_flagged);
CREATE INDEX idx_wa_fi_reg   ON wa_file_index(registry_id);
CREATE INDEX idx_wa_fi_word  ON wa_file_index(word);
CREATE INDEX idx_wa_fi_wrfk ON wa_file_index(word_registry_fk);
CREATE INDEX idx_wfel_entity ON wa_finding_entity_links(entity_type, entity_id);
CREATE INDEX idx_wfel_finding_id ON wa_finding_entity_links(finding_id);
CREATE INDEX idx_lsj_parsed_term ON wa_lsj_parsed (term_inv_id);
CREATE INDEX idx_meaning_parsed_term_inv ON wa_meaning_parsed (term_inv_id);
CREATE INDEX idx_meaning_sense_level ON wa_meaning_sense (parsed_meaning_id, level_code);
CREATE INDEX idx_meaning_sense_parsed ON wa_meaning_sense (parsed_meaning_id);
CREATE INDEX idx_meaning_stem_parsed ON wa_meaning_stem (parsed_meaning_id);
CREATE INDEX idx_wsrf_registry ON wa_session_research_flags (registry_id);
CREATE INDEX idx_wsrf_resolved ON wa_session_research_flags (resolved);
CREATE INDEX idx_wa_ti_del ON wa_term_inventory (delete_flagged);
CREATE INDEX idx_wa_ti_file    ON wa_term_inventory(file_id);
CREATE INDEX idx_wa_ti_id      ON wa_term_inventory(term_id);
CREATE INDEX idx_wa_ti_lang    ON wa_term_inventory(language);
CREATE INDEX idx_wa_ti_owner ON wa_term_inventory (term_owner_type, delete_flagged);
CREATE INDEX idx_wa_ti_strongs ON wa_term_inventory(strongs_number);
CREATE INDEX idx_wa_ti_strongs_live
        ON wa_term_inventory(strongs_number)
        WHERE delete_flagged = 0
    ;
CREATE INDEX idx_wa_ti_strongs_owner ON wa_term_inventory (strongs_number, term_owner_type, delete_flagged);
CREATE INDEX idx_wa_rw ON wa_term_related_words(term_inv_id);
CREATE INDEX idx_wa_rf ON wa_term_root_family(term_inv_id);
CREATE INDEX idx_wa_vr_term         ON wa_verse_records (term_inv_id);
CREATE INDEX idx_wa_vr_term_live
        ON wa_verse_records(term_inv_id)
        WHERE delete_flagged = 0
    ;
CREATE INDEX idx_wavr_book_ch_v     ON wa_verse_records (book_id, chapter, verse_num);
CREATE INDEX idx_wavr_del ON wa_verse_records (delete_flagged);
CREATE INDEX idx_wavr_file_term_pos ON wa_verse_records (file_id, term_id, book_id, chapter, verse_num);
CREATE INDEX idx_wavr_reference     ON wa_verse_records (reference);
CREATE INDEX idx_wavr_term_del ON wa_verse_records (term_inv_id, delete_flagged);
CREATE INDEX idx_wavr_term_id       ON wa_verse_records (term_id);
CREATE INDEX idx_vtl_term  ON wa_verse_term_links (term_inv_id);
CREATE INDEX idx_vtl_verse ON wa_verse_term_links (verse_id);
CREATE INDEX idx_wr_cluster ON word_registry (cluster_assignment);
CREATE INDEX idx_wr_no ON word_registry (no);
CREATE INDEX idx_wr_sb_status ON word_registry (session_b_status);
CREATE INDEX idx_wr_vc_status ON word_registry (verse_context_status);

-- ═══════════════ Triggers ═══════════════

CREATE TRIGGER prose_section_ad AFTER DELETE ON prose_section
        BEGIN
            DELETE FROM prose_section_fts WHERE rowid = old.id;
        END;

CREATE TRIGGER prose_section_ai AFTER INSERT ON prose_section
        BEGIN
            INSERT INTO prose_section_fts(rowid, body, heading, section_type_code, registry_id, status)
            SELECT new.id, new.body, new.heading, pst.code, new.registry_id, new.status
            FROM prose_section_type pst WHERE pst.id = new.section_type_id;
        END;

CREATE TRIGGER prose_section_au AFTER UPDATE ON prose_section
        BEGIN
            DELETE FROM prose_section_fts WHERE rowid = old.id;
            INSERT INTO prose_section_fts(rowid, body, heading, section_type_code, registry_id, status)
            SELECT new.id, new.body, new.heading, pst.code, new.registry_id, new.status
            FROM prose_section_type pst WHERE pst.id = new.section_type_id;
        END;

CREATE TRIGGER wa_verse_records_updated_at
AFTER UPDATE ON wa_verse_records
BEGIN
    UPDATE wa_verse_records
    SET updated_at = strftime('%Y-%m-%dT%H:%M:%S','now')
    WHERE id = NEW.id;
END;
