"""
20240702 1022 PT
In this python, I test if the x,y coordinate of recorder matches the position of the executing script. 
The result is that, the x,y coordinate of recorder is correct, but for exeuating script, it requires the x,y coordinate divided by 2 then execute.
Unknown reasons for this. 
"""

from pynput.mouse import Controller, Listener, Button
from pynput.keyboard import Listener as KeyboardListener, Key
import time

# Set expected positions to click
click_positions = [
    (100, 100),
    (2900, 100),
    (100, 1900)
]

# Initialize mouse controller
mouse = Controller()

def automated_click():
    for pos in click_positions:
        mouse.position = pos
        mouse.click(Button.left)
        print(f"Clicked at {pos}")
        time.sleep(1)  # wait a second between clicks

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Detected click at ({x}, {y})")

def on_press(key):
    # Stop listener if escape key is pressed
    if key == Key.esc:
        return False

if __name__ == "__main__":
    # Set up the listener for mouse clicks
    with Listener(on_click=on_click) as listener:
        with KeyboardListener(on_press=on_press):
            print("Automated clicking will start in 3 seconds...")
            time.sleep(3)  # Delay to switch to the screen where you want to test
            automated_click()
            listener.join()
