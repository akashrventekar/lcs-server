from flask import abort

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
