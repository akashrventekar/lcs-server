from flask import Flask, jsonify, abort
from flask import request
import json

app = Flask(__name__)


@app.errorhandler(400)
def resource_not_found(e):
    return jsonify(error=str(e)), 400


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.errorhandler(405)
def resource_not_found(e):
    return jsonify(error=str(e)), 405


@app.errorhandler(415)
def resource_not_found(e):
    return jsonify(error=str(e)), 415


def validate_request_body(input):
    if not input.is_json:
        abort(415, description="Add Content-Type header with value as application/json")
    elif not input.data:
        abort(400, description='format of the request is not acceptable. Format: {"setOfStrings": [{"value": "string"}]}')
    elif input.is_json:
        request_body_json = input.get_json()
        strings = request_body_json.get('setOfStrings')
        if not strings:
            abort(400, description='setOfStrings field not present or empty. Format: {"setOfStrings": [{"value": "string"}]}')
        elif not isinstance(strings, list):
            abort(400, description='setOfStrings not of list type. Format: {"setOfStrings": [{"value": "string"}]}')
        elif len(strings) != len(set(str(string) for string in strings)):
            abort(400, description="setOfStrings must be a set")



def create_response(answer):
    return {
        "lcs": [
            {"value": answer}
        ]
    }


@app.route("/lcs", methods=['POST'])
def compute_lcs():
    validate_request_body(input=request)

    set_of_strings_value = request.json.get('setOfStrings')

    # If capital letters are provided, then convert them to lower case
    list_of_input_strings = [string['value'].lower() for string in set_of_strings_value]
    lcs_list = longest_common_substrings(input=list_of_input_strings)
    lcs_list.sort()
    comma_separated_lcs_string = ",".join(lcs_list)
    return create_response(answer=comma_separated_lcs_string)


def longest_common_substrings(input):
    substr = ['']
    if not input or len(input) == 1:
        return input

    if len(input) > 1 and input[0]:
        for i in range(len(input[0])):
            for j in range(len(input[0]) - i + 1):
                if j > len(substr[0]) and is_substring(input[0][i:i + j], input):
                    substr = [input[0][i:i + j]]
                elif j == len(substr[0]) and is_substring(input[0][i:i + j], input):
                    substr.append(input[0][i:i + j])
    return substr


def is_substring(find_string, strings):
    if not strings and not find_string:
        return False
    for string in strings:
        if find_string not in string:
            return False
    return True
