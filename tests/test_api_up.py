import requests


def test_api_running():
    context = "test"
    payload = {
        "context": context,
        "token_max_length": 2,
        "temperature": 0.0,
        "top_p": 0.0,
    }
    response = requests.post(
        "http://api.vicgalle.net:5000/generate", params=payload
    ).json()

    assert len(response["text"]) > 0
