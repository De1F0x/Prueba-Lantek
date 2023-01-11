import pytest
import main
import requests
from requests.auth import HTTPBasicAuth

URL = "https://app-academy-neu-codechallenge.azurewebsites.net/api/2d/cut"

def test_no_credentials():
    user = ""
    passw = ""
    request = main.api_request(URL, user, passw)
    assert request.status_code == 401
    
def test_wrong_credentials():
    user = "Pedro"
    passw = "123"
    request = main.api_request(URL, user, passw)
    assert request.status_code == 401
    
def test_good_call_to_endpoint():
    user = "lantekacademy"
    passw = ":cPIi<kyF(=5OXc"
    request = main.api_request(URL, user, passw)
    assert request.status_code == 200
    
def test_resquet_keys():
    keys = ["id", "name", "manufacturer"]
    user = "lantekacademy"
    passw = ":cPIi<kyF(=5OXc"
    request = main.api_request(URL, user, passw)
    for row in request.json():
        assert keys == list(row.keys())
    
