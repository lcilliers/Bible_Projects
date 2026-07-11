# `ib_characteristic` — table analysis (Psalms normalised index)

> Generated 2026-07-11 from `database/bible_research.db`. The table was rebuilt this session (§7D of the cycle doc) as the **normalised characteristic index**: one record per characteristic **word** (base Strong's), gathering all its read char-spans. This is an analysis of what the 502 Psalms records reveal — the observations, and the scenarios (both analytical opportunities and data-quality issues) that fall out of it.

## 0. Shape (verified)
- **502 records**, book_scope = 19 (Psalms); one per distinct characteristic word.
- **2,168 char-spans linked** (every read characteristic → its word-record via `verse_span_index.ib_char_id`).
- **`family` = NULL on all 502** — the roll-up into recurring families is entirely *pending* (this analysis sets it up).
- **29 legacy conceptual families** archived in `ib_characteristic_legacy` (the roll-up target — see §7).

---

## 1. OBSERVATION — the frequency shape is steeply Zipfian
| occurrences | records | spans |
|---|--:|--:|
| 1 (hapax) | **251** (50%) | 251 (12%) |
| 2–4 | 151 | 395 |
| 5–9 | 46 | 299 |
| 10–29 | 44 | 726 |
| 30+ | **10** | 497 (23%) |

**Half the "characteristics" appear once; a core of ~12 words carries most of the weight.** The dominant core (by occurrences): `soul` (83), `give-thanks` (61), `heart` (61), `praise` (51), `bless` (44), `call` (44), `know` (43), `trust` (39), `keep` (37), `glad` (34), `fear` (28), `love` (27). This *is* the inner-being vocabulary of the Psalter — a small dense centre and a long peripheral tail.

## 2. OBSERVATION — two kinds of characteristic: SEATS vs OPERATIONS (the primary family axis)
Type (`ve_nr 102`) across the 2,168 instances: **action 780**, status 384, state 275, disposition 241, affect 206, faculty 108, volition 95, cognition 64, seat 12.

- **The inner being is read overwhelmingly through what it DOES** — `action` is the largest type (780), then states/statuses.
- The high-frequency records split cleanly:
  - **SEATS** — `soul` (nephesh), `heart` (leb), `spirit` — nouns (type status/seat) that *host* operations; they recur because many operations happen *in/to* them.
  - **OPERATIONS** — `trust`, `praise`, `know`, `bless`, `call`, `give-thanks` — verbs (type action) — the inner being's doings.

This seat-vs-operation split is the **first natural grouping axis** for the pending family layer.

## 3. OBSERVATION — sense-spread separates consistent words from rich ones
Distinct read-senses per record (how many different things one word does):
- **262 records = 1 sense** (a word doing one consistent thing).
- 135 = 2–3 · 48 = 4–6 · **57 = 7+ senses** (highly polysemous).
- Highest spread: `soul` (46 senses / 83 occ), `heart` (34/61), `know` (27/43), `trust` (26/39), `give-thanks` (26/61), `praise` (25/51).

**High spread has three different causes** (which the family work must disentangle):
1. a **seat** (`soul` hosts 46 different operations — it isn't one characteristic);
2. a **polysemous operation** (`trust` in 26 shades — grounding, valuing, self-stilling…);
3. a **homograph** (see §5a).

## 4. OBSERVATION — God is the arena, not the subject (the screen held)
Locus (`ve_nr 116`): `internal:ib-state` 913, **`external:god` 469 (22%)**, `external:person` 73, `internal:heart` 25, `internal:spirit` 6. Nearly a quarter of instances carry God as the locus/target — confirming Screen 0: God enters as the *arena* the human inner being acts toward, never as a characteristic himself.

---

## 5. SCENARIOS — issues the table surfaces (to resolve before / during the family work)

### 5a. Homographs are merged (data quality)
Lemma-grain lumps genuinely different Hebrew roots that share a Strong's form. Clearest case — **`H1481` (gur)** merges two unrelated stems: *"sojourn / dwell"* **and** *"stir up strife / band together."* Its `operation` field even reads "band together / stir up" for what includes the sojourn spans. **Rare but real** — a handful of records need splitting by sense-cluster. (Most high-spread is *polysemy*, not homography: `H5375 nasa` = lift/bear/carry applied to eyes/hands/soul — one root, many objects.)

### 5b. The `operation` field is one span's, not the record's
`operation` is copied from `key_span_id` (a single representative occurrence). For a 46-sense record like `soul`, that one operation is unrepresentative. **The record needs an *aggregated* operation/summary, not a single representative** — a build refinement.

### 5c. The type vocabulary is uncontrolled
The `102 type` values are inconsistent free-text (`action`, `status`, `state`, `disposition`, `faculty`, `state` vs `status`…). **A controlled type vocabulary is a prerequisite** for grouping by type/faculty.

### 5d. ⚠ 112/116 field swap on ~31% of chars
**666 of 2,168 char-spans (31%)** carry a *prose* value in `ve_nr 116 (locus)` (e.g. "paired with giving thanks") instead of a `internal:/external:` code — with the locus code sitting in `112 (coupling)` instead. This is an **authoring inconsistency across the ~150 hand-built psalm readers** (the coupling and locus args were transposed in a subset). It should be corrected before locus/coupling are used analytically.

### 5e. `family` is empty — the grouping is the whole next layer
All 502 records have `family = NULL`. The normalised index exists and links cleanly; **the analytical value — rolling the 502 words up into recurring characteristics — has not been done.** This is what §7 sets up.

---

## 6. OBSERVATION — the hapax tail is the periphery / emergent edge
The 251 single-occurrence records are the peripheral and read-emergent words: `submit`, `folly`, `give-ear`, `terrors`, `apple-of-eye`, `devour`, `languishing`, `groaning`, `guilt`… Genuine inner-being expressions, but each attested once — the diffuse edge of the Psalter's inner life, versus the dense core of §1.

## 7. WHAT THIS SETS UP — the family roll-up (the pending analytical goal)
The 29 archived legacy families are the natural **roll-up target**:
`trust-refuge · fear-of-the-lord · love-aheb · the-heart · desire-appetite · seeking · waiting-hope · grief-lament · joy-gladness · humility · self-mastery · self-examination · memory · rest-stillness · restoration · being-known · being-heard · entrustment · fearlessness · forgiveness-confession · speech-outflow · teachability · integrity-legibility · self-address · self-toward-others · the-felt-interior · the-compulsive-will · formation-by-relation · wisdom-formation.`

The next step is to **populate `family`** by mapping each of the 502 words to a family (`batach`→trust-refuge, `yare`→fear-of-the-lord, `nephesh`/`leb`→the-felt-interior/seats), so the index answers "how does *trust* behave across the Psalter" — grouping many instances into one characteristic, which is the point of the normalised layer.

*Filed 2026-07-11. Read-only analysis over `ib_characteristic` + `ve_lexical` + `verse_span_index`.*
