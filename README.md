# Manufacturer-Independent Drone Platform

The project aims to be a **manufacturer-independent drone platform**, connecting various drone devices with standardized interfaces and performing **Redis-based authentication and status management**.

---

## Project Structure

This platform consists of multiple independent repositories:

| Component | Description                                       | Repository                                                              |
|---------|---------------------------------------------------|-------------------------------------------------------------------------|
| Server | Core drone platform server (API, Auth, Telemetry) | [GitHub](https://github.com/seyun4047/drone-platform-server)            |
| Monitoring Server | Real-time Drone health check monitoring service   | [GitHub](https://github.com/seyun4047/drone-platform-monitoring-server) |
| Drone Data Tester | Test client for drone telemetry & data simulation | [GitHub](https://github.com/seyun4047/drone-platform-server)       |
| Drone Client | Drone Data Collection, Transmission & Analysis | -                                                                       |

---

## Overview

This project focuses on building a universal drone control and monitoring platform that can operate independently of drone manufacturers and hardware-specific constraints.

---

## Background

Although custom drones, commercial drones, and consumer drones share similar basic control mechanisms,  
their operational methods and **command and control structures** in real-world environments vary significantly.

In practice, drones are often utilized as tools that depend heavily on:
- Specific equipment
- Highly trained personnel

Recently, many institutions and companies have attempted to build drone systems integrated with AI technologies.  
However, these systems have clear limitations. They typically rely on tuning specific drone models or operating a single type of custom-built drone, which results in strong dependency on specialized personnel and proprietary technologies.

Such dependency is particularly critical in **life-saving and disaster response operations**.

---

## Project Goal

Based on this problem, the goal of this project is defined as follows:

> **A universal drone control and monitoring platform that enables immediate deployment of any camera-equipped drone—including consumer drones—for life-saving and disaster response missions.**

---
## Objectives

- A drone control and monitoring system deployable regardless of drone model or manufacturer
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

## Architecture

### Overall System Architecture
<img width="5823" height="3493" alt="Drone Redis Token Flow-2026-01-27-183514" src="https://github.com/user-attachments/assets/2693c67c-8110-4f79-86f5-22768663c5ae" />



---

### 1. Auth Logic

This component defines the authentication and connection control flow using Redis-based token management.
<img width="3310" height="8192" alt="Redis Token Connection Flow-2026-02-01-182619" src="https://github.com/user-attachments/assets/cf0e6a9e-eeae-4525-aaf1-198c98e61c90" />

---

### 2. Control Data From Drone

This flow describes how control and telemetry data are received and processed from drones after authentication.
<img width="2602" height="6167" alt="Redis Token Connection Flow-2026-02-01-182817" src="https://github.com/user-attachments/assets/669647c6-ee30-4bfb-baea-d02e306070ea" />

---

### 3. Token Validation for Data

This process validates Redis tokens for incoming drone data to ensure integrity and authenticity.
<img width="3354" height="5544" alt="Redis Token Connection Flow-2026-02-01-182531" src="https://github.com/user-attachments/assets/456dc993-64a0-4ac8-9138-0f5446aaad07" />

---

### 4. Drone State Monitoring Server

The monitoring server periodically checks drone connection states and maintains system consistency.
<img width="1823" height="3419" alt="Redis Token Connection Flow-2026-02-01-182910" src="https://github.com/user-attachments/assets/592adb6b-9066-47ac-8f9d-d5117492a6af" />
 
