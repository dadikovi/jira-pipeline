from briefly.process import *
from briefly.common import *
from jira_pipeline.exceptions import *
from jira_pipeline.system import *
from jira_pipeline.utils import *
from json.decoder import JSONDecodeError
import json

@simple_process
def query_issues(self, system, jql):
    """Simple process to execute given JQL queries on specified JIRA system.
    Attributes:
        primary - dummy
        jql - json representation of jql to execute with "jql" key
        system - an initialized System object which represents the JIRA system where the JQL should be executed.
    Returns: json representations of the queried issues."""
    
    try:
        jql = json.loads(jql)["jql"]
    except JSONDecodeError as e:
        ErrorHandler.error("query_issues requires valid JSON object as second parameter. ", e)

    u = system.api().search_url(jql)
    j = system.get(u)
    
    if j:
        links = system.api().parse_issue_links(j)
        for u in links:
            j = system.get(u)
            if j:
                self.write(Utils.jsonstr_to_formatable_str(json.dumps(j)))

@simple_process
def cut_key(self):
    for j in self.read():
        try:
            issue = json.loads(j)
            self.write(issue["key"])
        except JSONDecodeError as e:
            ErrorHandler.error("cut_key requires valid JSON objects as primary input. ", e)



@simple_process
def dump(self):
  '''Dump result to standard output.'''
  for line in self.read():
    self.write(line)
    print (line)