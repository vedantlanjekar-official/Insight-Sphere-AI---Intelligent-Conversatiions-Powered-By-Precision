# Insight Sphere AI

A modern, intelligent AI chatbot application built with FastAPI and Ollama, featuring a professional Gemini-inspired web interface. Insight Sphere AI provides an open, versatile AI assistant capable of handling any question or task across multiple domains.

![Insight Sphere AI](https://img.shields.io/badge/AI-Insight%20Sphere-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-teal)
![Ollama](https://img.shields.io/badge/Ollama-Enabled-orange)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setup](#setup)
- [Running the Project](#running-the-project)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
- [Usage Examples](#usage-examples)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## 🎯 Overview

Insight Sphere AI is a full-stack AI chatbot application that combines the power of Ollama's local LLM models with a sleek, modern web interface. The application features:

- **Streaming Responses**: Real-time AI responses as they're generated
- **Professional UI**: Gemini-inspired black and white interface
- **Open Environment**: No topic restrictions - ask anything
- **Modular Architecture**: Clean, maintainable codebase
- **Multiple Launch Options**: CLI, web interface, and automated launchers

## ✨ Features

### Core Features

- 🤖 **Intelligent AI Assistant**: Powered by Ollama with Llama 3 model
- ⚡ **Lightning Fast**: Instant responses to your queries
- 🧠 **Intelligent**: Advanced AI understands context and nuance
- 🌐 **Versatile**: Handles any topic from science to creative writing
- 🔒 **Secure**: Private conversations, no data collection
- ✅ **Accurate**: Reliable information you can trust
- 📡 **Streaming**: Real-time responses as AI thinks
- ♾️ **Unlimited**: No restrictions on topics or questions
- 🕐 **24/7 Available**: Always ready to assist you

### Interface Features

- **Professional Design**: Clean black and white Gemini-inspired interface
- **Responsive Layout**: Works seamlessly on desktop and mobile
- **Smart Formatting**: Automatic point formatting with line breaks
- **Quick Actions**: Pre-defined prompts for common queries
- **Real-time Status**: Online/offline indicators
- **Smooth Animations**: Polished user experience

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

1. **Python 3.8 or higher**
   ```bash
   python --version
   ```

2. **Ollama** - Download and install from [ollama.ai](https://ollama.ai)
   - Windows: Download installer from the website
   - macOS: `brew install ollama` or download from website
   - Linux: `curl -fsSL https://ollama.ai/install.sh | sh`

3. **Git** (optional, for cloning the repository)

## 🚀 Installation

### Step 1: Clone or Download the Project

If you have the project files, navigate to the project directory:
```bash
cd "path/to/Ai chatbot code"
```

### Step 2: Install Python Dependencies

Install the required Python packages:

```bash
pip install fastapi uvicorn ollama
```

Or install all at once:
```bash
pip install -r requirements.txt
```

*(Note: If `requirements.txt` doesn't exist, the packages will be installed automatically when you run the server)*

### Step 3: Setup Ollama

1. **Start Ollama Service**:
   ```bash
   ollama serve
   ```
   Keep this terminal window open. The service runs in the background.

2. **Pull the Llama 3 Model**:
   ```bash
   ollama pull llama3
   ```
   
   This downloads the model (approximately 4.7GB). You can also use other models:
   ```bash
   ollama pull llama3.2
   ollama pull mistral
   ollama pull codellama
   ```

## ⚙️ Setup

### Verify Installation

1. **Check Ollama is running**:
   ```bash
   ollama list
   ```
   You should see `llama3` in the list.

2. **Test Ollama connection**:
   ```bash
   ollama run llama3 "Hello"
   ```

### Configure the Model (Optional)

The default model is `llama3`. To change it, edit `chatbot_module/service.py`:

```python
class OllamaService:
    def __init__(self, model: str = "llama3"):  # Change "llama3" to your preferred model
        self.model = model
        self.system_prompt = INSIGHT_SPHERE_SYSTEM_PROMPT
```

## 🏃 Running the Project

### Method 1: Automated Launcher (Recommended)

**Windows:**
- Double-click `RUN.bat` - This will start the server and open Chrome automatically

**Cross-platform:**
```bash
python launch.py
```

### Method 2: Manual Server Start

1. **Start the Server**:
   ```bash
   python test_server.py
   ```

2. **Open in Browser**:
   - Navigate to `http://127.0.0.1:8000` in your web browser
   - Or use the automated launcher to open Chrome automatically

### Method 3: CLI Interface

For a command-line interface:
```bash
python cli_chat.py
```

### Method 4: Advanced Startup Script

For dependency checking and automatic setup:
```bash
python start.py
```

## 📁 Project Structure

```
Ai chatbot code/
│
├── chatbot_module/          # Core chatbot module
│   ├── __init__.py         # Module initialization
│   ├── prompts.py          # System prompts and AI configuration
│   ├── routes.py           # FastAPI routes and endpoints
│   ├── service.py          # Ollama service integration
│   └── README.md           # Module-specific documentation
│
├── index.html              # Frontend web interface
│
├── test_server.py          # Main FastAPI server
├── cli_chat.py             # Command-line interface
├── launch.py               # Automated launcher script
├── start.py                # Advanced startup script
│
├── RUN.bat                 # Quick launcher (Windows)
├── start.bat               # Alternative launcher (Windows)
│
├── verify_chatbot.py       # Testing script
├── verify_streaming.py     # Streaming test script
├── debug_ollama.py         # Ollama debugging script
│
└── README.md               # This file
```

## 📡 API Documentation

### Base URL
```
http://127.0.0.1:8000
```

### Endpoints

#### 1. Root Endpoint
- **URL**: `/`
- **Method**: `GET`
- **Description**: Serves the web interface
- **Response**: HTML file (`index.html`)

#### 2. Chat Endpoint
- **URL**: `/api/v1/chat`
- **Method**: `POST`
- **Description**: Send a message to the AI and receive a streaming response
- **Content-Type**: `application/json`

**Request Body**:
```json
{
  "message": "Your question or message here",
  "model": "llama3"  // Optional, defaults to llama3
}
```

**Response**:
- **Type**: Streaming text/plain
- **Format**: Real-time text chunks as they're generated

**Example Request** (using curl):
```bash
curl -X POST http://127.0.0.1:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Explain quantum computing"}'
```

**Example Request** (using Python):
```python
import requests

response = requests.post(
    'http://127.0.0.1:8000/api/v1/chat',
    json={'message': 'What is artificial intelligence?'},
    stream=True
)

for chunk in response.iter_content(chunk_size=None):
    if chunk:
        print(chunk.decode('utf-8'), end='')
```

**Example Request** (using JavaScript):
```javascript
const response = await fetch('http://127.0.0.1:8000/api/v1/chat', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ message: 'Hello, how are you?' })
});

const reader = response.body.getReader();
const decoder = new TextDecoder();

while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    
    const chunk = decoder.decode(value, { stream: true });
    console.log(chunk);
}
```

### Error Responses

**400 Bad Request**:
```json
{
  "detail": "Message cannot be empty"
}
```

**500 Internal Server Error**:
- Occurs when Ollama is not running or model is not available
- Check that `ollama serve` is running
- Verify the model is pulled: `ollama list`

## 💡 Usage Examples

### Web Interface

1. Start the server using any method above
2. Open `http://127.0.0.1:8000` in your browser
3. Type your message in the input field
4. Press Enter or click Send
5. Watch the AI response stream in real-time

### CLI Interface

```bash
python cli_chat.py
```

Then type your messages. Type `quit` or `exit` to close.

### Programmatic Usage

#### Python Example
```python
import requests

def chat_with_ai(message):
    response = requests.post(
        'http://127.0.0.1:8000/api/v1/chat',
        json={'message': message},
        stream=True
    )
    
    for chunk in response.iter_content(chunk_size=None):
        if chunk:
            print(chunk.decode('utf-8'), end='', flush=True)
    print()  # Newline at end

# Usage
chat_with_ai("What is machine learning?")
```

#### JavaScript/Node.js Example
```javascript
const fetch = require('node-fetch');

async function chatWithAI(message) {
    const response = await fetch('http://127.0.0.1:8000/api/v1/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message })
    });
    
    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    
    while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        process.stdout.write(decoder.decode(value, { stream: true }));
    }
}

chatWithAI("Explain neural networks");
```

## 🔧 Configuration

### Changing the AI Model

Edit `chatbot_module/service.py`:
```python
def __init__(self, model: str = "llama3"):  # Change to your preferred model
```

Or pass it in the API request:
```json
{
  "message": "Your message",
  "model": "mistral"
}
```

### Changing the Port

Edit `test_server.py`:
```python
uvicorn.run(app, host="127.0.0.1", port=8000)  # Change port number
```

### Modifying System Prompt

Edit `chatbot_module/prompts.py` to customize the AI's behavior and personality.

### Customizing the Interface

Edit `index.html` to modify:
- Colors and styling
- Layout and components
- Features and functionality

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'ollama'"

**Solution**: Install the missing package:
```bash
pip install ollama fastapi uvicorn
```

### Issue: "Error communicating with Ollama"

**Solutions**:
1. Ensure Ollama is running: `ollama serve`
2. Verify the model is pulled: `ollama list`
3. Check Ollama is accessible: `ollama run llama3 "test"`

### Issue: Server won't start

**Solutions**:
1. Check if port 8000 is already in use
2. Change the port in `test_server.py`
3. Ensure all dependencies are installed

### Issue: Chrome doesn't open automatically

**Solutions**:
1. Manually navigate to `http://127.0.0.1:8000`
2. Check Chrome installation path in `launch.py`
3. Use the default browser fallback

### Issue: Responses are slow

**Solutions**:
1. Use a smaller/faster model: `ollama pull llama3.2`
2. Ensure sufficient system resources (RAM, CPU)
3. Close other resource-intensive applications

### Issue: Model not found

**Solution**: Pull the required model:
```bash
ollama pull llama3
```

### Issue: Streaming not working

**Solutions**:
1. Check browser console for errors
2. Verify the API endpoint is correct
3. Ensure the server is running and accessible

## 🎨 Customization

### Adding New Features

1. **New API Endpoints**: Add routes in `chatbot_module/routes.py`
2. **UI Components**: Modify `index.html`
3. **AI Behavior**: Update `chatbot_module/prompts.py`
4. **Service Logic**: Extend `chatbot_module/service.py`

### Styling Changes

The interface uses CSS variables for easy theming. Modify the `:root` section in `index.html`:
```css
:root {
    --black: #000000;
    --white: #ffffff;
    /* Add your custom colors */
}
```

## 📝 Development

### Running in Development Mode

For auto-reload during development:
```bash
uvicorn test_server:app --reload --host 127.0.0.1 --port 8000
```

### Testing

Run the verification scripts:
```bash
python verify_chatbot.py
python verify_streaming.py
```

### Debugging

Use the debug script:
```bash
python debug_ollama.py
```

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available for personal and commercial use.

## 🙏 Acknowledgments

- **Ollama** - For providing local LLM capabilities
- **FastAPI** - For the excellent web framework
- **Llama 3** - For the powerful AI model
- **Google** - For design inspiration (Gemini interface)

## 📞 Support

For issues, questions, or contributions:
- Check the troubleshooting section above
- Review the code comments
- Test with the verification scripts

## 🔮 Future Enhancements

Potential features for future versions:
- [ ] Multi-model support with model switching
- [ ] Conversation history and persistence
- [ ] Export chat functionality
- [ ] Dark/light theme toggle
- [ ] Voice input/output
- [ ] File upload and analysis
- [ ] Code syntax highlighting
- [ ] Markdown rendering
- [ ] Multi-language support

---

**Made with ❤️ using FastAPI, Ollama, and modern web technologies**

*Last updated: 2025*

