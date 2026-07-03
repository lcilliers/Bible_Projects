# Psalms — inner-being readings (folder)

> **The DB is the corpus. These files are regenerable VIEWS, not a second source of truth.**
> Every document here is stored canonically in `database/bible_research.db` (`prose_section`) and reproduces from it **byte-for-byte** (verified 2026-07-03, 152/152). If a file and the DB ever disagree, the DB wins.

## What's here
- **`readings/`** — the 150 Phase-2 inner-being chapter-readings (`wa-psalmN-inner-being-reading-*.md`), one per psalm. Canonical home: `prose_section`, type `lexical_prose_chapter` (id 104), `metadata.phase = "2-chapter-reading"`, active version per chapter.
- **`phase1-views/`** — the Phase-1 lexical inspection views (`wa-psaN-phase1-lexical-view-*.md`). These are *dry-run inspection dumps* of the `ve_lexical` rows; regenerable by re-running the Phase-1 script for a chapter.

## The cross-cutting outputs (kept in `../_reports/`, also DB-canonical)
- **Synthesis (structured):** `wa-psalter-synthesis-per-characteristic-v1-20260703.md` → `prose_section` id **580** (type `lexical_synthesis_psalter`, id 105).
- **Synthesis (essay / story voice):** `wa-psalter-synthesis-essay-v1-20260703.md` → `prose_section` id **581** (type `lexical_synthesis_psalter_essay`, id 106). Shareable PDF: `outputs/pdf/The inner being of the Psalms - an essay.pdf`.
- **Harvest grid:** `wa-characteristic-harvest-20260703.md` — regenerable from `scripts/_harvest_characteristic_evidence_v1_20260703.py` (reads the DB).
- **Tracker / session-end** (`wa-psalms-chapter-readings-PROGRESS.md`, `wa-session-end-*`) — these are **governance/session logs**, *not* corpus and *not* reproducible from the DB; they are process records, deliberately not filed into `prose_section`.

## Reproduce / verify (reusable scripts)
```bash
# prove the DB reproduces every folder view byte-for-byte
python scripts/_export_prose_to_md_v1_20260703.py --verify

# regenerate all readings + syntheses from the DB
python scripts/_export_prose_to_md_v1_20260703.py --export --outdir verse-analysis/psalms/readings

# regenerate a Phase-1 view for one chapter (dry-run writes the view; no DB change)
python scripts/_apply_poetic_chapter_lexical_v1_20260702.py --book=Psa --chapter=N

# render any markdown to a shareable PDF
python scripts/_export_md_to_pdf_v1_20260703.py --in PATH.md --out PATH.pdf --title "..."
```

## What is "corpus" vs. "view" vs. "governance"
- **Corpus (DB-canonical, the source of truth):** the 150 readings + the two syntheses. All in `prose_section`.
- **Regenerable views (safe to delete/regenerate):** these `.md` files, the phase-1 views, the harvest grid, the PDF. Kept for browsing/sharing; the DB can rebuild them.
- **Governance (not corpus, not reproducible):** the tracker and session-end logs — session process records.
