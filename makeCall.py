import requests
from config import Config

headers = {
    "Authorization": f"Bearer {Config.BOLNA_API_KEY}",
    "Content-Type": "application/json"
}


def initiate_call(to_phone_number, from_phone_number, agent_id, variables, message):
    url = f"{Config.BOLNA_API_URL}/call"

    payload = {
    "agent_id": "123e4567-e89b-12d3-a456-426655440000",
    "recipient_phone_number": "+10123456789",
    "from_phone_number": "+19876543007",
    "user_data": {
        "variable1": "value1",
        "variable2": "value2",
        "variable3": "some phrase as value"
        }
    }
    payload = {
    "agent_id": {agent_id},
    "recipient_phone_number": {to_phone_number},
    "from_phone_number": {from_phone_number},
    "user_data": variables
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

