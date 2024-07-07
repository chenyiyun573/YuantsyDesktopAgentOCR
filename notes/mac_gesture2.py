"""
20240706-1526-PT 
This code by GPT4 is actually press and drag by mouse, not the gesture swipe. 
This is a mistake by GPT4. 
"""

import pyautogui
import time

def simulate_swipe(start_x, start_y, end_x, end_y, duration):
    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragTo(end_x, end_y, duration, button='left')

if __name__ == "__main__":
    # Example: Simulate a swipe from (100, 500) to (400, 500) over 0.5 seconds
    simulate_swipe(100, 500, 400, 500, 0.5)

