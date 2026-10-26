import sys
sys.path.insert(0, "outputs/prior-capture/work")
from cap import Fill
c = Fill(20, "M02")
print(c.auto())
c.done()
