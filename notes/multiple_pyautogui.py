"""
This script to execute the combination of keys works well. 
"""


import pyautogui
import time

# Number of times to press the keys
press_count = 5

# Function to press and release a combination of keys
def press_keys(*keys):
    pyautogui.hotkey(*keys)

# Press Ctrl + Right and Ctrl + Left multiple times
for _ in range(press_count):
    # Press Ctrl + Right
    press_keys('ctrl', 'right')
    print("Ctrl + Right")
    time.sleep(1)  # Pause between presses

    # Press Ctrl + Left
    press_keys('ctrl', 'left')
    print("Ctrl + Left")
    time.sleep(1)  # Pause between presses
