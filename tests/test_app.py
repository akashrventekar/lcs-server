import pytest

from app import app
from helpers.helpers import is_substring, longest_common_substrings


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_not_found(client):
    response = client.post('/non-existent')
    assert response.status_code == 404
    assert response.json == {
        'error': '404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.'}


def test_method_not_allowed(client):
    response = client.get('/lcs')
    assert response.status_code == 405
    assert response.json == {'error': '405 Method Not Allowed: The method is not allowed for the requested URL.'}


def test_unsupported_media_type(client):
    response = client.post('/lcs', data="test")
    assert response.status_code == 415
    assert response.json == {
        'error': '415 Unsupported Media Type: Add Content-Type header with value as application/json'}


@pytest.mark.parametrize(
    "request_body, expected_status_code, expected_response_body",
    [
        (
                None,
                400,
                {
                    'error': '400 Bad Request: format of the request is not acceptable. Format: {"setOfStrings": [{"value": "string"}]}'}
        ),
        (
                {},
                400,
                {
                    'error': '400 Bad Request: setOfStrings field not present or empty. Format: {"setOfStrings": [{"value": "string"}]}'}
        ),
        (
                {'setOfStrings': ''},
                400,
                {
                    'error': '400 Bad Request: setOfStrings field not present or empty. Format: {"setOfStrings": [{"value": "string"}]}'}
        ),
        (
                {'setOfStrings': 'Test'},
                400,
                {
                    'error': '400 Bad Request: setOfStrings not of list type. Format: {"setOfStrings": [{"value": "string"}]}'}
        ),
        (
                {'setOfStrings': ['Test', 'Test']},
                400,
                {
                    'error': '400 Bad Request: setOfStrings must be a set'}
        ),
        (
                {
                    'setOfStrings': [
                        {"value": "comcasttest"},
                        {"value": "comcastictest"},
                        {"value": "broadcastertest"}
                    ]
                },
                200,
                {
                    "lcs": [
                        {"value": "cast,test"}
                    ]
                }
        ),
        (
                {
                    'setOfStrings': [
                        {"value": "comcast"},
                        {"value": "communicate"},
                        {"value": "commutation"}
                    ]
                },
                200,
                {
                    "lcs": [
                        {"value": "com"}
                    ]
                }
        ),
        (
                {
                    'setOfStrings': [
                        {"value": "Comcast"},
                        {"value": "Communicate"},
                        {"value": "Commutation"}
                    ]
                },
                200,
                {
                    "lcs": [
                        {"value": "com"}
                    ]
                }
        ),

    ]
)
def test_post_request(client, request_body, expected_status_code, expected_response_body):
    response = client.post('/lcs', headers={"Content-Type": "application/json"}, json=request_body)
    assert response.status_code == expected_status_code
    assert response.json == expected_response_body


@pytest.mark.parametrize(
    "find_string, strings, expected_response",
    [
        (
                "",
                [],
                False
        ),
        (
                "",
                [""],
                True
        ),
        (
                "t",
                [""],
                False
        ),
        (
                "t",
                ["t"],
                True
        ),
        (
                "test",
                ["tes"],
                False
        ),
        (
                "test",
                ["test1"],
                True
        ),
    ]
)
def test_is_substring(find_string, strings, expected_response):
    actual_response = is_substring(find_string, strings)
    assert actual_response == expected_response


@pytest.mark.parametrize(
    "list_of_input_strings, expected_response",
    [
        (
                [],
                []
        ),
        (
                [''],
                ['']
        ),
        (
                ['Test'],
                ['Test']
        ),
        (
                ['Test1'],
                ['Test1']
        ),
        (
                ['test1'],
                ['test1']
        ),
        (
                ['Aston Martin'],
                ['Aston Martin']
        ),
        (
                ['', 'Aston Martin'],
                ['']
        ),
        (
                ['A', 'Aston Martin'],
                ['A']
        ),
        (
                ['As', 'Aston Martin'],
                ['As']
        ),
        (
                ['Aston Martin', 'As'],
                ['As']
        ),
        (
                ['Aston Martin', 'Aston '],
                ['Aston ']
        ),
    ]
)
def test_longest_common_substrings(list_of_input_strings, expected_response):
    actual_response = longest_common_substrings(input=list_of_input_strings)
    assert actual_response == expected_response
