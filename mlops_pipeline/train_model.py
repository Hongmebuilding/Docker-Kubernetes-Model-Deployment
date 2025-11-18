import tensorflow as tf
import pandas as pd
import numpy as np
import os

DATA_FILE = "data/generated_data.csv"
MODEL_DIR = "model"
MODEL_PATH = "model/model.keras"

if not os.path.exists(DATA_FILE):
    print("❌ 데이터 파일이 없습니다. 데이터 생성 후 다시 실행하세요.")
    exit()

df = pd.read_csv(DATA_FILE)

# 🔥 숫자형 컬럼만 선택
df = df.select_dtypes(include=[np.number])
feature_count = df.shape[1] - 1  # 마지막 컬럼(y) 제외

def create_model(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(input_dim,)),
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(8, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

os.makedirs(MODEL_DIR, exist_ok=True)

if os.path.exists(MODEL_PATH):
    print("✅ 기존 모델 로드 중...")
    model = tf.keras.models.load_model(MODEL_PATH)
else:
    print("🚀 새 모델 생성 중...")
    model = create_model(feature_count)

def train():
    df = pd.read_csv(DATA_FILE).select_dtypes(include=[np.number])

    if df.shape[1] - 1 != feature_count:
        print(f"⚠️ 데이터셋 피처 개수({df.shape[1] - 1})가 모델({feature_count})과 다릅니다.")
        return

    X, y = df.iloc[:, :-1].values, df.iloc[:, -1].values
    model.fit(X, y, epochs=5, batch_size=8, verbose=1)
    model.save(MODEL_PATH)
    print(f"✅ 모델 저장 완료: {MODEL_PATH}")

if __name__ == "__main__":
    train()

