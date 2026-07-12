# Family analysis — `restoration-revival-satisfaction` (Psalms), in isolation

> Source: `verse-analysis/psalms/_base-sources/psalms__restoration-revival-satisfaction.json` (generated 2026-07-11). Scope: this one file only. 15 meanings · 19 instances · 17 passages. Every claim cites `reference · span_id · Dnnn(label)`. Discovery notes cited as D114.

Instance roster (span_id · reference · meaning · cluster · locus):
274814 Psa 17:14 satisfied · M46 · internal · 275838 Psa 23:4 comfort · M05 · internal · 275314 Psa 19:7 reviving · M45 · internal · 275597 Psa 22:11 help · M38 · internal · 279648 Psa 51:10 renew · null · internal(spirit) · 281062 Psa 63:5 satisfied · M46 · internal · 281207 Psa 65:4 satisfied · M46 · internal · 281845 Psa 69:32 revive · M25 · internal(heart) · 282248 Psa 72:13 saves · null · external · 282255 Psa 72:14 redeems · null · external · 282317 Psa 72:4 give-deliverance · null · external · 306652 Psa 72:12 delivers · null · external · 271503 Psa 119:147 cry-for-help · null · external(god) · 271894 Psa 119:50 comfort · M33 · internal · 282951 Psa 77:2 comforted · M05 · internal · 283124 Psa 78:29 filled · M46 · internal · 283825 Psa 81:16 satisfy · M46 · internal · 284323 Psa 86:17 comforted · M05 · internal · 284472 Psa 88:3 full · M46 · internal.

---

## 0. Data-integrity screen (done first)

**D112(coupling)/D116(locus) field-swap — NONE.** In all 19 instances the order is correct per the method: D116(locus) holds a code (`internal:ib-state`, `internal:spirit` @ Psa 51:10 · span 279648 · D116(locus), `internal:heart` @ Psa 69:32 · span 281845 · D116(locus), `external:person`, `external:god` @ Psa 119:147 · span 271503 · D116(locus)) and D112(coupling) holds a prose phrase (e.g. Psa 63:5 · span 281062 · D112(coupling) = "issues in joyful praise"). No instance is transposed. The file is clean on this axis.

**Self-loop "edges" are not network links.** Every instance carries D105(bearer) and (where "none") D107(target)/D108(manner)/D112(coupling) edges of `item_type:"flag"`, `resolution:"inferred"`, `from_span:null`, `to_span` = the span's own id. These are self-loops, not links (e.g. Psa 23:4 · span 275838 · D105/D107/D112 all point to 275838). They are excluded from the network.

**Genuine cross-span edges (resolution `span`, to a different span) — 18, but only ONE stays in-file.** All target spans lie *outside* this file's 19 instances, except one: Psa 72:14 · span 282255 · D112(coupling) → **282248** (= the "saves" instance, Psa 72:13, in-file). So the file's declared network is almost entirely outward-pointing; the interior graph cannot be reconstructed from this source alone (see §3).

**D104(seat) / D108(manner) = "none".** Seat unfilled in **15/19** (filled only at Psa 77:2 · span 282951 "the soul (nephesh)"; Psa 63:5 · span 281062 "the soul"; Psa 51:10 · span 279648 "within me (the spirit)"; Psa 69:32 · span 281845 "the heart"). Manner unfilled in **12/19** (filled at spans 282951, 281062, 281207, 306652, 282255, 279648, 281845).

**Absent dimensions (across all 19 instances):** D103(source), D109(intensity), D110(specifier), D111(effect), D113(prohibition) — never recorded. Present dimensions only: 101,102,104,105,106,107,108,112,114,115,116. Note D103(source) is one the method asks for; it is entirely underivable here (movers appear only inside D106 operation prose).

**Cluster NULL / T2.** No T2. NULL cluster in **6 instances / 6 meanings**: Psa 72:12 · span 306652 (delivers, H5337); Psa 72:4 · span 282317 (give-deliverance, H3467); Psa 119:147 · span 271503 (help/shava, H7768); Psa 72:14 · span 282255 (redeems, H1350); Psa 51:10 · span 279648 (renew, H2318); Psa 72:13 · span 282248 (saves, H3467). The term-cluster cannot type these.

**Outliers (is_outlier=true; note says family expects M38 Salvation).** 4 meanings / 6 instances: M05 Love — comfort/nacham (Psa 23:4·275838, Psa 77:2·282951, Psa 86:17·284323); M33 Peace — comfort/nechamah (Psa 119:50·271894); M25 Life — revive/chayah (Psa 69:32·281845); M45 Transformation — reviving/shuv (Psa 19:7·275314). The expected cluster **M38 Salvation actually occurs only once** — Psa 22:11 · span 275597 (help/azar) — and there it names *absence* of help, not salvation delivered.

---

## 1. Coherence check — the label FUSES distinct movements

The family label "restoration-revival-satisfaction" does **not** name one inner-being movement. The term-clusters scatter (M05, M33, M46, M38, M25, M45, null) and the senses fall into **four separable movements**, one of which is not interior at all:

1. **Satiety / fullness** (saba, H7646) — 6 instances, all M46 Abundance: Psa 17:14·274814, Psa 63:5·281062, Psa 65:4·281207, Psa 78:29·283124, Psa 81:16·283825, Psa 88:3·284472. Interior fullness — but **double-valued** (see §2.1).
2. **Comfort / consolation** (nacham/nechamah, H5162/H5165) — 4 instances, M05/M33: Psa 23:4·275838, Psa 77:2·282951, Psa 86:17·284323, Psa 119:50·271894. Soothing of grief, distinct from satiety of desire.
3. **Revival / renewal** (chayah H2421, shuv H7725, chadash H2318) — 3 instances, M25/M45/null: Psa 69:32·281845, Psa 19:7·275314, Psa 51:10·279648. The interior brought back to life / re-made — the truest fit to "revival/restoration".
4. **Deliverance / rescue** (natsal H5337, yasha H3467×2, gaal H1350, azar H5826, shava H7768) — 6 instances: Psa 72:12·306652, Psa 72:4·282317, Psa 72:13·282248, Psa 72:14·282255, Psa 22:11·275597, Psa 119:147·271503. **Four of these are external royal acts** (Psa 72 king verbs, D116(locus)=`external:person`) — the king delivering/saving/redeeming others, not an interior state. They enter the family only by the English keyword net.

**First-class finding:** the grouping fuses interior *satiety* (M46), interior *consolation* (M05/M33), interior *revival* (M25/M45), and largely *external deliverance-action* (Psa 72, null clusters). Only movement 3 (and arguably the God-ward pole of 1) matches the "revival/restoration" intent; the Psa 72 deliverance verbs are the weakest members (external locus, king-as-bearer).

---

## 2. The movements evidenced

### 2.1 Satiety / fullness (saba) — a double-valued interior

D102(type) = affect/status/state; bearer human. The verb runs the full moral range:

- **Filled by God (positive):** Psa 63:5 · span 281062 — "My soul will be SATISFIED as with fat and rich food" (D102=status; D104(seat)="the soul"; D114 "desert-longing turned to banquet-satisfaction"); Psa 65:4 · span 281207 — "We shall be SATISFIED with the goodness of your house" (D107(target)="with the goodness of God's house"; D108(manner)="with the holiness of his temple"); Psa 81:16 · span 283825 — "with honey from the rock I would SATISFY you" (D105(bearer)="you (Israel)"; the fullness withheld only by their refusal, D114).
- **Bounded by this life (contrast):** Psa 17:14 · span 274814 — "the worldly SATISFIED with this life" (D102=affect; D107(target)="this-life-satisfaction"; D114 "a satisfaction that stops at the grave"). Bearer = "men of the world" (D105) — a foil, not the devout IB.
- **Satiety under judgment / of grief (inverted):** Psa 78:29 · span 283124 — "they ate and were well FILLED, for he gave them what they craved" (D114 "the sated appetite God granted even in displeasure"); Psa 88:3 · span 284472 — "my soul is FULL of troubles" (D106(operation)="be sated / glutted"; D107(target)="with troubles"; D114 "satiety of suffering"). Same lexeme, opposite interior.

So "satisfaction" is not a single good state: the file records satiety-by-God, satiety-by-the-world, and satiety-by-grief under one term (H7646).

### 2.2 Comfort / consolation (nacham)

- **Consolation received:** Psa 23:4 · span 275838 — "your rod and staff COMFORT me" (D102=affect; D106(operation)="a felt consolation from God's guiding, protecting nearness"; D114 "the very instruments of guidance and defence become a source of comfort"); Psa 86:17 · span 284323 — "you... have helped me and COMFORTED me" (D107(target)="by God"; D112(coupling)="paired with being helped"); Psa 119:50 · span 271894 — "This is my COMFORT in my affliction, that your promise gives me life" (D102=state; consolation from the promise).
- **Consolation refused (negative pole):** Psa 77:2 · span 282951 — "my soul refuses to be COMFORTED" (D104(seat)="the soul (nephesh)"; D108(manner)="withheld / declined"; D112(coupling)="the comfort the soul refuses"; D114 "comfort named only to be declined — the shape of unassuageable grief"). The one instance with a filled seat *and* a filled negative manner — the richest comfort record in the file.

### 2.3 Revival / renewal — the label's true core

- Psa 19:7 · span 275314 (H7725 shuv, M45) — "the law of the Lord... REVIVING the soul" (D106(operation)="the perfect law of the LORD revives/restores the soul"; D114 "the word acts on the soul the way food acts on a faint body"). Passage anchor.
- Psa 69:32 · span 281845 (H2421 chayah, M25) — "let your hearts REVIVE" (D104(seat)="the heart"; D108(manner)="in the heart"; D105(bearer)="those who seek God"; D114 "drooping faith quickened again").
- Psa 51:10 · span 279648 (H2318 chadash, null) — "RENEW a right spirit within me" (D104(seat)="within me (the spirit)"; D116(locus)=`internal:spirit`; D107(target)="a right / steadfast spirit"; D114 "the will re-established toward God after collapse"). The only `internal:spirit` locus in the file.

These three name the mover as God's word / God's re-creating act, and the seat as soul→heart→spirit — the clearest interior "restoration" data in the source.

### 2.4 Deliverance / rescue — mostly external royal action

- **Psa 72 king cluster (external:person, bearer="the king", D102=action):** delivers Psa 72:12·306652 (natsal; D107(target)="the needy who calls"); give-deliverance Psa 72:4·282317 (yasha; D107="the children of the needy"); saves Psa 72:13·282248 (yasha; D107="the lives of the needy"; passage anchor); redeems Psa 72:14·282255 (gaal; D107="their life, from oppression and violence"; D114 "the highest reach of royal mercy"). These are outward acts *toward* others — characteristic of the king as agent, not interior movements of his IB.
- **Interior/God-ward members:** Psa 22:11 · span 275597 (azar, M38) — "there is none to HELP" (D102=state; D106(operation)="utter isolation"; D107(target)="helplessness"; D114 "every human support has failed"). This is the sole M38 Salvation instance and it names the *lack* of help. Psa 119:147 · span 271503 (shava, null) — "I rise before dawn and CRY for help" (D102=action; D116(locus)=`external:god`; interior-driven cry directed outward).

---

## 3. The network (genuine pair/event edges only)

Method rule applied: keep only edges with `resolution:"span"` linking to a *different* span; drop self-loop flags. Result — **18 genuine directed edges, of which 17 exit this file's scope**; the interior graph is therefore not reconstructable from this source.

**The single in-file edge:** Psa 72:14 · span 282255 (redeems) — D112(coupling) → **282248** (saves, Psa 72:13, in-file). Redemption is bound to the saving act within the Psa 72 king portrait.

**Edges exiting scope (to spans not carried in this file):**
- Psa 77:2·282951: D104(seat)→282949; D106(operation)→282950; D112(coupling)→282950.
- Psa 63:5·281062: D104(seat)→281061; D105(bearer)→281061; D112(coupling)→281066.
- Psa 65:4·281207: D107(target)→281208; D108(manner)→281210; D112(coupling)→281202.
- Psa 72:12·306652: D107(target)→306653; D112(coupling)→**282244**.
- Psa 72:13·282248: D107(target)→282249; D112(coupling)→**282244**.
- Psa 72:4·282317: D107(target)→282319; D112(coupling)→282320.
- Psa 51:10·279648: D104(seat)→279650; D107(target)→279650; D112(coupling)→279645.
- Psa 69:32·281845: D104(seat)→281844; D108(manner)→281844; D112(coupling)→281841.

**Shared external anchor:** span **282244** (out of file, presumably the Psa 72:13 "pity" clause) is the coupling target of *both* delivers (306652) and saves (282248) — the pivot of the king's compassion, but it is not present in the source, so its content is underivable here.

Network verdict: **sparse and outward**. The only intra-family link is redeems→saves within Psa 72. The remaining 8 meanings (single-instance, or with self-loops only) contribute *no* network edges (e.g. all comfort instances except Psa 77:2 carry self-loops only; Psa 19:7 reviving, Psa 88:3 full, Psa 78:29 filled, Psa 81:16 satisfy, Psa 22:11 help, Psa 119:147 cry, Psa 119:50 comfort — self-loops only).

---

## 4. The interior anatomy the data actually names

Filled seats (D104), the only named interior locations:
- **soul / nephesh** — Psa 77:2·282951 (comfort refused), Psa 63:5·281062 (satisfied).
- **spirit** — Psa 51:10·279648 ("within me", `internal:spirit`), renewed.
- **heart** — Psa 69:32·281845 (revived), `internal:heart`.

Loci (D116): 14 instances `internal:ib-state` (undifferentiated interior), 1 `internal:spirit`, 1 `internal:heart`, 4 `external` (Psa 72 ×3 `external:person` + Psa 119:147 `external:god`). Wait-note: Psa 72:14 redeems and 72:12 delivers, 72:13 saves, 72:4 give-deliverance = the four `external:person`; Psa 119:147 = `external:god`. So **5 instances are non-interior in locus** — the anatomy of these is "not in the inner being" by the file's own coding.

Role (D115): **all 19 = "characteristic"** — no qualifier, no standalone. The file asserts every item as a characteristic even where the locus is external (the Psa 72 king acts), which sits in tension with §1's finding that those are outward acts.

Type spread (D102): state 8 · action 6 · status 3 · affect 2. No disposition/faculty/volition/cognition recorded. The interior here is read as **state/status** (satiety, comfort, revival, fullness) plus **action** (the deliverance verbs + cry + renew-petition).

Movers, where derivable, sit only inside D106(operation) prose, never as D103(source): God's rod/staff (Psa 23:4), the perfect law (Psa 19:7), God giving the craved food (Psa 78:29), God's re-creating word (Psa 51:10). The "what moves it" is real in the notes but structurally uncaptured.

---

## 5. What could not be derived from this source

- **D103(source) — entirely absent.** No instance records what originates the movement; only D106 prose gestures at it. The agent behind restoration (God, his word, his instruments) is uncoded.
- **D109(intensity), D110(specifier), D111(effect), D113(prohibition) — absent in all 19.** No graded intensity, no specifier, no downstream effect, no prohibition anywhere in the family.
- **The network is unrecoverable within scope.** 17 of 18 genuine edges point to spans not carried in the file (incl. the shared anchor 282244); their content cannot be read here.
- **6 instances carry NULL clusters** (delivers, give-deliverance, saves, redeems, renew, cry-for-help) — the term-cluster cannot type them; their family placement rests on the meaning-keyword net alone.
- **15/19 seats and 12/19 manners are "none"** — the interior location and mode are unstated for most of the family.
- **5 instances are non-interior by locus** (4 `external:person`, 1 `external:god`) yet coded role="characteristic"; whether they belong in an inner-being family is a coding tension the file does not resolve.
- **The expected cluster (M38 Salvation) is essentially unattested** — 1 of 19 instances, and that one names the *absence* of help (Psa 22:11·275597).

---

## Summary

`restoration-revival-satisfaction` is a **keyword-fused family, not one movement**: it braids interior *satiety* (saba/M46, 6 — itself double-valued: filled-by-God vs. filled-by-world vs. filled-with-grief), interior *consolation* (nacham/M05·M33, 4 — incl. comfort refused), interior *revival/renewal* (chayah/shuv/chadash, 3 — the label's true core), and largely *external royal deliverance* (Psa 72 verbs, null clusters, 4 — outside the inner being by their own locus). Data is clean on the D112/D116 axis (no swaps) but thin on structure: D103 and D109–D113 wholly absent, 15/19 seats "none", the network all but one edge exiting scope, and the nominal cluster M38 attested once (as *lack* of help). The strongest interior anatomy the source names is the **soul→spirit→heart** re-vivified by God's word (Psa 19:7, 51:10, 69:32); the Psa 72 deliverance verbs are the family's weakest, external-locus members.
