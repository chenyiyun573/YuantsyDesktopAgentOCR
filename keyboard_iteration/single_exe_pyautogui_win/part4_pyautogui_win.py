"""
The results shows that:
esc, space, tab, enter, backspace are working well on windows 11. 

Capslock works on windows but not on mac. 

Fn does not work. 
"""

import pyautogui
import time

# List of keys to press

keys1 = ['esc', 'space', 'tab','enter', 'backspace']

keys2= ['a','capslock','a','capslock','a']
keys3 = ['a','fn','a','fn','a']

time.sleep(3)
# Iterate over each key and press it with a delay to observe the effect
for key in keys1:
    pyautogui.press(key)
    print(f"Pressed {key}")
    time.sleep(2)  # Delay to observe the effect

print("Finished pressing special purpose keys.")

# c = 0