"""

['esc', 'space', 'tab', 'enter', 'backspace'] can be executed correctly. - Yiyun Chen
But Key.caps_lock and Fn cannot be executed correctly. - Yiyun Chen
"""


from pynput.keyboard import Controller, Key
import time

# Initialize the keyboard controller
keyboard = Controller()

# List of keys that are straightforward to control
keys1 = ['esc', 'space', 'tab', 'enter', 'backspace']

# Testing with capslock, which might show toggling behavior
keys2 = ['a', Key.caps_lock, 'a', Key.caps_lock, 'a']

# Start with a delay to switch to the desired application
time.sleep(3)

# Iterate over each key in keys1 and press it with a delay
for key in keys1:
    if key == 'esc':
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
    elif key == 'space':
        keyboard.press(Key.space)
        keyboard.release(Key.space)
    elif key == 'tab':
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
    elif key == 'enter':
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    elif key == 'backspace':
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
    print(f"Pressed {key}")
    time.sleep(2)  # Delay to observe the effect

# Iterate over each key in keys2 and press it with a delay
for key in keys2:
    if key == Key.caps_lock:
        keyboard.press(Key.caps_lock)
        keyboard.release(Key.caps_lock)
    else:
        keyboard.press(key)
        keyboard.release(key)
    print(f"Pressed {key}")
    time.sleep(2)  # Delay to observe the effect

print("Finished pressing special purpose keys.")

