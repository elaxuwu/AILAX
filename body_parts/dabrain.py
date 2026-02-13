import ollama
import json
from pathlib import Path
from enum import Enum
from termcolor import colored

print(colored("STARTING BRAIN!!!", "yellow", attrs=["bold"]))

# ============================================================
# Personality
# ============================================================

GLOBAL_PERSONALITY = (
    "You are a helpful personal assistant named AILAX, you are a friend of the user, "
    "their name is elax. You assist with many tasks and speak naturally. "
    "Anything you write will be spoken out loud, so avoid formatting and be concise, also don't use emojis or icons. "
    "Answer as short as possible while being informative and helpful. "
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

SWITCHING_MODE_KEYWORDS = ["switch mode", "change mode", "switch mod"]

GENERAL_MODE_KEYWORDS = ["general mode", "normal mode", "general"]
CODING_MODE_KEYWORDS = ["coding mode", "code mode", "code"]

CLEAR_HISTORY_KEYWORDS = ["clear memory", "reset memory", "forget history"]

# ============================================================
# Tools
# ============================================================

available_tools = {
    "web_search": ollama.web_search,
    "web_fetch": ollama.web_fetch
}

# ============================================================
# Mode Enum
# ============================================================

class Mode(Enum):
    GENERAL = 1
    CODING = 2

current_mode = Mode.GENERAL

# ===========================================================
# MEMORY (a noun, not the song my Maroon 5, but it's good :3)
# uh..i think the song name is Memories not memory.. whatever
# ============================================================

def load_memory():
    if MEMORY_FILE.exists():
        try:
            with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data if isinstance(data, list) else []
        except (json.JSONDecodeError, ValueError):
            print(colored("[Warning] Memory file corrupted, starting fresh.", "yellow"))
            return []
    return []

def save_memory(history):
    with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

MEMORY_FILE = Path("ailax_memory.json")

conversation_history = load_memory()
MEMORY_LIMIT = 10 # max number of exchanges to remember

# ============================================================
# TOOL-ENABLED CHAT LOOP
# ============================================================

def run_with_tools(model, system_prompt, user_text, speak_function=None, history=None):

    if history is None:
        raise ValueError("History must be provided for conversation context.")


    messages = [{"role": "system", "content": system_prompt + "\nUse web search when information may be recent or uncertain."}]

    messages.extend(history)

    messages.append({"role": "user", "content": user_text})

    while True:
        response = ollama.chat(
            model=model,
            messages=messages,
            tools=[ollama.web_search, ollama.web_fetch],
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

    history.append({"role": "user", "content": user_text})
    if msg.content:
        history.append({"role": "assistant", "content": msg.content})

    if len(history) > MEMORY_LIMIT * 2:
        history[:] = history[-MEMORY_LIMIT * 2:]

    # Save memory to disk after each conversation
    save_memory(history)

# ============================================================
# MAIN THINK ROUTER
# ============================================================

def think(user_text, speak_function=None):
    global current_mode, conversation_history

    text = user_text.lower()
    is_switching_mode = any(k in text for k in SWITCHING_MODE_KEYWORDS)

    is_clearing_history = any(k in text for k in CLEAR_HISTORY_KEYWORDS)

    # ---------------- MODE SWITCH ----------------

    if is_switching_mode:
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

    # ---------------- CLEAR HISTORY ----------------

    if is_clearing_history:
        print(colored("[Memory Cleared]", "red", attrs=["bold"]))
        conversation_history.clear()
        save_memory(conversation_history)  # Save the cleared state to disk
        if speak_function:
            speak_function("Memory cleared.")
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
            speak_function=speak_function,
            history = conversation_history
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
            speak_function=speak_function,
            history = conversation_history
        )




# ============================================================
# MAIN TESTING LOOP
# ============================================================

if __name__ == "__main__":

    def temp_mouth(text):
        print(f"\n[AI's MOUTH]: {text}")

    try:
        while True:
            think(input("\nYou: "), temp_mouth)
    except KeyboardInterrupt:
        print("\nExiting BRAIN...")
