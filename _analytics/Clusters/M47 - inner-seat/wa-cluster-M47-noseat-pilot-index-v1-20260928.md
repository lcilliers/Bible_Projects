# M47 — the no-seat pilot: index and method as applied (v1)

**Date:** 2026-09-28 · **Author:** Claude Code · **Status:** pilot done (M02, M20), awaiting researcher review before scale-up. Nothing has been written to the DB.
**Picks up from:** `M47-handoff-batches-C-to-H-v12-20260928.md` (NEXT STEP) and `wa-cluster-M47-noseat-decisions-v1-20260928.md`.

## 1. The pilot readings (one per cluster, in that cluster's own folder)

| Cluster | Verses | With seat (M47 set) | No seat | Observations file |
|---|---|---|---|---|
| M20 Doubt & Discouragement | 275 | 30 | 245 | `../M20 - doubt-discouragement/wa-cluster-M20-noseat-observations-v1-20260928.md` (+ `…-noseat-verses-v1-….csv`) |
| M02 Anger & Wrath | 681 | 66 | 615 | `../M02 - anger-wrath/wa-cluster-M02-noseat-observations-v1-20260928.md` (+ `…-noseat-verses-v1-….csv`) |

The "with seat" counts match the M47 pairs CSV v2 exactly: 30/30 and 66/66 verses, with nothing found in only one of the two.

## 2. Researcher rulings applied (chat, 2026-09-28)

- **Intent.** Work through each cluster's verses that are **not** in the M47 cross-cluster CSV, and determine why the verse does not mention a seat: is the seat implicit, or is there another observation to be made? *(The body-seat list, C2 in the decisions file, was set aside as not relevant.)*
- **Pilots:** M02 and M20. **T-codes** can help show a verse's significance, but they are not the primary driver.
- **Cross-correlation (D).** It is built on the M47 work already done: "if you read a verse, where another verse for the same strong established a seat, then the seat correlation is implicit". bible_research.db plays no part (governance: it is prose-only).
- **Output (E).** Each cluster gets its own md with observations for the Strong's without any seat.
- **The inner-being definition (B)** is taken from config, not invented:
  - `cfg_prose_concept.inner_being_definition` → prose section 5, "Defining Inner Being": *non-physical, internal states, capacities, and expressions … how a person thinks, feels, chooses, relates, and orients*, plus the non-physical test
  - prose sections 1089 and 1090 ("inner being" / "non-inner being") and `cfg_method_rule` `hib.set` non-human-scope: **the subject is the human inner being**
  - `cfg_method_rule` `phenomenon.set` hidden-behind-act: an inner state may sit behind a stated act
- **Data is read directly from `iba.db`** (`verse_lexical.role`, `verse`, `strong`). No CSVs were prepared by the researcher.

## 3. Method as applied, with one refinement to flag

1. **Seat** = a token whose `verse_lexical.role` carries M47. **No-seat verses** for cluster X = verses with an X token and no M47 token.
2. For each X Strong's: count its no-seat verses, its **seated** verses corpus-wide (the verses where it stands beside an M47 token), and all its verses.
3. **Refinement, needing your confirmation:**
   - A "seated elsewhere" link counts **only where that verse's M47 word is used in an inner-being sense and belongs to the relevant party.**
   - Examples that fail: *ruach* = the day's wind (Gen 3:8, the only seat link of *chava* "hide"); *basar* = meat (Exo 16:8, the only link of *lun* "grumble"); the divine Spirit speaking (Rev 2:17, the only link of *kruptō*); a heart belonging to another person (2Ch 22:9).
   - Without this check, three M20 Strong's would count as "implicit" on links that establish no seat. The same failure also occurs in M02 (wind, meat, hunger), but it strips no M02 Strong's of its implicit status.
   - This is consistent with ruling 1: keep all the senses, but a sense counts as a seat only where it touches the inner being.
4. Every verse of the never-seated Strong's was read, and the implicit-seat Strong's were read verse by verse. M02's long divine-anger formula series was read as a series. Context of about 50 key passages was read in all.
5. The scratchpad scripts (`temp_noseat_extract.py`, `temp_ctx.py`) are throwaway `temp_` scripts, not registered utilities (`governance.scripts_and_routines`). If the method scales up, the extract should become a registered utility first.

## 4. What the pilot found, across both clusters

- **Yes, inner-being operations occur with no explicit seat, in both clusters.** What carries them:
  - the operation word itself
  - the act (hiding for fear; anger turned straight into a deed)
  - the face and body
  - quoted speech
  - **another person naming the seat** (Jezebel to Ahab, God to Cain, Jesus in Luk 24:38)
  - a reflexive pronoun ("in himself")
  - a seat built into the word (*dipsuchos*, *athumeō*, *thumos*, *cholaō*)
  - body words outside M47: *chob* "bosom", *cheder-beten* "chambers of the belly"
- **The implicit (cross-correlated) seat is real, but it needs the sense to match.** Often it belongs to **another party**:
  - M20: God hides his face, and **the human** is dismayed
  - M02: God's anger answers **the provoker's heart** or strikes **the sufferer's life**
- **The seat often arrives in the next verse, as explanation or consequence:** Neh 5:6→7; 1Ki 21:4→5; 1Sa 1:7→15; Deu 1:27→28; Phili 4:6→7. The ±3-verse neighbour measure in the seat-coverage plan picks these up. The per-Strong's measure does not.
- **A large share of both clusters is not an inner operation at all.** In M20 it is concealment of objects and people, and "cut off". In M02 it is dirges, splinters, warm bread, the raging sea, and the long run of divine-anger formulae, whose inner-being content sits with the human party.

## 5. Open for the researcher (items 1–2 are escalation #1883)

1. **Confirm or reject the §3.3 refinement.** It changes which Strong's count as "never seated".
2. **Scale-up.** Go to the next clusters with the same method, or adjust it first? For example: register the extract as a utility, add the next-verse seat check as a standard column (the CSV already carries `seat_within_3`), and read divine-bearer formula series as series by default.
3. **Candidate additions to the M47 "excluded / other inner-place words" list:** *chob* "bosom" (H2243), *cheder* "chamber" (H2315) with *beten* "belly", and the Greek reflexive "in himself". These are recorded only, not proposed.
4. **Pointers for later revisits:** Jon 4 in Batch G §16 (the death side); 1Ki 21:5 and 1Sa 1:15 in Batch F (one person naming another's inner state).
5. Escalation **#1882** (config rule for the per-cluster folder name) is still awaiting your approval. The pilot folders use its proposed form `{code} - {short name}`.
