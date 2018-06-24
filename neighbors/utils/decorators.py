import json
import logging
from functools import wraps
from marshmallow import ValidationError

from errors import (
    NoBodyError,
    JSONParseError,
    UnprocessableEntityError
)


class LoadJson:
    def __init__(self, schema):
        self.schema = schema(strict=True)

    def __call__(self, func):
        @wraps(func)
        def wrapper(handler, req, resp, *args, **kwargs):
            body = req.bounded_stream.read()
            if not body:
                raise NoBodyError()

            try:
                loaded = json.loads(body.decode())
                data = self.schema.load(loaded).data
            except (json.decoder.JSONDecodeError, UnicodeDecodeError, ValueError):
                raise JSONParseError()
            except ValidationError as e:
                raise UnprocessableEntityError(e)

            return func(handler, req, resp, *args, **kwargs, data=data)

        return wrapper
