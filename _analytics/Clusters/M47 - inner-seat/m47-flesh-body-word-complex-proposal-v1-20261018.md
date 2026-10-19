# Flesh and body as one word complex: proposal (#2163, for #2162)

v1, 2026-10-18. For approval. Nothing has been written.

Researcher, chat 2026-10-18 (verbatim): *"the body words should be clustered in with the flesh
cluster, and be part of the flesh word complex. the word-registry has a range of associated terms
associated with a word."*

## 1. Where the codes stand now (iba.db, read live)

Registry word **150 `flesh`** (`raw-complete`) holds G4561, H1320, H1321, H7607 (M47) and G4559
(M28). Each has a full concordance in `strong_verse`, equal to its span verses.

| Code | Gloss | Origin | Word now | Cluster now | strong_verse | Span verses |
|---|---|---|---|---|---|---|
| G4983 *sōma* | body | backfill | none | T14 | 0 | 122 |
| H1472 *gᵉwiyyāh* | body | word | deadness | T2 | 11 | 11 |
| H1655 *gᵉšēm* (Aram.) | body | backfill | none | T2 | 0 | 5 |
| G4984 *sōmatikos* | bodily | backfill | none | T2 | 0 | 2 |
| G4954 *sussōmos* | of the same body | word | the afflicted | T2 | 1 | 1 |
| H0990J *beṭen* | belly: body | backfill | none | T14 | 0 | 9 |
| H1480 *gûpāh* | body | backfill | none | T2 | 0 | 1 |
| H6106I *ʿeṣem* | bone: body | backfill | none | T2 | 0 | 2 |
| G4560 *sarkinos* | fleshly | backfill | none | M28 | 0 | 2 |

The backfill codes have meaning only. Their verses are in iba.db only because other words pulled
them, so nothing guarantees their full verse set.

## 2. Proposed change (the established route: #1880, BUILD.md §93–§97)

1. **Word links.** Add `word_strong` rows linking word 150 `flesh` to the eight body codes. Also add
   G4560 *sarkinos* ("fleshly"), whose sibling adjective G4559 is already under `flesh`. Existing
   links (H1472 to `deadness`, G4954 to `the afflicted`) are kept, so those two become cross-links.
2. **Cluster.** Re-code the eight body codes to **M47**: the T2/T14 rows are soft-deleted and M47
   rows inserted. G4560 keeps M28, as G4559 does.
3. **How it is written.** A one-off migration
   `iba/app/migration/apply_flesh_body_complex_2163_v1_20261018.py`. It uses the `migration` writer
   (granted for both tables), soft-deletes and inserts, takes source
   `researcher-ruling-2163-20261018`, is idempotent, and runs as a dry run first. The DB is
   backed up before the live run.
4. **Promotion (the STEP pull).** `lib.strongreconcile.reconcile()` for each code. For a backfill
   code now under M47 with a word link, it fetches the full concordance through
   `raw.verses_one` (writer `call3_strong`: `strong_verse` + `verse` + `span`), sets
   `origin='word'`, and builds `verse_lexical` for the verses fetched. The way it is run is
   point 6.
5. **After.** Run `VerseLexical.ps1 -Step lexical.build` over the touched chapters (the role
   refresh, as in #1880), then `Spine-Check.ps1`, then
   `WordRegistrySpan-Report.ps1` for `flesh`. Restate overview §2 and §6 from the result (v2) and
   remove the "#2138 route" line.

## 3. Points for you

- **P1. Two codes will not promote.** `reconcile` refuses a backfill code whose sibling variant is
  word-origin or already clustered (the sibling-conflict rule):
  - **H0990J** *beṭen* "belly: body": siblings H0990G (T14), H0990H (T14), H0990I (T2).
  - **H6106I** *ʿeṣem* "bone: body": sibling H6106G "bone" belongs to the word `strength` (T14).

  They will be linked and clustered, but their verses stay incidental (9 and 2) and
  `cluster.validate` will list them. Proposed: accept that, and read their verses with batch 4.
- **P2. G4560 *sarkinos*.** Include it with `flesh` (proposed), or leave it out?
- **P3. Corpse codes** (G4430, G2966, H5038, H6297, H4658). These are not included: your ruling
  holds them as data unless a verse speaks of the person. Confirm that they stay out of the complex.
- **P4. Running `reconcile`.** `Cluster-Assign.ps1 -Step Assign` is a DB-wide sweep. Proposed:
  run `Cluster-Assign.ps1 -Step Validate` first (read-only) to see whether the sweep would touch
  anything else. If it would, the migration calls `reconcile()` for the nine codes only, through
  the same handler context.
- **Rule 70 (#1970, no re-tagging).** This re-code is by your own instruction, so it is recorded
  as your ruling, not raised by Claude.
