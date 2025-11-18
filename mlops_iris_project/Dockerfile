FROM python:3.9

WORKDIR /app

# 필요한 라이브러리 설치
COPY requirements.txt .
RUN pip install -r requirements.txt

# 애플리케이션 복사
COPY . .

# Flask 서버 실행
CMD ["python", "app.py"]
