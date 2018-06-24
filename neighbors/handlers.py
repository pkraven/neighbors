import json
import falcon

from schemas import CreateUserSchema, ResponseNeighborsSchema
from utils.decorators import LoadJson
# import dao


class UserHandler:
    """Handler for user"""

    @LoadJson(CreateUserSchema)
    def on_post(self, request, response, data):
        """
        Create user
        """
        user = dao.User(request.context.get('session'))

        user.add(data)

        response.status = falcon.HTTP_204


class FindNeighborsHandler:
    """Handler for search nearest users"""

    def on_get(self, request, response, coords):
        """
        Search by coords
        """
        limit = request.query_string.get('limit')

        neighbors = dao.Neighbors(request.context.get('session'))

        users = neighbors.find(session, coords, limit)

        response.body = ResponseNeighborsSchema().dumps(users, many=True).data
        response.status = falcon.HTTP_200