import json

import falcon


class ApplicationError(Exception):
    status = falcon.HTTP_500

    def __init__(self, messages=None):
        self.messages = messages


def exception_handler(exception, request, response, error=None):
    response.status = exception.status
    if exception.messages:
        response.body = json.dumps(exception.messages)


class HttpRequestError(ApplicationError):
    status = falcon.HTTP_400


class JSONParseError(HttpRequestError):
    def __init__(self):
        super().__init__({
            'code': 'json_parse_error',
            'detail': "JSON object is expected"
        })


class NoBodyError(HttpRequestError):
    def __init__(self):
        super().__init__({
            'code': 'empty_body',
            'detail': "Body is expected"
        })


class NotFound(ApplicationError):
    status = falcon.HTTP_404


class UnprocessableEntityError(ApplicationError):
    status = falcon.HTTP_422

    def __init__(self, exception):
        messages = exception.messages
        super().__init__({
            'errors': messages
        })
