# wa-sessiona-prose-instruction-v1_0-20260427

Version: v1_0

> **Framework B — Soul Word Analysis Programme**
> **Session A — Phase 1 Prose Generation Instruction**
> Version: v1_0  ·  Date: 20260427  ·  Status: Active
> Supersedes: (new — first issue, replaces ad-hoc invocation)
> Governed by: wa-global-rules-all [current], wa-global-general-rules [current]
> Companion: wa-sessionb-analysis-readiness [current]

---

| **Document** | **Value** |
|---|---|
| Filename | wa-sessiona-prose-instruction-v1_0-20260427.md |
| Purpose | Specify the production, capture, and re-generation of Phase 1 (Session A) prose — the deterministic narrative rendered from DB state that is itself written back to the DB as `prose_section` rows under `source_stage='session_a'`. |
| Authoritative script | `scripts/generate_session_a_extract.py` |
| Authoritative output | 6 `prose_section` rows per registry, codes `sa_s1_d1` .. `sa_s1_d6` |
| Researcher trigger | A registry has reached `phase1_status=Complete` and `verse_context_status=Complete` and is being prepared for Session B Stage 1 readiness. |
| Claude Code role | Run the extract; review the `.md`; apply the PROSE patch; verify the DB rows; commit. |
| Claude AI role | (none — this is a deterministic mechanical render; no analytical judgement) |

---

## 1. What Phase 1 prose is

Phase 1 (Session A) prose is the **mechanical narrative summary** of a registry's data state, rendered deterministically from the database with no analytical judgement. It captures:

- Registry orientation (no, word, cluster, status fields, term/verse counts)
- Lexical foundation (parsed meaning, senses, stems, LSJ for Greek terms)
- Term inventory (OWNER + XREF terms with status, flags, root family, related words)
- Verse-context groupings (groups + dimensions + verse records)
- Pointers (existing SB findings, SD pointers, cross-registry links, phase2 flags)
- Catalogue questions in scope (universal + registry extensions)

This prose is the **input substrate** that the Analysis Readiness sweep then composes into the Stage 1 readiness `.md`+`.json` (the artefact AI reads at the start of Session B Stage 2).

The flow is:

```text
DB state  →  generate_session_a_extract  →  .md + PROSE patch
                                              ↓
                                          apply_session_patch  →  prose_section rows in DB
                                                                    ↓
                                                                Analysis Readiness sweep
                                                                    ↓
                                                              readiness .md + .json (AI input)
```

**Why capture to DB before the readiness sweep:** the readiness sweep reads `prose_section` rows by `source_stage='session_a'` to compose its registry-orientation, term-inventory, and lexical-foundation panels. If the rows are absent, those panels render thin or empty.

---

## 2. Authoritative script

**Use:** [`scripts/generate_session_a_extract.py`](../../scripts/generate_session_a_extract.py)

This is the **only** script that produces Phase 1 prose intended for DB capture. It writes:

- A markdown `.md` file (researcher-readable; six sections separated by `<!-- PROSE_SECTION ... -->` markers)
- A JSON PROSE patch (carries the same content as `prose_section` insert/replace operations)

**Do not use:** `scripts/build_session_a_prose.py`. That script serves a different purpose — it produces per-term `.md` files for **Verse Context** classification work (renders a single Strong's term's data for VC input). It does **not** write to the prose store and does not produce the 6-section sa_s1_d* extract.

If a future task genuinely requires the per-term VC-input rendering, use `build_session_a_prose.py --term=H1234`. For Phase 1 prose to DB, use `generate_session_a_extract.py`.

---

## 3. The 6 sections

Phase 1 prose for any registry comprises exactly six sections, mapped to `prose_section_type` rows seeded with `source_stage='session_a'`:

| section_type_id | code | chapter_no | label | Content |
|---:|---|---:|---|---|
| 1 | `sa_s1_d1` | 1 | Session A — Word Summary | Registry orientation: no, word, cluster, statuses, term/verse counts, dimension list |
| 2 | `sa_s1_d2` | 2 | Session A — Meaning | Parsed meaning, senses, stems, LSJ entries (Greek) |
| 3 | `sa_s1_d3` | 3 | Session A — Verses | Group-first verse rendering with dimensions, verse records |
| 4 | `sa_s1_d4` | 4 | Session A — Terms | OWNER + XREF inventory with MTI status, mti_term_flags, quality flags, root family, related words, verse counts |
| 5 | `sa_s1_d5` | 5 | Session A — Pointers | wa_session_b_findings, SD pointers (wa_session_research_flags), cross-registry links, phase2 flags |
| 6 | `sa_s1_d6` | 6 | Session A — Questions | Universal catalogue questions + registry-specific extensions in scope |

**The section type ids are stable.** Do not change them in a regenerate; the script targets them by `code`.

---

## 4. Patch envelope

The PROSE patch produced by the script must conform to the `apply_session_patch.py` contract:

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-SESSIONA-R{NNN}-V1",
    "patch_type": "PROSE",
    "produced_at": "{ISO-8601 UTC}",
    "registry_id": {NN},
    "session_b_status": null
  },
  "operations": [
    { "op_id": "SA-R{NNN}-SUMMARY",   "table": "prose_section", "operation": "insert",  "record": {...} },
    { "op_id": "SA-R{NNN}-MEANING",   "table": "prose_section", "operation": "insert",  "record": {...} },
    { "op_id": "SA-R{NNN}-VERSES",    "table": "prose_section", "operation": "insert",  "record": {...} },
    { "op_id": "SA-R{NNN}-TERMS",     "table": "prose_section", "operation": "insert",  "record": {...} },
    { "op_id": "SA-R{NNN}-POINTERS",  "table": "prose_section", "operation": "insert",  "record": {...} },
    { "op_id": "SA-R{NNN}-QUESTIONS", "table": "prose_section", "operation": "insert",  "record": {...} }
  ]
}
```

Key requirements (these were the gotchas that caused the 2026-04-27 scramble; the script now emits them correctly — but if you hand-edit a patch, preserve them):

1. **`_patch_meta` envelope** — top-level metadata MUST nest under `_patch_meta`. Flat top-level fields (`patch_id`, `patch_type` at root) are not read by the applicator and will fail validation with `"_patch_meta.session_b_status is required"` even though `PROSE` is exempt — because the exemption check itself reads from `_patch_meta`.
2. **`registry_id` not `registry_no`** — inside `_patch_meta`, the field is named `registry_id` (its value is the registry number, despite the misleading name; the applicator's `_validate()` looks up `word_registry.no = ?`).
3. **`session_b_status: null`** — required field. Phase 1 prose does not advance session_b_status; null is the correct value.
4. **`patch_type: "PROSE"`** — the applicator routes the patch to the prose handler on this type.
5. **`operations[].operation`** — `"insert"` for first generation; `"session_a_replace"` for re-generation against an existing `prose_section.id` (see §6).

---

## 5. Standard workflow — first generation

When a registry has no Phase 1 prose in the DB yet:

```bash
# 1. Generate the .md and the PROSE patch (no DB writes yet)
python scripts/generate_session_a_extract.py --registry=N

# 2. Inspect outputs
#    .md:    Sessions/Session_A/Data_Prose/wa-{NNN}-{word}-sessiona-{YYYYMMDD}.md
#    patch:  Sessions/Patches/wa-{NNN}-{word}-sessiona-patch-{YYYYMMDD}.json

# 3. Dry-run the patch to confirm validation passes
python scripts/apply_session_patch.py --dry-run "Sessions/Patches/wa-{NNN}-{word}-sessiona-patch-{YYYYMMDD}.json"

# 4. Apply live
python scripts/apply_session_patch.py "Sessions/Patches/wa-{NNN}-{word}-sessiona-patch-{YYYYMMDD}.json"

# 5. Verify the 6 rows landed
python -c "
import sqlite3
conn = sqlite3.connect('database/bible_research.db')
for r in conn.execute('''
  SELECT pst.code, ps.id, ps.version, ps.status, length(ps.body) as len
    FROM prose_section ps
    JOIN prose_section_type pst ON pst.id = ps.section_type_id
   WHERE ps.registry_id = (SELECT id FROM word_registry WHERE no = N)
     AND pst.source_stage = \"session_a\"
   ORDER BY pst.sort_order
'''): print(r)"

# 6. Refresh manifest
python scripts/build_file_manifest.py
```

**Or in one shot** (script does steps 1, then 4 via subprocess):

```bash
python scripts/generate_session_a_extract.py --registry=N --apply
```

The `--apply` mode produces the `.md`, writes the patch to `Sessions/Patches/`, and invokes `apply_session_patch.py` automatically. It is safe for first generation. The patch is auto-archived to `archive/patches/` on successful apply.

---

## 6. Re-generation (after DB state changes)

When DB state has changed since the prior Phase 1 prose was written (e.g. terms added, dimensions reviewed, mti_term flags changed) and the prose needs to be refreshed:

```bash
# Re-run the extract; the script auto-detects existing rows and emits
# session_a_replace operations targeting their ids.
python scripts/generate_session_a_extract.py --registry=N
```

The patch will use `operation: "session_a_replace"` for each existing row with the matching `id`. Apply it the same way as a first generation.

**Behaviour:**
- The replace operation updates `body`, `word_count`, `heading`, `metadata_json`, `source_file` on the existing row.
- It does **not** bump `version` or write a supersede chain row — Phase 1 prose is treated as a refresh-in-place (the data is deterministically derivable from DB; there is no analytical history to preserve).
- If you instead need a supersede with version-bump audit trail (rare for Phase 1), use the manual prose-supersede mechanism documented in `wa-sessionb-analysis-output [current]` §v2.7.

---

## 7. Output destinations (post-2026-04-27 restructure)

| Artefact | Destination | Naming pattern |
|---|---|---|
| Phase 1 prose `.md` | `Sessions/Session_A/Data_Prose/` | `wa-{NNN}-{word}-sessiona-{YYYYMMDD}.md` |
| PROSE patch JSON | `Sessions/Patches/` | `wa-{NNN}-{word}-sessiona-patch-{YYYYMMDD}.json` |
| Applied patch (after apply) | `archive/patches/` | (filename preserved; auto-archive by applicator) |
| DB rows | `prose_section` (registry_id, source_stage=session_a) | 6 rows per registry; codes sa_s1_d1..sa_s1_d6 |
| Pre-apply DB backup | `backups/` | `bible_research_backup_{YYYYMMDD}_{HHMMSS}_PATCH-{...}.db` |

The script's `--out-dir` argument default is `Sessions/Session_A/Data_Prose`. Override only for ad-hoc renderings (e.g. debugging, comparison) — never for the canonical capture flow.

---

## 8. Pre-conditions

Phase 1 prose is generated only when:

| Condition | DB check |
|---|---|
| Registry exists | `word_registry.no = ?` returns a row |
| Phase 1 audit complete | `word_registry.phase1_status = 'Complete'` |
| VC classification complete | `word_registry.verse_context_status = 'Complete'` |
| Engine audit clean | `word_registry.last_automation_run = 'AUDITED'` |
| Schema at v3.17.0+ | `schema_version` table reports 3.17.0 or later (M40-M43 applied) |

The script does not enforce these gates strictly — it will produce a render against partial state. The pre-conditions are operational discipline: don't generate Phase 1 prose for a registry that hasn't passed VC, because the verse_context-based sections (`sa_s1_d3 Verses`, `sa_s1_d6 Questions`) will mis-render or render with `In Progress` markers.

---

## 9. What goes in the .md (and what does not)

**In:** Everything the script can render deterministically from DB tables. The `.md` is a **machine-faithful snapshot** of the data state at the moment of generation.

**Not in:** Researcher-authored interpretive content. Specifically:

- `word_registry.inference_note` (researcher-authored synthesis hint) — rendered if present, but the script does not author it.
- `word_registry.word_synopsis` (researcher-authored short narrative) — rendered if present; null with explicit `_Word synopsis not yet authored_` placeholder otherwise.
- Any analytical reflection or judgement — Phase 1 prose is mechanical; reflection happens in Session B.

If the researcher wants to populate `inference_note` or `word_synopsis` for a registry, that is a **separate** action via a researcher-authored patch (not produced by `generate_session_a_extract.py`). After such a patch lands, re-run Phase 1 generation to capture the new content into the prose sections.

---

## 10. Failure protocol

| Failure | Cause | Remediation |
|---|---|---|
| `validation FAILED: _patch_meta.session_b_status is required` | Patch envelope missing `_patch_meta` nesting | Pre-2026-04-27 patches had this issue. Re-run the extract with the current `generate_session_a_extract.py`; or if hand-fixing, wrap top-level metadata in `_patch_meta`. |
| `apply_session_patch.py: error: the following arguments are required: patch_file` | `--apply` invocation used `--patch-file=PATH` | Pre-2026-04-27 invocation form. The current script uses positional argument. Re-pull the script. |
| `prose_section_type code 'sa_s1_dX' not found` | Section type seed missing | Confirm via `SELECT * FROM prose_section_type WHERE source_stage='session_a'` returns 6 rows with codes sa_s1_d1..sa_s1_d6. If absent, rerun the relevant migration (M21). |
| `Patch {patch_id} already applied (found in engine_run_log)` | Same patch applied twice | Idempotency check fired correctly. If you genuinely want to re-apply, regenerate to get a new `patch_id` (date is in the id). |
| `--apply` produces .md and patch but apply step skipped or fails silently | Subprocess error surfaced through stderr | Re-run apply manually with `python scripts/apply_session_patch.py <patch-file>`. |

---

## 11. Validation queries

After applying Phase 1 prose for a registry, verify with these SQL queries:

```sql
-- 1. All 6 sections present, current (not superseded), approved
SELECT pst.code, ps.id, ps.version, ps.status, ps.author, length(ps.body) AS body_len
  FROM prose_section ps
  JOIN prose_section_type pst ON pst.id = ps.section_type_id
 WHERE ps.registry_id = (SELECT id FROM word_registry WHERE no = ?)
   AND pst.source_stage = 'session_a'
   AND ps.superseded_by_id IS NULL
   AND (ps.delete_flagged = 0 OR ps.delete_flagged IS NULL)
 ORDER BY pst.sort_order;
-- Expect: 6 rows, status='approved', author='claude_code'.

-- 2. Patch logged in engine_run_log
SELECT run_id, started_at, ended_at, outcome
  FROM engine_run_log
 WHERE run_id = 'PATCH-{YYYYMMDD}-SESSIONA-R{NNN}-V1';

-- 3. Patch archived to archive/patches/
-- (filesystem check; not in DB)
```

---

## 12. Programme-wide application track (status as of 2026-04-27)

Phase 1 prose has been generated and captured to DB for the following registries:

| no | word | First generation | DB state |
|---:|---|---|---|
| 30 | contrition | 2026-04-27 (this instruction's first application) | 6 rows, ids 71–76 |
| 35 | covetousness | 2026-04-20 (pre-instruction; .md produced; patch may not have applied — verify) | (verify) |
| 62 | fellowship | 2026-04-20 (pre-instruction; .md + patch produced) | (verify) |
| 134 | renewal | 2026-04-20 (pre-instruction; .md produced) | (verify) |
| 206 | vulnerability | 2026-04-20 (pre-instruction; .md + patch produced) | (verify) |
| 207 | blindness_spiritual | 2026-04-20 (pre-instruction; .md produced) | (verify) |

Pre-instruction artefacts in `Sessions/Session_A/Data_Prose/` may not all have made it into the `prose_section` table. A one-off audit comparing the `.md` files in that folder to the DB rows by registry is recommended before relying on Phase 1 prose state for any of those five registries.

All future Phase 1 prose generations follow this instruction.

---

## 13. Companion: Analysis Readiness sweep

After Phase 1 prose lands in DB, the next step is the Analysis Readiness sweep. That is a separate operation governed by [wa-sessionb-analysis-readiness [current]](wa-sessionb-analysis-readiness-v1_7-20260427.md). The sweep reads:

- `prose_section` rows where `source_stage='session_a'` (Phase 1 prose; this instruction's output)
- `word_registry`, `wa_term_inventory`, `mti_terms` (registry/term state)
- `verse_context`, `verse_context_group`, `wa_dimension_index` (VC state)
- `wa_session_b_findings` open items, `wa_session_research_flags` SD pointers (open work)
- `wa_obs_question_catalogue` (questions in scope)

…and composes the Stage 1 readiness `.md`+`.json` for AI to read at the start of Session B Stage 2.

If the readiness sweep produces a thin or incomplete output, the first thing to check is whether Phase 1 prose has landed for the registry in question.

---

## Change Log

**v1_0 (2026-04-27):** First issue. Filed in response to the 2026-04-27 scramble around producing Phase 1 prose for registry 30 (contrition). Codifies the authoritative script, output destinations, patch envelope, workflow, failure modes, and validation queries. Identifies `build_session_a_prose.py` as a separate-purpose script (VC term-prose; not for Phase 1 to DB).

---

*wa-sessiona-prose-instruction-v1_0-20260427.md*
*Framework B — Soul Word Analysis Programme*
*Filed in Workflow/Instructions/ per the 2026-04-27 folder restructure.*
