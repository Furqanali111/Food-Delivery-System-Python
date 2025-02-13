<<<<<<< HEAD
# Your code here (the one you're merging now)
import requests
from Schemas import schemas
from EnviornmentVariable import enVVar

def create_token(payload:schemas.auth_payload):
    url =enVVar.CREATE_TOKEN_URL
    response = requests.post(url, json=payload.dict())
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)

def refresh_token(payload:schemas.refresh_token):
    url = enVVar.REFRESH_TOKEN_URL
    response = requests.post(url, json=payload.dict())
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
=======
# Upstream code here (the company's version)
# It might have some changes to the same code you wrote
import requests
from Schemas import schemas
from EnviornmentVariable import enVVar

def create_token(payload:schemas.auth_payload):
    url =enVVar.CREATE_TOKEN_URL
    response = requests.post(url, json=payload.dict())
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)

def refresh_token(payload:schemas.refresh_token):
    url = enVVar.REFRESH_TOKEN_URL
    response = requests.post(url, json=payload.dict())
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
>>>>>>> upstream/master
