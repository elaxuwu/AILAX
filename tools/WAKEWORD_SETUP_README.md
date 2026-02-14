# Wake Word Setup Guide

This guide will help you set up a custom wake word for AILAX using the `lwake-setup.py` tool.

uhh...I think you know why the guide on how to setup a wake word is put in a separate file...

## What is a Wake Word?

A wake word (like "Hey Siri" or "OK Google") is a phrase that activates your AI assistant. Instead of pressing ENTER every time, you can just say your custom wake word to start talking to AILAX!

## Prerequisites

- Working microphone
- Quiet environment (for best results)
- `local-wake` package installed (automatically installed via `setup.bat/setup.sh`)

## Quick Start

1. **Run the setup tool:**
   ```bash
   cd tools
   python lwake-setup.py
   ```

2. **Follow the prompts:**
   - Choose your wake word phrase (e.g., "Hey AILAX", "OK Computer", "Jarvis")
   - Record yourself saying it 3-5 times
   - Test the detection

3. **That's it!** Your wake word samples will be saved in the `wakeword_samples` folder.

## Step-by-Step Guide

### Step 1: Choose Your Wake Word

Pick a phrase that is:
- ✅ **Unique** - Not commonly said in everyday conversation
- ✅ **Easy to say** - Something you can say naturally
- ✅ **2-4 syllables** - Works best with this length
- ✅ **Clear pronunciation** - Avoid mumbling

**Good examples:**
- "Hey AILAX"
- "OK Computer"
- "Jarvis activate"
- "Hello Assistant"

**Bad examples:**
- "Hi" (too short, commonly said)
- "Computer please activate the artificial intelligence system" (too long)
- Single words like "Computer" (too generic)

### Step 2: Record Your Samples

The tool will ask you to record 3-5 samples of your wake word.

**Recording Tips:**
- 🎤 Speak **clearly and naturally**
- 📏 Stay at a **consistent distance** from the mic
- 🔇 Record in a **quiet environment**
- 🗣️ Use your **normal speaking voice** (not whisper, not shouting)
- 🎭 **Vary slightly** between recordings (different tones, speeds)

Each recording is **3 seconds long** with automatic silence trimming.

### Step 3: Test Detection

After recording, you can test if AILAX recognizes your wake word:
- Say your wake word multiple times
- Try different distances and angles
- Check if it detects reliably

**If detection is poor:**
- Record more samples (3-5 is recommended)
- Speak more clearly
- Reduce background noise
- Adjust the threshold (see below)

## Advanced Configuration

### Sensitivity Threshold

The `threshold` parameter controls how sensitive the detection is:

```python
lwake.listen("wakeword_samples", threshold=0.15, ...)
```

| Threshold | Behavior |
|-----------|----------|
| `0.05-0.10` | Very sensitive - More false positives |
| `0.15` | **Recommended** - Balanced detection |
| `0.20-0.30` | Less sensitive - Fewer false positives, might miss some |

**Adjust based on your needs:**
- Living alone? Use lower threshold (0.10) for convenience
- Noisy environment? Use higher threshold (0.20) to avoid false triggers

### Recording Duration

Default is 3 seconds. You can change this in `lwake-setup.py`:

```python
RECORDING_DURATION = 3  # Increase if your wake word is longer
```

### Number of Samples

More samples = better accuracy:
- **Minimum:** 3 samples
- **Recommended:** 5 samples
- **Maximum:** As many as you want (diminishing returns after 10)

## Integrating with AILAX

Once you've set up your wake word, you can integrate it into AILAX:

### Option 1: Replace Manual Input (in `main.py`)

**Before:**
```python
input("Press ENTER to speak your command or 'q' to quit: ")
```

**After:**
```python
import lwake

def wait_for_wakeword():
    print("Listening for wake word...")
    detected = False
    
    def handle_detection(detection, stream):
        nonlocal detected
        print(f"✓ Wake word detected!")
        detected = True
    
    lwake.listen("wakeword_samples", threshold=0.15, callback=handle_detection)
    return detected

# In your main loop
if wait_for_wakeword():
    # Record and process command
    pass
```

### Option 2: Continuous Listening Mode

```python
import lwake

def handle_wakeword(detection, stream):
    print(f"Wake word detected at {detection['timestamp']}s")
    # Record user command after wake word
    audio, _ = stream.read(16000 * 5)  # Record 5 seconds
    # Process audio with AILAX...

# Keep listening forever
lwake.listen("wakeword_samples", threshold=0.15, callback=handle_wakeword)
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'lwake'"

**Solution:** Make sure `local-wake` is installed:
```bash
pip install local-wake
```

Note: The package name is `local-wake` but you import it as `lwake`.

### Wake word not detected

**Try these:**
1. Record more samples (5 is better than 3)
2. Lower the threshold to 0.10 or 0.12
3. Speak louder and clearer
4. Check your microphone is working: `python tools/findMicID.py`
5. Reduce background noise

### Too many false positives

**Try these:**
1. Increase the threshold to 0.20
2. Choose a more unique wake word
3. Record samples in a quieter environment
4. Speak more distinctly during recording

### Recording fails

**Check:**
- Microphone permissions (OS level)
- Microphone is not being used by another app
- Run `python tools/findMicID.py` to verify your mic works
- Try a different microphone

## File Structure

After setup, you'll have:

```
AILAX/
├── tools/
│   ├── lwake-setup.py           # Setup tool
│   └── WAKEWORD_SETUP_README.md # This file
└── wakeword_samples/            # Your recordings
    ├── sample_1.wav
    ├── sample_2.wav
    ├── sample_3.wav
    ├── sample_4.wav
    └── sample_5.wav
```

## Tips for Best Results

1. **Consistent Environment**: Record all samples in the same location you'll use AILAX
2. **Vary Slightly**: Don't sound robotic - speak naturally with slight variations
3. **Test Thoroughly**: Test from different positions before committing
4. **Backup Samples**: Keep your `wakeword_samples` folder backed up
5. **Re-record if Needed**: If performance degrades over time, re-record samples

## Resources

- **local-wake Documentation**: [GitHub](https://github.com/s-matke/local-wake)
- **AILAX Main README**: `../README.md`
- **Microphone Setup**: `python tools/findMicID.py`

---

Need help? Check the main AILAX README or create an issue on GitHub!

