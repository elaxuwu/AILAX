import os
import io
import wave
import numpy as np
from piper.voice import PiperVoice
from pvspeaker import PvSpeaker

# paths
model_path = "voice_models/en_US-amy-medium.onnx"
config_path = "voice_models/en_US-amy-medium.onnx.json"

voice = None
speaker = None

# 1.0 is default. Lower (0.8) is faster. Higher (1.2) is slower.
SPEAKING_SPEED = 0.7

# ensure the JSON config's length_scale matches SPEAKING_SPEED
try:
    import json

    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            cfg = json.load(f)

        if 'inference' not in cfg or not isinstance(cfg['inference'], dict):
            cfg['inference'] = {}

        cfg['inference']['length_scale'] = float(SPEAKING_SPEED)

        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(cfg, f, indent=2)
        print(f"Updated config length_scale to {SPEAKING_SPEED}")
except Exception as e:
    print(f"Could not update config length_scale: {e}")

# initialize

if os.path.exists(model_path):
    try:
        voice = PiperVoice.load(model_path, config_path)
        speaker = PvSpeaker(
                            sample_rate=voice.config.sample_rate,
                            bits_per_sample=16,
                            device_index=1,) 
        speaker.start()
        print("Voice model loaded successfully. Herzt:", voice.config.sample_rate)
    except Exception as e:
        print(f"Error loading voice model: {e}")
    
def speak(text):
    if not voice or not speaker:
        print("Voice model or speaker not initialized.")
        return
    
    # ? streaming audio ^^
    
    try:
        
        with io.BytesIO() as wav_buffer:
            
            with wave.open(wav_buffer, 'wb') as wf:
                voice.synthesize_wav(text, wf)
                
            wav_buffer.seek(0)
            
            with wave.open(wav_buffer, 'rb') as rf:
                
                raw_Data = rf.readframes(rf.getnframes())
                
                pcm = np.frombuffer(raw_Data, dtype=np.int16)
                
                speaker.write(pcm)
    except Exception as e:
        print(f"Error during speech synthesis: {e}")
        
        
if __name__ == "__main__":
    print("Testing TTS...")
    speak("jew jew jew jew jew jew jew jew jew jew")
    wait = input("Press Enter to exit...")