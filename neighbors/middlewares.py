
from utils.db import SessionManager


class DatabaseSessionManager():
    def process_request(self, request, response):
        manager = SessionManager()
        request.context['scoped_session'] = manager.get_scoped_session()
        request.context['session'] = manager.get_session()

    def process_response(self, request, response, resource, params=None):
        request.context['session'].close()
        request.context['scoped_session'].remove()
