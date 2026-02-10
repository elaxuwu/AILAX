import os
import google.generativeai as genai
import ollama
from dotenv import load_dotenv

import sys
from termcolor import colored, cprint

# ! [Load api key]
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# ! [Config Gemini]
# ? check key
if api_key:
    genai.configure(api_key=api_key)
else:
    print("You did not set the GEMINI_API_KEY environment variable (in .env file).")
    
# ! [Keywords]
PRIVATE_KEYWORDS = [
    "private", "confidential", "sensitive", "secret", "for eyes only",
    "do not share", "classified", "restricted", "internal use",
    "off the record", "protected", "no disclosure", "personal",
    "encrypted", "confidential handoff",
    "bí mật", "tuyệt mật", "riêng tư", "nội bộ", "chỉ dành cho người xem",
    "cấm chia sẻ", "không tiết lộ", "nhạy cảm", "bảo mật", "mật",
    "không công khai"
]
    
# ! [Router]
def think(user_text):
    text = user_text.lower()
    
    isPrivate = any(keyword in text for keyword in PRIVATE_KEYWORDS)
    
    # ? Ollama (Private)
    if isPrivate:
        print(colored("PRIVATE MODE - USING OLLAMA", "red"))
        
    
    # ? Gemini (Not private)
    else:
        print(colored("NOT PRIVATE MODE - USING GEMINI", "green"))