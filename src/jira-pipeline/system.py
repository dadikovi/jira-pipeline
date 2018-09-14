import requests
import json
from json.decoder import JSONDecodeError
from .exceptions import ErrorHandler
from .jiraapi import *

class System:
    """TODO some methods should be moved to JiraAPI"""

    def __init__(self, config):
        self.config = json.loads(config)
        self.alias = self.config["alias"]
        self._api = JiraAPI()
        self.start_session()

    def get_config(self, alias):
        if alias in self.config:
        	return self.config[alias]
        else:
        	return None

    def start_session(self):
    	self._session = self.create_session()

    def session(self):
    	return self._session

    def api(self):
        return self._api

    def create_session(self):
        sess_id = self.query_session_id()
        session = requests.Session()
        session.auth = self.query_session_id_auth()
        session.verify = False
        session.cookies = requests.cookies.cookiejar_from_dict({ 'JSESSIONID' : sess_id })
        session.headers.update(self.api().get_json_header())
        return session

    def query_session_id(self):
        try:
            response = requests.post(
                self.query_session_id_url(),
                auth = self.query_session_id_auth(),
                verify = False,
                data = self.query_session_id_data(),
                headers = self.api().get_json_header()
            )
            resp_json = json.loads(response.text)
            return resp_json["session"]["value"]
        except JSONDecodeError:
            ErrorHandler.api_error(response.text, self.query_session_id_url())
        except TimeoutError:
            ErrorHandler.connection_timeout_error(self.query_session_id_url())

    def query_session_id_auth(self):
        if self.get_config('username_http'):
            return (
                self.get_config('username_http'),
                self.get_config('password_http')
                )
        else:
            return None

    def query_session_id_url(self):
        url = self.get_config('url_base')
        url = url + self.get_config('url_postfix_auth')
        return url

    def query_session_id_data(self):
        data = dict()
        data["username"] = self.get_config('username')
        data["password"] = self.get_config('password')
        return json.dumps(data)

    def create_full_url(self, url):
        return self.get_config('url_base') + self.get_config('url_postfix_api') + url

    def get(self, url):
        try:
            if url.startswith("http"):
                # Full URL provided
                u = url
            else:
                # The base address of this system is not contained by url
                u = self.create_full_url(url)

            r = self.session().get(u)
            j = json.loads(r.text)
            self.api().verify_response(j)
            return j
        except JSONDecodeError:
            ErrorHandler.api_error(r.text, u)
            return dict()
        except APIError as e:
            ErrorHandler.api_error(e, u)
            return dict()


