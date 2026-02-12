해당 문서는 gemini-2.5-flash 로 자동 번역되었습니다.<br>정확한 내용은 여기서 확인해주세요: [English Document](https://github.com/seyun4047/drone-platform-trans-tester/blob/main/README.md)

---

# Drone Data Transmission Tester

---
## Repository Overview
This repository provides a **Drone Data Transmission Tester**  
that simulates drone connection, telemetry, and event data
to verify the server’s API behavior.
---

## How It Works

| Step | API Endpoint             | Description | Purpose | etc.      |
|------|--------------------------|-------------|---------|-----------|
| 1 | `/auth/connect`          | Sends drone serial and device name. Receives authentication token if approved. | Establish a valid session between drone and server |
| 2 | `/api/telemetry`| Sends normal telemetry data (angle, position) with token. | Transmit periodic drone status information | (event=0) |
| 3 | `/api/telemetry` | Sends telemetry with event flag and event details (e.g., human detected). | Report important detection events | (event=1) |
| 4 | `/auth/update`           | Sends current token and receives a refreshed token. | Maintain a valid authenticated session |
| 5 | `/auth/disconnect`       | Sends disconnect request with token. | Cleanly close the connection |

---

## Installation
Install the required dependencies:
```bash
pip install -r requirements.txt
```
---
## Usage
Run the application:
```bash
python3 main.py
```
---


---

