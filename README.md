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
[운영자]

│

│ ansible-playbook 실행

▼

[Ansible Controller]

│

│ SSH / Inventory

▼

[Target Servers (약 30대 추후에 더 늘어날수도 있음)]

│

│ 서버 정보 수집

▼

[Raw Data (JSON / TXT)]

│

│ Python 정규화 스크립트

▼

[Normalized Data]

│

│ Excel 작성

▼

[Excel Report]

## Workflow
1. Playbook 실행
2. Raw Data 수집
3. Python 파싱
4. Excel 생성

## Result
- 작업 시간 약 95% 단축
- 점검 데이터 표준화
- 운영 효율 향상

