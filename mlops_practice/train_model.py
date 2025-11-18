# train_model.py - AI 모델 학습 및 저장 (Keras 사용)
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
import os

# 1️⃣ 모델 저장 경로 설정
MODEL_PATH = "model/model.keras"
os.makedirs("model", exist_ok=True)

# 2️⃣ 간단한 신경망 모델 생성
model = Sequential([
    Dense(10, activation='relu', input_shape=(10,)),  # 입력층
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')  # 출력층
])

# 3️⃣ 모델 컴파일 및 학습 (더미 데이터 사용)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

X_dummy = np.random.rand(100, 10)  # 100개의 입력 데이터 (10차원)
y_dummy = np.random.randint(0, 2, 100)  # 이진 분류

model.fit(X_dummy, y_dummy, epochs=5, batch_size=8, verbose=1)

# 4️⃣ 모델 저장
model.save(MODEL_PATH)
print(f"✅ 모델이 성공적으로 저장되었습니다: {MODEL_PATH}")
