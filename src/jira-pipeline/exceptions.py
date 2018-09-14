class UnexpectedInputException(Exception):
    pass

class APIError(Exception):
    pass

class ErrorHandler():
    @staticmethod
    def api_error(response, url):
        print("[ERROR] Unexpected response for request!")
        print("[ERROR] URL: " + url)
        print("[ERROR]" + str(response))

    @staticmethod
    def connection_timeout_error(url):
        print("[ERROR] Connection failed because of timeout!")
        print("[ERROR] URL: " + url)

    @staticmethod
    def error(msg, e):
        print("[ERROR] " + msg)
        print(str(e))