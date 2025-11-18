FROM python:3.9  
# 1️⃣ Python 3.9 환경의 기본 이미지 사용

# 2️⃣ 작업 디렉토리 설정
WORKDIR /app  

# 3️⃣ 필요한 패키지 설치
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt  

# 4️⃣ 모델 및 Flask API 코드 복사
COPY app.py /app/
COPY model /app/model/

# 5️⃣ 모델 폴더가 없으면 생성 (RUN 단계에서 추가 가능)
RUN mkdir -p /app/model  

# 6️⃣ Flask API 실행
CMD ["python", "/app/app.py"]
