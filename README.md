# lcs-server
Simple App that allows users to request Longest Common Substring (LCS) given a list of strings

## Solve LCS problem via HTTP POST

###  Running the application
```
pip3 install -U -r requirements.txt
flask run
```

Request the LCS of a Set of Strings by sending a POST request with the below body to the server at http://127.0.0.1:5000/lcs

```json
{
  "setOfStrings": [
    {"value": "comcast"},
    {"value": "communicate"},
    {"value": "commutation"}
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

## Assumptions
* The input will work for digits and special characters as well. No specific validation is put in to filter out digits or special characters
* The input will be converted to lowercase to make sure that the program is case-insensitive and the output will be returned as lowercase

# Tests
pytests are present in tests folder
