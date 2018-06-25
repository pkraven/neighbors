import geoalchemy2.functions as geofunc
from sqlalchemy import func

from models import Users


class User:
    def __init__(self, session):
        self.session = session

    def add(self, data: dict):
        """
        add user to database
        :param data: user params dict 'name', 'coord_x', 'coord_y'
        :return:
        """
        instance = Users(
            name=data['name'],
            coords=f"SRID=4326;POINT({data['coord_y']} {data['coord_x']})"
        )
        self.session.add(instance)
        self.session.commit()


class Neighbors:
    def __init__(self, session):
        self.session = session

    def find(self, coords: dict, limit: int) -> list:
        """
        get the nearest users by coordinates and sort
        :param coords: coordinates dict 'coord_x', 'coord_y'
        :param limit: max users
        :return: list sorted users
        """
        distance = func.round(geofunc.ST_Distance_Sphere(
            Users.coords,
            f"SRID=4326;POINT({coords['coord_y']} {coords['coord_x']})"
        )).label('distance')
        users = self.session.query(Users.name, distance) \
                            .order_by('distance').limit(limit).all()

        return users
