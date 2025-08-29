import base64
import json
import requests

API_URL = "http://10.176.100.44:9000/api/StateJITIntegration/state-hoa"

headers = {
    "UserId": "WbIfmsStateJIT",
    "Password": "KsdrFSrnkUUyawfCp/7vIME5nXXRFJinUQZDx/ZrveOS74dAvLGb2Fo/Fv9imMg1WAjUwgBpmjDo34aIJ32+U67OKl4FUzIbr6xSxgtVVZWhVdtLbZz1RDUdkQIXPxCARGTHW8glfR+375i6rzvL9WMOwVps4mwAx/xaG2ZhtEWZCoDnbiYKvBO6m+QO0VP6c8OYHKPI22FLsK4DlbXiWVI5mCgwTkit6GVE5SRCxncObmKwTjAjFmxP2aUpAdwwI5BJ59hxuGShWtaJD+A7lzup/9O33d154irVkjsDC9C0fK826dJ7R9Qqj3LWjgRD3lUcqjYpLODPD+KdgIZvFQ==",
    "Content-Type": "application/json"
}
def rand_digits(length):
    return str(random.randint(10**(length-1), 10**length - 1))

# 👉 Your raw JSON payload
payload = [
    {
        "deptCode": "FD",
        "demandNo": rand_digits(2),        # 2-digit
        "majorHead": rand_digits(4),       # 4-digit
        "submajorHead": rand_digits(2),    # 2-digit
        "minorHead": rand_digits(3),       # 3-digit
        "planStatus": rand_digits(2),      # 2-digit
        "schemeHead": rand_digits(3),      # 3-digit
        "detailHead": rand_digits(2),      # 2-digit
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

# Step 1: Convert JSON → string
payload_str = json.dumps(payload)

# Step 2: Encode Base64
payload_base64 = base64.b64encode(payload_str.encode("utf-8")).decode("utf-8")

# Step 3: Send request
data = {"data": payload_base64}

response = requests.post(API_URL, headers=headers, json=data)

print("Status:", response.status_code)
print("Response:", response.text)
