"""Update Registry Management Guide with new fields, queries, and terminology."""
import os

GUIDE_PATH = os.path.join(
    os.path.dirname(__file__), "..",
    "data", "imports", "WA", "Workflow", "Frameword_B", "Session_B",
    "WA-Registry-Management-Guide-v5.2-20260327.docx"
)

with open(GUIDE_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add new fields to Section 2
old_anchor = "| anchor_verses | Key verses identified as particularly significant for this word. |"
new_anchor = """| anchor_verses | Key verses identified as particularly significant for this word. |
| cluster_assignment | Cluster this word belongs to. Format: C01, C02, etc. See Section 5. |
| sb_classification | Inner being standing classification from Session B analysis: confirmed_characteristic / plausible / uncertain / instrumental / relational_only |
| sb_classification_reasoning | Reasoning for non-confirmed classifications. NULL for confirmed. |
| carry_forward | Whether this word carries forward to Session D: 1 (yes) / 0 (no). Default 1. |
| unique_term_count | Number of terms unique to this registry (not shared with any other word). Engine-derived. |
| shared_term_count | Number of terms that also appear in other registries. Engine-derived. |
| term_sharing_ratio | Proportion of shared terms: 0.0 (all unique) to 1.0 (all shared). Engine-derived. |"""
content = content.replace(old_anchor, new_anchor)

# 2. Add Section 6.6 — Term Sharing Query
old_6_5 = """## **6.5 Cluster Progress**

| SELECT cluster_assignment, COUNT(*) as total, SUM(CASE WHEN session_b_status = 'Session B Complete' THEN 1 ELSE 0 END) as complete FROM word_registry GROUP BY cluster_assignment;  Returns: cluster completion status. Requires cluster field — see WA-Implementation-Instruction-v5. |
| --- |"""
new_6_5 = """## **6.5 Cluster Progress**

| SELECT cluster_assignment, COUNT(*) as total, SUM(CASE WHEN session_b_status = 'Session B Complete' THEN 1 ELSE 0 END) as complete FROM word_registry GROUP BY cluster_assignment;  Returns: cluster completion status. Requires cluster field — see WA-Implementation-Instruction-v5. |
| --- |

## **6.6 Term Sharing — Not-Shared Words**

Words with term_sharing_ratio = 0 have no cross-registry term overlap. These words can be analysed independently — their term inventories and verse sets do not intersect with any other registry. This makes them the simplest candidates for Session B analysis.

| SELECT no, word, cluster_assignment, unique_term_count, phase1_term_count, phase1_verse_count, session_b_status FROM word_registry WHERE term_sharing_ratio = 0.0 AND phase1_status != 'Excluded' AND phase1_term_count > 0 ORDER BY no;  Returns: registries with no shared terms — can be analysed without cross-registry considerations. |
| --- |

## **6.7 Term Sharing — Ownership Distribution**

The term_owner_type field on wa_term_inventory marks whether each term record is the primary owner (OWNER) or a cross-reference copy (XREF). XREF verse records are delete_flagged and excluded from standard queries and exports.

| SELECT term_owner_type, COUNT(*) as terms FROM wa_term_inventory WHERE delete_flagged = 0 GROUP BY term_owner_type;  Returns: owner vs cross-reference term distribution. |
| --- |"""
content = content.replace(old_6_5, new_6_5)

# 3. Add to Section 8 — Terminology
old_term_patch = """| Patch | A JSON file of database operations submitted to Claude Code for application to bible_research.db. |"""
new_term_patch = """| Patch | A JSON file of database operations submitted to Claude Code for application to bible_research.db. |
| Term sharing ratio | Proportion of a registry's terms that also appear in other registries. 0.0 = all unique, 1.0 = all shared. Engine-derived from wa_term_inventory cross-file analysis. |
| Not-shared word | A registry where term_sharing_ratio = 0.0 — all terms are unique to this word. Can be analysed independently without cross-registry verse overlap. |
| Owner term | A term_inventory record where term_owner_type = OWNER — the primary location for this Strong's number. |
| Cross-reference term | A term_inventory record where term_owner_type = XREF — a copy of a term that belongs primarily to another registry. XREF verse records are delete_flagged. |"""
content = content.replace(old_term_patch, new_term_patch)

# 4. Update change control
old_change = """**Change control — v7**"""
new_change = """**Change control — v8**
Section 2 (Registry Fields): Added cluster_assignment, sb_classification, sb_classification_reasoning, carry_forward, unique_term_count, shared_term_count, term_sharing_ratio. Section 6.6 and 6.7 added: term sharing queries for not-shared words and ownership distribution. Section 8 (Terminology): Added term sharing ratio, not-shared word, owner term, cross-reference term. wa_term_inventory.term_owner_type column documented. XREF verse records are delete_flagged.

**Change control — v7**"""
content = content.replace(old_change, new_change)

# Also update the header version
content = content.replace(
    "Version 7  |  March 2026  |  Reference guide",
    "Version 8  |  March 2026  |  Reference guide"
)
content = content.replace(
    "WA-Registry-Management-Guide-v7-20260327.docx",
    "WA-Registry-Management-Guide-v8-20260328.docx"
)
content = content.replace(
    "WA-Registry-Management-Guide-v6-20260327.docx",
    "WA-Registry-Management-Guide-v7-20260327.docx"
)

with open(GUIDE_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Registry Management Guide updated to v8.")
