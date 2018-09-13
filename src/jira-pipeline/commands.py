from briefly.process import *
from briefly.common import *
from briefly.properties import *
from jira_pipeline.exceptions import *
from jira_pipeline.system import *

@simple_process
def jira_connect(self):
    """Simple process to initialize user session to JIRA system.    
    Attributes:
        primary - JSON data with the details of the JIRA system.
    Returns: an initialized System object.
    TODO: documentation of the required Property object"""

    try:
        s = ""
        for line in self.read():
            s = s + line + "\n"
        p = json.loads(s)
    except Exception:
        raise UnexpectedInputException('jira_connect requires JSON config string as primary input.')

    s = System(p)
    s.start_session()

    return s    

@simple_process
def read_properties(self, path):
    """Simple process to create Properties object from given file path.    
    Attributes:
        path - an str representing the file path of the property file.
    Returns: str representation of the Property object."""

    p = Properties()
    p.load(path)
    self.write(p.to_json())

@simple_process
def dump(self):
  '''Dump result to standard output.'''
  for line in self.read():
    self.write(line)
    print (line)