# Verse-meaning methods — Experiment Round 1 (see them in operation)

- **File:** wa-verse-meaning-method-experiment-round1-v1-20260626.md · **2026-06-26 · Author:** Claude Code.
- **Purpose (researcher, 2026-06-26):** "I'm not knowledgeable about these methods — I want to see them in operation and test them on our use case, experiment until there's a clear winner." So: the **same real verses**, rendered each way, with plain-language notes on what each captures and misses. Hand-built from the actual span/morphology data (not a build).
- **What we're testing each method against:** (1) does it give a **control on compounds** — stop bare co-occurrence; (2) is the **meaningful border** clear (what's part of the movement vs scenery); (3) does it capture **operations morphing into each other**; (4) can a **human read it**; (5) can the **engine build it** from what we store (morph/stem/roles/gloss); (6) does it **let patterns emerge** (RESET) rather than impose a grid.

Three verses, chosen for contrast:
- **Gen 6:5** — compound-heavy (heart, thoughts, intention, evil) → tests the *border/control*.
- **Eze 36:26** — explicit *morphing* (heart of stone → heart of flesh, God-caused) → tests *operations morphing*.
- **Heb 9:14** — roles + figurative + divine binding → tests *roles, border, and the mechanical limit*.

---

## VERSE 1 — Gen 6:5
*"…every intention of the thoughts of his heart was only evil continually."*
Real spans (study terms): `saw`(H7200,T2,Qal) · `wickedness`(H7451,M27) · `intention`(H3336,M29) · `thoughts`(H4284,M14) · `heart`(H3820,M47) · `evil`(H7451,M27); scenery: Lord, that, man, great, earth, every, only, continually.

### Method A — CURRENT (flat fields + co-occurrence compounds) — the baseline
```
heart (M47)  sense=heart  type=status  faculty=(seat)
  compound: intention — partner
  compound: thoughts  — partner
  compound: evil      — partner
  compound: man       — qualifier
  compound: saw       — partner
```
**What it captures:** that these terms co-occur.
**What it misses:** *everything structural.* It can't say the heart **produces** the thoughts, whose **intention** is **morally evil**, **continually**. "partner" is applied to 5 unrelated things. **No control** — every co-occurring term is a "compound."

### Method B — MEANING GRAPH (typed, role-bound edges; function words dropped)
```
movement root: heart (M47, the seat)
  └─ produces ──▶ thoughts (M14)
        └─ has-intention ──▶ intention / yetser (M29)   ← the operation (the inclination)
              ├─ moral-colour ──▶ evil (M27)
              └─ manner ──▶ "only … continually"  (totality + perpetual)
  framing (peripheral): the LORD ─perceives▶ [this movement] ; located in: man, earth
```
**Control on compounds:** a term is in the graph only if it fills a **role** (produces / has-intention / moral-colour / manner). `man`, `great`, `earth` fill no role in the *inner* movement → **scenery**, not compounds. `saw`/`LORD` = the framing perception, marked peripheral.
**Border:** clear — `heart, thoughts, intention, evil` are nodes; `only/continually` are a manner edge; the rest is scenery.

### Method C — FRAME TEMPLATE (operation evokes a frame; fill core elements)
```
Operation frame: DEVISING/INTENTION-FORMING  (evoked by yetser/machashavah)
  CORE  Cognizer  = the heart of man        [filled]
  CORE  Content   = evil                    [filled]
  CORE  Locus     = heart (M47)             [filled]
  non-core Manner = only / continually      [filled]
  non-core Cause  = —                       [silent: verse gives none]
```
**Border:** the frame's **core slots** define what's meaningful; everything else is non-core or scenery.

> **Round-1 read on Gen 6:5:** B and C both fix the border; A doesn't. B shows the *structure* (heart→thoughts→intention→evil); C shows *completeness* (are the core slots filled). They're complementary, not rivals.

---

## VERSE 2 — Eze 36:26  (the morphing test)
*"I will give you a new heart … remove the heart of stone from your flesh and give you a heart of flesh."*
Real spans: `give`(H5414,M12,Qal) ×3 · `remove`(H5493,M30,**Hiphil**=causative) · `heart`(H3820,M47) · `spirit`(H7307) · `stone`(H0068) · `flesh`(H1320,M47).

### Method A — CURRENT (flat)
```
heart (M47): compound: remove—partner, give—partner, stone—qualifier, flesh—qualifier, spirit—co-seated
```
**Misses the entire point:** that the heart **changes from stone to flesh**. The morphing is invisible — it's just a pile of "partners/qualifiers."

### Method B+D — MEANING GRAPH with RRG/Aktionsart morphing (uses the Hebrew stem)
```
agent: God ("I will…")
  ├─ CAUSE ─▶ remove (H5493, HIPHIL=causative)
  │             └─ patient ▶ heart{quality: stone}   ─source▶ flesh(person)
  └─ CAUSE ─▶ give   (H5414, Qal, divine subject)
                └─ patient ▶ heart{quality: flesh}

  ⇒ TRANSITION (operations morphing into one movement):
        heart:  [stone] ───remove → give───▶ [flesh]
        kind = replacement/reversal · agent = God · trigger = divine promise (yiqtol "I will")
```
**Operations morphing — captured explicitly.** Two operations (`remove`, `give`) **compose into one transition** of the heart's quality (stone→flesh). The **Hiphil stem on `remove`** is the mechanical signal that God *causes* it — we already store this in `stem`. This is exactly the RRG model (`CAUSE(BECOME(...))`), and it's the thing the flat model can't see.

> **Round-1 read on Eze 36:26:** only a model with a **transition edge** + **stem-driven causation** captures the verse's actual meaning. This is the decisive case for "operations morphing."

---

## VERSE 3 — Heb 9:14  (roles + figurative + divine binding)
*"…purify our conscience from dead works to serve the living God."*
Real spans: `Spirit`(G4151,M25) · `purify`(G2511,M12) · `conscience`(G4893,M47) · `dead`(G3498,T2) · `serve`(G3000,M36) · `God`(G2316).

### Method B — MEANING GRAPH (typed edges)
```
operation: purify (M12)
  ├─ agent ──▶ Spirit (M25) / blood-of-Christ
  ├─ object ──▶ conscience (M47, seat)         ← the inner being acted ON
  ├─ source(from) ──▶ "dead works"   ⚑ FIGURATIVE (works = conduct) → DEPTH GATE
  └─ purpose(to) ──▶ serve (M36) ─object▶ God
```
**Why this beats today's data:** earlier the flat pass put faculty=conscience+moral_evaluation **on the Spirit** (proximity bleed) and asserted divine roles ungrounded. The graph **binds by role** — the Spirit is the *agent of purify*, the conscience is the *object*; the Spirit does not "operate in" the conscience. The bias we spent today cleaning **can't occur** in a role-bound graph.

### Method C — FRAME (core/non-core)
```
Frame: CLEANSING (purify)
  CORE Cleanser = Spirit/blood   CORE Affected = conscience   non-core Source = dead works
  Purpose = serve God
  ⚑ "dead works" core-Source is figurative → flagged for depth (not forced mechanically)
```
**Border + honesty:** the figurative slot is **flagged, not guessed** — matches the RESET depth-gate. The mechanical layer fills what it can; the read finishes the rest.

---

## Scorecard (Round 1)
| need | A · current flat | B · meaning graph | C · frame template | D · RRG morphing |
|---|---|---|---|---|
| control on compounds | ✗ none (co-occurrence) | ✓ role-bound | ✓ slot-bound | ✓ (within ops) |
| meaningful border | ✗ unclear | ✓ node vs scenery | ✓ core vs non-core | ◐ ops only |
| operations morphing | ✗ invisible | ◐ as transition edge | ✗ static | ✓✓ its specialty |
| human-readable | ◐ list | ✓ graph reads like the verse | ✓ checklist | ◐ formal notation |
| engine-feasible (from morph/stem/roles) | ✓ (already) | ◐ needs role assignment | ◐ needs frame inventory | ✓ stem already stored |
| lets patterns emerge (RESET) | ◐ | ✓ | ✗ risk of grid | ✓ |

**Round-1 observation (not a verdict):** the front-runner looks like a **hybrid — a meaning graph (B) whose edges are typed by role, with a first-class transition edge (D) for morphing, and frame-core (C) used as the completeness check**, not as an imposed grid. But the point of the experiment is that you now *see* them; the winner should be decided by running more verses, especially ones where these differ.

## Proposed next rounds (your steer)
- **Round 2:** a figurative/distributed case (Psa 24:4 "clean hands and a pure heart" → outcome in v.5–6) — tests the border + adjacency + depth gate hardest.
- **Round 3:** a "quiet" verse with one inner-being term and lots of scenery — tests that the control doesn't over-prune.
- **Round 4:** a verse where two methods disagree on the border, to force a decision.
- Then pick the winner and define it precisely before any build.

Tell me which verses to run next (or give me your own), and whether the hybrid above is the direction to keep pressure-testing.
