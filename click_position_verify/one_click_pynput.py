"""
20240709 1646 PT
Using pynput need to divide the x,y coordinate by 2 to match the position of the executing script.
Unknown reasons for this.


Verification done. 
"""

from pynput.mouse import Button, Controller
import time

# Create a mouse controller object
mouse = Controller()

# Sleep for 3 seconds before moving the mouse
time.sleep(3)

# Move the mouse to the specified coordinates
mouse.position = (2220/2, 375.5/2)

# Pause for 0.5 seconds after moving to let the mouse cursor settle
time.sleep(0.5)

# Click the left mouse button
mouse.click(Button.left, 1)

