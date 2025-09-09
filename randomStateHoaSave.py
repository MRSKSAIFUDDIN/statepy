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

Globalcount = 2 

# Function to generate random numeric strings of fixed length
def rand_digits(length):
    return str(random.randint(10**(length-1), 10**length - 1))

# Generate HOA strings and save to file
def generate_and_save_hoas(file_name="hoas.txt", count=Globalcount):
    with open(file_name, "w") as f:
        for _ in range(count):
            demandNo = "04"
            majorHead = rand_digits(4)
            submajorHead = rand_digits(2)
            minorHead = rand_digits(3)
            planStatus = rand_digits(2)
            schemeHead = rand_digits(3)
            detailHead = rand_digits(2)
            subdetailHead = rand_digits(2)
            votedCharged = "V"

            hoa = f"{demandNo}-{majorHead}-{submajorHead}-{minorHead}-{planStatus}-{schemeHead}-{detailHead}-{subdetailHead}-{votedCharged}"
            f.write(hoa + "\n")

    print(f"✅ Generated {count} HOAs and saved to {file_name}")

# Build payload using a given HOA string
def generate_payload(hoa):
    parts = hoa.split("-")
    return [
        {
            "deptCode": "AM",
            "demandNo": parts[0],
            "majorHead": parts[1],
            "submajorHead": parts[2],
            "minorHead": parts[3],
            "planStatus": parts[4],
            "schemeHead": parts[5],
            "detailHead": parts[6],
            "subdetailHead": parts[7],
            "votedCharged": parts[8],
            "description": "Agriculture and Farmers Welfare Scheme",
            "budgetCode": f"AGF{rand_digits(5)}",
            "category": "Revenue",
            "finyear": "2025-2026",
            "capitalComponent": True,
            "salaryComponent": False
        }
    ]

# Step 1: Generate HOA file (only once)
generate_and_save_hoas("hoas.txt", count=Globalcount)

# Step 2: Read HOAs and hit API
with open("hoas.txt", "r") as f:
    hoas = [line.strip() for line in f.readlines()]

for i, hoa in enumerate(hoas, start=1):
    payload = generate_payload(hoa)
    payload_str = json.dumps(payload)

    # Step A: Base64 encode
    payload_base64 = base64.b64encode(payload_str.encode("utf-8")).decode("utf-8")

    # Step B: Hash of Base64 string
    payload_hash = hashlib.sha256(payload_base64.encode("utf-8")).hexdigest()

    # Step C: Prepare data with both base64 and hash
    data = {
        "data": payload_base64,
        "hash": payload_hash
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data, timeout=10)
        print(f"[{i}] HOA: {hoa} → Status: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"[{i}] HOA: {hoa} → Error: {e}")

    time.sleep(0.5)  # delay to avoid flooding
