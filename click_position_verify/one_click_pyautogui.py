"""
20240709 1646 PT
Verifed.
Using PyAutoGUI to click on the specified position also need divide the x,y coordinate by 2 to match the position of the executing script.

"""



import pyautogui
import time

# Sleep for 3 seconds before moving the mouse
time.sleep(3)

# Move the mouse to the specified coordinates
pyautogui.moveTo(2220/2, 375.5/2, duration=1)

# Click the left mouse button
pyautogui.click()
