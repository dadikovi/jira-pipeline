from .exceptions import APIError

class JiraAPI:
    """Each JIRA API - specific thing goes here. The goal is,
    that if JIRA API changes, only this file has to be changed."""

    ISSUE = "issue"
    ISSUES = "issues"
    SELF = "self"
    ISSUE_PREFIX = ISSUE + "/"
    TRANSITIONS = "/transitions"
    ASSIGNEE = "/assignee"
    ATTACHMENTS = "/attachments"
    SEARCH_URL_PREFIX = "search?jql="
    ERROR_MESSAGES = "errorMessages"
    ERRORS = "errors"

    def get_json_header(self):
        return {'Content-Type':'application/json'}

    # URLs
    def search_url(self, jql):
        return JiraAPI.SEARCH_URL_PREFIX + jql
    def issue_put_url(self):
        return JiraAPI.ISSUE
    def issue_get_url(self, key):
        return JiraAPI.ISSUE_PREFIX + key
    def transition_url(self, id):
        return JiraAPI.ISSUE_PREFIX + id + JiraAPI.TRANSITIONS
    def assignee_url(self, id):
        return JiraAPI.ISSUE_PREFIX + id + JiraAPI.ASSIGNEE
    def attach_file_url(self, key):
        return JiraAPI.ISSUE_PREFIX + key + JiraAPI.ATTACHMENTS

    # Parse methods

    def parse_issue_links(self, json):
        """Parses the response for a JQL search query 
        and returns a list of issue links."""

        links = []

        if JiraAPI.ISSUES in json:            
            for issue in json[JiraAPI.ISSUES]:
                links.append(issue[JiraAPI.SELF])
            
        return links

    # Other actions

    def verify_response(self, json):
        """Parses errors and error messages in provided JSON"""
        if JiraAPI.ERROR_MESSAGES in json:
            raise APIError(str(json[JiraAPI.ERROR_MESSAGES]))
        if JiraAPI.ERRORS in json:
            raise APIError("Error without message in response: " + str(json[JiraAPI.ERRORS]))