from marshmallow import Schema, fields


class CurrentUserSchema(Schema):
    """ JSON Serializer for current user. """

    id = fields.Int()
    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Str()


current_user_schema = CurrentUserSchema()
