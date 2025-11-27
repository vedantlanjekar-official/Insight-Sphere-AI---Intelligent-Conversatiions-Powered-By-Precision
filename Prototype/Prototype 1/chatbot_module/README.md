# Chatbot Module Integration

## Overview
This module provides an AI chatbot powered by Ollama (Llama 3). It is built using FastAPI.

## Prerequisites
1.  **Ollama**: Must be installed and running (`ollama serve`).
2.  **Model**: The `llama3` model must be pulled (`ollama pull llama3`).
3.  **Python Packages**: `ollama`, `fastapi`, `uvicorn`.

## Integration Steps

To add this module to your main Insight Sphere AI application (`app.py` or `main.py`):

1.  **Copy the folder**: Move the `chatbot_module` folder into your project root.
2.  **Add these 2 lines** to your main FastAPI app:

```python
from chatbot_module.routes import router as chatbot_router
app.include_router(chatbot_router, prefix="/api/v1")
```

*(Note: You can change `prefix="/api/v1"` to whatever path you prefer, e.g., `/chat`)*

## Testing
You can test the module independently using the provided `test_server.py`:
```bash
python test_server.py
```
Then send a POST request to `http://127.0.0.1:8000/api/v1/chat`.
