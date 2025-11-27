"""
Automatic startup script for Insight Sphere AI
This script starts the FastAPI server and opens Google Chrome automatically
"""
import subprocess
import time
import sys
import os
import webbrowser
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import fastapi
        import uvicorn
        import ollama
        return True
    except ImportError as e:
        print(f"Missing dependency: {e}")
        print("Installing required packages...")
        subprocess.run([sys.executable, "-m", "pip", "install", "fastapi", "uvicorn", "ollama"], check=True)
        return True

def check_ollama_running():
    """Check if Ollama service is running"""
    try:
        import ollama
        # Try to list models to check if Ollama is accessible
        ollama.list()
        return True
    except Exception as e:
        print(f"Warning: Could not connect to Ollama: {e}")
        print("Please make sure Ollama is installed and running.")
        print("You can start it with: ollama serve")
        return False

def start_server():
    """Start the FastAPI server"""
    print("=" * 60)
    print("Starting Insight Sphere AI Server...")
    print("=" * 60)
    
    # Change to script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    # Import and run the server
    import uvicorn
    from fastapi import FastAPI
    from fastapi.responses import FileResponse
    from fastapi.staticfiles import StaticFiles
    from chatbot_module.routes import router as chatbot_router
    
    app = FastAPI(title="Insight Sphere AI")
    
    # Mount the chatbot router
    app.include_router(chatbot_router, prefix="/api/v1")
    
    # Serve the HTML file
    @app.get("/")
    def root():
        return FileResponse("index.html")
    
    # Wait a moment for server to start, then open browser
    def open_browser():
        time.sleep(2)
        url = "http://127.0.0.1:8000"
        print(f"\n✓ Server is running at {url}")
        print("Opening in Google Chrome...")
        
        # Try to open in Chrome specifically
        chrome_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            os.path.expanduser(r"~\AppData\Local\Google\Chrome\Application\chrome.exe"),
        ]
        
        chrome_found = False
        for chrome_path in chrome_paths:
            if os.path.exists(chrome_path):
                subprocess.Popen([chrome_path, url])
                chrome_found = True
                break
        
        if not chrome_found:
            # Fallback to default browser
            webbrowser.open(url)
            print("Opened in default browser (Chrome not found in standard locations)")
    
    # Start browser opening in background
    import threading
    browser_thread = threading.Thread(target=open_browser, daemon=True)
    browser_thread.start()
    
    print("\nServer starting on http://127.0.0.1:8000")
    print("Press Ctrl+C to stop the server\n")
    
    # Run the server
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")

if __name__ == "__main__":
    try:
        # Check dependencies
        if not check_dependencies():
            sys.exit(1)
        
        # Check Ollama (warning only, don't block)
        check_ollama_running()
        
        # Start server
        start_server()
    except KeyboardInterrupt:
        print("\n\nServer stopped by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nError starting server: {e}")
        sys.exit(1)

