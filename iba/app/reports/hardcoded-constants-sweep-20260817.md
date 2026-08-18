# Hardcoded module-level constants -- content sweep for escalation #648

> Scanned 232 active, non-exempt registered scripts via `ast.parse` for module-level ALL_CAPS assignments -- the same signal the project already recognises as "should be cfg_setting" (`engine/constants.py`'s own `config_exempt_reason`). Split into two tiers by whether the value is a plain literal (`ast.literal_eval`-able -- a real number/string/lookup, genuinely portable to a DB row) or a computed expression (path derivation via `__file__`, a `re.compile(...)`, a dispatch dict of function references -- structurally can't be a `cfg_setting` value, excluded from the candidate count even though the name matches the ALL_CAPS pattern).

**Tier 1 (real candidates): 105 files, 263 constants.**  Tier 2 (structural, not real candidates): 177 files, 423 constants -- listed for transparency, not for action.

This is a candidate list for researcher triage, not a migration -- nothing changed.

## Tier 1 -- real candidates

### `iba/app/lib/narrativegenerate.py`

| constant | value | line |
|---|---|---|
| API_URL | `'https://api.anthropic.com/v1/messages'` | 39 |
| API_VERSION | `'2023-06-01'` | 40 |
| CHARS_PER_TOKEN | `4` | 41 |

### `iba/app/lib/wordregistryspanreport.py`

| constant | value | line |
|---|---|---|
| STEP | `'report.word_registry_span'` | 53 |

### `iba/prototype/export_md.py`

| constant | value | line |
|---|---|---|
| B | `'http://localhost:8989'` | 22 |

### `iba/prototype/inspect_verse.py`

| constant | value | line |
|---|---|---|
| STATE | `{'a': 'absolute', 'c': 'construct', 'd': 'determined'}` | 28 |
| GENDER | `{'m': 'masculine', 'f': 'feminine', 'c': 'common', 'b': 'both'}` | 29 |
| NUMBER | `{'s': 'singular', 'p': 'plural', 'd': 'dual'}` | 30 |
| POS | `{'N': 'noun', 'V': 'verb', 'R': 'preposition', 'C': 'conjunction', 'T': 'particle', 'A': 'adjective'...` | 31 |
| STEM | `{'q': 'Qal', 'n': 'Niphal', 'p': 'Piel', 'P': 'Pual', 'h': 'Hiphil', 'H': 'Hophal', 't': 'Hithpael',...` | 33 |

### `iba/scripts/build_dbschema.py`

| constant | value | line |
|---|---|---|
| CATEGORICAL_CUTOFF | `200` | 43 |
| EXACT_BELOW_ROWS | `50000` | 44 |
| TOP_N | `8` | 45 |

### `iba/scripts/cfg_helper.py`

| constant | value | line |
|---|---|---|
| MARKER_DEFAULTS | `'_envelope_defaults'` | 32 |
| MARKER_COMMENT | `'_comment'` | 33 |
| NOT_RULES | `{'meta', 'sections', 'layout', 'file_hashes', 'last_change', 'not_a_seed_file', 'implemented_by', 'c...` | 36 |

### `iba/scripts/cfg_kernel.py`

| constant | value | line |
|---|---|---|
| ENVELOPE | `{'id': (True, None), 'governs': (True, 'vocab.governs'), 'kind': (True, 'vocab.kind'), 'status': (Tr...` | 40 |
| VALIDATION_FIELDS | `{'axis': (True, 'vocab.axis'), 'severity': (True, 'vocab.severity'), 'enforcement': (True, 'vocab.en...` | 53 |
| FACETS | `['process', 'entities', 'output', 'validation', 'naming', 'filing']` | 60 |
| MARKER_DEFAULTS | `'_envelope_defaults'` | 67 |
| MARKER_COMMENT | `'_comment'` | 68 |

### `iba/scripts/probe_step_api.py`

| constant | value | line |
|---|---|---|
| READ_BY_CLIENT | `{'module.getInfo': {'vocabInfos[].strongNumber', 'vocabInfos[].stepGloss', 'vocabInfos[].count', 'vo...` | 35 |

### `research/VE-lexical/faculty-map-build/_build_batch4.py`

| constant | value | line |
|---|---|---|
| D | `{'H2603A': (['affect', 'volition'], 'be gracious / show mercy / plead: gracious favour disposition (...` | 8 |

### `research/VE-lexical/faculty-map-build/_classify_batch1.py`

| constant | value | line |
|---|---|---|
| D | `{'G0014': ([], 'to do good = moral act/conduct, not an inner capacity', 'high', ''), 'G0015': ([], '...` | 6 |

### `scripts/_apply_cause_from_api.py`

| constant | value | line |
|---|---|---|
| STAMP | `'2026-06-16T00:00:00Z'` | 14 |

### `scripts/_apply_create_constitution_cluster.py`

| constant | value | line |
|---|---|---|
| CODE | `'M47'` | 11 |
| NAME | `'Constitution'` | 12 |
| DESC | `'Constitution: the inner-being seats and faculties (heart, soul, spirit, mind, flesh, conscience)'` | 13 |
| SEATS | `['H3820A', 'H3824', 'G2588', 'H5315G', 'H7308', 'G3563', 'G4561', 'G4893']` | 15 |

### `scripts/_apply_d6_capture_contributor_source.py`

| constant | value | line |
|---|---|---|
| TYPES | `{'src_logos': 'Contributor source — Logos extract (capture once → route many)', 'src_aichat': 'Contr...` | 18 |

### `scripts/_apply_drop_code_softdelete.py`

| constant | value | line |
|---|---|---|
| DROP_OBS | `[241, 257, 258, 259, 282, 283, 284, 366, 367, 368, 387, 388, 389, 390, 391, 392]` | 19 |
| REASON | `'DROP per catalogue restructure v2 §3 (2026-06-11): fabricated/templated DROP-family finding, not va...` | 20 |

### `scripts/_apply_excluded_registry_cascade.py`

| constant | value | line |
|---|---|---|
| TABLES | `['wa_verse_records', 'wa_term_inventory', 'mti_terms', 'verse_context', 'finding']` | 16 |

### `scripts/_apply_faculty_rederive_v1.py`

| constant | value | line |
|---|---|---|
| STAMP | `'faculty-rule-v1-20260615'` | 15 |
| FACULTIES | `{'perception': ('T3.1', ['see', 'saw', 'seen', 'sees', 'seeing', 'look', 'looked', 'behold', 'beheld...` | 18 |

### `scripts/_apply_field_from_api.py`

| constant | value | line |
|---|---|---|
| STAMP | `'2026-06-16T00:00:00Z'` | 10 |
| CFG | `{'location': ('update', 5, 'T2', "ve_label='location' AND value='UNRESOLVED'"), 'divine-involvement'...` | 12 |

### `scripts/_apply_flag_empty_to_t2.py`

| constant | value | line |
|---|---|---|
| CHAR | `{'H3513H': 'M22', 'H3513I': 'M22', 'H3513J': 'M22', 'H2470B': 'M21', 'H0014': 'M30', 'G4090': 'M03',...` | 13 |

### `scripts/_apply_flag_triage_moves.py`

| constant | value | line |
|---|---|---|
| T2_KW | `['\\bnot\\b', 'do not', '\\blest\\b', '\\bif\\b', '\\bsurely\\b', '\\bindeed\\b', '\\balso\\b', '\\b...` | 17 |
| CLUSTER_KW | `[('M02', ['\\banger\\b', '\\bwrath\\b', '\\brage\\b', '\\bfury\\b', 'indignation', 'provoke to anger...` | 27 |

### `scripts/_apply_generate_ve_lexical_v2.py`

| constant | value | line |
|---|---|---|
| PROV | `'v2_engine_iter1'` | 20 |
| STAMP | `'2026-06-26T00:00:00Z'` | 21 |
| VE_MAP | `{'sense': (1, 'T7.1.3'), 'type': (2, 'T1.2.1'), 'compound': (3, 'T6.1.1'), 'location': (5, 'T2'), 'o...` | 26 |

### `scripts/_apply_ingest_verse_morphology.py`

| constant | value | line |
|---|---|---|
| NOW | `'2026-06-16T00:00:00Z'` | 23 |

### `scripts/_apply_l2_write.py`

| constant | value | line |
|---|---|---|
| LOCUS | `[('heart', 267), ('mind', 270), ('bowel', 276), ('kidney', 276), ('inward', 276), ('breast', 276)]` | 23 |
| CLUSTER_FACULTY | `{'M01': (300, 'affect (fear engages the affective faculty)')}` | 27 |

### `scripts/_apply_l2_write_refit.py`

| constant | value | line |
|---|---|---|
| FACULTY | `{294: ['know', 'knew', 'understand', 'discern', 'wisdom', 'wise', 'insight', 'prudent', 'comprehend'...` | 22 |
| LOCATION | `{260: ['spirit'], 264: ['soul'], 267: ['heart'], 270: ['mind'], 276: ['bowel', 'kidney', 'liver', 'b...` | 35 |

### `scripts/_apply_migrate_sb_findings.py`

| constant | value | line |
|---|---|---|
| CLOSED_SB | `{'resolved_qa', 'resolved_sd', 'confirmed', 'superseded', 'folded', 'set_aside', 'set_aside_non_evid...` | 16 |

### `scripts/_apply_migrate_ve_findings_to_lexical.py`

| constant | value | line |
|---|---|---|
| STAMP | `'M59-migration-20260615'` | 21 |
| VE_NR | `{'Lexical and Semantic Analysis': 1, 'Kind': 2, 'Co-occurrence': 3, 'Modes of Operation': 4, 'Heart'...` | 25 |

### `scripts/_apply_morph_backfill.py`

| constant | value | line |
|---|---|---|
| HEB_STEM | `{'q': 'Qal', 'N': 'Niphal', 'p': 'Piel', 'P': 'Pual', 'h': 'Hiphil', 'H': 'Hophal', 't': 'Hithpael',...` | 23 |
| ARAMAIC_STEM | `{'q': 'Peal', 'Q': 'Peil', 'u': 'Hithpeel', 'p': 'Pael', 'P': 'Pual', 'M': 'Hithpaal', 'a': 'Aphel',...` | 27 |

### `scripts/_apply_persist_narration_finding_v1.py`

| constant | value | line |
|---|---|---|
| STAMP | `'ve-narration-v1-20260615'` | 17 |
| CREATED | `'2026-06-15T00:00:00Z'` | 18 |

### `scripts/_apply_phase2_flags_patch.py`

| constant | value | line |
|---|---|---|
| NEW_FLAGS | `[('ARAMAIC_FORM', 'TERM_ANALYSIS'), ('BODY_INNER_EXPRESSION', 'TERM_ANALYSIS'), ('CAUSATIVE_OF_INNER...` | 25 |

### `scripts/_apply_reset_l2_meaning_flags.py`

| constant | value | line |
|---|---|---|
| FT_OBS | `{248: 'immediate_response', 251: 'produces_effect', 238: 'relational_implication', 227: 'purpose_equ...` | 10 |
| NULL | `{'none', 'silent', 'not-stated', 'n/a', 'na', ''}` | 11 |
| STOP | `{'the', 'and', 'that', 'with', 'from', 'this', 'into', 'upon', 'have', 'been', 'which', 'their', 'pe...` | 12 |

### `scripts/_apply_term_decisions.py`

| constant | value | line |
|---|---|---|
| SOUL_ANCHOR_PARENTS | `{'H5315G', 'G5590G'}` | 57 |
| PARTICLE_CEILING | `1000` | 61 |

### `scripts/_apply_ve_rebuild_mechanical_v1.py`

| constant | value | line |
|---|---|---|
| STAMP | `'ve-rebuild-mechanical-v1-20260615'` | 21 |
| PROV | `'mechanical_v1'` | 22 |
| LOC_SEAT | `['heart', 'soul', 'mind', 'spirit', 'conscience', 'flesh']` | 25 |
| LOC_BODY | `['eyes', 'ears', 'neck', 'shoulder', 'hand', 'lips', 'members', 'back']` | 26 |
| LOC_TIER | `{'spirit': 'T2.1.1', 'soul': 'T2.2.1', 'heart': 'T2.3.1', 'mind': 'T2.4.1', 'conscience': 'T2.5.1', ...` | 27 |
| ORIG_WITHIN | `['within', 'internal', 'own', 'self']` | 29 |
| ORIG_BESTOWED | `['give', 'pour', 'fill', 'grant', 'show']` | 30 |
| ORIG_RECEIVED | `['from']` | 31 |
| FACULTY | `{'perception': ['see', 'hear', 'behold', 'eyes', 'ears'], 'cognition': ['know', 'understand', 'consi...` | 32 |
| FACULTY_TIER | `{'perception': 'T3.1', 'cognition': 'T3.2', 'memory': 'T3.3', 'volition': 'T3.6', 'affect': 'T3.4', ...` | 41 |
| DIVINE_WORDS | `['lord', 'god', 'almighty', 'yhwh']` | 43 |
| DIVINE_PHRASE | `['holy one', 'holy spirit']` | 44 |
| DIVINE_POSSESS | `['of god', "god's", 'of the lord', "lord's", 'of the almighty']` | 45 |
| REL_DIR | `['to', 'toward', 'from', 'for', 'against', 'before', 'into', 'upon']` | 46 |
| REL_VERB | `['give', 'show', 'serve', 'seek', 'deliver', 'call', 'choose', 'forsake', 'covenant']` | 47 |

### `scripts/_apply_verse_read_meaning.py`

| constant | value | line |
|---|---|---|
| MODEL | `'claude-sonnet-4-6'` | 24 |
| MAX_TOKENS | `12000` | 25 |
| BATCH | `6` | 26 |
| PROV_TIER | `'l2_api'` | 27 |
| PROV_MEAN | `'l2_meaning'` | 28 |
| FIELD_OBS | `{'sense_applied': 395, 'type': 239, 'compound': 240, 'mode': 245, 'origin': 285, 'attributed_to_God'...` | 31 |
| FACULTY_OBS | `{'perception': 291, 'cognition': 294, 'memory': 297, 'affect': 300, 'creativity': 303, 'volition': 3...` | 38 |
| LOCATION_OBS | `{'spirit': 260, 'soul': 264, 'heart': 267, 'mind': 270, 'body': 276}` | 41 |
| NULLISH | `{'none', 'silent', 'not-stated', 'n/a', 'na', ''}` | 42 |
| FIELDS_ORDER | `['sense_applied', 'type', 'compound', 'mode', 'constitutional_location', 'origin', 'faculty', 'attri...` | 44 |
| SYSTEM_PROMPT | `'You are doing VERSE-LEVEL MEANING extraction for an academic study of Scripture\'s vocabulary for t...` | 119 |
| AUDIT_CONTENT | `{'immediate_response', 'produces_effect', 'relational_implication', 'purpose_equips'}` | 290 |

### `scripts/_assess_l2_findings_view.py`

| constant | value | line |
|---|---|---|
| QLABEL | `{'T7.1.3': 'T7.1 lexical', 'T1.2.1': 'T1.2 kind', 'T1.4.1': 'T1.4 mode', 'T2.6.1': 'T2 body', 'T2.3....` | 12 |

### `scripts/_assess_l2_triage.py`

| constant | value | line |
|---|---|---|
| HEB_STEM | `{'q': 'Qal', 'N': 'Niphal', 'p': 'Piel', 'P': 'Pual', 'h': 'Hiphil', 'H': 'Hophal', 't': 'Hithpael'}` | 17 |

### `scripts/_assess_relationship_probe.py`

| constant | value | line |
|---|---|---|
| POS | `{'V': 'ACTION(verb)', 'N': 'STATUS(noun)', 'A': 'QUALITY(adj)', 'D': 'adverb', 'R': 'prep', 'C': 'co...` | 12 |

### `scripts/_assess_study_state.py`

| constant | value | line |
|---|---|---|
| POETIC_TAG | `'poetic-lexical'` | 22 |

### `scripts/_assess_t2_cleanup.py`

| constant | value | line |
|---|---|---|
| SUF | `('ingly', 'ing', 'edly', 'ed', 'ied', 'ies', 'ness', 'ment', 'ful', 'less', 'ity', 'ly', 'es', 's')` | 18 |
| INNER_OW | `{'anger', 'fear', 'sorrow', 'anguish', 'distress', 'grief', 'guilt', 'shame', 'love', 'peace', 'pati...` | 59 |

### `scripts/_assess_t2_relevance_surface.py`

| constant | value | line |
|---|---|---|
| SUFFIXES | `('ingly', 'ing', 'edly', 'ed', 'ied', 'ies', 'ness', 'ment', 'ful', 'less', 'ity', 'ly', 'es', 's')` | 19 |

### `scripts/_assess_verse_corroboration.py`

| constant | value | line |
|---|---|---|
| SUFFIXES | `('ingly', 'ing', 'edly', 'ed', 'ied', 'ies', 'ness', 'ment', 'ful', 'less', 'ity', 'ly', 'es', 's')` | 28 |

### `scripts/_assess_verse_raw_data.py`

| constant | value | line |
|---|---|---|
| FUNCTION_GLOSSES | `{'not', 'the', 'and', 'a', 'to', 'of', 'in', 'that', 'his', 'their', 'your', 'him', 'they'}` | 21 |

### `scripts/_backfill_span_match.py`

| constant | value | line |
|---|---|---|
| DB | `'G:\\My Drive\\Bible_study_projects\\database\\bible_research.db'` | 24 |

### `scripts/_build_cluster_verse_read_gate.py`

| constant | value | line |
|---|---|---|
| PROF | `[('type', 239), ('origin', 285), ('typology', 234), ('attributed_to_God', 225)]` | 11 |
| FACULTY | `{300: 'affect', 291: 'perception', 294: 'cognition', 312: 'moral-eval', 321: 'relational', 306: 'vol...` | 12 |

### `scripts/_build_ps119.py`

| constant | value | line |
|---|---|---|
| WORD | `{'H8451': 'law (torah)', 'H6490': 'precepts (piqqudim)', 'H2706': 'statutes (chuqqim)', 'H4687': 'co...` | 27 |
| GODACT | `{'H2421': 'give life / revive (chayah)', 'H3384': 'teach (yarah)', 'H1580': 'deal bountifully (gamal...` | 37 |
| STAND | `{'H5769': 'forever (olam)', 'H6118': 'end (eqeb)', 'H1870': 'way (derek)', 'H0734': 'way/path (orach...` | 49 |
| CH | `{}` | 65 |
| KEEP_SHAMAR | `{4: "'You have commanded your precepts to be KEPT diligently' - the charge to keep, the psalm's prem...` | 75 |
| KEEP_NATSAR | `{2: "'Blessed are those who KEEP his testimonies, who seek him with their whole heart' - the guardin...` | 98 |
| LOVE | `{47: "'I find my delight in your commandments, which I LOVE' - love of the commandments as the sprin...` | 118 |
| DELIGHT | `{('H8191', 24): "'Your testimonies are my DELIGHT; they are my counsellors' - the testimonies as del...` | 137 |
| MED | `{('H7878', 15): "'I will MEDITATE on your precepts and fix my eyes on your ways' - meditation joined...` | 155 |
| HOPE | `{('H3176', 43): "'Take not the word of truth utterly out of my mouth, for my HOPE is in your rules' ...` | 170 |
| SOUL | `{20: "'My SOUL is consumed with longing for your rules at all times' - the self wasting with unceasi...` | 206 |
| INSOLENT | `{21: "'You rebuke the INSOLENT, accursed ones, who wander from your commandments' - the proud who st...` | 237 |
| WICKED | `{53: "'Hot indignation seizes me because of the WICKED, who forsake your law' - the psalmist's indig...` | 250 |
| FALSE | `{29: "'Put FALSE ways far from me and graciously teach me your law!' - the false way the psalmist be...` | 276 |
| QOVR | `{('H3925', 12): 'teach (lamad)', ('H3925', 26): 'teach (lamad)', ('H3925', 64): 'teach (lamad)', ('H...` | 291 |
| SOVR | `{('H3925', 99): 'teachers (lamad)', ('H2459', 70): 'fat (cheleb)', ('H7451', 101): 'evil way (ra)', ...` | 312 |

### `scripts/_build_t2_flag_sample.py`

| constant | value | line |
|---|---|---|
| T2 | `['et', 'al', 'a.ni', 'mi', 'yad', 'ra.ah', 'qe.rev', 'o.zen']` | 10 |
| FLAG | `['lev', 'kardia', 'ne.phesh', 'sarx', 'mish.pat', 'be.rit', 'shem', 'me.od']` | 11 |
| L | `['# T2 and FLAG — sample verses + meanings (for judgement)', '', '> READ-ONLY. Real verse text + the...` | 25 |

### `scripts/_build_term_verse_findings_report.py`

| constant | value | line |
|---|---|---|
| FIELD | `[(395, 'sense_applied'), (239, 'type'), (240, 'compound'), (245, 'mode'), (285, 'origin'), (225, 'at...` | 12 |
| FACULTY | `{291: 'perception', 294: 'cognition', 297: 'memory', 300: 'affect', 303: 'creativity', 306: 'volitio...` | 15 |
| LOCATION | `{260: 'spirit', 264: 'soul', 267: 'heart', 270: 'mind', 276: 'body'}` | 17 |

### `scripts/_build_vc_revision_ledger.py`

| constant | value | line |
|---|---|---|
| PATCHES | `[('VCB-7', 'wa-vc-134-patch-vcnew-v1-20260424.json', 'VCNEW'), ('VCB-7', 'wa-vc-134-patch-vcrecovery...` | 29 |

### `scripts/_build_verse_read_pilot_review.py`

| constant | value | line |
|---|---|---|
| IDS | `[266, 269, 703, 1554, 1681]` | 8 |
| NAME | `{266: 'fobos G5401', 269: 'yir.ah H3374', 703: 'cha.tat H2865', 1554: 'ra.gaz H7264', 1681: 'ya.re H...` | 9 |
| OBS2F | `{225: 'attributed_to_God', 227: 'purpose_equips', 234: 'typology_direction', 238: 'relational_implic...` | 10 |
| FACULTY | `{291: 'perception', 294: 'cognition', 297: 'memory', 300: 'affect', 303: 'creativity', 306: 'volitio...` | 13 |
| LOCATION | `{260: 'spirit', 264: 'soul', 267: 'heart', 270: 'mind', 276: 'body'}` | 15 |
| FREETEXT | `{'immediate_response', 'produces_effect', 'relational_implication', 'purpose_equips'}` | 16 |
| NULL | `{'none', 'silent', 'not-stated', 'n/a', 'na', ''}` | 17 |
| STOP | `{'the', 'and', 'that', 'with', 'from', 'this', 'into', 'upon', 'have', 'been', 'which', 'their', 'pe...` | 18 |
| V | `{}` | 29 |
| L | `['# M01 verse-read pilot — review', '', '> READ-ONLY review of the live 5-term pilot (223 verses, 3,...` | 55 |

### `scripts/_check_integrity_controls.py`

| constant | value | line |
|---|---|---|
| TOTALS | `{'mti_active': "SELECT COUNT(*) FROM mti_terms WHERE status NOT IN ('delete','candidate_delete','exc...` | 20 |
| CLUSTER | `'SELECT cluster_code, COUNT(*) FROM mti_terms WHERE cluster_code IS NOT NULL GROUP BY cluster_code'` | 34 |
| INV | `{'dup_owner_strong': "SELECT COUNT(*) FROM (SELECT strongs_number FROM wa_term_inventory WHERE term_...` | 38 |
| COMPLETE | `{'vr_out_of_corpus': 'SELECT COUNT(*) FROM wa_verse_records vr\n     WHERE (vr.delete_flagged=0 OR v...` | 53 |

### `scripts/_check_ve_signal_lists.py`

| constant | value | line |
|---|---|---|
| EXPECTED | `{'DIVINE': {'H3068': 'YHWH', 'H3069': 'YHWH (Elohim-pointing)', 'H0430': 'Elohim', 'H0433': 'Eloah',...` | 16 |

### `scripts/_delete_empty_fi.py`

| constant | value | line |
|---|---|---|
| KEEP | `{73, 145, 169, 176}` | 8 |

### `scripts/_explore_cluster_timing.py`

| constant | value | line |
|---|---|---|
| IDLE_THRESHOLD_S | `1800` | 26 |

### `scripts/_explore_drop_code_findings.py`

| constant | value | line |
|---|---|---|
| FAMILIES | `[('T1.2.3', 'Best working description', [241]), ('T1.8', 'Dimension Classification', [257, 258, 259]...` | 19 |
| OBS2CODE | `{}` | 27 |
| OBS2FAM | `{}` | 28 |

### `scripts/_explore_m_vs_r_divergence.py`

| constant | value | line |
|---|---|---|
| OBS | `395` | 21 |

### `scripts/_explore_tier_findings.py`

| constant | value | line |
|---|---|---|
| SLUG | `{'T7.1.3': 'sense_applied', 'T1.2.1': 'type', 'T1.2.2': 'compound', 'T1.4.1': 'mode', 'T2.9.1': 'ori...` | 28 |
| FACULTY_CODES | `{'T3.1.1', 'T3.2.1', 'T3.3.1', 'T3.4.1', 'T3.5.1', 'T3.6.1', 'T3.7.1', 'T3.8.1', 'T3.9.1', 'T3.11.1'...` | 34 |
| LOCATION_CODES | `{'T2.1.1', 'T2.2.1', 'T2.3.1', 'T2.4.1', 'T2.6.1'}` | 36 |
| COLS | `['sense_applied', 'type', 'compound', 'mode', 'origin', 'attributed_to_God', 'purpose_equips', 'typo...` | 38 |

### `scripts/_explore_ve_by_cluster.py`

| constant | value | line |
|---|---|---|
| VE | `[('type', ['T1.2.1'], 'cat'), ('compound', ['T1.2.2'], 'cat'), ('origin', ['T2.9.1'], 'cat'), ('attr...` | 20 |
| NULLTOKENS | `{'NONE', 'SILENT', 'not-stated', ''}` | 37 |
| NORMALISE | `{'compound', 'literary_setting'}` | 46 |

### `scripts/_generate_cluster_gate.py`

| constant | value | line |
|---|---|---|
| VOCAB | `{'type': {'action', 'status', 'quality'}, 'origin': {'within-person', 'received-from-outside', 'best...` | 23 |
| VAL2FIELD | `{}` | 40 |

### `scripts/_generate_meaning_quality_check.py`

| constant | value | line |
|---|---|---|
| FIELD_LABELS | `['sense_applied', 'type', 'compound', 'mode', 'origin', 'attributed_to_God', 'purpose_equips', 'typo...` | 12 |

### `scripts/_preflight_m20_dir_005_M20_A_mapping.py`

| constant | value | line |
|---|---|---|
| DB | `'database/bible_research.db'` | 11 |
| TERMS | `{'G3308': 350, 'G3309': 2709, 'H1672': 259}` | 16 |
| REFINE_VCGS | `{220: '350-001', 222: '2709-001', 224: '2709-003', 888: '259-002'}` | 19 |
| SPLIT_VCGS | `{221: '350-002', 223: '2709-002', 887: '259-001'}` | 20 |
| VERSES | `[('Mat 13:22', 'G3308', 'id=220', 0), ('Mar 4:19', 'G3308', 'id=220', 0), ('Luk 8:14', 'G3308', 'id=...` | 23 |

### `scripts/_pro_read_lib.py`

| constant | value | line |
|---|---|---|
| IB | `'internal:ib-state'` | 19 |
| GOD | `'external:god'` | 19 |
| PER | `'external:person'` | 19 |

### `scripts/_prototype_finding_lifecycle.py`

| constant | value | line |
|---|---|---|
| DIRECTIVES | `[{'id': 'M01-0007', 'clarification': 'REVOKE god-present->reverence (it INDUCES); apply fear-of-God-...` | 14 |

### `scripts/_prototype_l1_mechanical.py`

| constant | value | line |
|---|---|---|
| SUF | `('ingly', 'ing', 'edly', 'ed', 'ied', 'ies', 'ness', 'ment', 'ful', 'less', 'ity', 'ly', 'es', 's')` | 22 |

### `scripts/_prototype_l1_morph.py`

| constant | value | line |
|---|---|---|
| VER | `'ESV_th'` | 18 |
| RANGES | `['Gen.1.1-Deut.34.12', 'Josh.1.1-Esth.10.3', 'Job.1.1-Song.8.14', 'Isa.1.1-Mal.4.6', 'Matt.1.1-Rev.2...` | 19 |
| STEMCHAR | `{'q': 'Qal', 'N': 'Niphal', 'p': 'Piel', 'P': 'Pual', 'h': 'Hiphil', 'H': 'Hophal', 't': 'Hithpael'}` | 20 |

### `scripts/_prototype_meaning_run.py`

| constant | value | line |
|---|---|---|
| HEB_STEM | `{'q': 'Qal', 'N': 'Niphal', 'p': 'Piel', 'P': 'Pual', 'h': 'Hiphil', 'H': 'Hophal', 't': 'Hithpael',...` | 18 |

### `scripts/_prototype_step_morph.py`

| constant | value | line |
|---|---|---|
| HEB_STEM | `{'q': 'Qal', 'N': 'Niphal', 'p': 'Piel', 'P': 'Pual', 'h': 'Hiphil', 'H': 'Hophal', 't': 'Hithpael',...` | 20 |
| POS | `{'V': 'verb', 'N': 'noun', 'A': 'adjective', 'P': 'pronoun', 'R': 'preposition', 'C': 'conjunction',...` | 24 |

### `scripts/_repair_03_wa_file_index.py`

| constant | value | line |
|---|---|---|
| EXPECTED_ROWS | `199` | 11 |

### `scripts/_repair_05_wa_term_related_words.py`

| constant | value | line |
|---|---|---|
| EXPECTED_ROWS | `10102` | 10 |

### `scripts/_repair_06_wa_term_root_family.py`

| constant | value | line |
|---|---|---|
| EXPECTED_ROWS | `641` | 10 |

### `scripts/_repair_07_wa_verse_records.py`

| constant | value | line |
|---|---|---|
| EXPECTED_ROWS | `57130` | 15 |

### `scripts/_reread_ledger_lib.py`

| constant | value | line |
|---|---|---|
| IB | `'internal:ib-state'` | 19 |
| GOD | `'external:god'` | 19 |
| PER | `'external:person'` | 19 |

### `scripts/_reset_registry_status.py`

| constant | value | line |
|---|---|---|
| DB | `'../database/bible_research.db'` | 11 |

### `scripts/_run_cause_api.py`

| constant | value | line |
|---|---|---|
| RATES | `{'claude-sonnet-4-6': (3.0, 15.0), 'claude-haiku-4-5-20251001': (1.0, 5.0), 'claude-opus-4-8': (15.0...` | 17 |

### `scripts/_run_ve_reads_governed.py`

| constant | value | line |
|---|---|---|
| RATES | `{'claude-sonnet-4-6': (3.0, 15.0), 'claude-haiku-4-5-20251001': (1.0, 5.0)}` | 18 |
| STAMP | `'2026-06-18T00:00:00Z'` | 19 |
| SPECS | `{'cause': ('pending-read', 'For EACH term, state what AROUSES / elicits the inner-being state it nam...` | 22 |

### `scripts/_ve_engine_v2.py`

| constant | value | line |
|---|---|---|
| SEAT | `{'H5315': 'soul', 'H5314': 'soul', 'G5590': 'soul', 'H3820': 'heart', 'H3824': 'heart', 'H3826': 'he...` | 34 |
| DIVINE | `{'H3068', 'H3069', 'H430', 'H433', 'H410', 'H136', 'H113', 'H7706', 'H3050', 'H5945', 'G2316', 'G296...` | 57 |
| FACULTY_BY_CLUSTER | `{'M01': 'affect', 'M15': 'cognition', 'M23': 'affect'}` | 59 |
| FACULTY_LEMMA | `{'H7200': 'perception', 'H2372': 'perception', 'G3708': 'perception', 'G1492': 'perception', 'H3045'...` | 62 |
| INTENSIFIER | `{'H7227': 'many', 'H7231': 'many', 'H3966': 'very', 'H3605': 'all', 'H1419': 'great', 'G4183': 'many...` | 69 |
| FROM_PREP | `{'H4480', 'H9006', 'G575', 'G1537'}` | 70 |
| SPEECH | `{'H559', 'H1696', 'H6030', 'H7121', 'G3004', 'G2036', 'G2980', 'G611'}` | 71 |
| INHERENT_VALENCE | `{'H7451': 'sinful', 'H7563': 'sinful', 'H6662': 'righteous', 'H6666': 'righteous'}` | 72 |
| NEGATION | `{'H3808', 'H408', 'G3361', 'G3756'}` | 73 |
| PERCEPTION | `{'G3708', 'G1492', 'G991', 'G2334', 'H7200', 'H2372', 'H8085', 'H5027', 'H238'}` | 74 |
| COGNITION | `{'G1380', 'G1097', 'H3045', 'H995'}` | 75 |
| CAUSAL | `{'H3588', 'G3754', 'G1063', 'G1360'}` | 77 |
| COORD | `{'H9002', 'G2532'}` | 78 |
| SPIRIT_BEINGS | `{'G4151', 'G1140', 'H7307', 'H7700'}` | 79 |
| GRAMMAR | `{'article', 'preposition', 'conjunction', 'particle', 'suffix'}` | 122 |
| FACULTY_GLOSS | `{'affect': ['fear', 'afraid', 'dread', 'terror', 'terrif', 'horror', 'panic', 'anxi', 'distress', 't...` | 124 |
| QUANT_SURF | `{'all', 'every', 'each', 'any', 'many', 'much', 'whole', 'some', 'most', 'few', 'both', 'one', 'two'...` | 218 |
| POSSESSIVE_SURF | `{'my', 'your', 'his', 'her', 'our', 'their', 'its', 'thy', 'mine', 'thine'}` | 220 |

### `scripts/analytics/morph_util.py`

| constant | value | line |
|---|---|---|
| GREEK_INDECL | `{'ADV', 'CONJ', 'COND', 'PRT', 'PREP', 'INJ', 'ARAM', 'HEB', 'N-LI', 'N-OI'}` | 41 |
| GREEK_INDECL_CAT | `{'ADV': 'adverb', 'CONJ': 'conjunction', 'COND': 'conditional', 'PRT': 'particle', 'PREP': 'preposit...` | 42 |
| HEBCAT | `{'V': 'verb', 'N': 'noun', 'A': 'adjective', 'C': 'conjunction', 'R': 'preposition', 'T': 'particle'...` | 45 |
| GRKCAT | `{'N': 'noun', 'V': 'verb', 'A': 'adjective', 'R': 'pronoun', 'C': 'conjunction', 'P': 'preposition',...` | 47 |
| HEB_STEM | `{'q': 'Qal', 'N': 'Niphal', 'p': 'Piel', 'P': 'Pual', 'h': 'Hiphil', 'H': 'Hophal', 't': 'Hithpael',...` | 50 |
| ARAMAIC_STEM | `{'q': 'Peal', 'Q': 'Peil', 'u': 'Hithpeel', 'p': 'Pael', 'P': 'Pual', 'M': 'Hithpaal', 'a': 'Aphel',...` | 53 |

### `scripts/backup_db_to_nas.py`

| constant | value | line |
|---|---|---|
| LOG_NAME | `'backup_log.txt'` | 44 |
| KEEP_RECENT | `24` | 47 |
| KEEP_DAILY | `30` | 48 |
| KEEP_WEEKLY | `26` | 49 |

### `scripts/build_cause_api_package.py`

| constant | value | line |
|---|---|---|
| PROMPT | `'TASK (do ONLY this): determine the CAUSE of an inner-being state, per item.\nFor each item: read `v...` | 14 |

### `scripts/build_complete_extract.py`

| constant | value | line |
|---|---|---|
| SCRIPT_VERSION | `'1.2'` | 23 |

### `scripts/build_corpus_prose.py`

| constant | value | line |
|---|---|---|
| CHAPTER_ORDER | `[('sb_s2c_ch1', 'Chapter 1 — Meaning'), ('sb_s2c_ch2', 'Chapter 2 — How It Works'), ('sb_s2c_ch3', '...` | 47 |
| COMPLETE_STATUSES | `('Analysis Complete', 'Session B Complete')` | 56 |

### `scripts/build_field_api_package.py`

| constant | value | line |
|---|---|---|
| FIELD_SPECS | `{'location': {'where': "x.ve_label='location' AND x.value='UNRESOLVED'", 'prompt': 'TASK (only this)...` | 13 |

### `scripts/build_file_manifest.py`

| constant | value | line |
|---|---|---|
| SKIP_DIRS | `{'.git', '__pycache__', 'venv', '.venv', 'env', 'node_modules', '.claude', '.idea', '.vscode', '.pyt...` | 41 |
| EXCLUDE_EXTS | `{'.pyc', '.pyo', '.pyd', '.tmp', '.swp', '.lock'}` | 47 |
| CURRENCY_RULES | `[('sessions-v2/', 'current'), ('workflow/', 'current'), ('research/', 'current'), ('docs/', 'current...` | 60 |

### `scripts/build_file_patterns_extract.py`

| constant | value | line |
|---|---|---|
| EXTRACTOR_VERSION | `'1.0'` | 28 |

### `scripts/build_label_patterns_extract.py`

| constant | value | line |
|---|---|---|
| EXTRACTOR_VERSION | `'1.0'` | 27 |

### `scripts/build_m01_by_characteristic.py`

| constant | value | line |
|---|---|---|
| OUT | `'Sessions-v2/M01-Fear/Data/wa-m01-by-characteristic-verse-records-20260618.json'` | 8 |
| CHARS | `[('c1', 'Reverent fear / awe (chiefly toward God)', 'God-directed, honouring fear; valence righteous...` | 17 |
| LEX_ORDER | `['sense', 'lemma_meaning', 'type', 'mode', 'faculty', 'location', 'origin', 'how', 'object', 'object...` | 61 |

### `scripts/build_m01_findings_oldnew_extract.py`

| constant | value | line |
|---|---|---|
| NEW_DIR | `'Sessions-v2/M01-Fear/findings'` | 12 |
| OUT_OLD | `'Sessions-v2/M01-Fear/findings/WA-m01-findings-OLD-dbexport-bytier-v1-20260619.md'` | 13 |
| OUT_NEW | `'Sessions-v2/M01-Fear/findings/WA-m01-findings-NEW-merged-bytier-v1-20260619.md'` | 14 |

### `scripts/build_m02_findings_oldnew_extract.py`

| constant | value | line |
|---|---|---|
| NEW_DIR | `'Sessions-v2/M02-Anger/findings'` | 13 |
| NEW_CHARS | `[('c1', 'C1 — Human kindled / burning anger'), ('c2', 'C2 — Divine wrath'), ('c3', 'C3 — Provoking t...` | 19 |

### `scripts/build_patch_types_extract.py`

| constant | value | line |
|---|---|---|
| EXTRACTOR_VERSION | `'1.0'` | 27 |

### `scripts/build_programme_prose_extract.py`

| constant | value | line |
|---|---|---|
| EXTRACTOR_VERSION | `'1.1'` | 36 |
| CHAPTER_NAMES | `{0: 'Preamble', 1: 'Programme purpose', 2: 'Research methodology', 3: 'Research approach', 4: 'Data ...` | 39 |
| BOOK_STAGE_MAP | `{'Programme': {'programme'}, 'Detail design': {'session_a', 'session_b', 'session_b_phase9', 'sessio...` | 49 |

### `scripts/build_reference_snapshot.py`

| constant | value | line |
|---|---|---|
| EXTRACTOR_VERSION | `'1.0'` | 40 |

### `scripts/build_rules_extract.py`

| constant | value | line |
|---|---|---|
| EXTRACTOR_VERSION | `'1.0'` | 34 |

### `scripts/build_script_registry.py`

| constant | value | line |
|---|---|---|
| CLASS_RULES | `[('^_tmp_', ('throwaway (delete/archive at session end)', 'varies')), ('^(_assess_\|_check_\|_discover...` | 22 |

### `scripts/build_session_a_prose.py`

| constant | value | line |
|---|---|---|
| BANKED_REGISTRIES | `[35, 62, 134, 206, 207]` | 39 |

### `scripts/build_ve_lexical_extract.py`

| constant | value | line |
|---|---|---|
| T2_CONTENT_POS | `{'verb', 'noun', 'adjective'}` | 16 |
| FIELDS_GUIDE | `{'sense': 'per-occurrence contextual sense (the ESV word used in THIS verse)', 'lemma_meaning': "the...` | 34 |
| ENGINE_CHANGES | `{'zero_pad_fix': "FOUNDATIONAL: Strong's seed lists were short-form (H430/H408/H853) but the DB meas...` | 57 |
| EXTRACT_VERSION | `'v1_0'` | 97 |
| DERIVATION | `{'_principle': "Every value is DERIVED from a named original-language measure (lemma · morphology · ...` | 100 |

### `scripts/build_vocab_extract.py`

| constant | value | line |
|---|---|---|
| EXTRACTOR_VERSION | `'1.0'` | 31 |

### `scripts/cost_ledger.py`

| constant | value | line |
|---|---|---|
| COL_ALIASES | `{'date': ['usage_date_utc', 'date', 'day', 'usage_date', 'timestamp'], 'model': ['model_version', 'm...` | 47 |

### `scripts/export_tier_catalogue.py`

| constant | value | line |
|---|---|---|
| TIER_TITLES | `{'T0': 'Divine Image and Created Design', 'T1': 'Definition', 'T2': 'Constitutional Location and Bou...` | 11 |

### `scripts/export_ve_status_reports.py`

| constant | value | line |
|---|---|---|
| OUTA | `'outputs/wa-ve-api-updated-overview-20260617.md'` | 9 |
| OUTB | `'outputs/wa-ve-status-by-cluster-by-veitem-20260617.md'` | 10 |
| PENDING | `('UNRESOLVED', 'pending-read', 'thing/abstract')` | 11 |

### `scripts/generate_programme_snapshot.py`

| constant | value | line |
|---|---|---|
| SB_SHORT | `{'Verse Context Reset': 'VC-Reset', 'Ready for Analysis': 'Ready', 'Pre-Analysis Complete': 'PreAn',...` | 35 |

### `scripts/generate_session_a_extract.py`

| constant | value | line |
|---|---|---|
| SOURCE_STAGE | `'session_a'` | 54 |
| AUTHOR | `'claude_code'` | 55 |
| STATUS | `'approved'` | 56 |
| SECTION_ORDER | `[('summary', 'Summary'), ('meaning', 'Meaning'), ('terms', 'Terms'), ('verses', 'Verses'), ('pointer...` | 61 |

### `scripts/populate_dimension_index.py`

| constant | value | line |
|---|---|---|
| DIMENSIONS | `['Emotion — Positive', 'Emotion — Negative', 'Cognition', 'Volition', 'Moral Character', 'Relational...` | 27 |

### `scripts/readiness_sweep_pilot.py`

| constant | value | line |
|---|---|---|
| DB | `'database/bible_research.db'` | 24 |

### `scripts/readiness_sweep_programme_scan.py`

| constant | value | line |
|---|---|---|
| DB | `'database/bible_research.db'` | 39 |

### `scripts/search_prose.py`

| constant | value | line |
|---|---|---|
| DEFAULT_LIMIT | `100` | 22 |

### `scripts/token_cost_history.py`

| constant | value | line |
|---|---|---|
| BUCKETS | `['input', 'output', 'cache_read', 'cache_write_5m', 'cache_write_1h']` | 47 |

### `scripts/v3_2_l1.py`

| constant | value | line |
|---|---|---|
| SUF | `('ingly', 'ing', 'edly', 'ed', 'ied', 'ies', 'ness', 'ment', 'ful', 'less', 'ity', 'ly', 'es', 's')` | 25 |
| PHYS_LIT | `{'wave', 'waves', 'breaker', 'shatter', 'shattered', 'broken', 'break'}` | 31 |
| METAPHOR | `{'burn', 'burning', 'heat', 'scorch', 'scorching', 'melt', 'melted', 'tremble', 'trembling', 'quake'...` | 32 |
| EXT | `{'punish', 'punishment', 'penalty', 'vengeance', 'judgment', 'judgement', 'recompense', 'retribution...` | 34 |

### `scripts/word_study_extract.py`

| constant | value | line |
|---|---|---|
| PARTICLE_CEILING | `1000` | 37 |
| CONTEXT_WINDOW | `5` | 38 |

## Tier 2 -- structural (excluded from the candidate count, shown for transparency)

### `iba/app/lib/dbsnapshot.py`

| constant | value | line |
|---|---|---|
| SNAPSHOT_DIR | `DB_PATH.parent / 'snapshots'` | 39 |

### `iba/app/lib/debaterun.py`

| constant | value | line |
|---|---|---|
| READY_CHECKS | `{'hib.set': hib_ready, 'passage.build': passage_ready, 'phenomenon.set': phenomenon_ready, 'operatio...` | 173 |

### `iba/app/lib/manifest.py`

| constant | value | line |
|---|---|---|
| PROJECT_ROOT | `pathlib.Path(__file__).resolve().parents[3]` | 39 |

### `iba/app/lib/versespanmeaningreport.py`

| constant | value | line |
|---|---|---|
| BASE_RE | `re.compile(_BASE_RE_FALLBACK)` | 33 |

### `iba/app/lib/wholebookread.py`

| constant | value | line |
|---|---|---|
| NEXT_H2_RE | `re.compile('^##\\s+\\S', re.MULTILINE)` | 54 |

### `iba/prototype/build_layers.py`

| constant | value | line |
|---|---|---|
| ROOT | `pathlib.Path(__file__).resolve().parents[2]` | 34 |
| SPAN_RE | `re.compile("<span[^>]*\\bmorph='([^']*)'[^>]*\\bstrong='([^']*)'[^>]*>([^<]*)</span>")` | 45 |

### `iba/prototype/build_prototype.py`

| constant | value | line |
|---|---|---|
| ROOT | `pathlib.Path(__file__).resolve().parents[2]` | 40 |
| SPAN_RE | `re.compile("<span[^>]*\\bmorph='([^']*)'[^>]*\\bstrong='([^']*)'[^>]*>([^<]*)</span>")` | 46 |
| BASE_RE | `re.compile('^([HG]\\d+)([A-Z]?)$')` | 47 |
| PARTICLE_RE | `re.compile('^[HG]9\\d{3}$')` | 48 |

### `iba/prototype/export_md.py`

| constant | value | line |
|---|---|---|
| ROOT | `pathlib.Path(__file__).resolve().parents[2]` | 21 |

### `iba/prototype/inspect_verse.py`

| constant | value | line |
|---|---|---|
| ROOT | `pathlib.Path(__file__).resolve().parents[2]` | 25 |

### `iba/scripts/build_dbschema.py`

| constant | value | line |
|---|---|---|
| ROOT | `pathlib.Path(__file__).resolve().parent.parent.parent` | 38 |
| CONFIG | `ROOT / 'iba' / 'config'` | 39 |
| MAINT | `CONFIG / 'utility' / 'DBSchema_maintenance.json'` | 40 |

### `iba/scripts/cfg_apply.py`

| constant | value | line |
|---|---|---|
| ROOT | `pathlib.Path(__file__).resolve().parent.parent` | 59 |
| CONFIG | `ROOT / 'config'` | 60 |
| KERNEL | `ROOT / 'scripts' / 'cfg_kernel.py'` | 61 |
| CHANGELOG | `CONFIG / '_change_log.jsonl'` | 62 |

### `iba/scripts/cfg_helper.py`

| constant | value | line |
|---|---|---|
| ROOT | `pathlib.Path(__file__).resolve().parent.parent` | 29 |
| CONFIG | `ROOT / 'config'` | 30 |

### `iba/scripts/probe_step_api.py`

| constant | value | line |
|---|---|---|
| ROOT | `pathlib.Path(__file__).resolve().parents[2]` | 31 |

### `scripts/_apply_cause_from_api.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 13 |

### `scripts/_apply_create_constitution_cluster.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 10 |

### `scripts/_apply_create_vc_for_onboarded.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 14 |
| OUTDIR | `os.path.join('outputs', 'integrity')` | 15 |

### `scripts/_apply_d6_capture_contributor_source.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 16 |

### `scripts/_apply_drop_code_softdelete.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 18 |

### `scripts/_apply_excluded_registry_cascade.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 15 |

### `scripts/_apply_faculty_rederive_v1.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 14 |

### `scripts/_apply_field_from_api.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 9 |

### `scripts/_apply_flag_empty_to_t2.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 11 |

### `scripts/_apply_flag_triage_moves.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 13 |

### `scripts/_apply_generate_ve_lexical_v2.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 18 |
| SNAP | `os.path.join('backups', 'bible_research_pre-reset-sweep_20260626.db')` | 19 |

### `scripts/_apply_ingest_verse_morphology.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 21 |
| SPAN | `re.compile("<span\\s+morph='([^']*)'\\s+strong='([^']*)'>([^<]*)</span>", re.I)` | 22 |
| BASE | `os.getenv('STEP_LOCAL_URL', 'http://localhost:8989').rstrip('/')` | 24 |
| VER | `os.getenv('STEP_VERSION', 'ESV_th')` | 25 |

### `scripts/_apply_l2_rollup.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 12 |

### `scripts/_apply_l2_write.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 17 |
| STEM_MARK | `re.compile('\\((Qal\|Niphal\|Piel\|Pual\|Hiphil\|Hophal\|Hithpael)\\)', re.I)` | 19 |
| SUBSHADE | `re.compile('\\d+[a-z]\\d+\\)')` | 20 |
| THREAT | `re.compile('\\b(enemy\|enemies\|sword\|army\|armies\|slay\|kill\|death\|die\|pursue\|nations\|destroy\|siege\|fle...` | 21 |
| NEG | `re.compile('\\b(do not fear\|fear not\|be not afraid\|not be afraid\|no fear)\\b', re.I)` | 22 |

### `scripts/_apply_l2_write_refit.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 14 |
| STEM_MARK | `re.compile('\\((Qal\|Niphal\|Piel\|Pual\|Hiphil\|Hophal\|Hithpael)\\)', re.I)` | 16 |
| SUBSHADE | `re.compile('\\d+[a-z]\\d+\\)')` | 17 |
| THREAT | `re.compile('\\b(enemy\|enemies\|sword\|army\|slay\|kill\|death\|die\|nations\|destroy\|flee\|afraid of)\\b', re...` | 18 |
| NEG | `re.compile('\\b(do not fear\|fear not\|be not afraid\|not be afraid\|no fear)\\b', re.I)` | 19 |

### `scripts/_apply_language_reconcile.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 19 |

### `scripts/_apply_link_mti_term_id.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 17 |

### `scripts/_apply_migrate_sb_findings.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 15 |
| MCODE | `re.compile('^M\\d+[a-z]?$')` | 18 |

### `scripts/_apply_migrate_ve_findings_to_lexical.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 20 |

### `scripts/_apply_morph_backfill.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 20 |
| SPAN | `re.compile("<span\\s+morph='([^']*)'\\s+strong='([^']*)'>([^<]*)</span>", re.I)` | 22 |

### `scripts/_apply_persist_narration_finding_v1.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 16 |

### `scripts/_apply_phase2_flags_patch.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join('database', 'bible_research.db')` | 20 |
| PATCH_PATH | `os.path.join('Sessions', 'Patches', 'phase2-flag-reassessment-20260319-v1.json')` | 21 |
| NOW | `datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')` | 47 |

### `scripts/_apply_prose_programme_chapter01.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `Path('database/bible_research.db')` | 36 |
| CATALOGUE_PATCH | `Path('Sessions/Patches/wa-prose-catalogue-chapter0-1-v1-20260421.json')` | 37 |
| PROSE_PATCH | `Path('Sessions/Patches/wa-prose-programme-chapter0-1-v1-20260421.json')` | 38 |

### `scripts/_apply_registry_metadata_patch.py`

| constant | value | line |
|---|---|---|
| ROOT | `Path(__file__).resolve().parent.parent` | 15 |
| DB_PATH | `ROOT / 'data' / 'bible_research.db'` | 16 |
| PATCH_PATH | `ROOT / 'data' / 'imports' / 'WA' / 'Patches' / 'registry-metadata-patch-20260320-v1.json'` | 17 |

### `scripts/_apply_reset_l2_meaning_flags.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 9 |

### `scripts/_apply_sense_from_subgloss.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 11 |

### `scripts/_apply_softdelete_excluded_empty_terms.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 13 |

### `scripts/_apply_softdelete_orphan_verses.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 12 |

### `scripts/_apply_stem_patch.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join('database', 'bible_research.db')` | 19 |
| PATCH_PATH | `os.path.join('Sessions', 'Patches', 'stem-extraction-patch-20260319-v1.json')` | 20 |

### `scripts/_apply_supersede_old_mechanical.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 11 |

### `scripts/_apply_t2_soft_delete.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 18 |

### `scripts/_apply_ve_rebuild_mechanical_v1.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 20 |

### `scripts/_apply_verse_read_meaning.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 23 |

### `scripts/_apply_verse_uniqueness_cleanup.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 15 |

### `scripts/_apply_wipe_ve_lexical_v1.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 15 |
| SNAP | `os.path.join('backups', 'bible_research_pre-ve_lexical-wipe_20260615.db')` | 16 |

### `scripts/_assess_cluster_profiles.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 10 |

### `scripts/_assess_cluster_v3_2_preeval.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 15 |
| STEM_LABEL | `re.compile('\\((Qal\|Niphal\|Piel\|Pual\|Hiphil\|Hophal\|Hithpael)\\)', re.I)` | 16 |

### `scripts/_assess_corpus_keyword_map.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 12 |
| WORD | `re.compile("[a-z][a-z'-]*[a-z]", re.I)` | 13 |
| PAREN | `re.compile('\\([^)]*\\)')` | 13 |
| STOP | `set('a an and or the of to be is are was were am in on at as by for with from into onto upon that\nt...` | 14 |
| ANALYTIC | `set('metaphor metaphorical metaphorically metonymy synecdoche hyperbole idiom idiomatic figurative\n...` | 21 |
| BOOKABBR | `set('gen exod exo lev num deut deu josh jos judg jdg ruth rut sam kgs kin chr chron ezra neh esth\ne...` | 27 |

### `scripts/_assess_corpus_keyword_typed.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 13 |
| WORD | `re.compile("[a-z][a-z'-]*[a-z]", re.I)` | 14 |
| PAREN | `re.compile('\\([^)]*\\)')` | 14 |
| STOP | `set('a an and or the of to be is are was were am in on at as by for with from into onto upon that\nt...` | 15 |
| ANALYTIC | `set('metaphor metaphorical metaphorically metonymy synecdoche hyperbole idiom idiomatic figurative\n...` | 22 |
| BOOKABBR | `set('gen exod exo lev num deut deu josh jos judg jdg ruth rut sam kgs kin chr chron ezra neh esth\ne...` | 28 |
| GLUE | `set('make made making makes cause caused causes causing give given gives giving gave put puts come\n...` | 33 |
| PROSE | `set("primarily passive active means implication moral ones one's oneself himself itself themselves\n...` | 39 |

### `scripts/_assess_cross_cluster_cooccurrence.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 14 |

### `scripts/_assess_keyword_corpus_report.py`

| constant | value | line |
|---|---|---|
| GLUE | `set('make made making cause caused act acts become became give given giving put set come came go wen...` | 12 |

### `scripts/_assess_keyword_overlap.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 12 |
| WORD | `re.compile("[a-z][a-z'-]*[a-z]", re.I)` | 13 |
| PAREN | `re.compile('\\([^)]*\\)')` | 13 |
| STOP | `set('a an and or the of to be is are was were am in on at as by for with from into onto upon that\nt...` | 14 |
| ANALYTIC | `set('metaphor metaphorical metaphorically metonymy synecdoche hyperbole idiom idiomatic figurative\n...` | 21 |
| BOOKABBR | `set('gen exod exo lev num deut deu josh jos judg jdg ruth rut sam kgs kin chr chron ezra neh esth\ne...` | 27 |

### `scripts/_assess_l2_findings_view.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 11 |

### `scripts/_assess_l2_triage.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 16 |
| STEM_MARK | `re.compile('\\((Qal\|Niphal\|Piel\|Pual\|Hiphil\|Hophal\|Hithpael)\\)', re.I)` | 18 |
| SUBSHADE | `re.compile('\\d+[a-z]\\d+\\)')` | 19 |
| GOD | `re.compile('\\b(lord\|god\|almighty\|most high\|holy one)\\b', re.I)` | 20 |
| THREAT | `re.compile('\\b(enemy\|enemies\|sword\|army\|armies\|war\|slay\|kill\|death\|die\|pursue\|afraid of\|nations\|han...` | 21 |
| NEG | `re.compile('\\b(not be afraid\|do not fear\|fear not\|be not afraid\|have no fear\|not fear\|fear no\|witho...` | 23 |

### `scripts/_assess_link_correlation.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 15 |
| WORD | `re.compile("[a-z][a-z'-]*[a-z]", re.I)` | 16 |
| PAREN | `re.compile('\\([^)]*\\)')` | 16 |
| STOP | `set('a an and or the of to be is are was were am in on at as by for with from into onto upon that\nt...` | 17 |
| ANALYTIC | `set('metaphor metaphorical metaphorically metonymy synecdoche hyperbole idiom idiomatic figurative\n...` | 24 |
| BOOKABBR | `set('gen exod exo lev num deut deu josh jos judg jdg ruth rut sam kgs kin chr chron ezra neh esth\ne...` | 30 |

### `scripts/_assess_meaning_tables.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join(os.path.dirname(__file__), '..', 'database', 'bible_research.db')` | 18 |

### `scripts/_assess_mti_duplicate_terms.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 14 |
| SUFFIX | `re.compile('^([HG]\\d+)[A-Z]*$')` | 15 |

### `scripts/_assess_p2_verse_scenarios.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 24 |
| MCLUS | `lambda cc: cc is not None and cc not in ('T2', 'FLAG')` | 25 |

### `scripts/_assess_qa_method_effectiveness.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join('database', 'bible_research.db')` | 37 |
| OUT_DIR | `os.path.join('research', 'investigations')` | 38 |

### `scripts/_assess_qa_method_quality_review.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join('database', 'bible_research.db')` | 54 |
| OUT_DIR | `os.path.join('research', 'investigations')` | 55 |

### `scripts/_assess_read_dedup.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 16 |
| MRE | `re.compile('\\((M\\w+)\\)')` | 17 |

### `scripts/_assess_registry_grounding.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 15 |

### `scripts/_assess_registry_vs_keywords.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 15 |
| WORD | `re.compile("[a-z][a-z'-]*[a-z]", re.I)` | 16 |
| PAREN | `re.compile('\\([^)]*\\)')` | 16 |

### `scripts/_assess_relationship_probe.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 11 |

### `scripts/_assess_shared_forms.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 10 |

### `scripts/_assess_study_state.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 19 |
| OUT | `os.path.join('verse-analysis', '_STATE.md')` | 20 |

### `scripts/_assess_t2_cleanup.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 11 |
| STOP | `set('a an and or the of to be is are was were in on at as by for with from into onto upon that this\...` | 13 |
| WORD | `re.compile('[a-zA-Z]+')` | 19 |
| PAREN | `re.compile('\\([^)]*\\)')` | 19 |
| PARTICLE | `set("and not or to from with in on at as by for this that who what which where when why how if then\...` | 22 |
| PARTICLE | `{p.strip().lower() for p in PARTICLE if p.strip()}` | 27 |
| NOISE | `re.compile('\\b(ape\|deer\|doe\|partridge\|snail\|whelp\|donkey\|goat\|porcupine\|reptile\|locust\|bird\|fish\|ac...` | 36 |
| PROPER | `re.compile('\\b(name\|proper noun\|personal name\|place name\|city of\|region of)\\b', re.I)` | 42 |

### `scripts/_assess_t2_relevance_surface.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 12 |
| STOP | `set('a an and or the of to be is are was were in on at as by for with from into onto upon that this\...` | 14 |
| WORD | `re.compile('[a-zA-Z]+')` | 20 |
| PAREN | `re.compile('\\([^)]*\\)')` | 21 |

### `scripts/_assess_termsense_ranking.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 11 |

### `scripts/_assess_verse_assembly.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 11 |
| STEM_MARK | `re.compile('\\((Qal\|Niphal\|Piel\|Pual\|Hiphil\|Hophal\|Hithpael\|Polel\|Pilpel\|Poel\|Tiphil\|Polpal)\\)', re...` | 13 |

### `scripts/_assess_verse_corroboration.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 16 |
| STOP | `set('a an and or the of to be is are was were in on at as by for with from into onto upon\nthat this...` | 19 |
| WORD | `re.compile('[a-zA-Z]+')` | 39 |

### `scripts/_assess_verse_raw_data.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 18 |
| GRAMMAR | `re.compile('^H9\\d{3}$')` | 20 |

### `scripts/_audit_step_extract_archiving.py`

| constant | value | line |
|---|---|---|
| SRC | `Path('Sessions/Session_A/STEP Extracts')` | 24 |
| DST | `Path('data/exports/archive/STEP Extracts')` | 25 |
| OUT | `Path('research/investigations') / f"step-extract-archive-plan-{datetime.now().strftime('%Y%m%d')}.md...` | 26 |
| PATTERN | `re.compile('^(?P<stem>.+?)_(?P<date>\\d{8})(?:_v(?P<ver>\\d+))?\\.json$')` | 32 |

### `scripts/_batch_audit.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join(os.path.dirname(__file__), '..', 'database', 'bible_research.db')` | 12 |
| ROOT | `os.path.join(os.path.dirname(__file__), '..')` | 13 |

### `scripts/_batch_extract.py`

| constant | value | line |
|---|---|---|
| ROOT | `os.path.join(os.path.dirname(__file__), '..')` | 11 |
| LIST_FILE | `os.path.join(os.path.dirname(__file__), '_batch_extract_list.json')` | 12 |

### `scripts/_build_M01_verse_read_review.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 5 |
| L | `['# M01 verse-complete run — review', '', f"> Run `{run['run_id']}` → **{run['outcome']}** ({run['st...` | 16 |

### `scripts/_build_cluster_verse_read_gate.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 10 |
| CL | `a.cluster` | 21 |
| L | `[f'# {CL} — verse-read per-cluster gate', '', f'> READ-ONLY gate (`scripts/_build_cluster_verse_read...` | 30 |

### `scripts/_build_ps119.py`

| constant | value | line |
|---|---|---|
| CANDS | `json.load(open(os.path.join(os.environ.get('TMP', ''), '')) if False else open('C:\\Users\\lerouxc\\...` | 21 |
| BYSID | `{x['sid']: x for x in CANDS}` | 24 |
| HEART | `{2: ('the psalmist', IB, "'Blessed are those who... seek him with their whole HEART' - the undivided...` | 185 |
| FORGET | `{16: ('the psalmist', IB, GOD, "'I will delight in your statutes; I will not FORGET your word' - the...` | 221 |
| SHAME | `{6: ('the psalmist', IB, "'Then I shall not be PUT TO SHAME, having my eyes fixed on all your comman...` | 263 |
| CHARS | `{('H3925', 7): ('learn (lamad)', 'action', _P, 'learn', 'external:god', "v7: 'I will praise you with...` | 320 |

### `scripts/_build_t2_flag_sample.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 6 |

### `scripts/_build_term_verse_findings_report.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 9 |
| L | `[f'# Verse-read findings report — {len(ids)} terms × up to {a.verses} verses', '', '> READ-ONLY. Per...` | 27 |

### `scripts/_build_vc_batch.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join('database', 'bible_research.db')` | 15 |
| OUTPUT_DIR | `os.path.join('data', 'exports', 'verse_context')` | 16 |

### `scripts/_build_vc_revision_ledger.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 24 |
| ARCHIVE | `os.path.join('archive', 'patches')` | 25 |
| OUT_DIR | `os.path.join('outputs', 'investigations')` | 26 |

### `scripts/_build_verse_read_pilot_review.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 7 |

### `scripts/_cc_verse_read.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 20 |

### `scripts/_check_doc_versions.py`

| constant | value | line |
|---|---|---|
| ROOT | `Path(__file__).resolve().parent.parent` | 36 |
| DOCS_DIR | `ROOT / 'Workflow' / 'Instructions'` | 38 |
| ARCHIVE_DIR | `ROOT / 'Workflow' / 'archive'` | 39 |
| FILENAME_RE | `re.compile('^(?P<prefix>wa-.+)-v(?P<major>\\d+)_(?P<minor>\\d+)-(?P<date>\\d{8})\\.md$')` | 43 |
| VERSION_INLINE_RE | `re.compile('(?:[Vv]ersion\|[Ii]nstruction)[:\\s]+v?\\s*(\\d+)_(\\d+)')` | 50 |

### `scripts/_check_integrity_controls.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 17 |
| OUT | `os.path.join('outputs', 'integrity')` | 18 |

### `scripts/_check_softdelete_integrity.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 17 |

### `scripts/_check_ve_seat_completeness.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 16 |
| SEAT_GLOSS | `re.compile('\\b(heart\|soul\|spirit\|mind\|conscience\|bowel\|kidney\|reins\|inward\|inmost\|liver\|flesh\|belly...` | 18 |
| FACULTY_ACT | `re.compile('\\b(remember\|recall\|discern\|understand\|knowledge\|will\\b\|decide\|want\|wish\|prophes\|return...` | 21 |

### `scripts/_check_ve_signal_lists.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 14 |
| ACTUAL | `{'DIVINE': eng.DIVINE, 'SPIRIT_BEINGS': eng.SPIRIT_BEINGS, 'PERCEPTION': eng.PERCEPTION, 'COGNITION'...` | 45 |

### `scripts/_explore_cluster_timing.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 25 |

### `scripts/_explore_drop_code_findings.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 17 |
| ALL_OBS | `[o for _f, _t, ol in FAMILIES for o in ol]` | 33 |

### `scripts/_explore_m_vs_r_divergence.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 20 |
| STOP | `set('a an the and or but to be is are was were of in on at by for with as from into onto\n  that thi...` | 23 |

### `scripts/_explore_tier_findings.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 25 |
| SLUG2CODE | `{v: k for k, v in SLUG.items()}` | 41 |

### `scripts/_explore_ve_by_cluster.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 17 |

### `scripts/_generate_cluster_gate.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 20 |

### `scripts/_generate_dimension_report.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join(os.path.dirname(__file__), '..', 'database', 'bible_research.db')` | 13 |
| OUT_DIR | `os.path.join(os.path.dirname(__file__), '..', 'outputs', 'reports', 'programme')` | 14 |

### `scripts/_generate_meaning_quality_check.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 10 |

### `scripts/_generate_programme_report.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join(os.path.dirname(__file__), '..', 'database', 'bible_research.db')` | 10 |
| OUT_DIR | `os.path.join(os.path.dirname(__file__), '..', 'Workflow', 'Programme')` | 11 |

### `scripts/_generate_verse_meanings_export.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 12 |

### `scripts/_integrity_full_check.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'database', 'bible_researc...` | 4 |

### `scripts/_list_shared_words.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join(os.path.dirname(__file__), '..', 'database', 'bible_research.db')` | 5 |

### `scripts/_patch_report.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join(os.path.dirname(__file__), '..', 'database', 'bible_research.db')` | 6 |
| REPORT | `os.path.join(os.path.dirname(__file__), '..', 'outputs', 'wa-programme-status-report-20260328.md')` | 7 |

### `scripts/_pro_read_lib.py`

| constant | value | line |
|---|---|---|
| OUT | `os.path.join('verse-analysis', 'proverbs', '_read')` | 20 |

### `scripts/_produce_final_extract.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join(os.path.dirname(__file__), '..', 'database', 'bible_research.db')` | 17 |
| OUT_DIR | `os.path.join(os.path.dirname(__file__), '..', 'data', 'exports')` | 18 |

### `scripts/_produce_registry_full_extract.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 10 |

### `scripts/_produce_vc_word_report.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join('database', 'bible_research.db')` | 28 |

### `scripts/_produce_ve_narration_v1.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 16 |

### `scripts/_prototype_l1_mechanical.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 14 |
| STOP | `set('a an and or the of to be is are was were in on at as by for with from into onto upon that this\...` | 17 |
| WORD | `re.compile('[a-zA-Z]+')` | 23 |
| STEMS | `re.compile('\\((Qal\|Niphal\|Piel\|Pual\|Hiphil\|Hophal\|Hithpael\|Peal\|Pael\|Aphel\|Haphel\|Ithpe?al\|Ithpaal\|...` | 39 |
| NUMSENSE | `re.compile('(?<![a-z])(\\d)\\)')` | 40 |
| HOMONYM | `re.compile('TWOT\|Also means\|another word\|homonym', re.I)` | 41 |
| PHYS | `{stem(w) for w in 'shatter shattered broken break crush melt waves wave breaker pour shoot body fles...` | 44 |
| EXT | `{stem(w) for w in 'punish punishment penalty vengeance avenge judgment judgement recompense retribut...` | 47 |

### `scripts/_prototype_l1_morph.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 16 |
| BASE | `os.getenv('STEP_LOCAL_URL', 'http://localhost:8989').rstrip('/')` | 17 |
| STEM_LABEL | `re.compile('\\((Qal\|Niphal\|Piel\|Pual\|Hiphil\|Hophal\|Hithpael)\\)', re.I)` | 21 |

### `scripts/_prototype_meaning_run.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 15 |
| SPAN | `re.compile("<span\\s+morph='([^']*)'\\s+strong='([^']*)'>([^<]*)</span>", re.I)` | 17 |
| STEM_MARK | `re.compile('\\((Qal\|Niphal\|Piel\|Pual\|Hiphil\|Hophal\|Hithpael\|Polel\|Pilpel\|Poel)\\)', re.I)` | 21 |
| NUM_MARK | `re.compile('(?:^\|\\n)\\s*(\\d+)\\)\\s')` | 22 |
| SUBSHADE | `re.compile('\\d+[a-z]\\d+\\)')` | 48 |

### `scripts/_prototype_p1_keywords.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 17 |
| WORD | `re.compile("[a-z][a-z'-]*[a-z]\|[a-z]", re.I)` | 19 |
| PAREN | `re.compile('\\([^)]*\\)')` | 20 |
| STOP | `set('a an and or the of to be is are was were am being been in on at as by for with from into onto\n...` | 22 |
| ANALYTIC | `set('metaphor metaphorical metaphorically metonymy metonymical synecdoche hyperbole hyperbolic\nidio...` | 30 |
| BOOKABBR | `set('gen exod exo lev num deut deu josh jos judg jdg ruth rut sam kgs kin chr chron ezra neh esth\ne...` | 38 |

### `scripts/_prototype_step_morph.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 17 |
| SPAN | `re.compile("<span\\s+morph='([^']*)'\\s+strong='([^']*)'>([^<]*)</span>", re.I)` | 19 |

### `scripts/_realign_meaning_tables.py`

| constant | value | line |
|---|---|---|
| ROOT | `os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))` | 49 |
| DB | `os.path.join(ROOT, 'database', 'bible_research.db')` | 54 |

### `scripts/_realign_quality_flags.py`

| constant | value | line |
|---|---|---|
| ROOT | `os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))` | 37 |
| DB | `os.path.join(ROOT, 'database', 'bible_research.db')` | 43 |

### `scripts/_repair_02_zero_padding.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `Path(__file__).parent.parent / 'data' / 'bible_research.db'` | 11 |

### `scripts/_repair_03_wa_file_index.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `Path(__file__).parent.parent / 'data' / 'bible_research.db'` | 10 |

### `scripts/_repair_05_wa_term_related_words.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `Path(__file__).parent.parent / 'data' / 'bible_research.db'` | 9 |

### `scripts/_repair_06_wa_term_root_family.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `Path(__file__).parent.parent / 'data' / 'bible_research.db'` | 9 |

### `scripts/_repair_07_wa_verse_records.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `Path(__file__).parent.parent / 'data' / 'bible_research.db'` | 14 |

### `scripts/_run_ve_reads_governed.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 17 |

### `scripts/_term_sharing_spider.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join(os.path.dirname(__file__), '..', 'database', 'bible_research.db')` | 12 |
| OUT | `os.path.join(os.path.dirname(__file__), '..', 'outputs')` | 13 |

### `scripts/_update_claude_code_instructions.py`

| constant | value | line |
|---|---|---|
| PATH | `os.path.join(os.path.dirname(__file__), '..', 'data', 'imports', 'WA', 'Workflow', 'Framework_B', 'S...` | 4 |

### `scripts/_update_reference_doc.py`

| constant | value | line |
|---|---|---|
| PATH | `os.path.join(os.path.dirname(__file__), '..', 'data', 'imports', 'WA', 'Workflow', 'Framework_B', 'S...` | 4 |

### `scripts/_update_registry_guide.py`

| constant | value | line |
|---|---|---|
| GUIDE_PATH | `os.path.join(os.path.dirname(__file__), '..', 'data', 'imports', 'WA', 'Workflow', 'Framework_B', 'S...` | 4 |

### `scripts/_ve_engine_v2.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 18 |
| SPAN | `re.compile("<span\\s+morph='([^']*)'\\s+strong='([^']*)'>([^<]*)</span>", re.I)` | 19 |
| SPIRIT_NONSEAT | `re.compile('\\b(wind\|winds\|breath\|air\|side\|quarter\|blast)\\b', re.I)` | 52 |
| QEREB_SEAT | `re.compile('\\b(within\|inward\|inmost\|inner)\\b', re.I)` | 53 |
| CHEQ_SEAT | `re.compile('\\b(bosom\|breast\|chest\|within\|heart)\\b', re.I)` | 54 |
| FLESH_NONSEAT | `re.compile('\\b(meat\|food\|kin\|kinsman\|kinsmen\|relative\|relatives\|mankind\|creature\|animal)\\b', re.I)` | 55 |
| VISCERA_LITERAL | `re.compile('\\b(entrails\|intestines\|carcass)\\b', re.I)` | 56 |
| PERC_COG | `PERCEPTION \| COGNITION` | 76 |
| SEAT | `{_canon(k): v for k, v in SEAT.items()}` | 81 |
| DIVINE | `{_canon(s) for s in DIVINE}` | 82 |
| FACULTY_LEMMA | `{_canon(k): v for k, v in FACULTY_LEMMA.items()}` | 83 |
| INTENSIFIER | `{_canon(k): v for k, v in INTENSIFIER.items()}` | 84 |
| FROM_PREP | `{_canon(s) for s in FROM_PREP}` | 85 |
| SPEECH | `{_canon(s) for s in SPEECH}` | 86 |
| INHERENT_VALENCE | `{_canon(k): v for k, v in INHERENT_VALENCE.items()}` | 87 |
| NEGATION | `{_canon(s) for s in NEGATION}` | 88 |
| PERCEPTION | `{_canon(s) for s in PERCEPTION}` | 89 |
| COGNITION | `{_canon(s) for s in COGNITION}` | 90 |
| PERC_COG | `PERCEPTION \| COGNITION` | 91 |
| CAUSAL | `{_canon(s) for s in CAUSAL}` | 92 |
| COORD | `{_canon(s) for s in COORD}` | 93 |
| SPIRIT_BEINGS | `{_canon(s) for s in SPIRIT_BEINGS}` | 94 |
| SEAT | `{_canon(k): v for k, v in SEAT.items()}` | 95 |
| SPIRIT_LEMMAS | `{_canon('H7307'), _canon('H7308'), _canon('G4151'), _canon('H5397')}` | 96 |
| QEREB | `_canon('H7130')` | 97 |
| MEEH | `_canon('H4578')` | 97 |
| CHEQ | `_canon('H2436')` | 97 |
| FLESH_LEMMAS | `{_canon('H1320'), _canon('H1321'), _canon('H7607'), _canon('G4561')}` | 98 |

### `scripts/analytics/bible_analytics.py`

| constant | value | line |
|---|---|---|
| ROOT_DIR | `os.path.join(os.path.dirname(__file__), '..')` | 26 |

### `scripts/analytics/db_client.py`

| constant | value | line |
|---|---|---|
| ROOT_DIR | `os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))` | 29 |

### `scripts/analytics/step_client.py`

| constant | value | line |
|---|---|---|
| CONFIG_PATH | `pathlib.Path(__file__).resolve().parents[2] / 'iba' / 'config' / 'utility' / 'step.json'` | 41 |

### `scripts/analytics/zotero_client.py`

| constant | value | line |
|---|---|---|
| ROOT_DIR | `os.path.join(os.path.dirname(__file__), '..')` | 21 |

### `scripts/apply_session_patch.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join(os.path.dirname(__file__), '..', 'database', 'bible_research.db')` | 75 |
| ARCHIVE_DIR | `os.path.join(os.path.dirname(__file__), '..', 'archive', 'patches')` | 76 |
| CANONICAL_DIMENSIONS | `_FALLBACK_CANONICAL_DIMENSIONS` | 133 |

### `scripts/backfill_root_families.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join(os.path.dirname(__file__), '..', 'database', 'bible_research.db')` | 21 |

### `scripts/backup_db_to_nas.py`

| constant | value | line |
|---|---|---|
| DEFAULT_SOURCE | `_ROOT / 'iba' / 'app' / 'db' / 'iba.db'` | 42 |
| DEFAULT_TARGET | `Path('\\\\LSUK-SYNRACK\\HomeMedia\\bible_study_projects\\db_backups')` | 43 |
| MIN_PLAUSIBLE_BYTES | `50 * 1024 * 1024` | 51 |

### `scripts/build_cause_api_package.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 13 |

### `scripts/build_cluster_findings_digest.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 17 |
| DATE | `datetime.now(timezone.utc).strftime('%Y%m%d')` | 18 |

### `scripts/build_complete_extract.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join(os.path.dirname(__file__), '..', 'database', 'bible_research.db')` | 20 |
| OUT_DIR | `os.path.join(os.path.dirname(__file__), '..', 'data', 'exports', 'Session C')` | 21 |

### `scripts/build_corpus_prose.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join('database', 'bible_research.db')` | 43 |
| OUT_DIR | `os.path.join('Workflow', 'Programme', 'Corpus_prose')` | 44 |

### `scripts/build_correlation_extract.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join(os.path.dirname(__file__), '..', 'database', 'bible_research.db')` | 29 |
| OUT_DIR | `os.path.join(os.path.dirname(__file__), '..', 'data', 'exports', 'session_d')` | 30 |

### `scripts/build_dimension_extract.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join(os.path.dirname(__file__), '..', 'database', 'bible_research.db')` | 24 |
| OUT_DIR | `os.path.join(os.path.dirname(__file__), '..', 'data', 'exports', 'dimension_review')` | 25 |

### `scripts/build_field_api_package.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 11 |

### `scripts/build_file_manifest.py`

| constant | value | line |
|---|---|---|
| PROJECT_ROOT | `Path(__file__).resolve().parent.parent` | 30 |
| MANIFEST_PATH | `PROJECT_ROOT / 'database' / 'file_manifest.json'` | 31 |
| DATE_COMPACT | `re.compile('(\\d{4})(\\d{2})(\\d{2})')` | 92 |
| DATE_HYPHEN | `re.compile('(\\d{4})-(\\d{2})-(\\d{2})')` | 93 |
| REG_PATTERNS | `[re.compile('(?:^\|[-_])(\\d{3})[-_]'), re.compile('registry[_-]?(\\d+)', re.I), re.compile('reg[_-]?...` | 96 |
| VERSION_RE | `re.compile('-v(\\d+(?:\\.\\d+)?)')` | 104 |
| VCB_RE | `re.compile('vcb[_-]?(\\d{3})', re.I)` | 107 |
| CLUSTER_RE | `re.compile('(?:^\|[-_])(c\\d{2})(?:[-_]\|$)', re.I)` | 110 |
| WORD_FROM_WA | `re.compile('wa-\\d{3}-([a-z]+)')` | 113 |
| WORD_FROM_UNDERSCORE | `re.compile('^([a-z]+)_\\d+')` | 114 |
| WORD_FROM_LONG | `re.compile('(?:registry\|reg)\\d+-([a-z]+)', re.I)` | 115 |

### `scripts/build_file_patterns_extract.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join('database', 'bible_research.db')` | 26 |
| OUT_DIR | `os.path.join('Workflow', 'reference')` | 27 |

### `scripts/build_label_patterns_extract.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join('database', 'bible_research.db')` | 25 |
| OUT_DIR | `os.path.join('Workflow', 'reference')` | 26 |

### `scripts/build_m01_by_characteristic.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 7 |
| CHAR_SET | `{cid: {canon(s) for s in strs} for cid, _n, _d, strs in CHARS}` | 47 |

### `scripts/build_m01_findings_oldnew_extract.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 11 |

### `scripts/build_m02_findings_oldnew_extract.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 12 |
| OUT_OLD | `f'{NEW_DIR}/WA-m02-findings-OLD-dbexport-bytier-v1-20260619.md'` | 14 |
| OUT_NEW | `f'{NEW_DIR}/WA-m02-findings-NEW-merged-bytier-v1-20260619.md'` | 15 |
| CLUSTER_FINDINGS_FILE | `f'{NEW_DIR}/wa-m02-cluster-findings-v1_0-20260619.md'` | 16 |

### `scripts/build_obs_catalogue_export.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join('database', 'bible_research.db')` | 27 |
| OUT_DIR | `os.path.join('data', 'imports', 'WA', 'Workflow', 'Framework_B', 'Session_B')` | 28 |

### `scripts/build_obs_catalogue_tiered_extract.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join('database', 'bible_research.db')` | 22 |
| OUT_DIR | `os.path.join('Workflow', 'Tiers')` | 23 |

### `scripts/build_patch_types_extract.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join('database', 'bible_research.db')` | 25 |
| OUT_DIR | `os.path.join('Workflow', 'reference')` | 26 |

### `scripts/build_programme_prose_extract.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join('database', 'bible_research.db')` | 33 |
| OUT_DIR | `os.path.join('Workflow', 'Programme', 'programme_prose')` | 34 |
| DOCX_OUT_DIR | `os.path.join('outputs', 'docx')` | 35 |

### `scripts/build_reference_snapshot.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join('database', 'bible_research.db')` | 38 |
| OUT_DIR | `os.path.join('Workflow', 'reference')` | 39 |

### `scripts/build_rules_extract.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join('database', 'bible_research.db')` | 32 |
| OUT_DIR | `os.path.join('Workflow', 'reference')` | 33 |

### `scripts/build_script_registry.py`

| constant | value | line |
|---|---|---|
| ROOT | `os.path.dirname(os.path.dirname(os.path.abspath(__file__)))` | 18 |
| SCRIPTS | `os.path.join(ROOT, 'scripts')` | 19 |
| VERSION_DATE | `re.compile('(_v\\d+)?(_\\d{8})?(\\.py\|\\.ps1)$')` | 39 |
| VN | `re.compile('_v(\\d+)')` | 40 |
| DT | `re.compile('_(\\d{8})')` | 41 |

### `scripts/build_session_a_prose.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `Path('database/bible_research.db')` | 35 |
| OUTPUT_DIR | `Path('data/exports/session_a')` | 36 |
| TERM_OUTPUT_DIR | `Path('Sessions/Session_A/terms')` | 37 |
| FILTER_REMINDER | `dedent("    > **Governing filter (VC Instruction §3).** For each verse, ask:\n    > *Does this verse...` | 43 |

### `scripts/build_ve_lexical_extract.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 15 |
| QUAL_KEEP | `{eng.base(s) for s in set(eng.SEAT) \| set(eng.DIVINE) \| set(eng.INTENSIFIER) \| set(eng.FACULTY_LEMMA...` | 21 |

### `scripts/build_vocab_extract.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join('database', 'bible_research.db')` | 29 |
| OUT_DIR | `os.path.join('Workflow', 'reference')` | 30 |

### `scripts/build_word_relationship_report.py`

| constant | value | line |
|---|---|---|
| ROOT | `os.path.dirname(os.path.dirname(os.path.abspath(__file__)))` | 13 |
| DB | `os.path.join(ROOT, 'database', 'bible_research.db')` | 14 |

### `scripts/classify_term_introduction_source.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join('database', 'bible_research.db')` | 47 |

### `scripts/combine_cluster_published_to_docx.py`

| constant | value | line |
|---|---|---|
| REPO | `Path(__file__).resolve().parent.parent` | 59 |
| DB | `REPO / 'database' / 'bible_research.db'` | 60 |
| RE_BOLD | `re.compile('\\*\\*(.+?)\\*\\*')` | 63 |
| RE_ITALIC_AST | `re.compile('(?<!\\*)\\*([^*\\n]+?)\\*(?!\\*)')` | 64 |
| RE_ITALIC_UND | `re.compile('(?<![A-Za-z0-9_])_([^_\\n]+?)_(?![A-Za-z0-9_])')` | 65 |
| RE_LINK | `re.compile('\\[([^\\]]+)\\]\\(([^)]+)\\)')` | 66 |
| RE_HTML_COMMENT | `re.compile('<!--.*?-->', re.DOTALL)` | 67 |
| RE_HR | `re.compile('^---+\\s*$')` | 70 |
| RE_EVIDENCE_OPEN | `re.compile('<!--\\s*EVIDENCE[\\s:]', re.IGNORECASE)` | 71 |
| RE_EVIDENCE_CLOSE | `re.compile('<!--\\s*/\\s*EVIDENCE', re.IGNORECASE)` | 72 |
| RE_CROSS_CHAPTER_HEADER | `re.compile('^##\\s+Cross-chapter\\s+consistency', re.IGNORECASE)` | 73 |
| RE_NUMBERED_SECTION_HEADER | `re.compile('^##\\s+\\d+\\.\\s+')` | 76 |
| RE_ANALYTICAL_LABEL | `re.compile('^\\s*\\*\\*\\s*Evidence\\b[^*]*\\*\\*\\s*$', re.IGNORECASE)` | 79 |
| RE_CHAPTER_FILE | `re.compile('^wa-cluster-([A-Za-z0-9]+)-ch(\\d+)-draft-v(\\d+)-(\\d{8})\\.md$', re.IGNORECASE)` | 84 |
| RE_APPENDIX_FILE | `re.compile('^wa-cluster-([A-Za-z0-9]+)-app([a-z])-draft-v(\\d+)-(\\d{8})\\.md$', re.IGNORECASE)` | 87 |

### `scripts/cost_ledger.py`

| constant | value | line |
|---|---|---|
| DEFAULT_PROJECTS_ROOT | `pathlib.Path.home() / '.claude' / 'projects'` | 40 |
| DEFAULT_RATES | `pathlib.Path('scripts/token_cost_rates.json')` | 41 |
| DEFAULT_SUBS | `pathlib.Path('scripts/cost_subscriptions.json')` | 42 |
| DEFAULT_OUT | `pathlib.Path('outputs/cost-history')` | 43 |
| API_EXPORT_DIR | `DEFAULT_OUT / 'api-exports'` | 44 |

### `scripts/export_database_schema.py`

| constant | value | line |
|---|---|---|
| ROOT_DIR | `os.path.join(os.path.dirname(__file__), '..')` | 25 |
| DB_PATH | `os.path.join(ROOT_DIR, 'database', 'bible_research.db')` | 26 |
| DEFAULT_OUTPUT_DIR | `os.path.join(ROOT_DIR, 'Workflow', 'schema')` | 27 |

### `scripts/export_prose_chapter_edit.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `Path('database/bible_research.db')` | 13 |
| DEFAULT_OUT_DIR | `Path('outputs/markdown')` | 14 |

### `scripts/export_tier_catalogue.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 8 |

### `scripts/export_ve_status_reports.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 8 |

### `scripts/extract_term_data.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join('database', 'bible_research.db')` | 24 |

### `scripts/generate_programme_snapshot.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join('database', 'bible_research.db')` | 32 |
| DEFAULT_OUT_DIR | `os.path.join('outputs', 'markdown')` | 33 |

### `scripts/generate_registry_overview.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join(os.path.dirname(__file__), '..', 'database', 'bible_research.db')` | 24 |
| OUT_DIR | `os.path.join(os.path.dirname(__file__), '..', 'Workflow', 'Programme', 'Program_reports')` | 25 |

### `scripts/generate_session_a_extract.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join('database', 'bible_research.db')` | 53 |
| SECTION_RENDERERS | `{'summary': render_summary, 'meaning': render_meaning, 'terms': render_terms, 'verses': render_verse...` | 1017 |

### `scripts/import_prose_chapter_edit.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `Path('database/bible_research.db')` | 15 |
| DEFAULT_PATCH_DIR | `Path('Sessions/Patches')` | 16 |
| MARKER_RE | `re.compile('<!-- PROSE_([A-Z_]+): ?(.*?) -->')` | 17 |
| ID_RE | `re.compile('<!-- PROSE_SECTION_ID: (\\d+) -->')` | 18 |

### `scripts/populate_dimension_index.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join('database', 'bible_research.db')` | 22 |

### `scripts/readiness_sweep_programme_scan.py`

| constant | value | line |
|---|---|---|
| DATE_STR | `datetime.now(timezone.utc).strftime('%Y%m%d')` | 40 |
| OUT_MD | `Path(f'outputs/reports/wa-global-readinesssweep-programme-scan-{DATE_STR}.md')` | 41 |
| OUT_JSON | `Path(f'outputs/reports/wa-global-readinesssweep-programme-scan-raw-{DATE_STR}.json')` | 42 |

### `scripts/search_prose.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `Path('database/bible_research.db')` | 20 |
| DEFAULT_OUT_DIR | `Path('outputs/markdown')` | 21 |

### `scripts/token_cost_history.py`

| constant | value | line |
|---|---|---|
| DEFAULT_PROJECTS_DIR | `pathlib.Path.home() / '.claude' / 'projects' / 'c--Bible-study-projects'` | 43 |
| DEFAULT_RATES | `pathlib.Path('scripts/token_cost_rates.json')` | 44 |
| DEFAULT_OUT | `pathlib.Path('outputs/cost-history')` | 45 |

### `scripts/v3_2_l1.py`

| constant | value | line |
|---|---|---|
| DB | `os.path.join('database', 'bible_research.db')` | 16 |
| STOP | `set('a an and or the of to be is are was were in on at as by for with from into onto upon that this\...` | 19 |
| WORD | `re.compile('[a-zA-Z]+')` | 26 |
| PAREN | `re.compile('\\([^)]*\\)')` | 26 |
| SREF | `re.compile('\\b[A-Z][a-z]{1,2}\\.?\\s*\\d')` | 26 |
| STEMS | `re.compile('\\((Qal\|Niphal\|Piel\|Pual\|Hiphil\|Hophal\|Hithpael)\\)', re.I)` | 27 |
| NUMSENSE | `re.compile('(?<![a-z])(\\d)\\)')` | 28 |
| HOMONYM | `re.compile('TWOT\|to shoot\|to pour', re.I)` | 29 |

### `scripts/verse_vertical_pass.py`

| constant | value | line |
|---|---|---|
| DB_PATH | `os.path.join(os.path.dirname(__file__), '..', 'database', 'bible_research.db')` | 20 |
| OUT_DIR | `os.path.join(os.path.dirname(__file__), '..', 'data', 'exports', 'vertical_pass')` | 21 |
