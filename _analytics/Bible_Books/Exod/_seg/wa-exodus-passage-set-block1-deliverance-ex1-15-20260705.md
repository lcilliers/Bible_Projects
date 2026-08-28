# Exodus passage-set — Block 1: Bondage, Call & Deliverance (Ex 1:1–15:21) — FOR REVIEW

- **Date:** 2026-07-05
- **Step:** 2–3 of the workflow (cast passage width → set passages). **Not yet loaded; not yet analysed.** Awaiting boundary review — and a data-readiness step (below) — before creating `segment_unit`s and reading.
- **Method:** identical to the Genesis narrative pipeline — each passage holds a whole **operation-web**, boundary set *where the web closes*, anchored on the non-T2 evidence verses; thin/formulaic stretches get a thin unit or fold as context. Governed by the same gate (`_check_passage_reading_coverage_v1`) and distinction-preservation discipline.
- **Provenance (on load):** `exodus-deliverance-v1-20260705`.
- **Versification:** DB uses **English** (ESV_th) versification (e.g. 8:1 "let my people go that they may serve me"). Ranges below are English.

---

## ⚠ Two things differ from Genesis — please note before we start

1. **Data-readiness / backfill needed (blocker for the *reading* phase).** Exodus is **term-sparse in the `verse` table**: only **793 of 1,213 verses present (420 missing)** — the context verses with no study anchor, exactly as Genesis needed before its readings. **The STEP local server is currently unreachable** (`http://localhost:8989` returned no response), and the backfill script (`_apply_backfill_chapter_verses_v1`) fetches from STEP. So: casting/loading/coverage-checking can proceed off the anchor spans, **but the passage *readings* cannot run until Ex 1–15 is backfilled, which needs STEP back up.** Please start the STEP server when convenient; I'll backfill then.
2. **Genre terrain — Exodus is not all narrative.** The non-T2 density scan (filed alongside) shows chs **1–24 and 32–34 are narrative-rich**, but the **tabernacle chapters (25–27, 35–40) are thin** (5–14 spans each) — construction/instruction lists, the Exodus analogue of Genesis genealogies. Block 1 (this doc) is **all narrative**; the thin material is a later-block scope question (see the block plan below).

---

## Passages (20) — Block 1, Ex 1:1–15:21

| # | Code | Span | Operation-web it holds | Key anchors (gloss) |
|---|---|---|---|---|
| 1 | EXO-01-oppression | 1:1–14 | The multiplying people and the fearful king; affliction and bitter service. | 1:7,12 multiply (`ravah`); 1:8 know (`yada`); 1:10 hate (`sane`); 1:11,12 afflict (`anah`); 1:13,14 serve (`avad`/`avodah`); 1:14 bitter (`marar`)/severe (`qasheh`) |
| 2 | EXO-02-midwives-fear-god | 1:15–22 | **The midwives who feared God above the king** — reverence overriding the death-decree. | 1:17,21 fear (`yare`); 1:16 live (`chayah`); 1:20 be-good (`yatav`) |
| 3 | EXO-03-moses-born-drawn-out | 2:1–10 | The fine child hidden; the pity at the weeping baby; drawn out. | 2:2 pleasant (`tov`); 2:6 spare/pity (`chamal`)/weep (`bakhah`); 2:10,11 grow (`gadal`) |
| 4 | EXO-04-flight-to-midian | 2:11–22 | Moses' violence and fear; the struggling Hebrews; flight and a content dwelling. | 2:13 struggle (`natsah`)/wicked (`rasha`); 2:14 fear (`yare`)/judge (`shaphat`)/know (`yada`); 2:15 seek (`baqash`); 2:21 be-willing (`yaal`) |
| 5 | EXO-05-god-hears-burning-bush | 2:23–25 + 3:1–22 | **God hears the groaning and remembers the covenant; the holy ground; the call; I AM.** | 2:24 remember (`zakhar`)/covenant (`berit`); 2:24,25 hear (`shama`)/know (`yada`); 3:5 holiness (`qodesh`); 3:6 fear (`yare`); 3:7 affliction (`oni`)/pain (`makhov`); 3:12 serve (`avad`) |
| 6 | EXO-06-objections-signs | 4:1–17 | Will they believe? the three signs; Moses' reluctance and God's kindled anger. | 4:1,5,8,9 believe (`aman`); 4:8 sign (`ot`); 4:14 incensed (`charah`)/rejoice (`samach`)/heart (`lev`) |
| 7 | EXO-07-return-believe | 4:18–31 | The return; harden-heart foretold; the bridegroom of blood; the people believe and bow. | 4:21 harden (`chazaq`)/heart (`lev`); 4:23 serve (`avad`); 4:31 hear (`shama`)/believe (`aman`)/affliction (`oni`) |
| 8 | EXO-08-bricks-without-straw | 5:1–21 | "Who is the LORD that I should obey?"; the increased burden; the officers' despair. | 5:2 know (`yada`)/obey (`shama`); 5:9 deception (`sheqer`); 5:16 sin (`chata`); 5:21 stink (`baash`)/judge (`shaphat`) |
| 9 | EXO-09-i-am-the-lord | 5:22–23 + 6:1–30 + 7:1–7 | **I AM the LORD; the covenant remembered; "I will redeem"; the people would not listen.** (6:14–27 genealogy — thin, lifespans only.) | 5:22 be-evil (`raa`); 6:4,5 covenant (`berit`); 6:5 remember (`zakhar`); 6:6 judgment (`shephet`); 6:9 listen (`shama`)/severe (`qasheh`) |
| 10 | EXO-10-serpent-nile-blood | 7:8–25 | The staff-serpent sign; the hardened heart begins; the Nile to blood. | 7:11 wise (`chakham`); 7:13,22 heart (`lev`)/harden (`chazaq`); 7:18,21 stink (`baash`) |
| 11 | EXO-11-frogs-gnats | 8:1–19 | Frogs and gnats; Pharaoh pleads then hardens; "the finger of God". | 8:8,9 pray (`atar`); 8:8 remove (`sur`); 8:15 heart (`lev`)/heavy (`kaved`); 8:19 harden (`chazaq`) |
| 12 | EXO-12-flies-livestock-boils | 8:20–32 + 9:1–12 | Flies, livestock, boils; the distinction of Goshen; the deceitful plea; the heart heavy. | 8:23 sign (`ot`); 8:28 pray (`atar`); 8:32,9:7 heart (`lev`)/heavy (`kaved`); 9:12 harden (`chazaq`) |
| 13 | EXO-13-hail | 9:13–35 | **"That you may know none like me"; those who feared the word; "I have sinned" that is not repentance.** | 9:14 heart (`lev`); 9:20,30 fear (`yare`); 9:27 sin (`chata`)/righteous (`tsaddiq`)/wicked (`rasha`); 9:34,35 heavy (`kaved`)/harden (`chazaq`) |
| 14 | EXO-14-locusts-darkness | 10:1–29 | Locusts and darkness; "how long will you refuse to humble yourself?"; the heart God hardens. | 10:1 heavy (`kaved`); 10:3 humble (`anah`); 10:16 sin (`chata`); 10:17 pray (`atar`); 10:20,27 harden (`chazaq`) |
| 15 | EXO-15-final-warning | 11:1–10 | The final warning; favor in Egypt's eyes; the heart hardened to the last. | 11:3 favor (`chen`)/give (`natan`); 11:8 burning (`chori`); 11:10 heart (`lev`)/harden (`chazaq`) |
| 16 | EXO-16-passover-instituted | 12:1–28 | The Passover lamb and the blood; the memorial to keep; teaching the children. | 12:5 unblemished (`tamim`); 12:13 destruction (`mashchit`); 12:16 holy (`qodesh`); 12:17,24,25 keep (`shamar`); 12:26 service (`avodah`) |
| 17 | EXO-17-firstborn-exodus-plunder | 12:29–51 | The death of the firstborn; the driving out; the plunder of Egypt. (12:43–51 ordinance — thin tail.) | 12:31 summon (`qara`)/serve (`avad`); 12:33 urgent (`chazaq`); 12:35,36 ask (`shaal`)/favor (`chen`)/give (`natan`) |
| 18 | EXO-18-consecrate-strong-hand | 13:1–16 | Consecrate the firstborn; remember this day; redeem; the strong hand. | 13:2 consecrate (`qadash`); 13:3 remember (`zakhar`); 13:13,15 ransom (`padah`); 13:14,16 strength (`chozeq`) |
| 19 | EXO-19-red-sea | 13:17–22 + 14:1–31 | **The pillar; the pursuit; fear then faith; "stand still, the LORD will fight"; the crossing.** | 13:17 relent (`nacham`); 14:4,8,17 heart (`lev`)/harden (`chazaq`); 14:10,13,31 fear (`yare`); 14:14 be-quiet (`charesh`); 14:31 believe (`aman`) |
| 20 | EXO-20-song-of-the-sea | 15:1–21 | **The song of triumph; the divine warrior; steadfast love; the nations' terror; Miriam.** | 15:1,21 rise-up (`gaah`); 15:2 strength (`oz`); 15:11 awesome (`yare`)/holiness (`qodesh`)/wonder (`pele`); 15:13 kindness (`chesed`); 15:16 terror (`emah`)/dread (`pachad`) |

---

## The recurring interior operations Block 1 will surface (let them emerge — do NOT impose)

- **The hardened heart** — the book's spine motif: `lev` welded to **`chazaq`** (*strengthen/make firm*) and **`kaved`** (*make heavy*), across every plague (7:13,22; 8:15,19,32; 9:7,12,34,35; 10:1,20,27; 11:10; 14:4,8,17). The *distinction between* "Pharaoh hardened his own heart" and "the LORD hardened Pharaoh's heart" — and between `chazaq` and `kaved` — is the finding, never to be lumped.
- **`avad` — serve/slave/worship** — the pivot of the whole block: the *same word* is Israel's *slavery to Pharaoh* (1:13,14; 5:18) and their *worship of God* ("let my people go that they may **serve** me", 3:12; 4:23; 7:16; 8:1…). The exodus is a *transfer of service* — from Pharaoh to God.
- **God who hears, remembers, knows, sees** — `shama`/`zakhar`/`yada` + the groaning (`neaqah`/`anach`/`zaaq`) and affliction (`oni`/`anah`): the divine regard that *initiates* the deliverance (2:23–25; 6:5).
- **The fear-of-God vs the fear-of-man** — the midwives (1:17,21), Moses (2:14; 3:6), the God-fearers in the hail (9:20,30), and Israel at the sea (14:31) — over against Pharaoh who *will not* fear.
- **Believe** — `aman`: will Israel *believe*? (4:1,5,8,9,31; 14:31 — faith at the sea).
- **The register of worship** — the Song of the Sea (15): triumph (`gaah`), the divine warrior, `chesed`, and the nations' `emah`/`pachad` — worship as the interior's *response* to deliverance.

---

## Coverage note

Every **non-T2 evidence verse** in Ex 1:1–15:21 falls inside a passage above; the ranges are **contiguous** from 1:1 to 15:21 (validated: 210 non-T2 span-verses, **0 gaps**). Three units cross a chapter boundary where the operation-web does (EXO-05 2:23→3; EXO-09 5:22→7:7; EXO-19 13:17→14). A formal `0 non-T2 gaps` check re-runs after load (post-backfill), before any reading.

---

## The overall Exodus block plan (for orientation — only Block 1 is cast here)

Genesis was read in 3 blocks (primeval / Abraham / Jacob). Exodus naturally divides into **5**:

| Block | Range | Character | Cast? |
|---|---|---|---|
| **1. Bondage, Call & Deliverance** | 1:1–15:21 | narrative-rich (this doc, 20 passages) | ✅ cast — under review |
| **2. Wilderness & Sinai Covenant** | 15:22–24:18 | narrative + the Decalogue/Book-of-the-Covenant (law with inner-being content: coveting, the sojourner's heart, justice) | later |
| **3. Tabernacle instructions** | 25:1–31:18 | **thin** (instruction lists); inner-being nodes = the *willing heart* (25:2), Bezalel *filled with the Spirit* (31:1–11), the *Sabbath* (31:12–17) | later — likely few thin units, much skipped-with-rationale |
| **4. Golden Calf & Renewal** | 32:1–34:35 | narrative-rich (apostasy, Moses' intercession, "show me your glory", the renewed covenant) | later |
| **5. Tabernacle construction** | 35:1–40:38 | **thin** (execution lists); nodes = *willing-hearted giving* (35:5,21–29), Bezalel, the *glory fills the tabernacle* (40:34–38) | later — thin |

The thin tabernacle blocks (3, 5) are where the **genre scope question** lands — whether to read the few inner-being nodes as thin units (like Genesis genealogies) or handle them differently. **That is a decision for when we reach them**, not now.

---

*Filed 2026-07-05 for boundary review. On approval **and** STEP back up: backfill Ex 1–15 → load via `_apply_load_segmentation_v1` → verify 0 non-T2 gaps → read EXO-01… passage-by-passage with the gate → commit every 2–3 → synthesis. Density scan: `scratchpad/exodus_readiness.py` output (to be filed with the reading reports).*
