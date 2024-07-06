import os
import requests
from PIL import ImageGrab
from io import BytesIO
import base64
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
import json
import dotenv
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfileo
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models

dotenv.load_dotenv()  # Load environment variables from .env file

# Setup mouse and keyboard controllers
mouse = MouseController()
keyboard = KeyboardController()

# Initialize chat history
chat_history = []

def get_encoded_image():
    """Capture the screen and encode the image in base64."""
    screenshot = ImageGrab.grab()
    buffered = BytesIO()
    screenshot.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('ascii')

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
        return resp.to_json_string()
    except TencentCloudSDKException as err:
        return str(err)

def send_request_to_gpt4o(image_base64, ocr_results):
    """Send the screenshot and OCR results to GPT-4O and receive the operations."""
    headers = {
        "Content-Type": "application/json",
        "api-key": os.getenv("GPT4V_KEY")
    }
    # Craft the initial message to include both the image and OCR results.
    user_message = {
        "role": "user",
        "content": [
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{image_base64}"
                }
            },
            {
                "type": "text",
                "text": f"""OCR Text: {ocr_results}"""+"""
                Analyze the screenshot and OCR text. Provide detailed mouse and keyboard operations to open YouTube and find the newest BBC news. 
                Return operations one at a time in JSON format. Example response formats:
                

                you can only return one operation each time, wait until next user input image to give next. 
                example response: {"type": "mouse_click", "x": 200, "y": 300, "button": "left", "pressed": true}, 
                or: {"type": "key_press", "key": "f", "special": false}, 
                or: {"type": "mouse_scroll", "dx": 0, "dy": -2}. 
                Continue providing instructions until the task is complete, then return 'DONE'. 
                Please know that I am on Windows, screen 3000*2000, you may need to find a browser and open it first.
                I am using pynut to control so key.cmd is the win key. 
                Please only return json content, no other words or any comments should appear in your response.

                I recommend you key: "cmd" then input "chrome", then key: "enter" to open a browser.
                If you feel win key already pressed, start input chrome; if you feel any button related to chrome already appears try to use mouse to click that position of "Google Chrome App".
                if you feel chrome shows up to enter, start input enter, special:true;
                if you see chrome start, you may need to click one user named "Yiyun Chen" to open the chrome. 
                if you see chrome webpage, you may need to click the address bar where "type a URL".
                then you may need to input youtube.com one by one. 
                then you may need to press enter, special:true to enter the website.
                then find the search bar, click it, then input BBC news, then press enter, special:true to search. 
                Please only return json content, no other words or any comments should appear in your response

                Each operation must be returned in the following JSON format, 
                Each operation must be returned in the following JSON format, 
                Each operation must be returned in the following JSON format, 
                Each operation must be returned in the following JSON format, 
                Each operation must be returned in the following JSON format, 
                Each operation must be returned in the following JSON format, 

                example response: {"type": "mouse_click", "x": 200, "y": 300, "button": "left", "pressed": true}, 
                or: {"type": "key_press", "key": "f", "special": false}, 
                or: {"type": "mouse_scroll", "dx": 0, "dy": -2}. 

                No other text or comments should be included in the response.
                No other text or comments should be included in the response.
                No other text or comments should be included in the response.
                No other text or comments should be included in the response.

                One operation per response,
                One operation per response,
                One operation per response,

                """
            }
        ]
    }
    chat_history.append(user_message)

    payload = {
        "messages": chat_history,
        "temperature": 0.7,
        "top_p": 0.95,
        "max_tokens": 800
    }
    endpoint = "https://yuantsy-westus.openai.azure.com/openai/deployments/YuantsyDesktopAgent/chat/completions?api-version=2024-02-01"
    response = requests.post(endpoint, headers=headers, json=payload)
    response.raise_for_status()
    operations = response.json().get('choices')[0].get('message').get('content')
    
    chat_history.append({
        "role": "assistant",
        "content": operations
    })
    
    return operations

def execute_operations(operations_json):
    """Execute the operations as provided by GPT-4O."""
    
    operations_json = operations_json.strip('`').replace('json\n', '').strip()
    op = json.loads(operations_json)
    
    if op['type'] == 'mouse_click':
        x, y = op['x'], op['y']
        button = Button.left if op['button'] == 'left' else Button.right if op['button'] == 'right' else Button.middle
        mouse.position = (x/2, y/2)
        if op['pressed']:
            mouse.press(button)
        else:
            mouse.release(button)
    elif op['type'] == 'key_press':
        key = op['key']
        try:
            key = getattr(Key, key) if op['special'] else key
        except AttributeError:
            pass  # Key is a regular character
        keyboard.press(key)
        keyboard.release(key)
    elif op['type'] == 'mouse_scroll':
        dx, dy = op['dx'], op['dy']
        mouse.scroll(dx, dy)

def main():
    """Main function to handle the loop of capturing, requesting, and executing."""
    while True:
        image_base64 = get_encoded_image()
        ocr_results = get_ocr_results(image_base64)
        print(ocr_results)
        operations = send_request_to_gpt4o(image_base64, ocr_results)
        print(operations)
        if operations.strip().upper() == 'DONE':
            print("Task completed by GPT-4O.")
            break
        execute_operations(operations)

if __name__ == "__main__":
    main()
