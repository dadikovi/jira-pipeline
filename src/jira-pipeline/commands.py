#from briefly.process import *
#from briefly.common import *
from jira_pipeline.wrappers import *
from jira_pipeline.exceptions import *
from jira_pipeline.system import *
from jira_pipeline.utils import *
from json.decoder import JSONDecodeError
import json

@jira_pipeline_process({})
def query_issues(self, system, jql):
    """Producer process to execute given JQL queries on specified JIRA system.
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
                self.write(Utils.jsonstr_to_formatable_str(json.dumps({
                    "type": "issue",
                    "value": j
                })))

@jira_pipeline_process({"inputs":['issue']})
def cut_key(self):
    """Simple process which cuts the key from an issue
    Attributes:
        primary - issue to cut
    Returns: the key of the issue."""
    for issue in self.inputs["issue"]:
        try:
            self.write(Utils.jsonstr_to_formatable_str(json.dumps({
                    "type": "key",
                    "value": issue["key"]
            })))
        except JSONDecodeError as e:
            ErrorHandler.error("cut_key requires valid JSON objects as primary input. ", e)

@jira_pipeline_process({})
def dump(self):
  '''Dump result to standard output.'''
  for line in self.inputs["all"]:
    self.write(Utils.jsonstr_to_formatable_str(json.dumps({
                    "type": "text",
                    "value": line
    })))
    print(line)