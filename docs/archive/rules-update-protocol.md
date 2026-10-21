# Rules Update Protocol — 2026-04-20

**Purpose:** How to update the DB-canonical global rules post-M33 (rules live in `wa_rule_registry` + `wa_addendum_registry`).

Pre-M33, you edited `wa-global-general-rules-v2_11-20260418.json` directly. Post-M33, the JSON file is audit-trail only; the DB is canonical. Updates flow through the patch system.

---

## 1. Three ways to initiate a rules change

### 1.1 Conversational (simplest — most common)

Tell CC in chat: *"Update rule GR-FILE-003 — add point X to the rule text. Mark rule GR-OLD-001 obsolete with reason Y. Add a new rule GR-NEW-001 in category 'process_discipline' saying Z."*

CC will:

1. Draft a `RULES` patch with the appropriate `insert` / `update` / `deprecate` operations
2. Show it for your approval before applying
3. Apply with per-patch backup
4. Regenerate the rules extract so the updated vocabulary is visible immediately

This works for one-off changes or small batches.

### 1.2 Markdown round-trip (for larger/bulk revisions)

Open the current rules extract MD: `Workflow/reference/wa-global-rules-extract-{YYYYMMDD}.md`. Mark up changes directly in the markdown — CC diffs and produces a patch. Pattern matches the prose store round-trip idea — use HTML comments to mark the operation:

```markdown
<!-- RULE_UPDATE rule_id: GR-FILE-003 fields: rule_text -->
{revised rule text...}

<!-- RULE_DEPRECATE rule_id: GR-OLD-001 reason: "replaced by GR-FILE-003 v3_0" superseded_by: GR-FILE-003 -->

<!-- RULE_INSERT category: process_discipline -->
rule_id: GR-NEW-001
subject: "New rule title"
rule_text: "Full rule text..."
applies_to: "all sessions"
version: "1.0"
```

Then hand the marked-up MD back. (Round-trip importer not yet built; conversational path 1.1 covers the need for now.)

### 1.3 Direct file edit + CC re-seed (avoid this)

Don't edit the source JSON (`wa-global-general-rules-v2_11-20260418.json`) directly — the DB will drift. The JSON is audit-trail, not canonical.

---

## 2. Operation types supported (post applicator extension)

`scripts/apply_session_patch.py` handles:

| Operation | Table | Purpose |
|---|---|---|
| `insert` | `wa_rule_registry` | New rule |
| `update` | `wa_rule_registry` | Revise fields (match by `rule_id`) |
| `deprecate` | `wa_rule_registry` | Mark obsolete + record superseded_by |
| `insert` | `wa_addendum_registry` | New addendum |
| `update` | `wa_addendum_registry` | Revise fields (match by `item_id`) |

`RULES` patch type registered in `wa_patch_type_registry` with `session_b_status_exempt = 1`.

---

## 3. Worked example — three updates in one patch

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-20260421-RULES-V1",
    "patch_type": "RULES",
    "produced_by": "claude_code",
    "produced_at": "2026-04-21T09:00:00Z",
    "motivation": "Add GR-NEW-001; revise GR-FILE-003; deprecate GR-OLD-001",
    "session_b_status": null
  },
  "operations": [
    {
      "op_id": "OP-001",
      "table": "wa_rule_registry",
      "operation": "insert",
      "record": {
        "rule_id": "GR-NEW-001",
        "category": "process_discipline",
        "subject": "New rule — short title",
        "rule_text": "Full rule text here...",
        "applies_to": "all sessions",
        "version": "1.0",
        "added_date": "20260421",
        "source_document": "PATCH-20260421-RULES-V1"
      }
    },
    {
      "op_id": "OP-002",
      "table": "wa_rule_registry",
      "operation": "update",
      "match": { "rule_id": "GR-FILE-003" },
      "set": {
        "rule_text": "Revised rule text...",
        "version": "3.1"
      }
    },
    {
      "op_id": "OP-003",
      "table": "wa_rule_registry",
      "operation": "deprecate",
      "match": { "rule_id": "GR-OLD-001" },
      "record": {
        "obsolete_reason": "Replaced by GR-NEW-001",
        "superseded_by": "GR-NEW-001"
      }
    }
  ]
}
```

Apply with:

```bash
python scripts/apply_session_patch.py Sessions/Patches/wa-rules-update-20260421.json
```

After apply, regenerate the rules extract:

```bash
python scripts/build_rules_extract.py --also-markdown
```

AI sessions starting after the regeneration see the updated vocabulary.

---

## 4. Automatic safety net

- **Per-patch backup** — applicator creates a DB snapshot before apply.
- **`last_modified` stamped** automatically on every `update` / `deprecate`.
- **Immutable fields** — `id`, `rule_id`, `created_at` protected from rewrite.
- **Column filter** — unknown columns silently dropped with `[NOTE]`, preventing schema drift from breaking the apply.
- **Extracts exclude obsolete by default** — retired rules are invisible to session-start loads unless `--include-obsolete` is explicit.

---

## 5. Rule-text multi-line content

The `rule_text` field often spans paragraphs (see e.g. GR-LOAD-001). Use JSON string escapes for newlines (`\n`) — or produce the patch file by hand with the rule text on a single line using `\n` separators, and CC normalises at apply time.

---

## 6. Protocol at a glance

| I want to ... | You say ... | CC does ... |
|---|---|---|
| Add a new rule | "Add a new rule GR-X in category Y saying Z" | Drafts INSERT op; shows it; applies on approval |
| Revise a rule | "Update rule GR-X — change field F to value V" | Drafts UPDATE op; shows the diff; applies on approval |
| Retire a rule | "Mark GR-X obsolete" (optional: "superseded by GR-Y") | Drafts DEPRECATE op; applies |
| Bulk revision | Mark up the current MD extract; hand it back | CC parses; produces one multi-op patch; applies |
| Revert a change | "Roll back the last rules patch" | Restores from per-patch backup |

---

*End of protocol.*
