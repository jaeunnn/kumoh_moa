# 클라우드컴퓨팅 프로젝트(과제)

## kumoh_moa

-   응원이 되는 명언 랜덤 표시
-   학사안내 부분 자동 크롤링 및 표시
-   행사안내 부분 자동 크롤링 및 표시

## 스택

-   Frontend: React 18 + TypeScript + Chakra UI
-   Backend: FastAPI + Python 3.11
-   DB: PostgreSQL 15

## 실행 및 소스코드

### 실행

-   http://20.196.104.117/

### github

-   https://github.com/jaeunnn/kumoh_moa.git

## 시스템 구축

-   git clone https://github.com/jaeunnn/kumoh_moa.git
-   docker-compose.yml 확인
-   init-data 폴더 확인 (01-schema.sql, 02-data.sql 포함)
-   docker compose up -d
-   물론 clone말고 docker-compose.yml, nginx.conf, init-data 폴더만으로도 사용가능
-   localhost:80으로 실행
