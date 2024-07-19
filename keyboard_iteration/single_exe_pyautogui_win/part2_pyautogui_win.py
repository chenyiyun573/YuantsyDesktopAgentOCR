"""
This script works well on windows. 20240718 Yiyun Chen
"""

import pyautogui
import time

keys_special = ['shift', 'ctrl', 'alt', 'win']

# Ensure the focus is on a text editor where you can see the output
time.sleep(5)  # Wait for 5 seconds to switch to the text editor

# Test Shift by typing an alphabet letter which should appear as uppercase
pyautogui.keyDown('shift')  # Hold Shift down
pyautogui.press('h')        # Should output 'H' in the text editor
pyautogui.press(';')
pyautogui.keyUp('shift')    # Release Shift

# Test Ctrl by performing a select all (Ctrl + A)
pyautogui.keyDown('ctrl')   # Hold Ctrl down
pyautogui.press('a')        # Normally selects all text in Windows applications
pyautogui.keyUp('ctrl')     # Release Ctrl

# Test Alt key by opening the File menu (Alt + F)
pyautogui.keyDown('alt')    # Hold Alt down
pyautogui.press('f')        # Should open the File menu in most applications
pyautogui.keyUp('alt')      # Release Alt

# Test Win key by opening the Start Menu (Win key)
pyautogui.keyDown('win')    # Hold Win down
pyautogui.press('d')        # Minimizes all windows, showing the desktop
pyautogui.keyUp('win')      # Release Win

# Test Win key by opening the Run dialog (Win + R)
pyautogui.keyDown('win')    # Hold Win down
pyautogui.press('r')        # Should open the Run dialog
pyautogui.keyUp('win')      # Release Win

print("Finished testing modifier keys.")
