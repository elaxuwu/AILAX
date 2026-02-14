# AILAX - Your at-home JARVIS-like AI

My personal "room's AI" :-D
I make this for fun (and for [my portfolio](https://elaxuwu.me) too :3 (hi future professor(s)!))

no virus here pookie, dont worry :3

and also please check out [my profile](https://elaxuwu.me.)!

thank you!

<hr>

## 📑 Table of Contents

1. [Installation Guide](#installation-guide)
   - [Prerequisites](#prerequisites)
   - [Setup Instructions](#setup-instructions)
   - [What the Setup Script Does](#what-the-setup-script-does)

2. [Running AILAX](#running-ailax)
   - [Quick Start](#quick-start)
   - [How to Use AILAX](#how-to-use-ailax)
   - [AI Modes](#ai-modes)
   - [Memory](#memory)

3. [Customization & Settings](#customization--settings)
   - [1. Change the AI Personality](#1-change-the-ai-personality-)
   - [2. Switch AI Models](#2-switch-ai-models-)
   - [3. Adjust Speech Speed](#3-adjust-speech-speed-)
   - [4. Adjust Speech Recognition](#4-adjust-speech-recognition-)
   - [5. Change Recording Duration](#5-change-recording-duration-)
   - [6. Change Memory Limit](#6-change-memory-limit-)
   - [7. Add Custom Voice Models](#7-add-custom-voice-models-)
   - [8. Add Custom Voice Commands](#8-add-custom-voice-commands-)
   - [9. Change Audio Device](#9-change-audio-device-)
   - [10. Customize Startup Messages](#10-customize-startup-messages-)
   - [11. Setup Custom Wake Word](#11-setup-custom-wake-word-)
   - [Configuration Summary](#configuration-summary)

4. [Troubleshooting](#troubleshooting)
   - [Setup Issues](#setup-issues)
   - [Startup Issues](#startup-issues)
   - [Runtime Issues](#runtime-issues)
   - [Model Issues](#model-issues)

5. [File Structure](#file-structure)

6. [License](#license)

7. [Update Logs](#update-logs)

<hr>

# Installation Guide

## Prerequisites
- [Python 3.10](https://www.python.org/downloads/) or higher _- of course bro, this is a Python project..._
- **[Ollama](https://ollama.com/download)** _- for running AI models (locally or cloud)_
- Internet connection _- i think you have this already 😊_
- Microphone and speakers _- do I even have to explain..._

## Setup Instructions

### Step 1: Install Ollama
1. Download Ollama from [https://ollama.com/download](https://ollama.com/download)
2. Install Ollama on your system
3. Make sure Ollama is running (it should start automatically after installation)
4. **Login to your Ollama account** (inside the Ollama app) - This is required to use the cloud models

> **Note:** AILAX uses cloud models (`qwen3-vl:235b-instruct-cloud` and `qwen3-coder-next:cloud`) which require an Ollama account. You can switch to local models if you prefer, but they'll run on your local machine and require a good computer.

### Step 2: Clone the Repository
```bash
git clone https://github.com/yourusername/AILAX.git
cd AILAX
```

Or download the ZIP from [GitHub releases](https://github.com/elaxuwu/AILAX/releases)(yes, this link, use latest stable version) and extract it. (pls use stable version, i don't have trust in BETAs)

### Step 3: Run the Automatic Setup Script
The setup script will **automatically**:
- ✅ Verify Ollama is installed
- ✅ Pull required AI models from Ollama
- ✅ Install all Python dependencies
- ✅ Download OpenWakeWord models

**For Windows:**
1. Double-click `setup.bat` or run in terminal:
   ```
   .\setup.bat
   ```

**For Mac/Linux:**
1. Make the script executable and run:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

## What the Setup Script Does
- ✅ **Checks if Ollama is installed** - Ensures AI models can be pulled
- ✅ **Verifies Python 3.10+** - Required for all dependencies
- ✅ **Pulls required AI models** - `qwen3-vl:235b-instruct-cloud` (General mode) and `qwen3-coder-next:cloud` (Coding mode)
- ✅ **Installs Python packages** - All dependencies from `requirements.txt`
- ✅ **Downloads OpenWakeWord models** - For future voice activation features

## Running AILAX

### Quick Start
After setup is complete, simply run:
- **Windows**: `python main.py`
- **Mac/Linux**: `python3 main.py`

### How to Use AILAX
1. **Startup Check**: AILAX will verify that all components (EARS, MOUTH, BRAIN) are ready
2. **Wait for prompt**: You'll see "Press ENTER to speak your command or 'q' to quit!"
3. **Record audio**: Press ENTER to start recording (records for ~5 seconds)
4. **Get response**: AILAX will transcribe your speech and respond using AI
5. **Exit**: Type 'q' and press ENTER to quit

### AI Modes
AILAX currently have two modes:
- **General Mode** (default): Uses `qwen3-vl:235b-instruct-cloud` for general conversations
- **Coding Mode**: Uses `qwen3-coder-next:cloud` for programming assistance

You can switch modes by saying: `"switch mode coding"` or `"switch mode general"`!

### Memory
By default, AILAX  remembers your last 10 interactions! Clear memory by saying: `"clear memory"` or `"reset memory"`
Go to [6. Change Memory Limit](#6-change-memory-limit-) to change how many interactions AILAX can remember!

## Customization & Settings

Make AILAX your own slav-...I mean AI assistant (pls don't hurt me when yall invade earth...)! Here's how to customize various aspects:

_(Note: Tell me you know basic coding and Python before reading these stuff...pwease...?)_

### 1. **Change the AI Personality** 📝
Edit `body_parts/dabrain.py` and modify the `GLOBAL_PERSONALITY` variable:

```python
# Line 27-32 in dabrain.py
GLOBAL_PERSONALITY = (
    "You are a helpful personal assistant named AILAX, you are a friend of the user, "
    "their name is elax. You assist with many tasks and speak naturally. "
    "Anything you write will be spoken out loud, so avoid formatting and be concise, also don't use emojis or icons. "
    "Answer as short as possible while being informative and helpful. "
    "There are two modes: General and Coding."
)
```

**Example customizations:**
- Change the AI's name: `"named AILAX"` → `"named JARVIS"`
- Change the user's name: `"their name is elax"` → `"their name is John"`
- Add personality traits: `"You are sarcastic and funny"` or `"You are professional and formal"`
- Add role: `"You are a Python expert"` or `"You are a motivational coach"`

### 2. **Switch AI Models** 🤖
_⚠️(It is recommended to use the default models cuz I've tested lots of different models and picked out the best ones, but you can switch to other Ollama models if you want!)⚠️_

Edit `body_parts/dabrain.py` to use different Ollama models:

```python
# Line 37-38 in dabrain.py
GENERAL_MODEL = "qwen3-vl:235b-instruct-cloud"  # Change this
CODING_MODEL = "qwen3-coder-next:cloud"         # Change this
```

**Available models (pull them first):**

View all available models on [this link](https://ollama.com/search)!

**Example** on how to pull models:
```bash
ollama pull glm-5:cloud
ollama pull llama3.2
ollama pull translategemma:12b
ollama pull glm-4.7-flash:latest
# THESE ARE JUST EXAMPLES!
```

Then update the variables (example):
```python
GENERAL_MODEL = "glm-4.7-flash:latest"
CODING_MODEL = "llama3.2"
# THESE ARE ALSO EXAMPLES!
```

### 3. **Adjust Speech Speed** 🎙️
Edit `body_parts/mouth.py` to change how fast AILAX speaks:

```python
# Line 17 in mouth.py
SPEAKING_SPEED = 0.7  # Range: 0.5 (very fast) to 1.5 (very slow)
```

**Speed guide:**
- `0.5` - Very fasttttttt, like an auctioneer
- `0.7` - Default, natural speed (at least for me)
- `1.0` - Slower, more deliberate 
- `1.5` - Very slow, for clarity (trust, you dont wanna try this out)

### 4. **Adjust Speech Recognition** 🎧
Edit `body_parts/hearing.py` to change audio settings:

```python
# Line 12 in hearing.py
model_size = "base"  # Change this - options: tiny, base, small, medium, large
```

**Model sizes:**
- `"tiny"` - Fastest, least accurate, uses ~1GB RAM
- `"base"` - Default, good balance, uses ~1GB RAM
- `"small"` - More accurate, uses ~2GB RAM
- `"medium"` - Very accurate, uses ~5GB RAM
- `"large"` - Most accurate, uses ~10GB RAM

### 5. **Change Recording Duration** ⏱️
Edit `body_parts/hearing.py` to change how long AILAX listens:

```python
# Line 21 in hearing.py - in the record_audio() function
def record_audio(filename="input.wav", duration=5, samplerate=16000):
    # duration=5 means 5 seconds
```

Change `duration=5` to your preferred length:
- `duration=3` - Short recordings
- `duration=5` - Default
- `duration=10` - Long, detailed recordings

### 6. **Change Memory Limit** 💾
Edit `body_parts/dabrain.py` to remember more or fewer interactions:

```python
# Line 78 in dabrain.py
MEMORY_LIMIT = 10  # How many interactions to remember
```

**Examples:**
- `MEMORY_LIMIT = 5` - Only remember last 5 exchanges
- `MEMORY_LIMIT = 10` - Default, remember 10 exchanges
- `MEMORY_LIMIT = 50` - Remember up to 50 exchanges (requires more RAM)

### 7. **Add Custom Voice Models** 🎤
Replace the default voice model with your own:

1. Download a new Piper TTS model from [Piper voices](https://github.com/rhasspy/piper/releases)
2. Extract to `voice_models/` directory
3. Update `body_parts/mouth.py`:

```python
# Line 10-11 in mouth.py
model_path = os.path.join(script_dir, "voice_models/YOUR_MODEL_NAME.onnx")
config_path = os.path.join(script_dir, "voice_models/YOUR_MODEL_NAME.onnx.json")
```

### 8. **Add Custom Voice Commands** 🗣️
Edit `body_parts/dabrain.py` to add new voice commands:

```python
# Line 48-50 in dabrain.py
SWITCHING_MODE_KEYWORDS = ["switch mode", "change mode", "switch mod"]
GENERAL_MODE_KEYWORDS = ["general mode", "normal mode", "general"]
CODING_MODE_KEYWORDS = ["coding mode", "code mode", "code"]
CLEAR_HISTORY_KEYWORDS = ["clear memory", "reset memory", "forget history"]

# ADD YOUR OWN:
YOUR_CUSTOM_KEYWORDS = ["your phrase", "another phrase"]
```

Then add logic in the `think()` function to handle your custom commands.

### 9. **Change Audio Device** 🔊
If you have multiple microphones or speakers, edit `body_parts/hearing.py`:

```python
# Line 15 in hearing.py
sd.default.device = (1, None)  # (1, None) = mic 1, default speaker
```

Find your device IDs:
```bash
python tools/findMicID.py
```

This will list all available audio devices. Use the device numbers in the tuple:
- `(device_id, None)` - Use specific microphone, default speaker
- `(None, device_id)` - Default microphone, specific speaker
- `(mic_id, speaker_id)` - Specific microphone AND speaker

### 10. **Customize Startup Messages** 💬
Edit `main.py` to change the welcome message:

```python
# Line 35 in main.py
mouth.speak("Hello boss! I'm AILAX. How can I help you today?")
```

Change the greeting to anything you want:
```python
mouth.speak("Hey! I'm AILAX. Ready to assist you!")
```

### 11. **Setup Custom Wake Word** 🎙️🔥
Instead of pressing ENTER every time, activate AILAX with your voice using a custom wake word (like "Hey AILAX" or "OK Computer")!
This was added in the v1.4 update!

**Quick Setup:**
```bash
cd tools
python lwake-setup.py
```
or just run `lwake-setup.py`.

The interactive tool will guide you through:
1. ✅ Choosing your wake word phrase
2. ✅ Recording 3-5 voice samples
3. ✅ Testing the detection
4. ✅ Adjusting sensitivity settings

**📖 For a complete step-by-step guide, see:**
- **Full Documentation**: [`tools/WAKEWORD_SETUP_README.md`](tools/WAKEWORD_SETUP_README.md)

The full guide includes:
- Best practices for recording
- Threshold tuning guide
- Integration examples
- Troubleshooting tips
- Advanced configuration

**Requirements:**
- The `local-wake` package (already in requirements.txt)
- A working microphone
- Quiet environment for recording

Once set up, your wake word samples are saved in the `wakeword_samples/` folder and ready to integrate into AILAX for hands-free activation!

## Configuration Summary

| Setting | File | Line | Default | What It Does |
|---------|------|------|---------|--------------|
| AI Personality | dabrain.py | 27 | Custom | How AILAX talks and acts |
| General Model | dabrain.py | 37 | qwen3-vl | AI for general conversation |
| Coding Model | dabrain.py | 38 | qwen3-coder-next | AI for coding help |
| Speech Speed | mouth.py | 17 | 0.7 | How fast AILAX talks |
| Whisper Size | hearing.py | 12 | base | Speech recognition accuracy |
| Record Duration | hearing.py | 21 | 5 seconds | How long to listen |
| Memory Limit | dabrain.py | 78 | 10 interactions | How many to remember |
| Audio Device | hearing.py | 15 | Device 1 | Which mic/speaker to use |

## Troubleshooting
(Uh.. for other errors that you can't find here, open an issue on Github, or email me (there's a not 0% chance that I will see it 😺))

### Setup Issues
- **"Ollama is not installed or not in PATH"**: Install Ollama from https://ollama.com/download
- **"Python is not installed or not in PATH"**: Ensure Python 3.10+ is installed and in your system PATH
- **"Failed to install dependencies"**: Try running manually: `pip install -r requirements.txt`

### Startup Issues
- **"EARS are NOT ready"**: Whisper model not loaded. Check your internet connection and try again.
- **"MOUTH is NOT ready"**: Voice model files missing or corrupted. Ensure `voice_models/` directory exists with `en_US-amy-medium.onnx` files.
- **"BRAIN is NOT ready"**: Ollama models not found. Make sure you ran setup.bat/setup.sh successfully.

### Runtime Issues
- **No audio input**: Run `python tools/findMicID.py` to find your microphone ID, then update line 15 in `hearing.py` with: `sd.default.device = (YOUR_MIC_ID, None)`
- **No audio output**: Check your speaker settings or try a different audio device
- **Models not responding**: Ensure Ollama is running and you're logged in (`ollama whoami`)
- **Slow responses**: This is normal for large models. Grab a coffee! ☕

### Model Issues
- **Models fail to download**: Check your internet connection, or manually pull models:
  ```
  ollama pull qwen3-vl:235b-instruct-cloud
  ollama pull qwen3-coder-next:cloud
  ```
- **Out of memory errors**: These are large models. Ensure you have at least 8GB free RAM.

## File Structure
```
AILAX/
├── main.py                 # Main entry point - starts AILAX interface
├── requirements.txt        # Python dependencies
├── setup.bat              # Windows setup script
├── setup.sh               # Mac/Linux setup script
├── ailax_memory.json      # Conversation memory (auto-created)
├── body_parts/
│   ├── dabrain.py         # AI brain - handles reasoning and memory
│   ├── hearing.py         # Ears - audio recording & speech-to-text
│   └── mouth.py           # Mouth - text-to-speech synthesis
├── tools/
│   ├── findMicID.py              # Utility to find your microphone ID
│   ├── lwake-setup.py            # Wake word setup tool
│   └── WAKEWORD_SETUP_README.md  # Wake word documentation
├── voice_models/          # TTS voice models
│   ├── en_US-amy-medium.onnx
│   └── en_US-amy-medium.onnx.json
└── wakeword_samples/      # Your custom wake word recordings (created after setup)
    ├── sample_1.wav
    ├── sample_2.wav
    └── ...
```

<hr>

# License

This software is **licensed** under the **PolyForm Noncommercial License 1.0.**

In simple terms, this is **similar** to **CC BY-NC 4.0**:

    Attribution: You must credit me.

    Non-Commercial: You cannot sell this or use it for business.

See the [LICENSE](LICENSE) file for the full legal text.

<hr>

# Update Logs:

## v1.3:

This patch focus on Documentation, Setup, and Customization.

Main Changes:
- **Fixed critical bug**: Updated `pvspeaker` version from 1.3.0 (unavailable) to 1.0.5 (latest available)
- **Enhanced README**: Added comprehensive Table of Contents for easy navigation
- **Fixed mouth.py**: Replaced inappropriate test message with professional alternative
- **Improved requirements.txt**: Added version pinning for all dependencies + added missing `requests` library for web search functionality
- **Updated setup.bat & setup.sh**: Fixed Python version requirement to 3.10+ (was 3.7+)
- **Added Customization & Settings section**: 10 ways to customize AILAX:
  - Change AI personality
  - Switch between different Ollama models
  - Adjust speech speed (0.5 - 1.5 range)
  - Choose speech recognition accuracy (tiny to large)
  - Configure recording duration
  - Adjust memory limit
  - Add custom voice models
  - Add custom voice commands
  - Change audio devices
  - Customize startup messages
- **Added Configuration Summary table**: Quick reference for all settings and their locations
- **Improved troubleshooting**: Reorganized into 4 clear categories with better solutions
- **Enhanced file structure documentation**: Better descriptions of what each component does

## v1.2:

This patch focus on the Brain (again).

Main Changes:
- Added MEMORY to AILAX! It can now remember what you said! The default limit is 10 interactions, but you can change it in the settings section in `dabrain.py`!
- That's all... 

## v1.0:

This patch focus on the Brain.

Everything else should be functioning :3

Main Changes:
- Removed all previous modes (private and public)
- Removed all previous models ("gemini 2.5 flash lite" and "llama3.2")
- Added mode switching function - say `"switch mode 'mode'"` to switch between available modes
- Currently available modes: **General mode** & **Coding mode**
- Added new models for each mode: **Qwen3-VL** for General; **Qwen3-Coder-Next** for Coding
- Updated new system instruction message logic
