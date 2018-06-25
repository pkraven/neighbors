import falcon

from handlers import UserHandler, FindNeighborsHandler
from middlewares import MiddlewareSessionManager
from errors import ApplicationError, exception_handler
from utils.db import SessionManager
from utils.config import get_config


# middleware
api = falcon.API(middleware=[
    MiddlewareSessionManager(
        session_manager=SessionManager(config=get_config()['db'])
    )
])

api.add_error_handler(ApplicationError, exception_handler)

# routes
api.add_route('/user', UserHandler())
api.add_route('/neighbors/{coords}', FindNeighborsHandler())
