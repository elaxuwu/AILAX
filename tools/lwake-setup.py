#!/usr/bin/env python3
"""
AILAX Wake Word Setup Tool
===========================
This tool helps you record and set up custom wake words for AILAX.

You'll record your wake word phrase 3-5 times, and AILAX will learn to
recognize it when you say it in the future.

Requirements:
- A working microphone
- A quiet environment for best results
- The local-wake package (should be installed via requirements.txt)
"""

# ! note from me: yes i made this specific script with AI cuz im lazy
# ! dont worry pookie, i spent 30 minutes on verifying and testing this script :3

import os
import sys
import lwake
from termcolor import colored

# Configuration
WAKEWORD_FOLDER = "wakeword_samples"
RECORDING_DURATION = 3  # seconds
MIN_SAMPLES = 3
MAX_SAMPLES = 5

def print_header(text):
    """Print a colored header."""
    print("\n" + colored("=" * 60, "cyan"))
    print(colored(f"  {text}", "cyan"))
    print(colored("=" * 60, "cyan") + "\n")

def print_success(text):
    """Print a success message."""
    print(colored(f"[SUCCESS] {text}", "green"))

def print_error(text):
    """Print an error message."""
    print(colored(f"[ERROR] {text}", "red"))

def print_info(text):
    """Print an info message."""
    print(colored(f"[INFO] {text}", "blue"))

def print_warning(text):
    """Print a warning message."""
    print(colored(f"[WARNING] {text}", "yellow"))

def setup_wakeword_folder():
    """Create the wake word samples folder if it doesn't exist."""
    if not os.path.exists(WAKEWORD_FOLDER):
        os.makedirs(WAKEWORD_FOLDER)
        print_success(f"Created folder: {WAKEWORD_FOLDER}")
    else:
        # Check if folder already has samples
        existing_files = [f for f in os.listdir(WAKEWORD_FOLDER) if f.endswith('.wav')]
        if existing_files:
            print_warning(f"Found {len(existing_files)} existing sample(s) in {WAKEWORD_FOLDER}")
            choice = input(colored("Do you want to delete them and start fresh? (y/N): ", "yellow"))
            if choice.lower() == 'y':
                for file in existing_files:
                    os.remove(os.path.join(WAKEWORD_FOLDER, file))
                print_success("Cleared existing samples")
            else:
                print_info("Keeping existing samples")
                return len(existing_files)
    return 0

def record_sample(sample_number, wake_phrase):
    """Record a single wake word sample."""
    filename = os.path.join(WAKEWORD_FOLDER, f"sample_{sample_number}.wav")

    print_info(f"Recording sample {sample_number}...")
    print(colored(f"Say: '{wake_phrase}'", "yellow", attrs=["bold"]))
    print(colored("Recording will start in 2 seconds...", "white"))

    import time
    time.sleep(2)

    print(colored("🔴 RECORDING NOW!", "red", attrs=["bold"]))

    try:
        lwake.record(filename, duration=RECORDING_DURATION, trim_silence=True)
        print_success(f"Sample {sample_number} recorded successfully!")
        return True
    except Exception as e:
        print_error(f"Failed to record sample: {e}")
        return False

def test_detection(wake_phrase):
    """Test the wake word detection with recorded samples."""
    print_header("Testing Wake Word Detection")
    print_info(f"Listening for: '{wake_phrase}'")
    print_info("Say your wake word to test detection (Press Ctrl+C to stop)")
    print(colored("\nTip: Try saying it from different distances and angles", "cyan"))

    detection_count = 0

    def handle_detection(detection, stream):
        nonlocal detection_count
        detection_count += 1
        print(colored(f"\n✓ Wake word detected! (#{detection_count})", "green", attrs=["bold"]))
        print(colored(f"  Timestamp: {detection['timestamp']:.2f}s", "white"))
        print(colored(f"  Wakeword: {detection['wakeword']}", "white"))
        print(colored("\nListening again...", "cyan"))

    try:
        # Use a lower threshold for better detection (adjust between 0.05 - 0.2)
        lwake.listen(
            WAKEWORD_FOLDER,
            threshold=0.15,  # Lower = more sensitive
            method="embedding",
            callback=handle_detection
        )
    except KeyboardInterrupt:
        print(colored("\n\nTesting stopped.", "yellow"))
        print_info(f"Total detections: {detection_count}")

        if detection_count > 0:
            print_success("Wake word detection is working!")
        else:
            print_warning("No detections recorded. You may need to:")
            print("  1. Record more samples")
            print("  2. Speak louder/clearer")
            print("  3. Adjust the threshold (lower = more sensitive)")

def main():
    """Main setup process."""
    print_header("AILAX Wake Word Setup")

    print("This tool will help you set up a custom wake word for AILAX.")
    print("You'll need to record yourself saying the wake word 3-5 times.\n")

    # Get wake word phrase
    print_info("Choose a wake word phrase (e.g., 'Hey AILAX', 'OK Computer', 'Jarvis')")
    wake_phrase = input(colored("Enter your wake word: ", "cyan")).strip()

    if not wake_phrase:
        print_error("Wake word cannot be empty!")
        sys.exit(1)

    print_success(f"Wake word set to: '{wake_phrase}'")

    # Setup folder
    existing_samples = setup_wakeword_folder()

    # Record samples
    print_header("Recording Wake Word Samples")
    print_info(f"You need to record {MIN_SAMPLES}-{MAX_SAMPLES} samples")
    print_info("Speak clearly and naturally, as you would when using AILAX\n")

    samples_to_record = MAX_SAMPLES - existing_samples

    if samples_to_record > 0:
        for i in range(existing_samples + 1, existing_samples + samples_to_record + 1):
            success = record_sample(i, wake_phrase)
            if not success:
                choice = input(colored("Try again? (Y/n): ", "yellow"))
                if choice.lower() != 'n':
                    record_sample(i, wake_phrase)

            if i < existing_samples + samples_to_record:
                input(colored("\nPress ENTER when ready for next sample...", "cyan"))

    # Check total samples
    total_samples = len([f for f in os.listdir(WAKEWORD_FOLDER) if f.endswith('.wav')])

    if total_samples < MIN_SAMPLES:
        print_error(f"Not enough samples! Need at least {MIN_SAMPLES}, got {total_samples}")
        sys.exit(1)

    print_success(f"Recorded {total_samples} samples successfully!")

    # Test detection
    print("\n")
    choice = input(colored("Would you like to test the wake word detection? (Y/n): ", "cyan"))
    if choice.lower() != 'n':
        test_detection(wake_phrase)

    # Final instructions
    print_header("Setup Complete!")
    print_success("Your wake word has been set up successfully!")
    print(colored("\n📝 Next Steps:", "cyan", attrs=["bold"]))
    print(f"  1. Your wake word samples are saved in: {colored(WAKEWORD_FOLDER, 'yellow')}")
    print(f"  2. To use wake word detection in AILAX:")
    print(f"     - Edit {colored('main.py', 'yellow')} or {colored('body_parts/hearing.py', 'yellow')}")
    print(f"     - Add: {colored('lwake.listen(...)', 'yellow')}")
    print(f"  3. Adjust {colored('threshold', 'yellow')} (0.05-0.2) if needed:")
    print(f"     - Lower = More sensitive (more false positives)")
    print(f"     - Higher = Less sensitive (might miss some)")
    print(f"\n  Current recommended threshold: {colored('0.15', 'green')}")
    print(colored("\n" + "=" * 60, "cyan"))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(colored("\n\nSetup cancelled by user.", "yellow"))
        sys.exit(0)
    except Exception as e:
        print_error(f"An unexpected error occurred: {e}")
        sys.exit(1)
