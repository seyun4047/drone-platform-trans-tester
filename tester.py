import time
import requests
import random

CLIENT_URL = "YOUR_URL"

# =====================================================
# TEST DRONE SET-SERIAL
# =====================================================
TEST_DRONES = [
    "A1001", "A1002",
    "B2001", "B2002",
    "C3001", "C3002",
    "D4001", "D4002",
    "E5001", "E5002",
]
# =====================================================
# TEST DRONE SET-NAME
# =====================================================
TEST_DRONES_NAME = [
    "A1", "A2",
    "B1", "B2",
    "C1", "C2",
    "D1", "D2",
    "E1", "E2",
]

# =====================================================
# TEST EVENT IMAGE URL SET
# =====================================================
IMAGES = [

]

# =====================================================
# DRONE STATE
# =====================================================
DRONES = {}
BASE_LAT = 37.51762
BASE_LON = 127.04100

for serial, name in zip(TEST_DRONES, TEST_DRONES_NAME):
    DRONES[serial] = {
        "device_name": name,
        "token": None,
        "connected": False,
        "lat": BASE_LAT + random.uniform(-0.01, 0.01),
        "lon": BASE_LON + random.uniform(-0.01, 0.01),
        "power": 100.0
    }

# =====================================================
# SELECT DRONES BY COUNT
# =====================================================
def select_drones_by_count(only_connected=False):
    try:
        count = int(input(f"How many drones? (max {len(TEST_DRONES)}) > ").strip())
    except:
        print("Invalid input")
        return []

    count = min(count, len(TEST_DRONES))
    selected = TEST_DRONES[:count]

    if only_connected:
        selected = [s for s in selected if DRONES[s]["connected"]]

    if not selected:
        print("❌ No valid drones.")
        return []

    return selected

# =====================================================
# STATE UPDATE
# =====================================================
def update_drone_state(serial):
    drone = DRONES[serial]

    drone["lat"] += random.uniform(-0.005, 0.005)
    drone["lon"] += random.uniform(-0.005, 0.005)

    drone["power"] -= random.uniform(0.2, 1.2)
    drone["power"] = max(drone["power"], 0)

    return (
        round(drone["lat"], 6),
        round(drone["lon"], 6),
        int(drone["power"])
    )

# =====================================================
# CONNECT
# =====================================================
def connect(serial):
    drone = DRONES[serial]

    try:
        res = requests.post(
            f"{CLIENT_URL}/auth/connect",
            json={
                "serial": serial,
                "device_name": drone["device_name"]
            },
            timeout=5
        )

        result = res.json()

        if not result.get("status"):
            print(f"[{serial}] ❌ Connect failed")
            return

        drone["token"] = result["token"]
        drone["connected"] = True
        print(f"[{serial}] ✅ Connected")

    except Exception as e:
        print(f"[{serial}] Connect error:", e)


def connect_multiple():
    selected = select_drones_by_count(only_connected=False)
    for serial in selected:
        if not DRONES[serial]["connected"]:
            connect(serial)

# =====================================================
# UPDATE TOKEN
# =====================================================
def update_token(serial):
    drone = DRONES[serial]
    if not drone["connected"]:
        return

    try:
        res = requests.post(
            f"{CLIENT_URL}/auth/update",
            json={
                "serial": serial,
                "token": drone["token"]
            },
            timeout=5
        )

        result = res.json()
        if result.get("status"):
            drone["token"] = result["token"]
            print(f"[{serial}] 🔄 Token updated")
        else:
            print(f"[{serial}] ❌ Token update failed")

    except Exception as e:
        print(f"[{serial}] Update error:", e)


def update_multiple():
    selected = select_drones_by_count(only_connected=True)
    for serial in selected:
        update_token(serial)

# =====================================================
# DISCONNECT
# =====================================================
def disconnect(serial):
    drone = DRONES[serial]
    if not drone["connected"]:
        return

    try:
        requests.post(
            f"{CLIENT_URL}/auth/disconnect",
            json={
                "serial": serial,
                "token": drone["token"]
            },
            timeout=5
        )

        drone["connected"] = False
        print(f"[{serial}] 🔌 Disconnected")

    except Exception as e:
        print(f"[{serial}] Disconnect error:", e)


def disconnect_multiple():
    selected = select_drones_by_count(only_connected=True)
    for serial in selected:
        disconnect(serial)

# =====================================================
# TELEMETRY
# =====================================================
def send_telemetry(serial):
    drone = DRONES[serial]
    if not drone["connected"]:
        return

    lat, lon, power = update_drone_state(serial)

    payload = {
        "event": 0,
        "serial": serial,
        "device": drone["device_name"],
        "token": drone["token"],
        "data": {
            "speed": round(random.uniform(20.0, 50.0), 2),
            "person_count": 0,
            "longitude": lon,
            "latitude": lat,
            "power": power
        },
        "updatedAt": int(time.time() * 1000)
    }

    try:
        r = requests.post(f"{CLIENT_URL}/api/telemetry", json=payload, timeout=5)
        print(f"[{serial}] Telemetry | {power}% | {r.status_code}")
    except Exception as e:
        print(f"[{serial}] Telemetry error:", e)

# =====================================================
# EVENT
# =====================================================
def send_event(serial):
    drone = DRONES[serial]
    if not drone["connected"]:
        return

    lat, lon, power = update_drone_state(serial)

    payload = {
        "event": 1,
        "serial": serial,
        "device": drone["device_name"],
        "token": drone["token"],
        "data": {
            "speed": round(random.uniform(20.0, 50.0), 2),
            "person_count": 1,
            "longitude": lon,
            "latitude": lat,
            "power": power,
            "event_detail": {
                "message": "human detected",
                "image": random.choice(IMAGES)
            }
        },
        "updatedAt": int(time.time() * 1000)
    }

    try:
        r = requests.post(f"{CLIENT_URL}/api/telemetry", json=payload, timeout=5)
        print(f"[{serial}] !!! Event | {power}% | {r.status_code}")
    except Exception as e:
        print(f"[{serial}] Event error:", e)

# =====================================================
# AUTO SIMULATE
# =====================================================
def auto_send():
    try:
        interval = float(input("Interval (seconds) > ").strip())
        selected = select_drones_by_count(only_connected=True)
    except:
        print("Invalid input")
        return

    if not selected:
        print("X No connected drones.")
        return

    print(f"\nSimulating {len(selected)} drones")
    print(f"Interval: {interval} sec | Ratio 3:1")
    print("Press Ctrl+C to stop\n")

    try:
        while True:
            for serial in selected:
                if random.randint(0, 3) < 3:
                    send_telemetry(serial)
                else:
                    send_event(serial)

            time.sleep(interval)

    except KeyboardInterrupt:
        print("\nSimulation stopped.")

# =====================================================
# MAIN MENU
# =====================================================
while True:
    print("\n----------------------------")
    print("1. Connect one")
    print("2. Connect multiple")
    print("3. Update one")
    print("4. Update multiple")
    print("5. Disconnect one")
    print("6. Disconnect multiple")
    print("7. Send telemetry (one)")
    print("8. Send event (one)")
    print("9. Auto simulate (3:1)")
    print("----------------------------")

    cmd = input("Select > ").strip()

    if cmd == "1":
        s = input("Serial > ").strip()
        if s in DRONES:
            connect(s)

    elif cmd == "2":
        connect_multiple()

    elif cmd == "3":
        s = input("Serial > ").strip()
        if s in DRONES:
            update_token(s)

    elif cmd == "4":
        update_multiple()

    elif cmd == "5":
        s = input("Serial > ").strip()
        if s in DRONES:
            disconnect(s)

    elif cmd == "6":
        disconnect_multiple()

    elif cmd == "7":
        s = input("Serial > ").strip()
        if s in DRONES:
            send_telemetry(s)

    elif cmd == "8":
        s = input("Serial > ").strip()
        if s in DRONES:
            send_event(s)

    elif cmd == "9":
        auto_send()

    else:
        print("Invalid input")
