해당 문서는 gemini-2.5-flash 로 자동 번역되었습니다.<br>정확한 내용은 여기서 확인해주세요: [English Document](https://github.com/seyun4047/drone-platform-trans-tester/blob/main/README.md)

---

# 드론 데이터 전송 테스터

---
## 저장소 개요
이 저장소는 드론 연결, 텔레메트리 및 이벤트 데이터를 시뮬레이션하여 서버의 API 동작을 검증하는 **드론 데이터 전송 테스터**를 제공합니다.
---

## 작동 방식

| Step | API Endpoint             | Description | Purpose | etc.      |
|------|--------------------------|-------------|---------|-----------|
| 1 | `/auth/connect`          | 드론 시리얼 및 장치 이름을 전송합니다. 승인되면 인증 토큰을 받습니다. | 드론과 서버 간 유효한 세션 설정 | |
| 2 | `/api/telemetry`| 토큰과 함께 일반 텔레메트리 데이터(각도, 위치)를 전송합니다. | 주기적인 드론 상태 정보 전송 | (event=0) |
| 3 | `/api/telemetry` | 이벤트 플래그 및 이벤트 상세 정보(예: 사람 감지됨)와 함께 텔레메트리를 전송합니다. | 중요한 감지 이벤트 보고 | (event=1) |
| 4 | `/auth/update`           | 현재 토큰을 전송하고 갱신된 토큰을 받습니다. | 유효한 인증 세션 유지 | |
| 5 | `/auth/disconnect`       | 토큰과 함께 연결 해제 요청을 전송합니다. | 연결을 깔끔하게 닫기 | |

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
python3 tester.py
```
---

---

<div align="center">
 
# 프로젝트 개요

  <a href="https://youtu.be/7IdtRp_fe1U" target="_blank">
    <img width="900" src="https://github.com/user-attachments/assets/7bc575a8-27f7-4e64-b04e-1e33d4a7848e" alt="MAIN_DRONE_LOGO"/>
  </a>
   <p><strong>소개 영상 클릭 및 시청</strong></p> 

---


이것은 **제조사 독립적인 드론 모니터링 플랫폼**입니다.

단일 환경에서 다양한 드론을 관리하도록 설계되어, **고급 전문가용 드론<br>부터 시판되는 취미용 카메라 드론까지** 모두 인명 구조 및 재난 대응에 활용될 수 있습니다.



---

## 프로젝트 구조

이 플랫폼은 여러 독립적인 저장소로 구성됩니다:

| 구성 요소 | 설명                                       | 저장소                                                              |
|---------|---------------------------------------------------|-------------------------------------------------------------------------|
| 서버 | 핵심 드론 플랫폼 서버 (API, 인증, 텔레메트리) | [GitHub](https://github.com/seyun4047/drone-platform-server)            |
| 모니터링 서버 | 실시간 드론 상태 확인 모니터링 서비스   | [GitHub](https://github.com/seyun4047/drone-platform-monitoring-server) |
| 드론 데이터 테스터 | 드론 텔레메트리 및 데이터 시뮬레이션 테스트 클라이언트 | [GitHub](https://github.com/seyun4047/drone-platform-trans-tester)       |
| 드론 클라이언트 | 드론 데이터 수집, 전송 및 분석 | [GitHub](https://github.com/seyun4047/drone-platform-client)            |
| 대시보드 | 드론 플랫폼 프론트엔드 | [GitHub](https://github.com/seyun4047/drone-platform-dashboard)            |
| 문서 | 플랫폼 문서, API | [GitHub](https://github.com/seyun4047/drone-platform-docs)|



---



## 배경

</div>

맞춤형 드론, 상업용 드론, 소비자용 드론은 기본적인 제어 메커니즘을 공유하지만,<br>실제 환경에서의 운용 방식과 **명령 및 제어 구조**는 크게 다릅니다.

실제로 드론은 다음과 같은 요소에 크게 의존하는 도구로 활용됩니다:
- 특정 장비
- 고도로 훈련된 인력

최근 많은 기관과 기업들이 AI 기술과 통합된 드론 시스템을 구축하려 시도했습니다. <br>그러나 이러한 시스템에는 명확한 한계가 있습니다.<br>일반적으로 특정 드론 모델을 튜닝하거나 단일 유형의 맞춤 제작 드론을 운용하는 방식에 의존하여,<br>전문 인력과 독점 기술에 대한 의존성이 강합니다.

이러한 의존성은 특히 **인명 구조 및 재난 대응 작전**에서 매우 중요합니다.

---

<div align="center">

 ## 프로젝트 목표

</div>

- 인명 구조 및 재난 대응 작전을 지원하는 제조사 독립적인 드론 모니터링 플랫폼.

---

<div align="center">
 
## 목표

</div>

- 드론 모델이나 제조사에 관계없이 배포 가능한 드론 모니터링 및 관리 시스템
- 복잡한 제어 절차 없이 현장에 즉시 배포할 수 있는 시스템
- 특정 드론 하드웨어의 성능 기능에 의존하지 않는 시스템
- 비전문 드론 취미 사용자도 비상 상황에서 효과적으로 기여할 수 있도록 하는 시스템

---

<div align="center">

 ## 예상되는 영향

</div>

인명 구조 및 재난 대응 시나리오에서, 전문 장비<br>또는 구조팀이 현장에 도착하기 전에, 누구든 조작할 수 있는 모든 가용한 드론은 즉시 다음을 위해 배포될 수 있습니다:
- 희생자 파악
- 위험 요소 식별
- 피해 규모 추정

이 중요한 **골든 타임**을 확보함으로써, 시스템은 더 빠른 의사 결정<br>과 고급 구조 자원의 더 효과적인 배포를 가능하게 하여, 궁극적으로 더 정교하고<br>영향력 있는 드론 지원 비상 대응 시스템으로 이어집니다.

---
<div align="center">
 
## 시스템 아키텍처

### 전체 시스템 아키텍처

<img width="8192" height="6302" alt="AWS Upload Presigned URL-2026-02-20-144917" src="https://github.com/user-attachments/assets/687f81a5-f03c-4f28-acc3-338f4d78a00a" />

---

## 핵심 시스템 흐름
<details>
  <summary>클릭하여 확장</summary>

|                                                                           인증 로직                                                                            |                                          드론으로부터의 제어 데이터                                          |                                           드론 토큰 유효성 검사                                              |                                             모니터링 서버                                             |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
|  <img width="450" alt="Auth logic flow" src="https://github.com/user-attachments/assets/cf0e6a9e-eeae-4525-aaf1-198c98e61c90" />  |<img width="450" alt="Control data flow" src="https://github.com/user-attachments/assets/f8c4acf7-0cbe-4ca3-b7fe-6aee4f3e854c" /> | <img alr="Token validation flow" src="https://github.com/user-attachments/assets/456dc993-64a0-4ac8-9138-0f5446aaad07" width="450"/>  |<img width="450" alt="Monitoring server flow" src="https://github.com/user-attachments/assets/6eea1ba2-663d-4bf1-be1d-c729e3bda2f7" />|
|                                                   **Redis 기반 인증 및 연결 제어 흐름.**                                                   |                    **인증 후 제어 및 텔레메트리 데이터 처리.**                     |                         **수신 드론 데이터에 대한 Redis 토큰 유효성 검사.**                          |                              **주기적인 드론 연결 상태 모니터링.**                             |

| 백엔드 <-> 프론트엔드 |
|:---:|
| <img width="700" alt="AWS Upload Presigned URL-2026-02-13-144904" src="https://github.com/user-attachments/assets/97c1dbf0-3e24-4b4d-8669-65f076a0ffe5" /> |
| **백엔드 서버와 프론트엔드 대시보드 간 통신** |

</details>

</div>