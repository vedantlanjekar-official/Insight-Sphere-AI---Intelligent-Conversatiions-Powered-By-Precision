import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from chatbot_module.routes import router as chatbot_router

app = FastAPI(title="Insight Sphere AI", description="Intelligent AI Assistant")

# Mount the chatbot router
app.include_router(chatbot_router, prefix="/api/v1")

@app.get("/")
def root():
    return FileResponse("index.html")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
