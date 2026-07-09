"""Load Gen 6:5's observations into ib_observation (additive; idempotent per verse).
Creates table IF NOT EXISTS (does NOT drop other verses); deletes only Gen 6:5/6:6 rows then re-inserts.
term_anchor NOT NULL (no phantoms)."""
import sqlite3, os
RAW='wa-gen-006-005-fanout-v1-20260627.md'
c=sqlite3.connect(os.path.join('database','bible_research.db')); c.row_factory=sqlite3.Row; cur=c.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS ib_observation(
  id INTEGER PRIMARY KEY, operation TEXT, dimension TEXT, narrative TEXT,
  term_anchor TEXT NOT NULL, origin_verse TEXT, origin_verse_id INTEGER,
  reconsider_at TEXT, status TEXT, provenance TEXT, basis TEXT, raw_file TEXT,
  created TEXT DEFAULT (datetime('now')))""")
cur.execute("DELETE FROM ib_observation WHERE origin_verse IN ('Gen 6:5','Gen 6:6')")
O=[
('heart','D1',"The heart (lev) is the inner core/seat of man — and here it is not passive: it OPERATES, forming intention and producing thoughts.",'H3820','Gen 6:5','heart verses; the Logos heart entries','resolved','researcher','Logos: heart attends/reflects/purposes/inclines'),
('heart','D3',"The heart is THE seat — the wellspring from which the thoughts flow ('the thoughts of his heart'); the evil is located in it.",'H3820','Gen 6:5','heart-as-source verses; Exo 1:13 obs','resolved','convergence','RESOLVES the Exo 1:13 heart-wellspring thread'),
('heart','D4',"The heart OPERATES WITH FACULTIES — it forms (yetser), devises (machashavah), thinks; it regurgitates the wickedness/evil that is IN it as its thoughts.",'H3820','Gen 6:5','Mark 7:21-23; Mat 15:18-19; Logos heart-faculties','needs-corroboration','convergence','researcher insight + Logos'),
('heart','D7',"Process: content IN -> thoughts OUT. The heart contains a moral content (evil) and externalises it as its intentions/thoughts — 'out of the heart come...' (Mark 7:21).",'H3820','Gen 6:5','Mark 7:21-23; Mat 15:18-19','needs-corroboration','convergence','heart-thoughts connection'),
('heart','D8',"What the heart produces here = intention (yetser) and thoughts (machashavah), wholly evil.",'H3820','Gen 6:5','H3336 (yetser); H4284 (machashavah)','resolved','mechanical','the verse structure'),
('heart','D12',"HIDDEN: GOD HAS A HEART that can grieve — Gen 6:6 'it grieved him to his heart.' The inner being (heart) is predicated of God; his heart grieves over man's heart-evil.",'H3820','Gen 6:6',"God's-heart verses; Isa 63:10; Eph 4:30",'open','researcher','researcher observation (Gen 6:6)'),
('heart','D1',"Intention (yetser) = the FORMED inclination — from yatsar 'to shape/fashion' (the potter forms the clay, Isa 29:16; Hab 2:18). The heart's bent is something SHAPED.",'H3336','Gen 6:5','yetser 9 verses; Isa 29:16; Hab 2:18','resolved','researcher','yetser<-yatsar etymology, verse-grounded'),
('heart','D7',"The yetser is DIRECTIONAL — bent to evil (Gen 6:5; 8:21) OR stayed on God (Isa 26:3 -> perfect peace; kept toward God 1Ch 29:18). The inclination can be re-set.",'H3336','Gen 6:5','Gen 8:21; Isa 26:3; 1Ch 29:18','needs-corroboration','convergence','the 9 yetser verses'),
('heart','D12',"HIDDEN: yetser (the formed inclination) is the OT's foundational moral disposition — the dispositional substrate beneath acts (M29 finding, verse-grounded). [Corroborates the Exo 1:13 heart-wellspring observation.]",'H3336','Gen 6:5','M29 yetser finding; Gen 8:21; Exo 1:13 obs','resolved','convergence','the one verse-grounded M29 finding'),
('heart','D11',"DISCOVERY: God SEES the inner being — 'the LORD saw' the heart's intentions (hidden to men). The inner being, latent/unobservable to us, is fully seen by God.",'H3820','Gen 6:5','1Ch 28:9 (God knows every yetser of the thoughts); 1Sa 16:7','needs-corroboration','convergence','matches the focus-point latency'),
('wickedness','D1',"Wickedness (ra, noun) = the aggregate corrupt STATE of man — 'great in the earth' (extensive in degree and reach).",'H7451','Gen 6:5','ra (H7451) verses','resolved','mechanical','HNcfsc noun; intensity great'),
('wickedness','D8',"The LORD SAW the wickedness (raah) -> it GRIEVED him (6:6) -> judgment (6:7). The inner corruption is perceived by God and provokes his response.",'H7451','Gen 6:5','Gen 6:6-7','resolved','mechanical','context 6:5-7'),
('evil','D1',"Evil (ra, adjective) = the moral QUALITY of every intention of the heart.",'H7451','Gen 6:5','ra adjective verses','resolved','mechanical','HAamsa adjective'),
('evil','D6',"Its extent is TOTAL and PERPETUAL — 'only' (raq = exclusivity) + 'continually' (kol-ha-yom = all the day). No admixture of good, no respite.",'H7451','Gen 6:5','totality-language verses','resolved','mechanical','raq + kol morphology'),
('evil','D12',"HIDDEN: the evil is DISPOSITIONAL, not merely behavioural — it is the heart's intention/inclination (yetser), the formed bent; Gen 8:21 'from his youth' marks it as the substrate, not occasional acts.",'H7451','Gen 6:5','Gen 8:21; M29 yetser finding','needs-corroboration','convergence','yetser=disposition'),
]
cur.executemany("""INSERT INTO ib_observation(operation,dimension,narrative,term_anchor,origin_verse,reconsider_at,status,provenance,basis,raw_file)
   VALUES(?,?,?,?,?,?,?,?,?,?)""",[(o[0],o[1],o[2],o[3],o[4],o[5],o[6],o[7],o[8],RAW) for o in O])
cur.execute("UPDATE ib_observation SET origin_verse_id=(SELECT id FROM verse WHERE reference=origin_verse) WHERE origin_verse_id IS NULL")
c.commit()
print('Gen 6:5 observations loaded; phantoms:', c.execute("SELECT COUNT(*) FROM ib_observation WHERE term_anchor IS NULL OR term_anchor=''").fetchone()[0])
print('table totals by origin:', dict(c.execute("SELECT CASE WHEN origin_verse LIKE 'Exo%' THEN 'Exo 1:13' ELSE 'Gen 6:5' END g, COUNT(*) FROM ib_observation GROUP BY g").fetchall()))
