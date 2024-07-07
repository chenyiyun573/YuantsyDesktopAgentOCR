from pynput.keyboard import Key, Controller
import time

# Create a Controller object
keyboard = Controller()

# Number of times to press the keys
press_count = 5

# Function to press and release a combination of keys in the specified order
def press_and_release_keys(main_key, *keys):
    keyboard.press(main_key)
    time.sleep(1)  # Pause between pressing main key and other keys
    for key in keys:
        keyboard.press(key)
        time.sleep(0.5)
    for key in keys:
        keyboard.release(key)
        time.sleep(0.5)
    time.sleep(1)  # Pause between pressing main key and other keys
    keyboard.release(main_key)

# Press Ctrl + Right and Ctrl + Left multiple times
for _ in range(press_count):
    # Press Ctrl + Right
    press_and_release_keys(Key.ctrl, Key.right)
    print("Ctrl + Right")
    time.sleep(1)  # Pause between presses

    # Press Ctrl + Left
    press_and_release_keys(Key.ctrl, Key.left)
    print("Ctrl + Left")
    time.sleep(1)  # Pause between presses
