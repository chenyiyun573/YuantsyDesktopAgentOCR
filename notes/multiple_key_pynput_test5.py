"""
This script to take screenshot works well. 
"""

from pynput.keyboard import Key, Controller
import time

# Create a Controller object
keyboard = Controller()

# Function to press and release a combination of keys in the specified order
def press_and_release_keys(*keys):
    for key in keys:
        keyboard.press(key)
        time.sleep(0.1)
    for key in reversed(keys):
        keyboard.release(key)
        time.sleep(0.1)

# Press Command + Shift + 3
press_and_release_keys(Key.cmd, Key.shift, '3')
print("Executed Command + Shift + 3")
