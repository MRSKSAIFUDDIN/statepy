import base64
import json
import requests
import hashlib

# API endpoint
API_URL = "http://10.176.100.59:9000/api/StateJITIntegration/allotment-files"

# Headers
headers = {
    "UserId": "WbIfmsStateJIT",
    "Password": "KsdrFSrnkUUyawfCp/7vIME5nXXRFJinUQZDx/ZrveOS74dAvLGb2Fo/Fv9imMg1WAjUwgBpmjDo34aIJ32+U67OKl4FUzIbr6xSxgtVVZWhVdtLbZz1RDUdkQIXPxCARGTHW8glfR+375i6rzvL9WMOwVps4mwAx/xaG2ZhtEWZCoDnbiYKvBO6m+QO0VP6c8OYHKPI22FLsK4DlbXiWVI5mCgwTkit6GVE5SRCxncObmKwTjAjFmxP2aUpAdwwI5BJ59hxuGShWtaJD+A7lzup/9O33d154irVkjsDC9C0fK826dJ7R9Qqj3LWjgRD3lUcqjYpLODPD+KdgIZvFQ==",
    "Content-Type": "application/json"
}

file_path = "D:\\SAIF\\python\\API DOCS\\IntegrationAPI\\pdf\\fileexample_PDF_1MB.pdf"

# Read + encode file
with open(file_path, "rb") as f:
    file_b64 = base64.b64encode(f.read()).decode()

# M126
payload = {
    "MemoNo": "M132", 
    "MemoDate": "2025-10-01",
    "Finyear": "2025-2026",
    "SaoCode": "SAO123",
    "File": file_b64,
    "FileName" : "file.pdf",
    "FileType" : "application/pdf"
}

# Step 1: Convert JSON → string
payload_str = json.dumps(payload)

# Step 2: Encode Base64
payload_base64 = base64.b64encode(payload_str.encode("utf-8")).decode("utf-8")

# Step 3: SHA256 hash of base64 string
payload_hash = hashlib.sha256(payload_base64.encode("utf-8")).hexdigest()

# Step 4: Final request body
newdata = {
    "data": payload_base64,
    "hash": payload_hash
}

# Step 5: Send request
response = requests.post(API_URL, headers=headers, json=newdata)

print("Status:", response.status_code)
print("Response:", response.text)

