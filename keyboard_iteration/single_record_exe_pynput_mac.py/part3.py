"""
This script cannot be executed correctly. 20240717 Yiyun Chen
"""


from pynput.keyboard import Controller, Key
import time

# Initialize the keyboard controller
keyboard = Controller()

# List of function keys
keys4 = [Key.f1, Key.f2, Key.f3, Key.f4, Key.f5, Key.f6, 
         Key.f7, Key.f8, Key.f9, Key.f10, Key.f11, Key.f12]

# Wait for 5 seconds to switch to the desired window
time.sleep(5)

# Iterate over each function key and press it
for key in keys4:
    keyboard.press(key)
    keyboard.release(key)
    print(f"Pressed {key}")
    time.sleep(0.5)  # Short delay to observe the effect of each key press

print("Finished iterating over all function keys.")
