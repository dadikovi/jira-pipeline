from briefly.process import *
from briefly.common import *
from jira_pipeline.commands import *
from jira_pipeline.utils import *
from jira_pipeline.system import *


pipe = Pipeline('Connect to JIRA server')

# Parameters

jira_connect_1 = Utils.read_properties('properties/internal_jira.properties')
query_issues_1 = Utils.read_properties('properties/search_jql.properties')

# Systems

internal_jira = System(jira_connect_1)

# Pype

target = pipe | query_issues(internal_jira, query_issues_1) | cut_key() | dump()

pipe.run(target)