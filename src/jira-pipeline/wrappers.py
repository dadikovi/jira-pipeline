from briefly.process import *
from .utils import *

def jira_pipeline_process(rules):
    def wrapped_jira_pipeline_process(func):
        '''A simple local running process.
            The wrapped function is the do_execute() of the process.
        '''
        class process_wrapper(SimpleProcess):
            def do_execute(self):
                self.inputs = Utils.read_input(self, rules)
                func(self, *self.args, **self.kargs)

        process_wrapper.__name__ = func.__name__
        return process_wrapper
    return wrapped_jira_pipeline_process