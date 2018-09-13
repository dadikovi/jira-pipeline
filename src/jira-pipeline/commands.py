from briefly.process import *
from briefly.common import *
from briefly.properties import *
from jira_pipeline.exceptions import *

@simple_process
def jira_connect(self):
    """Simple process to initialize user session to JIRA system.    
    Attributes:
        #1 - a Property object with the details of the JIRA system.
    Returns:
        #1 - an initialized System object.
    TODO:
        documentation of the required Property object"""

    p = self.read()
    if(not isinstance(p, Properties)):
        raise UnexpectedInputException(self.___name___ + ' requires Properties object as first input.')

@simple_process
def read_properties(self):
    """Simple process to create Properties object from given file path.    
    Attributes:
        #1 - an str representing the file path of the property file.
    Returns:
        #1 - an initialized Properties object."""

    p = Properties()
    p.load(self.read())
    self.write(p)

@simple_process
def dump(self):
  '''Dump result to standard output.'''
  for line in self.read():
    self.write(line)
    print (line)