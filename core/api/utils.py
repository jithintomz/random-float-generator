"""All utilities used in the api
"""


def string_only_type(value):
    """A custom api paramater validator that validates if the
    input is string.
    Writing this because the default flask_restful string validator converts
    non string value to string

    Args:
        value (Any): The input type which needs to be validated

    Raises:
        ValueError: Errorn representing the type mismatch
    """
    if not isinstance(value, str):
        raise ValueError("Value is not of type string")
