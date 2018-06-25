

class MiddlewareSessionManager():
    def __init__(self, session_manager):
        self.session_manager = session_manager

    def process_request(self, request, response):
        request.context['scoped_session'] = self.session_manager.get_scoped_session()
        request.context['session'] = self.session_manager.get_session()

    def process_response(self, request, response, resource, params=None):
        request.context['session'].close()
        request.context['scoped_session'].remove()
