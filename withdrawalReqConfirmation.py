import base64
import hashlib
import json
import requests

# API endpoint for withdrawal request
API_URL = "http://10.176.100.59:9000/api/StateJITIntegration/allotment-withdrawal-confirmation"

# Headers
headers = {
    "UserId": "WbIfmsStateJIT",
    "Password": "KsdrFSrnkUUyawfCp/7vIME5nXXRFJinUQZDx/ZrveOS74dAvLGb2Fo/Fv9imMg1WAjUwgBpmjDo34aIJ32+U67OKl4FUzIbr6xSxgtVVZWhVdtLbZz1RDUdkQIXPxCARGTHW8glfR+375i6rzvL9WMOwVps4mwAx/xaG2ZhtEWZCoDnbiYKvBO6m+QO0VP6c8OYHKPI22FLsK4DlbXiWVI5mCgwTkit6GVE5SRCxncObmKwTjAjFmxP2aUpAdwwI5BJ59hxuGShWtaJD+A7lzup/9O33d154irVkjsDC9C0fK826dJ7R9Qqj3LWjgRD3lUcqjYpLODPD+KdgIZvFQ==",
    "Content-Type": "application/json"
}

# ✅ Corrected payload
payload = {
    "saoCode": "SAO01",
    "allotmentId": 229341,
    "allotmentWithdrawlRequestId": "1"
}

# Step 1: Convert payload to JSON string
payload_str = json.dumps(payload)

# Step 2: Encode JSON string to Base64
payload_base64 = base64.b64encode(payload_str.encode("utf-8")).decode("utf-8")

# Step 3: SHA256 hash of base64 string
payload_hash = hashlib.sha256(payload_base64.encode("utf-8")).hexdigest()

# Step 4: Prepare final request body
data = {
    "data": payload_base64,
    "hash": payload_hash
}

# Step 5: Send POST request
response = requests.post(API_URL, headers=headers, json=data)

# Step 6: Print response
print("Status Code:", response.status_code)
print("Response:", response.text)
