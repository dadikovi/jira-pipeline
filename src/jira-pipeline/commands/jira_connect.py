from briefly.process import *
from briefly.common import *
from briefly.properties import *
from jira_pipeline.exception.exceptions import *

@simple_process
def jira_connect(self):
    # Expected input is a Property object with the configuration.
    p = self.read()
    if(not isinstance(p, Properties)):
        raise UnexpectedInputException(self.___name___ + '')