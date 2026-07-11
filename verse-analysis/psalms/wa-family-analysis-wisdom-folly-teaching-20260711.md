# Family analysis (in isolation): Psalms — `wisdom-folly-teaching`

> Source: `outputs/data/psalms-family-base-sources/psalms__wisdom-folly-teaching.json` only. Book: Psalms (book_id 19). Declared counts: **27 meanings · 41 instances · 34 passages**. All 41 instances verified present and read. Every finding cites `reference · span · Dnnn(label)` into that file. Genre for all 41 = `poetic/wisdom`. Role (D115) = `characteristic` on all 41; none is qualifier or standalone.

---

## 0. Data-integrity screen (done first)

### 0.1 D112(coupling) / D116(locus) field-swap — 11 of 41 instances transposed
Correct order = D116(locus) holds a code (`internal:`/`external:`), D112(coupling) holds a prose phrase. The following **11 instances are swapped** (D116 holds a prose phrase, D112 holds the `internal:`/`external:` code) and must be read corrected:

| span | ref | D116 as-stored (phrase → really coupling) | D112 as-stored (code → really locus) |
| --- | --- | --- | --- |
| 307476 | Psa 106:35 | `paired with mixing` | `internal:ib-state` |
| 270575 | Psa 111:10 | `paired with the fear of the LORD` | `internal:ib-state` |
| 285230 | Psa 92:6 (fool) | `paired with the stupid man's ignorance` | `internal:ib-state` |
| 285431 | Psa 94:8 (fools) | `paired with the call to be wise` | `internal:ib-state` |
| 285226 | Psa 92:6 (stupid) | `paired with the fool's failure to understand` | `internal:ib-state` |
| 270038 | Psa 107:43 (wise) | `paired with attending and considering` | `internal:ib-state` |
| 285433 | Psa 94:8 (wise) | `paired with the folly rebuked` | `internal:ib-state` |
| 269896 | Psa 107:17 (fools) | `paired with their sinful ways and iniquities` | `internal:ib-state` |
| 270999 | Psa 116:6 (simple) | `paired with being brought low and saved` | `internal:ib-state` |
| 269437 | Psa 105:22 (teach) | `paired with binding princes at his pleasure` | `internal:ib-state` |
| 307511 | Psa 107:27 (wits) | `paired with reeling and staggering` | `internal:ib-state` |

Corrected, all 11 have locus = `internal:ib-state`. The remaining 30 instances are in correct order. All corrected-locus reads below use this table.

### 0.2 Self-loop "edges" are not real links
The dominant edge shape in this file is `item_type:"flag"`, `resolution:"inferred"`, `from_span:null`, `to_span` = the span's own id (on D105 bearer, D107 target, D112 coupling). These are **self-loops, not network edges** and are excluded from the network (§ network). Only `pair`/`event` edges with `resolution:"span"` linking to a **different** span are genuine. Genuine edges exist on only 13 spans (see § network); every one links **within a single verse/passage** — there are **no cross-passage / cross-psalm edges** in the whole file.

### 0.3 seat(D104) / manner(D108) = "none"
- **seat** filled on only **3 / 41**: `in the secret heart` (Psa 51:6 · 279762 · D104), `the heart` (Psa 53:1 · 279881 · D104, a `span` pair), `in the secret heart` (Psa 51:6 · 279760 · D104). The other **38 leave seat = none**.
- **manner** filled on only **5 / 41**: Psa 53:1 · 279881 (`inwardly, in the heart`), Psa 51:6 · 279760 (`in the secret heart`), Psa 55:14 · 280068 (`sweet, walking to God's house…`), Psa 73:22 · 282431 (`like a beast toward God`), Psa 69:5 · 281878 (`not hidden from God`). The other **36 leave manner = none**.

### 0.4 Absent dimensions
Across **all 41 instances**, these dimensions never appear: **D109 intensity, D110 specifier, D111 effect, D113 prohibition** — wholly absent. **D103 source** appears **once only** (Psa 74:18 · 282584 · D103 `whom God is asked to remember`). Present on most/all: D101, D102, D104, D105, D106, D107, D108, D112, D114, D115, D116.

### 0.5 Cluster NULL / T2 — 13 instances (9 meanings) the term-cluster cannot type
- **Pure NULL cluster (11 instances / 7 meanings):** `learn` H3925 ×4 (272023, 272036, 272050, 307476); `teach` H3925 ×2 (273855, 277148); `ceased` H2308 (277529); `foolish`(kesel) H3689 (279302); `teach` H2449 (269437); `wise` H2449 (275319); `wiser` H2449 (305872).
- **NULL code but `all_candidates: T2(Supplementary)` (2 instances / 2 meanings):** `counsel` H3245 (Psa 2:2 · 276523); `wounds` H2250 (Psa 38:5 · 277977).

The verbs of learning/teaching (lamad; several yada/chakam senses) and the somatic "wounds" span therefore sit outside the M-cluster typing entirely.

### 0.6 Declared outlier
One meaning is `is_outlier: true`: `folly` (kislah) H3690, Psa 85:8 · 284238, term-cluster **M19(Trust)** where the family expects M15(Wisdom) — per its `outlier_note`.

---

## 1. Coherence — does the label fit its data?

**Core fits; the grouping has fused in a distinct "counsel/deliberation" movement and one somatic stray.** 24 of 27 meanings sit cleanly on the wisdom↔folly↔teaching axis; the M-clusters confirm this: **M15 Wisdom** (6 meanings / 12 inst.), **M16 Folly** (8 meanings / 12 inst.). But three things do not belong to that axis:

1. **A "counsel/deliberation" movement (M17 + one T2), 4 instances, 4 meanings** — keyword-fused via English "counsel":
   - Psa 13:2 · 273544 · D101 `counsel in the soul, sorrow in the heart` — anxious inner churn (etsah), D102 cognition; an **affliction/anxiety** movement, not wisdom.
   - Psa 2:2 · 276523 · D101 `rulers take counsel together` — political **conspiracy** against the LORD (D106 `organised rebellion`), bearer = the rulers; not the wisdom axis.
   - Psa 55:14 · 280068 · D101 `intimate counsel / close fellowship (sod)` — betrayed **friendship/intimacy** (D116 `external:person`); a relational movement.
   - Psa 81:12 · 283806 · D101 `counsels (moetsah)` — self-devised plans preferred to God (D102 faculty); autonomy-as-apostasy.
   These four are one coherent *deliberation/plotting/fellowship* strand, distinct from wisdom-folly-teaching.
2. **A somatic stray:** Psa 38:5 · 277977 · D101 `my wounds fester through my folly` (D102 **state**, cluster T2) — the term is "wounds", not a wisdom/folly term; pulled in only because the verse names foolishness.
3. **The declared outlier:** Psa 85:8 · 284238 (kislah → M19 Trust) — a "turning-back to folly" that the term-cluster reads as mis-placed trust.

A further register-split *within* the wisdom pole: Psa 107:27 · 307511 · D101 `wits (chokmah)` and Psa 105:22 · 269437 · D101 `teach (chakam)` use wisdom vocabulary for **practical craft/skill** (sailors' seamanship; Joseph instructing Egypt's elders), not moral-covenantal wisdom — same lemma family, different register.

**Verdict:** the label is accurate for the dominant body (wisdom/folly/teaching), but the family is *not* a single movement — it fuses (a) the wisdom↔folly moral-cognitive axis, (b) a counsel/deliberation/fellowship strand, and (c) a somatic-folly stray.

---

## 2. The movements evidenced (cited)

### 2A. Wisdom as gift received / interior maturing (M15 + H2449/H7919)
Wisdom is repeatedly something *given to* the interior, not self-generated:
- Psa 19:7 · 275319 · D101 `the simple made wise` / D106 `the sure testimony… makes the simple wise` — an untrained interior opened (passage anchor).
- Psa 51:6 · 279762 · D101 `wisdom (chokmah - taught in the secret heart)`, D104 `in the secret heart` — implanted wisdom, D116 `internal:heart`.
- Psa 90:12 · 284973 · D101 `wisdom (chokmah)` / D107 `from numbering our days` — wisdom as fruit of facing death (D102 disposition).
- Psa 111:10 · 270575 · D101 `wisdom (chokmah)` / D107 `from fearing God` — its root (corrected D116 `internal:ib-state`).
- Psa 119:98 · 305872 · D101 `be wise (chakam)` / D106 `be made wiser` — from the ever-present commandment.
- Psa 49:3 · 279379 · D101 `wisdom (chokmah)`, D102 status / D106 `speak` — the teacher's inner store overflowing into speech.

### 2B. Wisdom as summons / the wise who attend (M15/H7919)
- Psa 2:10 · 276498 · D101 `be wise, be warned` / D106 `kings… summoned to prudence` — the rebellious interior called to sober sense (D102 cognition).
- Psa 94:8 · 285433 · D101 `be wise (sakal)` / D106 `become wise` — fools urged toward discernment.
- Psa 107:43 · 270038 · D101 `wise (chakam)` / D107 `to attend to God's ways` — the coda's charge.
- Psa 49:10 · 279273 · D101 `wise (chakam)` / D106 `die` — mortality levels even the wise.

### 2C. Folly as practical-atheism and moral senselessness (M16)
The strongest, most seated movement:
- Psa 14:1 · 274506 (anchor) · D101 `the fool says 'no God'` / D106 `an interior verdict… that clears the way for abominable deeds` (D102 cognition) — denial as licence.
- Psa 53:1 · 279881 (anchor) · D101 `fool (nabal)…` / D104 `the heart` (span pair) / D108 `inwardly, in the heart` — the Ps14 twin ("Elohim" for YHWH), D114 notes it as practical, not intellectual, atheism.
- Psa 92:6 · 285230 · D101 `fool (kesil)` / D107 `unable to understand God's ways`; paired stupidity Psa 92:6 · 285226 · D101 `stupid (baar)`.
- Psa 94:8 · 285431 · D101 `fools (kesil)` — rebuked ("when will you be wise?").
- Psa 49:10 · 279275 · D101 `fool (kesil)` + 279276 · D101 `stupid / brutish (baar)` — die alike with the wise.
- Psa 73:22 · 282431 · D101 `brutish / stupid (baar - I was brutish and ignorant)` — the psalmist's own humbling self-recognition (bearer = the psalmist).

### 2D. Folly as owned confession / caught corruption (M16)
- Psa 69:5 · 281878 · D101 `folly / foolishness (ivveleth)` / D106 `known (by God)` — honest confession.
- Psa 106:35 · 307476 · D101 `learn (lamad)` / D106 `learn` — folly *caught by association* (D114 "sin caught by association"; corrected D116 `internal:ib-state`, coupling `paired with mixing`).
- Psa 49:13 · 279302 · D101 `foolish confidence / folly (kesel)` — self-assured folly trusting in wealth.
- Psa 107:17 · 269896 (anchor) · D101 `fools (evil)` / D107 `through sinful ways` — folly bringing sickness.
- Psa 74:18 · 282584 · D101 `foolish (nabal…reviles your name)` — the only span carrying **D103 source** (`whom God is asked to remember`).
- Psa 85:8 · 284238 · D101 `folly (kislah)` — turning-back to folly (declared outlier → M19 Trust).
- Psa 116:6 · 270999 · D101 `simple (pethi)` / D106 `be preserved` — the artless whom God keeps (a *positive* reading of "simple").

### 2E. Teaching / learning — outward-reaching transmission
- Learn (lamad, all NULL-cluster): Psa 119:7 · 272023, 119:71 · 272036, 119:73 · 272050 — D101 `learn (lamad)`, D107 `God's word`, D116 `external:god`; learning as ground of upright praise / affliction as the school of learning.
- Teach as passing-on: Psa 34:11 · 277148 · D101 `I will teach you the fear of the LORD` (D102 volition); Psa 78:5 · 283270 · D101 `teach (yada, hiphil)` / D116 `external:person` — the charge to instruct the young; Psa 105:22 · 269437 · D101 `teach (chakam)` — Joseph teaching Egypt's elders.
- Teach as being-taught: Psa 51:6 · 279760 · D101 `make known / teach (yada hiphil)` / D107 (pair→279762 wisdom) / D104 `in the secret heart`; Psa 143:10 · 273855 · D101 `desire to be taught God's will` (D102 volition) — the interior wanting conformity.

### 2F. Deliberation / abandonment (M17 + strays)
- Psa 36:3 · 277529 · D101 `he has ceased to act wisely` (D102 volition) — a chosen abdication of wisdom.
- Psa 13:2 · 273544 · D101 `counsel in the soul, sorrow in the heart` — wearying self-consultation.
- Psa 81:12 · 283806 · D101 `counsels (moetsah)` / D107 `instead of God` — autonomy as apostasy.
- Psa 2:2 · 276523 · D101 `rulers take counsel together` — conspiracy.
- Psa 55:14 · 280068 · D101 `intimate counsel (sod)` — betrayed fellowship.
- Psa 50:17 · 279537 · D101 `discipline / instruction (musar)` — the correction the wicked spurns (D112 pair `the object of the wicked's hatred`).
- Psa 38:5 · 277977 · D101 `my wounds fester through my folly` (D102 state) — folly's somatic rot.

---

## 3. The network (genuine `span`-resolution edges only)

All genuine edges are **intra-verse**; there is no book-level link structure. Genuine edges sit on 13 spans:

- **Antithetical / appositional folly pairs (Psa 49:10):** 279275(fool) ↔ 279276(stupid) on D112 (reciprocal); 279273(wise) → 279275(fool) on D112 — the wise, fool and stupid welded together in one death-levelling verse.
- **Teaching ↔ wisdom weld (Psa 51:6):** 279760(teach) → 279762(wisdom) on D107 target; 279762(wisdom) → 279760(teach) on D112 coupling; 279760 → 279758 on D112 (`truth in the inward being`). The only place teach and wisdom are *linked*, not merely co-listed.
- **Fool-in-heart chain (Psa 53:1):** 279881 → 279883 on D104 seat and D108 manner (`the heart`); 279881 → 279886 on D112 (`issues in corruption`).
- **Wisdom → understanding (Psa 49:3):** 279379 → 279382 on D112.
- **Brutishness → ignorance (Psa 73:22):** 282431 → 282432 on D112.
- **Counsel → friend / worship (Psa 55:14):** 280068 → 280067 (D108 manner), → 280066 (D112 coupling).
- **Discipline → the wicked's hatred (Psa 50:17):** 279537 → 279536 on D112.
- **Folly known → wrongs done (Psa 69:5):** 281878 → 281877 on D106 (God knows), → 281879 on D112.
- **Foolish confidence → boasts (Psa 49:13):** 279302 → 279304 on D112.
- **Foolish people → name/scoff (Psa 74:18):** 282584 → 282579 (D103 source), → 282586 (D106 revile), → 282588 (D107 name), → 282532 (D112). The richest single node.

**Network shape:** sparse, local, undirected (`direction:null` throughout). Only three edges join two *family* terms to each other (fool↔stupid, wise→fool, teach↔wisdom); the rest reach out to non-family co-text spans. Convergence in this family is therefore by **keyword grouping, not by linked evidence**.

---

## 4. The interior anatomy the data actually names

Assembling only filled seats / source / couplings:
- **Seat:** the interior is localised **only to the heart** — `the secret heart` (Psa 51:6, wisdom implanted + God's teaching: 279762, 279760) and `the heart` (Psa 53:1, the fool's denial: 279881). Wisdom-received and folly-as-denial both seat in the heart; nothing else in the family is given an organ.
- **Source (D103):** named once — Psa 74:18 · 282584 (the foolish enemy "whom God is asked to remember"). The *origin* of wisdom or folly is otherwise structurally unrecorded.
- **Locus (D116, corrected):** overwhelmingly `internal:ib-state`; `internal:heart` twice (279762, 279760); **`external:god`** on the three lamad-learn spans (272023/272036/272050 — learning directed outward to God's word); **`external:person`** twice (Psa 78:5 · 283270 teaching father→child; Psa 55:14 · 280068 intimate counsel). So the anatomy the data draws: wisdom/folly *seated inwardly (heart)*, teaching/learning *reaching outward* to God's word or to another person.
- **Couplings that recur as a real motif:** wisdom is coupled to *the fear of the LORD* (Psa 111:10 · 270575) and to *the heart/understanding* (Psa 49:3, 90:12); folly is coupled to *corruption / wrongs / sinful ways / boasts* (Psa 53:1, 69:5, 107:17, 49:13). Wisdom binds upward to reverence; folly binds downward to deed.

---

## 5. What could not be derived from this source

- **No intensity, specifier, effect, or prohibition** anywhere (D109/D110/D111/D113 absent on all 41) — the file records *what* the movement is but not its degree, its outcome, or any proscription.
- **Source (D103) missing on 40/41** — the mover/origin of wisdom-gain or folly is not structurally captured except at Psa 74:18.
- **Seat unstated on 38/41; manner on 36/41** — the interior *location* and *mode* of these movements are almost never localised; only the heart, thrice.
- **13 instances (9 meanings) untyped by cluster** (§0.5) — including the whole `learn` verb-set and several `teach`/`wise` senses (H2449) and the somatic `wounds`; the cluster layer cannot place the teaching/learning verbs at all.
- **Bearer is inferential throughout** — 40+ bearer edges are `inferred` self-loops (from_span null → own id), never anchored to another span; "whose inner being" is a read, not a link. One bearer is anomalous: Psa 50:17 · 279537 · D105 `discipline (hated by the wicked)` names the *abstraction*, not a person (the real IB-bearer is the wicked who hate it).
- **No cross-passage network** — all genuine edges are intra-verse; no book-scale movement can be traced from the edge data. The 11 D112/D116 swaps (§0.1) had to be corrected before locus could be read at all.
- **Screen-0 (IB is human) holds:** no instance makes God the bearer; God appears only as arena/agent (teacher, the one who knows, the one who makes wise). Corporate/adversarial human bearers (kings Psa 2, foolish enemy people Psa 74, sailors Psa 107, the fathers Psa 106) are still human IB.

---

## Summary
`wisdom-folly-teaching` (Psalms) — **27 meanings / 41 instances**, all `poetic/wisdom`, all role=characteristic. The wisdom↔folly moral-cognitive axis is genuine and dominant (M15 6/12, M16 8/12), but the family fuses in a separate **counsel/deliberation/fellowship** strand (M17 + T2, 4 inst.) and a somatic-folly stray (Psa 38:5 wounds), plus one declared outlier (Psa 85:8 kislah → M19 Trust). Wisdom is read as *gift received, seated in the heart, bound to the fear of the LORD*; folly as *practical-atheism seated in the heart, bound to corrupt deed*; teaching/learning as the family's only *outward-reaching* (external:god / external:person) movement. The evidence is thin structurally — no intensity/effect/prohibition, source once, seat thrice, and a sparse intra-verse-only network — so family cohesion rests on keyword grouping, not linked evidence. **11 D112/D116 swaps corrected; 13 instances untyped by cluster; God never the bearer.**
