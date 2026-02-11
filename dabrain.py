import os
import re
import ollama

from enum import Enum

from termcolor import colored, cprint

print(colored("STARTING BRAIN!!!", "yellow", attrs=["bold"]))


    
# setup Ollama
GLOBAL_PERSONALITY = (
    "You are a helpful personal assistant named AILAX, you are a friend of the user, their name is elax. You are designed to assist with a wide range of tasks, including answering questions, providing information, and engaging in conversation. You are friendly, knowledgeable, and always eager to help. Your goal is to make the user's life easier and more enjoyable by providing accurate and helpful responses. Anything you write in the response will be spoken out loud, so don't include any special formatting or brackets. Do not give unnecessary long answers. Currently there are two modes: General and Coding - Your mode will be told by the following system message after this one."
)

# setup models

GENERAL_MODEL = "gemma3:27b-cloud" # for general tasks
CODING_MODEL = "deepseek-v3.2:cloud" # for coding tasks

#keywords

SWITCHING_MODE_KEYWORDS = ["switch mode", "change mode"] # trigger mode changing

GENERAL_MODE_KEYWORDS = ["general mode", "normal mode","general"] # change to general mode
CODING_MODE_KEYWORDS = ["coding mode", "code mode", "code"] # chnage to code mode

# ! Mode Enum
class Mode(Enum):
    GENERAL = 1
    CODING = 2
    
current_mode = Mode.GENERAL


# ! Buffering

def stream_and_buffer(generator, speak_function=None):
    buffer = ""
    split_pattern = r'([.!?;\n]+)' # look for . ! ? ; or new lines
    
    for chunk in generator:
        
        #fast printing (for debug)
        print(chunk, end="", flush=True)
        buffer += chunk
        
        parts = re.split(split_pattern, buffer)
        
        if len(parts) >1:
            for i in range(0, len(parts)-1, 2):
                sentence = parts[i] + parts[i+1]
                if speak_function and sentence.strip():
                    speak_function(sentence)
            buffer = parts[-1]
    
    #cleanup
    if buffer.strip() and speak_function:
        speak_function(buffer)
    print()
    
# ! router (main thinking)
def think(user_text, speak_function=None):
    
    global current_mode
    
    text = user_text.lower()
    
    isSwitchingMode = any(keyword in text for keyword in SWITCHING_MODE_KEYWORDS)
    
    generator = None
    
    if isSwitchingMode:
        print(colored("[Mode Switching Requested]", "yellow", attrs=["bold"]))
        if any(keyword in text for keyword in CODING_MODE_KEYWORDS): # ? change to coding mode
            print(colored("Switching to CODING mode.", "yellow", attrs=["bold"]))
            current_mode = Mode.CODING
            if speak_function:
                speak_function("Switched to coding mode.")
        elif any(keyword in text for keyword in GENERAL_MODE_KEYWORDS): # ? change to general mode
            print(colored("Switching to GENERAL mode.", "yellow", attrs=["bold"]))
            current_mode = Mode.GENERAL
            if speak_function:
                speak_function("Switched to general mode.")
        else:
            print(colored("No valid mode specified. Staying in current mode.", "red", attrs=["bold"]))
            if speak_function:
                speak_function("I didn't catch which mode to switch to. Please specify coding mode or general mode.")
        return
    
    if current_mode == Mode.CODING and not isSwitchingMode:
        print(colored("[CODING MODE ACTIVATED]", "yellow", attrs=["bold"]))
        print("Model:", CODING_MODEL)
        
        # COMBINED SYSTEM MESSAGE
        full_system_prompt = GLOBAL_PERSONALITY + "\n\n" + "You are the coding version (CODING MODE) of AILAX. Provide accurate and efficient code solutions. When answering, focus on coding-related tasks. Also remember to add comments on explaining the code."
        
        stream = ollama.chat(
            model=CODING_MODEL,
            messages=[
                {"role": "system", "content": full_system_prompt},
                {"role": "user", "content": user_text},
            ],
            stream=True,
        )
        
        def ollama_generator():
            for chunk in stream:
                yield chunk["message"]['content']
                
        generator = ollama_generator()
        
    elif current_mode == Mode.GENERAL and not isSwitchingMode:
        print(colored("[GENERAL MODE ACTIVATED]", "yellow", attrs=["bold"]))
        print("Model:", GENERAL_MODEL)
        
        # COMBINED SYSTEM MESSAGE
        full_system_prompt = GLOBAL_PERSONALITY + "\n\n" + "You are the general version (GENERAL MODE) of AILAX. Provide helpful and informative responses to all user queries. Act as a friend and personal assistant."

        stream = ollama.chat(
            model=GENERAL_MODEL,
            messages=[
                {"role": "system", "content": full_system_prompt},
                {"role": "user", "content": user_text},
            ],
            stream=True,
        )
        
        def ollama_generator():
            for chunk in stream:
                yield chunk["message"]['content']
                
        generator = ollama_generator()
        
    if generator:
        stream_and_buffer(generator, speak_function)
            
if __name__ == "__main__":
    def temp_mouth(text):
        print(f"\n[AI's MOUTH]: {text}")
        
        
    try:
        while True:
            think(input("You: "), temp_mouth)
    except KeyboardInterrupt:
        print("\nExiting BRAIN...")