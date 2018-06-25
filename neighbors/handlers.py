import json
import falcon
from marshmallow import ValidationError

from schemas import (
    CoordsUserSchema,
    CreateUserSchema,
    ResponseNeighborsSchema
)
from utils.decorators import LoadJson
from errors import HttpRequestError, UnprocessableEntityError
import dao


class UserHandler:

    @LoadJson(CreateUserSchema)
    def on_post(self, request, response, data: dict):
        """
        add user to database
        :param data: user params dict 'name', 'coord_x', 'coord_y'
        :return:
        """
        user = dao.User(request.context.get('session'))
        user.add(data)

        response.status = falcon.HTTP_201


class FindNeighborsHandler:

    def on_get(self, request, response, coords: str):
        """
        get the nearest users by coordinates
        :param coords: coordinates string '{coord_x},{coord_y}'
        :param limit: max return users /?limit=100
        :return:
        """
        limit = request.params.get('limit')
        limit = int(limit) if limit and limit.isdigit() else 100

        coords = self._get_coords(coords)

        neighbors = dao.Neighbors(request.context.get('session'))
        users = neighbors.find(coords, limit)

        response.body = ResponseNeighborsSchema().dumps(users, many=True).data
        response.status = falcon.HTTP_200
        response.content_type = 'application/json'

    @staticmethod
    def _get_coords(coords: str) -> dict:
        """
        parse and validate coordinates string
        :param coords: coordinates string '{coord_x},{coord_y}'
        :return: coordinates dict 'coord_x', 'coord_y'
        """
        coords = coords.split(',')
        if len(coords) < 2:
            raise HttpRequestError()

        try:
            coords = CoordsUserSchema(strict=True).load({
                "coord_x": coords[0],
                "coord_y": coords[1]
            }).data
        except ValidationError as e:
            raise UnprocessableEntityError(e)

        return coords
