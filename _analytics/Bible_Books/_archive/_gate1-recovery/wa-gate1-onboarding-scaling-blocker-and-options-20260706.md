# Gate-1 onboarding — scaling blocker (existing registries) + options

> Discovered while preparing the batch after the successful `salvation` pilot. **The pilot path (audit_word) does not cleanly extend to the 45 orphans that map to EXISTING populated registries.** This document states the finding (from the engine code) and the options. Date: 2026-07-06. No DB writes.

## The finding — audit_word is a whole-registry re-audit, not a surgical term-add

For an existing registry, `audit_word` (`engine/audit_word.py`):
1. **Loads ALL the registry's files** into the snapshot (lines 1624–1637) — the whole existing term set is in scope.
2. **DB_ONLY_TERM stream** (line 599): any active term in the DB **not in the extract's `terms` array** (include list) is **delete-flagged** — *unless* it has verses or analytical signals (protected, line 615). Measured at-risk (active, verse-free) existing terms: **terror 25, agony 24, wisdom 21, corruption 1** — a partial extract would delete-flag these.
3. **RESTORE stream** (line 937): terms delete-flagged in the DB but present in the extract's include list are **un-delete-flagged**.
4. **A7/A8** re-parse meaning and **full-reset** quality flags across all files' terms.

So the two obvious ways both break:
- **Partial extract (orphan only):** delete-flags existing thin terms (#2). ✗
- **Registry's original input extract + orphan:** the originals are **March 2026 snapshots** (`research/discovery/NNN_word_step_data_20260328.json`). Re-auditing from March would **revert 2+ months of term-level curation** — restoring terms deleted since, delete-flagging terms added since (#2/#3). ✗

The `salvation` pilot was clean only because it was a **brand-new empty registry** — no existing terms to disturb. The incremental sync tool (`_extract_word_terms.py`) is **archived/retired**.

## Scope of the problem
Of the 93 remaining orphans: **~45 map to existing populated registries** (Group C existing + Group B), **8 are Group A** (mti-reconcile only — no onboarding needed), and any assigned to genuinely-new registries could use the clean pilot path. The blocker is specifically the **adds to populated registries**.

## Options

**A — Surgical additive routine (recommended).** A small, engine-faithful helper that onboards ONE orphan into an existing registry: create `mti_terms` (owned), `wa_term_inventory` (OWNER), pull all occurrences via STEP, insert `wa_verse_records` (fully scaffolded), parse meaning — scoped to the orphan, **never touching existing terms** (no DB_ONLY_TERM/A8 sweep). Produces the identical established structure the pilot did, just scoped. Pro: existing registries untouched; same 100%-scaffolded result. Con: new tooling (must be validated against the integrity gate like the pilot).

**B — Own registry per orphan (pilot path as-is).** Each orphan (or small orphan-group) becomes its own new REGISTER, onboarded via the proven pilot path. Pro: zero new tooling; fully validated. Con: fragments the registry model (e.g. "discipline" split from "wisdom"); 45+ tiny registries.

**C — Full current re-audit per registry.** Regenerate a CURRENT full input extract per registry (from current DB state or a fresh STEP pull of current anchors) + the orphan, then re-audit. Pro: uses audit_word as-designed. Con: refreshes/churns every existing registry; STEP re-expansion may drift the term set; heaviest; needs a DB→input-extract converter.

## Recommendation
**Option A.** It preserves the "religiously maintained standard" (existing registries are not re-audited or disturbed), yields the same fully-scaffolded first-class terms as the pilot, and stays behind the same integrity snapshot/compare gate. I would build it, validate it on one existing registry (e.g. `corruption` / H0444, 1 term) end-to-end, confirm zero collateral against the integrity gate, then batch the rest. Group A (8) is a separate light mti-reconcile; genuinely-new registries (if any beyond salvation) use the pilot path.

*Filed 2026-07-06. Awaiting a steer on A / B / C before proceeding.*
