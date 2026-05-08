# CAC-Error-Collection-Automation
## Overview
반복적인 Linux 서버 점검 업무를 자동화하기 위해
Ansible + Python 기반 자동화 시스템 구축

## Features
- CAC Error 자동 수집
- 데이터 파싱 및 정규화
- Excel 보고서 자동 생성

## Tech Stack
- Python
- Ansible
- Linux


## Architecture
```text
[ 운영자 ]
    │
    │ ansible-playbook 실행
    ▼
[ Ansible Controller ] ────────┐
    │                          │
    │ SSH / Inventory          │ 서버 정보 수집 (Raw Data)
    ▼                          │
[ Target Servers ] ────────────┘
    │
    ▼
[ Data Processing (Python) ]
    │
    │ 정규화 및 파싱
    ▼
[ Excel Report ]
'''
## Workflow
1. Playbook 실행
2. Raw Data 수집
3. Python 파싱
4. Excel 생성

## Result
기존 방식: 수동 서버 접속 및  확인 (대당 3~5분 소요)
개선 방식: Ansible 병렬 처리를 통한 일괄 수집 (100대 기준 약 5분 미만)
성과: 전체 점검 공수 95% 절감 및 휴먼 에러(데이터 누락) 0% 달성

