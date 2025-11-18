import pandas as pd
import numpy as np
import time
import os

DATA_PATH = "data/generated_data.csv"

# 데이터 저장 폴더 생성
os.makedirs("data", exist_ok=True)

# 초기 CSV 파일이 없으면 생성
if not os.path.exists(DATA_PATH):
    df = pd.DataFrame(columns=["timestamp", "feature1", "feature2", "feature3", "target"])
    df.to_csv(DATA_PATH, index=False)

while True:
    # 새로운 데이터 생성
    new_data = {
        "timestamp": [pd.Timestamp.now()],
        "feature1": [np.random.rand()],
        "feature2": [np.random.rand()],
        "feature3": [np.random.rand()],
        "target": [np.random.randint(0, 2)]  # 0 또는 1
    }
    
    df_new = pd.DataFrame(new_data)
    df_new.to_csv(DATA_PATH, mode="a", header=False, index=False)

    print(f"새로운 데이터 추가됨: {new_data}")
    time.sleep(1)  # 1초마다 데이터 추가
