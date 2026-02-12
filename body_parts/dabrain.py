import os
import re
import ollama

from ollama import web_fetch, web_search, chat
from enum import Enum
from termcolor import colored

print(colored("STARTING BRAIN!!!", "yellow", attrs=["bold"]))

# ============================================================
# Personality
# ============================================================

GLOBAL_PERSONALITY = (
    "You are a helpful personal assistant named AILAX, you are a friend of the user, "
    "their name is elax. You assist with many tasks and speak naturally. "
    "Anything you write will be spoken out loud, so avoid formatting and be concise. "
    "There are two modes: General and Coding."
)

# ============================================================
# Models
# ============================================================

GENERAL_MODEL = "qwen3-vl:235b-instruct-cloud"
CODING_MODEL = "qwen3-coder-next:cloud"

# ============================================================
# Keywords
# ============================================================

SWITCHING_MODE_KEYWORDS = ["switch mode", "change mode"]

GENERAL_MODE_KEYWORDS = ["general mode", "normal mode", "general"]
CODING_MODE_KEYWORDS = ["coding mode", "code mode", "code"]

# ============================================================
# Tools
# ============================================================

available_tools = {
    "web_search": web_search,
    "web_fetch": web_fetch
}

# ============================================================
# Mode Enum
# ============================================================

class Mode(Enum):
    GENERAL = 1
    CODING = 2

current_mode = Mode.GENERAL

# ============================================================
# TOOL-ENABLED CHAT LOOP
# ============================================================

def run_with_tools(model, system_prompt, user_text, speak_function=None):
    messages = [
        {"role": "system", "content": system_prompt + "\nUse web search when information may be recent or uncertain."},
        {"role": "user", "content": user_text}
    ]

    while True:
        response = chat(
            model=model,
            messages=messages,
            tools=[web_search, web_fetch],
            think=True
        )

        msg = response.message

        if msg.thinking:
            print(colored(f"[Thinking] {msg.thinking}", "cyan"))

        if msg.content:
            print(msg.content)
            if speak_function:
                speak_function(msg.content)

        messages.append(msg)

        if msg.tool_calls:
            for tool_call in msg.tool_calls:
                tool_name = tool_call.function.name
                tool_fn = available_tools.get(tool_name)

                if not tool_fn:
                    messages.append({
                        "role": "tool",
                        "tool_name": tool_name,
                        "content": "Tool not found"
                    })
                    continue

                args = tool_call.function.arguments
                result = tool_fn(**args)

                result_text = str(result)[:8000]

                messages.append({
                    "role": "tool",
                    "tool_name": tool_name,
                    "content": result_text
                })
        else:
            break

# ============================================================
# MAIN THINK ROUTER
# ============================================================

def think(user_text, speak_function=None):
    global current_mode

    text = user_text.lower()
    isSwitchingMode = any(k in text for k in SWITCHING_MODE_KEYWORDS)

    # ---------------- MODE SWITCH ----------------

    if isSwitchingMode:
        print(colored("[Mode Switching Requested]", "yellow", attrs=["bold"]))

        if any(k in text for k in CODING_MODE_KEYWORDS):
            current_mode = Mode.CODING
            print(colored("Switched to CODING mode.", "yellow", attrs=["bold"]))
            if speak_function:
                speak_function("Switched to coding mode.")

        elif any(k in text for k in GENERAL_MODE_KEYWORDS):
            current_mode = Mode.GENERAL
            print(colored("Switched to GENERAL mode.", "yellow", attrs=["bold"]))
            if speak_function:
                speak_function("Switched to general mode.")

        else:
            if speak_function:
                speak_function("Please specify coding mode or general mode.")

        return

    # ---------------- CODING MODE ----------------

    if current_mode == Mode.CODING:
        print(colored("[CODING MODE ACTIVATED]", "yellow", attrs=["bold"]))
        print("Model:", CODING_MODEL)

        full_system_prompt = (
            GLOBAL_PERSONALITY +
            "\nYou are the CODING MODE version of AILAX. "
            "Focus on writing correct, efficient code with explanations."
        )

        run_with_tools(
            model=CODING_MODEL,
            system_prompt=full_system_prompt,
            user_text=user_text,
            speak_function=speak_function
        )

    # ---------------- GENERAL MODE ----------------

    else:
        print(colored("[GENERAL MODE ACTIVATED]", "yellow", attrs=["bold"]))
        print("Model:", GENERAL_MODEL)

        full_system_prompt = (
            GLOBAL_PERSONALITY +
            "\nYou are the GENERAL MODE version of AILAX. "
            "Be helpful, friendly, and informative."
        )

        run_with_tools(
            model=GENERAL_MODEL,
            system_prompt=full_system_prompt,
            user_text=user_text,
            speak_function=speak_function
        )

# ============================================================
# MAIN LOOP
# ============================================================

if __name__ == "__main__":

    def temp_mouth(text):
        print(f"\n[AI's MOUTH]: {text}")

    try:
        while True:
            think(input("\nYou: "), temp_mouth)
    except KeyboardInterrupt:
        print("\nExiting BRAIN...")
