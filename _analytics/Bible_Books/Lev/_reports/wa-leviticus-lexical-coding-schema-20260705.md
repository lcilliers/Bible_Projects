# Leviticus — the lexical-coding schema (built backwards from the questions)

> **Design principle (researcher's steer, 2026-07-05):** the higher-order questions ride *on top of* the lexical study and depend on it. So the lexical analysis must **code each occurrence on a set of indicator-dimensions**, chosen so that **each question becomes a filter or cross-tab over evidence** — not a re-read. This document defines those dimensions, maps them to the questions, and shows the coding working on a cross-domain sample.

---

## Part 1 — The questions → the indicators that resolve them

| Your question | The indicator that surfaces the answer | Coded field(s) |
|---|---|---|
| **Why is it necessary to clean?** | the stated *purpose/consequence* clause tied to the occurrence (what cleanness enables / uncleanness costs) | `purpose` |
| **Where does "unclean" come from?** | the *source/cause* of the state + the term's *root sense* | `source`, `source_domain`, term-header `etymology` |
| **Why cover the unclean — why not scrub it clean?** | *which reset-verb attaches to which kind of uncleanness* (cross-tab) | `reset` × `source_domain` |
| **Is cleanness IB-desired / external expectation / prerequisite?** | the *driver* and the *person's role* (does he want it, is he commanded, is it access-conditional; active or passive) | `driver`, `person_role` |
| **Does awareness of unclean come into play?** | *knowledge/intent markers* co-occurring (hidden / made-known / unwitting / high-hand) | `awareness` |
| **Is clean status past-only or also future?** | the *temporal frame* — remedy-of-past vs standing-forward vs recurring vs permanent | `temporal` |

The whole schema exists so these six rows (and the ones you'll add later) can be **answered from the coded corpus by query**, with every answer traceable to its occurrences.

---

## Part 2 — Per-occurrence coding schema (controlled vocabularies)

For **every inner-being axis-term occurrence** (clean/unclean, sin/guilt, holy/profane, atone/cover, self, bless/curse, redeem), code:

| Field | Controlled vocabulary (extendable) |
|---|---|
| `ref` · `term` · `gloss` · `axis` | Lev ch:vn · translit · gloss · CLEAN_UNCLEAN / SIN_GUILT / HOLY_PROFANE / ATONE_COVER / SELF / BLESS_CURSE / REDEEM / OTHER |
| `polarity` | unclean · clean · holy · common · profaned · guilty · cleared · n.a. |
| `bearer` (locus of the state) | person · priest · congregation · body · garment · vessel · house · land · sanctuary · animal · food |
| `source` (cause of the state) | corpse/death · disease-tsaraat · discharge-zav · menstrual-niddah · semen · childbirth · carcass-contact · dietary-animal · sexual-moral · idolatry-Molech · bloodguilt · unintentional-sin · contact-transfer · unstated |
| `source_domain` | **mortuary** · **genital/bodily** · **dietary** · **moral** · **cultic** · unstated |
| `reset` (mechanism, multi) | wash-body(rachats) · launder(kabas) · wait-evening · wait-7day · atone/cover(kaphar) · pronounce/purge-clean(taher-rite) · sin-offering(chattat) · guilt-offering(asham) · burn · banish/scapegoat · exclude-outside-camp · shave · sprinkle-blood/water · confess · none/irreversible |
| `purpose` (why it matters) | access-enable(approach / eat-holy / enter) · danger-avert(death / cut-off) · protect-holy(not-defile-sanctuary/name) · belonging(be-holy-as-God / "be mine") · unstated |
| `driver` | command(imperative) · prerequisite-access · divine-initiative(done-for-them) · **desire/volition** *(flagged wherever it actually appears)* |
| `person_role` | active(performs the reset / confesses) · passive(reset done for/to him) · n.a. |
| `awareness` | unintentional(shegagah) · hidden-then-known · knowing/high-hand · not-in-view |
| `temporal` | remedy-past · standing-forward · recurring-required · permanent(olam) · until-evening · seven-day |
| `co_terms` | other axis-terms in the same verse (sin, holy, atone, nephesh, blood…) |
| `note` | one-line verse-context |

**Per-TERM header** (once per term, not per occurrence): `root` + *literal sense* (etymology) · ANE/cognate note · sense-cluster in Leviticus · polarity-partner · first-occurrence in Torah. *(This carries the "where does the word come from" etymology answer.)*

---

## Part 3 — The schema working on a cross-domain sample

Coding 13 occurrences across the domains (bodily / dietary / moral / holiness):

| ref | term | polarity | source_domain | reset | purpose | driver | awareness | temporal |
|---|---|---|---|---|---|---|---|---|
| 11:24 | tame | unclean | dietary/mortuary (carcass) | wait-evening | unstated | command | — | until-evening |
| 11:25 | tame | unclean | dietary (carcass carried) | launder + wait-evening | unstated | command | — | until-evening |
| 11:44 | tame/qadosh | (don't defile)/holy | dietary | (avoid) | belonging (**"be holy for I am holy"**) | command | — | standing-forward |
| 15:13 | taher | clean | genital/bodily (discharge) | wait-7day + launder + bathe(fresh water) | (return to clean) | command | — | seven-day |
| 15:16 | tame | unclean | genital/bodily (semen) | bathe-body + wait-evening | unstated | command | — | until-evening |
| 5:2 | tame/asham | unclean→guilty | contact (unclean carcass) | *(→ 5:6)* | (guilt incurred) | — | **hidden** | remedy-past |
| 5:3 | tame/asham | unclean→guilty | contact (human uncleanness) | *(→ 5:6)* | — | — | **hidden-then-known** | remedy-past |
| 5:5 | chata/asham | guilty | moral | **confess** | — | command | **realized** | remedy-past |
| 5:6 | chattat/kipper | guilty→cleared | moral | **sin/guilt-offering + atone(kaphar)** | (be forgiven) | divine-initiative | realized | remedy-past |
| 16:30 | kipper→taher | sins→clean | moral (all sins) | **atone(kaphar) → cleanse(taher)** | (clean before the LORD) | divine-initiative | — | recurring(annual) |
| 19:2 | qadosh | holy | — | — | belonging (**"be holy for I am holy"**) | command | — | standing-forward |
| 20:25 | tame/tahor | unclean/clean | dietary | **separate/discern** | (not detestable) | command | — | standing-forward |
| 20:26 | qadosh | holy | cultic | (separation) | belonging (**"that you should be mine"**) | divine-election + command | — | standing-forward |

### What the sample *already* shows (previewing the discoveries)

- **Q3 (cover vs scrub) — the answer is visible in the cross-tab.** *Bodily/dietary* uncleanness (carcass, discharge, semen) is reset by **washing, laundering, bathing, waiting** — literally *scrubbing + time*, **never covering**. *Moral* fault (sin/guilt) is reset by **atonement = kaphar "cover"** + sacrifice. So **"covering" is reserved for sin/moral fault; "scrubbing" for bodily uncleanness.** They are *different domains with different resets* — which is itself the beginning of an answer to your deeper question about *why* the moral is *covered* rather than *scrubbed*.
- **Q5 (awareness) — yes, decisively, in the moral domain.** Lev 5:2–6 makes *knowledge the hinge*: unclean-by-contact + **hidden** → nothing yet; **"when he comes to know it"** → *guilty* → *confess* → *atone*. **Awareness activates the moral remedy** (the bodily remedy, by contrast, runs automatically — carcass-contact defiles whether you know or not, and lapses at evening). So awareness matters *for the moral, not the bodily* — a sharp finding.
- **Q4 (desire / external / prerequisite) — the driver is God, not the self.** Every holiness command is grounded in *God's* nature or claim: *"be holy, for I am holy"* (11:44; 19:2), *"that you should be mine"* (20:26). The person is **commanded** and (when aware) **active in confessing** — but no occurrence yet shows *the inner being desiring to be clean for its own sake*. The `driver`/`person_role` fields will let us test this across all 546 verses: **does volition/desire ever appear, or is it always external-command + access-prerequisite?**
- **Q6 (past or future) — split by domain, and the field will quantify it.** Bodily uncleanness is **momentary** (*until evening*, *seven days*) — a *remedy of the immediate past*, constantly re-incurred. Holiness is a **standing-forward** state (*"be holy"* ongoing, *olam*). So *clean ≠ holy*: clean is a *repeatedly-restored baseline*; holy is a *maintained vocation*. The atonement of the Day is **recurring-annual** — cleansing that *expires and must be renewed*, implying it addresses *accumulated past*, not a secured future.
- **Q1 (why necessary) — belonging + protecting the holy.** The `purpose` field so far returns *belonging* ("be mine", "as I am holy") and *protecting the holy* (don't defile) — not self-benefit. The full coding will show whether *access-enable* and *danger-avert* dominate elsewhere (they will, in the priestly/sanctuary texts).

That the sample resolves five of six questions *in preview* is the proof the schema is aimed correctly: **once every occurrence is coded, the questions are answered by reading the columns.**

---

## Part 4 — How Phase A and Phase B use the schema

- **Phase A (baseline, covering ALL of Leviticus) = the coding itself.** Chapter by chapter, every inner-being axis-term occurrence is coded on the schema (the fields above). Ritual-only verses are logged as *[ritual — no inner-being span]* so nothing is missed and the ritual/inner-being boundary is explicit. Output: a coded table per chapter-group (readable `.md`) **plus a machine-readable companion** (JSON / small SQLite `lev_coding` table) so Phase B can query. This *is* the "quick exposition of all verses," but structured — each verse's inner-being content captured as coded indicators, not just prose.
- **Phase B (discoveries) = queries + close reading over the coded corpus.** Each question (yours above, and the ones you'll add) becomes: *filter/cross-tab the coded fields → read the returned occurrences in context → write the discovery.* Because every answer traces to coded occurrences, the resolution is **transparent and auditable** — you can see exactly which verses drive each conclusion. Per-term headers carry the etymology/origin layer.

---

## Part 5 — Two decisions before I run Phase A across all 27 chapters

1. **Schema sign-off** — is the field-set above right, or do you want to add/adjust dimensions? (e.g., a `transmissibility` field — does the uncleanness *spread* to others/objects? — would sharpen "where it comes from / how it behaves." I'd recommend adding it.)
2. **Persistence** — code into (i) readable `.md` tables + a JSON companion I query for Phase B *(recommended — fast, git-tracked, no new DB infra yet)*, or (ii) a new DB table `lev_coding` from the start (heavier, but fits the "all study in the DB" rule; we can migrate the JSON in once the schema settles). **Recommend (i)** now, migrate to (ii) once the schema is proven over a few chapters.

---

*Filed 2026-07-05. Builds on [`wa-leviticus-terminology-orientation-and-plan-20260705.md`](wa-leviticus-terminology-orientation-and-plan-20260705.md). No full coding generated pending schema sign-off + the two decisions.*
