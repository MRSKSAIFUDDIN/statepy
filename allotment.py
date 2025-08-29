import base64
import json
import requests

# API endpoint
API_URL = "http://10.176.100.44:9000/api/StateJITIntegration/ddo-wise-allotment"

# Headers
headers = {
    "UserId": "WbIfmsStateJIT",
    "Password": "KsdrFSrnkUUyawfCp/7vIME5nXXRFJinUQZDx/ZrveOS74dAvLGb2Fo/Fv9imMg1WAjUwgBpmjDo34aIJ32+U67OKl4FUzIbr6xSxgtVVZWhVdtLbZz1RDUdkQIXPxCARGTHW8glfR+375i6rzvL9WMOwVps4mwAx/xaG2ZhtEWZCoDnbiYKvBO6m+QO0VP6c8OYHKPI22FLsK4DlbXiWVI5mCgwTkit6GVE5SRCxncObmKwTjAjFmxP2aUpAdwwI5BJ59hxuGShWtaJD+A7lzup/9O33d154irVkjsDC9C0fK826dJ7R9Qqj3LWjgRD3lUcqjYpLODPD+KdgIZvFQ==",
    "Content-Type": "application/json"
}

# 👉 Raw JSON payload (not yet base64)
payload = {
  "memoNo": "M139",
  "memoDate": "2025-02-26",
  "finyear": "2025-2026",
  "remarks": "Quarterly budget allocation",
  "purpose": "Allotment of funds to DDOs",
  "saoCode": "SAO01",
  "hoaDetails": [
    {
      "hoa": "33-6668-23-936-51-700-61-93-V",
      "childAmount": 5000,
      "totalAmount": 5000,
      "deptCode": "12",
      "ddoCode": "DDO001",
      "allotmentId": 11265,
      "uoNo": "UO-456",
      "uoDate": "2025-08-20"
    }
    
  ]
}

# Step 1: Convert JSON → string
payload_str = json.dumps(payload)

# Step 2: Encode Base64
payload_base64 = base64.b64encode(payload_str.encode("utf-8")).decode("utf-8")

# Step 3: Send request
data = {"data": payload_base64}

response = requests.post(API_URL, headers=headers, json=data)

print("Status:", response.status_code)
print("Response:", response.text)
