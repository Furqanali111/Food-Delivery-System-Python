import requests
from Schemas import schemas
from EnviornmentVariable import enVVar

def update_order_status(payload:schemas.order_payload):

    url =enVVar.UPDATE_ORDER_STATUS_URL

    response = requests.post(url, json=payload.dict())

    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)


