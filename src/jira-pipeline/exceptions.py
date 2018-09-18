class UnexpectedInputException(Exception):
    pass

class APIError(Exception):
    pass

class PipelineStopException(Exception):
    pass

class ErrorHandler():
    @staticmethod
    def api_error(response, url):
        print("[ERROR] Unexpected response for request!")
        print("[ERROR] URL: " + url)
        print("[ERROR]" + str(response))
        raise PipelineStopException()

    @staticmethod
    def connection_timeout_error(url):
        print("[ERROR] Connection failed because of timeout!")
        print("[ERROR] URL: " + url)
        raise PipelineStopException()

    @staticmethod
    def error(msg, e):
        print("[ERROR] " + msg)
        print(str(e))
        raise PipelineStopException()

    @staticmethod
    def input_type_error(msg, e, valid):
        print("[ERROR] Invalid input for process: " + msg)
        print("[ERROR] Possible valid types: " + str(valid))
        print(str(e))
        raise PipelineStopException()