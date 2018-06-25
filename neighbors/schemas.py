from marshmallow import Schema, fields


class CoordsUserSchema(Schema):
    coord_x = fields.Float(required=True, validate=lambda val: -90 < val < 90)
    coord_y = fields.Float(required=True, validate=lambda val: -180 < val < 180)


class CreateUserSchema(CoordsUserSchema):
    name = fields.String(required=True)


class ResponseNeighborsSchema(Schema):
    name = fields.String()
    distance = fields.Integer()
