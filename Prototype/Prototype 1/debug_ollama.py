import ollama

try:
    print("Attempting to list models...")
    models = ollama.list()
    print("Models found:", models)
except Exception as e:
    print(f"Error: {e}")
