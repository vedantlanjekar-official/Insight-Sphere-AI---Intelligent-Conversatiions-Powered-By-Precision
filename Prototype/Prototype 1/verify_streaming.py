import requests
import time

url = "http://127.0.0.1:8000/api/v1/chat"
payload = {"message": "Count to 5."}

print("Sending request...")
start_time = time.time()
with requests.post(url, json=payload, stream=True) as response:
    if response.status_code == 200:
        print("Response stream started.")
        for chunk in response.iter_content(chunk_size=None):
            if chunk:
                print(f"Chunk received: {chunk.decode('utf-8')}")
    else:
        print(f"Error: {response.status_code}")

print(f"\nTotal time: {time.time() - start_time:.2f}s")
