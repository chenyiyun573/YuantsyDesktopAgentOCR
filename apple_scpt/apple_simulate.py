import subprocess

def execute_applescript(script_path):
    subprocess.run(["osascript", script_path])

if __name__ == "__main__":
    # Path to the AppleScript
    script_path = "./apple_scpt/swipe_desktop.scpt"
    execute_applescript(script_path)
