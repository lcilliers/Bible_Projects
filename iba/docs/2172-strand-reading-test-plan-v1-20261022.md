# #2172 reading process: test plan and run (v1, 2026-10-22)

> Escalations #2172 and #2219 (open items, section 4). `cfg_behaviour_rule` 46 test-plan-per-module-utility. Covers
> `iba/app/lib/narrativeregister.py` (block tellings, EditSection, rewrite, publish),
> `iba/app/lib/strandreading.py` and `iba/app/handlers/strandreading.py` (the eight steps), the
> close gate in `iba/app/lib/escalation.py`, and the schema migration. Runners (temporary):
> `iba/app/tools/temp_2172_register_test_run.py`, `temp_2172_rewrite_test_run.py`,
> `temp_2172_strand_test_run.py`, `temp_2172_map_handler_test_run.py`, `temp_2219_strand_items_test_run.py`, each run as
> `python iba/app/tools/<runner> <scratch folder>`. They work on a `dbsnapshot.copy_db` copy of
> iba.db whose settings point the chapter folder, the register files and the strand reports at the
> scratch folder; live iba.db and live files are never written. The word family in the strand test
> is real (G0022, 4 hits); every reading in its JSON files is made up.
>
> **Run 2026-10-22, with the #2219 migration applied to each copy before it went live: 106 of 106
> pass** (sections 1 to 4). The #2172 migrations, run on copies before they went live: 432 passage
> tellings to 378 block tellings, the same 260 claims in the narrative, a second run writing
> nothing, no unregistered table, column or trigger. The #2219 migration on a copy: 29 cfg writes,
> a second run writing nothing.

## 1. The register on blocks (temp_2172_register_test_run.py: 23 of 23)

| case | expected | result |
|---|---|---|
| Check after the migration | no file differs, no double or dead telling (the 46 claims no block tells are the pre-existing ones) | Pass |
| a heading that repeats ("The words", Ch 10.1) | refused, naming the parents | Pass |
| "Anxiety > The words" | the right block | Pass |
| an unknown heading | refused | Pass |
| Tell on a block | telling, one change row with the block's text, in_narrative 1 | Pass (3 cases) |
| Tell twice; in part with no part | refused | Pass (2 cases) |
| Untell; Untell what is not told | removed; refused | Pass (2 cases) |
| EditSection rename | tellings follow, heading line follows, not logged as a move, claims stay in the narrative, chapter published from the database | Pass (6 cases) |
| EditSection add a block; an unknown block without -Level | added and published; refused | Pass (2 cases) |
| Find (chapter and section; told in more than one), History, Export | run on the block tellings | Pass (4 cases) |

## 2. Rewrite (temp_2172_rewrite_test_run.py: 20 of 20)

| case | expected | result |
|---|---|---|
| R1 a block rewritten keeping its claims, a reference added | update written; chapter v+1 published, the old file in archive/; the file reads as the database renders it; one 'telling changed' row per claim with before and after; the citation added; Check finds no difference | Pass (6 cases) |
| R2 a told claim dropped, not accounted | refused, nothing written | Pass |
| R3 accounted 'withdrawn', the claim not withdrawn | refused, nothing written | Pass |
| R4 accounted 'moved' to a block that does not tell it | refused, nothing written | Pass |
| R5 'moved' to a block that tells it in the same rewrite | both chapters published | Pass |
| R6 a quotation not in the ESV text | refused, nothing written | Pass |
| R7 a block not opening with its heading; R8 a second heading inside | refused, nothing written | Pass (2 cases) |
| R9 the same update twice | refused | Pass |
| R10 a new block after a named block | placed after it and its sub-blocks | Pass (2 cases) |
| R11 a block retired with a claim not accounted | refused | Pass |
| R12 a block retired, its claim kept elsewhere | out of the narrative, no current telling | Pass (2 cases) |
| final Check | no file differs, no double or dead telling | Pass |

## 3. The reading process (temp_2172_strand_test_run.py: 40 of 40; temp_2172_map_handler_test_run.py: 1 of 1)

| step | case | expected | result |
|---|---|---|---|
| Define | no title/cluster/escalation; a code not in verse_lexical; a new strand; a word added twice | refused; refused; created; not doubled | Pass (4) |
| Context (handler) | first run; report; second run; no -By | one hit per live occurrence; report written; no hit added; refused | Pass (4) |
| Record | face and reason both; a hit not the strand's; a verse where the strong does not occur; no basis; a quotation not in the text | refused, nothing written | Pass (5) |
| Record | an observation and two hits | row with its parts (stage, tag, basis, run), grounded in ib_node, hits faced/reasoned and linked, verses analysed | Pass (5) |
| Record | supersedes | the earlier row withdrawn | Pass |
| Account / gate | gaps open | 2 unread hits, 1 undisposed observation counted; close refused naming the strand | Pass (2) |
| Gather | related blocks | 3 blocks, 1 claim told nowhere | Pass |
| Map | a related block left out; a statement with no claim/new claim/item | refused, nothing written | Pass (2) |
| Map | every block mapped | new claim added and told in its block; held statements raised as `chapter` open items on the strand's thread | Pass (3) |
| Map (handler) | held statements mapped again | the same open items reused; no comment on the strand's escalation | Pass |
| Derive | an observation not the strand's; a new claim with no source; held on an item that does not exist | refused, nothing written | Pass (3) |
| Derive | new claim on the observation, disposed 'claim'; a claim withdrawn | observation source added, status resolved; withdrawn | Pass (3) |
| Rewrite | a block rewritten with a withdrawn claim accounted | update names the strand and its escalation; cited verses citated | Pass (3) |
| Record, gate, Account | the remaining hits read, the matched open items answered | close allowed; account shows no gated gap | Pass (3) |
| Check | after the whole strand | no file differs, no double or dead telling | Pass |

## 4. Open items in the reading (#2219; temp_2219_strand_items_test_run.py: 22 of 22)

Design: `outputs/escalation/2219-open-item-handling-in-strand-reading-v1-20261022.md` section 3,
option A. A test thread with six items (a base Strong's code unpadded, a chapter holding a hit, the
strand's code, a cluster the word sits in, and two that should not match) is raised on the copy.

| Area | Case | Expected | Result |
|---|---|---|---|
| Match | a T cluster item (T3); an M cluster item (M64) | both found (the cluster pattern takes T codes) | Pass (2) |
| Context | matching | base code G22 to G0022, the chapter, the strand code, the word's other cluster; not G9999, not Gen 1:1 | Pass |
| Context | a second run; the report | nothing recorded again; items listed, each "not yet" | Pass (2) |
| Gate | items unanswered, one with a note dated before matching | every matched item listed, the earlier note not counted; close refused naming open items | Pass (2) |
| Answer | one `touched` response; then every item answered | that item only answered; no item gap, the gate names only the unread hits | Pass (3) |
| Record | an item not kind:value; a good item with a bad hit | refused, nothing written, no thread raised | Pass (2) |
| Record | a new item; the same item again | raised on the strand's own thread, linked 'raised'; reused, not doubled | Pass (2) |
| Record | an observation with `stable_key` and `note` (#2172 catch-up) | both kept on the row | Pass |
| Gate | raised items | not gated | Pass |
| Derive | held with both item and new_item; held on a new_item | refused; item raised, observation `open`, note names the item | Pass (2) |
| Raise | a settled item found again; the strand's thread completed | reopened on the same thread; the next item opens a new thread | Pass (2) |
| Account | the report | items listed with source and answer; console counts the gated gaps | Pass (2) |

## 5. Not covered

- `Strand-Reading.ps1` itself (the PS wrapper) cannot be run against a copy: `run.py` has no
  database override, so the handlers were called in-process with a `Ctx` on the copy. The wrapper
  was run live only with calls that are refused before any write (2026-10-22): `-Step Account
  -Strand no-such-strand` (RUN-20261022_094257_440-STRANDREAD, "strand 'no-such-strand' does not
  exist") and `-Step Context` without `-By` (RUN-20261022_094308_190-STRANDREAD, "-By ... is
  required"), both routed `report-continue` by `cfg_on_fail`.
- A real reading of a strand: study work, waiting for the study to re-open.
