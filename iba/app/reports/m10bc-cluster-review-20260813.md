# M10b / M10c cluster review — why they look broken, and what to do about it

> Ad-hoc investigation, outside the app's structured pipeline (per researcher instruction 2026-08-13). No DB writes made. `iba.db` = `iba/app/db/iba.db`.

## 1. The symptom, confirmed

From `report.cluster` (`iba/app/reports/cluster-v2-20260812.md`) and a direct query of `cluster_strong`:

| cluster_code | short_name | description | strongs currently assigned |
| --- | --- | --- | --- |
| M10b | Wickedness | Wickedness, Evil and Abomination | **1** — H5240 "vile" |
| M10c | Defilement | Defilement and Impurity | **4** — G6410 "impure", H2610 "to pollute", H2612/H2613 "profaneness" |

Both are `review_flag=1`/low-confidence except one auto-precedent row. Meanwhile `M10` (Sin, Guilt and Transgression) holds **132–173** word-origin strongs, and its own top-10-meanings list (in the same report) is dominated by exactly the vocabulary M10b/M10c's `gloss` fields claim: *"abominable/abomination"* (271 freq), *"wicked, wickedness"* (312 freq), *"unclean"* (271 freq), *"defilement, to defile"* (204 freq), *"Evil-merodach, evil, evil actions, evil thinking, evil/bad, evil: trouble, evil: wickedness"* (674 freq). So: not a rendering glitch — M10b/M10c are genuinely near-empty stub clusters sitting next to a heavily overloaded parent whose content matches their own definitions.

Also relevant: `report.cluster`'s "word-origin gap list" is **0** — every word-origin strong already has *some* cluster assignment. So the fix here can only be a **relocation** of already-assigned strongs, never a fresh gap-fill run — matches how you framed the ask.

## 2. Root cause (traced, not guessed)

Three things compound:

1. **M10b/M10c are legacy migration artefacts, not a fresh IBA design decision.** The 2026-08-11 cluster-allocation observation log (`iba/docs/cluster assignment process/wa-obslog-global-cluster-alloc-v1-20260811.md:29`) records the seed taxonomy as-received: *"49 cluster rows... M10 split into M10/M10b/M10c"*, sourced entirely from `old-system-migration` (the old `bible_research.db` programme's cluster table, 2,801 rows carried over as reference).
2. **That exact three-way split was already reversed once, in the old system, by your own ruling.** `scripts/_apply_merge_m10bc_into_m10_20260623.py` (2026-06-23) collapses M10b+M10c into M10 with the comment: *"the three-way split was an artificial linear-partition; they are one sin operation."* That merge lives only in `bible_research.db` — the IBA migration snapshot that seeded `iba.db`'s `cluster` table evidently predates it (or wasn't told about it), so M10b/M10c came back as live targets in IBA without anyone re-deciding the question.
3. **The 2026-08-11/12 LLM allocation pass noticed the ambiguity and never resolved it.** Its own working notes flag it directly: *"T-defile: defile/defilement/unclean/sexual-sin → M10c vs M10"* (obslog line 94) — logged as an open tension, no default rule set. Case-by-case, every wickedness/defilement-shaped strong that reached this fork got decided the same way, visible in the `cluster_strong.rationale` text: `"precedent conflict: M10[P1]; M10b[P2] | accepted"`, `"precedent conflict: M10[P1]; M10c[P2] | accepted"` — M10, as the higher-precedent (older/parent) cluster, won every time, even on rows where its own profile score barely edged out M10b/M10c (e.g. H0192 "Evil-merodach": *"M10:7.4, M27:7.1, M10b:6.7"*).

Net effect: M10b/M10c were never actually rejected as a design — they were structurally starved by a precedent tie-break that always favours the parent.

## 3. Relocation candidates (queried directly, not from the report)

Searching every word-origin strong currently in M10 / M27 / T2 / T3 for a gloss matching M10b's or M10c's own `cluster.gloss` keyword set:

- **M10b-shaped: 39 strongs, combined STEP frequency 2,528** — currently: 27 in M10, 10 in M27, 2 in T3.
- **M10c-shaped: 21 strongs, combined STEP frequency 789** — currently: 16 in M10, 4 in T3, 1 in T2.

### High-confidence M10b candidates (abomination / evil / wicked / unrighteous / wrong / blaspheme vocabulary, currently in M10 or M27)

| strong | gloss | count | currently in | note |
| --- | --- | --- | --- | --- |
| G4190 | evil/bad | 383 | M10 | |
| G2556G | evil/harm: evil | 342 | M27 | scored M27:18.7, M10:14.8, **M10b:13.4** |
| H7563 | wicked | 266 | M10 | |
| G0093 | unrighteousness | 214 | M10 | |
| H7451H | bad: evil | 182 | M27 | |
| H7451I | distress: evil | 150 | M27 | |
| G2549 | evil | 125 | M10 | |
| H8441 | abomination | 120 | M10 | |
| G0946 | abomination | 117 | M10 | |
| H7451B | bad: evil | 116 | M27 | |
| H7489A | be evil | 100 | M27 | |
| H0205G | evil: wickedness | 66 | M10 | |
| G4189 | evil | 49 | M10 | |
| G0987 | to blaspheme | 40 | M10 | |
| H7562 | wickedness | 30 | M10 | |
| H2154 | wickedness | 29 | M27 | |
| H8251 | abomination | 28 | M10 | |
| G2554 | to do evil/harm | 26 | M27 | |
| G0988 | blasphemy | 21 | M10 | |
| H7455 | evil | 19 | M10 | |
| G5337 | evil | 15 | M10 | |
| H7564 | wickedness | 15 | M10 | |
| H0205H | evil: trouble | 12 | M10 | |
| G0824 | wrong | 11 | M10 | |
| G2556H | evil/harm: harm | 10 | M27 | |
| G2555 | wrongdoing | 7 | M10 | |
| G0989 | blasphemous | 6 | M10 | |
| H0192 | Evil-merodach | 4 | M10 | profile M10:7.4/M27:7.1/**M10b:6.7** |
| G7774 | evil-minded | 2 | M27 | |
| G0947 | abominable | 2 | M10 | |
| G6662 | abomination | 2 | M10 | **explicit precedent conflict: M10[P1]; M10b[P2]** |
| G8238 | abomination | 2 | M10 | **explicit precedent conflict: M10[P1]; M10b[P2]** |
| H4849 | wickedness | 1 | M10 | |
| G7771 | an evil deed | 1 | M10 | |
| G7773 | evil thinking | 1 | M10 | |
| G4191 | more evil | 0 | M27 | |
| G7772 | evil actions | 0 | M10 | |

*(2 T3 operation-verb rows omitted — "to wrong" (G5233/H1970) — arguably correct as T3 already; see §4.)*

### High-confidence M10c candidates (defile / defilement / impurity / unclean vocabulary, currently in M10)

| strong | gloss | count | currently in | note |
| --- | --- | --- | --- | --- |
| G0169 | unclean | 183 | M10 | |
| H2930A | to defile | 161 | M10 | |
| H2931 | unclean | 88 | M10 | |
| G0167 | impurity | 61 | M10 | |
| H5079 | impurity | 29 | M10 | |
| G3435 | to defile | 15 | M10 | |
| H1351 | to defile | 11 | M10 | **explicit precedent conflict: M10[P1]; M10c[P2]** |
| G3393 | defilement | 4 | M10 | **explicit precedent conflict: M10[P1]; M10c[P2]** |
| G7121 | to defile | 4 | M10 | **explicit precedent conflict: M10[P1]; M10c[P2]** |
| G3436 | defilement | 2 | M10 | |
| G4510 | to defile | 2 | M10 | **explicit precedent conflict: M10[P1]; M10c[P2]** |
| G3394 | defilement | 1 | M10 | |
| G0234 | defilement | 1 | M10 | **explicit precedent conflict: M10[P1]; M10c[P2]** |
| G7170 | to defile | 1 | M10 | **explicit precedent conflict: M10[P1]; M10c[P2]** |
| H1352 | defilement | 1 | M10 | **explicit precedent conflict: M10[P1]; M10c[P2]** |

*(5 rows omitted as lower-confidence "profane" operation-verbs already routed to T3/T2 by the T2/T3 operation-carve-out rule: H2490H, H2490C, G0953, G2840, H2491B — these were deliberately triaged as operations, not nouns, so leaving them in T3/T2 may well be correct; flagging only for completeness.)*

## 4. This is a judgement call, not a bug fix — two real options

I'm not relocating anything yet. Two defensible paths, and they contradict each other:

**Option A — honour the 2026-06-23 ruling; retire M10b/M10c in IBA too.**
You already decided, in the old system, that this exact split was artificial and collapsed it. IBA's taxonomy resurrected it only because the migration snapshot predated that decision — arguably an oversight, not a fresh design choice. Under this option: move the 5 strongs currently sitting in M10b/M10c back into M10, retire the two cluster rows (mirroring the old `_apply_merge_m10bc_into_m10_20260623.py` pattern), and M10's own top-10-meanings breakdown (already showing sin/evil/abomination/unclean/iniquity/defilement as sub-senses within one cluster) stands as the intended shape.

**Option B — the split is deliberate in IBA and the *allocation* is what's broken; repopulate M10b/M10c.**
IBA's cluster set and method aren't a strict continuation of the old programme (new schema, new pipeline, new researcher-facing rules) — if the split is wanted here regardless of the old ruling, then the 2026-08-11 allocation simply mishandled the M10-vs-child tie-break, and the ~39 + ~21 candidates above (2,528 + 789 combined STEP frequency) should move out of M10/M27 into M10b/M10c per their own gloss definitions.

Note also raised in passing: **M27 "Evil, Wickedness and Abomination"** is near-identical in description to M10b "Wickedness, Evil and Abomination" — worth deciding at the same time whether M27 and M10b should also merge, or what actually distinguishes them (M27 currently holds ruin/idolatry/violence/devastation-type senses; M10b's own gloss list is narrower — abomination/evil/wicked/unrighteous/blaspheme). Not resolved here.

Which way do you want to go — collapse M10b/M10c back into M10 (Option A), or repopulate them from the candidate lists above (Option B)? If B, say so and I'll also settle the M10c "profane"-verb rows and the M27/M10b overlap before relocating anything.

---

## 5. Decision recorded (2026-08-13): **Option B** — repopulate M10b/M10c, no merge

You chose Option B. Before relocating anything I pulled M27's full membership (not just its top-10) to work out whether M27 and the-repopulated-M10b are actually one overlapping mess or two genuinely separable clusters.

## 6. M27's full membership (45 word-origin strongs), sorted into what it actually contains

M27's `cluster.gloss` seed text (`"bad: harmful, be desolate: destroyed, be evil, devastation, idol, idol's temple, idolater, idolatrous, idolatry, refuse, refuse, sacrificed to idols, shade, to detest, to do evil/harm, to ruin"`) is itself already a mix of unrelated senses. The 45 actually-assigned members split cleanly into five groups:

**Group 1 — moral-quality "evil/bad/wicked" vocabulary (character, not act) — this *is* the M10b overlap:**

| strong | gloss | count | note |
| --- | --- | --- | --- |
| G2556G | evil/harm: evil | 342 | scored M27:18.7 vs **M10b:13.4** — close |
| H7451H | bad: evil | 182 | root `ra` adjective, "homonym risk" flagged already |
| H7451B | bad: evil | 116 | same root/sense as H7451H |
| H7451A | bad: harmful | 68 | same root, character sense |
| H7489A | be evil | 100 | |
| H2154 | wickedness | 29 | |
| G2554 | to do evil/harm | 26 | verb form, but character-of-the-doer sense |
| H0873 | bad | 4 | scored M27:4.5, M10:2.7, **M10b:2.7** |
| G7774 | evil-minded | 2 | |
| G2550 | malice | 1 | |
| H4827 | mischief | 1 | |
| G4191 | more evil | 0 | |
| H8262 | to detest | 7 | revulsion-at-evil sense, matches M10b's "abomination" register |

*(H7451I "distress: evil" (150) is dual-tagged M03+M27 — that's the **noun** `ra'ah` calamity/misfortune sense, correctly home in M03 Grief; the M27 tag on it is redundant, not a M10b candidate. H7451C "distress: harm" (157), same noun family, is M03-only — consistent.)*

**Group 2 — idolatry / false worship — genuinely M27's own territory, no M10b overlap:**

H1544, H6459, H6456, H0457, H6091, H5566 (idol, 5–48 freq each), G1495 (idolatry, 4), G2712 (idolatrous, 1).

**Group 3 — ruin / devastation / violence (evil's *consequence*, not its character) — also genuinely M27's own territory:**

H7843, H7703, G4938, G2679, H8077A, H8074G, H8074H, G2692, H5856, G3832, H5754, H3589, H4072, H7591, H8395 (all "ruin/devastation/desolate", 1–146 freq), H2555 (violence, 60).

**Group 4 — "refuse" — a homonym collision, home is neither M27 nor M10b:**

The `cluster.gloss` seed has "refuse" twice, and it's two unrelated English words: *to refuse* (decline) vs *refuse* (a rejected/detestable thing). Four members inherited this ambiguity —

| strong | gloss | actual sense | better home |
| --- | --- | --- | --- |
| H3985 | to refuse | decline/refuse-to-act (verb) | M30 (Obedience/Disobedience) or T3, not evil at all |
| G3868 | to refuse/excuse | same | M30 or T3 |
| H6292 | refuse | *paggul* — ritually-rejected/abhorrent sacrificial meat | M10c (Defilement) — it's about ritual abhorrence, not moral character |
| H3973 | refuse | *ma'us* — a contemptible/detestable thing | M10b (Wickedness/abomination register) |

**Group 5 — one outlier:** H7496 "shade" (8) = *repha'im*, the shades of the dead — unrelated to evil in any sense; looks like inherited gloss-seed noise from the old system, not a live allocation decision (`old-system-migration`, no rationale). Flagging only; not part of this M10b/M27 question.

## 7. Refined proposal — two distinct clusters, not a merge

**M10b (Wickedness, Evil and Abomination)** = moral **character/quality** register — what a person or act *is*:

- current M10b member (1) + the 39 M10-sourced candidates from §3 + Group 1 above (13 items) + H3973 from Group 4 = **54 strongs**, combined STEP frequency ≈ 3,470.
- Optionally the 2 T3 "to wrong" operation-verbs from §3 (G5233, H1970) if you want the verb form included too — I'd leave those in T3 as-is; they're process, not character.

**M27 (rename candidate: "Idolatry, Ruin and Violence" — keep code/short_name, tighten description away from "Wickedness/Evil" wording that duplicates M10b)** = evil **enacted / its consequence**:

- Group 2 (8 idolatry items) + Group 3 (16 ruin/devastation/violence items) = **24 strongs**, dropping the redundant H7451I dual-tag.
- `cluster.description` changes from *"Evil, Wickedness and Abomination"* (near-verbatim duplicate of M10b's *"Wickedness, Evil and Abomination"*) to something like *"Idolatry, Ruin and Violence"* so the two clusters read as distinct on sight, not as synonyms.

**M10c (Defilement and Impurity)** gains one more candidate from this pass: H6292 (Group 4) alongside the §3 list.

**Not part of M10b/M27 at all** — flagged as a side-finding, needs its own small decision: H3985 and G3868 ("to refuse" = decline) probably belong in M30 (Obedience/Disobedience) or T3 (Operations), not "Evil"; H7496 ("shade"/Rephaim) doesn't belong in M27 either. I haven't touched these — say if you want them folded into this relocation pass or handled separately.

## 8. Status

Nothing has been written to `iba.db` yet. Once you confirm this refined split (and the two side-findings in §7 last paragraph), I'll apply: relocate the ~54 M10b members, ~24 M27 members, the M10c additions from §3+§6, update M27's `description`, and re-run `report.cluster` to verify.
