# M10c prep — Phase 1 (UT verse review) — 2026-05-26

**Cluster:** M10c — Defilement and Impurity
**Status:** `Not started` → start Phase 1 (UT review)
**Governing instruction:** `wa-sessionb-cluster-instruction-v2_8-20260519` §4
**Reference impl:** `scripts/_apply_m10b_ut_review_via_api_20260525.py`

## 1. Term universe (8 terms, 275 verses)

| Strong | Translit | Lang | Total V | UT | VC rows | Relevant | Gloss |
|---|---|---|---:|---:|---:|---:|---|
| H2930A | ta.me (verb) | Heb | 128 | **19** | 109 | 109 | to defile |
| H2931 | ta.me (adj) | Heb | 78 | **39** | 39 | 39 | unclean |
| G0169 | akathartos | Gre | 30 | 0 | 30 | 30 | unclean |
| H5079 | nid.dah | Heb | 24 | 0 | 24 | 24 | impurity |
| G0167 | akatharsia | Gre | 10 | 0 | 10 | 10 | impurity |
| G3435 | molunō | Gre | 3 | 0 | 3 | 3 | to defile |
| G3436 | molusmos | Gre | 1 | 0 | 1 | 1 | defilement |
| G3394 | miasmos | Gre | 1 | 0 | 1 | 1 | defilement |
| **TOTAL** | | | **275** | **58** | **217** | **217** | |

**Inherited:** 217 verse_context rows already exist (all is_relevant=1) from pre-split M10 work; not re-classified by Phase 1 (§4.1).

**UT load:** 58 verses across 2 terms. All in `ta.me` (the verb + the adjective).

## 2. Cluster scope (proposed system-prompt domain block)

**M10c owns the STATE of uncleanness** — the inner-being condition produced by contact with what defiles, OR the moral-defilement register where outward purity is contrasted with inner impurity.

M10c sits between two siblings:

- **M10 (Sin/Guilt/Transgression)** — owns the ACT/STATE/EXPERIENCE of moral failure. The act of sinning produces guilt; uncleanness produces a state needing cleansing — distinct registers.
- **M10b (Wickedness/Evil/Abomination)** — owns the CHARACTER of evil. Abomination (to.e.vah / shiq.quts) belongs to M10b as moral-character judgement; ritual abomination (dietary, cultic) may overlap with M10c.

M10c owns the verse when its content names:

1. **Ritual / cultic uncleanness rendered by contact** — corpses, leprosy, menstruation (nid.dah), bodily emissions, unclean animals, sin offerings: what defiles, what is defiled, the process of defilement.
2. **Unclean as state-condition** — the person/thing in its rendered-unclean state (ta.me adj; akathartos), separated from holy.
3. **Inner moral defilement** — NT-distinctive register where defilement extends inward: heart-defilement (Mat 15:18-20), conscience-defilement (Tit 1:15), moral-impurity-as-defilement (akatharsia in vice lists), cleansing of "defilement of body and spirit" (2Cor 7:1).
4. **Uncleanness as moral category** — verses where uncleanness/impurity names a moral state distinct from sin-act (M10) or evil-character (M10b).
5. **Cleansing / purification** — the response to defilement (washing, sacrifice, time-bounded separation, eventually Christ-cleansing).

## 3. Disambiguation hot-spots (UT-relevant)

These are the per-verse judgement calls the API classifier will be asked to make.

### ta.me verb (19 UT verses)

The defilement verb covers a wide range:
- Ritual-cultic defilement (Lev/Num passim — most common; should be M10c-relevant)
- Defilement of sanctuary, land, name (Lev 20:3, Eze 36:17 — extended ritual + moral hybrid; M10c-relevant)
- Defile by contact with corpse / unclean animal / nid.dah (clear M10c)
- NT moral-defilement metaphorical uses (Heb 12:15 "defile" of many; clear M10c when inner)

### ta.me adjective (39 UT verses)

The "unclean" adjective:
- Ritual-unclean state (vast majority — clear M10c)
- Categorical use ("unclean animal", "unclean spirit" — boundary calls)
- Unclean spirits (akathartos in NT, NOT in this set since this is Hebrew adj — but Hebrew tā.me does name "unclean person" / "unclean place")
- Moral metaphor ("we are all as an unclean thing", Isa 64:6 — clear M10c moral)

## 4. Forbidden grounds (§4.5.1 — global)

Per the instruction, SET_ASIDE may NOT use:
- "Not God-directed" / "no vertical framing"
- "Lacks theological depth"
- "Inner state too mundane / circumstantial"
- "Inner state too negative / too corrupt"
- "Bodily/sensory rather than spiritual"

**For M10c specifically:** the "bodily/sensory rather than spiritual" trap is the danger. M10c IS the cluster about bodily/material/ritual defilement extending into the inner being. Do NOT set_aside because the defilement is "merely physical" — bodily defilement of the inner person is exactly the cluster's content.

Valid SET_ASIDE for M10c:

- "No inner-being state evidenced — verse describes external ritual procedure / dietary list only (no inner state).
- "Term here means X (literal non-defilement sense) — outside M10c scope."
- "Out-of-scope by design — verse evidences moral-character abomination (→ M10b) or act-of-moral-failure (→ M10), not defilement-state."

## 5. Outputs (canonical filenames)

- VCNEW patch: `Sessions/Session_Clusters/M10c/wa-cluster-M10c-patch-vcnew-utreview-api-v1-20260526.json`
- Review doc: `Sessions/Session_Clusters/M10c/wa-cluster-M10c-ut-verse-review-api-v1-20260526.md`
- Raw API responses: `Sessions/Session_Clusters/M10c/wa-cluster-M10c-ut-api-raw-responses-v1-20260526.json`

## 6. Cost estimate

- 58 UT verses across 2 terms. Both will fit in one chunk each (well under 50-chunk threshold).
- Estimated total API calls: **2** (one per term). System prompt cached after first call.
- Model: claude-sonnet-4-6 (same as M10b).

## 7. Phase 2 input (pre-estimate)

After Phase 1:
- ~217 inherited + ~50 new relevant (estimate) ≈ 267 is_relevant rows needing Pass A meaning + keywords.
- ~6 batches at default size 50; ~6 API calls.

## 8. Next steps

1. Build `scripts/_apply_m10c_ut_review_via_api_20260526.py` (clone M10b's, adapt SYSTEM_PROMPT).
2. Dry-run to confirm UT load = 58.
3. Run live API.
4. Apply VCNEW patch.
5. Verify post-state (vc_completed; R4 anchor rule; no forbidden grounds).
6. Phase 2: run generic `_run_passa_via_api_v1_20260515.py --m-cluster M10c`.
7. Apply VCREVISE patch; verify §5.6 hard gate = 0.
8. Obslog + commit.
