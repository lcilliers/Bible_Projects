import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,123,
  note="Ps123 the upward look (4v). Char-arcs: A eyes LIFTED in dependence v1-2 (to you I lift up my eyes; as servants' eyes to their master's hand, our eyes to the LORD till he has mercy); B surfeit of contempt v3-4 (our SOUL has had more than enough of scorn - the arrogant at EASE, the PROUD). God's enthroned/mercy = qualifiers; maidservant-imagery + contempt/scorn reproach-content = standalone.")
CH=[
 (307798,"lift up the eyes (nasa)","action","the psalmist","lift up the eyes","to God enthroned",GOD,"paired with the servant's upward look for mercy",
  "v1: 'To you I LIFT UP (nasa) my eyes, O you who are enthroned in the heavens!' - the upward look of dependence, eyes raised to the enthroned God for mercy."),
 (272469,"soul (nephesh)","faculty","the people","be surfeited","with scorn and contempt",IB,"paired with the scorn of the proud",
  "v4: 'Our SOUL (nephesh) has had more than enough of the scorn of those who are at ease' - the self glutted with humiliation, worn out under reproach."),
 (272473,"at ease (shaanan)","status","the complacent","be at ease","scorning the afflicted",IB,"paired with the proud",
  "v4: 'the scorn of those who are AT EASE (shaanan)' - the complacent, whose comfortable ease breeds contempt for the afflicted."),
 (272475,"proud (yonah/gaayon)","status","the proud","despise","the afflicted",IB,"paired with those at ease",
  "v4: 'and of the contempt of the PROUD (proud)' - the arrogant whose contempt the humbled people have borne to the full."),
]
for a in CH: r.ch(*a)
QU=[
 (307800,"enthroned (yashab)",307798,"v1: 'O you who are ENTHRONED (yashab) in the heavens!' - God enthroned on high, to whom the eyes are lifted. Qualifier."),
 (272460,"mercy (chanan)",307798,"v2: 'so our eyes look to the LORD our God, till he has MERCY (chanan) upon us' - God's mercy awaited. Qualifier."),
 (272462,"mercy (chanan)",272469,"v3: 'Have MERCY (chanan) upon us, O LORD' - God's mercy petitioned. Qualifier."),
 (272464,"mercy (chanan)",272469,"v3: 'have MERCY (chanan) upon us' - God's mercy petitioned, doubled. Qualifier."),
]
for sid,sense,src,d in QU: r.qu(sid,sense,src,d)
for sid,sense,d in [
 (307796,"Ascents (maalah)","v0 superscription: 'A Song of ASCENTS (maalah)' - the pilgrim-song heading. Standalone."),
 (272450,"maidservant (shiphchah)","v2: 'as the eyes of a MAIDSERVANT (shiphchah) to the hand of her mistress' - the servant-image of dependent looking. Standalone."),
 (272453,"mistress (gebereth)","v2: 'to the hand of her MISTRESS (gebereth)' - the mistress on whom the maid's eyes depend, image. Standalone."),
 (272467,"enough (saba)","v3: 'for we have had more than ENOUGH (saba) of contempt' - the surfeit of contempt endured (char soul, 272469), image. Standalone."),
 (272468,"contempt (buz)","v3: 'more than enough of CONTEMPT (buz)' - the contempt suffered, object. Standalone."),
 (272471,"enough (saba)","v4: 'Our soul has had more than ENOUGH (saba)' - the surfeit of scorn, image. Standalone."),
 (272472,"scorn (laag)","v4: 'the SCORN (laag) of those who are at ease' - the mockery of the complacent (char at-ease, 272473), object. Standalone."),
 (272474,"contempt (buz)","v4: 'and of the CONTEMPT (buz) of the proud' - the contempt of the arrogant (char proud, 272475), object. Standalone."),
]: r.st(sid,sense,d)
r.write()
