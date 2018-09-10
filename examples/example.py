from briefly.process import *
from briefly.common import *
from jira_pipeline.commands.jira_connect import *
from jira_pipeline.commands.read_properties import *

pipe = Pipeline('Connect to JIRA server')

target = read_properties('example.properties') | jira_connect() | dump()

pipe.run(target)
