"""
This script works well on Macbook. 20240717 Yiyun Chen
"""


import pyautogui
import time

keys_special = ['shift', 'ctrl', 'option', 'command']


# Ensure the focus is on a text editor where you can see the output
time.sleep(5)  # Wait for 5 seconds to switch to the text editor

# Test Shift by typing an alphabet letter which should appear as uppercase
pyautogui.keyDown('shift')  # Hold Shift down
pyautogui.press('h')        # Should output 'H' in the text editor
pyautogui.keyUp('shift')    # Release Shift

# Test Command by performing a select all (Cmd + A)
pyautogui.keyDown('command')    # Hold Command down
pyautogui.press('a')        # Normally selects all text in macOS applications
pyautogui.keyUp('command')      # Release Command

# Test Option key by using it to access a special character
# Example: Option + 2 on a US keyboard typically types the ™ symbol
pyautogui.keyDown('option') # Hold Option down
pyautogui.press('2')        # Should type ™ in the text editor if set to US layout
pyautogui.keyUp('option')   # Release Option

# Test Control by performing a right-click equivalent (Ctrl + click)
# You will need to manually observe this as it requires mouse interaction
pyautogui.keyDown('ctrl')   # Hold Control down
pyautogui.click()           # Simulates a right-click in macOS
pyautogui.keyUp('ctrl')     # Release Control

# Test Command by opening Spotlight search (Command + Space)
pyautogui.keyDown('command')    # Hold Command down
pyautogui.press('space')    # Should open Spotlight search
pyautogui.keyUp('command')      # Release Command

print("Finished testing modifier keys.")
