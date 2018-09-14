from briefly.properties import *

class Utils:

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