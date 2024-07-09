"""
20240709 0230 PT
This script is used to compare two images and output the differences between them.
This mechanism is also used by human eyes to detect changes in the video stream, which we want to imply in our project. 

"""


import os
import numpy as np
from PIL import Image

def find_differences(image1, image2):
    # Convert images to numpy arrays
    arr1 = np.array(image1)
    arr2 = np.array(image2)

    # Create a boolean mask where differences occur
    diff = arr1 != arr2

    # Debug: Print if any differences are found
    if np.any(diff):
        print("Differences detected.")
    else:
        print("No differences detected.")

    # Combine all differences across channels to a single mask
    diff_mask = np.any(diff, axis=-1)

    # Debug: print positions of different pixels
    diff_positions = np.where(diff_mask)
    print("Positions of different pixels (y, x):", list(zip(*diff_positions)))

    # Create an output image where differences are marked with the second image's pixels,
    # and the rest is set to black
    output = np.zeros_like(arr1)
    output[diff_mask] = arr2[diff_mask]

    return Image.fromarray(output.astype('uint8'))

# Set the directory where the screenshots are stored
directory = 'screenshots'

# File paths
file1 = os.path.join(directory, 'screenshot1.png')
file2 = os.path.join(directory, 'screenshot2.png')
file3 = os.path.join(directory, 'screenshot3.png')  # Define the output file path

# Load the images
image1 = Image.open(file1)
image2 = Image.open(file2)

# Find differences
result_image = find_differences(image1, image2)
result_image.save(file3)  # Save the result image
