import requests

ENDPOINT = ("https://todo.pixegami.io")

def test_can_call_api_todo():
    response = requests.get(ENDPOINT)
    code_response = response.status_code
    assert code_response == 200 

def test_can_create_task():
    req_body = {
                "content": "nakarm kota",
                "user_id": "Iza ma kota",
                "task_id": "007",
                "is_done": False
                }
    response_put = requests.put(ENDPOINT + "/create-task", json = req_body)
    assert response_put.status_code == 200