"""
I write this script to verify if the coordinate x,y from OCR API is allied with the x,y pixel position of the screen.
The results shows that the coordinate matches. 
"""

import os
import requests
from PIL import Image, ImageDraw, ImageFont, ImageGrab
from io import BytesIO
import time
import base64
import json
import dotenv
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models

dotenv.load_dotenv()  # Load environment variables from .env file

def get_encoded_image():
    """Capture the screen and encode the image in base64."""
    screenshot = ImageGrab.grab()
    buffered = BytesIO()
    screenshot.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('ascii'), screenshot

def get_ocr_results(image_base64):
    """Get OCR results from Tencent Cloud OCR for the given base64 image."""
    try:
        # Load credentials from environment variables
        SecretId = os.getenv("SECRET_ID")
        SecretKey = os.getenv("SECRET_KEY")
        cred = credential.Credential(SecretId, SecretKey)

        # Setup HTTP and client profile
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ocr.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile

        # Create OCR client
        client = ocr_client.OcrClient(cred, "ap-shanghai", clientProfile)

        # Prepare request
        req = models.GeneralBasicOCRRequest()
        params = {"ImageBase64": image_base64}
        req.from_json_string(json.dumps(params))

        # Execute request and return results
        resp = client.GeneralBasicOCR(req)
        return json.loads(resp.to_json_string())
    except TencentCloudSDKException as err:
        return str(err)

def add_ocr_results_to_image(image, ocr_results):
    """Add OCR results to the image."""
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    if 'TextDetections' in ocr_results:
        for item in ocr_results['TextDetections']:
            text = item['DetectedText']
            item_polygon = item.get('ItemPolygon', {})
            x = item_polygon.get('X', 0)
            y = item_polygon.get('Y', 0)
            width = item_polygon.get('Width', 0)
            height = item_polygon.get('Height', 0)

            # Draw bounding box
            draw.rectangle([x, y, x + width, y + height], outline="red", width=2)
            
            # Draw text within the bounding box
            draw.text((x, y), text, fill="red", font=font)

    return image


time.sleep(3)

# Capture screenshot and get its dimensions
image_base64, screenshot = get_encoded_image()
width, height = screenshot.size
print(f"Width: {width}, Height: {height}")

# Get OCR results
ocr_results = get_ocr_results(image_base64)
print("OCR Results:", ocr_results)

# Add OCR results to the image
image_with_ocr = add_ocr_results_to_image(screenshot, ocr_results)

# Save the image with OCR results
output_path = "screenshot_with_ocr.png"
image_with_ocr.save(output_path)
print(f"OCR results added to image and saved as {output_path}")
