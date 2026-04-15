# Assessment: wa_cross_registry_links

> Analysis date: 2026-04-14
> Table row count: 158 links across 29 source registries
> Related reference table: wa_crosslink_type (11 rows)

---

## 1. Table Purpose

`wa_cross_registry_links` records explicit semantic connections between word registries, created during Session A analysis. Each row says: "registry X is connected to word Y through Strong's term Z, via connection type T." The `note` field explains the reasoning.

The connection types are defined in `wa_crosslink_type` (11 codes). Links are anchored to `wa_file_index` (source registry) and optionally to `word_registry` (target registry).

---

## 2. Field-Level Summary

### file_id (FK to wa_file_index)

| Metric | Value |
|--------|-------|
| NULL | 0 |
| Populated | 158 (100%) |
| Distinct file_ids | 43 |
| Orphaned (no matching wa_file_index) | 0 |

FK integrity is clean. All links trace back to a valid source file.

### linked_word

| Metric | Value |
|--------|-------|
| NULL | 0 |
| Distinct words | 43 |

Top targets by frequency:

| linked_word | Count |
|-------------|------:|
| anguish | 16 |
| anger | 13 |
| grief | 12 |
| soul | 9 |
| agony | 8 |
| sorrow | 7 |
| humility | 7 |
| distress | 7 |
| desire | 7 |
| pride | 6 |

### linked_registry_id (FK to word_registry)

| Metric | Value |
|--------|-------|
| NULL | 7 |
| Populated | 151 (96%) |
| Distinct target registries | 33 |
| Orphaned (no matching word_registry) | 0 |

The 7 NULL rows reference words/concepts that do not have their own registry entry:

| id | linked_word | connecting_term | note (truncated) |
|----|-------------|-----------------|------------------|
| 3 | horror | miph.le.tset | miph.le.tset belongs to the pa.lats / pal.la.tsut / tiph.le.tset root cluster... |
| 11 | spirit/ruach | ru.ach H7307J | ru.ach (H7307) is a primary biblical anthropology word that will have its own re... |
| 25 | anointed / Messiah | ma.shi.ach | ma.shi.ach (H4899) is the OT root of the Messianic title... |
| 26 | joy / gladness | ma.shach | Psa 45:7 and Heb 1:9 use 'oil of gladness' in the context of anointing... |
| 27 | Holy Spirit / Spirit | chrio | chrio (G5548) in Luk 4:18, Act 10:38, and 2Cor 1:21 links anointing directly to... |
| 54 | Holy Spirit | a.tsav | Isa 63:10 uses a.tsav to describe Israel grieving the Holy Spirit... |
| 57 | Holy Spirit | lu.pe.o | Eph 4:30 -- 'do not grieve the Holy Spirit of God' -- uses lu.pe.o (G3076)... |

These are legitimate references to concepts outside the programme's registry scope. They are not data errors.

### connection_type_id (FK to wa_crosslink_type)

| Metric | Value |
|--------|-------|
| NULL | 0 |
| Populated | 158 (100%) |

Distribution across all 11 defined types:

| type_code | Count | % | Description |
|-----------|------:|--:|-------------|
| SHARED_TERM | 64 | 41% | The same Hebrew or Greek term appears in both word studies |
| SEMANTIC_OVERLAP | 45 | 28% | The two registries share overlapping meaning space |
| SHARED_ROOT | 21 | 13% | The registries share a common etymological root |
| SHARED_VERSE | 16 | 10% | The same verse references appear in both word studies |
| THEMATIC_LINK | 3 | 2% | Thematic connection identified during Session B analysis |
| THEOLOGICAL | 2 | 1% | The registries are connected by a theological concept or theme |
| SEMANTIC_OPPOSITION | 2 | 1% | The registries represent antonyms or semantic contrasts |
| CO_OCCURRENCE | 2 | 1% | Terms from the two registries frequently appear together in passages |
| SISTER_REGISTRY | 1 | 1% | Parallel registries covering closely related vocabulary |
| OVERLAPPING_DOMAIN | 1 | 1% | Registries sharing terms with overlapping semantic domains |
| CAUSATIVE_CHAIN | 1 | 1% | Causal relationship between inner states across registries |

The table is heavily skewed toward the first four types (92% of all links). The remaining seven types have 1-3 uses each — either underutilised or narrowly applicable.

### connecting_term

| Metric | Value |
|--------|-------|
| NULL | 6 |
| Populated | 152 (96%) |
| Distinct Strong's numbers | 117 |

Top connecting terms:

| connecting_term | Gloss (from mti_terms) | Count |
|-----------------|----------------------|------:|
| ne.phesh | (no mti match) | 7 |
| chul | (no mti match) | 4 |
| na.cham | (no mti match) | 4 |
| ya.gon | (no mti match) | 3 |
| me.eh | (no mti match) | 3 |
| cha.raph / cher.pah | (no mti match) | 3 |
| ba.ash | (no mti match) | 3 |
| za.am | (no mti match) | 2 |
| ya.chal | (no mti match) | 2 |
| sofia | (no mti match) | 2 |

**Critical finding:** The `connecting_term` field stores transliterated forms (e.g. "ne.phesh", "chul", "na.cham") rather than Strong's numbers (e.g. "H5315", "H2342", "H5162"). This means:

- The field **cannot be joined** to `mti_terms.strongs_number` or `wa_term_inventory.strongs_number`
- Programmatic resolution of which term creates a connection is not possible
- The transliteration format is also inconsistent (some include Strong's codes inline like "ru.ach H7307J", most do not)

This is a **data format issue**, not a data quality issue — the information is present but not in a machine-readable form.

### note

| Metric | Value |
|--------|-------|
| NULL | 0 |
| Empty string | 0 |
| Populated | 158 (100%) |

Every row has a substantive explanation. Sample notes:

- *"ne.phesh appears in both heart and soul word sets as XREF."*
- *"o.du.ne (G3601) is glossed 'anguish' and has direct meaning overlap with any anguish word set. Rom 9:2 pairs it with lu."*
- *"chrio (G5548) in Luk 4:18, Act 10:38, and 2Cor 1:21 links anointing directly to the conferral of the Holy Spirit."*
- *"pang (tsir H6735C) appears in sorrow STEP header but is owned by anguish (registry 005). Treated as cross-reference in both."*

The notes are the most analytically valuable field in the table — they carry the reasoning that the structured fields do not.

### last_changed

| Metric | Value |
|--------|-------|
| NULL | 12 (8%) |
| Populated | 146 (92%) |
| Earliest | 2026-03-16 11:32:38 |
| Latest | 2026-03-26T06:28:08Z |

Only two dates:

| Date | Count |
|------|------:|
| 2026-03-16 | 140 |
| 2026-03-26 | 6 |

All links were created in two bulk operations during Session A.

---

## 3. Provenance

### Source registries (which registries created outbound links)

| Registry | Word | Links |
|----------|------|------:|
| 183 | heart | 13 |
| 71 | grief | 13 |
| 43 | desire | 11 |
| 5 | anguish | 11 |
| 103 | love | 8 |
| 151 | sorrow | 8 |
| 51 | distress | 8 |
| 135 | repentance | 6 |
| 146 | shame | 6 |
| 178 | wrath | 6 |
| 182 | soul | 6 |
| 184 | spirit | 6 |
| 197 | authority | 6 |
| 116 | patience | 4 |
| 123 | pride | 4 |

Only **29 of 214 registries** (14%) have outbound links. These are all from the first wave of Session A analysis.

### Directionality

Links are **unidirectional**. If registry 103 (love) links to registry 43 (desire), there is no guarantee that registry 43 links back to registry 103. The table records "from registry X, we observed a connection to word Y" — it is a source-side observation, not a bidirectional relationship.

Sample link chains:

```
abomination     (reg   1) --[SHARED_TERM]-->      anger       via za.am
abomination     (reg   1) --[SEMANTIC_OVERLAP]-->  shame       via ta.av
abomination     (reg   1) --[SHARED_ROOT]-->       horror      via miph.le.tset
love            (reg 103) --[SHARED_TERM]-->       desire      via o.hav
love            (reg 103) --[SHARED_VERSE]-->      hope        via che.sed
love            (reg 103) --[SEMANTIC_OVERLAP]-->  grief       via ra.cha.mim
patience        (reg 116) --[SHARED_TERM]-->       anger       via aph
patience        (reg 116) --[SHARED_ROOT]-->       hope        via ya.chal
patience        (reg 116) --[SHARED_VERSE]-->      humility    via makrothumia
```

---

## 4. Coverage

| Metric | Value |
|--------|------:|
| Total registries in programme | 214 |
| Source registries (have outbound links) | 29 (14%) |
| Target registries (linked TO) | 33 |
| Total links | 158 |
| Average links per source registry | 5.4 |
| Registries with zero links (source or target) | ~160 (75%) |

Coverage is sparse. Three-quarters of the programme's registries have no cross-registry links at all. This reflects the early-stage nature of the data — Session A analysed a subset of registries, and the correlation/SD pointer systems in Session B/D are designed to build a much richer cross-registry map.

---

## 5. Data Quality Issues

### 5.1 connecting_term format mismatch

The field stores transliterated forms instead of Strong's numbers. This prevents programmatic joins to `mti_terms` or `wa_term_inventory`. A repair script could resolve most transliterations to Strong's numbers using `mti_terms.transliteration` or `wa_term_inventory.transliteration`, but the inconsistent formatting (some entries have inline Strong's codes, some use dotted notation, some use slashes for alternatives) makes automated resolution non-trivial.

### 5.2 Seven unresolved target registries

Seven links point to words not in the registry (horror, spirit/ruach, Holy Spirit, anointed/Messiah, joy/gladness). These are analytically interesting but cannot be traced further in the database. They represent connections to concepts outside the programme's current scope.

### 5.3 Unidirectional only

The absence of bidirectional linking means that querying "what is connected to registry X" requires searching both the source side (via file_id) and the target side (via linked_registry_id). No single query gives a complete picture without a UNION.

### 5.4 No link to wa_session_research_flags

The SD_POINTER flags in `wa_session_research_flags` (327 rows, growing) represent a newer, richer cross-registry signal system. The two tables are not connected — there is no FK or cross-reference between a cross_registry_link and an SD_POINTER flag. As Session B/D progresses, the SD_POINTER system will likely supersede this table's function.

---

## 6. Verdict

The table contains **legitimate Session A analytical work** with good note quality and clean FK integrity. However:

1. **Low coverage** — 14% of registries, all from early analysis
2. **connecting_term not joinable** — transliterated forms instead of Strong's numbers
3. **Unidirectional** — source-side observations only
4. **Being superseded** — the SD_POINTER / correlation system in Session B/D provides richer, bidirectional, and programmatically structured cross-registry signals

The 158 links are not wrong — the notes carry real analytical value. But the table's structural limitations mean it serves as a historical reference rather than an active analytical tool. The connecting_term format issue could be repaired, but the higher priority may be ensuring the SD_POINTER system captures equivalent (and richer) connections as Session B progresses.

---

## 7. Repair Options

| Option | Action | Consequence |
|--------|--------|-------------|
| **A. Repair connecting_term** | Script to resolve transliterations to Strong's numbers using mti_terms lookup | Makes the field joinable; ~70-80% automated resolution likely, remainder manual |
| **B. Keep as reference** | No changes; treat as historical Session A observations | Notes remain valuable; programmatic use stays limited |
| **C. Migrate to SD_POINTER** | Convert the 158 links into SD_POINTER flags in wa_session_research_flags | Consolidates cross-registry signals into one system; original links archived |

**Recommendation:** Option B for now. The SD_POINTER system is the strategic path forward. As Session B completes more registries, the 327 (and growing) SD_POINTERs will provide far richer cross-registry coverage than these 158 Session A links. Repair effort is better spent on Session B throughput.
