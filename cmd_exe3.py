"""
20240706-2103-PT
I found that the cvs of special key recorded by pynput cannot be executed by pyautogui in cmd_exe2.py successfully.
like the cmd and command below. So it need to be converted to the format of pyautogui.
This is modified into cmd_exe3.py.
"""


import csv
import time
import ast
import pyautogui

# Function to execute commands
def execute_command(command):
    command_type = command.get("type")
    
    if command_type == "mouse_click":
        x = command.get("x")
        y = command.get("y")
        button = command.get("button")
        pressed = command.get("pressed")

        pyautogui.moveTo(x, y)
        
        if button == "left":
            if pressed:
                pyautogui.mouseDown(button='left')
            else:
                pyautogui.mouseUp(button='left')
        elif button == "right":
            if pressed:
                pyautogui.mouseDown(button='right')
            else:
                pyautogui.mouseUp(button='right')
    
    elif command_type == "key_press":
        key = command.get("key")
        special = command.get("special", False)
        action = command.get("action")

        # Map special keys to pyautogui format
        if special:
            if key == 'cmd':
                key = 'command'
            key = key.lower()

        if action == "press":
            pyautogui.keyDown(key)
        elif action == "release":
            pyautogui.keyUp(key)
    
    elif command_type == "mouse_scroll":
        dx = command.get("dx", 0)
        dy = command.get("dy", 0)
        
        pyautogui.scroll(dy, dx)
    else:
        print(f"Unknown command type: {command_type}")

# Read commands from CSV file and execute them
csv_file_path = './desktop_log/event_log.csv'

with open(csv_file_path, mode='r', newline='') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        timestamp = row['Timestamp']
        command_str = row['Command']
        try:
            # Use ast.literal_eval to safely evaluate the string as a dictionary
            command = ast.literal_eval(command_str)
            print(f"Executing command at {timestamp}: {command}")
            execute_command(command)
            time.sleep(1)  # Adjust the sleep time as necessary
        except (SyntaxError, ValueError) as e:
            print(f"Error: {e} in line: {command_str}")
