import falcon

from handlers import UserHandler, FindNeighborsHandler
from middlewares import DatabaseSessionManager
from errors import ApplicationError, exception_handler
from utils.db import SessionManager
from utils.config import get_config


SessionManager(config=get_config()['db'])

api = falcon.API(middleware=[
    DatabaseSessionManager()
])
api.add_error_handler(ApplicationError, exception_handler)

api.add_route('/user/', UserHandler())
api.add_route('/neighbors/{coords}', FindNeighborsHandler())
