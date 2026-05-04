# R067 Goodness — Session B Artefact Bundle

**Consolidated:** 2026-05-01

**Folder layout:**

- `inputs/` — registry data package, validation report, analytic status, readiness outputs (Stage 2 prerequisites)
- `obslog/` — comprehensive obslog `.md` and session log `.md` (AI's Stage 2a/2b/2c output)
- `capture/` — parse manifests, parsed-capture-preview, validation records (CC's Phase 2 writer output)
- `chapters/` — six assembled chapter files + combined extract (mechanically assembled from DB)
- `prior/` — older artefacts from earlier pipeline iterations (kept as historical record)

**Capture model:** see `capture/` for the parser version applied. Chapters were assembled by `scripts/_tmp_assemble_chapters_full.py` reading from `database/bible_research.db` (schema v3.17.0) on 2026-05-01.
