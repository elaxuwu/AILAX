# AILAX - Your at-home JARVIS-like AI

My personal "room's AI" :-D
I make this for fun (and for [my portfolio](https://elaxuwu.me) too :3 (hi future professor(s)!))

no virus here pookie, dont worry :3

<hr>

# Installation Guide

## Prerequisites
- [Python 3.10](https://www.python.org/downloads/) or higher installed on your machine
- **[Ollama](https://ollama.com/download)** - Download and install the Ollama app for your operating system

## Setup Instructions

### Step 1: Install Ollama
1. Download Ollama from [https://ollama.com/download](https://ollama.com/download)
2. Install Ollama on your system
3. Make sure Ollama is running (it should start automatically after installation)
4. **Login to your Ollama account** (inside the Ollama app) - This is required to use the cloud models

> **Note:** AILAX uses cloud models (`qwen3-vl:235b-instruct-cloud` and `qwen3-coder-next:cloud`) which require an Ollama account. You can switch to local models if you prefer, but they'll run on your local machine and require a good computer.

### Step 2: Run Setup Script
The setup script will **automatically** pull the required AI models, install Python packages, and download OpenWakeWord models.

**For Windows:**
1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Double-click `setup.bat` or run in terminal:
   ```
   .\setup.bat
   ```

**For Mac/Linux:**
1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Make the script executable and run it:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```
   
   Or run directly:
   ```bash
   bash setup.sh
   ```

## What the Setup Script Does
- ✅ Checks if Ollama is installed
- ✅ **Automatically pulls required AI models** (`qwen3-vl:235b-instruct-cloud` and `qwen3-coder-next:cloud`)
- ✅ Installs all required Python packages (ollama, faster-whisper, piper-tts, openwakeword, etc.)
- ✅ Downloads OpenWakeWord models automatically
- ✅ Prepares AILAX to run on your system

## Running AILAX
After setup is complete:
- **Windows**: `python main.py`
- **Mac/Linux**: `python3 main.py` 

<hr>

# License

This software is **licensed** under the **PolyForm Noncommercial License 1.0.**

In simple terms, this is **similar** to **CC BY-NC 4.0**:

    Attribution: You must credit me.

    Non-Commercial: You cannot sell this or use it for business.

See the [LICENSE](LICENSE) file for the full legal text.

<hr>

# Update Logs:

## v1.2:

This patch focus on the Brain (again).

Main Changes:
- Added MEMORY to AILAX! It can now remember what you said! The default limit is 10 interactions, but you can change it in the settings section in main.py!
- That's all... 

## v1.0:

This patch focus on the Brain.

Everything else should be functioning :3

Main Changes:
- Removed all previous mode (private and public)
- Removed all previous models ("gemini 2.5 flash lite" and "llama3.2")

- Added mode switching function, you can now say "switch mode 'mode'" to switch between available modes! (Currently available mode: General mode & Coding mode)
- Added new models for each mode (Gemma 3 for General; Deepseek v3.2 for Coding)

-Updated new system instruction message logic
