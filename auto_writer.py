import json
import time
import pyautogui
import random
import sys
import os

# Load typing pattern
with open('typing_intervals.json', 'r') as f:
    data = json.load(f)
    mean = data['mean']
    std = data['std']

# Get sentence to type: from txt file if provided, else prompt
if len(sys.argv) > 1 and sys.argv[1].endswith('.txt') and os.path.exists(sys.argv[1]):
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        to_type = f.read().strip()
    print(f"Loaded text from {sys.argv[1]}")
else:
    to_type = input("Enter the sentence you want to auto-type: ")

# Set speed multiplier for much faster typing (0.5 = 2x faster, lower for even faster)
# Adjust this value to control speed
speed_multiplier = 0.5
mean *= speed_multiplier
std *= speed_multiplier

print("You have 5 seconds to focus the target input box...")
time.sleep(5)

for char in to_type:
    if char.isupper():
        pyautogui.keyDown('shift')
        pyautogui.typewrite(char.lower())
        pyautogui.keyUp('shift')
    elif char == "'":
        pyautogui.press("'")
    else:
        pyautogui.typewrite(char)
    # Generate a random interval (minimum 1ms to avoid zero/negative delays)
    delay = max(0.001, random.gauss(mean, std) / 1000)
    time.sleep(delay)

print("Done!") 