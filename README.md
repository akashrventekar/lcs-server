# lcs-server
Simple API that allows users to request Longest Common Substring (LCS) given a list of strings

## Solve LCS problem via HTTP POST

###  Installation and running the application
```
pip3 install -U -r requirements.txt
flask run
```

Request the LCS of a Set of Strings by sending a POST request with the below body to the server at http://127.0.0.1:5000/lcs

**Input:**
```json
{
  "setOfStrings": [
    {"value": "comcast"},
    {"value": "communicate"},
    {"value": "commutation"}
  ]
}
```

**Output:**
```json
{
  "lcs": [
  {
    "value": "com"
  }
  ]
}
```

Sample curl request:
```
curl --location --request POST 'http://127.0.0.1:5000/lcs' \
--header 'Content-Type: application/json' \
--data-raw '{
                    "setOfStrings": [
                        {"value": "comcasttest2"},
                        {"value": "comcastictest2"},
                        {"value": "broadcastertest2"}
                    ]
                }'
```

## Requirements

* If there is no POST body in the request or if the POST body is not in the correct format the
server will respond with a 400 Bad Request HTTP status code, and a response body explaining
that the format of the request was not acceptable.
* If setOfStrings is empty the server will respond with a 400 Bad Request HTTP status code
with a response body explaining that setOfStrings should not be empty.
* If the setOfStrings supplied is not a set (i.e. all strings are not unique) the server will
respond with a a 400 Bad Request HTTP status code, and a response
body explaining that "setOfStrings" must be a Set
* If there is more than one LCS, then the server will return them all in
alphabetic order separated by comma(,).
* Check the tests folder for testing and verifying the functionality of the server by making HTTP
requests and verifying that the responses are appropriate. This can also be changed to the requests library.

## Assumptions
* The input will work for digits and special characters as well. No specific validation is put in to filter out digits or special characters
* The input will be converted to lowercase to make sure that the program is case-insensitive and the output will be returned as lowercase

## Tests
pytests are present in tests folder
