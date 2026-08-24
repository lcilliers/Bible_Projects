> **Superseded by [prose-change-log-design-v7-20260824.md](prose-change-log-design-v7-20260824.md).**
> Kept on disk for history only.

# Prose change log design — versioning integrity (#836)

Supersedes: [prose-change-log-design-v5-20260824.md](prose-change-log-design-v5-20260824.md) (v1–v5
kept on disk for history). Researcher decisions this round (2026-08-24): §10 fully closed (Model A
accepted, change-date = date applied, not source-event date); body compression accepted; no
fine-grained before/after isolation needed; `change_reason` guidance given; and — the big structural
change — **a single shared `change_log` table, not the two separate per-table history tables v4 §13
proposed**, dictated directly with a starting field list. This round restates the decisions plainly,
then works out the one real gap the dictated field list leaves open (where the actual prior content
lives) and the semantic consequence of "version = the log's own id."

Status: **mostly settled** — a small number of direct questions remain, marked clearly below, not
assumed either way.

---

## 18. Decisions recorded, no longer open

| From v5/v4 | Researcher's answer (2026-08-24) | Effect |
|---|---|---|
| §10 Model A vs B | **Model A accepted.** | Closed. §11/§12's current-state column lists (drop `supersedes_id`/`superseded_by_id`, add `updated_at`, etc.) stand. |
| §16.1's one open check (system-time vs real-world-valid-time) | **"the change date is the date it is applied, not the date that the source event occurred."** | Closed — temporal-table/system-time semantics confirmed, not SCD2's real-world-valid-time. §10 has no remaining open question. |
| §16.2 compression | **Accepted** — "body storage (of the previous version) can be compressed." | `body` in the log is stored compressed. |
| Whether prior-version body must stay retrievable at all | **Yes — "very unlikely, but must remain possible."** | Confirms a full (compressed) snapshot is still needed per version, not a metadata-only log — reinforces that Option C from v2 §6 (metadata-only, no content) was never the right answer for `prose_section`. |
| Fine-grained before/after isolation within a change | **Not required** — "the exact before and after for the changed element does not have to be isolated." | No need to compute or store a structured, field-by-field diff. Directly simplifies v4 §13.2's "true delta, one typed column per field" design — see §20 below, that shape is no longer required. |
| `change_reason` values | **Source-dependent, given directly:** for a flag-driven change, `change_reason` = the flag type. In most other cases, the best value is the change's own source reference (whatever process/script/patch originated it). | Not a fixed closed vocabulary decided in advance — a population rule instead: default to the source reference; flag-driven changes use the flag type specifically. Recorded as the write-time rule for whatever process populates `change_log.change_reason`. |
| `source_file` | **Moves out of `prose_section` entirely** — "does source_file not move to the log file, no longer in prose_section table." | §11's column list is corrected: `source_file` is **dropped** from `prose_section`, not kept as "source of current version" as v4 had it. It lives only in the log now. |

---

## 19. The dictated shape — one shared `change_log` table

Direct instruction, quoted in full: *"§11 version = prose_change_log_id... The change_log table does
the following - single version number per change - could be applied across tables and rows;
change_datetime, change_source (file_name if driven from an input file), change_reason, status
(change proposed, change applied?)"*

Read plainly: **not** v4 §13's two separate, differently-shaped history tables
(`prose_section_history` full-snapshot / `prose_section_type_history` delta) — instead **one**
`change_log` table, generic enough to record a change against any target row in any covered table,
whose own row id **is** the "version" value written onto `prose_section.version` /
`prose_section_type.version`.

### 19.1 Fields as dictated

| Field | Meaning |
|---|---|
| `id` | The log row's own PK — **this is what gets written as `version` on the target row** |
| `change_datetime` | When the change was applied (system time, per §18) |
| `change_source` | File name, if driven from an input file — otherwise the originating process/script |
| `change_reason` | Per §18's population rule (flag type, or the source reference) |
| `status` | `change proposed` / `change applied` (open — see §19.3) |

### 19.2 One real gap the dictated list leaves open — where does the content live?

Nothing in the dictated field list names a place for the actual prior content — the compressed `body`
text a `prose_section` change needs (confirmed still required, §18), or whatever summary of what
changed a `prose_section_type` change needs (no longer required to be a field-by-field diff, §18, but
still needs to say *something* about what changed). Two ways to close this gap, not decided here:

- **(a) One shared `payload` column on `change_log` itself** — holds the compressed body for a
  `prose_section` change, or a loose text/JSON summary for a `prose_section_type` change. Keeps
  everything in the single table the instruction describes; the column is simply unused/NULL for
  whichever shape doesn't apply to a given row.
- **(b) A separate, narrower payload table**, FK'd to `change_log.id` — keeps the (potentially large,
  compressed-blob) content out of what may become a frequently-scanned, cross-table log table, at the
  cost of no longer being the one single table the instruction describes literally.

**Proposed: (a).** It matches the instruction's own framing ("the change_log table does the
following") more literally, and nothing about scale argues against it — the compressed blob for
`prose_section` sits in exactly one place either way; a separate table would only help if `change_log`
itself needed to stay lean for fast scanning independent of payload size, which hasn't been named as a
requirement. Flagging this as **my addition, not dictated** — the instruction's own field list didn't
name it, so this is the one point in this round genuinely asking for confirmation rather than
restating a decision already given.

Two further fields carried forward from v4, not contradicted by anything in this round, proposed as
also needed:

- **`changed_by`** — who/what executed the change (may differ from `author` — e.g. Claude Code
  applying a researcher-approved fix). Confirmed as a distinct, correct concept by the AI-authorship
  research (v5 §16.3); nothing in this round removes the need for it.
- **`target_table` / `target_id`** — required for "could be applied across tables and rows" to
  actually work: the log needs to say *which* row of *which* table each entry describes. Implied by
  the instruction's own framing, not stated as separate fields, so naming them explicitly here rather
  than assuming the phrasing alone covers it.
- **`batch_id`** (v4 §13.1, not mentioned this round either way) — still proposed, to answer §2 item
  3/§0c's "did these changes happen together" question. Not dictated, not contradicted — flagged as
  still open rather than assumed carried over.

### 19.3 `status` — likely needs a third value

Two values given (`change proposed`, `change applied`) map directly onto the flag-fix workflow
already designed at #829 §12.4/#835 (search → propose fix → researcher approval → apply) — a
`change_log` row in `proposed` status would naturally **be** that proposed-fix artifact, which is a
good sign this design connects cleanly to work already planned elsewhere, not a coincidence worth
losing. One gap worth naming: a workflow with a `proposed` state generally also needs a way to record
a proposal that was **not** applied — rejected, or superseded by a different fix — otherwise a
declined proposal has nowhere to go but staying `proposed` forever. Not assuming a third value should
exist; asking directly whether `status` needs one (e.g. `rejected` or `withdrawn`) or whether that
case is out of scope for this table.

### 19.4 The consequence of "version = the log's own id" — stated plainly, not silently accepted

Because `change_log` is shared **across every row of every covered table** (not one log per section),
its `id` is a single, globally increasing sequence across all of them. Setting
`prose_section.version = change_log.id` directly (rather than mirroring a small, per-item counter, as
v2 §8's "Option A" had proposed) means:

- `version` stops meaning "this is the Nth time this particular row changed" — a section's version
  numbers will jump unpredictably (e.g. 118 → 4502 → 4503) depending on how many other rows across
  the whole log changed in between, not count up 1, 2, 3 the way it does today and the way every
  prior document in this thread (including the researcher's own framing of "version 3") has assumed.
- "How many times has this row changed" becomes a **derived** fact (count the `change_log` rows for
  that `target_table`/`target_id`), not something readable directly off the row's own `version` value.
- What's gained in exchange: `version` becomes a direct, literal foreign key to the exact log entry
  describing the row's last change — no join predicate beyond `change_log.id = version` needed, and no
  risk of the two-mirrored-numbers drift that produced today's mixed-type legacy data (§1) in the
  first place.

This is exactly the tradeoff named as "Option B" back in v2 §8, now made concrete by the shared-table
design. Not a problem — just a real, worth-stating-plainly semantic shift from what "version" meant in
every version of this document up to v5. Confirming this consequence is intended (the instruction
("§11 version = prose_change_log_id") reads as a clear, deliberate choice, not an oversight) rather
than assuming silently.

---

## 20. §13 (v4) — superseded by this round

v4 §13's two separate, differently-internally-shaped history tables (`prose_section_history` full
snapshot, `prose_section_type_history` typed delta) are **superseded** by §19's single `change_log`
table. The reasoning that justified two different *internal shapes* (one dominant body field vs. many
independent structural fields) still explains *why the payload differs by target table* — but that
now lives inside one table's flexible `payload` field (§19.2), not as two structurally different
tables.

---

## 21. Direct questions

1. **§19.2** — confirm (or correct) the `payload`-column-on-`change_log` approach for where prior
   content lives, since the dictated field list didn't name a place for it.
2. **§19.3** — does `status` need a third value for a declined/withdrawn proposal, or is that
   out of scope here?
3. **§19.4** — confirm the version-numbering consequence (no longer a small per-item counter; becomes
   a direct pointer to the log) is the intended tradeoff.
4. **Scope** — is `change_log` meant to cover only the two prose tables (`prose_section`,
   `prose_section_type`), or is "could be applied across tables and rows" pointing at a genuinely
   project-wide, reusable mechanism (in which case a non-`prose_`-prefixed name may fit better — not
   renaming anything without asking)?

---

## 22. Still open (carried, unchanged)

- `batch_id` — proposed, not yet confirmed (§19.2).
- Diff-based storage for `payload` — named as a future option (v5 §16.2), not scheduled.
- Migration of the 91 existing superseded rows and mixed-type legacy `version` values (v4 §14) — a
  build-phase task, still not designed.
