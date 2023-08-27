"""Resources of random generator application
"""
import random
import sys

from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from core.api.utils import string_only_type


class GenerateRandomFloats(Resource):
    """
    ---
    post:
      tags:
        - api
      summary: Generate random floats from string
      description: Generate a list of random floats given a text input
      requestBody:
        content:
          application/json:
            schema:
              RandomGeneratorRequestSchema
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  result:
                    type: List[float]
                    example: [
                        -1.9053262812964352e+18,
                        ...
                        -8.689205877287778e+18,
                    ]
    """
    method_decorators = [jwt_required()]

    def post(self):
        """Generate a list of random floats given a text input
        """
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(
            "input_text", location="json", required=True,
            type=string_only_type, nullable=False
        )
        # Parsing args to trigger validation even if args are unused
        parser.parse_args()

        size_of_list = 500
        upper_limit = sys.maxsize
        lower_limit = upper_limit * -1

        random_floats = [
            random.uniform(lower_limit, upper_limit)
            for _ in range(size_of_list)
        ]

        return {
            "result": random_floats
        }
