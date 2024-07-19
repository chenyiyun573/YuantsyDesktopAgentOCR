import csv
from pynput import keyboard
import time
import os

# Specify the path for the CSV file
csv_file_path = 'key_log.csv'

# Function to initialize the CSV file
def initialize_csv():
    # Check if the file already exists
    if not os.path.isfile(csv_file_path):
        # Open the CSV file to write the headers if it does not exist
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['time', 'key', 'action'])
            writer.writeheader()  # Write the header only once

# Initialize the CSV file
initialize_csv()

# Function to handle key press events
def on_press(key):
    """Function to execute when a key is pressed."""
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['time', 'key', 'action'])
        try:
            action = {'time': time.time(), 'key': key.char, 'action': 'press'}
        except AttributeError:
            action = {'time': time.time(), 'key': str(key), 'action': 'press'}
        writer.writerow(action)
        print(f"Logged: {action}")  # Print message when logging

# Function to handle key release events
def on_release(key):
    """Function to execute when a key is released."""
    action = {'time': time.time(), 'key': str(key), 'action': 'release'}
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['time', 'key', 'action'])
        writer.writerow(action)
    print(f"Logged: {action}")  # Print message when logging
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start monitoring the keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
