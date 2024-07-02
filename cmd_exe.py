import csv
import time
import ast
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController

# Initialize controllers
mouse = MouseController()
keyboard = KeyboardController()

def execute_command(command):
    command_type = command.get("type")
    
    if command_type == "mouse_click":
        x = command.get("x")
        y = command.get("y")
        button = command.get("button")
        pressed = command.get("pressed")

        mouse.position = (x/2, y/2)
        mouse_button = Button.left if button == "left" else Button.right
        
        if pressed:
            mouse.press(mouse_button)
        else:
            mouse.release(mouse_button)
    
    elif command_type == "key_press":
        key = command.get("key")
        special = command.get("special", False)
        
        if special:
            key = getattr(Key, key, None)
        if key:
            keyboard.press(key)
            keyboard.release(key)
    
    elif command_type == "mouse_scroll":
        dx = command.get("dx", 0)
        dy = command.get("dy", 0)
        
        mouse.scroll(dx, dy)
    else:
        print(f"Unknown command type: {command_type}")

# Read commands from CSV file and execute them
csv_file_path = 'c:/Users/yiyun/Desktop/YuantsyDesktopAgentOCR/desktop_log/event_log.csv'

with open(csv_file_path, mode='r', newline='') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        timestamp = row['Timestamp']
        command_str = row['Command']
        try:
            # Use ast.literal_eval to safely evaluate the string as a dictionary
            command = ast.literal_eval(command_str)
            execute_command(command)
            print(f"Executed command at {timestamp}: {command}")
            time.sleep(4)
        except (SyntaxError, ValueError) as e:
            print(f"Error: {e} in line: {command_str}")
