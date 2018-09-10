from briefly.process import *
from briefly.common import *
from briefly.properties import *

@simple_process
def read_properties(self):
    p = Properties()
    p.load(self.read())
    self.write(p)