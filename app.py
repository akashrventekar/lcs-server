from flask import Flask, jsonify
from flask import request
from helpers.helpers import longest_common_substrings, create_response, validate_request_body

app = Flask(__name__)


@app.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 400


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify(error=str(e)), 405


@app.errorhandler(415)
def unsupported_media_type(e):
    return jsonify(error=str(e)), 415


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
