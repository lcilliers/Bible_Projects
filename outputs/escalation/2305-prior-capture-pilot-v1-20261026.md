# #2305 Pilot: the two documents of design v2 section 7 (v1)

**Date:** 2026-10-26 · **Escalation:** #2305 · **Design:** `outputs/escalation/2305-prior-work-capture-design-v2-20261026.md`
· **Tool:** `iba/app/ps/Prior-Capture.ps1` (Prepare, Record, Report) · **Where:** a backup-API copy of iba.db with the
migration applied. **Nothing was written to the live database.** Fills by Claude (Sonnet 5.5) in this chat session,
from reading each document, no API. Test results: `outputs/escalation/2305-prior-capture-test-v1-20261026.md` (47 of 47).

## 1. What was captured

| | M18 group D reading | Fear ledger unit 2 |
|---|---|---|
| Document | `_analytics/Clusters/M18 - desire-longing/m18-group-D-reading-v1-20261009.md` | `_analytics/Clusters/M01 - fear-awe/fear-observation-ledger-unit2-v1-20261001.md` |
| Lines naming a verse, all answered | 28 | 185 |
| captured / already recorded / not an observation (answer rows) | 34 / 0 / 5 | 111 / 29 / 45 |
| New observations | 29 (14 face, 10 statement, 3 link, 1 use, 1 silence) | 35 (18 face, 6 statement, 4 link, 3 party, 2 term, 1 use, 1 unfitted) |
| Nodes | 119: 88 on a word, 31 verse only; 82 carry a subgroup; 6 words with no single occurrence | 290: 214 on a word, 76 verse only; 211 carry a subgroup; 3 words with no single occurrence; 9 trace another observation |

- **Fear ledger, the parts October took:** the 28 ids with a live observation naming the file, plus FE-64
  (observation 11776), are answered `already recorded` and unchanged. Captured: FE-50, FE-56, FE-63, FE-67, FE-70,
  FE-72, FE-78, FE-79, FE-80, FE-81 (with its parties line), the faces table (A to T, 18 faces), the
  change-of-character rows with verses (four, each a link traced to the findings it compares), and the
  surface-alignment note (tag `unfitted`).
- **Examples against the design:** FE-50 (example a) is one observation with nodes on Job 23:15 *terrified* (H0926,
  M24), *consider* (H0995, M15), *dread* (H6342, M01), Job 23:16 *heart* (H3820A, M47) and the other quoted words, each
  with its subgroup and disposition `told`. The M18 face "Consumes the one who has it" (example c) has nodes on Psa 69:9
  *zeal* (H7068, M18, characteristic) and *reproach* (H2778A, M53). The run report and the filled JSON of each
  document are in `outputs/escalation/2305-pilot-files/`.
- **What the run reports list:** one `unfitted` observation (the note that STEP sets a surface on the neighbouring
  English word, lines 40 to 43); one flag in each document; the words with no single occurrence (the same surface
  twice in a verse); no reference to no single verse; one quotation not found in the ESV text, a gloss label,
  "to dread" (captured as written).

## 2. What the pilot found

1. **FE-64 was missing from Prepare's October list.** Observation 11776 (`fear:FE-64`, held to OT-108.26) has a
   `revisit_note` that does not name the file, so Prepare did not list it, and Record refused my first fill on it.
   Fixed (self-correctable, no new decision): Prepare now also lists live ids of the same prefix as
   `october_same_prefix`, kept apart from the document's own. Test T1b2.
2. **My first node helper limited nodes to the document's cluster,** against the design's "every word the quotation
   names". Fixed in the fill: every M-coded word of the verse that the finding's text names is a node, with its own
   cluster. T-coded words (*For*, *on*, *me*, *consumed*) are not noded: a convention of this fill, put as D3 below.
3. **The reading index holds false references** that the run lists but does not hide: in the M18 document the bare
   citations on the quote-check line were indexed as Mark 3:7 and Mark 1:15 and 1:16 (the document itself says they
   name Philippians and Galatians). The line is answered `weave or quote-check record`. The index is #2228's.
4. **Pace is not measured.** The design asks for tokens and time per document. A chat session does not report its
   token use per document, and the time was not recorded, so no pace figure is given. What is known: the two
   documents are 213 of the 19,034 lines, filled by hand in this session.

## 3. Decisions for the researcher (each blocks something, none is taken)

| # | Question | Options | Recommended |
|---|---|---|---|
| D1 | The document's own disposition **RS** (reshapes existing text) and **NS** (new structure needed): Q4 maps W to `told`, held to `held`, data to `data` and says nothing of RS or NS. The pilot wrote RS as `told` with the document's wording in `disposition_note` | a) RS and NS as `told`, wording in the note; b) RS and NS left empty, wording in the note | a: they are woven; the note keeps the distinction |
| D2 | `ib_node.cluster_code` cannot be empty. A node on a verse alone (no placeable word) takes the document's cluster, as October did. **Ten documents have no cluster**, so a verse-only node, or a node on a word in no M or T cluster, cannot be written for them | a) those ten are captured last, and only findings with a placeable M or T word; b) a rule for which cluster a clusterless document's verse-only node takes; c) a column change so a node may have no cluster | a: it needs no schema change, and the ten are last in the order (design 5) |
| D3 | Which words a node names: the pilot fill nodes every **M-coded** word the finding's text names and no T-coded word | a) M-coded only; b) M- and T-coded | a: T-coded words are function and grammar words; a T word that is itself the characteristic is the T-a case (RA-01) |

## 4. Not done

- The migration is **not applied to the live database**, and no live capture was run (design 7: results are shown
  before the live run). The live steps, on approval: a pre-run snapshot, the migration, then document by document.
- BUILD.md, USER-GUIDE.md section 7.2 and the PS worksheet tab are written; `Config-Maintenance.ps1 -Step Validate`
  on the live database waits for the live migration.
