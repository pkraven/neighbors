import json
import falcon

from schemas import CreateUserSchema
from utils.decorators import LoadJson
import dao.users


class UserHandler:
    """Handler for user"""

    @LoadJson(CreateUserSchema)
    def on_post(self, request, response, data):
        """
        Create user
        """
        session = request.context.get('session')

        dao.users.add(session)

        response.status = falcon.HTTP_204
