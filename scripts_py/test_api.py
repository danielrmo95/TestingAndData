import requests

ENDPOINT = "http://127.0.0.1:8000/getusers"
response = requests.get(ENDPOINT)
print (response)

data = response.json()
print(data)

status_code = response.status_code
print(status_code)

def test():
        response = requests.get(ENDPOINT)
        assert response.status_code == 200