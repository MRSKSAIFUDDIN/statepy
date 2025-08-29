import base64
import json
import requests
import random
import time
from datetime import datetime, timedelta

# ========= GLOBAL CONFIG =========
API_URL = "http://10.176.100.44:9000/api/StateJITIntegration/ddo-wise-allotment"
ITERATIONS = 10   # 🔹 how many payloads to send
AMOUNT_MIN = 1000000
AMOUNT_MAX = 500000000
# =================================

headers = {
    "UserId": "WbIfmsStateJIT",
    "Password": "KsdrFSrnkUUyawfCp/7vIME5nXXRFJinUQZDx/ZrveOS74dAvLGb2Fo/Fv9imMg1WAjUwgBpmjDo34aIJ32+U67OKl4FUzIbr6xSxgtVVZWhVdtLbZz1RDUdkQIXPxCARGTHW8glfR+375i6rzvL9WMOwVps4mwAx/xaG2ZhtEWZCoDnbiYKvBO6m+QO0VP6c8OYHKPI22FLsK4DlbXiWVI5mCgwTkit6GVE5SRCxncObmKwTjAjFmxP2aUpAdwwI5BJ59hxuGShWtaJD+A7lzup/9O33d154irVkjsDC9C0fK826dJ7R9Qqj3LWjgRD3lUcqjYpLODPD+KdgIZvFQ==",
    "Content-Type": "application/json"
}

def random_amount():
    return random.randint(AMOUNT_MIN, AMOUNT_MAX)

def random_date():
    start_date = datetime(2025, 1, 1)
    end_date = datetime(2025, 12, 31)
    rand_days = random.randint(0, (end_date - start_date).days)
    return (start_date + timedelta(days=rand_days)).strftime("%Y-%m-%d")

def rand_digits(length):
    return str(random.randint(10**(length-1), 10**length - 1))

# Read HOAs
with open("hoas.txt", "r") as f:
    hoas = [line.strip() for line in f.readlines() if line.strip()]

# Read DDO codes
with open("ddocode.txt", "r") as f:
    ddocodes = [line.strip() for line in f.readlines() if line.strip()]

# 🔹 Run for N payloads
for n in range(1, ITERATIONS + 1):
    hoa_details_list = []

    # Loop through all HOAs and build array
    for i, hoa in enumerate(hoas, start=1):
        amount = random_amount()
        # print(hoa)
        ddo = random.choice(ddocodes)
        # print(ddo)
        hoa_details_list.append({
            "hoa": f"{hoa}",
            "childAmount": amount,
            "totalAmount": amount,
            "deptCode": "12",
            "ddoCode": f"{ddo}",
            "allotmentId": f"{rand_digits(5)}{n}",   # unique per payload
            "uoNo": f"UO-{n}{100 + i}",       # unique
            "uoDate": random_date()
        })

    # 🔹 One payload with all hoaDetails
    payload = {
        "memoNo": f"M{rand_digits(2)}{n}",
        "memoDate": random_date(),
        "finyear": "2025-2026",
        "remarks": f"Quarterly budget allocation batch {n}",
        "purpose": "Allotment of funds to DDOs",
        "saoCode": f"SAO{str(n).zfill(2)}",
        "hoaDetails": hoa_details_list
    }
    print(payload)
    # Encode payload
    payload_str = json.dumps(payload)
    payload_base64 = base64.b64encode(payload_str.encode("utf-8")).decode("utf-8")
    data = {"data": payload_base64}

    try:
        response = requests.post(API_URL, headers=headers, json=data, timeout=10)
        print(f"[Batch {n}] Status: {response.status_code} | Response: {response.text}")
    except Exception as e:
        print(f"[Batch {n}] Error: {e}")

    time.sleep(0.5)
