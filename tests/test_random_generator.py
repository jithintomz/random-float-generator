"""All tests for random generator module
"""
import uuid


def test_random_gen_generates_correct_output_format(
        client, admin_headers
):
    """Test random generator generates
        A list of float values of 500 length
        The value is different for different output
    """
    response = client.post(
        "api/v1/generate-random-floats",
        json={"input_text": "A sample input"},
        headers=admin_headers
    )
    assert response.status_code == 200
    response_data = response.get_json()

    assert "result" in response_data, "result not found in response"
    assert isinstance(response_data["result"], list), "Reponse is not a list"
    assert len(response_data["result"]), "Response does not contain 500 values"

    assert all(isinstance(value, float) for value in response_data["result"]), "Response contain non float values" # noqa


def test_random_gen_validates_input_data(
        client, admin_headers
):
    """Test if random gen returns validation error status codes
        and messages
    """
    response = client.post(
        "api/v1/generate-random-floats",
        json={},
        headers=admin_headers
    )
    assert response.status_code == 400
    response_data = response.get_json()

    assert response_data["message"]["input_text"] == \
        "Missing required parameter in the JSON body", \
        "Missing paramater error not returned correctly"

    response = client.post(
        "api/v1/generate-random-floats",
        json={"input_text": 123456789},
        headers=admin_headers
    )
    assert response.status_code == 400
    response_data = response.get_json()

    assert response_data["message"]["input_text"] == \
        "Value is not of type string", \
        "The error message for type validation is not returned correctly"


def test_random_gen_output_is_random(
        client, admin_headers
):
    """Test if random gen generates SUFFICIENTLY RANDOM floats
    """

    response_data_1 = client.post(
        "api/v1/generate-random-floats",
        json={"input_text": "A sample input"},
        headers=admin_headers
    ).get_json()

    response_data_2 = client.post(
        "api/v1/generate-random-floats",
        json={"input_text": "A sample input"},
        headers=admin_headers
    ).get_json()

    assert response_data_1 != response_data_2, \
        "The genrated numbers are same for same input"

    random_input_strings = [uuid.uuid4().hex for _ in range(50)]

    response_list = []
    for input_string in random_input_strings:
        response_values = client.post(
            "api/v1/generate-random-floats",
            json={"input_text": input_string},
            headers=admin_headers
        ).get_json()["result"]
        response_list.append(str(response_values))

    assert len(set(response_list)) == len(response_list), \
        "The randoms collide within a small set of sample values"
