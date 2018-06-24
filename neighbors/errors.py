import json
import logging

import falcon


class ApplicationError(Exception):
    """
    Custom errors base class
    """
    error = {
        'status': falcon.HTTP_500,
        'detail': 'Unhandled exception'
    }

    def __init__(self, messages=None):
        if messages is None:
            self.messages = {'errors': []}
        elif isinstance(messages, dict) and not messages.get('errors'):
            self.messages = {'errors': [messages]}
        else:
            self.messages = messages

    @staticmethod
    def handle(exception, req, resp, error=None):
        resp.status = exception.error.get('status', falcon.HTTP_500)
        resp.body = json.dumps(exception.messages)


class HttpRequestError(ApplicationError):
    error = {'status': falcon.HTTP_400}


class JSONParseError(HttpRequestError):
    def __init__(self):
        super().__init__({
            'code': 'json_parse_error',
            'detail': "JSON object is expected"
        })


class NotFound(ApplicationError):
    error = {'status': falcon.HTTP_404}


class UnprocessableEntity(ApplicationError):
    error = {'status': falcon.HTTP_422}

    def __init__(self, exception):
        messages = exception.messages
        super().__init__({'errors': messages})

