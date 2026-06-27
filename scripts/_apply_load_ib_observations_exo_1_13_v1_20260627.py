"""Create ib_observation + load Exo 1:13's observations (authored data; idempotent).
term_anchor NOT NULL (no phantoms). raw_file = provenance to the raw source collection.
Dimensions per catalogue D1-D12 (D12 = Hidden meaning). Reversible: DROP TABLE.
Canonical source of the Exo 1:13 observation records."""
import sqlite3, os
RAW='wa-exo-1-13-fanout-v1-20260627.md'
c=sqlite3.connect(os.path.join('database','bible_research.db')); c.row_factory=sqlite3.Row; cur=c.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS ib_observation(
  id INTEGER PRIMARY KEY, operation TEXT, dimension TEXT, narrative TEXT,
  term_anchor TEXT NOT NULL, origin_verse TEXT, origin_verse_id INTEGER,
  reconsider_at TEXT, status TEXT, provenance TEXT, basis TEXT, raw_file TEXT,
  created TEXT DEFAULT (datetime('now')))""")
cur.execute("DELETE FROM ib_observation WHERE origin_verse IN ('Exo 1:13','Exo 1:14')")  # additive: only own rows
# (operation, dim, narrative, term_anchor, origin_ref, reconsider_at, status, provenance, basis)
O=[
('ruthlessness','D1',"Ruthlessness (perek) is an inner cruelty — a hard, crushing disposition exercised by an actor over another.",'H6531','Exo 1:13','perek (H6531) — the 6 occurrences','resolved','mechanical','perek lemma; manner-noun'),
('ruthlessness','D2',"It springs from the Egyptians' dread of Israel — fear of a perceived threat to power.",'H6531','Exo 1:13','Exo 1:12; fear->cruelty (Gen 20:11; Deut 25:18)','needs-corroboration','convergence','Exo 1:12 context; researcher+logos+claude'),
('ruthlessness','D2',"Its restraint is the fear of God; its absence removes the brake.",'H6531','Exo 1:13','Lev 25:43; Deut 25:18; Ps 36:1','needs-corroboration','convergence','3-witness; most explicit causal thread'),
('ruthlessness','D2',"Beneath the trigger (dread), the deeper wellspring of cruelty is the HEART — every intention of the heart 'only evil' (Gen 6:5); evil comes from within (Mark 7:21-23).",'H3820','Exo 1:13','Gen 6:5; Jer 17:9; Mark 7:21-23','needs-corroboration','convergence','logos+claude — heart as the source (links to Gen 6:5)'),
('ruthlessness','D2',"Anger/wrath produces cruelty — 'their wrath, for it is cruel' (Gen 49:7); 'wrath is cruel' (Pro 27:4).",'H0639','Exo 1:13','Gen 49:7; Pro 27:4','needs-corroboration','claude-chat','aph (H0639) anger-cruelty texts'),
('ruthlessness','D2',"Power without restraint enables cruelty — man has power over man to his hurt (Eccl 8:9); having the power becomes the justification.",'H6531','Exo 1:13','Eccl 8:9','needs-corroboration','convergence','logos+claude — power-without-restraint'),
('ruthlessness','D2',"Ruthlessness is enabled by a severed relationship / lost covenant memory — a new king who did not know (yada) Joseph (Exo 1:8).",'H3045','Exo 1:13','Exo 1:8','needs-corroboration','claude-chat','the Exo 1 motive chain'),
('ruthlessness','D3',"It is borne by the actor (the Egyptians); no inner seat (heart/spirit) is named in the verse.",'H6531','Exo 1:13','verses where a cruelty term names a seat','silent','mechanical','no seat lemma in-verse'),
('ruthlessness','D5',"Its object is always a weaker party (here Israel) — perek is exercised over the subjugated.",'H6531','Exo 1:13','the 6 perek verses (all = rule-over)','needs-corroboration','researcher','the 6 perek verses concern ruling over the weak'),
('ruthlessness','D9',"It couples to enslavement as its MANNER (be-perek modifies the Hiphil abad) — realised through the act it qualifies, not standalone.",'H6531','Exo 1:13','H5647; coupling 3 verses','resolved','mechanical','morph: be-perek on HVhw3mp'),
('ruthlessness','D10',"It is condemned — the Levitical law forbids ruling perek over a brother (Lev 25:43,46,53).",'H6531','Exo 1:13','Lev 25:43; 25:46; 25:53','needs-corroboration','convergence','the 3 Leviticus prohibitions'),
('ruthlessness','D11',"Ruthlessness is a MANNER-operation — no act of its own, only the cruel quality of another operation. Reconsider whether all inner-cruelty terms behave as manners.",'H6531','Exo 1:13','other inner-cruelty terms','open','researcher','discovery from the coupling'),
('ruthlessness','D12',"HIDDEN: the same cruelty-word (perek) Egypt used becomes the word Israel is FORBIDDEN to use on its own (Lev 25); Eze 34:4 turns it inward on Israel's leaders — the oppressed must not become the oppressor.",'H6531','Exo 1:13','Lev 25:43-46; Eze 34:4','needs-corroboration','claude-chat','the perek theological shape (Claude)'),
('enslavement','D1',"Enslavement is 'cause-to-serve' (abad Hiphil) — an actor forcing another into the state of serving.",'H5647','Exo 1:13','abad (H5647) Hiphil — the 8 occurrences','resolved','mechanical','abad H5647 Hiphil'),
('enslavement','D4',"The Hiphil stem is the mark that the actor CAUSES the state — enslavement is the actor producing 'enslaved'.",'H5647','Exo 1:13','abad-Hiphil verses','resolved','mechanical','morph HVhw3mp Hiphil'),
('enslavement','D5',"Its object is the people of Israel (the subjugated).",'H5647','Exo 1:13',None,'resolved','mechanical','object marker on people-of-Israel'),
('enslavement','D7',"The process is a causative chain: cause-to-serve (Hiphil) -> make-bitter (marar Piel) -> serve (Qal).",'H5647','Exo 1:13','H4843 (marar); Exo 1:14','resolved','mechanical','Exo 1:13-14 stems'),
('enslavement','D8',"Its produced state is twofold — 'enslaved' (subjugation) and 'bitter' (the affective fruit, Exo 1:14).",'H5647','Exo 1:14','H4843 (marar)','resolved','mechanical','Exo 1:14'),
('enslavement','D8',"Bitterness (marar, Piel/factitive) is an affective inner state CAUSED in the enslaved — the inner fruit of oppression.",'H4843','Exo 1:14','marar (H4843) occurrences','resolved','mechanical','marar Piel HVpw3mp'),
('enslavement','D9',"Enslavement couples to ruthlessness (its manner here); ruthless-enslavement is a rare dynamic (3 verses) — Egypt's act, forbidden to Israel (Lev 25:46).",'H5647','Exo 1:13','Lev 25:46; H6531','resolved','mechanical','coupling 3 verses'),
('enslavement','D10',"Cause-to-serve is morally NEUTRAL as an operation — oppressive (Exo 1:13), devotional (2Ch 34:33), inversion (Isa 43:23-24). Valence set by who-serves-whom and the manner.",'H5647','Exo 1:13','2Ch 34:33; Isa 43:23-24','needs-corroboration','convergence','the abad-Hiphil 8-verse spread'),
('enslavement','D11',"The SAME operation inverts in valence across the corpus — valence is not intrinsic to the operation but to its object+manner. Reconsider for other neutral operations.",'H5647','Exo 1:13','abad-Hiphil verses; other neutral operations','open','researcher','discovery from the 8-verse spread'),
('enslavement','D12',"HIDDEN: abad is the SAME word for being enslaved (forced service) AND for serving/worshipping God — the inner being's 'serving' is one operation; bondage vs worship is set entirely by WHO is served and HOW. Implication: the inner being is constitutionally a servant, never master-less — the only question is the master.",'H5647','Exo 1:13','2Ch 34:33 (serve LORD); Isa 43:23; the abad spread','open','researcher','researcher noticed in Logos comment (serve/worship God)'),
]
cur.executemany("""INSERT INTO ib_observation(operation,dimension,narrative,term_anchor,origin_verse,reconsider_at,status,provenance,basis,raw_file)
   VALUES(?,?,?,?,?,?,?,?,?,?)""",[(o[0],o[1],o[2],o[3],o[4],o[5],o[6],o[7],o[8],RAW) for o in O])
cur.execute("UPDATE ib_observation SET origin_verse_id=(SELECT id FROM verse WHERE reference=origin_verse)")
c.commit(); print('loaded', c.execute('SELECT COUNT(*) FROM ib_observation').fetchone()[0], 'observations; phantoms:', c.execute("SELECT COUNT(*) FROM ib_observation WHERE term_anchor IS NULL OR term_anchor=''").fetchone()[0])
for r in c.execute("SELECT dimension, COUNT(*) k FROM ib_observation GROUP BY dimension ORDER BY dimension"):
    print(' ',r['dimension'],r['k'])
