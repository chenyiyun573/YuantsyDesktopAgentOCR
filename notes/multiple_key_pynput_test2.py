"""
20240706-1559-PT 
I originally want the code to execute multiple key events.
However, it does not work as expected to swipe screen on mac. 

So here, I want to test if the left, right works on mac. 
The result shows that left, and right works on mac.
"""

from pynput.keyboard import Key, Controller
import time

# Create a Controller object
keyboard = Controller()

# Number of times to press the keys
press_count = 5

# Function to press and release a combination of keys
def press_keys(*keys):
    for key in keys:
        keyboard.press(key)
    for key in reversed(keys):
        keyboard.release(key)

# Press Ctrl + Right and Ctrl + Left multiple times
for _ in range(press_count):
    # Press Ctrl + Right
    press_keys(Key.right)
    print("Right")
    time.sleep(0.5)  # Pause between presses
    # Press Ctrl + Right
    press_keys(Key.right)
    print("Right")
    time.sleep(0.5)  # Pause between presses
    # Press Ctrl + Right
    press_keys(Key.right)
    print("Right")
    time.sleep(0.5)  # Pause between presses
    # Press Ctrl + Right
    press_keys(Key.right)
    print("Right")
    time.sleep(0.5)  # Pause between presses

    # Press Ctrl + Left
    press_keys(Key.left)
    print("Left")
    time.sleep(0.5)  # Pause between presses
    # Press Ctrl + Left
    press_keys(Key.left)
    print("Left")
    time.sleep(0.5)  # Pause between presses
    # Press Ctrl + Left
    press_keys(Key.left)
    print("Left")
    time.sleep(0.5)  # Pause between presses
    # Press Ctrl + Left
    press_keys(Key.left)
    print("Left")
    time.sleep(0.5)  # Pause between presses
