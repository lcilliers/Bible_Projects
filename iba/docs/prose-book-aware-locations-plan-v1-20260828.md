# Prose book/cluster-aware output locations — plan (v1)

> Escalation #989. A plan for the researcher's decision, not a build — the researcher's own
> reaction to the discovery: *"you asking the question make me think that the prose location
> definition cannot be right."* Grounded in live data, not assumed.

## 1. What's actually there, confirmed live

`prose_section_type.book_label` (4 books) and `prose_section.cluster_code` (nullable, already
exists in the schema) together decide where a section's content conceptually belongs:

| Book | Rows | `cluster_code` populated | Folder that already exists |
|---|---|---|---|
| Programme | 51 | 0 (book has no cluster concept) | `Workflow/Programme/{programme_prose,prose-edits,...}` |
| Detail design | 45 (`prose_section`: 141 None + 28 `M01`) | Partially | **No folder exists at all** |
| Findings | 6 types (`prose_section`: 582 None + 1 `M06`) | **Almost none** | `_analytics/clusters/M##-Name/findings/`, `_analytics/findings_prose` |
| Essays | 1 (`prose_section`: 9 rows, all `M01`) | Fully, for what exists | `_analytics/clusters/M##-Name/essays/`, `_analytics/essay`, `_analytics/essay_prose` |

`cluster.cluster_code` + `cluster.short_name` (e.g. `M01`+`Fear`) is the live mapping to the
`M##-Name` folder segment the `_analytics/clusters/` tree already uses.

**The data itself isn't fully cluster-tagged yet** — most `Findings`/`Detail design` rows have
`cluster_code IS NULL` even though the live folder structure for `Findings`/`Essays` is per-cluster.
That's a separate, prior gap (content not yet attributed), not something this plan fixes — noted so
it isn't mistaken for a location-config problem once this ships.

## 2. What this means for `prosestore.py`

Today's single flat `output_dir(cfg)`/`docx_output_dir(cfg)`/`search_output_dir(cfg)`/
`patch_output_dir(cfg)` (escalation #971/#976, `BUILD.md` §195) works correctly for exactly one
book (`Programme`) and has no sensible answer for the other three — `Detail design` has nowhere to
go, `Findings`/`Essays` need a *cluster*, not just a book.

## 3. Proposed design

1. **A new resolver, `output_dir_for(cfg, book_label, cluster_code=None)`**, replacing the flat
   `output_dir(cfg)` as the real entry point (`output_dir(cfg)` stays as the `Programme`-only
   fallback default, same non-breaking pattern every other `filingkit`-adjacent change this round
   used):
   - `book_label == "Programme"` → `Workflow/Programme/programme_prose` (unchanged).
   - `book_label in ("Findings", "Essays")` → requires `cluster_code`; resolves via
     `cluster.short_name` to `_analytics/clusters/{cluster_code}-{short_name}/{findings|essays}`.
     Raises (not a silent fallback) if `cluster_code` is `None` — matches the data-gap in §1: a
     row with no cluster attribution has no correct folder to go to, and guessing one would be
     worse than refusing.
   - `book_label == "Detail design"` → **no live folder exists.** Needs the researcher's own call:
     create one now (where?), or leave `run_extract`/`run_export_chapter` refusing this book until
     a location is decided (same "refuse rather than guess" principle as the cluster case above).
2. **`cfg_prose.prose.output_dir` etc. become per-book/per-cluster-aware settings** rather than one
   flat value each — exact shape (a JSON map keyed by book, a `cfg_prose_location` table keyed by
   book+cluster, or something else) is itself an open question, not pre-decided here.
3. **`docx_output_dir`/`search_output_dir`/`patch_output_dir`** — same question applies to each;
   not necessarily the identical answer (a search-result file may reasonably stay flat even if the
   canonical extract output is book/cluster-scoped — not assumed here either way).

## 4. Open questions for the researcher

1. Does the design in §3 match what you meant by "already imbedded in the folders that exist
   today," or is the actual intended structure different from what's currently on disk (i.e., is
   the live `_analytics/clusters/.../findings` layout itself provisional/wrong too)?
2. `Detail design` — where should its output actually go? No folder exists yet to infer from.
3. Should `docx_output_dir`/`search_output_dir`/`patch_output_dir` follow the same book/cluster
   scoping as `output_dir`, or do any of them legitimately stay flat?
4. Config shape for the per-book/per-cluster mapping — a `cfg_prose` JSON value, a new small table,
   or something else?
5. Should the `cluster_code`-attribution gap (most `Findings`/`Detail design` rows currently have
   none) block this rollout, or ship the location logic now and let attribution catch up
   separately?

Approve scope (and answer 1–5), and this builds next round.
