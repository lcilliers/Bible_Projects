import sys
sys.path.insert(0, "outputs/prior-capture/work")
from cap import Fill
R = {33: "a record of which verses the readings carry and where, and the wording slips list: a gap record, not a finding",
     18: "a row of the proposed process: what each step would add, with an example: a plan, not a finding",
     25: "a row of the handoff: how the faces are to be assigned: a plan, not a finding",
     34: "a test result: coverage counts and the verses outside the set: a record of the check, not a finding",
     38: "the method of the investigation: its origin, the verse count, the search terms and the steps: a method record, not a finding"}
for fid, why in R.items():
    c = Fill(fid, "M02")
    c.not_(sorted(c.by_line), "scope or method or process record", why)
    c.done()
