from briefly.properties import *
from jira_pipeline.exceptions import *
from json.decoder import JSONDecodeError
import json

class Utils:

    ALL_TYPES = ["issue", "key", "fields", "comments", "attachments", "text"]

    @staticmethod
    def read_properties(path):
        """Util method to create Properties object from given file path.
        Attributes:
            path - an str representing the file path of the property file.
        Returns: json representation of the Property object."""

        p = Properties()
        p.load(path)
        return p.to_json()

    @staticmethod
    def jsonstr_to_formatable_str(json):
        #ret = json.replace('{', '{{')
        #ret = ret.replace('}', '}}')
        ret = json.replace('%', '%%')
        return ret

    @staticmethod
    def read_allow_types(rules):
        try:
            return rules["inputs"]
        except Exception:
            # No inputs were specified by process, input wont be validated.
            return Utils.ALL_TYPES

    @staticmethod
    def init_inputs(allow):
        inputs = dict()
        inputs["all"] = list()
        for t in allow:
            inputs[t] = list()
        return inputs

    @staticmethod
    def read_input(process, rules):
        allow_types = Utils.read_allow_types(rules)
        inputs = Utils.init_inputs(allow_types)
        try:
            for line in process.read():
                line = json.loads(line)
                t = Utils.validate_type(line, allow_types)
                inputs[t].append(line["value"])
                inputs["all"].append(line["value"])
        except JSONDecodeError as e:
            ErrorHandler.input_type_error("Input must be JSON formatted!", e, allow_types)
        except TypeError as e:
            # Empty input
            pass
        return inputs

    @staticmethod
    def validate_type(line, allow_types):
        try:
            t = line["type"]
        except KeyError as e:
            # TODO better error handling with describe where it should be fixed
            ErrorHandler.input_type_error("Missing type declaration!", e, allow_types)
        if t not in allow_types:
            ErrorHandler.input_type_error("Invalid type declaration!", e, allow_types)
        return t

