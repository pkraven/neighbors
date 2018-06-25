from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Column, Text, Integer
from geoalchemy2 import Geometry


@as_declarative()
class BaseModel():
    @declared_attr
    def __tablename__(self):
        return self.__name__.lower()


class Users(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    coords = Column(Geometry(geometry_type='POINT', srid=4326), nullable=False)
