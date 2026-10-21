"""Update WA-Reference-v5.1 to v5.2 with new columns from housekeeping."""
import os

PATH = os.path.join(
    os.path.dirname(__file__), "..",
    "data", "imports", "WA", "Workflow", "Framework_B", "Session_B",
    "WA-Reference-v5.1-20260328.md"
)

with open(PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update version header
content = content.replace(
    "Version 5.1 | March 2026 | Schema v3.7.0",
    "Version 5.2 | March 2026 | Schema v3.7.0"
)
content = content.replace(
    "WA-Reference-v5.1-20260328.docx",
    "WA-Reference-v5.2-20260329.docx"
)
content = content.replace(
    "Supersedes | WA-Reference-v5-20260327.docx",
    "Supersedes | WA-Reference-v5.1-20260328.docx"
)

# 2. Add change control for v5.2
old_cc = "**Change Control Note — v5.1**"
new_cc = """**Change Control Note — v5.2**

| **Change** | **Detail** |
| --- | --- |
| Section 13.1 | word_registry: added unique_term_count, shared_term_count, term_sharing_ratio |
| Section 13.3 | wa_term_inventory: added term_owner_type (OWNER/XREF) |
| Section 13.6 | wa_verse_records: added mti_term_id (direct FK to mti_terms), target_word, span_strong_match |
| Section 13.11 | New: wa_quality_flag_types — CONCRETE_PHYSICAL flag documented |
| Section 15 | New: Term ownership and housekeeping reference |

**Change Control Note — v5.1**"""
content = content.replace(old_cc, new_cc)

# 3. Update Section 13.1 — word_registry
old_wr = "| id (PK) \u2502 no \u2502 word \u2502 source_list \u2502 category_hint \u2502 phase1_status \u2502 phase1_term_count \u2502 phase1_verse_count \u2502 session_b_status \u2502 origin \u2502 dimensions (formerly source_category \u2014 see Section 4.3) \u2502 notes \u2502 anchor_verses \u2502 cluster_assignment \u2502 sb_classification \u2502 sb_classification_reasoning \u2502 carry_forward |"
new_wr = "| id (PK) \u2502 no \u2502 word \u2502 source_list \u2502 category_hint \u2502 phase1_status \u2502 phase1_term_count \u2502 phase1_verse_count \u2502 session_b_status \u2502 origin \u2502 dimensions (formerly source_category \u2014 see Section 4.3) \u2502 notes \u2502 anchor_verses \u2502 cluster_assignment \u2502 sb_classification \u2502 sb_classification_reasoning \u2502 carry_forward \u2502 unique_term_count (new v5.2) \u2502 shared_term_count (new v5.2) \u2502 term_sharing_ratio (new v5.2) |"
content = content.replace(old_wr, new_wr)

# 4. Update Section 13.3 — wa_term_inventory
old_ti = "| id (PK) \u2502 file_id \u2502 language \u2502 term_id \u2502 strongs_number \u2502 transliteration \u2502 step_search_gloss \u2502 word_analysis_gloss \u2502 occurrence_count \u2502 testament \u2502 delete_flagged \u2502 status_note \u2502 evidential_status (new v3.7.0) \u2502 retention_note (new v3.7.0) |"
new_ti = "| id (PK) \u2502 file_id \u2502 language \u2502 term_id \u2502 strongs_number \u2502 transliteration \u2502 step_search_gloss \u2502 word_analysis_gloss \u2502 occurrence_count \u2502 testament \u2502 delete_flagged \u2502 status_note \u2502 evidential_status (new v3.7.0) \u2502 retention_note (new v3.7.0) \u2502 term_owner_type (new v5.2) |"
content = content.replace(old_ti, new_ti)

# 5. Update Section 13.6 — wa_verse_records
old_vr = "| id (PK) \u2502 file_id \u2502 term_inv_id \u2502 reference \u2502 verse_text \u2502 testament \u2502 translation \u2502 book_id \u2502 chapter \u2502 verse_num \u2502 delete_flagged |"
new_vr = "| id (PK) \u2502 file_id \u2502 term_inv_id \u2502 reference \u2502 verse_text \u2502 testament \u2502 translation \u2502 book_id \u2502 chapter \u2502 verse_num \u2502 delete_flagged \u2502 target_word \u2502 span_strong_match \u2502 mti_term_id (new v5.2) |"
content = content.replace(old_vr, new_vr)

# 6. Update schema source reference
content = content.replace(
    "Source: database_schema_20260328.json",
    "Source: database_schema_20260329.json"
)

# 7. Add Section 15 — Term Ownership and Housekeeping
# Insert before the final line
final_marker = "WA-Reference-v5.1 | 20260328"
section_15 = """# **15. Term Ownership and Housekeeping**

## **15.1 term_owner_type**

Each record in `wa_term_inventory` is classified as OWNER or XREF:

| **Value** | **Meaning** |
| --- | --- |
| OWNER | This registry is the canonical home for this Strong's number. Verses are active. |
| XREF | Cross-reference copy — term belongs primarily to another registry. Verses are delete_flagged. |

XREF term records remain active (delete_flagged = 0) for cross-registry linkage queries. Their verse records are delete_flagged to prevent duplicate counting.

## **15.2 Term Sharing Fields on word_registry**

| **Field** | **Meaning** |
| --- | --- |
| unique_term_count | Number of OWNER terms whose Strong's number appears only in this registry |
| shared_term_count | Number of OWNER terms whose Strong's number also appears in other registries |
| term_sharing_ratio | shared_term_count / (unique + shared). 0.0 = all unique. 1.0 = all shared. |

A word with term_sharing_ratio = 0.0 can be analysed independently — no cross-registry verse overlap.

## **15.3 mti_term_id on wa_verse_records**

Direct FK from verse record to mti_terms.id. Provides one-hop path from verse to master term index without joining through wa_term_inventory.

## **15.4 CONCRETE_PHYSICAL Quality Flag**

Terms flagged as CONCRETE_PHYSICAL denote concrete physical objects (sand, hand, stork). They are flagged but NOT excluded — verse analysis may reveal inner-being usage in context. Filter with:

| SELECT term_id FROM wa_data_quality_flags dqf JOIN wa_quality_flag_types qft ON qft.id = dqf.flag_id WHERE qft.flag_code = 'CONCRETE_PHYSICAL' |
| --- |

## **15.5 Housekeeping Rules (delete_flagged)**

Records with delete_flagged = 1 are excluded from all standard queries and exports. They include:

- Particle terms (ki, asher, al, im, etc.) across all registries
- Terms where mti_status = delete (synced from mti_terms)
- Verse records under delete_flagged terms
- XREF verse records (duplicate verses belonging to non-owner registries)

No physical deletion occurs. All flagged records remain in the database.

---

"""

content = content.replace(final_marker, section_15 + "WA-Reference-v5.2 | 20260329")
content = content.replace(
    "| 20260328 | Schema v3.7.0 | Supersedes WA-Reference-v5-20260327.docx",
    "| 20260329 | Schema v3.7.0 | Supersedes WA-Reference-v5.1-20260328.docx"
)

with open(PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("WA-Reference updated to v5.2")
