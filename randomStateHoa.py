import random
import json
import base64
import hashlib
import requests
import time

API_URL = "http://10.176.100.59:9000/api/StateJITIntegration/state-hoa"

headers = {
    "UserId": "WbIfmsStateJIT",
    "Password": "KsdrFSrnkUUyawfCp/7vIME5nXXRFJinUQZDx/ZrveOS74dAvLGb2Fo/Fv9imMg1WAjUwgBpmjDo34aIJ32+U67OKl4FUzIbr6xSxgtVVZWhVdtLbZz1RDUdkQIXPxCARGTHW8glfR+375i6rzvL9WMOwVps4mwAx/xaG2ZhtEWZCoDnbiYKvBO6m+QO0VP6c8OYHKPI22FLsK4DlbXiWVI5mCgwTkit6GVE5SRCxncObmKwTjAjFmxP2aUpAdwwI5BJ59hxuGShWtaJD+A7lzup/9O33d154irVkjsDC9C0fK826dJ7R9Qqj3LWjgRD3lUcqjYpLODPD+KdgIZvFQ==",
    "Content-Type": "application/json"
}

# Function to generate random numeric strings of fixed length
def rand_digits(length):
    return str(random.randint(10**(length-1), 10**length - 1))

# Function to create a new random payload
def generate_payload():
    return [
        {
            "deptCode": "AM",
            "demandNo": "04",
            "majorHead": rand_digits(4),
            "submajorHead": rand_digits(2),
            "minorHead": rand_digits(3),
            "planStatus": rand_digits(2),
            "schemeHead": rand_digits(3),
            "detailHead": rand_digits(2),
            "subdetailHead": rand_digits(2),
            "votedCharged": "V",
            "description": "Agriculture and Farmers Welfare Scheme",
            "budgetCode": f"AGF{rand_digits(5)}",
            "category": "Revenue",
            "finyear": "2025-2026",
            "capitalComponent": True,
            "salaryComponent": False
        }
    ]

# Run multiple times
for i in range(1, 10):
    payload = generate_payload()
    payload_str = json.dumps(payload)
    
    # Step 1: Base64 encode
    payload_base64 = base64.b64encode(payload_str.encode("utf-8")).decode("utf-8")
    
    # Step 2: SHA256 hash of Base64 string
    payload_hash = hashlib.sha256(payload_base64.encode("utf-8")).hexdigest()
    
    # Step 3: Prepare request body
    data = {
        "data": payload_base64,
        "hash": payload_hash
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data, timeout=10)
        print(f"[{i}] Status: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"[{i}] Error: {e}")

    # Small delay so API is not overloaded
    time.sleep(0.5)
