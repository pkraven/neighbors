import json
import logging
from functools import wraps
from marshmallow import ValidationError

from errors import (
    HttpRequestError,
    JSONParseError,
    UnprocessableEntity
)


class LoadJson:
    def __init__(self, schema):
        self.schema = schema(strict=True)

    def __call__(self, f):
        @wraps(f)
        def wrapper(handler, req, resp, *args, **kwargs):
            body = req.context['data']
            if not body:
                raise HttpRequestError()

            try:
                loaded = json.loads(body.decode())
                data = self.schema.load(loaded).data
            except (json.decoder.JSONDecodeError, UnicodeDecodeError, ValueError) as e:
                logging.exception('Exception on message loading')
                raise JSONParseError()
            except ValidationError as e:
                logging.exception('Exception on message validation')
                raise UnprocessableEntity(e)

            return f(handler, req, resp, *args, **kwargs, data=data)

        return wrapper

