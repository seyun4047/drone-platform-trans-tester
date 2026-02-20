Korean version: [한국어 문서](https://github.com/seyun4047/drone-platform-trans-tester/blob/main/README.kr.md)

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
python3 tester.py
```
---


---

<div align="center">
 
# PROJECT OVERVIEW

  <a href="https://youtu.be/7IdtRp_fe1U" target="_blank">
    <img width="900" src="https://github.com/user-attachments/assets/7bc575a8-27f7-4e64-b04e-1e33d4a7848e" alt="MAIN_DRONE_LOGO"/>
  </a>
   <p><strong>Click & Watch the Introduction Video</strong></p> 

---


It is a **Manufacturer-Independent Drone Monitoring Platform.**

It is designed to manage various drones within a single environment, enabling both **high-end professional drones
<br>and commercially available hobby camera drones**
to be used for lifesaving and disaster response.



---

## Project Structure

This platform consists of multiple independent repositories:

| Component | Description                                       | Repository                                                              |
|---------|---------------------------------------------------|-------------------------------------------------------------------------|
| Server | Core drone platform server (API, Auth, Telemetry) | [GitHub](https://github.com/seyun4047/drone-platform-server)            |
| Monitoring Server | Real-time Drone health check monitoring service   | [GitHub](https://github.com/seyun4047/drone-platform-monitoring-server) |
| Drone Data Tester | Test client for drone telemetry & data simulation | [GitHub](https://github.com/seyun4047/drone-platform-trans-tester)       |
| Drone Client | Drone Data Collection, Transmission & Analysis | [GitHub](https://github.com/seyun4047/drone-platform-client)            |
| Dashboard | Drone platform's front-end | [GitHub](https://github.com/seyun4047/drone-platform-dashboard)            |
| Docs | Platform Documents, API's | [GitHub](https://github.com/seyun4047/drone-platform-docs)|



---



## Background

</div>

Although custom drones, commercial drones, and consumer drones share similar basic control mechanisms,
<br>their operational methods and **command-and-control structures** in real-world environments vary significantly.

In practice, drones are often utilized as tools that depend heavily on:
- Specific equipment
- Highly trained personnel

Recently, many institutions and companies have attempted to build drone systems integrated with AI technologies.  
However, these systems have clear limitations.
<br>They typically rely on tuning specific drone models or operating a single type of custom-built drone,
<br>which results in strong dependency on specialized personnel and proprietary technologies.

Such dependency is particularly critical in **life-saving and disaster response operations**.

---

<div align="center">

 ## Project Goal

</div>

- A manufacturer-independent drone monitoring platform that supports lifesaving and disaster response operations.

---

<div align="center">
 
## Objectives

</div>

- A drone monitoring and management system deployable regardless of drone model or manufacturer
- A system that can be immediately deployed in the field without complex control procedures
- A system that does not rely on the performance capabilities of specific drone hardware
- A system that allows non-professional drone hobbyists to contribute effectively in emergency situations

---

<div align="center">

 ## Expected Impact

</div>

In life-saving and disaster response scenarios, before professional equipment<br>
or rescue teams arrive on site, any available drone—if operable by anyone—can be immediately deployed to:
- Assess victims
- Identify hazards
- Estimate damage

By securing this critical **golden time**, the system enables faster decision-making<br>
and more effective deployment of advanced rescue resources, ultimately leading to more sophisticated<br>
and impactful drone-assisted emergency response systems.

---
<div align="center">
 
## System Architecture

### Overall System Architecture

<img width="8192" height="6302" alt="AWS Upload Presigned URL-2026-02-20-144917" src="https://github.com/user-attachments/assets/687f81a5-f03c-4f28-acc3-338f4d78a00a" />

---

## Core System Flows
<details>
  <summary>Click to expand</summary>

|                                                                           Auth Logic                                                                            |                                          Control Data From Drone                                          |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
|  <img width="450" alt="Redis Token Connection Flow-2026-02-01-182619" src="https://github.com/user-attachments/assets/cf0e6a9e-eeae-4525-aaf1-198c98e61c90" />  | <img width="450" alt="Redis Token Connection Flow-2026-02-01-182708" src="https://github.com/user-attachments/assets/a344e0c5-b12a-45ab-951c-0cefcc87bf2b" />
 |
|                                                   **Redis-based authentication and connection control flow.**                                                   |                    **Processing of control and telemetry data after authentication.**                     |

|                                             Token Validation                                              |                                             Monitoring Server                                             |
|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
| <img src="https://github.com/user-attachments/assets/456dc993-64a0-4ac8-9138-0f5446aaad07" width="450"/>  |<img width="450" alt="Untitled diagram-2026-02-11-173920" src="https://github.com/user-attachments/assets/6eea1ba2-663d-4bf1-be1d-c729e3bda2f7" />|
|                          **Validation of Redis tokens for incoming drone data.**                          |                              **Periodic drone connection state monitoring.**                             |

| Back-End <-> Front-End |
|:---:|
| <img width="700" alt="AWS Upload Presigned URL-2026-02-13-144904" src="https://github.com/user-attachments/assets/97c1dbf0-3e24-4b4d-8669-65f076a0ffe5" /> |
| **Communication between Back-End Server and Front-End Dashboard** |

</details>

</div>
