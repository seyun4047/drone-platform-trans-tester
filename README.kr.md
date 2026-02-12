해당 문서는 gemini-2.5-flash 로 자동 번역되었습니다.<br>정확한 내용은 여기서 확인해주세요: [English Document](https://github.com/seyun4047/drone-platform-trans-tester/blob/main/README.md)

---

# 드론 데이터 전송 테스터

---
## 저장소 개요
이 저장소는 드론 연결, 텔레메트리, 이벤트 데이터를 시뮬레이션하여 서버의 API 동작을 검증하는 **드론 데이터 전송 테스터**를 제공합니다.
---

## 작동 방식

| 단계 | API 엔드포인트             | 설명 | 목적 | 비고      |
|------|--------------------------|-------------|---------|-----------|
| 1 | `/auth/connect`          | 드론 시리얼 및 장치 이름을 전송합니다. 승인되면 인증 토큰을 받습니다. | 드론과 서버 간 유효한 세션 설정 | |
| 2 | `/api/telemetry`| 토큰과 함께 일반 텔레메트리 데이터(각도, 위치)를 전송합니다. | 주기적인 드론 상태 정보 전송 | (event=0) |
| 3 | `/api/telemetry` | 이벤트 플래그 및 이벤트 상세 정보(예: 사람 감지됨)와 함께 텔레메트리를 전송합니다. | 중요한 감지 이벤트 보고 | (event=1) |
| 4 | `/auth/update`           | 현재 토큰을 전송하고 갱신된 토큰을 받습니다. | 유효한 인증된 세션 유지 | |
| 5 | `/auth/disconnect`       | 토큰과 함께 연결 해제 요청을 전송합니다. | 연결을 깔끔하게 종료 | |

---

## 설치
필요한 종속성을 설치하십시오:
```bash
pip install -r requirements.txt
```
---
## 사용법
애플리케이션을 실행하십시오:
```bash
python3 main.py
```
---

---

# PROJECT OVERVIEW
# Manufacturer-Independent Drone Platform

---
It is a **manufacturer-independent integrated drone monitoring platform.**

It is designed to manage various drones within a single environment,
enabling both **high-end professional drones and commercially available hobby camera drones**
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
| Docs | Platform Documents | [GitHub](https://github.com/seyun4047/drone-platform-docs)|

---

## Background

Although custom drones, commercial drones, and consumer drones share similar basic control mechanisms,
their operational methods and **command-and-control structures** in real-world environments vary significantly.

In practice, drones are often utilized as tools that depend heavily on:
- Specific equipment
- Highly trained personnel

Recently, many institutions and companies have attempted to build drone systems integrated with AI technologies.  
However, these systems have clear limitations. They typically rely on tuning specific drone models or operating a single type of custom-built drone, which results in strong dependency on specialized personnel and proprietary technologies.

Such dependency is particularly critical in **life-saving and disaster response operations**.

---
## Project Goal
- A manufacturer-independent drone monitoring platform that supports lifesaving and disaster response operations.

---
## Objectives

- A drone monitoring and management system deployable regardless of drone model or manufacturer
- A system that can be immediately deployed in the field without complex control procedures
- A system that does not rely on the performance capabilities of specific drone hardware
- A system that allows non-professional drone hobbyists to contribute effectively in emergency situations

---

## Expected Impact

In life-saving and disaster response scenarios, before professional equipment or rescue teams arrive on site,  
any available drone—if operable by anyone—can be immediately deployed to:
- Assess victims
- Identify hazards
- Estimate damage

By securing this critical **golden time**, the system enables faster decision-making and more effective deployment of advanced rescue resources, ultimately leading to more sophisticated and impactful drone-assisted emergency response systems.

---

## System Architecture

### Overall System Architecture
<img height="900" alt="Untitled diagram-2026-02-11-182634" src="https://github.com/user-attachments/assets/8842dd09-471e-4a75-8804-674f9cff675a" />


---

## Core System Flows

|                                                                           Auth Logic                                                                            |                                          Control Data From Drone                                          |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
|  <img width="450" alt="Redis Token Connection Flow-2026-02-01-182619" src="https://github.com/user-attachments/assets/cf0e6a9e-eeae-4525-aaf1-198c98e61c90" />  | <img src="https://github.com/user-attachments/assets/669647c6-ee30-4bfb-baea-d02e306070ea" width="450"/>  |
|                                                   **Redis-based authentication and connection control flow.**                                                   |                    **Processing of control and telemetry data after authentication.**                     |

|                                             Token Validation                                              |                                             Monitoring Server                                             |
|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
| <img src="https://github.com/user-attachments/assets/456dc993-64a0-4ac8-9138-0f5446aaad07" width="450"/>  |<img width="450" alt="Untitled diagram-2026-02-11-173920" src="https://github.com/user-attachments/assets/6eea1ba2-663d-4bf1-be1d-c729e3bda2f7" />|
|                          **Validation of Redis tokens for incoming drone data.**                          |                              **Periodic drone connection state monitoring.**                             |

---
