# Collections of surfaces by likeness of meaning, method plan v2 (#2360)

> Developer Mode session 325129d4, 2026-11-05. Nothing in this plan is built as a registered routine; the experiment ran as scratch scripts (not in the project) and wrote files only. It follows the researcher's rulings D1 to D3 of 2026-11-04 (#2360 v2, v3, v5). Every judgement is inferential (B:4) until the researcher confirms it.

## 1. What the experiment showed (checked in the files named)

Pool: 1,303 single-word bases (phrases are assigned last, D2). Files are in `outputs/concept-mapping/collections/`.

1. **Embedding model.** On 53 known prefix-opposite pairs, the share found within the nearest 10 bases: `qwen3-embedding` bare 38, framed 41; `nomic-embed-text` bare 22, framed 22 (`recall-gold-v1-20261104.json`). The frame costs five times as long (1,599 s against 321 s) for a gain only in the nearest 5. **Choice proposed: `qwen3-embedding`, bare word.**
2. **Pairwise judge** (A and B, no collection): 1,536 pairs, synonym 0, opposite 97, associated 1,329, unrelated 110 (`pair-judgements-v1-20261104.jsonl`). It cannot separate synonym from associated. Not used.
3. **Whole-collection judge** (seed collection shown, candidate compared with any member, "when unsure, no"): three seeds, 247 judgements (`seed-test-v1-20261104.jsonl`, `seed-collections-v1-20261104.json`). The collections drifted: fear grew to 25 bases and became a general distress and grief group; love took joy, hope, peace, grace; deceive took truthful and true as synonyms. Clear synonyms were refused (afraid, dread, terrify, panic, affection, lie, mislead). Not used.
4. **Core-word-anchored judge** (candidate against the seed's core word only; synonym, opposite or distinct; model reasoning off), 28 cases. Right: afraid, dread, fearful, affection, lie, mislead (synonym); hate, courage, truth, truthful (opposite); grace, hope, peace, mercy, compassion, joy, sorrow, grief (distinct). Wrong or doubtful: deceit and panic (distinct, should be synonym), frighten and tremble (distinct), 3 s a call. With the model's reasoning on, the calls take 33 to 234 s and are not better (affection and lie came out distinct). **Choice proposed: anchored, reasoning off.**

## 2. The method (progressive, D3)

- **Unit:** the base. Every surface of one base goes together (D1). Behaviour and state surfaces are not separated.
- **Round:** pick about three seed core words; shortlist the nearest 40 unassigned bases to each core word (not to the growing centroid, which caused the drift); judge each shortlisted base against the core word only; synonyms and opposites join (opposites sit in the collection, your answer to my earlier D3); then take the next 40 nearest to the core word plus the members, as the members have been judged against the core word only; stop when a pass adds none. Then pick the next three seeds from the unassigned pool.
- **No size cap.** A collection that takes a large share of the pool is flagged as a suspect definition for your review.
- **Phrases last (D2).** After the single words, each phrase is judged against the collections by its head word.
- **Flagged items travel (D2):** 99 surfaces with an opposite or other lead, 47 with a base outside the list, the possessives (`love’s`, `heart’s`, `fool’s` as separate bases), the held M1 pairs and failed words.
- **Files, not the database (D1).**

## 3. The open point, which only you can settle

The anchored judge finds **synonyms and opposites** well, and it deliberately refuses words that are only **associated** (joy, hope and mercy against love). You asked for "the words that are associated by meaning" too. Left in the same judge, association made the collections drift. Options:

- **A. Two tiers (my suggestion).** Collections are built from synonyms and opposites only. Associated words are written into a separate, labelled column for each collection (the judge's second question, asked of the remaining pool against each finished collection), for you to inspect, and a later rollup into larger concepts (D1, 250 to 300) is the place where they merge.
- **B. Associated words join the collection directly,** with a second judged step against the members, accepting the drift risk and relying on your review of each collection.
- **C. Synonyms and opposites only,** with association left to the rollup.

## 4. Known weaknesses

- The anchored judge missed deceit and panic. Misses leave a base in the pool for a later seed, so a miss costs a later round, not a wrong membership; a wrong inclusion is the more serious error. The next test measures both against 100 bases that I list for you to read.
- Seeds are chosen by me from the pool. You may choose them instead.

## 5. For the researcher to decide

1. **Association: A, B or C?**
2. **Model and frame:** `qwen3-embedding` bare for the shortlist and `qwen3:30b` with reasoning off for the judge, as shown in section 1.
3. **Next step:** (a) run three further seeds of your choice or mine with the anchored judge, to a list for you to read; or (b) first build the registered routine (work package, settings, wrapper) for it, as CHARTER section 1 requires, before more rounds. My suggestion: (a), and (b) once the collections look right to you.
