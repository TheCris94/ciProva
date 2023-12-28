import pytest
import xml.etree.ElementTree as ET
from src.stupidCalc import add
import requests

url = 'https://api.github.com/repos/apache/commons-io/pulls'


# @pytest.fixture
# def github_token():
#     return "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"


def test_add():
    i = add(4, 5)
    assert i == 9


def test_api():
    tree = ET.parse('config.xml')
    root = tree.getroot()
    token = "".join(root[0].text.split())
    header = {"Authorization": "Bearer " + token}
    response = requests.get(url, headers=header)
    assert response.status_code == 200
