import json
import falcon

from schemas import FindNeighborsSchema
from decorators import LoadJson
import dao.neighbors


class FindNeighborsHandler:
    """Handler for search nearest users"""

    def on_get(self, request, response, coords):
        """
        Search by coords
        """
        limit = request.query_string.get('limit')
        session = request.context.get('session')
        users = dao.neighbors.get_list(session, coords, limit)

        response.body = FindNeighborsSchema().dumps(users, many=True).data
        response.status = falcon.HTTP_200
