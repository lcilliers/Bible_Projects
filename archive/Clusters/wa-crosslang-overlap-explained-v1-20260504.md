# Hebrew/Greek cluster overlap — answer

**Question (researcher, 2026-05-04 09:47):** *"does all the greek cluster overlap with hebrew clusters, and if not, why not"*
**Source data:** [outputs/markdown/term-clusters-crosslang-20260504.md](term-clusters-crosslang-20260504.md) (raw report) and [.json](term-clusters-crosslang-20260504.json)

---

## ⚠ ID-mismatch caveat (read first)

The crosslang report was run on the **intermediate 5-way clustering** (80 Hebrew clusters `C0..C79` + 40 Greek clusters `C0..C39`), **not** on the final term-anchor structure (55 Hebrew `H000..H054` + 33 Greek `G000..G032`).

Why: the term-anchor build (T1/T2/FLAG/EXTRACTION-NOISE bucketing) happened *after* the crosslang analysis, and re-numbered the T1-only clusters. So the `C29`, `C75`, `C4` etc. references below are intermediate cluster IDs.

The structural findings below still hold — same vector space, same terms, just with different IDs and slightly different cluster boundaries. **If you want clean H001↔G001 mapping using the catalogue you just reviewed, I can re-run the crosslang analysis against the final term-anchor structure** (~10-minute job). Flagged as next step.

## 1. Headline answer

**No** — Greek clusters do not all overlap with Hebrew clusters. Of 40 Greek clusters analysed:

| Verdict | Greek count | What it means |
|---|---:|---|
| **ALIGNED** | 6 | Cosine similarity ≥ 0.55 to a Hebrew cluster *and* ≥ 1 shared theme word — clear lexical-semantic overlap |
| **PARTIAL** | 29 | Decent similarity (0.40–0.55) but no shared theme word, or high similarity with no theme overlap |
| **ORPHAN** | 5 | Top-1 similarity < 0.40 — no close Hebrew counterpart |

Hebrew → Greek (the reverse direction):

| Verdict | Hebrew count |
|---|---:|
| ALIGNED | 10 of 80 |
| PARTIAL | 61 of 80 |
| ORPHAN | 9 of 80 |

So **only ~15% of clusters cleanly bridge the two languages**. The majority sit in the "partial" zone — semantically related but cutting the lexical field differently.

## 2. Why so few clean alignments — three structural reasons

### 2.1 No shared verses (method constraint)

Hebrew (OT) and Greek (NT) share zero verses, so the **co-occurrence vector** — which was the strongest within-language clustering signal — is useless for crosslang. The crosslang analysis had to use only the **semantic vector** (root + gloss + meaning, weighted). This is fundamentally a thinner signal.

### 2.2 Hebrew and Greek cut the lexical field differently

The two languages don't carve up emotional/ethical/cultic concepts the same way. Examples from the report:

| Concept | Greek structure | Hebrew structure | Result |
|---|---|---|---|
| Love | `phileō` family (own cluster, G008) AND `agapē/agapaō` (mixed into G026 truth/love/holiness) | `chesed`, `aheb`, `racham`, `dod` — distributed across H019 covenantal core, H039 peace, H043 lust, H050 enemy | No 1-to-1 match. Greek ALIGNED-side `agapē` cluster sits at PARTIAL with Hebrew. |
| Justice/Righteousness | `dikaios` family — own tight cluster (G004 = G C29 in report) | `tsedeq/tsadiq/mishpat` distributed: integrity-side in H019 covenantal core, justice-side in C29 (mixed keep/righteousness), wickedness-side in H028 anger/turning | Greek `dikaios` is **ORPHAN** (sim 0.39). Hebrew has the vocabulary but it's split. |
| Remembrance | `mna-` family — own clean cluster (G020 = G C25 in report) | `zakar/zikkaron` — pulled into H019 covenantal core | **ORPHAN** (sim 0.29). |
| Slavery/Service | `doulos` — own cluster (G C37) | `avad` — own cluster (H012 Service & Ministry, was C71) | Both have own clusters but **don't align semantically** (sim 0.31). The Hebrew `avad` carries cultic-ministry overtones the Greek `doulos` lacks; Greek `doulos` carries social-property meaning the Hebrew `avad` largely lacks. |
| Kingdom | `basil-` family — own clean cluster (G031 = G C33 in report) | Hebrew `melek/malkut` distributed; mostly didn't even cluster as kingdom — its closest match is C72 (height/contempt/queen) at sim 0.32. | **ORPHAN.** |

In each case the *concept* exists in both languages but the *clustering geometry* differs because:
- One language has a tight morphological family, the other distributes the meaning across multiple roots
- English glosses for parallel concepts often use different translation choices
- Some Greek theological terms (`charis`, `dikaiosunē`, `pistis` in NT theological sense) developed *after* the LXX, so they have no exact Hebrew lexical counterpart

### 2.3 Five Greek ORPHAN clusters (no Hebrew partner)

These are the "Greek-only" theological vocabulary the researcher's question implicitly anticipated:

| Greek cluster (intermediate ID) | Theme | Final identity-catalogue equivalent | Why no Hebrew partner |
|---|---|---|---|
| G C29 (n=16) | just/crime/righteousness — `dikaios` family | **G004 Justice & Righteousness** | Hebrew tsedeq/tsadiq/mishpat distributed across H019, H028, H016 — not in one cluster |
| G C33 (n=7) | reign/kingdom/palace — `basil-` family | **G031 Kingdom & Reign** | Hebrew kingship vocab (melek, malkut) is split across height/rule clusters; theological "kingdom of God" concept is a NT development |
| G C20 (n=13) | gift/free/deliver — `dōrea/dōrēma` | mostly **G003 Sin, Grace & Salvation** | Hebrew has gift words (matanah, shai) but they cluster with cultic offerings (H036), not with grace |
| G C37 (n=8) | slave/enslave — `doulos` family | mostly **G029 Wrath, Calling & Mercy** (T2: filos cluster) | Hebrew `avad` clusters with ministry/service (H012); Greek `doulos` carries different sociological weight |
| G C25 (n=9) | remembrance/remember/remind — `mna-` family | **G020 Remembrance** | Hebrew `zakar` is buried in the covenantal-core mega-cluster (H019), not isolated |

### 2.4 Nine Hebrew ORPHAN clusters (no Greek partner)

The reverse case — Hebrew structures that don't have a Greek partner:

| Hebrew cluster (intermediate ID) | Theme | Why no Greek partner |
|---|---|---|
| Hebrew C10 (n=18) | hand (`yad` family) | NT Greek `cheir` is too low-frequency to form a cluster; Hebrew yad is highly polysemous |
| Hebrew C20 (n=11) | reckon (`paqad`) | `paqad`'s range — visit, count, punish, oversee — doesn't map to a single Greek concept |
| Hebrew C24 (n=10) | master/rule (`baal/mashal`) | Greek splits these (kurios for master, archō for rule) into different clusters |
| Hebrew C71 (n=10) | serve/service (`avad/avodah`) — what is now **H012 Service & Ministry** | Greek `doulos`/`leitourgia`/`latreuō` are spread across several Greek clusters |
| Hebrew C25 (n=10) | call/encounter (`qara`) — what is now **H022 Calling & Encounter** | Hebrew `qara` carries both "call" AND "encounter"; Greek splits these (kaleō vs hupantaō) |
| Hebrew C69 (n=9) | living/alive (`chay` family) | Greek `zaō`/`zōē` are in different clusters from Greek faith/spirit clusters |
| Hebrew C66 (n=9) | glorious/riches/rank | No tight Greek "glory" cluster (Greek `doxa` is in G024 with "harden/blind") |
| Hebrew C78 (n=9) | end/perfection (`kalah`) — what is now **H030 End & Completion** | Greek end-words (telos, plērōma) are dispersed |
| Hebrew C46 (n=7) | honor/heaviness (`kavod`) — what is now **H044 Honor & Glory** | Greek `timē/doxa/kleos` are in different Greek clusters |

## 3. Six clean ALIGNED Greek clusters (the bridges that DO work)

These pass both the similarity threshold and the shared-theme test:

| Greek (intermediate) | Final equivalent | Hebrew partner | Sim | Shared themes |
|---|---|---|---:|---|
| G C9 (desire/will/anger) | mostly **G019 Will & Purpose** | C4 (sin/guilty/iniquity) | 0.64 | desire, innocent |
| G C8 (peace/anxiety/endure) | mostly **G005 Joy, Peace & Endurance** | C58 (peace) ≈ **H039 Peace & Well-being** | 0.63 | peace |
| G C18 (sin/sinful) | part of **G003 Sin, Grace & Salvation** | C4 (sin) ≈ **H036 Sin & Consecration** | 0.62 | sin |
| G C12 (hell/plan/sense) | mostly **G030 Faith & Mercy** | C75 (seek/rule) | 0.61 | choose |
| G C11 (quiet/foolish/judge) | mostly **G010 Wisdom & Folly** | C29 (keep/justice) | 0.60 | shame |
| G C27 (shame/interpret/praise) | mostly **G027 Atonement & Grief (NT)** | C29 (keep/justice) | 0.57 | seek |

Notice that even the strongest crosslang bridges max out around sim 0.64 — that's a "moderate" similarity. By comparison, within-language clusters routinely show neighbour similarities of 0.7–0.9.

## 4. What this tells us about the cluster ecosystem

1. **The cluster structure is genuinely language-specific.** The same theological/ethical concepts ARE present in both languages, but their *clustering geometry* — which terms group with which — is not transferable. This is a real linguistic finding, not a bug of the method.

2. **The largest mega-clusters absorb cross-language signals.** Hebrew C75 (seek/rule), C29 (keep/justice), and C4 (sin/guilty) appear as top-1 match for **24 of 40 Greek clusters**. These are the gravitational sinks — broad, mid-cohesion clusters that *almost* match many Greek clusters by being broadly themed. This is actually evidence the Hebrew side has an *under-clustering* problem at this granularity (recursive sub-clustering should help — and the validate pass confirms 0 LOOSE clusters survive sub-clustering).

3. **NT theological vocabulary is partly Greek-only at this granularity.** `dikaios`, `basil-`, `doulos` (in NT sense), `mna-` form their own tight Greek clusters with no Hebrew counterpart. That is actually the most interesting structural finding: **the cluster ecosystem itself confirms that NT Greek developed lexical structures around grace/kingdom/righteousness/remembrance that the OT Hebrew doesn't have at the same level of consolidation.**

4. **Cross-language bridges should be expected at the *sub-cluster* level, not the top level.** The current crosslang result suggests bridges work better when you compare *recursive leaves* rather than top-level clusters. Hebrew H019 covenantal-core has chesed-leaf, emet-leaf, qadosh-leaf etc. — those leaves should map cleanly to NT Greek charis-cluster, alētheia-cluster, hagios-cluster respectively.

## 5. Suggested next step

**Re-run the crosslang analysis against the final term-anchor structure** (`H001..H055` + `G001..G033` from the catalogue) so the cluster IDs in this analysis match the catalogue you just named. Then optionally extend to recursive sub-cluster bridges.

Cost: ~10 min for a script update + a re-run. No new vectors needed — `term-semantic-weighted-vectors-20260504.npz` already covers it.

If you want, I'll do that next.
