import os
import base64
from PIL import Image
from io import BytesIO
import json
import dotenv
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tiia.v20190529 import tiia_client, models

dotenv.load_dotenv()  # Load environment variables from .env file

def get_encoded_image_from_file(file_path):
    """Read an image file and encode it in base64."""
    with open(file_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('ascii')

def get_encoded_image():
    """Capture the screen and encode the image in base64."""
    screenshot = Image.open("city.png")  # For demonstration, use the 'city.png' as a screenshot.
    buffered = BytesIO()
    screenshot.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('ascii')

def detect_image_labels(image_base64):
    """Detect labels in the given base64 image using Tencent Cloud TIIA."""
    try:
        # Load credentials from environment variables
        SecretId = os.getenv("SECRET_ID")
        SecretKey = os.getenv("SECRET_KEY")
        cred = credential.Credential(SecretId, SecretKey)

        # Setup HTTP and client profile
        httpProfile = HttpProfile()
        httpProfile.endpoint = "tiia.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile

        # Create TIIA client
        client = tiia_client.TiiaClient(cred, "ap-shanghai", clientProfile)

        # Prepare request
        req = models.DetectLabelRequest()
        params = {"ImageBase64": image_base64}
        req.from_json_string(json.dumps(params))

        # Execute request and return results
        resp = client.DetectLabel(req)
        return json.loads(resp.to_json_string())
    except TencentCloudSDKException as err:
        return str(err)

# Read and encode image from file
image_base64 = get_encoded_image_from_file("chrome.png")

# Detect labels
labels_result = detect_image_labels(image_base64)
print("Labels Detected:", labels_result)
