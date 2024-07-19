"""
All keys in this script work well on windows 11. 20240718 Yiyun Chen
"""
import pyautogui
import time

# List of keys to iterate over
keys1 = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

keys2 = [
    '`',  # Backtick
    '-',  # Minus
    '=',  # Plus (this is usually the key for equal, but with Shift it becomes plus)
    '[',  # Left bracket
    ']',  # Right bracket
    ';',  # Semicolon
    '\'', # Quote
    ',',  # Comma
    '.',  # Period
    '/',  # Slash
    '\\'  # Backslash
]

keys3 = ['up', 'down', 'left', 'right']



time.sleep(5)  # Delay to switch to the desired window`-=[]\;'`

# Iterate over each key and press it
for key in keys3:
    pyautogui.press(key)
    print(f"Pressed {key}")
    time.sleep(0.5)  # short delay to see the effect of each key press

print("Finished iterating over all keys.")
