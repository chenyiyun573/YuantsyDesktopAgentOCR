"""
Part1 can all be executed correctly by pynput. - Yiyun Chen
"""


from pynput.keyboard import Controller, Key
import time

# Initialize the keyboard controller
keyboard = Controller()

# List of regular keys
keys1 = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# List of special keys
keys2 = [
    '`', '-', '=', '[', ']', ';', '\'', ',', '.', '/', '\\'
]

# List of navigation keys
keys3 = ['up', 'down', 'left', 'right']

# Start with a delay to allow switching to the target application
time.sleep(5)

# Press each key in keys1
for key in keys1:
    keyboard.press(key)
    keyboard.release(key)
    print(f"Pressed {key}")
    time.sleep(0.5)

# Press each key in keys2
for key in keys2:
    keyboard.press(key)
    keyboard.release(key)
    print(f"Pressed {key}")
    time.sleep(0.5)

# Press each arrow key in keys3
for key in keys3:
    if key == 'up':
        keyboard.press(Key.up)
        keyboard.release(Key.up)
    elif key == 'down':
        keyboard.press(Key.down)
        keyboard.release(Key.down)
    elif key == 'left':
        keyboard.press(Key.left)
        keyboard.release(Key.left)
    elif key == 'right':
        keyboard.press(Key.right)
        keyboard.release(Key.right)
    print(f"Pressed {key}")
    time.sleep(0.5)

print("Finished iterating over all keys.")
