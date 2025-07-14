import requests
x = requests.get("https://todo.pixegami.io")
print(x) #response 200

import requests

ENDPOINT = "https://todo.pixegami.io"

def test_can_call_api():
    response = requests.get(url=ENDPOINT)
    code_response = response.status_code
    assert code_response == 200

def test_api_returns_404_for_bad_url():
    """GET https://todo.pixegami.io/status
       should return 404 """
    response = requests.get(url=ENDPOINT + "/status")
    assert response.status_code == 404

def test_api_returns_hello_msg():
    """Body should return hello world... msg
       '{"message":"Hello World from Todo API"}'"""
    expected = "Hello World from Todo API"
    response = requests.get(url=ENDPOINT)
    body = response.json()
    # print(body)
    # print(expected)
    assert expected == body["message"]

def test_api_returns_not_found_for_bad_url():
    """
    1. get response for GET https://todo.pixegami.io/status
    2. get body from response
    3. body should contain "Not Found"
    body: {"detail":"Not Found"}
    """
    pass