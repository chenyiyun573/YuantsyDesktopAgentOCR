import subprocess

applescript_code = '''
tell application "System Events"
    key code 123 using control down
end tell

delay 1

tell application "System Events"
    key code 124 using {command down}
end tell

delay 1

tell application "System Events"
    key code 20 using {command down, shift down}
end tell

delay 1

tell application "System Events"
    key code 53 using {option down, command down}
end tell

delay 1

tell application "System Events"
    key code 49 using {command down}
end tell

delay 1

tell application "System Events"
    key code 48 using {command down}
end tell

delay 1

tell application "System Events"
    key code 126 using control down
end tell

delay 1

tell application "System Events"
    key code 125 using control down
end tell

delay 1

tell application "System Events"
    key code 124 using control down
end tell
'''

process = subprocess.Popen(['osascript', '-e', applescript_code], stdout=subprocess.PIPE)
stdout, stderr = process.communicate()

print(stdout)
print(stderr)
