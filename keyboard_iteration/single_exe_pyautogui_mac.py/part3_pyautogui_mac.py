# This part did not work on macbook keyboard.  - Yiyun Chen 20240717



keys4 = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12']

import pyautogui
import time

time.sleep(5)  # Delay to switch to the desired window`-=[]\;'`

# Iterate over each key and press it
for key in keys4:
    pyautogui.press(key)
    print(f"Pressed {key}")
    time.sleep(0.5)  # short delay to see the effect of each key press

print("Finished iterating over all keys.")
