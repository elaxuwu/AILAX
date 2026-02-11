import body_parts.dabrain as dabrain
import body_parts.hearing as hearing
import body_parts.mouth as mouth

import os
from termcolor import colored, cprint

def start_AILAX():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    cprint("========================================", "cyan", attrs=["bold"])
    cprint("          WELCOME TO AILAX v1.0     ", "cyan", attrs=["bold"])
    cprint("An AI Personal Assistant created by elax", "cyan", attrs=["bold"])
    cprint("========================================", "cyan", attrs=["bold"])
    
    if hearing.model:
        cprint("EARS are ready!", "yellow", attrs=["bold"])
    else:
        cprint("EARS are NOT ready! Please check your Whisper model setup.", "red", attrs=["bold", "blink"])
        
    if mouth.voice and mouth.speaker:
        cprint("MOUTH is ready!", "yellow", attrs=["bold"])
    else:
        cprint("MOUTH is NOT ready! Please check your voice model setup.", "red", attrs=["bold", "blink"])
        
    if dabrain.GENERAL_MODEL or dabrain.GLOBAL_PERSONALITY:
        cprint("BRAIN is ready!", "yellow", attrs=["bold"])
    else:
        cprint("BRAIN is NOT ready! Please check your Models or Personality Setup.", "red", attrs=["bold", "blink"])
        
    mouth.speak("Hello boss! I'm AILAX. How can I help you today?")
    
    while True:
        try:
            
            cprint("\nPress ENTER to speak your command or 'q' to quit!", "green", attrs=["bold", "blink"])
            user_input = input()
            
            if user_input.lower() == 'q':
                cprint("Shutting down AILAX. Goodbye!", "cyan", attrs=["bold"])
                break
            
            hearing.record_audio()
            user_text = hearing.transcribe_audio()
            
            if not user_text or len(user_text.strip()) < 2:
                cprint("I didn't catch that. Please try again.", "red", attrs=["bold"])
                mouth.speak("the fuck did you just say?")
                continue
            
            print("You said:", end=" ")
            print(user_text)
            
            dabrain.think(user_text, speak_function=mouth.speak)
        except KeyboardInterrupt:
            cprint("\nShutting down AILAX. Goodbye!", "cyan", attrs=["bold"])
            break
        except Exception as e:
            cprint(f"An error occurred: {e}", "red", attrs=["bold"])
            
if __name__ == "__main__":
    start_AILAX()