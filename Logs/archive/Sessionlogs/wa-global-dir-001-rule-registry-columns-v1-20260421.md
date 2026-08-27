# Directive — Schema Change: wa_rule_registry Four-Field Restructure Support

**Filename:** wa-global-dir-001-rule-registry-columns-v1-20260421.md
**Date produced:** 2026-04-21
**Reference to prior output:** wa-global-rules-review-obslog-v1_0-20260421.md §34.1, §35.
**Governed by:** wa-global-general-rules [current] GR-PROG-005 (two-AI division); wa-directive-instruction [current].

---

## 1. DIRECTIVE ID

`DIR-20260421-001`

## 2. MOTIVATION

The researcher has adopted Option B (Pattern 1 field split) from the rules-clarity review on 2026-04-21, recorded in obslog §24 and §30. Rules in `wa_rule_registry` will carry their binding text in the existing `rule_text` column, with supporting commentary in three new nullable TEXT columns: `rationale`, `application_notes`, and `examples`.

The restructure gives the programme:
- A concise binding statement in `rule_text` — clear for session-start compliance.
- Separable commentary — rationale (why), application notes (how/edge cases), examples (illustrations).
- Independent auditability — a clarification to rationale can be made without disturbing `rule_text`.
- Consistent structure across all rules — same four fields for every rule, populated or NULL.

The RULES patch that rewrites the rule content assumes these columns exist. This directive prepares the schema before the patch is applied.

## 3. SCOPE

**Table affected:** `wa_rule_registry` only.

**Tables NOT affected:** `wa_addendum_registry`, `wa_patch_type_registry`, `wa_rule_history` (if present), `wa_vocab_set`, `wa_vocab_member`, or any other table.

**Rows affected:** zero. This is a structural change only — no data rows are read, updated, inserted, or deleted. New columns arrive populated as NULL on all existing 59 rows (36 active + 23 obsolete).

**Indexes, constraints, triggers:** none added by this directive.

## 4. OUTCOME REQUIRED

After execution, `wa_rule_registry` has three additional columns:

| Column name | Data type | Nullable | Default |
|---|---|---|---|
| `rationale` | TEXT | Yes | NULL |
| `application_notes` | TEXT | Yes | NULL |
| `examples` | TEXT | Yes | NULL |

All other columns remain exactly as they are in schema v3.14.0 (see database-schema-v3_14_0-20260421.json `/tables/wa_rule_registry`). The existing columns listed below must still be present with their current types and constraints — including the existing singular `example` column, which is **preserved as-is** (see §7 held item):

`id`, `rule_id` (UNIQUE NOT NULL), `category` (NOT NULL), `subject`, `rule_text` (NOT NULL), `example`, `applies_to`, `version`, `added_date`, `last_modified`, `obsolete` (NOT NULL DEFAULT 0), `obsolete_reason`, `superseded_by`, `addendum_ref`, `source_document`, `created_at` (NOT NULL).

Row count must remain 59 after execution.

## 5. EXECUTION APPROACH

CC determines the correct SQLite DDL. The natural pattern is three `ALTER TABLE ... ADD COLUMN ... TEXT` statements executed in a transaction with a pre-change backup.

CC is free to use a different execution path if it produces the same outcome (e.g. a CREATE-copy-RENAME sequence), provided the row count, existing column structure, and all data are preserved.

Per GR-PROC-004, CC presents the proposed DDL (or equivalent plan) for researcher approval before executing.

## 6. COMPLETION CONFIRMATION

CC returns to the researcher the output of:

```sql
PRAGMA table_info(wa_rule_registry);
```

The output must show:
- All 16 existing columns with their original types and constraints (unchanged).
- Three new columns at the end of the column list (or wherever the DDL places them): `rationale` (TEXT, notnull=0, dflt=NULL), `application_notes` (TEXT, notnull=0, dflt=NULL), `examples` (TEXT, notnull=0, dflt=NULL).

CC also returns:

```sql
SELECT COUNT(*) FROM wa_rule_registry;
```

Expected result: `59` (same as pre-change).

And:

```sql
SELECT rule_id, rationale, application_notes, examples
FROM wa_rule_registry
WHERE rule_id = 'GR-LOAD-001';
```

Expected result: one row returned with `rationale`, `application_notes`, and `examples` all NULL (confirms columns exist and default to NULL on pre-existing rows).

Claude AI reviews these three confirmations against this directive before the operation is considered complete.

## 7. HELD ITEMS — RESEARCHER DECISION BEFORE EXECUTION

The following question is held for the researcher and should be resolved before CC executes this directive:

**Naming collision — existing `example` (singular) vs proposed `examples` (plural).**

The `wa_rule_registry` table already has a column named `example` (singular). The v2_2 patch instruction §13.4.1 shows `example` as an optional field on insert. This directive proposes adding `examples` (plural) alongside it.

Three options:
- **(a) Keep both columns.** `example` retains its current role (single illustration, currently NULL across the rule set). `examples` carries the plural/block-form illustrations added in the restructure. Simpler for this pass; leaves a minor ambiguity in future authoring.
- **(b) Rename `example` → `examples` as part of this directive.** Single plural column going forward. SQLite supports `ALTER TABLE ... RENAME COLUMN ...` since v3.25 — CC would need to confirm the DB's SQLite version. The v2_2 worked example §13.4.1 would need a follow-up patch to the instruction document to reflect the rename.
- **(c) Drop `example` and add `examples`.** Clean but destructive if any rule's `example` field is populated. A pre-check of `SELECT rule_id, example FROM wa_rule_registry WHERE example IS NOT NULL` shows whether dropping is safe.

**Recommendation placeholder — per GR-HF-001 this is direction/principle (researcher's call).**

This directive as currently written proceeds on **option (a) — keep both columns**. If the researcher selects (b) or (c), the directive is redrafted before CC executes.

## 8. REFERENCES

- Schema snapshot: `database-schema-v3_14_0-20260421.json` `/tables/wa_rule_registry`
- Patch instruction: `wa-patch-instruction [current]` §3 (patch format), §13 (rules-update workflow), §13.4.2 (update on wa_rule_registry)
- Directive instruction: `wa-directive-instruction [current]`
- Global rules: `wa-global-general-rules [current]` — GR-PROG-005, GR-PROC-004
- Decision trail: obslog §24 (Option B adoption), §30 (decisions #1/#2), §34 (schema findings)

---

*End of directive.*
