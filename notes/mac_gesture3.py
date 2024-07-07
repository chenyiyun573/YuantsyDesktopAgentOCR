"""
Actually, the 3 finger gesture can be done by keyboard ctrl + left/right arrow
"""

import pyautogui
import time

def control_left_arrow():
    pyautogui.keyDown('ctrl')    # Press down the Control key
    pyautogui.press('left')      # Press the Left Arrow key
    pyautogui.keyUp('ctrl')      # Release the Control key

def control_right_arrow():
    pyautogui.keyDown('ctrl')    # Press down the Control key
    pyautogui.press('right')     # Press the Right Arrow key
    pyautogui.keyUp('ctrl')      # Release the Control key

if __name__ == "__main__":
    time.sleep(2)  # Wait for 2 seconds before executing the key press
    control_left_arrow()  # Simulate Control + Left Arrow
    time.sleep(1)  # Wait for 1 second
    control_right_arrow()  # Simulate Control + Right Arrow
