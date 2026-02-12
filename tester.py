import requests
import random

CLIENT_URL = "YOUR_URL"

SERIAL = "SAMPLE_SERIAL"
DRONE_NAME = "SAMPLE_DRONE_DEVICE_NAME"

TOKEN = None
CONNECTED = False

# ===============================
# 1. CONNECT
# ===============================
def connect():
    global TOKEN, CONNECTED

    try:
        res = requests.post(
            f"{CLIENT_URL}/auth/connect",
            json={
                "serial": SERIAL,
                "device_name": DRONE_NAME
            },
            timeout=5
        )
        result = res.json()

        if not result["status"]:
            print("Connection failed:", result)
            return

        TOKEN = result["token"]


        CONNECTED = True
        print("Connected successfully")
        print("TOKEN:", TOKEN)

    except Exception as e:
        print("Connection error:", e)

# ===============================
# 2. SEND TELEMETRY
# ===============================
def send_data():
    if not CONNECTED:
        print("Please connect first (option 1)")
        return

    data = {
        "event": 0,
        "serial": SERIAL,
        "device": DRONE_NAME,
        "token": TOKEN,
        "data": {
            "angle": random.randint(0, 360),
            "position": "(2,200)"
        }
    }

    try:
        res = requests.post(
            f"{CLIENT_URL}/api/telemetry",
            json=data,
            timeout=5
        )
        print("Data sent:", res.json())

    except Exception as e:
        print("Data transmission failed:", e)

# ===============================
# 3. SEND EVENT DATA
# ===============================
def send_event_data():
    if not CONNECTED:
        print("Please connect first (option 1)")
        return

    event_data = {
        "event": 1,
        "serial": SERIAL,
        "device": DRONE_NAME,
        "token": TOKEN,
        "data": {
            "angle": random.randint(0, 360),
            "position": "(2,200)",
            "event_detail": {
                "message": "human detected",
                "position": "(12,100)"
            }
        },
    }

    try:
        res = requests.post(
            f"{CLIENT_URL}/api/telemetry",
            json=event_data,
            timeout=5
        )
        print("Event sent:", res.json())

    except Exception as e:
        print("Event transmission failed:", e)

# ===============================
# UPDATE DEVICE TOKEN
# ===============================
def updateToken():
    global TOKEN

    data = {
        "serial": SERIAL,
        "token": TOKEN,
    }

    try:
        res = requests.post(
            f"{CLIENT_URL}/auth/update",
            json=data,
            timeout=5
        )
        result = res.json()

        if not result["status"]:
            print("Token update failed:", result)
            return

        TOKEN = result["token"]
        print("Token updated successfully")
        print("TOKEN:", TOKEN)

    except Exception as e:
        print("Token update error:", e)

# ===============================
# DISCONNECT
# ===============================
def disconnect():
    data = {
        "serial": SERIAL,
        "token": TOKEN
    }

    try:
        res = requests.post(
            f"{CLIENT_URL}/auth/disconnect",
            json=data,
            timeout=5
        )
        print("Disconnected:", res.json())

    except Exception as e:
        print("Disconnect failed:", e)


# ===============================
# MAIN MENU LOOP
# ===============================
while True:
    print("\n-----------------")
    print("1. Connect")
    print("2. Send telemetry data")
    print("3. Send event data")
    print("4. Update token")
    print("5. Disconnect")
    print("-----------------")

    cmd = input("Select > ").strip()

    if cmd == "1":
        connect()
    elif cmd == "2":
        send_data()
    elif cmd == "3":
        send_event_data()
    elif cmd == "4":
        updateToken()
    elif cmd == "5":
        disconnect()
    else:
        print("Invalid input")
