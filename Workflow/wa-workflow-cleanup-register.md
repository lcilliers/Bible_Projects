# Workflow folder cleanup — disposition register

> **Living document · Doc version: 1 · Last updated: 2026-06-04.**
> **Purpose:** go through every `Workflow/` subfolder and reduce each to **only the final
> authoritative version(s)**, archiving the rest (move → `archive/`, never delete; manifest-indexed,
> fully recoverable). One row per file. CC executes the **CLEAR** archives; **DECISION** rows are held
> for the researcher's markup (mark `keep` / `archive` / `relocate→…` in the Decision column).
> Reversible by design — `git log --follow` + the archive subfolders preserve everything.

**Disposition key:** `KEEP` = stays as authoritative · `ARCHIVE` = moved to the folder's `archive/`
(superseded/historical) · `DECISION` = needs your call before I move it.

---

## Workflow/Tiers/  — DONE (clear archives) · 3 decisions held

**Context:** the catalogue ground truth is the database (`wa_obs_question_catalogue`). The fresh
DB extract is therefore the single authoritative catalogue; every prior markdown/JSON render of the
catalogue, plus the tier-debate logs and tier-definition drafts, are superseded or historical.

### Kept (authoritative)
| File | Why |
|---|---|
| `wa-tier-questions-extract-v1-20260604.md` | **The** authoritative catalogue — 189 tier questions pulled live from the DB (schema 3.28.0). |

### Archived (CLEAR — moved to `Tiers/archive/`)
| File | Why superseded |
|---|---|
| `wa-obs-catalogue-tiered-v2_1-20260513.md` | Prior tiered-catalogue render (schema 3.21.0) — superseded by the 2026-06-04 DB extract. |
| `wa-obs-question-catalogue-extract-20260419.md` | Pre-tier full extract (194 Q, deleted=0) — superseded. |
| `wa-obs-catalogue-generic-v1-20260426.json` | Pre-tier generic source JSON (147 Q) — superseded by the tiered DB catalogue. *(the file you had open)* |
| `wa-obs-catalogue-with-links-20260416.json` | Old catalogue-with-links JSON — superseded. |
| `WA-obs-catalogue-tier-classification-v1-2026-04-28.md` | First-pass tier classification, working doc — superseded by the live `tier`/`component` columns in the DB. |
| `WA-obs-framework-first-tier-v1_1-2026-04-29.md` | Precursor to the consolidated framework-definitions. |
| `WA-obs-framework-second-tier-prelim-v1-2026-04-29.md` | Preliminary, superseded. |
| `WA-obslog-t1-second-tier-prelim-v1-2026-04-28.md` | Prelim obslog. |
| `WA-tier-T1-definition-v1-2026-04-29.md` | Single-tier draft — folded into framework-definitions. |
| `WA-tier-T2-draft-v1-2026-04-29.md` | Single-tier draft — folded into framework-definitions. |
| `WA-session-log-tier-framework-debate-v1-2026-04-28.md` | Tier-debate session log (process history). |
| `WA-session-log-tier-debate-session2-v1-2026-04-29.md` | Tier-debate session log. |
| `WA-session-log-tier-debate-session3-v1-2026-04-29.md` | Tier-debate session log. |
| `WA-session-log-tier-debate-final-v1-2026-04-29.md` | Tier-debate session log (final). |
| `WA-prose-suggested-edits-v2-2026-04-29.md` | Not a catalogue — prose edit suggestions, applied/spent. |

### Decisions held (NOT yet moved)
| File | Question | Decision |
|---|---|---|
| `WA-tier-framework-definitions-v1_2-2026-04-29.md` | This is the current **prose definition of all 8 tiers** (title/scope/boundaries). You're rewriting tier definitions in §c of `wa-study-foundations.md` right now, which will supersede it. Archive it now, or **keep until §c is finalised** so you can consult it while writing? | _______ |
| `wa-tpopb-findings-catalogue-extract-20260416.json` | **Not a tier doc** — it's a findings-catalogue extract that happens to live here. Archive, or relocate to `research/investigations/`? | _______ |
| `wa-tpopc-btarget-flags-extract-20260416.json` | **Not a tier doc** — B-target flags extract. Archive, or relocate to `research/investigations/`? | _______ |

---

## Remaining Workflow subfolders — to process

Processed one at a time; each gets a section above as it is done.

- [ ] `Instructions/`  (the `[current]` governing docs — keep highest version, archive prior)
- [ ] `Global_rules/`
- [ ] `Clusters/`
- [ ] `Sciences/`
- [ ] `Programme/`
- [ ] `methodology/`
- [ ] `reference/`
- [ ] `registry/`
- [ ] `schema/`
- [ ] `Sessionlogs/`  (logs are historical — lighter touch; archive only if explicitly superseded)

---

## Working notes
- _2026-06-04:_ Register created. Tiers/ clear-archives executed; 3 decisions held for researcher markup.
