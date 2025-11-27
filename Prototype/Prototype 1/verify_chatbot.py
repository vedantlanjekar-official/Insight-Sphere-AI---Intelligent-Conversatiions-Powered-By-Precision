import requests
import json

url = "http://127.0.0.1:8000/api/v1/chat"
payload = {"message": "Hello, who are you?"}
headers = {"Content-Type": "application/json"}

try:
    response = requests.post(url, json=payload, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")
