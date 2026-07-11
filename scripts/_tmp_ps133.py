import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,133,
  note="Ps133 'how good when brothers dwell in unity' (3v). Operation = brotherly CONCORD - the GOOD and PLEASANT state of brothers DWELLING in unity, likened to anointing oil flowing down and dew descending. God's commanded-blessing = qualifier; oil/beard/dew/mountains imagery = standalone.")
CH=[
 (272995,"good (tob)","state","brothers","dwell together as good","in unity",IB,"paired with the pleasantness of unity",
  "v1: 'Behold, how GOOD (tob) and pleasant it is when brothers dwell in unity!' - the operation of concord perceived as good: the moral rightness and worth of brothers united."),
 (272996,"pleasant (naim)","state","brothers","dwell together as pleasant","in unity",IB,"paired with the goodness of unity",
  "v1: 'how good and PLEASANT (naim) it is' - the delight of unity, concord felt not only as right but as sweet, like oil and dew."),
 (272998,"dwell in unity (yashab)","action","brothers","dwell together","in harmony",IB,"paired with the good and pleasant",
  "v1: 'when brothers DWELL (yashab) in unity!' - the operation itself: brothers living together in concord, the harmony that the whole psalm celebrates and images."),
]
for a in CH: r.ch(*a)
QU=[
 (273023,"commanded (tsavah)",272998,"v3: 'For there the LORD has COMMANDED (tsavah) the blessing' - God's decree of blessing on unity. Qualifier."),
 (273024,"blessing (berakah)",272998,"v3: 'the LORD has commanded the BLESSING (berakah), life forevermore' - God's blessing where concord dwells. Qualifier."),
]
for sid,sense,src,d in QU: r.qu(sid,sense,src,d)
for sid,sense,d in [
 (272993,"Ascents (maalah)","v0: heading, of David. Standalone."),
 (272999,"unity (yachad)","v1: 'when brothers dwell in UNITY (yachad)!' - the togetherness (char dwell, 272998), image. Standalone."),
 (273000,"precious (tob)","v2: 'It is like the PRECIOUS (tob) oil on the head' - the fine oil, image of unity's richness. Standalone."),
 (273001,"oil (shemen)","v2: 'like the precious OIL (shemen)' - the anointing oil, image of unity flowing down. Standalone."),
 (273003,"head (rosh)","v2: 'the oil on the HEAD (rosh)' - the anointed head, image. Standalone."),
 (273004,"running down (yarad)","v2: 'RUNNING DOWN (yarad) on the beard' - the oil flowing down, image of unity spreading. Standalone."),
 (273006,"beard (zaqan)","v2: 'on the BEARD (zaqan)' - Aaron's beard, image. Standalone."),
 (273007,"beard (zaqan)","v2: 'on the BEARD (zaqan) of Aaron' - the beard repeated, image of the oil's descent. Standalone."),
 (273009,"running down (yarad)","v2: 'RUNNING DOWN (yarad) on the collar of his robes!' - the oil reaching the robes, image. Standalone."),
 (273011,"collar (peh)","v2: 'on the COLLAR (peh) of his robes' - the robe's edge, image. Standalone."),
 (273013,"robes (middah)","v2: 'the collar of his ROBES (middah)!' - the priestly garments, image. Standalone."),
 (273014,"dew (tal)","v3: 'It is like the DEW (tal) of Hermon' - the descending dew, image of unity's refreshment. Standalone."),
 (273017,"falls (yarad)","v3: 'which FALLS (yarad) on the mountains of Zion!' - the dew descending, image. Standalone."),
 (273019,"mountains (har)","v3: 'on the MOUNTAINS (har) of Zion!' - Zion's hills, image. Standalone."),
 (273025,"life (chay)","v3: 'the blessing, LIFE (chay) forevermore' - the life God's blessing gives, image. Standalone."),
 (273026,"forevermore (olam)","v3: 'life FOREVERMORE (olam)' - the perpetuity of the blessing; temporal. Standalone."),
]: r.st(sid,sense,d)
r.write()
