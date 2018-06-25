from marshmallow import Schema, fields


class CreateUserSchema(Schema):
    name = fields.String(required=True)
    coord_x = fields.Float(required=True, validate=lambda val: -90 < val < 90)
    coord_y = fields.Float(required=True, validate=lambda val: -180 < val < 180)


class ResponseNeighborsSchema(Schema):
    name = fields.String()
    distance = fields.Float()
