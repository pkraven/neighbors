from models import Users


class User:
    def __init__(self, session):
        self.session = session

    def add(self, data: dict):
        instance = Users(
            name=data['name'],
            coords=f"SRID=4326;POINT({data['coord_y']} {data['coord_x']})"
        )
        self.session.add(instance)
        self.session.commit()
