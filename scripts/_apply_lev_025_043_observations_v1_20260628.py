"""Capture Lev 25:43 inner-being observations into ib_observation.

Three streams open at Lev 25:43:
  - fear-of-god  (M01, H3372)  — the GOVERNING stream (whole treatment of the vulnerable); 12 dims
  - dominion     (M23, H7287)  — radah, the impulse being bounded; 12 dims (D2 silent)
  - ruthlessness (M06, H6531)  — be-perek; the dims THIS verse adds to the existing track; 6 dims

Idempotent: deletes any existing Lev 25:43 rows for these three operations, then re-inserts.
Source doc: verse-analysis/Lev/wa-lev-025-043-observations-v1-20260628.md (the reading)
            verse-analysis/Lev/wa-lev-025-043-fanout-v1-20260628.md       (the raw data)
"""
import sqlite3, os, datetime

DB = os.path.join('database', 'bible_research.db')
ORIGIN = 'Lev 25:43'
ORIGIN_ID = 15522
RAW = 'wa-lev-025-043-fanout-v1-20260628.md'
NOW = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

# (dimension, narrative, term_anchor, status, provenance, reconsider_at, basis)
FEAR = ('fear-of-god', 'H3372', [
 ('D1', 'Reverential fear of God — an enduring inner orientation (not reactive fright); the constitutive disposition that governs the whole inner life.', 'resolved', 'digested', '91 fear-of-God verses', 'M01-A definition'),
 ('D2', 'Received-from-outside — learnable, transmissible, divinely-implantable; not self-generated. Here commanded by God.', 'resolved', 'digested', '-', 've_lexical origin=received-from-outside; M01-A'),
 ('D3', 'Borne by "you" (the addressed master/the Israelite holding power); engages the affect faculty.', 'resolved', 'digested', '-', 'finding f#1037327; ve_lexical faculty=affect'),
 ('D4', 'yare, Qal (HVqq2ms) — the act of fearing/revering.', 'resolved', 'mechanical', '-', 'morphology HVqq2ms'),
 ('D5', 'God (elohim) — the One feared.', 'resolved', 'mechanical', '-', '"your God"'),
 ('D6', 'Commanded — "you shall fear" (imperatival); a recurring refrain through Lev 25 treatment-laws (25:17, 25:36, 25:43).', 'resolved', 'digested+fan-out', 'Lev 25:17; 25:36', 've_lexical valence=commanded'),
 ('D7', 'REFRAMED: fear of God is the governing orientation over the WHOLE treatment of the vulnerable — it underwrites the entire protective regime toward one sold into servitude (no wronging 25:17; no usury 25:36; no ruthless rule 25:43; hired-worker not slave 25:40,42; jubilee release 25:41). Restraining ruthlessness is ONE expression.', 'resolved', 'researcher+fan-out', 'Lev 25:17; 25:36; 25:43', 'Lev 25 "fear your God" refrain'),
 ('D8', 'A rightly-governed treatment of the vulnerable — humane economic/social conduct toward the weak; exploitation (cheating, usury, cruelty) does not occur. Non-occurrence of cruelty is one part.', 'needs-corroboration', 'digested+fan-out', 'Lev 25:17; 25:36', 'vc#4212/4263 analysis-notes'),
 ('D9', 'In Lev 25 it couples to a SET of treatment-commands as their shared motive-clause ("...but fear your God"); here specifically set against ruthless-dominion (paired verbs). The standing counter-force to every form of mistreatment.', 'resolved', 'digested+fan-out', 'Lev 25:17; 25:36; 25:43', 've_lexical compound; verse structure'),
 ('D10', 'Commanded / good — the prescribed orientation; its absence marks moral blindness.', 'resolved', 'digested', '-', 'M01-A; ve_lexical valence'),
 ('D11', 'Fear-of-God is a GOVERNING operation — produces no act of its own; acts by governing the inner being\'s whole conduct toward others, surfacing as the motive behind humane law. Test across the Lev 25 refrain (17/36/43) + 91 fear-of-God verses.', 'open', 'researcher', 'Lev 25:17; 25:36; 91 yare+elohim verses', 'cross-operation governing pattern'),
 ('D12', 'HIDDEN: the safety of the vulnerable is located in the perpetrator\'s vertical relationship (fear of God), not in the victim\'s protection or external enforcement — humane treatment is anchored from within, by reverence. And God, who commands fear, does not fear (creaturally-distinctive).', 'needs-corroboration', 'digested+researcher', 'Lev 25:17; 25:36', 'M01 f#7323'),
])

DOMINION = ('dominion', 'H7287', [
 ('D1', 'Dominion/rule (radah) exercised over another — the will to rule; here over a brother, and (forbidden) with ruthlessness.', 'resolved', 'mechanical+digested', '25 radah verses', 'finding f#1037328'),
 ('D2', 'Not stated in-verse — the verse addresses the RESTRAINT of dominion, not its origin.', 'silent', 'mechanical', 'verses naming dominion\'s source', 'verse content'),
 ('D3', 'Borne by "you" (the master holding the indentured brother).', 'resolved', 'digested', '-', 'finding "borne by other (addressed)"'),
 ('D4', 'radah, Qal (HVqi2ms) — "rule over / have dominion / tread down".', 'resolved', 'mechanical', '-', 'morphology HVqi2ms'),
 ('D5', '"him" — the impoverished/indentured brother (person). (NB: the verse-read finding mis-slotted the object as "ruthlessly"; the object is the servant.)', 'resolved', 'mechanical+fan-out', '-', 'v.39 context; v.46 "brothers"; DQ flag'),
 ('D6', 'The forbidden MANNER is be-perek (ruthlessly). What the command forbids is the ruthless manner of the rule, not rule itself.', 'resolved', 'mechanical', '-', 'be-perek modifies radah'),
 ('D7', 'When unrestrained, dominion+cruelty unfolds into enslavement and bitterness (Exo 1:13-14); here the command prevents that unfolding.', 'needs-corroboration', 'fan-out', 'Exo 1:13; 1:14', 'perek arc'),
 ('D8', '(If ruthless) the subjugation/crushing of the brother — here forestalled by the command.', 'needs-corroboration', 'fan-out', 'Exo 1:13; 1:14', 'perek arc'),
 ('D9', 'Coupled to fear-of-God as its restraint (paired verbs, inverse of the fear stream); and to perek as its forbidden manner. perek attaches to ANY domination-act (abad in Exo 1:13, radah here).', 'resolved', 'mechanical+fan-out', 'Exo 1:13 (abad); Lev 25:46,53', 'verse structure; perek arc'),
 ('D10', 'radah is itself valence-NEUTRAL — only the ruthless manner over a brother is forbidden; dominion per se is not condemned.', 'resolved', 'researcher', 'Gen 1:26-28; Isa 14; Eze 34', 'radah spread'),
 ('D11', 'radah is valence-neutral: the SAME verb is the God-given creation mandate (Gen 1:26-28) AND tyranny (Isa 14; Eze 34). What flips it is the manner (perek) and the object (a brother). Mirrors enslavement (abad). Test across the 25 radah verses; M23 not started.', 'open', 'researcher+fan-out', 'Gen 1:26-28; Isa 14:2,6; Eze 34:4; 25 radah verses', 'radah spread; cross-operation neutrality'),
 ('D12', 'HIDDEN: dominion over fellow image-bearers carries a built-in limit — the faculty God gave for creation (Gen 1) must not be turned ruthlessly on a brother; the boundary is the brotherhood of the ruled + the fear of God.', 'needs-corroboration', 'researcher', 'Gen 1:26-28; Eze 34:4', 'image-bearer limit'),
])

RUTHLESS = ('ruthlessness', 'H6531', [
 ('D5', 'Its object is the weaker party — here the impoverished/indentured brother; perek is exercised over the subjugated.', 'resolved', 'mechanical+fan-out', 'the 6 perek verses', 'v.39 context'),
 ('D6', 'The manner be-perek — harshness/severity; the untracked-until-now manner-word.', 'resolved', 'mechanical', '-', 'morphology HNcmsa + be-'),
 ('D9', 'Here perek couples to radah (rule), whereas at Exo 1:13 it couples to abad (enslave) — confirming perek is a MANNER attaching to any domination-act, not bound to one verb.', 'resolved', 'mechanical+fan-out', 'Exo 1:13 (abad); Lev 25:46,53', 'cross-verse coupling'),
 ('D10', 'Forbidden — explicitly prohibited ("lo" + command). This is the prohibition Exo 1:13 D10 pointed to (convergence: flips needs-corroboration -> resolved).', 'resolved', 'digested+convergence', 'Lev 25:46; 25:53', 've_lexical valence=forbidden'),
 ('D11', 'Confirms perek is a MANNER-operation — no act of its own, only the cruel quality of another act (radah here, abad at Exo 1:13).', 'resolved', 'fan-out', 'other inner-cruelty terms', 'cross-verse manner pattern'),
 ('D12', 'HIDDEN: the cruelty-word Egypt used (Exo 1) becomes the word Israel is FORBIDDEN to use against a brother (Lev 25); here its restraint is named outright — the fear of God. Eze 34:4 turns it inward on Israel\'s shepherds.', 'needs-corroboration', 'researcher', 'Lev 25:46; 25:53; Eze 34:4', 'oppressed-must-not-become-oppressor'),
])

ALL = [FEAR, DOMINION, RUTHLESS]

def main():
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    c = conn.cursor()
    ops = [op for op, _, _ in ALL]
    # idempotent: clear existing Lev 25:43 rows for these ops
    q = ",".join("?" * len(ops))
    before = c.execute(f"SELECT count(*) FROM ib_observation WHERE origin_verse=? AND operation IN ({q})",
                       [ORIGIN, *ops]).fetchone()[0]
    c.execute(f"DELETE FROM ib_observation WHERE origin_verse=? AND operation IN ({q})", [ORIGIN, *ops])
    n = 0
    for op, anchor, rows in ALL:
        for dim, narr, status, prov, recon, basis in rows:
            c.execute("""INSERT INTO ib_observation
                (operation,dimension,narrative,term_anchor,origin_verse,origin_verse_id,
                 reconsider_at,status,provenance,basis,raw_file,created)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
                (op, dim, narr, anchor, ORIGIN, ORIGIN_ID,
                 None if recon == '-' else recon, status, prov, basis, RAW, NOW))
            n += 1
    conn.commit()
    print(f"cleared {before} prior rows; inserted {n} observations for Lev 25:43")
    for op, _, _ in ALL:
        cnt = c.execute("SELECT count(*) FROM ib_observation WHERE origin_verse=? AND operation=?",
                        (ORIGIN, op)).fetchone()[0]
        print(f"  {op}: {cnt}")
    conn.close()

if __name__ == '__main__':
    main()
