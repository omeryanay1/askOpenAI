import pytest
import requests

def test_ask():
    url = 'http://127.0.0.1:5001/ask'
    data = {
       "question" : "what is the capital of israel?" 
    }
    response = requests.post(url,json=data)
    assert response.status_code == 201
    data_res = response.json()
    assert 'answer' in data_res
    assert data_res['answer'] == 'Jerusalem'
    
