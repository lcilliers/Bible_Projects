# Report Definition — PASSAGE_OBSERVATION (working / review document)

- **Type:** living definition spec · Version 2 · 2026-06-30 (renamed from Verse_observation; reframed per architecture register §8)
- **Report class:** per-passage **snapshot** → versioned `-vN`, bump-on-change
- **Generator:** `scripts/_assess_passage_observations.py` (**to build**)
- **Output path:** `verse-analysis/{Book}/wa-{book}-{chap}-{verse}-observations-vN-YYYYMMDD.md` (anchor verse)
- **Sample:** [SAMPLE-passage-observation-exo-001-013.md](samples/SAMPLE-passage-observation-exo-001-013.md)
- **Source of truth:** the DB only; **index-driven (no full-text scans)**; never hand-edited.

---

## 1. Purpose
The digested, **index-driven** picture for a passage, and the **working document the researcher comments on**. It collates **all observations by characteristic** for the passage, **plus all DB evidence** (findings, lexical, logos, chat) for **every verse in the passage** — pulled by key from `verse_evidence_index` / `verse_term_index`, never by scanning text.

## 2. Unit & input
- Unit = the **passage** (the `wa_verse_records` group label, DEC-1). Verses in the passage carrying observations/evidence.
- Input: `--ref` / `--group`.

## 3. Sections
1. **Observations — by characteristic** — *source `ib_observation`* keyed by passage verses, grouped by **characteristic** (DEC-4): id, dimension, status, anchor, full narrative.
2. **Corpus evidence for the passage** — *source `verse_evidence_index`*: per verse, the `finding_verse`, `lexical` (ve_lexical), and (when built) **logos** / **ai-chat** evidence. Shows coverage honestly (e.g. 0 findings) rather than implying it.
3. **Logos / AI-chat portions** — *source: external-extract portion-index* (DEC-5): captured-in-full docs live in the secured folder; **portions** indexed to these verses surface here **by key, never by scanning the docs**. «PENDING build».
4. **Review comments** — the round-trip surface (§4).

## 4. Review-comment round-trip (DEC-6)
The report is the comment surface. Each comment is dispositioned:
- **About a verse or characteristic** → becomes an **observation or finding** in the DB (then re-renders as a captured row).
- **About process or workflow** → filed to the appropriate `Workflow/` folder.
No separate comment table; comments resolve into existing stores.

## 5. Versioning & filing
- Per-passage snapshot → **versioned `-vN`, bump-on-change** (same hash rule as Fanout).

## 6. Constraints
- **Index/key lookups only — no full-text scans** (researcher requirement; the volume will grow).
- Shows only captured/indexed content; does not infer beyond stored narratives.
- Read-only generation; content changes via the DB, then regenerate.

## 7. Build status & prerequisites
- **Generator to build.** Prerequisites (register §9): characteristic mapping (DEC-4); external-extract store + portion-index (DEC-5). Findings + lexical can ship first; logos/chat second.

---

## Provenance — researcher comments that shaped this spec (verbatim)
This report must be based on indexes and keys, not full text scans. Verse observations (better named **passage observations**): the verse/passage consists of various related IB concepts — each forming its own characteristic — each with its own observations. This report includes all observations by track for the passage **as well as all findings, logos, chats etc in the DB for all verses in the passage**. This requires all current findings, logos extracts, chats etc to be scanned and indexed for verses and keywords. The report becomes the working document for review comments, which trigger DB updates; responses are captured as DB entries or written back to the report.
