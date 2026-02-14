import sounddevice as sd
import soundfile as sf
from faster_whisper import WhisperModel

import os

from termcolor import colored

print(colored("STARTING EARS!!!", "yellow", attrs=["bold"]))

# ! CONFIGURATION
model_size = "small" # Model size can be "tiny", "base", "small", "medium", "large"
model = WhisperModel(model_size, device="cpu", compute_type="int8")

sd.default.device = (1, None)
print(f"Using device: {sd.query_devices(sd.default.device[0])['name']}")

# Get project root directory for file paths
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def record_audio(filename="input.wav", duration=7, samplerate=16000):
    # Use absolute path if relative path is provided
    if not os.path.isabs(filename):
        filename = os.path.join(project_root, filename)
    print(colored("Listening...", "green", attrs=["bold", "blink"]))
    
    audio_data = sd.rec(int(duration*samplerate), samplerate=samplerate, channels=1, dtype='float32')
    
    sd.wait()
    
    sf.write(filename, audio_data, samplerate)
    print(colored("Done listening :D", "green", attrs=["bold", "blink"]))
    
def transcribe_audio(filename="input.wav"):
    # Use absolute path if relative path is provided
    if not os.path.isabs(filename):
        filename = os.path.join(project_root, filename)
    segments, info =  model.transcribe(filename, beam_size=5)
    
    full_text = ""
    for segment in segments:
        full_text += segment.text
    return full_text


if __name__ == "__main__":
    record_audio(duration=5)
    result = transcribe_audio()
    print(colored("Transcription Result:", "blue", attrs=["bold"]))
    print("'", end="")
    print(result, end="")
    print("'", end="")