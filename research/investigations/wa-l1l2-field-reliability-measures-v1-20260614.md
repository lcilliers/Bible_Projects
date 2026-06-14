# L1/L2 fields — reliable measures, what's needed, expected answer

> **Investigation · v1 · 2026-06-14.** Records the discussion that reframed the L1/L2 reliability problem, then works through each of the 14 verse-extraction fields: *what it is · what is needed to arrive at the answer (its reliable measure[s]) · the expected answer.* Read-only design analysis; no DB change.

## 1. The discussion, recorded

**The impasse.** The study is a decompose strategy: whole (inner being) → pieces (words) → verses. The *decomposition* into structured per-verse facts held — where the verse-read ran, the findings are verse-resolved and trace back to a term + verse. What failed was the *re-composition*: pulling the pieces back into the full interdependent web of meaning, exhaustively and as generated prose. That web can't be held, traced both ways, and kept consistent by a single human or AI pass — the meaning paragraphs read well *because* they were narrated, not derived, which is exactly why they couldn't be traced back. The run was also too slow and costly to ever finish (≈5–7 h per cluster; 3 of ~46 done; M02's run never completed), with duplicated layers (1,224 term-in-verse units carrying both `l2_mechanical` and `l2_api`) and ~30k findings redone.

**The reframe (the key move).** "Sense" looked like an irreducible judgment — but deciding *pneuma* = wind vs Holy Spirit is done by **combining the node with other nodes in the verse** (the governing verb, the co-occurring terms, the setting). So **sense is not a property *of* the node — it is a property of the combination of nodes; it lives on the edges, not in the node.** That collapses the "mechanical facts vs interpretive meaning" split: **the meaning emerges from the web of facts.** Sense and the web are the same operation.

**The consequence — reliability = derivability from named measures = traceability.** A finding is reliable exactly to the degree it is **derived from named, present measures** (facts/nodes). When it is, the measures *are* the trace — you can show which facts forced the answer (*pneuma* = Holy-Spirit **because** of these nodes). That is the thing the generative meaning never had. The neighbourhood that decides a field is **local and bounded** (a verse / small passage), and **joint** (a node's sense and its neighbour's sense settle together) — so it is a *constraint problem over a small graph*, not narration of the whole web.

**The strata that fall out.** The 14 fields are not one thing. Each sits in one of four reliability strata by the *kind* of measure it needs:
- **Bedrock fact** — one mechanical signal (morphology, book, lexical structure). Definitive now.
- **Node-combination** — derived from the deciding node(s) present in the verse/passage. Reliable where the node is in reach; traceable to it.
- **Sense-dependent** — derived from the *resolved* sense, so only as reliable as the sense.
- **Out-of-reach residue** — needs the narrative/passage/canon beyond the local node-graph; the genuinely hard ones.

## 2. The 14 fields

> Each is produced per **typed term-in-verse**. "What is needed" names the **measure(s)** that make the finding reliable, tagged with its stratum. "Expected answer" is the value space.

| # | Field — what it is | What is needed to arrive at the answer (the reliable measure[s]) | Expected answer |
|---|---|---|---|
| **1** | **sense_applied** — which STEP sense the term carries *here* | **[node-combination, joint]** the term's STEP **sense-set** (candidate space) **+** the **disambiguating neighbour-nodes** — governing verb, co-occurring terms and their senses, syntactic role, literary setting, sometimes a surrounding verse. Reliable where a neighbour decides; residue where none in reach does | one clean sense phrase from the term's listed senses (or: flagged ambiguous) |
| **2** | **type** — act / disposition / quality | **[bedrock]** the term's **morphology** (part-of-speech / form): verb→action, abstract noun→quality/status, participle/adjective→status. *(status-vs-quality split may need the resolved sense)* | `action` · `status` · `quality` |
| **3** | **compound** — simple or made of parts | **[bedrock — lexical]** the term's **lexical/etymological structure** (is the form a compound, e.g. *makros*+*thumos*) — a term property, not verse-specific | `simple` · `compound:<parts>` |
| **4** | **mode** — operative form + manner here | **[bedrock]** the verse's **morphology** (stem/binyan, voice, tense) for the form; **[node-combination]** the context/direction/level nuance from the verse | short mode phrase (form + manner) |
| **5** | **constitutional_location** — where it's located here | **[node-combination]** an explicit **seat/body node co-occurring** in the verse (*lev*/heart, *ruach*/spirit, *nephesh*/soul, mind, a named organ); keyword-seeded, read-confirmed; silence = NONE | `spirit · soul · heart · mind · other-soul:<x> · body-part:<x> · NONE` (multi) |
| **6** | **origin** — where it comes from constitutionally | **[node-combination]** **source cues** in the verse/passage — a giving/sending verb, a divine-source node, a generational marker, an internal-generation cue; absent ⇒ not-stated | `within-person · received-from-outside · bestowed-by-God · carried-generationally · not-stated` |
| **7** | **faculty** — which inner faculty(ies) it engages | **[sense-dependent]** the term's **resolved sense → a sense→faculty mapping** (fear-sense→affect, know-sense→cognition); per-term from lexical meaning. Only as reliable as the sense | one+ of: perception·cognition·memory·affect·creativity·volition·agency·moral-evaluation·conscience·relational · `NONE` (multi) |
| **8** | **attributed_to_God** — is it predicated of God here | **[node-combination]** the verse's **subject/possessor node** — is God the one who acts/owns/extends the term (a divine-subject or "of God/LORD" node) | `yes` · `no` (+ how-note) |
| **9** | **purpose_equips** — what it equips the person to be/do/become | **[residue / passage-dependent]** a **purpose/result clause** in the verse or surrounding passage ("so that / in order to", or the narrative outcome); interpretive; absent ⇒ not-stated | purpose phrase · `not-stated` |
| **10** | **typology_direction** — typological direction if any | **[residue — canonical]** a **typological signal** (term applied to God vs human as pattern) **+** canonical/theological context beyond the local graph; no signal ⇒ none | `human→divine · divine→human · none` |
| **11** | **immediate_response** — first inner-being response here | **[passage-dependent / node-combination]** a **response node** in the verse/passage (the reaction shown — a following verb/state); absent ⇒ SILENT | response phrase · `SILENT` |
| **12** | **produces_effect** — what it produces in the inner being here | **[residue / passage-dependent]** an **effect/result node** — what follows from it in the verse/passage narrative | effect phrase |
| **13** | **relational_implication** — directional/relational force it carries | **[node-combination]** the **relational structure** in the verse — who/what the term orients toward (subject→object, direction) | relational/directional phrase |
| **14** | **literary_setting** — the form carrying the verse | **[bedrock + node-combination]** the **book's genre** (from book metadata = definitive) **+** **setting cues** in the passage | `narrative · poetry · law · prophecy · wisdom · epistle · gospel · apocalyptic` (+ setting: judicial/liturgical/covenantal/communal/eschatological) |

## 3. Strata summary

| Stratum | Fields | Reliability story |
|---|---|---|
| **Bedrock fact** | 2 type · 3 compound · 4 mode (form) · 14 literary-form | definitive now, from one mechanical signal (morphology / lexicon / book) |
| **Node-combination** | 1 sense · 5 location · 6 origin · 8 attributed-to-God · 13 relational-implication · 14 setting | reliable **where the deciding node is present** in the verse/passage; the node *is* the trace |
| **Sense-dependent** | 7 faculty | reliable **iff** the sense (field 1) is resolved |
| **Out-of-reach residue** | 9 purpose · 10 typology · 11 immediate-response · 12 produces-effect | need the narrative/passage/canon beyond the local node-graph — the genuinely hard ones |

## 4. Notes

- **Order matters.** The node-combination and sense-dependent fields presuppose earlier ones: field **1 (sense)** must settle before **7 (faculty)**; the **bedrock** fields (2, 3, 4, 14) are inputs available with no read. A resolution pass should run bedrock → sense → sense-dependent → residue.
- **The trace is the deliverable.** For every non-bedrock field, the reliable finding must **cite the node(s) that forced it** — that is what makes it back-trackable (the gap the generative meaning had).
- **Co-occurrence** (the verse's term-array — *which other in-scope terms share the verse*) is a **bedrock web-edge** (definitive from the spans). It is not one of the 14 but is the literal first "web string"; worth carrying as a 15th, since the whole reframe is that meaning rides on such combinations.
- **The residue is honest residue.** Fields 9–12 are where no local-node measure settles it — flag these as the cases that genuinely need the passage/canon, rather than letting a generative step invent them.
