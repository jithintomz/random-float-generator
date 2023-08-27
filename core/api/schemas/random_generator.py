from core.extensions import ma
from marshmallow import fields


class RandomGeneratorRequestSchema(ma.Schema):
    input_text = fields.Str()
