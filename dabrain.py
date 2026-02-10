import os
import re
import ollama
from google import genai
from google.genai import types
from dotenv import load_dotenv

from termcolor import colored, cprint

print(colored("STARTING BRAIN!!!", "yellow", attrs=["bold"]))

# set up keys
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# setup Gemini
client = None
if api_key:
    client = genai.Client(api_key=api_key)
    
# setup Ollama
OLLAMA_PERSONALITY = (
    "You are a helpful personal assistant named AILAX, you are a friend of the user, his name is elax. You are designed to assist with a wide range of tasks, including answering questions, providing information, and engaging in conversation. You are friendly, knowledgeable, and always eager to help. Your goal is to make the user's life easier and more enjoyable by providing accurate and helpful responses. Anything you write in the response will be spoken out loud, so don't include any special formatting or brackets."
)

# setup models

GEMINI_MODEL = "gemini-2.5-flash-lite"
OLLAMA_MODEL = "llama3.2"

#keywords

PRIVATE_KEYWORDS = ["private"]

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
    text = user_text.lower()
    is_private = any(keyword in text for keyword in PRIVATE_KEYWORDS)
    
    generator = None
    
    # ? Private stuff => using Ollama
    if is_private:
        print(colored("[Private Mode Activated - Using Ollama]", "red", attrs=["bold"]))
        print("Model:", OLLAMA_MODEL)
        
        stream = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[
                {"role": "system", "content": OLLAMA_PERSONALITY},
                {"role": "system", "content": "You are the private version of AILAX. Keep all responses confidential. When answering, ignore the user mentioning 'private mode'."},
                {"role": "user", "content": user_text},
            ],
            stream=True,
        )
        
        def ollama_generator():
            for chunk in stream:
                yield chunk["message"]['content']
        
        generator = ollama_generator()
        
    # ? Public stuff => using Gemini
    
    else:
        print(colored("[Public Mode Activated - Using Gemini]", "green", attrs=["bold"]))
        print("Model:", GEMINI_MODEL)
        
        if not client:
            print(colored("Error: Gemini API key not found. Please set GEMINI_API_KEY in your environment variables.", "red", attrs=["bold"]))
            return
        
        try:
            response = client.models.generate_content_stream(
                model=GEMINI_MODEL,
                contents=[user_text],
                config=types.GenerateContentConfig(system_instruction=OLLAMA_PERSONALITY),
                )
            
            def gemini_generator():
                for chunk in response:
                    if chunk.text:
                        yield chunk.text
            
            generator = gemini_generator()
            
        except Exception as e:
            print(f"Error during Gemini API call: {e}")
            return
        
    if generator:
        stream_and_buffer(generator, speak_function)
            
if __name__ == "__main__":
    
    def temp_mouth(text):
        print(f"\n[AI's MOUTH]: {text}")
        
    think(input("You: "), temp_mouth)