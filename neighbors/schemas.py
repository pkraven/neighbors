from marshmallow import Schema, fields


class CreateUserSchema(Schema):
    name = fields.String(required=True)
    coord_x = fields.Float(required=True)
    coord_y = fields.Float(required=True)


class ResponseNeighborsSchema(Schema):
    name = fields.String()
    distance = fields.Float()
