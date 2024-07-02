import os
import csv
import time
from datetime import datetime
from pynput import mouse, keyboard

# Ensure the directory exists
log_dir = './desktop_log'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Define the output CSV file
log_file = os.path.join(log_dir, 'event_log.csv')

# Open the CSV file for writing
with open(log_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestamp', 'Command'])

    def on_click(x, y, button, pressed):
        event_time = datetime.now()
        timestamp = event_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        button_name = 'left' if button == mouse.Button.left else 'right'
        command = {
            "type": "mouse_click",
            "x": x,
            "y": y,
            "button": button_name,
            "pressed": pressed
        }
        writer.writerow([timestamp, command])
        file.flush()
        print(f"[DEBUG] {command}")

    def on_scroll(x, y, dx, dy):
        event_time = datetime.now()
        timestamp = event_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        command = {
            "type": "mouse_scroll",
            "x": x,
            "y": y,
            "dx": dx,
            "dy": dy
        }
        writer.writerow([timestamp, command])
        file.flush()
        print(f"[DEBUG] {command}")

    def on_press(key):
        event_time = datetime.now()
        timestamp = event_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        try:
            key_name = key.char
            special = False
        except AttributeError:
            key_name = str(key).split('.')[1]
            special = True
        command = {
            "type": "key_press",
            "key": key_name,
            "special": special
        }
        writer.writerow([timestamp, command])
        file.flush()
        print(f"[DEBUG] {command}")

    # Set up listeners
    with mouse.Listener(on_click=on_click, on_scroll=on_scroll) as mouse_listener:
        with keyboard.Listener(on_press=on_press) as keyboard_listener:
            mouse_listener.join()
            keyboard_listener.join()
