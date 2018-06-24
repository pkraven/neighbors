from functools import wraps
from amqp_client import Message

from errors import BadContentType
from utils.config import get_config
from utils.db import SessionManager


class DatabaseSessionManager():
    def process_request(self, request, response):
        manager = SessionManager(config=get_config()['db'])
        request.context['scoped_session'] = manager.get_scoped_session()
        request.context['session'] = manager.get_session()

    def process_response(self, request, response, resource, params=None):
        request.context['session'].close()
        request.context['scoped_session'].remove()
