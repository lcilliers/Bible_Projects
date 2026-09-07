# marah / mar (bitterness-of-soul) — DB lookup · 2026-06-19

> Read-only lookup requested re: M02 C7 (Bitterness) scope. **Headline: the Hebrew bitterness family
> (mar / marah) lives in M03 (Grief), not M02 (Anger).** M02's only bitterness term is the Greek G4088 *pikria*.

## Where the bitterness terms sit (by cluster)

| Cluster | name | bitterness terms it owns |
|---|---|---|
| **M03** | **Grief — Grief, Sorrow and Mourning** | **H4751 mar** "bitter" (12 occ), **H4843 ma.rar** "to be bitter" (13), H4844 ma.ror (3), H4786 mo.rah (1), H4787 mor.rah (1), H4470 me.mer, H4472 mam.ror, H1059 be.kheh "bitterly", H4798 mar.ze.ach "mourning", G4087 pikrainō, G4090 pikrōs |
| **M02** | Anger — Anger, Wrath and Indignation | **G4088 pikria** "bitterness" (the basis of C7); H4843 ma.rar also tagged here in its *"to provoke / embitter"* sense (status NULL) |
| **M28** | Envy — Envy, Greed and Lust | G4089 pikros "bitter" |

So **mar / marah ("bitter, bitterness of soul") are an M03 (Grief) asset.** The verb *ma.rar* (H4843) is split by
sense: the **"be bitter"** sense → M03; the **"provoke/embitter"** sense → M02 (it's why M02 lists it glossed
"to provoke").

## "Bitterness of soul" — the mar / marah occurrences (all in M03)

H4751 *mar* (12) + H4843 *ma.rar* (13) + H4786/4787 *morah* across the OT — the classic *mar nephesh*
"bitterness of soul" texts among them:

- **1Sa 1:10** — Hannah, "bitterness of soul" (H4751 mar)
- **Job 3:20 · 7:11 · 10:1** — Job, "bitterness/anguish of soul" (mar)
- **2Sa 17:8** — "enraged / bitter of soul" (mar)
- **Rut 1:20** — Naomi: "call me Mara, for the Almighty has dealt very bitterly" (ma.rar)
- **Isa 38:15,17** — Hezekiah, "the bitterness of my soul" (mar / ma.rar)
- **Ecc 7:26 · Pro 14:10 · Pro 27:7 · Gen 27:34 · Judg 18:25 · Jer 4:18 · Job 27:2 · Zec 12:10** — further mar/ma.rar
- full list (27 verses) returned by the query; every one carries `cluster=M03`.

## Bearing on the C7 (Bitterness) scope decision

- M02 C7 as built rests on **G4088 *pikria*** (4 NT occurrences) — thin, and Greek-only.
- The rich OT "bitterness-of-soul" material is **already M03's** (Grief). So pulling it into M02 C7 is a
  **cross-cluster boundary question (M02 Anger ↔ M03 Grief)**, not a simple gap-fill — the terms are owned and
  analysed elsewhere.
- Note the genuine seam: *pikria/pikros* in the NT (M02/M28) carries a **resentment/anger** edge ("bitterness…
  and wrath and anger", Eph 4:31), whereas OT *mar nephesh* is **grief/anguish** (M03). The English word
  "bitterness" spans both; the DB already splits them by that sense.

*(This is the data for the C7 decision; the decision itself remains with the researcher.)*

## Follow-up — H4843 *ma.rar* in M02 (2026-06-19)

Checked whether the M02 H4843 rows should move to M03. **They carry nothing to move:** the 3 M02 H4843 rows
(ids 4606, 4775, 5144) have **0 verses, 0 ve_lexical, 0 findings, 0 vcg/subgroup links** — empty duplicate
shells (OT-DBR-009). The verse-bearing H4843 (13 verses, 139 lexical rows) is **already in M03** (id 166,
registry 71 "anguish"). The 3 M02 shells were **already soft-deleted** (`delete_flagged=1`, since 2026-03-28);
on 2026-06-19 their `exclusion_reason` was documented (was NULL). **Active H4843 is now M03-only** — no move
made (a move would only have added empty duplicates to M03).
