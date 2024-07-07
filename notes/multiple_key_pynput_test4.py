"""
This script still do not work. 
"""

from pynput.keyboard import Key, Controller
import time

# Create a Controller object
keyboard = Controller()

# Number of times to press the keys
press_count = 5

# Function to press and release a combination of keys in the specified order
def press_and_release_keys(modifier, key):
    keyboard.press(modifier)
    print(f"Pressed {modifier}")
    time.sleep(0.1)
    keyboard.press(key)
    print(f"Pressed {key}")
    time.sleep(0.1)
    keyboard.release(key)
    print(f"Released {key}")
    time.sleep(0.1)
    keyboard.release(modifier)
    print(f"Released {modifier}")
    time.sleep(0.1)

# Press Ctrl + Right and Ctrl + Left multiple times
for _ in range(press_count):
    # Press Ctrl + Right
    press_and_release_keys(Key.ctrl_l, Key.right)
    print("Ctrl + Right")
    time.sleep(1)  # Pause between presses

    # Press Ctrl + Left
    press_and_release_keys(Key.ctrl_l, Key.left)
    print("Ctrl + Left")
    time.sleep(1)  # Pause between presses
