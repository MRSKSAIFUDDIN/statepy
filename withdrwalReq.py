import base64
import json
import requests

# API endpoint for withdrawal request
API_URL = "http://10.176.100.59:9000/api/StateJITIntegration/withdrawal-request"

# Headers (as per your example)
headers = {
    "UserId": "WbIfmsStateJIT",
    "Password": "KsdrFSrnkUUyawfCp/7vIME5nXXRFJinUQZDx/ZrveOS74dAvLGb2Fo/Fv9imMg1WAjUwgBpmjDo34aIJ32+U67OKl4FUzIbr6xSxgtVVZWhVdtLbZz1RDUdkQIXPxCARGTHW8glfR+375i6rzvL9WMOwVps4mwAx/xaG2ZhtEWZCoDnbiYKvBO6m+QO0VP6c8OYHKPI22FLsK4DlbXiWVI5mCgwTkit6GVE5SRCxncObmKwTjAjFmxP2aUpAdwwI5BJ59hxuGShWtaJD+A7lzup/9O33d154irVkjsDC9C0fK826dJ7R9Qqj3LWjgRD3lUcqjYpLODPD+KdgIZvFQ==",
    "Content-Type": "application/json"
}

# ✅ Corrected payload
payload = {
    "memoNo": "M226",
    "memoDate": "2025-08-26",
    "finyear": "2025-2026",
    "remarks": "Quarterly budget allocation",
    "purpose": "Allotment of funds to DDOs",
    "saoCode": "SAO01",
    "hoa": "34-2401-01-101-02-201-02-03-V",
    "childWithdrawlAmount": 50000,
    "deptCode": "12",
    "ddoCode": "DDO001",
    "allotmentId": 11227,
    "uoNo": "UO-456",
    "uoDate": "2025-08-20",
    "totalWithdrawlAmount": 50000,
    "allotmentWithdrawlId": "1"
}

# Step 1: Convert payload to JSON string
payload_str = json.dumps(payload)

# Step 2: Encode JSON string to Base64
payload_base64 = base64.b64encode(payload_str.encode("utf-8")).decode("utf-8")

# Step 3: Prepare data for API
data = {"data": payload_base64}

# Step 4: Send POST request
response = requests.post(API_URL, headers=headers, json=data)

# Step 5: Print response
print("Status Code:", response.status_code)
print("Response:", response.text)
