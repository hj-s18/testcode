# 베이스 이미지로 Python 3.9 슬림 사용
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 환경변수 파일 복사 (선택 사항)
COPY .env /app/

# Python 패키지 설치
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Flask 앱 파일 복사
COPY app.py /app/

# 추가 패키지 설치
RUN apt-get update && apt-get install -y \
    libmariadb-dev gcc default-mysql-client && \
    rm -rf /var/lib/apt/lists/*

# Gunicorn을 사용해 애플리케이션 실행
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]
