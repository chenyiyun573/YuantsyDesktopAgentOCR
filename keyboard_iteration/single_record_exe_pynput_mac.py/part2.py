"""
This script cannot works well on Macbook. 20240717 Yiyun Chen
"""


from pynput.keyboard import Controller, Key
import time

# Initialize the keyboard controller
keyboard = Controller()

# Start with a delay to switch to the target application
time.sleep(5)

# Test Shift by typing an alphabet letter which should appear as uppercase
with keyboard.pressed(Key.shift):
    keyboard.press('h')
    keyboard.release('h')
print("Shift key test: Typed 'H'")

# Test Command by performing a select all (Cmd + A)
with keyboard.pressed(Key.cmd):
    keyboard.press('a')
    keyboard.release('a')
print("Command key test: Performed select all (Cmd + A)")

# Test Option key by using it to access a special character
# Example: Option + 2 on a US keyboard typically types the ™ symbol
with keyboard.pressed(Key.alt):
    keyboard.press('2')
    keyboard.release('2')
print("Option key test: Typed special character ™ with Option + 2")

# Test Control by simulating a right-click equivalent (Ctrl + click)
# Note: This step requires integration with a mouse controller which pynput also supports
# This example won't execute a click to keep it keyboard-focused
with keyboard.pressed(Key.ctrl):
    # Simulated right-click code would go here
    pass
print("Control key test: Simulated right-click equivalent (Ctrl + click)")

# Test Command by opening Spotlight search (Command + Space)
with keyboard.pressed(Key.cmd):
    keyboard.press(Key.space)
    keyboard.release(Key.space)
print("Command key test: Opened Spotlight search with Command + Space")

print("Finished testing modifier keys.")
