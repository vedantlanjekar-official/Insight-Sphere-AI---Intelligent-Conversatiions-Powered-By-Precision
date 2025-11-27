import requests
import sys

API_URL = "http://127.0.0.1:8000/api/v1/chat"

def main():
    print("="*50)
    print("Insight Sphere AI CLI (Type 'quit' to exit)")
    print("="*50)

    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ['quit', 'exit']:
                print("Goodbye!")
                break
            
            if not user_input.strip():
                continue

            # Send request to the server
            try:
                print("AI: ", end="", flush=True)
                with requests.post(API_URL, json={"message": user_input}, stream=True) as response:
                    if response.status_code == 200:
                        for chunk in response.iter_content(chunk_size=None):
                            if chunk:
                                text = chunk.decode('utf-8')
                                print(text, end="", flush=True)
                        print() # Newline at the end
                    else:
                        print(f"\nError: Server returned {response.status_code} - {response.text}")
            except requests.exceptions.ConnectionError:
                print("\nError: Could not connect to the server. Is test_server.py running?")
        
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
