from briefly.process import *
from briefly.common import *
from jira_pipeline.commands import *

pipe = Pipeline('Connect to JIRA server')

internal_jira = pipe | read_properties('properties/internal_jira.properties') | jira_connect()

pipe.run(internal_jira)