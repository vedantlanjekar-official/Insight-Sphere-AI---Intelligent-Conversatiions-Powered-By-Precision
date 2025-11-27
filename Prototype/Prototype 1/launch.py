"""
Simple launcher script that starts the server and opens Chrome automatically
"""
import subprocess
import time
import sys
import os
import webbrowser
from pathlib import Path

def find_chrome():
    """Find Chrome executable path"""
    chrome_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expanduser(r"~\AppData\Local\Google\Chrome\Application\chrome.exe"),
    ]
    for path in chrome_paths:
        if os.path.exists(path):
            return path
    return None

def open_chrome(url):
    """Open Chrome with the given URL"""
    chrome_path = find_chrome()
    if chrome_path:
        subprocess.Popen([chrome_path, url])
        print(f"[OK] Opened Chrome: {url}")
    else:
        webbrowser.open(url)
        print(f"[OK] Opened in default browser: {url}")

if __name__ == "__main__":
    print("=" * 60)
    print("Insight Sphere AI - Auto Launcher")
    print("=" * 60)
    print("\nStarting server...")
    print("Server URL: http://127.0.0.1:8000")
    print("\nOpening Chrome in 3 seconds...\n")
    
    # Change to script directory
    os.chdir(Path(__file__).parent)
    
    # Start server
    server_process = subprocess.Popen(
        [sys.executable, "test_server.py"],
        creationflags=subprocess.CREATE_NEW_CONSOLE if sys.platform == "win32" else 0
    )
    
    # Wait a bit for server to start
    time.sleep(3)
    
    # Open Chrome
    open_chrome("http://127.0.0.1:8000")
    
    print("\n" + "=" * 60)
    print("[OK] Server is running!")
    print("[OK] Chrome has been opened with the chatbot interface")
    print("\nBackend API: http://127.0.0.1:8000/api/v1/chat")
    print("Frontend: http://127.0.0.1:8000")
    print("\nThe server is running in a separate window.")
    print("Close that window to stop the server.")
    print("=" * 60)
    print("\nPress Enter to exit this launcher (server will keep running)...")
    try:
        input()
    except (EOFError, KeyboardInterrupt):
        pass

