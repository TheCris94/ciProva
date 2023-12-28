from src.stupidCalc import add
import requests

url = 'https://api.github.com/repos/apache/commons-io/pulls'
TOKEN = "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"
header = {"Authorization": "Bearer " + TOKEN}

def test_add():
    i = add(4,5)
    assert i == 9

def test_api():
    response = requests.get(url, headers=header)
    assert response.status_code == 200